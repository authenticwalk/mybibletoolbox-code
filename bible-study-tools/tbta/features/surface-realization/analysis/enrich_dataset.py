#!/usr/bin/env python3
"""
Enrich draft dataset with strongs_number and reason_group fields.

This script:
1. Reads draft_datasets.jsonl/datasets.jsonl
2. For each entry:
   - Infers strongs_number from the constituent and strongs list
   - Assigns reason_group based on constituent type and context
   - Sets difficulty based on ambiguity and theological significance
3. Samples down to target size (max 1000 total: 800 train, 100 validate, 100 test)
4. Writes to datasets.jsonl
"""

import json
import re
from collections import defaultdict
from typing import Dict, List, Any

# Define reason groups based on research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml
REASON_GROUPS = {
    # Theological entities
    'GOD': ['God', 'Yahweh', 'Lord', 'Spirit', 'Holy Spirit'],
    'JESUS': ['Jesus', 'Christ', 'Son', 'Messiah', 'Savior', 'Master'],
    'DIVINE': ['angel', 'cherub', 'seraph', 'demon', 'Satan', 'devil'],

    # Proper names and titles
    'PERSON-NAME': ['David', 'Moses', 'Abraham', 'Peter', 'Paul', 'John', 'Mary',
                     'Nathanael', 'Pharaoh', 'Caesar'],
    'PLACE-NAME': ['Israel', 'Jerusalem', 'Egypt', 'Judah', 'Galilee', 'Babylon',
                   'Rome', 'Samaria'],
    'PEOPLE-GROUP': ['Israelite', 'Jew', 'Gentile', 'Pharisee', 'Sadducee',
                      'Samaritan', 'Roman', 'Greek'],

    # Generic human referents
    'HUMAN-ROLE': ['king', 'prophet', 'priest', 'disciple', 'apostle', 'servant',
                    'slave', 'soldier', 'scribe'],
    'HUMAN-KIN': ['son', 'daughter', 'father', 'mother', 'brother', 'sister',
                   'child', 'husband', 'wife'],
    'HUMAN-GENERIC': ['man', 'woman', 'person', 'people', 'one'],

    # Body parts (always realized as nouns in most languages)
    'BODY-PART': ['hand', 'foot', 'eye', 'ear', 'head', 'heart', 'mouth',
                   'face', 'body', 'arm', 'leg'],

    # Abstract concepts
    'ABSTRACT': ['word', 'truth', 'faith', 'love', 'hope', 'glory', 'wisdom',
                  'power', 'kingdom', 'covenant', 'law', 'commandment'],

    # Concrete objects
    'OBJECT': ['house', 'temple', 'altar', 'sword', 'stone', 'bread', 'water',
                'gold', 'silver', 'garment', 'book', 'scroll'],

    # Place concepts
    'LOCATION': ['city', 'land', 'mountain', 'valley', 'wilderness', 'sea',
                  'river', 'gate', 'field', 'garden'],

    # Time concepts
    'TIME': ['day', 'night', 'year', 'month', 'sabbath', 'feast', 'hour',
              'beginning', 'end'],

    # Collective entities
    'COLLECTIVE': ['army', 'assembly', 'congregation', 'nation', 'tribe',
                    'family', 'household'],

    # Catch-all
    'OTHER': ['thing', 'way', 'work', 'place']
}

def find_reason_group(constituent: str) -> str:
    """Find the reason_group for a constituent."""
    # Normalize for comparison
    const_lower = constituent.lower()

    # Check each group
    for group, keywords in REASON_GROUPS.items():
        for keyword in keywords:
            if keyword.lower() == const_lower or keyword.lower() in const_lower:
                return group

    # Default to OTHER
    return 'OTHER'

def infer_strongs_number(entry: Dict[str, Any]) -> str:
    """
    Infer the Strong's number for the constituent.

    Strategy:
    1. Parse the strongs field to get all codes
    2. Try to match the constituent word to a strongs code
    3. If multiple matches, prefer the first one
    4. Return the most likely code
    """
    strongs_str = entry.get('strongs', '')
    constituent = entry.get('constituent', '').lower()

    # Parse strongs codes
    # Format: "H0430-God H0853-(et) H1886a H8064"
    codes = []
    for token in strongs_str.split():
        match = re.match(r'([HG]\d{4}[a-z]?)', token)
        if match:
            code = match.group(1)
            # Extract gloss if present
            gloss_match = re.match(r'[HG]\d{4}[a-z]?-(.+)', token)
            gloss = gloss_match.group(1).lower() if gloss_match else ''
            codes.append((code, gloss))

    # Try to find a matching code by gloss
    for code, gloss in codes:
        if gloss and constituent in gloss:
            return code
        if gloss and gloss in constituent:
            return code

    # If no match, return first code (better than nothing)
    if codes:
        return codes[0][0]

    return ""

