#!/usr/bin/env python3
"""
TBTA Reason Grouping Script
===========================

Groups TBTA verses by theological/grammatical reason categories to help
identify patterns and add verse-specific hints.

This script is used in the analysis phase to:
1. Group verses that share similar theological contexts (Trinity, prophecy, etc.)
2. Identify verses that may need special handling
3. Prepare data for the LLM to add hints to edge cases

Usage:
    # Group by existing reason field (if present)
    python group_by_reasons.py --input analysis/tbta-extract.jsonl \\
        --output analysis/grouped-by-reason.jsonl

    # Load theological groupings from research file
    python group_by_reasons.py --input analysis/tbta-extract.jsonl \\
        --groups research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml \\
        --output analysis/grouped-by-reason.jsonl

Output format (one line per reason group):
    {
        "reason": "TRINITY",
        "description": "Verses involving Trinitarian theology...",
        "count": 45,
        "verses": ["GEN.001.026", "GEN.003.022", ...]
    }
"""

import argparse
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Well-known theological groupings with their verse patterns
# These are common categories that often need special handling
DEFAULT_THEOLOGICAL_GROUPS = {
    "TRINITY": {
        "description": "Verses involving Trinitarian theology - plural forms referring to the one God",
        "patterns": [
            r"GEN\.001\.026",  # Let us make man
            r"GEN\.003\.022",  # Man has become like one of us
            r"GEN\.011\.007",  # Let us go down
            r"ISA\.006\.008",  # Whom shall I send, who will go for us
            r"MAT\.028\.019",  # Baptizing in the name of Father, Son, Spirit
            r"MAT\.003\.016",  # Baptism of Jesus - all three present
            r"JHN\.014\.0(16|17|26)",  # Jesus promises the Spirit
            r"JHN\.015\.026",  # Spirit from the Father
            r"2CO\.013\.014",  # Trinitarian benediction
        ],
        "keywords": ["us", "our", "we"]  # In divine speech contexts
    },
    "DIVINE_SPEECH": {
        "description": "Direct speech from God - often uses exclusive first person",
        "patterns": [
            r"GEN\.00[1-3]\.",  # Creation narrative
            r"EXO\.003\.",  # Burning bush
            r"EXO\.020\.",  # Ten Commandments
            r"ISA\.04[0-9]\.",  # Isaiah's comfort oracles
        ],
        "keywords": ["I am", "says the LORD", "thus says"]
    },
    "MESSIANIC": {
        "description": "Messianic prophecies - may have complex person/number patterns",
        "patterns": [
            r"ISA\.00(7|9)\.",  # Emmanuel, Wonderful Counselor
            r"ISA\.053\.",  # Suffering Servant
            r"PSA\.022\.",  # My God, my God
            r"PSA\.110\.",  # The LORD says to my Lord
            r"MIC\.005\.002",  # Bethlehem prophecy
            r"ZEC\.009\.009",  # King on a donkey
        ],
        "keywords": []
    },
    "CORPORATE_SOLIDARITY": {
        "description": "Israel/Church addressed as singular or plural collectively",
        "patterns": [
            r"DEU\.006\.",  # Shema and following
            r"HOS\.",  # Israel as unfaithful wife
            r"ROM\.009\.",  # Israel discussion
            r"ROM\.011\.",  # Olive tree metaphor
        ],
        "keywords": ["Israel", "my people", "the church"]
    },
    "INCARNATION": {
        "description": "Verses about Christ's divine-human nature",
        "patterns": [
            r"JHN\.001\.001",  # Word was God
            r"JHN\.001\.014",  # Word became flesh
            r"PHP\.002\.0(5|6|7|8|9|10|11)",  # Christ hymn
            r"COL\.001\.01[5-9]",  # Supremacy of Christ
            r"COL\.002\.009",  # Fullness of deity
            r"HEB\.001\.",  # Son superior to angels
        ],
        "keywords": []
    },
    "PRAYER": {
        "description": "Prayer contexts - addressee is typically God",
        "patterns": [
            r"PSA\.",  # Many psalms are prayers
            r"MAT\.006\.0(9|10|11|12|13)",  # Lord's Prayer
            r"JHN\.017\.",  # Jesus' high priestly prayer
        ],
        "keywords": ["pray", "prayer", "O Lord", "O God"]
    },
    "IMPERATIVE": {
        "description": "Commands - may affect mood/aspect analysis",
        "patterns": [],
        "keywords": ["do not", "let", "shall", "must", "command"]
    },
    "POETRY": {
        "description": "Poetic/wisdom literature - may have unusual structures",
        "patterns": [
            r"JOB\.",
            r"PSA\.",
            r"PRO\.",
            r"ECC\.",
            r"SNG\.",
            r"LAM\.",
        ],
        "keywords": []
    }
}


