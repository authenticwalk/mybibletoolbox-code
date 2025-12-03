#!/usr/bin/env python3
"""
TBTA Reason Grouping Script
===========================

Groups TBTA verses by their reason_group field (set during dataset creation).

Usage:
    python group_by_reasons.py --input analysis/train.jsonl
    python group_by_reasons.py --input analysis/train.jsonl --output grouped.jsonl

Output format (one line per reason group):
    {
        "reason": "TRINITY",
        "count": 45,
        "verses": ["GEN.001.026", "GEN.003.022", ...]
    }
"""

import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Group TBTA verses by reason_group field",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python group_by_reasons.py --input train.jsonl
    python group_by_reasons.py --input train.jsonl --output grouped.jsonl
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file")
    parser.add_argument("--output", default="", help="Output JSONL file (stdout if empty)")
    parser.add_argument("--max-per-group", type=int, default=500,
                        help="Maximum verses per group (default: 500)")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    logger.info(f"Reading from {args.input}...")

    # Group entries by reason_group
    grouped_data: Dict[str, List[Dict]] = defaultdict(list)
    total_count = 0

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            total_count += 1
            
            # Get reason_group from entry (or UNSET if not present)
            dataset = entry.get('dataset', {})
            reason = dataset.get('reason_group') or 'UNSET'
            
            if len(grouped_data[reason]) < args.max_per_group:
                grouped_data[reason].append(entry)

    logger.info(f"Processed {total_count} entries")

    # Build output objects
    output_objects = []
    for reason, entries in sorted(grouped_data.items()):
        verses = sorted(set(e.get('verse', '') for e in entries))
        output_objects.append({
            "reason": reason,
            "count": len(entries),
            "verses": verses
        })

    # Write output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            for obj in output_objects:
                f.write(json.dumps(obj, ensure_ascii=False) + '\n')
        logger.info(f"Output: {args.output}")
    else:
        for obj in output_objects:
            print(json.dumps(obj, ensure_ascii=False))

    # Summary
    logger.info("=" * 50)
    logger.info("GROUPING COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Total groups: {len(grouped_data)}")
    for reason in sorted(grouped_data.keys()):
        count = len(grouped_data[reason])
        logger.info(f"  {reason}: {count} entries")


if __name__ == "__main__":
    main()
