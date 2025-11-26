#!/usr/bin/env python3
"""
TBTA Append Hints Script
========================

Appends generated hints to verse commentary files in the data directory.
Used after group_by_reasons.py to persist theological hints for specific verses.

The hints are stored in: $DATA_DIR/commentary/{BOOK}/{CCC}/{VVV}/{BOOK}-{CCC}-{VVV}-tbta-hints.yaml

Usage:
    # Append hints from grouped reasons (after LLM added hint field)
    python append_to_verses.py --input analysis/grouped-with-hints.jsonl --feature Number

    # Dry run to see what would be updated
    python append_to_verses.py --input analysis/grouped-with-hints.jsonl --feature Number --dry-run

Input formats supported:
    1. Group format (from group_by_reasons.py with added 'hint' field):
       {"reason": "TRINITY", "hint": "Trinitarian context...", "entries": [...]}

    2. Single verse format:
       {"verse": "GEN.001.026", "hint": "This verse..."}

Output YAML structure (per verse file):
    feature_name:
      hints:
        - REASON_CODE:
            description: "Hint text explaining the theological context..."
"""

import argparse
import json
import logging
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.config import get_verse_path
from src.constants.bible import parse_verse_ref

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def update_verse_file(verse_ref: str, feature_name: str, reason_code: str,
                      description: str, dry_run: bool = False) -> bool:
    """
    Update the tbta-hints.yaml file for a specific verse.

    Args:
        verse_ref: Verse reference (e.g., "GEN.001.026")
        feature_name: Feature name (e.g., "Number", "Clusivity")
        reason_code: Reason code (e.g., "TRINITY", "DIVINE_SPEECH")
        description: Hint description text
        dry_run: If True, don't actually write files

    Returns:
        True if file was updated (or would be in dry_run), False if skipped
    """
    try:
        book, chapter, verse = parse_verse_ref(verse_ref)
    except ValueError:
        logger.warning(f"Invalid verse ref: {verse_ref}")
        return False

    verse_dir = get_verse_path(book, chapter, verse)
    filename = f"{book}-{chapter:03d}-{verse:03d}-tbta-hints.yaml"
    file_path = verse_dir / filename

    # Load existing data
    data = {}
    if file_path.exists():
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            logger.warning(f"Failed to load {file_path}, will create new: {e}")

    # Initialize structure
    if feature_name not in data:
        data[feature_name] = {'hints': []}
    if 'hints' not in data[feature_name]:
        data[feature_name]['hints'] = []

    # Check if hint already exists to avoid duplicates
    for h in data[feature_name]['hints']:
        if isinstance(h, str) and h == reason_code:
            return False  # Already exists as simple string
        elif isinstance(h, dict):
            if reason_code in h:
                return False  # Already exists as dict key
            if h.get('code') == reason_code:
                return False  # Already exists with 'code' field

    # Add new hint
    if description:
        new_hint = {
            reason_code: {
                "description": description
            }
        }
    else:
        new_hint = reason_code

    data[feature_name]['hints'].append(new_hint)

    # Write file
    if not dry_run:
        # Ensure directory exists
        verse_dir.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Append TBTA hints to verse commentary files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Append hints after LLM added hint text to groups
    python append_to_verses.py --input grouped-with-hints.jsonl --feature Number

    # Dry run to preview changes
    python append_to_verses.py --input grouped-with-hints.jsonl --feature Number --dry-run
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file with hints")
    parser.add_argument("--feature", required=True, help="Feature name (e.g., Number, Clusivity)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview what would be updated without writing files")

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    logger.info(f"Reading hints from {args.input}...")
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

                # Handle "Group" format (from group_by_reasons.py with added hint)
                if 'reason' in obj and 'entries' in obj and 'hint' in obj:
                    hint_text = obj['hint']
                    reason_code = obj['reason']

                    for entry in obj['entries']:
                        verse_ref = entry.get('verse')
                        if not verse_ref:
                            continue

                        if update_verse_file(verse_ref, args.feature, reason_code,
                                           hint_text, dry_run=args.dry_run):
                            updates_count += 1
                        else:
                            skipped_count += 1

                # Handle "Single Verse" format
                elif 'verse' in obj and 'hint' in obj:
                    reason = obj.get('reason', 'HINT')
                    if update_verse_file(obj['verse'], args.feature, reason,
                                       obj['hint'], dry_run=args.dry_run):
                        updates_count += 1
                    else:
                        skipped_count += 1

                # Handle group format without hint (skip)
                elif 'reason' in obj and 'entries' in obj:
                    logger.debug(f"Line {line_num}: Group '{obj['reason']}' has no 'hint' field, skipping")
                    skipped_count += len(obj.get('entries', []))

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
    logger.info(f"Verses {'would be ' if args.dry_run else ''}updated: {updates_count}")
    logger.info(f"Skipped (already exists or no hint): {skipped_count}")
    if error_count:
        logger.info(f"Errors: {error_count}")


if __name__ == "__main__":
    main()
