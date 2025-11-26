#!/usr/bin/env python3
"""
Enrich TBTA Extract with Verse Text
===================================

Reads the tbta-extract.jsonl file and appends verse text for specified languages.
Each language's text is stored as a top-level key (ISO code) for easy access.

Usage:
    python enrich_extract_with_verses.py --input analysis/tbta-extract.jsonl \
        --languages eng,spa,fra --output analysis/tbta-extract-with-verses.jsonl

Output format:
    {
        "verse": "REV.001.010",
        "label": "Singular",
        "constituent": "sound",
        "part": "Noun",
        "path": "Clause[4]/Clause[0]/NP[0]",
        "eng": {"NIV": "...", "ESV": "..."},
        "spa": {"RV1960": "..."},
        "fra": {"LSG": "..."}
    }
"""

import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.tools.fetch_verse import (ensure_sparse_checkout_chapter, fetch_verse,
                                   filter_by_languages)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def parse_verse_ref(ref: str):
    """Parse TBTA verse ref to (book, chapter, verse).

    Supports formats:
    - GEN.001.001 (standard)
    - GEN-001-001 (alternate)
    - REV.001.010
    """
    # Try dot format first (standard)
    parts = ref.split('.')
    if len(parts) == 3:
        return parts[0], int(parts[1]), int(parts[2])
    # Try hyphen format
    parts = ref.split('-')
    if len(parts) == 3:
        return parts[0], int(parts[1]), int(parts[2])
    return None, None, None


def organize_by_language(translations: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """
    Reorganize translations from flat dict to nested by language.

    Input:  {"eng-NIV": "...", "eng-ESV": "...", "spa-RV1960": "..."}
    Output: {"eng": {"NIV": "...", "ESV": "..."}, "spa": {"RV1960": "..."}}
    """
    result = {}
    for trans_id, text in translations.items():
        parts = trans_id.split('-', 1)
        lang = parts[0].lower()
        version = parts[1] if len(parts) > 1 else "default"

        if lang not in result:
            result[lang] = {}
        result[lang][version] = text

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Enrich TBTA extract with verse text from multiple languages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python enrich_extract_with_verses.py --input tbta-extract.jsonl \\
        --languages eng,spa,fra,deu --output tbta-extract-with-verses.jsonl

    # With more languages for diversity analysis
    python enrich_extract_with_verses.py --input tbta-extract.jsonl \\
        --languages eng,spa,fra,deu,por,ita,nld,swe,dan,nor,fin,rus,pol,ces,hun,ron,ell,tur,ara,heb,zho \\
        --output tbta-extract-with-verses.jsonl
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file (tbta-extract.jsonl)")
    parser.add_argument("--languages", required=True,
                        help="Comma-separated list of ISO-639-3 codes (e.g., eng,spa,fra)")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="Delay between fetches in seconds (default: 0.1)")
    parser.add_argument("--skip-errors", action="store_true",
                        help="Skip verses that fail to fetch instead of stopping")

    args = parser.parse_args()

    languages = [lang.strip().lower() for lang in args.languages.split(',')]
    logger.info(f"Enriching with {len(languages)} languages: {', '.join(languages)}")

    # Cache for fetched verses to avoid refetching same verse
    # Key: "BOOK.CCC.VVV", Value: {lang: {version: text}}
    verse_cache: Dict[str, Dict[str, Dict[str, str]]] = {}

    processed_count = 0
    error_count = 0
    cache_hits = 0

    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    # Count total lines for progress
    with open(input_path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for line in f if line.strip())
    logger.info(f"Processing {total_lines} entries...")

    # Open output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:

        for line_num, line in enumerate(f_in, 1):
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
                verse_ref = entry.get('verse')

                if not verse_ref:
                    # Pass through without modification
                    f_out.write(line)
                    continue

                # Check cache first
                if verse_ref in verse_cache:
                    # Merge cached translations into entry
                    for lang, versions in verse_cache[verse_ref].items():
                        entry[lang] = versions
                    cache_hits += 1
                else:
                    # Fetch new verse
                    book, chapter, verse = parse_verse_ref(verse_ref)
                    if book:
                        try:
                            # Ensure sparse checkout has this chapter
                            ensure_sparse_checkout_chapter(book, chapter)

                            # Fetch all translations
                            translations = fetch_verse(book, chapter, verse, use_cache=True)

                            # Filter by requested languages
                            filtered = filter_by_languages(translations, languages)

                            # Organize by language
                            organized = organize_by_language(filtered)

                            # Store in entry and cache
                            for lang, versions in organized.items():
                                entry[lang] = versions
                            verse_cache[verse_ref] = organized

                            time.sleep(args.delay)

                        except Exception as e:
                            logger.warning(f"Failed to fetch {verse_ref}: {e}")
                            error_count += 1
                            if not args.skip_errors:
                                raise
                    else:
                        logger.warning(f"Invalid verse format: {verse_ref}")
                        error_count += 1

                # Write enriched entry
                f_out.write(json.dumps(entry, ensure_ascii=False) + '\n')
                processed_count += 1

                # Progress indicator
                if processed_count % 100 == 0:
                    pct = (line_num / total_lines) * 100
                    logger.info(f"Progress: {processed_count}/{total_lines} ({pct:.1f}%) - Cache hits: {cache_hits}")

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")
                continue

    # Summary
    logger.info("=" * 50)
    logger.info("ENRICHMENT COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Processed: {processed_count} entries")
    logger.info(f"Cache hits: {cache_hits} (verses appearing multiple times)")
    logger.info(f"Fetch errors: {error_count}")
    logger.info(f"Output: {args.output}")


if __name__ == "__main__":
    main()
