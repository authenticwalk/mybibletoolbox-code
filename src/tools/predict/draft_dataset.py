#!/usr/bin/env python3
"""
Draft Dataset Tool
==================

Filters and balances a JSONL dataset for training preparation.
Outputs a single file with stratified sampling, ready for manual review/enrichment.

Usage:
    python draft_dataset.py --input data.jsonl --output-dir splits/
"""

import argparse
import json
import logging
import random
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Dict, List, Set

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Genre Mapping
GENRE_MAP = {
    # Narrative / Law / History
    "GEN": "Narrative", "EXO": "Narrative", "LEV": "Narrative", "NUM": "Narrative", 
    "DEU": "Narrative", "JOS": "Narrative", "JDG": "Narrative", "RUT": "Narrative",
    "1SA": "Narrative", "2SA": "Narrative", "1KI": "Narrative", "2KI": "Narrative",
    "1CH": "Narrative", "2CH": "Narrative", "EZR": "Narrative", "NEH": "Narrative", 
    "EST": "Narrative", "MAT": "Narrative", "MRK": "Narrative", "LUK": "Narrative", 
    "JHN": "Narrative", "ACT": "Narrative",
    # Poetry / Wisdom
    "JOB": "Poetry", "PSA": "Poetry", "PRO": "Poetry", "ECC": "Poetry", "SNG": "Poetry",
    "LAM": "Poetry",
    # Prophecy
    "ISA": "Prophecy", "JER": "Prophecy", "EZK": "Prophecy", "DAN": "Prophecy",
    "HOS": "Prophecy", "JOL": "Prophecy", "AMO": "Prophecy", "OBA": "Prophecy",
    "JON": "Prophecy", "MIC": "Prophecy", "NAM": "Prophecy", "HAB": "Prophecy",
    "ZEP": "Prophecy", "HAG": "Prophecy", "ZEC": "Prophecy", "MAL": "Prophecy",
    "REV": "Prophecy",
    # Epistles
    "ROM": "Epistle", "1CO": "Epistle", "2CO": "Epistle", "GAL": "Epistle",
    "EPH": "Epistle", "PHP": "Epistle", "COL": "Epistle", "1TH": "Epistle",
    "2TH": "Epistle", "1TI": "Epistle", "2TI": "Epistle", "TIT": "Epistle",
    "PHM": "Epistle", "HEB": "Epistle", "JAS": "Epistle", "1PE": "Epistle",
    "2PE": "Epistle", "1JN": "Epistle", "2JN": "Epistle", "3JN": "Epistle",
    "JUD": "Epistle"
}

def get_genre(verse_ref: str) -> str:
    if not verse_ref:
        return "Unknown"
    book = verse_ref.split('.')[0]
    return GENRE_MAP.get(book, "Other")

def group_and_cap(data: List[Dict], key_func, max_count: int, name: str) -> List[Dict]:
    """Groups data by key_func and keeps at most max_count items per group."""
    groups = defaultdict(list)
    for item in data:
        key = key_func(item)
        if len(groups[key]) < max_count:
            groups[key].append(item)
    
    result = []
    for key, items in groups.items():
        result.extend(items)
    
    logger.info(f"Applied {name} cap (max {max_count}). kept {len(result)}/{len(data)} items.")
    # Log distribution
    counts = {k: len(v) for k, v in groups.items()}
    for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        logger.info(f"  {k}: {v}")
    if len(counts) > 10:
        logger.info(f"  ... and {len(counts)-10} more")
        
    return result

def interleave_groups(groups: Dict[str, List[Dict]]) -> List[Dict]:
    """
    Interleaves items from different groups (Round Robin).
    Example: G1:[a,b], G2:[c] -> [a, c, b]
    """
    result = []
    # Use deques for efficient popping
    active_groups = {k: deque(v) for k, v in groups.items() if v}
    keys = sorted(active_groups.keys()) # Deterministic order of keys
    
    while active_groups:
        empty_keys = []
        for k in keys:
            if k in active_groups:
                if active_groups[k]:
                    result.append(active_groups[k].popleft())
                
                if not active_groups[k]:
                    empty_keys.append(k)
        
        for k in empty_keys:
            del active_groups[k]
            
    return result

