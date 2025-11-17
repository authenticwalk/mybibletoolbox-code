#!/usr/bin/env python3
"""
Fetch translations for number-systems question sheets.

This script:
1. Reads *_questions.yaml files
2. Fetches translations from .data/commentary/ (eBible) OR BibleHub
3. Populates the translations field with actual text
4. Focuses on: Fijian (fij), Hawaiian (haw), Samoan (smo), Slovenian (slv), Tok Pisin (tpi)
"""

import yaml
import sys
from pathlib import Path
import json

# Find project root (go up from experiments/)
PROJECT_ROOT = Path(__file__).resolve().parents[4]  # experiments -> features -> tbta -> bible-study-tools -> root

# Add quote-bible scripts to path
QUOTE_BIBLE_DIR = PROJECT_ROOT / ".claude/skills/quote-bible/scripts"
sys.path.insert(0, str(QUOTE_BIBLE_DIR))

try:
    from biblehub_fetcher import fetch_verses_from_biblehub, VerseFetchError
    BIBLEHUB_AVAILABLE = True
except ImportError:
    print("⚠️  BibleHub fetcher not available. Will only use cached data.")
    BIBLEHUB_AVAILABLE = False

# Data directory - try multiple possible locations
DATA_DIRS = [
    PROJECT_ROOT / ".data",
    PROJECT_ROOT.parent / ".data",  # Parent of mybibletoolbox-code
    Path("/Users/chrispriebe/projects/mybibletoolbox/.data"),
]

DATA_DIR = None
for data_path in DATA_DIRS:
    if data_path.exists() and (data_path / "commentary").exists():
        DATA_DIR = data_path
        break

if DATA_DIR is None:
    print("⚠️  No .data/commentary directory found. Will only use BibleHub.")
    DATA_DIR = DATA_DIRS[0]  # Use first as fallback

# Target languages
TARGET_LANGUAGES = ['fij', 'haw', 'smo', 'slv', 'tpi']

def parse_verse_ref(ref: str):
    """Parse GEN.001.026 format into book, chapter, verse."""
    parts = ref.split('.')
    book = parts[0]
    chapter = int(parts[1])
    verse = int(parts[2])
    return book, chapter, verse

def fetch_from_ebible_cache(book: str, chapter: int, verse: int, lang: str):
    """
    Try to fetch from .data/commentary/ eBible cache.
    
    Expected path: .data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-ebible.yaml
    """
    chapter_dir = DATA_DIR / "commentary" / book / f"{chapter:03d}"
    verse_dir = chapter_dir / f"{verse:03d}"
    ebible_file = verse_dir / f"{book}-{chapter:03d}-{verse:03d}-ebible.yaml"
    
    if not ebible_file.exists():
        return None
    
    try:
        with open(ebible_file, 'r', encoding='utf-8') as f:
            ebible_data = yaml.safe_load(f)
        
        # eBible data structure may vary - look for translations by language code
        if 'translations' in ebible_data and lang in ebible_data['translations']:
            return ebible_data['translations'][lang].get('text', '')
        
        # Alternative structure: direct language key
        if lang in ebible_data:
            if isinstance(ebible_data[lang], dict):
                return ebible_data[lang].get('text', '')
            elif isinstance(ebible_data[lang], str):
                return ebible_data[lang]
        
        return None
    except Exception as e:
        print(f"  Warning: Could not read {ebible_file}: {e}")
        return None

def fetch_from_biblehub(book: str, chapter: int, verse: int, lang: str):
    """
    Try to fetch from BibleHub as fallback.
    
    Note: BibleHub primarily has English translations. Non-English (fij, haw, smo, slv, tpi)
    may not be available.
    """
    if not BIBLEHUB_AVAILABLE:
        return None
    
    try:
        translations = fetch_verses_from_biblehub(book, chapter, verse, use_cache=True)
        
        # Look for language code in translations
        # BibleHub uses different format: might be lang-VERSION
        for key, text in translations.items():
            if key.startswith(f"{lang}-") or key == lang:
                return text
        
        return None
    except VerseFetchError as e:
        print(f"  BibleHub error for {book} {chapter}:{verse}: {e}")
        return None
    except Exception as e:
        print(f"  Unexpected error fetching from BibleHub: {e}")
        return None

