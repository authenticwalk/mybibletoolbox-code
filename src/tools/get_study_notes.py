#!/usr/bin/env python3
"""Fetch comprehensive study notes for a Bible verse.

This tool aggregates data from multiple sources:
- Commentary YAML files for the verse
- Strong's lexicon data for words in the verse
- Translations with optional language filtering

Usage:
    python get_study_notes.py 1PE-001-001                           # All tools
    python get_study_notes.py "MAT 5:3" --include "macula|tbta"     # Only matching tools
    python get_study_notes.py JHN.3.16 --exclude "ebible"           # Exclude matching
    python get_study_notes.py ROM-8-28 --lang eng,spa               # Filter translations
"""

import argparse
import json
import os
import re
import sys
import yaml
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Add quote-bible scripts to path for book_codes
quote_bible_scripts = project_root / '.claude' / 'skills' / 'quote-bible' / 'scripts'
if str(quote_bible_scripts) not in sys.path:
    sys.path.insert(0, str(quote_bible_scripts))

from book_codes import parse_reference

from src.util.yaml_merger import merge_yaml_data, merge_yaml_files
from src.tools.fetch_verse import ensure_sparse_checkout_chapter, filter_by_languages

# Public API
__all__ = [
    'get_study_notes',
    'get_verse_commentary_files',
    'get_strongs_files',
    'extract_strongs_from_macula',
    'StudyNotesError'
]


class StudyNotesError(Exception):
    """Error fetching study notes."""
    pass


def get_data_dir() -> Path:
    """Get the data directory path."""
    return Path(os.environ.get('DATA_DIR', '.data'))


