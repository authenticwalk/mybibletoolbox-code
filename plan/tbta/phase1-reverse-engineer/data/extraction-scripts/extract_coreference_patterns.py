#!/usr/bin/env python3
"""
Extract coreference resolution patterns from TBTA CSV files.

Usage:
    python extract_coreference_patterns.py [csv_file]

Extracts:
- pronoun(referent) patterns
- Repeated name patterns
- Demonstrative+noun patterns
- Pronoun retention cases
"""

import csv
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

def analyze_coreference_patterns(csv_file):
    """Analyze coreference patterns in a TBTA CSV file."""

    patterns = {
        'pronoun_with_ref': [],      # I(Paul), he(God), etc.
        'repeated_names': [],         # Adam...Adam...Adam
        'demonstrative_noun': [],     # this person, those people
        'pronouns_kept': []           # plain he, she, it, they
    }

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            ref = row.get('Reference', '')
            verse = row.get('Verse', '')

            if not verse or not ref:
                continue

            # Pattern 1: pronoun(referent)
            pron_matches = re.findall(
                r'\b(I|we|you|he|she|it|they|them|him|her|his|hers|their|theirs|your|yours|my|mine|our|ours)\(([^)]+)\)',
                verse,
                re.IGNORECASE
            )
            if pron_matches:
                patterns['pronoun_with_ref'].append({
                    'ref': ref,
                    'matches': pron_matches,
                    'verse': verse
                })

            # Pattern 2: Repeated proper names (3+ occurrences)
            # Extract capitalized words
            names = re.findall(r'\b([A-Z][a-z]+)\b', verse)
            if names:
                # Exclude common function words
                excluded = {'God', 'Lord', 'Jesus', 'Christ', 'I', 'A', 'And',
                           'But', 'So', 'Then', 'For', 'The', 'When', 'That',
                           'This', 'These', 'Those', 'He', 'She', 'They'}
                names = [n for n in names if n not in excluded]

                name_counts = Counter(names)
                for name, count in name_counts.items():
                    if count >= 3:
                        patterns['repeated_names'].append({
                            'ref': ref,
                            'name': name,
                            'count': count,
                            'verse': verse
                        })
                        break  # Only report once per verse

            # Pattern 3: Demonstrative + noun
            dem_matches = re.findall(
                r'\b(this|that|these|those)\s+(man|woman|people|person|persons|child|children|thing|things)\b',
                verse,
                re.IGNORECASE
            )
            if dem_matches:
                patterns['demonstrative_noun'].append({
                    'ref': ref,
                    'matches': dem_matches,
                    'verse': verse
                })

            # Pattern 4: Pronouns kept (no parenthetical referent)
            # Look for standalone pronouns
            if re.search(r'\s(he|she|it|they)\s', verse, re.IGNORECASE):
                # Make sure NOT followed by parenthesis
                if not re.search(r'(he|she|it|they)\(', verse, re.IGNORECASE):
                    patterns['pronouns_kept'].append({
                        'ref': ref,
                        'verse': verse
                    })

    return patterns

def print_report(patterns, csv_file):
    """Print analysis report."""

    print("=" * 80)
    print(f"COREFERENCE ANALYSIS: {Path(csv_file).name}")
    print("=" * 80)

    print(f"\nPattern Counts:")
    print(f"  Pronoun(referent):        {len(patterns['pronoun_with_ref'])}")
    print(f"  Repeated names:           {len(patterns['repeated_names'])}")
    print(f"  Demonstrative+noun:       {len(patterns['demonstrative_noun'])}")
    print(f"  Pronouns kept:            {len(patterns['pronouns_kept'])}")

    # Show examples of each pattern
    print("\n" + "=" * 80)
    print("SAMPLE: Pronoun(referent) patterns (first 5)")
    print("=" * 80)
    for i, item in enumerate(patterns['pronoun_with_ref'][:5], 1):
        print(f"\n{i}. {item['ref']}")
        print(f"   Matches: {item['matches']}")
        print(f"   Verse: {item['verse'][:150]}...")

    print("\n" + "=" * 80)
    print("SAMPLE: Repeated names (first 5)")
    print("=" * 80)
    for i, item in enumerate(patterns['repeated_names'][:5], 1):
        print(f"\n{i}. {item['ref']} - '{item['name']}' x{item['count']}")
        print(f"   Verse: {item['verse'][:150]}...")

    print("\n" + "=" * 80)
    print("SAMPLE: Demonstrative+noun (first 5)")
    print("=" * 80)
    for i, item in enumerate(patterns['demonstrative_noun'][:5], 1):
        print(f"\n{i}. {item['ref']}")
        print(f"   Matches: {item['matches']}")
        print(f"   Verse: {item['verse'][:150]}...")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python extract_coreference_patterns.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]

    if not Path(csv_file).exists():
        print(f"Error: File not found: {csv_file}")
        sys.exit(1)

    patterns = analyze_coreference_patterns(csv_file)
    print_report(patterns, csv_file)