def load_theological_groups(groups_file: Path) -> Dict:
    """Load theological groupings from YAML file."""
    try:
        import yaml
    except ImportError:
        logger.error("PyYAML required for loading groups file. pip install pyyaml")
        sys.exit(1)

    if not groups_file.exists():
        logger.warning(f"Groups file not found: {groups_file}")
        return {}

    try:
        with open(groups_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data.get('groups', data) if isinstance(data, dict) else {}
    except Exception as e:
        logger.error(f"Failed to load groups file: {e}")
        return {}


def match_verse_to_groups(verse_ref: str, entry: Dict, groups: Dict) -> List[str]:
    """
    Determine which theological groups a verse belongs to.

    Returns list of group codes (e.g., ["TRINITY", "DIVINE_SPEECH"])
    """
    matched = []

    for group_code, group_def in groups.items():
        # Check verse patterns
        patterns = group_def.get('patterns', [])
        for pattern in patterns:
            if re.match(pattern, verse_ref):
                matched.append(group_code)
                break
        else:
            # Check keywords in constituent/text
            keywords = group_def.get('keywords', [])
            constituent = entry.get('constituent', '').lower()
            for keyword in keywords:
                if keyword.lower() in constituent:
                    matched.append(group_code)
                    break

    return matched


def main():
    parser = argparse.ArgumentParser(
        description="Group TBTA verses by theological/grammatical reasons",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Use default theological groupings
    python group_by_reasons.py --input tbta-extract.jsonl \\
        --output grouped-by-reason.jsonl

    # Use custom groupings from research file
    python group_by_reasons.py --input tbta-extract.jsonl \\
        --groups research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml \\
        --output grouped-by-reason.jsonl

    # Filter to specific dataset
    python group_by_reasons.py --input tbta-extract.jsonl \\
        --output grouped-by-reason.jsonl --dataset train
        """
    )
    parser.add_argument("--input", required=True, help="Input JSONL file")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--groups", type=Path,
                        help="YAML file with theological groupings (optional)")
    parser.add_argument("--dataset", choices=['train', 'test', 'validate', 'all'], default='all',
                        help="Filter to specific dataset split (default: all)")
    parser.add_argument("--max-per-group", type=int, default=500,
                        help="Maximum verses per group (default: 500)")

    args = parser.parse_args()

    # Load theological groups
    if args.groups:
        groups = load_theological_groups(args.groups)
        if groups:
            logger.info(f"Loaded {len(groups)} groups from {args.groups}")
        else:
            logger.info("Using default theological groups")
            groups = DEFAULT_THEOLOGICAL_GROUPS
    else:
        groups = DEFAULT_THEOLOGICAL_GROUPS
        logger.info(f"Using {len(groups)} default theological groups")

    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    logger.info(f"Reading from {args.input}...")

    # Group entries
    grouped_data: Dict[str, List[Dict]] = defaultdict(list)
    unset_count = 0
    total_count = 0

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Filter by dataset if specified
            if args.dataset != 'all':
                entry_dataset = entry.get('dataset', 'train')
                if entry_dataset != args.dataset:
                    continue

            total_count += 1
            verse_ref = entry.get('verse', '')

            # Check if entry already has a reason assigned
            existing_reason = entry.get('reason')
            if existing_reason and existing_reason != 'UNSET':
                if len(grouped_data[existing_reason]) < args.max_per_group:
                    grouped_data[existing_reason].append(entry)
                continue

            # Try to match to theological groups
            matched_groups = match_verse_to_groups(verse_ref, entry, groups)

            if matched_groups:
                for group in matched_groups:
                    if len(grouped_data[group]) < args.max_per_group:
                        entry_copy = entry.copy()
                        entry_copy['reason'] = group
                        grouped_data[group].append(entry_copy)
            else:
                # No match - add to UNSET
                if len(grouped_data['UNSET']) < args.max_per_group:
                    grouped_data['UNSET'].append(entry)
                unset_count += 1

    logger.info(f"Processed {total_count} entries")
    logger.info(f"Verses without reason: {unset_count}")

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        for reason, entries in sorted(grouped_data.items()):
            # Get description from groups definition
            description = ""
            if reason in groups:
                description = groups[reason].get('description', '')
            elif reason == 'UNSET':
                description = "Verses not matched to any theological grouping - needs manual review"

            # Get unique verses
            verses = sorted(set(e.get('verse', '') for e in entries))

            group_obj = {
                "reason": reason,
                "description": description,
                "count": len(entries),
                "verses": verses  # All unique verses in this group
            }
            f.write(json.dumps(group_obj, ensure_ascii=False) + '\n')

    # Summary
    logger.info("=" * 50)
    logger.info("GROUPING COMPLETE")
    logger.info("=" * 50)
    logger.info(f"Total groups: {len(grouped_data)}")
    for reason in sorted(grouped_data.keys()):
        count = len(grouped_data[reason])
        logger.info(f"  {reason}: {count} entries")
    logger.info(f"Output: {args.output}")


if __name__ == "__main__":
    main()
