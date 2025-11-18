#!/usr/bin/env python3
"""
TBTA Feature Extraction Script
================================

Extracts feature values from TBTA dataset for STAGES.md Step 4.

Usage:
    python extract_feature.py --field Clusivity
    python extract_feature.py --field Mood --max-per-value 500
    python extract_feature.py --field Participant --output data.yaml

Features:
- Downloads fresh TBTA data from GitHub
- Extracts all verses for a given feature field
- Counts distribution across OT/NT and books
- LRU cache to cap verses per value (default: 2000)
- Outputs simplified YAML for LLM processing

Output format matches STAGES.md Step 4 requirements (simplified version).
LLM will add genre/difficulty/notes in subsequent step.
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

# Book name to USFM code mapping (from tbta_processor.py)
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

# OT books (for testament distribution counting)
OT_BOOKS = {
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT",
    "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST",
    "JOB", "PSA", "PRO", "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN",
    "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"
}


class LRUCache:
    """LRU cache for capping verses per value."""

    def __init__(self, max_size=2000):
        self.cache = OrderedDict()
        self.max_size = max_size

    def add(self, value, verse_ref):
        """Add verse to value's list, maintaining LRU cap."""
        if value not in self.cache:
            self.cache[value] = []

        # Add verse
        self.cache[value].append(verse_ref)

        # Trim if over max_size (FIFO within value)
        if len(self.cache[value]) > self.max_size:
            self.cache[value].pop(0)

    def get(self, value):
        """Get all verses for a value."""
        return self.cache.get(value, [])

    def values(self):
        """Get all values."""
        return self.cache.keys()


def clone_tbta_repo():
    """Clone or update TBTA repository."""
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


def get_git_commit_hash():
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


def parse_filename(filename):
    """
    Parse TBTA filename like '00_001_001_Genesis.json'
    Returns (book_name, chapter, verse) tuple
    """
    import re
    match = re.match(r'(\d+)_(\d+)_(\d+)_([^.]+)\.json', filename)
    if match:
        chapter = int(match.group(2))
        verse = int(match.group(3))
        book_name = match.group(4)
        return book_name, chapter, verse
    return None, None, None


def extract_field_from_clause(clause_data, field_name):
    """
    Recursively search for field in clause tree.
    Returns list of values found (can be multiple in nested clauses).
    """
    values = []

    if not isinstance(clause_data, dict):
        return values

    # Check if field exists at this level
    if field_name in clause_data:
        value = clause_data[field_name]
        # Filter out nullish values
        if value and value not in ["Not Applicable", "Unspecified", "."]:
            values.append(value)

    # Recurse into Children
    if "Children" in clause_data and isinstance(clause_data["Children"], list):
        for child in clause_data["Children"]:
            values.extend(extract_field_from_clause(child, field_name))

    return values


def process_json_file(json_file, field_name):
    """
    Process a single TBTA JSON file.
    Returns list of (book_code, chapter, verse, value) tuples.
    """
    book_name, chapter, verse = parse_filename(json_file.name)

    if not book_name:
        return []

    # Get USFM book code
    book_code = BOOK_NAME_MAP.get(book_name)
    if not book_code:
        logger.warning(f"Unknown book name: {book_name}")
        return []

    # Load JSON
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            tbta_data = json.load(f)
    except Exception as e:
        logger.error(f"Failed to parse {json_file.name}: {e}")
        return []

    # Extract field values
    values = []

    if isinstance(tbta_data, list):
        for clause in tbta_data:
            values.extend(extract_field_from_clause(clause, field_name))
    elif isinstance(tbta_data, dict):
        values.extend(extract_field_from_clause(tbta_data, field_name))

    # Return tuples for each value found
    results = []
    for value in values:
        results.append((book_code, chapter, verse, value))

    return results


