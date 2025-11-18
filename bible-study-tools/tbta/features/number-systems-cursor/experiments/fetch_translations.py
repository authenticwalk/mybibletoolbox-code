#!/usr/bin/env python3
"""
Fetch translations for number-systems question sheets.

This script:
1. Reads *_questions.yaml files
2. Fetches translations using the fetch_verse.py skill
3. Populates the translations field with actual text
4. Focuses on: Fijian (fij), Hawaiian (haw), Samoan (smo), Slovenian (slv), Tok Pisin (tpi)
5. Also fetches common languages for algorithm refinement: English, Greek, Hebrew
"""

import yaml
import sys
from pathlib import Path

# Find project root (go up from experiments/)
# __file__ = experiments/fetch_translations.py
# .parents[0] = experiments/
# .parents[1] = number-systems-cursor/
# .parents[2] = features/
# .parents[3] = tbta/
# .parents[4] = bible-study-tools/
# .parents[5] = mybibletoolbox-code/ (PROJECT ROOT)
PROJECT_ROOT = Path(__file__).resolve().parents[5]

# Add quote-bible scripts to path
QUOTE_BIBLE_DIR = PROJECT_ROOT / ".claude" / "skills" / "quote-bible" / "scripts"
sys.path.insert(0, str(QUOTE_BIBLE_DIR))

try:
    from fetch_verse import fetch_verse, filter_by_languages, VerseFetchError
    FETCH_VERSE_AVAILABLE = True
except ImportError:
    print("⚠️  fetch_verse not available. Cannot fetch translations.")
    FETCH_VERSE_AVAILABLE = False
    sys.exit(1)

# Target languages for number system validation
TARGET_LANGUAGES = ['fij', 'haw', 'smo', 'slv', 'tpi']

# Additional useful languages for algorithm refinement
REFERENCE_LANGUAGES = ['eng', 'grc', 'heb']

# All languages to fetch
ALL_LANGUAGES = TARGET_LANGUAGES + REFERENCE_LANGUAGES

def parse_verse_ref(ref: str):
    """Parse GEN.001.026 format into book, chapter, verse."""
    parts = ref.split('.')
    book = parts[0]
    chapter = int(parts[1])
    verse = int(parts[2])
    return book, chapter, verse

def fetch_translations_for_verse(verse_ref: str, languages: list):
    """
    Fetch all translations for a verse using the fetch_verse skill.
    
    Args:
        verse_ref: Verse reference (e.g., "GEN.001.026")
        languages: List of language codes to fetch (e.g., ['eng', 'fij', 'haw'])
    
    Returns:
        dict: {lang_code: translation_text, ...}
    """
    book, chapter, verse = parse_verse_ref(verse_ref)
    
    try:
        # fetch_verse() returns dict like: {'eng-NIV': 'text', 'eng-KJV': 'text', ...}
        # NOTE: It fetches ALL available translations, then we filter
        all_translations = fetch_verse(book, chapter, verse)
        
        if not all_translations:
            return {}
        
        # Filter to only requested languages
        filtered = filter_by_languages(all_translations, languages)
        
        # Group by language code - take first version we find for each language
        by_language = {}
        for version_code, text in filtered.items():
            lang = version_code.split('-')[0]  # Extract language code (before dash)
            if lang in languages:
                # Store the first version we find for each language
                if lang not in by_language:
                    by_language[lang] = text
        
        return by_language
        
    except VerseFetchError as e:
        print(f"  Warning: Could not fetch {verse_ref}: {e}")
        return {}
    except Exception as e:
        print(f"  Warning: Unexpected error fetching {verse_ref}: {e}")
        return {}

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
    # Use ALL_LANGUAGES (target + reference languages)
    translations_included = ALL_LANGUAGES
    
    print(f"  Verses: {total_verses}")
    print(f"  Languages: {', '.join(translations_included)}")
    print(f"  Target languages (number systems): {', '.join(TARGET_LANGUAGES)}")
    print(f"  Reference languages (algorithm refinement): {', '.join(REFERENCE_LANGUAGES)}")
    print()
    
    # Statistics
    stats = {lang: {'found': 0, 'missing': 0} for lang in translations_included}
    
    # Process each verse
    for i, verse_entry in enumerate(data['verses'], 1):
        verse_ref = verse_entry['reference']
        
        if i % 50 == 0:
            print(f"  Progress: {i}/{total_verses} verses...")
        
        # Fetch all translations for this verse at once
        fetched_translations = fetch_translations_for_verse(verse_ref, translations_included)
        
        # Initialize translations dict if not exists
        if 'translations' not in verse_entry or not isinstance(verse_entry['translations'], dict):
            verse_entry['translations'] = {}
        
        # Update with fetched translations
        for lang in translations_included:
            if lang in fetched_translations and fetched_translations[lang]:
                verse_entry['translations'][lang] = fetched_translations[lang]
                stats[lang]['found'] += 1
            else:
                # Don't overwrite existing translations
                if lang not in verse_entry['translations'] or not verse_entry['translations'][lang]:
                    verse_entry['translations'][lang] = None  # Explicitly mark as not found
                    stats[lang]['missing'] += 1
                else:
                    stats[lang]['found'] += 1  # Already had translation
        
        # Remove the "note" field if it exists (was placeholder)
        if 'note' in verse_entry:
            del verse_entry['note']
    
    # Remove top-level note if exists
    if 'note' in data:
        del data['note']
    
    # Update translations_included field
    data['translations_included'] = translations_included
    
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
        
        print(f"  {lang:5} Found: {found:3}/{total:3} ({pct:5.1f}%)")
    
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
    print(f"Target languages (number systems): {', '.join(TARGET_LANGUAGES)}")
    print(f"Reference languages (refinement): {', '.join(REFERENCE_LANGUAGES)}")
    print(f"Fetching {len(ALL_LANGUAGES)} languages total")
    print(f"Using: fetch_verse.py skill")
    
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

