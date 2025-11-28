#!/usr/bin/env python3
"""
Final Dataset Splitter
======================

Reads a single dataset file containing a 'dataset' object with a 'split' field
and separates it into train.jsonl, val.jsonl, and test.jsonl.

Usage:
    python split_dataset.py --input datasets.jsonl --output-dir data/
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Split finalized dataset based on split field")
    
    parser.add_argument("--input", required=True, type=Path, help="Input JSONL file (datasets.jsonl)")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory for split files")
    # Retain --original argument for compatibility with instructions (even if unused for simple split)
    parser.add_argument("--original", type=Path, help="Original extract file (unused in this version but kept for compatibility)")

    args = parser.parse_args()

    if not args.input.exists():
        logger.error(f"Input file not found: {args.input}")
        return

    splits: Dict[str, List[Dict]] = {
        "train": [],
        "validate": [], # Maps to val.jsonl
        "test": []
    }
    
    # Mapping from dataset.split value to output filename prefix
    # Handle potential variations (val vs validate)
    split_map = {
        "train": "train",
        "validate": "val",
        "val": "val",
        "test": "test"
    }
    
    outputs = {
        "train": [],
        "val": [],
        "test": []
    }

    count = 0
    with open(args.input, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                item = json.loads(line)
                dataset_meta = item.get('dataset', {})
                split_name = dataset_meta.get('split', '').lower()
                
                if not split_name:
                    logger.warning(f"Item missing dataset.split: {item.get('verse', 'unknown')}")
                    continue
                    
                target = split_map.get(split_name)
                if target:
                    outputs[target].append(item)
                    count += 1
                else:
                    logger.warning(f"Unknown split name '{split_name}' for verse {item.get('verse')}")
                    
            except json.JSONDecodeError:
                continue

    logger.info(f"Processed {count} items.")
    
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    for name, items in outputs.items():
        out_path = args.output_dir / f"{name}.jsonl"
        with open(out_path, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        logger.info(f"Wrote {len(items)} items to {out_path}")

if __name__ == "__main__":
    main()
