#!/usr/bin/env python3
"""Debug script to test TBTA extraction on a single verse."""

import sys
from pathlib import Path

# Import from the main script
sys.path.insert(0, str(Path(__file__).parent))
from extract_tbta_nodes import (
    load_macula_data,
    process_verse,
    extract_tbta_nodes_from_clause,
    TBTA_LOCAL_PATH
)

def test_single_verse():
    """Test processing John 1:1"""

    # Test file
    tbta_file = TBTA_LOCAL_PATH / "json" / "42_001_001_John.json"

    print(f"Testing: {tbta_file}")
    print(f"Exists: {tbta_file.exists()}")
    print()

    # Test Macula loading
    print("=" * 60)
    print("TESTING MACULA LOADING")
    print("=" * 60)
    macula = load_macula_data("JHN", 1, 1)
    if macula:
        print(f"✓ Macula loaded successfully")
        print(f"  Words: {len(macula.get('words', []))}")

        # Show first few words
        for i, word in enumerate(macula.get('words', [])[:5]):
            pos = word.get('position')
            strong = word.get('lexical', {}).get('strong')
            text = word.get('text')
            word_id = word.get('ids', {}).get('wordID', '')
            prefix = "G" if word_id.startswith("n") else "H"
            print(f"  Word {pos}: '{text}' -> {prefix}{strong}")
    else:
        print("✗ Failed to load Macula data")
        return

    print()

    # Test TBTA processing
    print("=" * 60)
    print("TESTING TBTA PROCESSING")
    print("=" * 60)

    results = process_verse(tbta_file)

    print(f"Results found: {len(results)}")

    if results:
        print("\nSample results:")
        for i, (prefix, strong_num, features, verse_ref) in enumerate(results[:10]):
            print(f"  {i+1}. {prefix}{strong_num} @ {verse_ref}")
            print(f"     Features: {list(features.keys())}")
    else:
        print("\n⚠ No results - debugging further...\n")

        # Load and debug manually
        import json
        with open(tbta_file, 'r') as f:
            tbta_data = json.load(f)

        print(f"TBTA data type: {type(tbta_data)}")
        print(f"TBTA clauses: {len(tbta_data) if isinstance(tbta_data, list) else 1}")

        # Extract nodes manually
        position_counter = [0]
        tbta_nodes = []

        if isinstance(tbta_data, list):
            for clause in tbta_data:
                nodes = extract_tbta_nodes_from_clause(clause, position_counter)
                tbta_nodes.extend(nodes)
                print(f"Clause extracted {len(nodes)} nodes")

        print(f"\nTotal TBTA nodes extracted: {len(tbta_nodes)}")

        if tbta_nodes:
            print("\nSample nodes:")
            for node in tbta_nodes[:5]:
                print(f"  Position {node['position']}: {node['features']}")

if __name__ == "__main__":
    test_single_verse()
