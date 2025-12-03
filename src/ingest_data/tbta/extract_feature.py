#!/usr/bin/env python3
"""
TBTA Feature Extraction Script
================================

Unified script for extracting feature values from TBTA dataset.
Supports both YAML output (for STAGES.md workflow) and JSONL output (for ML pipelines).

Usage:
    # Extract to YAML (default, for STAGES.md Step 4)
    python extract_feature.py --field Clusivity
    python extract_feature.py --field Mood --max-per-value 500 --output data.yaml

    # Extract to JSONL (for ML training pipelines)
    python extract_feature.py --field Number --format jsonl --output data.jsonl
    python extract_feature.py --source-dir /path/to/tbta --field Person --format jsonl

    # Extract with reconstructed text (shows clause with highlighted word)
    python extract_feature.py --field Number --format jsonl --with-text --output data.jsonl

    # Extract with Strong's codes from macula dataset
    python extract_feature.py --field Number --format jsonl --with-strongs --output data.jsonl

Features:
- Downloads fresh TBTA data from GitHub (or use custom --source-dir)
- Extracts all verses for a given feature field
- Multiple output formats: YAML (summary), JSONL (detailed)
- Counts distribution across OT/NT and books
- LRU cache to cap verses per value (default: 2000)
- Hierarchical path tracking for detailed analysis

Output Formats:
1. YAML: Simplified summary format for STAGES.md Step 4
   - Feature metadata and distribution statistics
   - Limited verses per value (LRU cached)

2. JSONL: Detailed format for ML pipelines
   - One annotation per line
   - Fields: verse, label, constituent, part, path
   - With --with-text: adds 'text' field with reconstructed clause
     Example: "then **God** say now God create person"
     (word with extracted feature wrapped in **)
   - With --with-strongs: adds 'strongs' field with Strong's codes and glosses from macula
     Example: "G3972-Paul G0652-an_apostle G5547-of_Christ G2424-Jesus..."
     (H prefix for OT, G prefix for NT, 4-digit zero-padded, gloss with underscores)
   - All occurrences included (no LRU limit)
"""

import argparse
import json
import logging
import os
import subprocess
import sys
from collections import Counter, OrderedDict, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("WARNING: PyYAML not installed. YAML output will be unavailable.")
    print("Install with: pip install pyyaml")
    exit(1)

# Add src to path for imports when run as script
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from config import DATA_DIR
    from util.cache import get_cached_verse
    MACULA_AVAILABLE = True
except ImportError:
    MACULA_AVAILABLE = False
    DATA_DIR = None

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


