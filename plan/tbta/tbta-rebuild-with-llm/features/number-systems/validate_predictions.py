#!/usr/bin/env python3
"""
Validate number-systems predictions against TBTA data.
"""

import json
from pathlib import Path

# Test verse mappings to TBTA files
VERSE_MAPPINGS = {
    # Adversarial test set
    'Gen 41:40': {
        'file': 'genesis_041_040.json',
        'prediction': 'Singular',
        'target': 'my people (עַמִּי)',
        'confidence': 'Medium'
    },
    'Gen 22:6': {
        'file': 'genesis_022_006.json',
        'prediction': 'Dual',
        'target': 'both of them (שְׁנֵיהֶם)',
        'confidence': 'High'
    },
    'Exod 4:11': {
        'file': 'exodus_004_011.json',
        'prediction': 'Singular',
        'target': 'blind (עִוֵּר)',
        'confidence': 'High'
    },
    # Random test set
    'Gen 1:26': {
        'file': 'genesis_001_026.json',
        'prediction': 'Trial',
        'target': 'God as speaker ("us")',
        'confidence': 'High'
    },
    'Gen 1:27': {
        'file': 'genesis_001_027.json',
        'prediction': 'Dual',
        'target': 'them (אֹתָם)',
        'confidence': 'High'
    },
    'Gen 18:2': {
        'file': 'genesis_018_002.json',
        'prediction': 'Plural',
        'target': 'three men (שְׁלֹשָׁה)',
        'confidence': 'Low'
    },
    'Gen 7:13': {
        'file': 'genesis_007_013.json',
        'prediction': 'Plural',
        'target': '8 persons (Noah\'s family)',
        'confidence': 'Medium-Low'
    },
}

def extract_numbers(element, results=None):
    if results is None:
        results = []

    constituent = element.get('Constituent', '')
    number = element.get('Number', '')
    part = element.get('Part', '')

    if number and number != 'Unspecified':
        results.append({
            'constituent': constituent,
            'number': number,
            'part': part
        })

    if 'Children' in element:
        for child in element['Children']:
            extract_numbers(child, results)

    return results

def main():
    samples_dir = Path('/home/user/mybibletoolbox-code/plan/tbta-rebuild-with-llm/tbta-data/samples')

    print("\n" + "="*80)
    print("TBTA Validation Results")
    print("="*80 + "\n")

    correct = 0
    total = 0

    for verse, info in VERSE_MAPPINGS.items():
        file_path = samples_dir / info['file']

        if not file_path.exists():
            print(f"{verse}: TBTA data not available")
            continue

        with open(file_path, 'r') as f:
            data = json.load(f)

        all_numbers = []
        for clause in data:
            all_numbers.extend(extract_numbers(clause))

        print(f"\n{verse}: {info['target']}")
        print(f"  Predicted: {info['prediction']} (Confidence: {info['confidence']})")
        print(f"  TBTA annotations found:")

        # Show all Number annotations
        value_counts = {}
        for item in all_numbers:
            val = item['number']
            value_counts[val] = value_counts.get(val, 0) + 1

        for val, count in sorted(value_counts.items()):
            print(f"    {val}: {count}x")

        # Simple validation logic - check if prediction appears in annotations
        if any(item['number'] == info['prediction'] for item in all_numbers):
            print(f"  Result: ✓ POSSIBLE MATCH (prediction found in verse)")
            correct += 1
        else:
            print(f"  Result: ✗ NO MATCH (prediction not found)")

        total += 1

    print(f"\n{'='*80}")
    print(f"Summary: {correct}/{total} verses with possible matches")
    print(f"Note: These are preliminary results - manual review required for exact constituent matching")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()
