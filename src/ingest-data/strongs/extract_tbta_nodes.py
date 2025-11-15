#!/usr/bin/env python3
"""
TBTA-to-Strong's Extraction Script
====================================

Extracts TBTA linguistic nodes for each Strong's word and generates YAML files.

This script implements a three-way join linking:
    TBTA linguistic features → Macula source text → Strong's numbers

Usage:
    python extract_tbta_nodes.py
    python extract_tbta_nodes.py --testament NT
    python extract_tbta_nodes.py --book JHN
    python extract_tbta_nodes.py --dry-run

Algorithm:
    1. Clone/update TBTA repository from GitHub
    2. For each TBTA JSON file:
        a. Parse filename → verse reference (BOOK.chapter.verse)
        b. Load TBTA JSON and corresponding Macula YAML
        c. Flatten TBTA hierarchical tree to word-level constituents
        d. Align TBTA words to Macula words by position
        e. Extract Strong's number from Macula
        f. Extract TBTA node attributes
        g. Store: strongs_id → {node_attributes, verse_ref}
    3. Aggregate nodes per Strong's ID
    4. Deduplicate identical nodes (same attribute set)
    5. Cap verses per node (max 100, LRU)
    6. Generate YAML files per Strong's word

Output: .data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml

See: /plan/strongs-tbta-script.md for full requirements
See: /plan/strongs-tbta-script/extraction-algorithm.md for detailed algorithm
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from collections import OrderedDict, Counter, defaultdict
import argparse
import logging
import re

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Configuration
TBTA_REPO_URL = "https://github.com/AllTheWord/tbta_db_export"
TBTA_LOCAL_PATH = Path("/tmp/tbta_db_export")
TBTA_JSON_DIR = TBTA_LOCAL_PATH / "json"
DATA_DIR = Path(".data")
COMMENTARY_DIR = DATA_DIR / "commentary"
STRONGS_DIR = DATA_DIR / "strongs"

# Book name to USFM code mapping
BOOK_NAME_MAP = {
    "Genesis": "GEN", "Exodus": "EXO", "Leviticus": "LEV", "Numbers": "NUM", "Deuteronomy": "DEU",
    "Joshua": "JOS", "Judges": "JDG", "Ruth": "RUT",
    "1Samuel": "1SA", "1_Samuel": "1SA",
    "2Samuel": "2SA", "2_Samuel": "2SA",
    "1Kings": "1KI", "1_Kings": "1KI",
    "2Kings": "2KI", "2_Kings": "2KI",
    "1Chronicles": "1CH", "2Chronicles": "2CH",
    "Ezra": "EZR", "Nehemiah": "NEH", "Esther": "EST", "Job": "JOB", "Psalms": "PSA",
    "Proverbs": "PRO", "Ecclesiastes": "ECC", "SongofSongs": "SNG", "Isaiah": "ISA",
    "Jeremiah": "JER", "Lamentations": "LAM", "Ezekiel": "EZK", "Daniel": "DAN",
    "Hosea": "HOS", "Joel": "JOL", "Amos": "AMO", "Obadiah": "OBA", "Jonah": "JON",
    "Micah": "MIC", "Nahum": "NAM", "Habakkuk": "HAB", "Zephaniah": "ZEP",
    "Haggai": "HAG", "Zechariah": "ZEC", "Malachi": "MAL",
    "Matthew": "MAT", "Mark": "MRK", "Luke": "LUK", "John": "JHN", "Acts": "ACT",
    "Romans": "ROM", "1Corinthians": "1CO", "2Corinthians": "2CO", "Galatians": "GAL",
    "Ephesians": "EPH", "Philippians": "PHP", "Colossians": "COL",
    "1Thessalonians": "1TH", "1_Thessalonians": "1TH",
    "2Thessalonians": "2TH", "2_Thessalonians": "2TH",
    "1Timothy": "1TI", "2Timothy": "2TI", "Titus": "TIT", "Philemon": "PHM", "Hebrews": "HEB",
    "James": "JAS", "1Peter": "1PE", "2Peter": "2PE",
    "1John": "1JN", "2John": "2JN", "2_John": "2JN",
    "3John": "3JN", "Jude": "JUD",
    "Revelation": "REV", "Revelations": "REV"
}

# OT books
OT_BOOKS = {
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT",
    "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST",
    "JOB", "PSA", "PRO", "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN",
    "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"
}

# TBTA word-level parts (for flattening)
WORD_PARTS = {
    'Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun',
    'Adposition', 'Conjunction', 'Particle', 'Determiner',
    'Numeral', 'Interjection'
}

# TBTA features to extract
TBTA_FEATURES = [
    # Core
    'Part', 'Constituent', 'LexicalSense',
    # Grammatical
    'Number', 'Person', 'Gender', 'Case', 'State',
    'Definiteness', 'Adjective Degree', 'NounListIndex',
    # Verbal
    'Mood', 'Aspect', 'Time', 'Voice', 'Transitivity',
    'Verb Form', 'Verbal Valency',
    # Semantic
    'Polarity', 'Proximity', 'Participant Tracking',
    'Surface Realization', 'SemanticComplexityLevel',
    'Semantic Role', 'Topic NP',
    # Discourse
    'Discourse Genre', 'Illocutionary Force', 'Discourse Function'
]


class MaculaCache:
    """Cache for Macula YAML files to avoid redundant I/O."""

    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def get(self, verse_ref):
        """Get Macula data for verse reference, using cache if available."""
        if verse_ref in self.cache:
            self.hits += 1
            return self.cache[verse_ref]

        self.misses += 1
        macula_data = load_macula_yaml(verse_ref)
        if macula_data:
            self.cache[verse_ref] = macula_data
        return macula_data

    def stats(self):
        """Return cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            'hits': self.hits,
            'misses': self.misses,
            'total': total,
            'hit_rate': f"{hit_rate:.1f}%"
        }


