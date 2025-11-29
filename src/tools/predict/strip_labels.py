#!/usr/bin/env python3
"""
Strip labels and dataset hints from a JSONL dataset.

This tool reads a JSONL file, removes the "label" and "dataset" fields (which contain
split information and correct answers), and outputs the cleaned data.

Usage:
    python src/tools/predict/strip_labels.py --input train.jsonl --output public.jsonl --limit 10
    python src/tools/predict/strip_labels.py --input data/test.secret.jsonl --fields verse,text
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, TextIO, Optional, List


def filter_fields(entry: dict[str, Any], fields: Optional[List[str]] = None) -> dict[str, Any]:
    """
    Filter fields from entry.
    
    If fields is provided, keeps ONLY those fields (and ignores label/dataset).
    If fields is None, removes ONLY 'label' and 'dataset'.
    """
    if fields:
        return {k: v for k, v in entry.items() if k in fields}
    
    return {k: v for k, v in entry.items() if k not in ("label", "dataset")}


def main():
    parser = argparse.ArgumentParser(
        description="Strip labels and dataset hints from a JSONL dataset"
    )
    parser.add_argument(
        "--input",
        default="train.jsonl",
        help="Input JSONL file (default: train.jsonl)",
    )
    parser.add_argument(
        "--output",
        help="Output JSONL file (default: stdout)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of entries to output",
    )
    parser.add_argument(
        "--fields",
        help="Comma-separated list of fields to keep (e.g. 'verse,text'). If provided, only these fields are kept.",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Parse fields if provided
    keep_fields = None
    if args.fields:
        keep_fields = [f.strip() for f in args.fields.split(",")]

    # Open output stream
    out_stream: TextIO = sys.stdout
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        out_stream = open(output_path, "w", encoding="utf-8")

    count = 0
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"Warning: Skipping invalid JSON at line {line_num}: {e}", file=sys.stderr)
                    continue

                filtered = filter_fields(entry, keep_fields)
                out_stream.write(json.dumps(filtered, ensure_ascii=False) + "\n")
                
                count += 1
                if args.limit and count >= args.limit:
                    break
    except BrokenPipeError:
        # Handle case where output is piped to head or similar
        sys.stderr.close()
    finally:
        if args.output and out_stream is not sys.stdout:
            out_stream.close()
            print(f"Wrote {count} entries to {args.output}", file=sys.stderr)
        elif out_stream is sys.stdout:
             # If writing to stdout, we might want to print the count to stderr
             print(f"Processed {count} entries", file=sys.stderr)

if __name__ == "__main__":
    main()