def fetch_translation(verse_ref: str, lang: str):
    """
    Fetch translation for a verse in a specific language.
    
    Priority:
    1. Try eBible cache (.data/commentary/)
    2. Try BibleHub
    3. Return None if not found
    """
    book, chapter, verse = parse_verse_ref(verse_ref)
    
    # Try eBible cache first
    text = fetch_from_ebible_cache(book, chapter, verse, lang)
    if text:
        return text, "ebible-cache"
    
    # Try BibleHub as fallback
    text = fetch_from_biblehub(book, chapter, verse, lang)
    if text:
        return text, "biblehub"
    
    return None, None

def process_question_sheet(input_file: Path, output_file: Path = None):
    """
    Process a question sheet, fetching translations for all verses.
    
    Args:
        input_file: Path to input *_questions.yaml
        output_file: Path to output file (default: overwrite input)
    """
    if output_file is None:
        output_file = input_file
    
    print(f"\nProcessing: {input_file.name}")
    print("=" * 80)
    
    # Load question sheet
    with open(input_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data or 'verses' not in data:
        print("  ❌ Invalid question sheet format")
        return False
    
    total_verses = len(data['verses'])
    translations_included = data.get('translations_included', TARGET_LANGUAGES)
    
    print(f"  Verses: {total_verses}")
    print(f"  Target languages: {', '.join(translations_included)}")
    print()
    
    # Statistics
    stats = {lang: {'found': 0, 'missing': 0, 'sources': {}} for lang in translations_included}
    
    # Process each verse
    for i, verse_entry in enumerate(data['verses'], 1):
        verse_ref = verse_entry['reference']
        
        if i % 50 == 0:
            print(f"  Progress: {i}/{total_verses} verses...")
        
        # Initialize translations dict if not exists
        if 'translations' not in verse_entry or not isinstance(verse_entry['translations'], dict):
            verse_entry['translations'] = {}
        
        # Fetch each language
        for lang in translations_included:
            # Skip if already has translation
            if lang in verse_entry['translations'] and verse_entry['translations'][lang]:
                stats[lang]['found'] += 1
                continue
            
            # Fetch translation
            text, source = fetch_translation(verse_ref, lang)
            
            if text:
                verse_entry['translations'][lang] = text
                stats[lang]['found'] += 1
                if source:
                    stats[lang]['sources'][source] = stats[lang]['sources'].get(source, 0) + 1
            else:
                verse_entry['translations'][lang] = None  # Explicitly mark as not found
                stats[lang]['missing'] += 1
        
        # Remove the "note" field if it exists (was placeholder)
        if 'note' in verse_entry:
            del verse_entry['note']
    
    # Remove top-level note if exists
    if 'note' in data:
        del data['note']
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    # Print statistics
    print("\n  Translation Statistics:")
    print("  " + "-" * 76)
    for lang in translations_included:
        found = stats[lang]['found']
        missing = stats[lang]['missing']
        total = found + missing
        pct = (found / total * 100) if total > 0 else 0
        
        sources_str = ", ".join(f"{src}:{cnt}" for src, cnt in stats[lang]['sources'].items())
        if not sources_str:
            sources_str = "none"
        
        print(f"  {lang:5} Found: {found:3}/{total:3} ({pct:5.1f}%)  Sources: {sources_str}")
    
    print(f"\n  ✓ Output written to: {output_file.name}")
    return True

def main():
    """Process all question sheets."""
    # Find all question sheet files
    experiments_dir = Path(__file__).parent
    question_files = list(experiments_dir.glob("*_questions.yaml"))
    
    if not question_files:
        print("No *_questions.yaml files found in experiments directory")
        return
    
    print("=" * 80)
    print("TRANSLATION FETCHER FOR NUMBER-SYSTEMS FEATURE")
    print("=" * 80)
    print(f"\nFound {len(question_files)} question sheet(s)")
    print(f"Target languages: {', '.join(TARGET_LANGUAGES)}")
    print(f"Data directory: {DATA_DIR}")
    print(f"BibleHub available: {BIBLEHUB_AVAILABLE}")
    
    success_count = 0
    for question_file in sorted(question_files):
        try:
            if process_question_sheet(question_file):
                success_count += 1
        except Exception as e:
            print(f"  ❌ Error processing {question_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print(f"COMPLETE: {success_count}/{len(question_files)} files processed successfully")
    print("=" * 80)
    
    if success_count < len(question_files):
        print("\n⚠️  Some files had errors. Check messages above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