class StrongsAggregator:
    """Aggregates TBTA nodes per Strong's ID with deduplication and verse capping."""

    def __init__(self, max_verses_per_node=100):
        self.max_verses = max_verses_per_node
        # Structure: {strongs_id: {node_key: {attributes, verses}}}
        self.data = defaultdict(lambda: defaultdict(lambda: {
            'attributes': {},
            'verses': []
        }))
        # Track total occurrences for coverage
        self.total_occurrences = Counter()
        self.tbta_coverage = Counter()

    def add_word(self, strongs_id, tbta_attributes, verse_ref):
        """Add a word occurrence with its TBTA attributes."""
        # Filter out null/empty attributes
        attrs = {
            k: v for k, v in tbta_attributes.items()
            if v is not None and v not in ['Not Applicable', 'Unspecified', '.', '']
        }

        # Skip if no meaningful attributes
        if not attrs:
            return

        # Create hashable key for deduplication
        attr_key = frozenset(attrs.items())

        # Initialize node if new
        if attr_key not in self.data[strongs_id]:
            self.data[strongs_id][attr_key]['attributes'] = dict(attrs)

        # Add verse reference (avoid duplicates)
        verses_list = self.data[strongs_id][attr_key]['verses']
        if verse_ref not in verses_list:
            verses_list.append(verse_ref)

            # Cap at max_verses (LRU: keep first N encountered)
            if len(verses_list) > self.max_verses:
                verses_list.pop(0)

        # Track coverage
        self.tbta_coverage[strongs_id] += 1

    def increment_total(self, strongs_id):
        """Increment total occurrence count for a Strong's word."""
        self.total_occurrences[strongs_id] += 1

    def get_strongs_data(self, strongs_id):
        """Get aggregated data for a Strong's word."""
        if strongs_id not in self.data:
            return None

        nodes_list = []
        for node_data in self.data[strongs_id].values():
            node = dict(node_data['attributes'])
            node['verses'] = node_data['verses']
            nodes_list.append(node)

        # Calculate coverage
        total = self.total_occurrences.get(strongs_id, 0)
        coverage = self.tbta_coverage.get(strongs_id, 0)
        coverage_pct = (coverage / total * 100) if total > 0 else 0

        return {
            'strongs_id': strongs_id,
            'coverage': {
                'total_occurrences': total,
                'tbta_coverage': coverage,
                'coverage_pct': round(coverage_pct, 1)
            },
            'nodes': nodes_list
        }

    def get_all_strongs_ids(self):
        """Get all Strong's IDs that have TBTA data."""
        return sorted(self.data.keys())


