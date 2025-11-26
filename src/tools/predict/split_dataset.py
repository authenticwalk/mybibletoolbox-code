#!/usr/bin/env python3
"""
Split enriched JSONL dataset into train/validate/test/leftovers files.

Output files:
  - train.jsonl: Training data with labels (for learning)
  - validate.jsonl + validate.secret.jsonl: Validation without/with labels
  - test.jsonl + test.secret.jsonl: Test without/with labels
  - leftovers.jsonl: Remaining entries from original (with labels)

Usage:
    python src/tools/predict/split_dataset.py \
        --input analysis/enriched.jsonl \
        --original analysis/tbta-extract.jsonl \
        --output analysis/data
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


def load_jsonl(filepath: Path) -> list[dict[str, Any]]:
    """Load JSONL file into list of dicts."""
    entries = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Warning: Skipping invalid JSON at line {line_num}: {e}", file=sys.stderr)
    return entries


def save_jsonl(filepath: Path, entries: list[dict[str, Any]]) -> None:
    """Save list of dicts to JSONL file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def strip_secret_fields(entry: dict[str, Any]) -> dict[str, Any]:
    """Remove 'label' and 'dataset' fields from entry."""
    result = {k: v for k, v in entry.items() if k not in ("label", "dataset")}
    return result


def get_entry_key(entry: dict[str, Any]) -> tuple:
    """Create a unique key for an entry based on verse + constituent."""
    return (entry.get("verse"), entry.get("constituent"), entry.get("part"))


def main():
    parser = argparse.ArgumentParser(
        description="Split enriched JSONL into train/validate/test/leftovers"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input enriched JSONL file with dataset.split field",
    )
    parser.add_argument(
        "--original",
        required=True,
        help="Original extract JSONL file (for computing leftovers)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for split files",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    original_path = Path(args.original)
    output_dir = Path(args.output)

    # Validate input files exist
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    if not original_path.exists():
        print(f"Error: Original file not found: {original_path}", file=sys.stderr)
        sys.exit(1)

    # Load data
    print(f"Loading input: {input_path}")
    input_entries = load_jsonl(input_path)
    print(f"  Loaded {len(input_entries)} entries")

    print(f"Loading original: {original_path}")
    original_entries = load_jsonl(original_path)
    print(f"  Loaded {len(original_entries)} entries")

    # Split by dataset.split field
    splits: dict[str, list[dict[str, Any]]] = {
        "train": [],
        "validate": [],
        "test": [],
    }

    # Track which entries from input we've seen (for leftovers calculation)
    input_keys = set()

    for entry in input_entries:
        dataset = entry.get("dataset", {})
        split = dataset.get("split", "train")

        if split not in splits:
            print(f"Warning: Unknown split '{split}', defaulting to train", file=sys.stderr)
            split = "train"

        splits[split].append(entry)
        input_keys.add(get_entry_key(entry))

    # Calculate leftovers (entries in original but not in input)
    leftovers = []
    for entry in original_entries:
        key = get_entry_key(entry)
        if key not in input_keys:
            leftovers.append(entry)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write split files
    for split_name, entries in splits.items():
        if entries:
            if split_name == "train":
                # Train: single file with all fields (labels visible for training)
                train_path = output_dir / "train.jsonl"
                save_jsonl(train_path, entries)
                print(f"Wrote {len(entries)} entries to {train_path}")
            else:
                # Validate/Test: public file (no labels) + secret file (with labels)
                secret_path = output_dir / f"{split_name}.secret.jsonl"
                save_jsonl(secret_path, entries)
                print(f"Wrote {len(entries)} entries to {secret_path}")

                public_path = output_dir / f"{split_name}.jsonl"
                public_entries = [strip_secret_fields(e) for e in entries]
                save_jsonl(public_path, public_entries)
                print(f"Wrote {len(public_entries)} entries to {public_path}")

    # Write leftovers (single file with all fields)
    if leftovers:
        leftovers_path = output_dir / "leftovers.jsonl"
        save_jsonl(leftovers_path, leftovers)
        print(f"Wrote {len(leftovers)} entries to {leftovers_path}")
    else:
        print("No leftovers found")

    # Rename original files to .secret.jsonl
    input_secret = input_path.with_suffix(".secret.jsonl")
    original_secret = original_path.with_suffix(".secret.jsonl")

    # Handle case where input already ends in .jsonl
    if input_path.suffix == ".jsonl":
        input_secret = input_path.parent / (input_path.stem + ".secret.jsonl")
    if original_path.suffix == ".jsonl":
        original_secret = original_path.parent / (original_path.stem + ".secret.jsonl")

    print(f"\nRenaming {input_path} -> {input_secret}")
    input_path.rename(input_secret)

    print(f"Renaming {original_path} -> {original_secret}")
    original_path.rename(original_secret)

    # Summary
    print("\n=== Summary ===")
    print(f"Train:    {len(splits['train'])} entries")
    print(f"Validate: {len(splits['validate'])} entries")
    print(f"Test:     {len(splits['test'])} entries")
    print(f"Leftovers: {len(leftovers)} entries")


if __name__ == "__main__":
    main()

