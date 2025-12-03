#!/usr/bin/env python3
"""
Enrich TBTA Extract with Verse Text
===================================

Reads the tbta-extract.jsonl file and appends verse text from cached ebible translations.
Uses src/util/cache.py to fetch from translations-ebible cache files.

Usage:
    python enrich_extract_with_verses.py --input analysis/tbta-extract.jsonl \
        --translations eng-NIV,eng-ESV,spa-RV1960 --output analysis/tbta-extract-with-verses.jsonl

Output format:
    {
        "verse": "REV.001.010",
        "label": "Singular",
        "constituent": "sound",
        "part": "Noun",
        "path": "Clause[4]/Clause[0]/NP[0]",
        "translations": {"eng-NIV": "...", "eng-ESV": "...", "spa-RV1960": "..."}
    }
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.config import DATA_DIR
from src.util.cache import get_cached_verse

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


def filter_translations_by_codes(translations: Dict[str, str], codes: list) -> Dict[str, str]:
    """
    Filter translations dict to include specified translation codes or language prefixes.

    Supports two formats:
    - Full code: "eng-YLT" matches exactly "eng-YLT"
    - Language prefix: "eng" matches first translation starting with "eng-" (e.g., "eng-NIV")

    Args:
        translations: Dict like {"eng-NIV": "...", "spa-RV1960": "...", "ara": "..."}
        codes: List of translation codes or 3-letter language prefixes

    Returns:
        Filtered dict with matching translations

    Example:
        codes = ["eng-YLT", "ara", "heb"]
        - "eng-YLT" -> exact match
        - "ara" -> matches first "ara-*" or exact "ara"
        - "heb" -> matches first "heb-*" or exact "heb"
    """
    result = {}

    for code in codes:
        # Check if it's a language prefix (3 letters, no hyphen)
        is_prefix = len(code) == 3 and '-' not in code

        if is_prefix:
            # Find first translation matching this language prefix
            for trans_key, trans_value in translations.items():
                # Match "ara" to "ara" or "ara-NAV"
                if trans_key == code or trans_key.startswith(code + '-'):
                    result[trans_key] = trans_value
                    break  # Only take first match for prefix
        else:
            # Exact match
            if code in translations:
                result[code] = translations[code]

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Enrich TBTA extract with verse text from multiple languages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python enrich_extract_with_verses.py --input tbta-extract.jsonl \\
        --translations eng-NIV,eng-ESV,spa-RV1960 --output tbta-extract-with-verses.jsonl
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file (tbta-extract.jsonl)")
    parser.add_argument("--translations", required=True,
                        help="Comma-separated list of translation codes or language prefixes. "
                             "Full codes (eng-YLT) match exactly. 3-letter prefixes (eng, ara, heb) "
                             "match the first available translation in that language.")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--limit", required=False, type=int, help="Limit the number of entries to process")

    args = parser.parse_args()

    translations = [t.strip() for t in args.translations.split(',')]
    logger.info(f"Enriching with {len(translations)} translations: {', '.join(translations)}")

    processed_count = 0
    cache_hits = 0
    cache_misses = 0

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

                # Parse verse reference
                book, chapter, verse = parse_verse_ref(verse_ref)
                if not book:
                    logger.warning(f"Invalid verse format: {verse_ref}")
                    f_out.write(line)
                    continue

                # Standardize verse reference in output (GEN-001-001)
                standard_ref = f"{book}-{chapter:03d}-{verse:03d}"
                entry['verse'] = standard_ref

                # Fetch from cache using translations-ebible suffix
                cached_data = get_cached_verse(book, chapter, verse, suffix="translations-ebible", cache_root=DATA_DIR / "commentary")
                
                if cached_data and 'translations' in cached_data:
                    # Filter by requested translation codes
                    filtered = filter_translations_by_codes(cached_data['translations'], translations)
                    if filtered:
                        entry['translations'] = filtered
                    cache_hits += 1
                else:
                    cache_misses += 1
                    print(f"Cache miss: {standard_ref} - add to sparse checkout: cd .data && git sparse-checkout add commentary/{book}/{chapter:03d}", file=sys.stderr)

                # Write enriched entry
                f_out.write(json.dumps(entry, ensure_ascii=False) + '\n')
                processed_count += 1

                # Progress indicator
                if processed_count % 100 == 0:
                    pct = (line_num / total_lines) * 100
                    logger.info(f"Progress: {processed_count}/{total_lines} ({pct:.1f}%) - Hits: {cache_hits}, Misses: {cache_misses}")
                if args.limit and processed_count >= args.limit:
                    break

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")
                continue

    # Summary
    logger.info("=" * 50)
    logger.info("ENRICHMENT COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Processed: {processed_count} entries")
    logger.info(f"Cache hits: {cache_hits}")
    logger.info(f"Cache misses: {cache_misses}")
    logger.info(f"Output: {args.output}")


if __name__ == "__main__":
    main()