def clone_tbta_repo():
    """Clone or update TBTA repository from GitHub."""
    if TBTA_LOCAL_PATH.exists():
        logger.info(f"TBTA repo already exists at {TBTA_LOCAL_PATH}")

        # Check if it's a git repo
        if (TBTA_LOCAL_PATH / ".git").exists():
            logger.info("Updating TBTA repo with git pull...")
            try:
                subprocess.run(
                    ["git", "pull"],
                    cwd=TBTA_LOCAL_PATH,
                    check=True,
                    capture_output=True
                )
                logger.info("✓ TBTA repo updated")
            except subprocess.CalledProcessError as e:
                logger.warning(f"Git pull failed: {e}. Continuing with existing data...")
        else:
            logger.warning("Directory exists but is not a git repo. Using existing data...")
    else:
        logger.info(f"Cloning TBTA repo from {TBTA_REPO_URL}...")
        logger.info("This may take a few minutes (shallow clone)...")

        try:
            subprocess.run(
                ["git", "clone", "--depth=1", TBTA_REPO_URL, str(TBTA_LOCAL_PATH)],
                check=True,
                capture_output=True
            )
            logger.info("✓ TBTA repo cloned successfully")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to clone TBTA repo: {e}")
            logger.error("Please clone manually: git clone --depth=1 " + TBTA_REPO_URL)
            sys.exit(1)

    # Verify JSON directory exists
    if not TBTA_JSON_DIR.exists():
        logger.error(f"JSON directory not found: {TBTA_JSON_DIR}")
        sys.exit(1)

    logger.info(f"Using TBTA data from: {TBTA_JSON_DIR}")


