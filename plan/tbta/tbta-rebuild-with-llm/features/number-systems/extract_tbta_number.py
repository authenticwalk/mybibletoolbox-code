#!/usr/bin/env python3
"""
Extract Number annotations from TBTA JSON files.
"""

import json
import sys
from pathlib import Path

def extract_numbers(element, results=None, path=""):
    """
    Recursively extract all Number annotations from TBTA JSON.

    Returns list of tuples: (constituent, number_value, path)
    """
    if results is None:
        results = []

    # Get constituent and Number if present
    constituent = element.get('Constituent', '')
    number = element.get('Number', '')
    part = element.get('Part', '')

    # Add to results if has Number annotation
    if number and number != 'Unspecified':
        results.append({
            'constituent': constituent,
            'number': number,
            'part': part,
            'path': path
        })

    # Recurse into children
    if 'Children' in element:
        for i, child in enumerate(element['Children']):
            child_path = f"{path}/{part}[{i}]" if path else f"{part}[{i}]"
            extract_numbers(child, results, child_path)

    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_tbta_number.py <json_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, 'r') as f:
        data = json.load(f)

    # data is array of clauses
    all_numbers = []
    for clause_idx, clause in enumerate(data):
        clause_numbers = extract_numbers(clause, path=f"Clause[{clause_idx}]")
        all_numbers.extend(clause_numbers)

    # Print results
    print(f"\n{'='*80}")
    print(f"File: {file_path.name}")
    print(f"{'='*80}\n")

    if not all_numbers:
        print("No Number annotations found.")
    else:
        print(f"Found {len(all_numbers)} Number annotations:\n")
        for item in all_numbers:
            print(f"  {item['constituent']:20s}  Number: {item['number']:1s}  Part: {item['part']:10s}")

    print(f"\n{'='*80}\n")

if __name__ == '__main__':
    main()
