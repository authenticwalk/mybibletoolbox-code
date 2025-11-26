#!/usr/bin/env python3
"""
Fast Enrich TBTA Extract from Cached Translations
==================================================

Uses already-cached translation YAML files from DATA_DIR/commentary.
Much faster than fetching from network.

Usage:
    python enrich_from_cache.py --input analysis/tbta-extract.jsonl \
        --languages eng,spa,fra --output analysis/tbta-extract-with-verses.jsonl
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Data directory
DATA_DIR = Path(os.environ.get('DATA_DIR', '.data'))


def parse_verse_ref(ref: str):
    """Parse TBTA verse ref to (book, chapter, verse)."""
    parts = ref.split('.')
    if len(parts) == 3:
        return parts[0], int(parts[1]), int(parts[2])
    parts = ref.split('-')
    if len(parts) == 3:
        return parts[0], int(parts[1]), int(parts[2])
    return None, None, None


def get_cache_path(book: str, chapter: int, verse: int) -> Path:
    """Get path to cached ebible translation file."""
    return DATA_DIR / 'commentary' / book / f'{chapter:03d}' / f'{verse:03d}' / f'{book}-{chapter:03d}-{verse:03d}-translations-ebible.yaml'


def filter_by_languages(translations: Dict[str, str], languages: List[str]) -> Dict[str, str]:
    """Filter translations by language codes."""
    if not languages:
        return translations

    languages_lower = [lang.lower() for lang in languages]
    filtered = {}
    for trans_id, text in translations.items():
        lang_code = trans_id.split('-')[0].lower()
        if lang_code in languages_lower:
            filtered[trans_id] = text
    return filtered


def organize_by_language(translations: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """Reorganize translations from flat dict to nested by language."""
    result = {}
    for trans_id, text in translations.items():
        parts = trans_id.split('-', 1)
        lang = parts[0].lower()
        version = parts[1] if len(parts) > 1 else "default"

        if lang not in result:
            result[lang] = {}
        result[lang][version] = text

    return result


def load_cached_translations(book: str, chapter: int, verse: int) -> Optional[Dict[str, str]]:
    """Load translations from cache."""
    cache_path = get_cache_path(book, chapter, verse)
    if not cache_path.exists():
        return None

    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data.get('translations', {})
    except Exception as e:
        logger.debug(f"Error loading {cache_path}: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Fast enrich TBTA extract from cached translations",
    )
    parser.add_argument("--input", required=True, help="Input JSONL file")
    parser.add_argument("--languages", required=True,
                        help="Comma-separated list of ISO-639-3 codes")
    parser.add_argument("--output", required=True, help="Output JSONL file")

    args = parser.parse_args()

    languages = [lang.strip().lower() for lang in args.languages.split(',')]
    logger.info(f"Enriching with {len(languages)} languages: {', '.join(languages)}")
    logger.info(f"Using cache from: {DATA_DIR / 'commentary'}")

    # Cache for fetched verses
    verse_cache: Dict[str, Dict[str, Dict[str, str]]] = {}

    processed_count = 0
    cache_miss = 0
    cache_hits = 0

    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    # Count total lines
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
                    f_out.write(line)
                    continue

                # Check memory cache first
                if verse_ref in verse_cache:
                    for lang, versions in verse_cache[verse_ref].items():
                        entry[lang] = versions
                    cache_hits += 1
                else:
                    # Load from file cache
                    book, chapter, verse = parse_verse_ref(verse_ref)
                    if book:
                        translations = load_cached_translations(book, chapter, verse)
                        if translations:
                            filtered = filter_by_languages(translations, languages)
                            organized = organize_by_language(filtered)

                            for lang, versions in organized.items():
                                entry[lang] = versions
                            verse_cache[verse_ref] = organized
                        else:
                            cache_miss += 1
                    else:
                        logger.warning(f"Invalid verse format: {verse_ref}")

                # Write entry (enriched or not)
                f_out.write(json.dumps(entry, ensure_ascii=False) + '\n')
                processed_count += 1

                # Progress indicator
                if processed_count % 1000 == 0:
                    pct = (line_num / total_lines) * 100
                    logger.info(f"Progress: {processed_count}/{total_lines} ({pct:.1f}%) - Hits: {cache_hits}, Miss: {cache_miss}")

            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON at line {line_num}")
                continue

    # Summary
    logger.info("=" * 50)
    logger.info("ENRICHMENT COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Processed: {processed_count} entries")
    logger.info(f"Memory cache hits: {cache_hits}")
    logger.info(f"File cache misses: {cache_miss}")
    logger.info(f"Output: {args.output}")


if __name__ == "__main__":
    main()