def get_strongs_from_macula(book_code: str, chapter: int, verse: int) -> str:
    """
    Get Strong's codes with glosses from macula data for a verse.
    
    Args:
        book_code: USFM book code (e.g., "MAT", "GEN")
        chapter: Chapter number
        verse: Verse number
        
    Returns:
        Space-separated Strong's codes formatted as (H|G)####-gloss
        Example: "G3972-Paul G0652-an_apostle G5547-of_Christ"
        Returns empty string if macula data not available
    """
    if not MACULA_AVAILABLE or DATA_DIR is None:
        return ""
    
    try:
        # Get macula data from cache
        cache_root = Path(DATA_DIR) / "commentary"
        logger.debug(f"Fetching macula for {book_code} {chapter}:{verse} from {cache_root}")
        
        macula_data = get_cached_verse(
            book_code, chapter, verse,
            suffix="macula",
            cache_root=cache_root
        )
        
        if not macula_data:
            logger.warning(f"No macula data found for {book_code} {chapter}:{verse}")
            return ""
            
        if 'words' not in macula_data:
            logger.warning(f"No 'words' key in macula data for {book_code} {chapter}:{verse}")
            return ""
        
        # Determine prefix based on testament (H for Hebrew/OT, G for Greek/NT)
        prefix = "H" if book_code in OT_BOOKS else "G"
        
        # Extract Strong's codes with glosses from words
        strongs_entries = []
        for word in macula_data.get('words', []):
            lexical = word.get('lexical', {})
            strong = lexical.get('strong')
            if strong:
                # Get gloss from translation
                translation = word.get('translation', {})
                gloss = translation.get('gloss', '')
                
                # Format as (H|G) + 4-digit zero-padded number
                try:
                    strong_num = int(strong)
                    code = f"{prefix}{strong_num:04d}"
                except (ValueError, TypeError):
                    # Handle cases where strong isn't a pure number
                    code = f"{prefix}{strong}"
                
                # Combine code with gloss (replace spaces with underscores)
                if gloss:
                    gloss_clean = gloss.replace(' ', '_')
                    strongs_entries.append(f"{code}-{gloss_clean}")
                else:
                    strongs_entries.append(code)
        
        return " ".join(strongs_entries)
        
    except Exception as e:
        logger.debug(f"Could not get macula data for {book_code} {chapter}:{verse}: {e}")
        return ""


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
    Parse TBTA filename.

    Handles two formats:
    1. GitHub format: '00_001_001_Genesis.json'
    2. Standard format: 'GEN-001-001.json' or 'BOOK-CCC-VVV.json'

    Returns (book_code, chapter, verse) tuple
    """
    import re

    # Try GitHub format first: 00_001_001_Genesis.json
    match = re.match(r'(\d+)_(\d+)_(\d+)_([^.]+)\.json', filename)
    if match:
        chapter = int(match.group(2))
        verse = int(match.group(3))
        book_name = match.group(4)
        book_code = BOOK_NAME_MAP.get(book_name)
        if book_code:
            return book_code, chapter, verse

    # Try standard format: GEN-001-001.json
    match = re.match(r'([A-Z0-9]+)-(\d+)-(\d+)\.json', filename)
    if match:
        book_code = match.group(1)
        chapter = int(match.group(2))
        verse = int(match.group(3))
        return book_code, chapter, verse

    return None, None, None


def extract_field_from_clause(clause_data, field_name, results=None, path=""):
    """
    Recursively search for field in clause tree.

    Args:
        clause_data: TBTA clause dictionary
        field_name: Field to extract (e.g., 'Number', 'Person')
        results: Accumulator list (internal)
        path: Hierarchical path for tracking location

    Returns:
        List of dicts with keys: value, constituent, part, path
    """
    if results is None:
        results = []

    if not isinstance(clause_data, dict):
        return results

    # Extract current element data
    constituent = clause_data.get('Constituent', '')
    value = clause_data.get(field_name, '')
    part = clause_data.get('Part', '')

    # Check if field exists at this level and has meaningful value
    if value and value not in ["Not Applicable", "Unspecified", "."]:
        results.append({
            'value': value,
            'constituent': constituent,
            'part': part,
            'path': path
        })

    # Recurse into Children (handle both "Children" and "children" keys)
    children = clause_data.get("Children") or clause_data.get("children") or []
    if isinstance(children, list):
        for i, child in enumerate(children):
            # Build hierarchical path
            child_path = f"{path}/{part}[{i}]" if path else f"{part}[{i}]"
            extract_field_from_clause(child, field_name, results, child_path)

    return results


def extract_tokens_with_paths(clause_data, tokens=None, path=""):
    """
    Extract all word tokens from a clause with their paths.

    Walks the clause tree in document order, collecting Constituent values
    (the semantic words) along with their paths for later highlighting.

    Args:
        clause_data: TBTA clause dictionary
        tokens: Accumulator list (internal)
        path: Current path in tree (matching extract_field_from_clause format)

    Returns:
        List of (token, path) tuples in document order
    """
    if tokens is None:
        tokens = []

    if not isinstance(clause_data, dict):
        return tokens

    constituent = clause_data.get('Constituent', '')
    part = clause_data.get('Part', '')

    # Add token if it's a real word:
    # - Has a Constituent value
    # - Not a marker (like -QuoteBegin, -QuoteEnd)
    # - Not a Space or Period
    skip_parts = {'Space', 'Period'}
    if constituent and not constituent.startswith('-') and part not in skip_parts:
        tokens.append((constituent, path))

    # Recurse into Children (using same path-building logic as extract_field_from_clause)
    children = clause_data.get("Children") or clause_data.get("children") or []
    if isinstance(children, list):
        for i, child in enumerate(children):
            child_path = f"{path}/{part}[{i}]" if path else f"{part}[{i}]"
            extract_tokens_with_paths(child, tokens, child_path)

    return tokens


def build_highlighted_text(tokens_with_paths, highlight_path):
    """
    Build readable text from tokens, highlighting the one at highlight_path.

    Args:
        tokens_with_paths: List of (token, path) tuples from extract_tokens_with_paths
        highlight_path: Path of the token to wrap in **

    Returns:
        String with reconstructed clause text, target word wrapped in **
    """
    result = []
    for token, path in tokens_with_paths:
        if path == highlight_path:
            result.append(f"**{token}**")
        else:
            result.append(token)
    return " ".join(result)


def process_json_file(json_file, field_name, output_format='yaml', with_text=False, with_strongs=False):
    """
    Process a single TBTA JSON file.

    Args:
        json_file: Path to JSON file
        field_name: TBTA field to extract
        output_format: 'yaml' or 'jsonl'
        with_text: Include reconstructed clause text with highlighting (JSONL only)
        with_strongs: Include Strong's codes from macula dataset (JSONL only)

    Returns:
        For 'yaml': list of (book_code, chapter, verse, value) tuples
        For 'jsonl': list of annotation dicts with verse references
    """
    book_code, chapter, verse = parse_filename(json_file.name)

    if not book_code:
        logger.warning(f"Cannot parse filename: {json_file.name}")
        return []

    # Load JSON
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            tbta_data = json.load(f)
    except Exception as e:
        logger.error(f"Failed to parse {json_file.name}: {e}")
        return []

    # Handle both list and dict structures
    clauses = tbta_data if isinstance(tbta_data, list) else [tbta_data]

    results = []
    
    # Get Strong's codes once per verse (shared across all annotations in this verse)
    strongs_codes = ""
    if output_format == 'jsonl' and with_strongs:
        strongs_codes = get_strongs_from_macula(book_code, chapter, verse)
        if not strongs_codes:
            logger.warning(f"Empty strongs codes for {book_code} {chapter}:{verse}")


    for clause_idx, clause in enumerate(clauses):
        try:
            # Build path prefix for this clause
            clause_path = f"Clause[{clause_idx}]"

            # Extract tokens for text reconstruction (JSONL with text only)
            tokens_with_paths = None
            if output_format == 'jsonl' and with_text:
                tokens_with_paths = extract_tokens_with_paths(clause, path=clause_path)

            # Extract features from this clause
            annotations = extract_field_from_clause(clause, field_name, path=clause_path)

            # Format based on output type
            if output_format == 'jsonl':
                # JSONL format: detailed annotations with verse reference
                verse_ref = f"{book_code}-{chapter:03d}-{verse:03d}"
                for ann in annotations:
                    result = {
                        'verse': verse_ref,
                        'label': ann['value'],
                        'constituent': ann['constituent'],
                        'part': ann['part'],
                        'path': ann['path']
                    }
                    # Add reconstructed text with highlighted word
                    if with_text and tokens_with_paths:
                        result['text'] = build_highlighted_text(tokens_with_paths, ann['path'])
                    # Add Strong's codes from macula
                    if with_strongs and strongs_codes:
                        result['strongs'] = strongs_codes
                    results.append(result)
            else:
                # YAML format: simple tuples for aggregation
                for ann in annotations:
                    results.append((book_code, chapter, verse, ann['value']))

        except Exception as e:
            logger.warning(f"Error processing clause {clause_idx} in {json_file.name}: {e}")
            continue

    return results


def extract_feature(field_name, source_dir=None, max_per_value=2000, output_format='yaml', dry_run=False, with_text=False, with_strongs=False, limit=None):
    """
    Extract all verses for a given feature field from TBTA data.

    Args:
        field_name: TBTA field to extract
        source_dir: Custom source directory (or None to use default TBTA repo)
        max_per_value: LRU cache size (YAML format only)
        output_format: 'yaml' or 'jsonl'
        dry_run: Show stats without writing output
        with_text: Include reconstructed clause text with highlighting (JSONL only)
        with_strongs: Include Strong's codes from macula dataset (JSONL only)
        limit: Maximum number of files to process (for testing)

    Returns:
        For 'yaml': dict with feature metadata and aggregated data
        For 'jsonl': list of annotation dicts
    """
    logger.info("=" * 60)
    logger.info(f"Extracting feature: {field_name}")
    logger.info(f"Output format: {output_format}")
    if output_format == 'yaml':
        logger.info(f"Max verses per value: {max_per_value}")
    if output_format == 'jsonl' and with_text:
        logger.info("Including reconstructed text with highlighting")
    if output_format == 'jsonl' and with_strongs:
        logger.info("Including Strong's codes from macula dataset")
    if limit:
        logger.info(f"Limiting processing to {limit} files")
    if dry_run:
        logger.info("DRY RUN MODE - No output file will be written")
    logger.info("=" * 60)

    # Determine source directory
    if source_dir:
        json_dir = Path(source_dir)
        if not json_dir.exists():
            logger.error(f"Source directory not found: {json_dir}")
            sys.exit(1)
    else:
        # Use default TBTA repo
        clone_tbta_repo()
        json_dir = TBTA_JSON_DIR

    # Get all JSON files
    json_files = sorted(json_dir.rglob("*.json"))
    logger.info(f"Found {len(json_files)} TBTA verse files")

    if len(json_files) == 0:
        logger.error(f"No JSON files found in {json_dir}")
        sys.exit(1)

    # Initialize data structures based on format
    if output_format == 'yaml':
        # YAML: aggregated format with LRU caching
        lru_cache = LRUCache(max_per_value)
        total_counts = Counter()
        book_counts = defaultdict(Counter)
        ot_counts = Counter()
        nt_counts = Counter()

        # Process files
        processed = 0
        for json_file in json_files:
            if limit and processed >= limit:
                break

            results = process_json_file(json_file, field_name, output_format='yaml')

            for book_code, chapter, verse, value in results:
                verse_ref = f"{book_code}.{chapter:03d}.{verse:03d}"

                # Update counts
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
            "tbta_commit": get_git_commit_hash() if not source_dir else "custom",
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

    else:
        # JSONL: detailed format with all annotations
        all_annotations = []
        error_count = 0
        file_count = 0

        total_files = len(json_files)

        for idx, json_file in enumerate(json_files, 1):
            if limit and (idx - 1) >= limit:
                break

            # Progress indicator
            if idx % 100 == 0 or idx == total_files:
                logger.info(f"Processing: {idx}/{total_files} files ({idx*100//total_files}%)")

            try:
                results = process_json_file(json_file, field_name, output_format='jsonl', with_text=with_text, with_strongs=with_strongs)
                all_annotations.extend(results)
                file_count += 1
            except Exception as e:
                error_count += 1
                logger.error(f"Failed to process {json_file}: {e}")
                continue

        # Summary statistics
        logger.info("=" * 60)
        logger.info("EXTRACTION COMPLETE")
        logger.info("=" * 60)
        logger.info(f"Files processed successfully: {file_count}/{total_files}")
        logger.info(f"Files with errors: {error_count}")
        logger.info(f"Total annotations extracted: {len(all_annotations)}")

        # Calculate label distribution
        if all_annotations:
            stats = defaultdict(int)
            for result in all_annotations:
                stats[result['label']] += 1

            logger.info("\nLabel distribution:")
            for label, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
                logger.info(f"  {label}: {count}")

        logger.info("=" * 60)

        return all_annotations


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Extract feature values from TBTA dataset",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract to YAML (for STAGES.md workflow)
  python extract_feature.py --field Clusivity
  python extract_feature.py --field Mood --max-per-value 500 --output mood.yaml

  # Extract to JSONL (for ML pipelines)
  python extract_feature.py --field Number --format jsonl --output number.jsonl
  python extract_feature.py --field Person --format jsonl --source-dir /path/to/tbta
  python extract_feature.py --field Number --format jsonl --limit 100 --output sample.jsonl

  # Dry run to see statistics
  python extract_feature.py --field Gender --dry-run
        """
    )

    parser.add_argument(
        "--field",
        required=True,
        help="TBTA field name (e.g., Clusivity, Mood, Number, Person, Gender, Tense)"
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        help="TBTA source directory containing JSON files (default: auto-clone from GitHub)"
    )
    parser.add_argument(
        "--format",
        choices=['yaml', 'jsonl'],
        default='yaml',
        help="Output format: 'yaml' (summary) or 'jsonl' (detailed, default: yaml)"
    )
    parser.add_argument(
        "--max-per-value",
        type=int,
        default=2000,
        help="Maximum verses per value for YAML format (LRU cache size, default: 2000)"
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
    parser.add_argument(
        "--with-text",
        action="store_true",
        help="Include reconstructed clause text with highlighted word (JSONL only)"
    )
    parser.add_argument(
        "--with-strongs",
        action="store_true",
        help="Include Strong's codes from macula dataset (JSONL only, requires .data/commentary)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of files to process (for testing)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Validate YAML dependency
    if args.format == 'yaml' and yaml is None and not args.dry_run:
        logger.error("PyYAML is required for YAML output. Install with: pip install pyyaml")
        sys.exit(1)

    # Check macula availability if strongs requested
    if args.with_strongs and not MACULA_AVAILABLE:
        logger.warning("--with-strongs requested but macula cache not available")
        logger.warning("Ensure .data/commentary has macula YAML files")
    
    # Extract feature
    result = extract_feature(
        args.field,
        source_dir=args.source_dir,
        max_per_value=args.max_per_value,
        output_format=args.format,
        dry_run=args.dry_run,
        with_text=args.with_text,
        with_strongs=args.with_strongs,
        limit=args.limit
    )

    # Output
    if not args.dry_run:
        if args.format == 'yaml':
            # YAML output
            yaml_output = yaml.dump(
                result,
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

        else:
            # JSONL output
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                with open(args.output, 'w', encoding='utf-8') as f:
                    for annotation in result:
                        f.write(json.dumps(annotation, ensure_ascii=False) + '\n')
                logger.info(f"✓ Output written to: {args.output}")
            else:
                for annotation in result:
                    print(json.dumps(annotation, ensure_ascii=False))


if __name__ == "__main__":
    main()