def assign_difficulty(entry: Dict[str, Any], reason_group: str) -> str:
    """
    Assign difficulty level based on context.

    Levels:
    - "" (blank/easy): Clear, unambiguous cases
    - "hard": Non-obvious factors (e.g., multiple same-gender participants)
    - "adversarial": Extremely challenging (e.g., ambiguous reference, theological nuance)
    """
    label = entry.get('label', '')
    constituent = entry.get('constituent', '').lower()

    # Personal Pronoun is adversarial (only 2 cases!)
    if label == 'Personal Pronoun':
        return 'adversarial'

    # "Always a Noun" is hard
    if label == 'Always a Noun':
        return 'hard'

    # Divine references are potentially hard (theological sensitivity)
    if reason_group in ['GOD', 'JESUS', 'DIVINE']:
        return 'hard'

    # Person names in narratives can be hard (ambiguous reference)
    if reason_group == 'PERSON-NAME':
        return 'hard'

    # Default to easy (blank)
    return ''

def main():
    input_file = '/workspace/bible-study-tools/tbta/features/surface-realization/analysis/draft_datasets.jsonl/datasets.jsonl'
    output_file = '/workspace/bible-study-tools/tbta/features/surface-realization/analysis/datasets.jsonl'

    print(f"Reading draft dataset from {input_file}")

    # Read all entries
    entries = []
    with open(input_file) as f:
        for line in f:
            entry = json.loads(line)
            entries.append(entry)

    print(f"Loaded {len(entries)} entries")

    # Group by split and label
    by_split_label = defaultdict(list)
    for entry in entries:
        split = entry['dataset']['split']
        label = entry['label']
        by_split_label[(split, label)].append(entry)

    # Sample to target sizes
    # Strategy: Keep ALL rare labels, sample Noun to fill up to target
    target_sizes = {
        'train': 800,
        'validate': 100,
        'test': 100
    }

    sampled = []
    for split, max_size in target_sizes.items():
        # First, add all rare labels (Always a Noun, Personal Pronoun)
        rare_entries = []
        rare_entries.extend(by_split_label.get((split, 'Always a Noun'), []))
        rare_entries.extend(by_split_label.get((split, 'Personal Pronoun'), []))

        # Then fill up to max_size with Noun entries
        noun_entries = by_split_label.get((split, 'Noun'), [])
        needed = max_size - len(rare_entries)
        if needed > 0:
            noun_entries = noun_entries[:needed]
        else:
            noun_entries = []

        split_entries = rare_entries + noun_entries
        sampled.extend(split_entries)

    print(f"Sampled down to {len(sampled)} entries")
    print(f"  train: {len([e for e in sampled if e['dataset']['split'] == 'train'])}")
    print(f"  validate: {len([e for e in sampled if e['dataset']['split'] == 'validate'])}")
    print(f"  test: {len([e for e in sampled if e['dataset']['split'] == 'test'])}")

    # Enrich each entry
    enriched = []
    for entry in sampled:
        # Add strongs_number
        strongs_number = infer_strongs_number(entry)

        # Add reason_group
        reason_group = find_reason_group(entry['constituent'])

        # Add difficulty
        difficulty = assign_difficulty(entry, reason_group)

        # Create enriched entry
        enriched_entry = {
            'verse': entry['verse'],
            'label': entry['label'],
            'constituent': entry['constituent'],
            'part': entry['part'],
            'reconstructed_verse': entry.get('text', ''),  # Rename text to reconstructed_verse
            'strongs': entry.get('strongs', ''),
            'strongs_number': strongs_number,
            'dataset': {
                'split': entry['dataset']['split'],
                'section': entry['dataset']['section'],
                'literary_type': entry['dataset']['literary_type'],
                'difficulty': difficulty,
                'reason_group': reason_group
            }
        }

        enriched.append(enriched_entry)

    # Write to output
    print(f"Writing enriched dataset to {output_file}")
    with open(output_file, 'w') as f:
        for entry in enriched:
            f.write(json.dumps(entry) + '\n')

    # Print summary statistics
    print("\nSummary:")
    print(f"Total entries: {len(enriched)}")

    # Count by reason_group
    reason_counts = defaultdict(int)
    for entry in enriched:
        reason_counts[entry['dataset']['reason_group']] += 1

    print("\nReason group distribution:")
    for reason, count in sorted(reason_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {reason}: {count}")

    # Count by label
    label_counts = defaultdict(int)
    for entry in enriched:
        label_counts[entry['label']] += 1

    print("\nLabel distribution:")
    for label, count in sorted(label_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {label}: {count}")

    print(f"\nDone! Enriched dataset written to {output_file}")

if __name__ == '__main__':
    main()