def extract_feature(field_name, max_per_value=2000, dry_run=False):
    """
    Extract all verses for a given feature field from TBTA data.

    Returns dict with:
    - feature: field name
    - extracted: timestamp
    - tbta_commit: git commit hash
    - max_per_value: LRU cache size
    - value: list of value data
    """
    logger.info("=" * 60)
    logger.info(f"Extracting feature: {field_name}")
    logger.info(f"Max verses per value: {max_per_value}")
    if dry_run:
        logger.info("DRY RUN MODE - No output file will be written")
    logger.info("=" * 60)

    # Initialize data structures
    lru_cache = LRUCache(max_per_value)
    total_counts = Counter()  # Overall counts (not limited by LRU)
    book_counts = defaultdict(Counter)  # Per-book counts per value
    ot_counts = Counter()  # OT counts per value
    nt_counts = Counter()  # NT counts per value

    # Get all JSON files
    json_files = sorted(TBTA_JSON_DIR.glob("*.json"))
    logger.info(f"Found {len(json_files)} TBTA verse files")

    # Process files
    processed = 0
    for json_file in json_files:
        results = process_json_file(json_file, field_name)

        for book_code, chapter, verse, value in results:
            # Create verse reference
            verse_ref = f"{book_code}.{chapter:03d}.{verse:03d}"

            # Update counts (always count, regardless of LRU)
            total_counts[value] += 1
            book_counts[value][book_code] += 1

            # Testament counts
            if book_code in OT_BOOKS:
                ot_counts[value] += 1
            else:
                nt_counts[value] += 1

            # Add to LRU cache
            lru_cache.add(value, verse_ref)

        processed += 1
        if processed % 1000 == 0:
            logger.info(f"  Processed {processed} files...")

    logger.info(f"✓ Processed {processed} files")

    # Build output structure
    feature_data = {
        "feature": field_name.lower(),
        "extracted": datetime.utcnow().isoformat() + "Z",
        "tbta_commit": get_git_commit_hash(),
        "max_per_value": max_per_value,
        "value": []
    }

    # Add data for each value
    for value in sorted(lru_cache.values()):
        value_data = {
            "specific_value": value,
            "total_verses": total_counts[value],
            "distribution": {
                "OT": ot_counts[value],
                "NT": nt_counts[value],
                "Books": dict(book_counts[value])
            },
            "verses": lru_cache.get(value)
        }
        feature_data["value"].append(value_data)

    # Summary
    logger.info("=" * 60)
    logger.info("EXTRACTION SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Feature: {field_name}")
    logger.info(f"Total values found: {len(feature_data['value'])}")

    for value_data in feature_data["value"]:
        value = value_data["specific_value"]
        total = value_data["total_verses"]
        cached = len(value_data["verses"])
        ot = value_data["distribution"]["OT"]
        nt = value_data["distribution"]["NT"]

        logger.info(f"  {value}:")
        logger.info(f"    Total verses: {total}")
        logger.info(f"    Cached verses: {cached} (OT: {ot}, NT: {nt})")
        if cached < total:
            logger.info(f"    ⚠ Truncated by LRU (showing first {cached} of {total})")

    logger.info("=" * 60)

    return feature_data


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract feature values from TBTA dataset",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python extract_feature.py --field Clusivity
  python extract_feature.py --field Mood --max-per-value 500
  python extract_feature.py --field Participant --output data.yaml --dry-run
        """
    )

    parser.add_argument(
        "--field",
        required=True,
        help="TBTA field name (e.g., Clusivity, Mood, Participant)"
    )
    parser.add_argument(
        "--max-per-value",
        type=int,
        default=2000,
        help="Maximum verses per value (LRU cache size, default: 2000)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show statistics without writing output"
    )

    args = parser.parse_args()

    # Clone/update TBTA repo
    clone_tbta_repo()

    # Extract feature
    feature_data = extract_feature(
        args.field,
        max_per_value=args.max_per_value,
        dry_run=args.dry_run
    )

    # Output
    if not args.dry_run:
        yaml_output = yaml.dump(
            feature_data,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False
        )

        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(yaml_output)
            logger.info(f"✓ Output written to: {args.output}")
        else:
            print("\n" + yaml_output)


if __name__ == "__main__":
    main()