def main():
    parser = argparse.ArgumentParser(description="Draft balanced dataset")
    
    parser.add_argument("--input", required=True, type=Path, help="Input JSONL file")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory")
    
    # Filtering options
    parser.add_argument("--sample-by-field", nargs='+', help="Fields to group by and cap")
    parser.add_argument("--max-sample-size", type=int, default=100, help="Max samples per group for sample-by-field")
    
    parser.add_argument("--label-field", default="label", help="Label field name")
    parser.add_argument("--max-per-label", type=int, default=1000, help="Max samples per label")
    
    parser.add_argument("--balance-by-genre", action="store_true", help="Stratify and interleave by genre")
    
    parser.add_argument("--one-per-verse", action="store_true", help="Limit to one sample per verse")
    parser.add_argument("--no-randomize", action="store_true", help="Disable randomization")
    
    parser.add_argument("--split-ratios", nargs=3, type=float, default=[0.8, 0.1, 0.1], help="Train/Val/Test ratios")
    
    args = parser.parse_args()
    
    # Load data
    if not args.input.exists():
        logger.error(f"Input file not found: {args.input}")
        sys.exit(1)
        
    data = []
    with open(args.input, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                try:
                    item = json.loads(line)
                    # Annotate genre
                    item['genre'] = get_genre(item.get('verse', ''))
                    data.append(item)
                except json.JSONDecodeError:
                    continue
                    
    logger.info(f"Loaded {len(data)} items from {args.input}")
    
    # Global Shuffle
    if not args.no_randomize:
        random.seed(42) # Reproducibility
        random.shuffle(data)
        logger.info("Randomized data (Global Shuffle)")

    # Initial Sort/Shuffle/Interleave BEFORE Caps
    if args.balance_by_genre:
        logger.info("Pre-sorting: Grouping and Interleaving by Genre and Label")
        
        # Group by label first
        label_groups = defaultdict(list)
        label_field = args.label_field
        for item in data:
            label_groups[item.get(label_field, 'Unknown')].append(item)
            
        if not args.no_randomize:
             for items in label_groups.values():
                random.shuffle(items)
        
        data_by_label = interleave_groups(label_groups)
        
        # Then group by Genre
        genre_groups = defaultdict(list)
        for item in data_by_label:
            genre_groups[item['genre']].append(item)
            
        # No shuffle here to preserve label interleaving
        data = interleave_groups(genre_groups)


    # One per verse (Dedup after sorting to prioritize rare/interleaved items)
    if args.one_per_verse:
        seen_verses = set()
        unique_data = []
        for item in data:
            verse = item.get('verse')
            if verse and verse not in seen_verses:
                seen_verses.add(verse)
                unique_data.append(item)
        data = unique_data
        logger.info(f"Filtered one per verse. Remaining: {len(data)}")

    # Sample by Field (Ensure minimums/diversity by capping)
    if args.sample_by_field:
        def field_key(item):
            return tuple(str(item.get(f, '')) for f in args.sample_by_field)
            
        data = group_and_cap(
            data,
            field_key,
            args.max_sample_size,
            f"Fields({args.sample_by_field})"
        )
        
    # Max per Label
    if args.max_per_label:
        data = group_and_cap(
            data,
            lambda x: x.get(args.label_field, 'Unknown'),
            args.max_per_label,
            "Label"
        )
    
    # Assign Splits (Train/Val/Test) to Metadata instead of creating separate files
    # Logic:
    # 1. Group by Genre (to ensure stratified assignment)
    # 2. Assign split labels based on ratios
    # 3. Interleave back into a single list
    
    # Prepare Ratios
    train_ratio, val_ratio, test_ratio = args.split_ratios
    ratio_sum = train_ratio + val_ratio + test_ratio
    train_ratio /= ratio_sum
    val_ratio /= ratio_sum
    test_ratio /= ratio_sum

    if args.balance_by_genre:
        logger.info("Assigning splits: Stratified by Genre")
        genre_groups = defaultdict(list)
        for item in data:
            genre_groups[item['genre']].append(item)
            
        # We don't shuffle again here to preserve the careful interleaving/selection from above
        # unless specifically requested? 
        # Actually, the selection (capping) has happened. Now we just need to assign T/V/T labels.
        # If we process linearly, the interleaved order [Nar, Poe, Pro, Nar...] might assign 
        # T, T, T ... then V, V ... which would bias T towards early items?
        # No, we slice list by ratio.
        
        final_groups = defaultdict(list) # Accumulate processed items
        
        for genre, items in genre_groups.items():
            if not args.no_randomize:
                 random.shuffle(items) # Shuffle within genre to randomize which specific items get T vs V vs Test

            count = len(items)
            t_end = int(count * train_ratio)
            v_end = t_end + int(count * val_ratio)
            
            # Assign splits
            for i, item in enumerate(items):
                split = "train"
                if i >= v_end:
                    split = "test"
                elif i >= t_end:
                    split = "validate"
                
                # Initialize dataset structure if not present
                if 'dataset' not in item:
                    item['dataset'] = {}
                
                item['dataset']['split'] = split
                item['dataset']['section'] = 'OT' if item.get('verse', '').startswith(('GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR', 'NEH', 'EST', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK', 'DAN', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL')) else 'NT'
                item['dataset']['literary_type'] = item['genre'].lower() # Narrative -> narrative
                
                final_groups[genre].append(item)
            
            logger.debug(f"  {genre}: {t_end} T, {v_end-t_end} V, {count-v_end} Test")
            
        # Interleave back for final output order
        data = interleave_groups(final_groups)
        
    else:
        # Simple random assignment
        if not args.no_randomize:
            random.shuffle(data)
            
        total = len(data)
        t_end = int(total * train_ratio)
        v_end = t_end + int(total * val_ratio)
        
        for i, item in enumerate(data):
            split = "train"
            if i >= v_end:
                split = "test"
            elif i >= t_end:
                split = "validate"
                
            if 'dataset' not in item:
                item['dataset'] = {}
            item['dataset']['split'] = split
            item['dataset']['section'] = 'OT' if item.get('verse', '').startswith(('GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR', 'NEH', 'EST', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK', 'DAN', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL')) else 'NT'
            item['dataset']['literary_type'] = item['genre'].lower()

    logger.info(f"Total items in draft: {len(data)}")
    
    # Write Single Output File
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_file = args.output_dir / "datasets.jsonl"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data:
            # Remove internal helper fields if desired, but genre is useful
            # if 'genre' in item: del item['genre'] 
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
                
    logger.info(f"Draft dataset written to {output_file}")

if __name__ == "__main__":
    main()
