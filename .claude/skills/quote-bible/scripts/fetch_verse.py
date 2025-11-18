#!/usr/bin/env python3
"""Fetch Bible verses from BibleHub and/or eBible corpus with caching and language filtering.

This module serves dual purposes:

1. **CLI Script**: Run directly to fetch verses with optional language filtering
   ```bash
   python fetch_verse.py MAT-005-003                    # All languages
   python fetch_verse.py "GEN 1:1" --lang eng           # English only
   python fetch_verse.py JHN.3.16 --lang eng,spa,fra    # Multiple languages
   python fetch_verse.py ROM-8-28 -l grc,heb            # Original languages
   ```

2. **Library/MCP Import**: Import and use programmatically
   ```python
   from fetch_verse import fetch_verse, filter_by_languages, VerseFetchError

   # Fetch verse
   translations = fetch_verse("MAT", 5, 3)
   
   # Filter by language
   eng_only = filter_by_languages(translations, ["eng"])
   ```

The module provides a clean API for fetching Bible verses with automatic caching,
language filtering, sparse checkout handling, and comprehensive error handling.

**Sparse Checkout Support**: Automatically adds chapter directories to Git sparse checkout
(commentary/{BOOK}/{chapter:03d}) if the data directory is using sparse checkout and the
chapter isn't already available.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Ensure imports work from both CLI and library usage
sys.path.insert(0, str(Path(__file__).parent))

# Add project root to path for src imports
project_root = Path(__file__).resolve().parent.parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from biblehub_fetcher import VerseFetchError, fetch_verses_from_biblehub
from book_codes import parse_reference

from src.ingest_data.ebible.ebible_fetcher import fetch_verses_from_ebible

# Public API for library/MCP usage
__all__ = ['fetch_verse', 'filter_by_languages', 'ensure_sparse_checkout_chapter', 'VerseFetchError']


def ensure_sparse_checkout_chapter(book: str, chapter: int, data_dir: Optional[Path] = None) -> bool:
    """
    Ensure a book chapter's commentary directory is available in sparse checkout.
    
    If the data directory is a git repo with sparse checkout enabled and the chapter's
    commentary directory doesn't exist, this will add it to the sparse checkout.
    
    Per STANDARDIZATION.md, the structure is: /commentary/{BOOK}/{chapter:03d}/{verse:03d}/
    
    Args:
        book: USFM book code (e.g., "MAT")
        chapter: Chapter number
        data_dir: Data directory path (default: $DATA_DIR or .data)
    
    Returns:
        True if chapter was added to sparse checkout or already available, False otherwise
    """
    if data_dir is None:
        data_dir = Path(os.environ.get('DATA_DIR', '.data'))
    
    data_dir = Path(data_dir)
    
    # Check if data directory exists and is a git repo
    if not data_dir.exists() or not (data_dir / '.git').exists():
        return False
    
    # Check chapter directory (per STANDARDIZATION.md: commentary/{BOOK}/{chapter:03d}/)
    chapter_path = data_dir / 'commentary' / book / f'{chapter:03d}'
    
    # If chapter directory already exists, nothing to do
    if chapter_path.exists():
        return True
    
    # Check if sparse checkout is enabled
    try:
        result = subprocess.run(
            ['git', 'config', '--get', 'core.sparseCheckout'],
            cwd=str(data_dir),
            capture_output=True,
            text=True,
            timeout=5
        )
        
        # If sparse checkout is not enabled or command failed, nothing to do
        if result.returncode != 0 or result.stdout.strip() != 'true':
            return False
        
        # Sparse checkout is enabled and chapter doesn't exist - add it
        checkout_path = f'commentary/{book}/{chapter:03d}'
        print(f"Adding {checkout_path} to sparse checkout...", file=sys.stderr)
        
        add_result = subprocess.run(
            ['git', 'sparse-checkout', 'add', checkout_path],
            cwd=str(data_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if add_result.returncode == 0:
            print(f"✓ {checkout_path} added to sparse checkout", file=sys.stderr)
            return chapter_path.exists()
        else:
            print(f"Warning: Failed to add {checkout_path} to sparse checkout: {add_result.stderr}", file=sys.stderr)
            return False
            
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        # Git not available or other error - silently continue
        print(f"Warning: Could not check sparse checkout status: {e}", file=sys.stderr)
        return False


def fetch_verse(book: str, chapter: int, verse: int, 
                suffix: str = "biblehub.json",
                cache_root: str = "./cache",
                use_cache: bool = True) -> Dict[str, str]:
    """
    Fetch verse from BibleHub with caching.
    
    Args:
        book: USFM book code (e.g., "MAT")
        chapter: Chapter number
        verse: Verse number
        suffix: File suffix for cache (default: "biblehub.json")
        cache_root: Root cache directory (default: "./cache")
        use_cache: Whether to use cache (default: True)
    
    Returns:
        Dictionary mapping version codes to verse text
        
    Raises:
        VerseFetchError: If fetching fails
    """
    return fetch_verses_from_biblehub(book, chapter, verse, use_cache=use_cache)



def filter_by_languages(translations: Dict[str, str], languages: Optional[List[str]]) -> Dict[str, str]:
    """
    Filter translations by language codes.
    
    Args:
        translations: Dictionary of translation_id -> text
        languages: List of ISO-639-3 language codes to include (None = all languages)
    
    Returns:
        Filtered dictionary containing only requested languages
    
    Example:
        >>> translations = {"eng-NIV": "...", "spa-RV": "...", "fra-LSG": "..."}
        >>> filter_by_languages(translations, ["eng", "spa"])
        {"eng-NIV": "...", "spa-RV": "..."}
    """
    if not languages:
        return translations
    
    # Normalize language codes to lowercase
    languages_lower = [lang.lower() for lang in languages]
    
    filtered = {}
    for trans_id, text in translations.items():
        # Extract language code (first part before hyphen)
        lang_code = trans_id.split('-')[0].lower()
        if lang_code in languages_lower:
            filtered[trans_id] = text
    
    return filtered


def main():
    """CLI entry point for fetching Bible verses."""
    parser = argparse.ArgumentParser(
        description="Fetch Bible verses from BibleHub and eBible corpus with language filtering",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python fetch_verse.py MAT-005-003                    # All languages (1000+ translations)
  python fetch_verse.py "GEN 1:1" --lang eng           # English only
  python fetch_verse.py JHN.3.16 --lang eng,spa,fra    # English, Spanish, French
  python fetch_verse.py ROM-8-28 -l grc,heb            # Original languages only

Format: BOOK-CCC-VVV (zero-padded) or "BOOK C:V" (convenience)
Book codes are USFM 3.0 codes (e.g., GEN, EXO, MAT, JHN, REV)
Language codes are ISO-639-3 (e.g., eng, spa, fra, grc, heb)
        """
    )
    
    parser.add_argument(
        'verse_reference',
        help='Verse reference (e.g., MAT-005-003, "GEN 1:1", JHN.3.16)'
    )
    
    parser.add_argument(
        '--lang', '-l',
        dest='languages',
        help='Comma-separated list of ISO-639-3 language codes (e.g., eng,spa,fra)',
        default=None
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Fetch all available translations (overrides --lang)'
    )
    
    args = parser.parse_args()

    # Parse the verse reference
    try:
        book, chapter, verse = parse_reference(args.verse_reference)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse language codes if provided
    languages = None
    if args.languages and not args.all:
        languages = [lang.strip().lower() for lang in args.languages.split(',')]
        print(f"Looking up {book}.{chapter}.{verse} (languages: {', '.join(languages)})...", file=sys.stderr)
    else:
        print(f"Looking up {book}.{chapter}.{verse} (all languages)...", file=sys.stderr)

    # Ensure chapter is available in sparse checkout if needed
    ensure_sparse_checkout_chapter(book, chapter)

    # Collect translations from all fetchers
    translations = {}
    fetchers = [fetch_verses_from_biblehub, fetch_verses_from_ebible]
    
    for fetcher in fetchers:
        try:
            result = fetcher(book, chapter, verse)
            if result:
                # Handle structured data (like eBible) vs flat data (like BibleHub)
                if 'translations' in result and isinstance(result['translations'], dict):
                    # Structured format: extract translations field
                    translations.update(result['translations'])
                elif isinstance(result, dict):
                    # Flat format: all items are translations
                    translations.update(result)
        except Exception as e:
            print(f"Warning: {fetcher.__name__} failed: {e}", file=sys.stderr)
    
    # Filter by languages if requested
    if languages:
        translations = filter_by_languages(translations, languages)
    
    # Print results
    print(json.dumps(translations, indent=2, ensure_ascii=False))
    
    # Print summary to stderr
    print(f"\nFound {len(translations)} translation(s)", file=sys.stderr)


if __name__ == '__main__':
    main()