def get_verse_commentary_files(
    book: str, 
    chapter: int, 
    verse: int,
    include_pattern: Optional[str] = None,
    exclude_pattern: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> List[Path]:
    """
    Get list of commentary YAML files for a verse, filtered by tool patterns.
    
    Args:
        book: USFM book code (e.g., "1PE")
        chapter: Chapter number
        verse: Verse number
        include_pattern: Regex pattern to include tools (default: all)
        exclude_pattern: Regex pattern to exclude tools (default: none)
        data_dir: Data directory path (default: $DATA_DIR or .data)
    
    Returns:
        List of paths to matching YAML files
    """
    if data_dir is None:
        data_dir = get_data_dir()
    
    # Path per STANDARDIZATION.md: commentary/{BOOK}/{chapter:03d}/{verse:03d}/
    verse_dir = data_dir / 'commentary' / book / f'{chapter:03d}' / f'{verse:03d}'
    
    if not verse_dir.exists():
        return []
    
    # Get all YAML files
    yaml_files = sorted(verse_dir.glob('*.yaml'))
    
    # Filter by patterns
    filtered = []
    include_re = re.compile(include_pattern) if include_pattern else None
    exclude_re = re.compile(exclude_pattern) if exclude_pattern else None
    
    for f in yaml_files:
        # Extract tool name from filename: {BOOK}-{chapter:03d}-{verse:03d}-{tool}.yaml
        tool_name = f.stem.split('-', 3)[-1] if '-' in f.stem else f.stem
        
        # Apply filters
        if include_re and not include_re.search(tool_name):
            continue
        if exclude_re and exclude_re.search(tool_name):
            continue
        
        filtered.append(f)
    
    return filtered


def get_strongs_files(
    strongs_id: str,
    include_pattern: Optional[str] = None,
    exclude_pattern: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> List[Path]:
    """
    Get list of Strong's lexicon YAML files for a Strong's number.
    
    Per STANDARDIZATION.md: strongs/{G|H}{number:04d}/{G|H}{number:04d}-{tool}.yaml
    
    Args:
        strongs_id: Strong's number (e.g., "G0652" or "652" for Greek)
        include_pattern: Regex pattern to include tools (default: all)
        exclude_pattern: Regex pattern to exclude tools (default: none)
        data_dir: Data directory path
    
    Returns:
        List of paths to matching YAML files
    """
    if data_dir is None:
        data_dir = get_data_dir()
    
    # Normalize strongs_id to standard format
    strongs_id = normalize_strongs_id(strongs_id)
    
    strongs_dir = data_dir / 'strongs' / strongs_id
    
    if not strongs_dir.exists():
        return []
    
    yaml_files = sorted(strongs_dir.glob('*.yaml'))
    
    # Filter by patterns
    filtered = []
    include_re = re.compile(include_pattern) if include_pattern else None
    exclude_re = re.compile(exclude_pattern) if exclude_pattern else None
    
    for f in yaml_files:
        # Extract tool name from filename
        tool_name = f.stem.split('-', 1)[-1] if '-' in f.stem else f.stem
        
        if include_re and not include_re.search(tool_name):
            continue
        if exclude_re and exclude_re.search(tool_name):
            continue
        
        filtered.append(f)
    
    return filtered


def normalize_strongs_id(strongs_id: str, is_nt: bool = True) -> str:
    """
    Normalize a Strong's number to standard format.
    
    Args:
        strongs_id: Strong's number (e.g., "652", "G652", "G0652")
        is_nt: Whether this is New Testament (Greek) - used if no prefix
    
    Returns:
        Normalized ID (e.g., "G0652")
    """
    strongs_id = str(strongs_id).strip()
    
    # Check if already has prefix
    if strongs_id.startswith('G') or strongs_id.startswith('H'):
        prefix = strongs_id[0]
        number = strongs_id[1:]
    else:
        prefix = 'G' if is_nt else 'H'
        number = strongs_id
    
    # Pad to 4 digits
    try:
        num = int(number)
        return f'{prefix}{num:04d}'
    except ValueError:
        return strongs_id  # Return as-is if can't parse


def extract_strongs_from_macula(macula_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract Strong's numbers and word info from macula data.
    
    Args:
        macula_data: Parsed macula YAML data
    
    Returns:
        List of word info dicts with strongs_id, text, lemma, gloss
    """
    words = macula_data.get('words', [])
    strongs_words = []
    
    for word in words:
        lexical = word.get('lexical', {})
        strong = lexical.get('strong')
        
        if strong:
            word_info = {
                'strongs_id': normalize_strongs_id(str(strong)),
                'text': word.get('text', ''),
                'lemma': word.get('lemma', ''),
                'gloss': word.get('translation', {}).get('gloss', ''),
                'position': word.get('position'),
                'morphology': word.get('morphology', {}),
            }
            strongs_words.append(word_info)
    
    return strongs_words


def load_strongs_data(
    strongs_ids: List[str],
    include_pattern: Optional[str] = None,
    exclude_pattern: Optional[str] = None,
    data_dir: Optional[Path] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Load Strong's lexicon data for multiple Strong's numbers.
    
    Args:
        strongs_ids: List of Strong's numbers
        include_pattern: Regex pattern to include tools
        exclude_pattern: Regex pattern to exclude tools
        data_dir: Data directory path
    
    Returns:
        Dict mapping strongs_id to merged tool data
    """
    if data_dir is None:
        data_dir = get_data_dir()
    
    result = {}
    seen_ids: Set[str] = set()
    
    for strongs_id in strongs_ids:
        normalized_id = normalize_strongs_id(strongs_id)
        
        # Skip duplicates
        if normalized_id in seen_ids:
            continue
        seen_ids.add(normalized_id)
        
        files = get_strongs_files(
            normalized_id,
            include_pattern=include_pattern,
            exclude_pattern=exclude_pattern,
            data_dir=data_dir
        )
        
        if files:
            try:
                merged = merge_yaml_files(files)
                result[normalized_id] = merged
            except Exception as e:
                print(f"Warning: Could not load strongs {normalized_id}: {e}", file=sys.stderr)
    
    return result


def get_study_notes(
    book: str,
    chapter: int,
    verse: int,
    include_tools: Optional[str] = None,
    exclude_tools: Optional[str] = None,
    languages: Optional[List[str]] = None,
    data_dir: Optional[Path] = None
) -> Dict[str, Any]:
    """
    Fetch comprehensive study notes for a Bible verse.
    
    Args:
        book: USFM book code (e.g., "1PE")
        chapter: Chapter number
        verse: Verse number
        include_tools: Regex pattern to include specific tools
        exclude_tools: Regex pattern to exclude specific tools
        languages: List of ISO-639-3 language codes to filter translations
        data_dir: Data directory path
    
    Returns:
        Dict with:
        - verse: Verse reference
        - commentary: Merged commentary data from all tools
        - strongs: Dict of Strong's lexicon data for words in verse
        - words: List of words from macula with Strong's references
        - tools_loaded: List of tools that were loaded
    """
    if data_dir is None:
        data_dir = get_data_dir()
    
    # Ensure sparse checkout includes this chapter
    ensure_sparse_checkout_chapter(book, chapter, data_dir)
    
    result = {
        'verse': f'{book} {chapter}:{verse}',
        'commentary': {},
        'strongs': {},
        'words': [],
        'tools_loaded': []
    }
    
    # Get commentary files
    commentary_files = get_verse_commentary_files(
        book, chapter, verse,
        include_pattern=include_tools,
        exclude_pattern=exclude_tools,
        data_dir=data_dir
    )
    
    if not commentary_files:
        return result
    
    # Track loaded tools
    tools = []
    macula_data = None
    
    # Load and merge commentary files
    for f in commentary_files:
        tool_name = f.stem.split('-', 3)[-1] if '-' in f.stem else f.stem
        tools.append(tool_name)
        
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                data = yaml.safe_load(fp)
            
            if data:
                # Capture macula data for strongs extraction
                if 'macula' in tool_name.lower():
                    macula_data = data
                
                result['commentary'] = merge_yaml_data(result['commentary'], data)
        except Exception as e:
            print(f"Warning: Could not load {f}: {e}", file=sys.stderr)
    
    result['tools_loaded'] = tools
    
    # Filter translations if languages specified
    if languages and 'translations' in result['commentary']:
        result['commentary']['translations'] = filter_by_languages(
            result['commentary']['translations'], 
            languages
        )
    
    # Extract Strong's numbers from macula and load strongs data
    if macula_data:
        words = extract_strongs_from_macula(macula_data)
        result['words'] = words
        
        # Get unique strongs IDs
        strongs_ids = list({w['strongs_id'] for w in words if w.get('strongs_id')})
        
        if strongs_ids:
            result['strongs'] = load_strongs_data(
                strongs_ids,
                include_pattern=include_tools,
                exclude_pattern=exclude_tools,
                data_dir=data_dir
            )
    
    return result


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch comprehensive study notes for a Bible verse",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python get_study_notes.py 1PE-001-001                           # All tools
  python get_study_notes.py "MAT 5:3" --include "macula|tbta"     # Only matching tools
  python get_study_notes.py JHN.3.16 --exclude "ebible"           # Exclude matching
  python get_study_notes.py ROM-8-28 --lang eng,spa               # Filter translations

Format: BOOK-CCC-VVV (zero-padded) or "BOOK C:V" (convenience)
Book codes are USFM 3.0 (e.g., GEN, MAT, 1PE, REV)
        """
    )
    
    parser.add_argument(
        'verse_reference',
        help='Verse reference (e.g., 1PE-001-001, "MAT 5:3", JHN.3.16)'
    )
    
    parser.add_argument(
        '--include', '-i',
        dest='include_tools',
        help='Regex pattern to include specific tools (e.g., "macula|tbta")',
        default=None
    )
    
    parser.add_argument(
        '--exclude', '-e',
        dest='exclude_tools',
        help='Regex pattern to exclude specific tools (e.g., "ebible")',
        default=None
    )
    
    parser.add_argument(
        '--lang', '-l',
        dest='languages',
        help='Comma-separated list of ISO-639-3 language codes (e.g., eng,spa,fra)',
        default=None
    )
    
    parser.add_argument(
        '--data-dir', '-d',
        dest='data_dir',
        help='Data directory path (default: $DATA_DIR or .data)',
        default=None
    )
    
    parser.add_argument(
        '--compact',
        action='store_true',
        help='Output compact JSON (no indentation)'
    )
    
    args = parser.parse_args()
    
    # Parse verse reference
    try:
        book, chapter, verse = parse_reference(args.verse_reference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Parse languages
    languages = None
    if args.languages:
        languages = [lang.strip().lower() for lang in args.languages.split(',')]
    
    # Parse data dir
    data_dir = Path(args.data_dir) if args.data_dir else None
    
    print(f"Fetching study notes for {book} {chapter}:{verse}...", file=sys.stderr)
    
    # Get study notes
    try:
        notes = get_study_notes(
            book, chapter, verse,
            include_tools=args.include_tools,
            exclude_tools=args.exclude_tools,
            languages=languages,
            data_dir=data_dir
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Output
    indent = None if args.compact else 2
    print(json.dumps(notes, indent=indent, ensure_ascii=False))
    
    # Summary
    print(f"\nLoaded {len(notes['tools_loaded'])} tool(s): {', '.join(notes['tools_loaded'])}", file=sys.stderr)
    print(f"Found {len(notes['words'])} word(s) with Strong's references", file=sys.stderr)
    print(f"Loaded {len(notes['strongs'])} Strong's entries", file=sys.stderr)


if __name__ == '__main__':
    main()

