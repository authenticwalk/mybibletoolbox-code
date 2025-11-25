#!/usr/bin/env python3
"""
Discover available languages using Quote Bible skill.

This tool fetches sample verses from NT and OT to discover all available
language codes and their metadata in the Bible translation corpus.

Usage:
    python discover_languages.py --output languages.jsonl
    python discover_languages.py --nt-verse JHN.003.016 --ot-verse GEN.001.001 --output out.jsonl
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, Tuple

# Import fetch_verse module from same directory
from fetch_verse import fetch_verse, filter_by_languages, VerseFetchError


def quote_verse(verse_ref: str) -> Dict[str, str]:
    """
    Fetch verse in all languages using fetch_verse module.

    Uses: src.tools.fetch_verse (imported directly)

    Args:
        verse_ref: Verse reference in STANDARDIZATION.md format (e.g., JHN.003.016)

    Returns:
        Dictionary mapping translation IDs to verse text

    Raises:
        RuntimeError: If verse fetching fails
    """
    # Import parse_reference to convert verse_ref to book, chapter, verse
    # Need to add quote-bible scripts to path
    project_root = Path(__file__).resolve().parent.parent.parent
    quote_bible_scripts = project_root / '.claude' / 'skills' / 'quote-bible' / 'scripts'
    if str(quote_bible_scripts) not in sys.path:
        sys.path.insert(0, str(quote_bible_scripts))

    from book_codes import parse_reference

    try:
        # Parse reference into book, chapter, verse
        book, chapter, verse = parse_reference(verse_ref)

        # Collect translations from all fetchers (matches main() logic in fetch_verse.py)
        translations = {}

        # Import fetchers
        from biblehub_fetcher import fetch_verses_from_biblehub
        from src.ingest_data.ebible.ebible_fetcher import fetch_verses_from_ebible

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

        return translations

    except Exception as e:
        raise RuntimeError(f"Failed to fetch verse {verse_ref}: {e}")


def parse_translation_id(trans_id: str) -> Tuple[str, str]:
    """
    Parse translation ID into language code and version.

    Format: {lang}-{version} or {lang}-{version}-{year}

    Args:
        trans_id: Translation ID (e.g., "eng-NIV", "spa-RV-1960")

    Returns:
        Tuple of (language_code, version)

    Examples:
        >>> parse_translation_id("eng-NIV")
        ('eng', 'NIV')
        >>> parse_translation_id("spa-RV-1960")
        ('spa', 'RV-1960')
    """
    parts = trans_id.split('-', 1)
    if len(parts) < 2:
        # Malformed ID - use whole thing as version
        return (parts[0], parts[0])

    lang_code = parts[0].lower()
    version = parts[1]

    return (lang_code, version)


def extract_languages(nt_result: Dict[str, str], ot_result: Dict[str, str]) -> Dict[str, Dict]:
    """
    Extract unique languages from NT and OT results.

    Args:
        nt_result: Dictionary of translation_id -> text from NT verse
        ot_result: Dictionary of translation_id -> text from OT verse

    Returns:
        Dictionary mapping language codes to metadata:
        {
            "lang_code": {
                "name": "Language Name",  # Inferred from version codes
                "testament": "both" | "nt_only" | "ot_only",
                "translations": count,
                "versions": [list of version codes]
            }
        }
    """
    languages = defaultdict(lambda: {
        'name': '',
        'testament': set(),
        'translations': 0,
        'versions': set()
    })

    # Process NT translations
    for trans_id in nt_result.keys():
        lang_code, version = parse_translation_id(trans_id)
        languages[lang_code]['testament'].add('nt')
        languages[lang_code]['versions'].add(version)

    # Process OT translations
    for trans_id in ot_result.keys():
        lang_code, version = parse_translation_id(trans_id)
        languages[lang_code]['testament'].add('ot')
        languages[lang_code]['versions'].add(version)

    # Convert sets to final format
    result = {}
    for lang_code, data in languages.items():
        testament_set = data['testament']
        if 'nt' in testament_set and 'ot' in testament_set:
            testament = 'both'
        elif 'nt' in testament_set:
            testament = 'nt_only'
        else:
            testament = 'ot_only'

        versions = sorted(list(data['versions']))
        translation_count = len(versions)

        result[lang_code] = {
            'testament': testament,
            'translations': translation_count,
            'versions': versions
        }

    return result


def main():
    """CLI entry point for language discovery."""
    parser = argparse.ArgumentParser(
        description='Discover available languages from Bible translation corpus',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python discover_languages.py --output languages.jsonl
  python discover_languages.py --nt-verse JHN.003.016 --ot-verse GEN.001.001 --output out.jsonl

Output Format (JSONL):
  {"lang": "eng", "testament": "both", "translations": 25, "versions": ["ASV", "KJV", "NIV", ...]}
  {"lang": "spa", "testament": "both", "translations": 3, "versions": ["RV", "RV-1960", ...]}
  {"lang": "mri", "testament": "nt_only", "translations": 1, "versions": ["Maori"]}
        """
    )

    parser.add_argument(
        '--nt-verse',
        default='JHN.003.016',
        help='NT sample verse in STANDARDIZATION.md format (default: JHN.003.016)'
    )

    parser.add_argument(
        '--ot-verse',
        default='GEN.001.001',
        help='OT sample verse in STANDARDIZATION.md format (default: GEN.001.001)'
    )

    parser.add_argument(
        '--output',
        required=True,
        help='Output JSONL file path'
    )

    args = parser.parse_args()

    try:
        # Fetch NT verse
        print(f"Fetching NT verse: {args.nt_verse}...", file=sys.stderr)
        nt_result = quote_verse(args.nt_verse)
        print(f"  Found {len(nt_result)} NT translations", file=sys.stderr)

        # Fetch OT verse
        print(f"Fetching OT verse: {args.ot_verse}...", file=sys.stderr)
        ot_result = quote_verse(args.ot_verse)
        print(f"  Found {len(ot_result)} OT translations", file=sys.stderr)

        # Extract languages
        print("Extracting language metadata...", file=sys.stderr)
        languages = extract_languages(nt_result, ot_result)

        # Write to output file
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            for lang_code in sorted(languages.keys()):
                lang_data = languages[lang_code]
                record = {
                    'lang': lang_code,
                    **lang_data
                }
                f.write(json.dumps(record, ensure_ascii=False) + '\n')

        print(f"\n✓ Found {len(languages)} languages, saved to {args.output}", file=sys.stderr)

        # Validation and statistics
        nt_count = sum(1 for data in languages.values() if data['testament'] in ('both', 'nt_only'))
        ot_count = sum(1 for data in languages.values() if data['testament'] in ('both', 'ot_only'))
        both_count = sum(1 for data in languages.values() if data['testament'] == 'both')

        print(f"\nStatistics:", file=sys.stderr)
        print(f"  NT languages: {nt_count}", file=sys.stderr)
        print(f"  OT languages: {ot_count}", file=sys.stderr)
        print(f"  Both testaments: {both_count}", file=sys.stderr)
        print(f"  NT only: {nt_count - both_count}", file=sys.stderr)
        print(f"  OT only: {ot_count - both_count}", file=sys.stderr)

        # Validation warning
        if nt_count < 900:
            print(f"\n⚠ WARNING: Expected ~1000 NT languages, found {nt_count}", file=sys.stderr)
            print("  This may indicate:", file=sys.stderr)
            print("  - Incomplete data fetch", file=sys.stderr)
            print("  - Quote Bible skill issues", file=sys.stderr)
            print("  - Network/cache problems", file=sys.stderr)
            print("  Debug and fix the language extraction logic or data sources", file=sys.stderr)
            sys.exit(1)

        # Top languages by translation count
        top_langs = sorted(languages.items(), key=lambda x: x[1]['translations'], reverse=True)[:10]
        print(f"\nTop 10 languages by translation count:", file=sys.stderr)
        for lang_code, data in top_langs:
            print(f"  {lang_code}: {data['translations']} translations ({data['testament']})", file=sys.stderr)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
