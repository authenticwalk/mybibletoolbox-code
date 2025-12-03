#!/usr/bin/env python3
"""
Append Hints to Strong's Files
==============================

Appends hints to Strong's YAML files in the data directory.
Uses the get_strongs library for file operations.

Usage:
    python append_to_strongs.py --input analysis/strongs-hints.jsonl --feature Number --tool tbta-hints
    python append_to_strongs.py --input analysis/strongs-hints.jsonl --feature Number --tool tbta-hints --dry-run

Input JSONL format:
    {"strongs": "H376", "word": "אִישׁ", "gloss": "man", "hint": "Look at the preceding numeral...", "pattern_type": "contextual"}
"""

import argparse
import json
import logging
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.lib.get_strongs import get_strongs_tool_file, save_strongs_tool_file

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def update_strongs_file(strongs_num: str, tool: str, feature_name: str,
                        hint_data: dict, dry_run: bool = False) -> bool:
    """
    Update the tool YAML file for a specific Strong's number.

    Args:
        strongs_num: Strong's number (e.g., "H376", "G2316")
        tool: Tool name (e.g., "tbta-hints")
        feature_name: Feature name (e.g., "Number", "Clusivity")
        hint_data: Dict with hint info (hint, pattern_type, label, etc.)
        dry_run: If True, don't actually write files

    Returns:
        True if file was updated (or would be in dry_run), False if skipped
    """
    # Load existing data using library
    data = get_strongs_tool_file(strongs_num, tool) or {}

    # Initialize structure
    if feature_name not in data:
        data[feature_name] = {'hints': []}
    if 'hints' not in data[feature_name]:
        data[feature_name]['hints'] = []

    # Build new hint entry
    new_hint = {}
    if hint_data.get('pattern_type'):
        new_hint['pattern_type'] = hint_data['pattern_type']
    if hint_data.get('label'):
        new_hint['label'] = hint_data['label']
    if hint_data.get('hint'):
        new_hint['hint'] = hint_data['hint']

    # Check if similar hint already exists
    for existing in data[feature_name]['hints']:
        if existing.get('hint') == new_hint.get('hint'):
            return False  # Already exists

    data[feature_name]['hints'].append(new_hint)

    # Add metadata if provided
    if hint_data.get('word') and 'word' not in data:
        data['word'] = hint_data['word']
    if hint_data.get('gloss') and 'gloss' not in data:
        data['gloss'] = hint_data['gloss']

    # Save file using library
    if not dry_run:
        save_strongs_tool_file(strongs_num, tool, data)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Append hints to Strong's YAML files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python append_to_strongs.py --input strongs-hints.jsonl --feature Number --tool tbta-hints
    python append_to_strongs.py --input strongs-hints.jsonl --feature Number --tool tbta-hints --dry-run
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file with hints")
    parser.add_argument("--feature", required=True, help="Feature name (e.g., Number, Clusivity)")
    parser.add_argument("--tool", required=True, help="Tool name for output file (e.g., tbta-hints)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be updated without writing files")

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    logger.info(f"Reading hints from {args.input}...")
    logger.info(f"Tool: {args.tool}, Feature: {args.feature}")
    if args.dry_run:
        logger.info("DRY RUN MODE - no files will be written")

    updates_count = 0
    skipped_count = 0
    error_count = 0

    with open(input_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip():
                continue

            try:
                obj = json.loads(line)

                if 'strongs' not in obj:
                    logger.warning(f"Line {line_num}: Missing 'strongs' field, skipping")
                    skipped_count += 1
                    continue

                if 'hint' not in obj:
                    logger.debug(f"Line {line_num}: No 'hint' field, skipping")
                    skipped_count += 1
                    continue

                if update_strongs_file(obj['strongs'], args.tool, args.feature,
                                       obj, dry_run=args.dry_run):
                    updates_count += 1
                    if args.dry_run:
                        logger.info(f"Would update: {obj['strongs']} - {obj.get('gloss', 'N/A')}")
                else:
                    skipped_count += 1

            except json.JSONDecodeError as e:
                logger.warning(f"Invalid JSON at line {line_num}: {e}")
                error_count += 1
            except Exception as e:
                logger.error(f"Error processing line {line_num}: {e}")
                error_count += 1

    # Summary
    logger.info("=" * 50)
    logger.info("APPEND COMPLETE" if not args.dry_run else "DRY RUN COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Strong's files {'would be ' if args.dry_run else ''}updated: {updates_count}")
    logger.info(f"Skipped (already exists or no hint): {skipped_count}")
    if error_count:
        logger.info(f"Errors: {error_count}")


if __name__ == "__main__":
    main()