def get_tbta_commit_hash():
    """Get current git commit hash from TBTA repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=TBTA_LOCAL_PATH,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()[:7]  # Short hash
    except:
        return "unknown"


def parse_tbta_filename(filename):
    """
    Parse TBTA filename like '00_001_001_Genesis.json'.

    Returns:
        tuple: (book_code, chapter, verse) or (None, None, None) if invalid
    """
    match = re.match(r'(\d+)_(\d+)_(\d+)_([^.]+)\.json', filename)
    if not match:
        return None, None, None

    chapter = int(match.group(2))
    verse = int(match.group(3))
    book_name = match.group(4)

    # Get USFM book code
    book_code = BOOK_NAME_MAP.get(book_name)
    if not book_code:
        logger.warning(f"Unknown book name: {book_name}")
        return None, None, None

    return book_code, chapter, verse


def flatten_tbta_tree(tbta_data):
    """
    Flatten hierarchical TBTA structure to sequential word list.

    Uses depth-first traversal to collect leaf nodes (word-level parts)
    while preserving document order (left-to-right).

    Args:
        tbta_data: TBTA JSON data (list of clauses or single clause dict)

    Returns:
        list: Word-level nodes with TBTA attributes
    """
    words = []

    def traverse(node):
        """Recursive DFS traversal."""
        if not isinstance(node, dict):
            return

        # Check if this is a word-level node
        if node.get('Part') in WORD_PARTS:
            words.append(node)
            # Don't recurse further (leaf node)
            return

        # Recurse into children (preserves left-to-right order)
        if 'Children' in node and isinstance(node['Children'], list):
            for child in node['Children']:
                traverse(child)

    # Process all top-level clauses
    if isinstance(tbta_data, list):
        for clause in tbta_data:
            traverse(clause)
    elif isinstance(tbta_data, dict):
        traverse(tbta_data)

    return words


def load_macula_yaml(verse_ref):
    """
    Load Macula YAML file for a verse reference.

    Args:
        verse_ref: Verse reference like "GEN.001.001"

    Returns:
        dict: Macula data or None if not found
    """
    # Parse verse reference
    match = re.match(r'([A-Z0-9]{3})\.(\d{3})\.(\d{3})', verse_ref)
    if not match:
        return None

    book = match.group(1)
    chapter = int(match.group(2))
    verse = int(match.group(3))

    # Construct Macula file path
    macula_path = (
        COMMENTARY_DIR / book / f"{chapter:03d}" /
        f"{book}-{chapter:03d}-{verse:03d}-macula.yaml"
    )

    if not macula_path.exists():
        return None

    # Load YAML
    try:
        with open(macula_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load Macula file {macula_path}: {e}")
        return None


def extract_strongs_from_macula(macula_word, language):
    """
    Extract Strong's number from Macula word data.

    Args:
        macula_word: Macula word dict
        language: 'heb' or 'grc'

    Returns:
        str: Strong's ID like "G2316" or "H7225", or None
    """
    try:
        # Get Strong's number from lexical.strong field
        strong_num = macula_word.get('lexical', {}).get('strong')
        if not strong_num:
            return None

        # Format with prefix
        prefix = 'G' if language == 'grc' else 'H'
        return f"{prefix}{int(strong_num):04d}"

    except (ValueError, TypeError):
        return None


def extract_tbta_attributes(tbta_word):
    """
    Extract TBTA features from word node.

    Args:
        tbta_word: TBTA word dict

    Returns:
        dict: Normalized TBTA attributes
    """
    attributes = {}

    for feature in TBTA_FEATURES:
        if feature in tbta_word:
            value = normalize_attribute_value(tbta_word[feature])
            if value:
                attributes[feature] = value

    return attributes


def normalize_attribute_value(value):
    """
    Normalize TBTA attribute values for consistency.

    Rules:
    1. Trim whitespace
    2. Preserve original capitalization (TBTA standard)
    3. Collapse multiple spaces to single space
    4. Convert null variants to None

    Args:
        value: Raw attribute value

    Returns:
        str or None: Normalized value
    """
    if value is None:
        return None

    value = str(value).strip()

    # Null variants
    if value in ['', '.', 'Not Applicable', 'Unspecified']:
        return None

    # Collapse whitespace
    value = ' '.join(value.split())

    return value


def align_words(tbta_words, macula_words):
    """
    Align TBTA words with Macula words by position.

    Args:
        tbta_words: List of TBTA word dicts
        macula_words: List of Macula word dicts

    Returns:
        list: Tuples of (tbta_word, macula_word)
    """
    if len(tbta_words) != len(macula_words):
        # Log alignment mismatch
        min_len = min(len(tbta_words), len(macula_words))
        logger.debug(
            f"Alignment mismatch: TBTA={len(tbta_words)} Macula={len(macula_words)}, "
            f"aligning first {min_len} words"
        )
        return list(zip(tbta_words[:min_len], macula_words[:min_len]))

    return list(zip(tbta_words, macula_words))


def process_verse(verse_ref, tbta_data, macula_cache, aggregator):
    """
    Process a single verse: link TBTA → Macula → Strong's.

    Args:
        verse_ref: Verse reference like "GEN.001.001"
        tbta_data: TBTA JSON data
        macula_cache: MaculaCache instance
        aggregator: StrongsAggregator instance

    Returns:
        dict: Statistics (words_processed, strongs_found, etc.)
    """
    stats = {
        'words_processed': 0,
        'strongs_found': 0,
        'alignment_mismatches': 0
    }

    # Load Macula data
    macula_data = macula_cache.get(verse_ref)
    if not macula_data:
        logger.debug(f"No Macula data for {verse_ref}")
        return stats

    # Flatten TBTA tree
    tbta_words = flatten_tbta_tree(tbta_data)
    if not tbta_words:
        return stats

    # Get Macula words
    macula_words = macula_data.get('words', [])
    if not macula_words:
        return stats

    # Get language
    language = macula_data.get('language', 'grc')

    # Align words
    aligned = align_words(tbta_words, macula_words)
    if len(tbta_words) != len(macula_words):
        stats['alignment_mismatches'] = 1

    # Process aligned words
    for tbta_word, macula_word in aligned:
        stats['words_processed'] += 1

        # Extract Strong's number
        strongs_id = extract_strongs_from_macula(macula_word, language)
        if not strongs_id:
            continue

        stats['strongs_found'] += 1

        # Track total occurrences (for coverage calculation)
        aggregator.increment_total(strongs_id)

        # Extract TBTA attributes
        tbta_attributes = extract_tbta_attributes(tbta_word)
        if not tbta_attributes:
            continue

        # Add to aggregator
        aggregator.add_word(strongs_id, tbta_attributes, verse_ref)

    return stats


def write_strongs_yaml(strongs_id, strongs_data, output_dir, dry_run=False):
    """
    Write YAML file for a Strong's word.

    Args:
        strongs_id: Strong's ID like "G2316"
        strongs_data: Aggregated data dict
        output_dir: Output directory path
        dry_run: If True, don't write file

    Returns:
        Path: Output file path
    """
    # Construct output path
    output_path = output_dir / strongs_id / f"{strongs_id}-tbta.yaml"

    if dry_run:
        return output_path

    # Create directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Add extraction metadata
    output_data = {
        'strongs_id': strongs_data['strongs_id'],
        'coverage': strongs_data['coverage'],
        'extraction': {
            'date': datetime.utcnow().isoformat() + 'Z',
            'tbta_commit': get_tbta_commit_hash(),
            'script_version': '1.0.0'
        },
        'nodes': strongs_data['nodes']
    }

    # Write YAML
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(
                output_data,
                f,
                default_flow_style=False,
                allow_unicode=True,
                sort_keys=False
            )
    except Exception as e:
        logger.error(f"Failed to write {output_path}: {e}")
        return None

    return output_path


def extract_all_verses(testament_filter=None, book_filter=None, dry_run=False):
    """
    Extract TBTA nodes for all verses and aggregate by Strong's ID.

    Args:
        testament_filter: 'OT' or 'NT' to filter by testament
        book_filter: Book code like 'JHN' to process only one book
        dry_run: If True, don't write output files

    Returns:
        dict: Extraction statistics
    """
    logger.info("=" * 60)
    logger.info("TBTA-to-Strong's Extraction")
    logger.info("=" * 60)
    if testament_filter:
        logger.info(f"Testament filter: {testament_filter}")
    if book_filter:
        logger.info(f"Book filter: {book_filter}")
    if dry_run:
        logger.info("DRY RUN MODE - No output files will be written")
    logger.info("=" * 60)

    # Initialize
    macula_cache = MaculaCache()
    aggregator = StrongsAggregator(max_verses_per_node=100)

    # Get all TBTA JSON files
    json_files = sorted(TBTA_JSON_DIR.glob("*.json"))
    logger.info(f"Found {len(json_files)} TBTA verse files")

    # Statistics
    total_stats = {
        'verses_processed': 0,
        'verses_with_tbta': 0,
        'verses_with_macula': 0,
        'verses_linked': 0,
        'words_processed': 0,
        'strongs_found': 0,
        'alignment_mismatches': 0
    }

    # Process files
    for i, json_file in enumerate(json_files, 1):
        # Parse filename
        book_code, chapter, verse = parse_tbta_filename(json_file.name)
        if not book_code:
            continue

        # Apply filters
        if testament_filter:
            is_ot = book_code in OT_BOOKS
            if testament_filter == 'OT' and not is_ot:
                continue
            if testament_filter == 'NT' and is_ot:
                continue

        if book_filter and book_code != book_filter:
            continue

        # Create verse reference
        verse_ref = f"{book_code}.{chapter:03d}.{verse:03d}"

        # Load TBTA data
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                tbta_data = json.load(f)
        except Exception as e:
            logger.error(f"Failed to parse {json_file.name}: {e}")
            continue

        total_stats['verses_processed'] += 1
        total_stats['verses_with_tbta'] += 1

        # Process verse
        verse_stats = process_verse(verse_ref, tbta_data, macula_cache, aggregator)

        # Update statistics
        if verse_stats['words_processed'] > 0:
            total_stats['verses_with_macula'] += 1
        if verse_stats['strongs_found'] > 0:
            total_stats['verses_linked'] += 1

        total_stats['words_processed'] += verse_stats['words_processed']
        total_stats['strongs_found'] += verse_stats['strongs_found']
        total_stats['alignment_mismatches'] += verse_stats['alignment_mismatches']

        # Progress logging
        if i % 1000 == 0:
            logger.info(f"  Processed {i} verses...")

    logger.info(f"✓ Processed {total_stats['verses_processed']} verses")

    # Summary statistics
    logger.info("=" * 60)
    logger.info("EXTRACTION SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Verses processed: {total_stats['verses_processed']}")
    logger.info(f"Verses with TBTA data: {total_stats['verses_with_tbta']}")
    logger.info(f"Verses with Macula data: {total_stats['verses_with_macula']}")
    logger.info(f"Verses successfully linked: {total_stats['verses_linked']}")
    logger.info(f"Words processed: {total_stats['words_processed']}")
    logger.info(f"Strong's numbers found: {total_stats['strongs_found']}")
    logger.info(f"Alignment mismatches: {total_stats['alignment_mismatches']}")

    # Macula cache stats
    cache_stats = macula_cache.stats()
    logger.info(f"Macula cache hit rate: {cache_stats['hit_rate']}")

    # Write output files
    strongs_ids = aggregator.get_all_strongs_ids()
    logger.info(f"Unique Strong's words with TBTA data: {len(strongs_ids)}")

    if not dry_run:
        logger.info("=" * 60)
        logger.info("WRITING OUTPUT FILES")
        logger.info("=" * 60)

        files_written = 0
        for i, strongs_id in enumerate(strongs_ids, 1):
            strongs_data = aggregator.get_strongs_data(strongs_id)
            if not strongs_data:
                continue

            output_path = write_strongs_yaml(
                strongs_id,
                strongs_data,
                STRONGS_DIR,
                dry_run=dry_run
            )

            if output_path:
                files_written += 1

            if i % 100 == 0:
                logger.info(f"  Written {i} files...")

        logger.info(f"✓ Written {files_written} YAML files to {STRONGS_DIR}")
    else:
        logger.info("DRY RUN - No files written")

    logger.info("=" * 60)
    logger.info("EXTRACTION COMPLETE")
    logger.info("=" * 60)

    return {
        'total_stats': total_stats,
        'cache_stats': cache_stats,
        'strongs_count': len(strongs_ids)
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract TBTA nodes for Strong's words",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extract_tbta_nodes.py
  python extract_tbta_nodes.py --testament NT
  python extract_tbta_nodes.py --book JHN
  python extract_tbta_nodes.py --dry-run
        """
    )

    parser.add_argument(
        "--testament",
        choices=['OT', 'NT'],
        help="Filter by testament (OT or NT)"
    )
    parser.add_argument(
        "--book",
        help="Filter by book code (e.g., JHN, GEN)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show statistics without writing output files"
    )

    args = parser.parse_args()

    # Verify data directory exists
    if not DATA_DIR.exists():
        logger.error(f"Data directory not found: {DATA_DIR}")
        logger.error("Run setup-minimal-data.sh first")
        sys.exit(1)

    # Clone/update TBTA repo
    clone_tbta_repo()

    # Extract all verses
    results = extract_all_verses(
        testament_filter=args.testament,
        book_filter=args.book,
        dry_run=args.dry_run
    )

    logger.info("Extraction complete!")


if __name__ == "__main__":
    main()
