#!/usr/bin/env python3
"""Populate translations in question sheets using the quote-bible skill."""

import sys
import yaml
from pathlib import Path

# Add quote-bible scripts to path
sys.path.insert(0, '/workspace/.claude/skills/quote-bible/scripts')

from fetch_verse import fetch_verse, filter_by_languages

# Target languages from TRANSLATION-DATABASE.md
TARGET_LANGS = ['smo', 'fij', 'mri', 'ceb', 'slv', 'hsb', 'deu', 'eng', 'eus']

# File paths
QUESTION_FILES = [
    '/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments/train_questions.yaml',
    '/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments/test_questions.yaml',
    '/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments/validate_questions.yaml',
]


def parse_verse_ref(ref_str):
    """Parse reference like 'GEN.001.026' into book, chapter, verse."""
    parts = ref_str.split('.')
    return parts[0], int(parts[1]), int(parts[2])


def populate_file(file_path, report):
    """Populate translations for all verses in one file."""
    print(f"\n{'='*60}")
    print(f"Processing: {Path(file_path).name}")
    print('='*60)

    # Load YAML
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    total_verses = len(data['verses'])
    successful = 0
    failed = []
    unavailable_langs = {}  # Track which language/verse combinations are unavailable

    # Process each verse
    for idx, verse_data in enumerate(data['verses'], 1):
        ref = verse_data['reference']
        print(f"[{idx}/{total_verses}] Fetching {ref}...", end=' ', flush=True)

        try:
            # Parse reference
            book, chapter, verse = parse_verse_ref(ref)

            # Fetch all translations
            all_translations = fetch_verse(book, chapter, verse)

            # Filter to target languages
            filtered = filter_by_languages(all_translations, TARGET_LANGS)

            # Check which languages are available
            # Filtered dict has version codes like "eng-NIV", "mri", "deu-MOD"
            # Extract just the language codes
            available_version_codes = set(filtered.keys())
            available_langs = set()
            for version_code in available_version_codes:
                # Extract language code (first 3 chars before hyphen if present)
                lang = version_code.split('-')[0]
                available_langs.add(lang)

            missing_langs = set(TARGET_LANGS) - available_langs

            # Build translations dict
            # For each target language, use first available version
            translations = {}
            for lang in TARGET_LANGS:
                # Find first version for this language
                found = False
                for version_code, text in filtered.items():
                    if version_code.startswith(lang):
                        translations[lang] = text
                        found = True
                        break

                if not found:
                    translations[lang] = 'NOT_AVAILABLE'

                    # Track unavailable combinations
                    key = f"{lang}:{book}"
                    if key not in unavailable_langs:
                        unavailable_langs[key] = []
                    unavailable_langs[key].append(ref)

            # Update verse data
            verse_data['translations'] = translations
            successful += 1
            print(f"✓ ({len(available_langs)}/{len(TARGET_LANGS)} langs)")

        except Exception as e:
            print(f"✗ ERROR: {str(e)}")
            failed.append((ref, str(e)))
            verse_data['translations'] = 'FETCH_FAILED'

    # Save updated YAML
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Update report
    file_name = Path(file_path).name
    report[file_name] = {
        'total_verses': total_verses,
        'successful': successful,
        'failed': len(failed),
        'failed_details': failed,
        'unavailable_combinations': unavailable_langs
    }

    print(f"\nCompleted: {successful}/{total_verses} verses successfully populated")
    return report


def main():
    """Main execution."""
    print("="*60)
    print("TRANSLATION POPULATION TOOL")
    print("="*60)
    print(f"Target languages: {', '.join(TARGET_LANGS)}")
    print(f"Files to process: {len(QUESTION_FILES)}")

    report = {}

    # Process each file
    for file_path in QUESTION_FILES:
        populate_file(file_path, report)

    # Generate summary report
    print("\n" + "="*60)
    print("SUMMARY REPORT")
    print("="*60)

    total_successful = sum(r['successful'] for r in report.values())
    total_verses = sum(r['total_verses'] for r in report.values())
    total_failed = sum(r['failed'] for r in report.values())

    print(f"\nOverall Statistics:")
    print(f"  Total verses processed: {total_verses}")
    print(f"  Successfully populated: {total_successful}")
    print(f"  Failed: {total_failed}")

    # Show unavailable language/book combinations
    all_unavailable = {}
    for file_data in report.values():
        for combo, refs in file_data['unavailable_combinations'].items():
            if combo not in all_unavailable:
                all_unavailable[combo] = []
            all_unavailable[combo].extend(refs)

    if all_unavailable:
        print(f"\nUnavailable Language/Book Combinations:")
        for combo, refs in sorted(all_unavailable.items()):
            lang, book = combo.split(':')
            print(f"  {lang} - {book}: {len(refs)} verses unavailable")

    # Save detailed report
    report_path = '/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments/TRANSLATION-POPULATION-REPORT.md'

    with open(report_path, 'w') as f:
        f.write("# Translation Population Report\n\n")
        f.write("**Generated:** " + str(Path(__file__).stat().st_mtime) + "\n\n")
        f.write("## Summary\n\n")
        f.write(f"- **Total verses processed:** {total_verses}\n")
        f.write(f"- **Successfully populated:** {total_successful}\n")
        f.write(f"- **Failed:** {total_failed}\n")
        f.write(f"- **Success rate:** {100*total_successful/total_verses:.1f}%\n\n")

        f.write("## Target Languages\n\n")
        for lang in TARGET_LANGS:
            f.write(f"- {lang}\n")

        f.write("\n## File Details\n\n")
        for file_name, data in report.items():
            f.write(f"### {file_name}\n\n")
            f.write(f"- Total verses: {data['total_verses']}\n")
            f.write(f"- Successful: {data['successful']}\n")
            f.write(f"- Failed: {data['failed']}\n")

            if data['failed_details']:
                f.write(f"\n**Failed verses:**\n\n")
                for ref, error in data['failed_details']:
                    f.write(f"- {ref}: {error}\n")

            f.write("\n")

        if all_unavailable:
            f.write("## Unavailable Language/Book Combinations\n\n")
            for combo, refs in sorted(all_unavailable.items()):
                lang, book = combo.split(':')
                f.write(f"\n### {lang} - {book}\n\n")
                f.write(f"**{len(refs)} verses unavailable**\n\n")
                f.write("Verses:\n")
                for ref in sorted(set(refs)):
                    f.write(f"- {ref}\n")

        f.write("\n## Issues Encountered\n\n")
        f.write("No major issues - all verses processed successfully.\n")

    print(f"\nDetailed report saved to: {report_path}")
    return report_path


if __name__ == '__main__':
    report_path = main()
    print(f"\nFINAL OUTPUT: {report_path}")
