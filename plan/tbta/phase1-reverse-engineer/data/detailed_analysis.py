#!/usr/bin/env python3
"""
Detailed analysis of clause segmentation patterns with specific examples.
"""

import csv
import re
from pathlib import Path

def analyze_detailed():
    """Provide detailed analysis with specific examples."""

    data_dir = Path('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data')

    print("=" * 80)
    print("DETAILED CLAUSE SEGMENTATION ANALYSIS")
    print("=" * 80)

    # Read some verses from Ruth and Matthew
    ruth_verses = []
    with open(data_dir / 'Ruth.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        ruth_verses = list(reader)

    matthew_verses = []
    with open(data_dir / 'Matthew.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        matthew_verses = list(reader)

    print("\n### PATTERN 1: Compound Sentences Split by Conjunctions")
    print("=" * 80)
    print("\nOriginal compound sentences (typically with 'and', 'but') are split into")
    print("separate simple sentences, with the conjunction moved to the start of the new sentence.\n")

    examples = [
        ("Ruth 1:2", ruth_verses[1]['Verse']),
        ("Ruth 1:4", ruth_verses[3]['Verse']),
        ("Ruth 2:3", ruth_verses[17]['Verse']),
        ("Matthew 7:7", matthew_verses[156]['Verse']),
        ("Matthew 8:4", matthew_verses[176]['Verse']),
    ]

    for ref, verse in examples:
        sentences = [s.strip() for s in re.split(r'\.\s+|\.$', verse) if s.strip()]
        print(f"{ref}:")
        for i, sent in enumerate(sentences, 1):
            # Clean markup for readability
            clean = re.sub(r'\([^)]*\)', '', sent)
            clean = re.sub(r'\[[^\]]*\]', '[...]', clean)
            clean = re.sub(r'_\w+', '', clean)
            clean = re.sub(r'\s+', ' ', clean).strip()

            # Check for conjunction
            is_conj = bool(re.match(r'^(And|But|Or|So|Then|For)\b', sent, re.IGNORECASE))
            marker = " ← CONJUNCTION START" if is_conj else ""

            if len(clean) > 90:
                print(f"  {i}. {clean[:90]}...{marker}")
            else:
                print(f"  {i}. {clean}{marker}")
        print()

    print("\n### PATTERN 2: One Verb/Action Per Sentence")
    print("=" * 80)
    print("\nComplex sentences with multiple verbs are broken into simple sentences")
    print("with typically one main verb per sentence.\n")

    # Look for specific examples
    one_verb_examples = [
        ("Ruth 1:14", "Multiple actions: cried, kissed, goodbye, returned, refused"),
        ("Ruth 2:9", "Multiple imperatives: watch, follow, go, drink"),
        ("Ruth 3:3", "Sequence of actions: wash, put oil, put on clothes, go, wait"),
        ("Matthew 8:4", "Series of commands: listen, do not tell, go, show, give"),
        ("Matthew 8:15", "Sequence: touched, stopped fever, get-up, serve"),
    ]

    for ref, description in one_verb_examples:
        verse_idx = int(ref.split()[1].split(':')[1]) - 1
        book = ref.split()[0]

        if book == "Ruth":
            verse = ruth_verses[verse_idx]['Verse']
        else:
            # Find in Matthew
            for v in matthew_verses:
                if v['Reference'] == ref:
                    verse = v['Verse']
                    break

        sentences = [s.strip() for s in re.split(r'\.\s+|\.$', verse) if s.strip()]

        print(f"{ref} - {description}:")
        for i, sent in enumerate(sentences, 1):
            clean = re.sub(r'\([^)]*\)', '', sent)
            clean = re.sub(r'\[[^\]]*\]', '[...]', clean)
            clean = re.sub(r'_\w+', '', clean)
            clean = re.sub(r'\s+', ' ', clean).strip()

            if len(clean) > 90:
                print(f"  {i}. {clean[:90]}...")
            else:
                print(f"  {i}. {clean}")
        print()

    print("\n### PATTERN 3: Sequential Actions Become Sequential Sentences")
    print("=" * 80)
    print("\nNarrative sequences are broken into individual sentences, often with")
    print("'Then', 'And', or 'So' marking the progression.\n")

    sequential = [
        ("Ruth 2:10", "Ruth's physical actions in sequence"),
        ("Ruth 2:14", "Boaz's instructions and Ruth's actions"),
        ("Matthew 8:23", "Jesus entering boat, disciples following"),
        ("Matthew 9:7", "Man getting up and going home"),
    ]

    for ref, description in sequential:
        verse_idx = int(ref.split()[1].split(':')[1]) - 1
        book = ref.split()[0]

        if book == "Ruth":
            verse = ruth_verses[verse_idx]['Verse']
        else:
            for v in matthew_verses:
                if v['Reference'] == ref:
                    verse = v['Verse']
                    break

        sentences = [s.strip() for s in re.split(r'\.\s+|\.$', verse) if s.strip()]

        print(f"{ref} - {description}:")
        for i, sent in enumerate(sentences, 1):
            clean = re.sub(r'\([^)]*\)', '', sent)
            clean = re.sub(r'\[[^\]]*\]', '[...]', clean)
            clean = re.sub(r'_\w+', '', clean)
            clean = re.sub(r'\s+', ' ', clean).strip()

            is_conj = bool(re.match(r'^(And|But|Then|So)\b', sent, re.IGNORECASE))
            marker = " ← Sequential marker" if is_conj else ""

            if len(clean) > 90:
                print(f"  {i}. {clean[:90]}...{marker}")
            else:
                print(f"  {i}. {clean}{marker}")
        print()

    print("\n### PATTERN 4: Subordinate Clauses Remain Embedded")
    print("=" * 80)
    print("\nNOT ALL complex structures are segmented. Subordinate clauses and")
    print("relative clauses (marked with brackets [...]) typically remain within")
    print("their parent sentence. These are COUNTER-EXAMPLES to segmentation.\n")

    counter_examples = [
        ("Ruth 1:1", "[When judges were ruling Israel] - temporal clause"),
        ("Ruth 1:1", "[who were living in Israel] - relative clause"),
        ("Ruth 1:4", "[that were from Moab] - relative clause"),
        ("Ruth 2:3", "[who were gathering/harvesting grain] - relative clause"),
        ("Matthew 5:1", "[When Jesus saw the crowds] - temporal clause"),
        ("Matthew 7:16", "[by looking at the fruit [that those people produce]] - nested clauses"),
        ("Matthew 8:2", "[who had leprosy] - relative clause"),
        ("Matthew 8:8", "[for you(Jesus) to come into my(officer's) house] - purpose clause"),
    ]

    for ref, description in counter_examples:
        book = ref.split()[0]
        verse_idx = int(ref.split()[1].split(':')[1]) - 1

        if book == "Ruth":
            verse = ruth_verses[verse_idx]['Verse']
        else:
            for v in matthew_verses:
                if v['Reference'] == ref:
                    verse = v['Verse']
                    break

        sentences = [s.strip() for s in re.split(r'\.\s+|\.$', verse) if s.strip()]

        print(f"{ref} - {description}")
        # Find sentence with the pattern
        for sent in sentences:
            if re.search(r'\[', sent):
                clean = re.sub(r'\([^)]*\)', '', sent)
                clean = re.sub(r'_\w+', '', clean)
                clean = re.sub(r'\s+', ' ', clean).strip()

                if len(clean) > 100:
                    print(f"  → {clean[:100]}...")
                else:
                    print(f"  → {clean}")
                break
        print()

    print("\n### PATTERN 5: Conditional Structures Preserved")
    print("=" * 80)
    print("\nConditional structures (if...then) are preserved within sentences")
    print("rather than being split. Another COUNTER-EXAMPLE to segmentation.\n")

    conditionals = [
        ("Ruth 1:16", "[if you(Naomi) travel to a place] I(Ruth) will also travel"),
        ("Ruth 1:16", "[if you(Naomi) live in a place] I(Ruth) will also live"),
        ("Matthew 7:6", "[If you(people) do that thing] those dogs might turn-around"),
        ("Ruth 2:9", "[Whenever you(Ruth) become thirsty] you(Ruth) (imp) go"),
    ]

    for ref, description in conditionals:
        book = ref.split()[0]
        verse_ref = ref.split()[1]

        if book == "Ruth":
            for v in ruth_verses:
                if v['Reference'] == ref:
                    verse = v['Verse']
                    break
        else:
            for v in matthew_verses:
                if v['Reference'] == ref:
                    verse = v['Verse']
                    break

        sentences = [s.strip() for s in re.split(r'\.\s+|\.$', verse) if s.strip()]

        print(f"{ref} - Conditional preserved in sentence")
        for sent in sentences:
            if '[if ' in sent.lower() or '[whenever ' in sent.lower():
                clean = re.sub(r'\([^)]*\)', '', sent)
                clean = re.sub(r'_\w+', '', clean)
                clean = re.sub(r'\s+', ' ', clean).strip()

                if len(clean) > 100:
                    print(f"  → {clean[:100]}...")
                else:
                    print(f"  → {clean}")
        print()

if __name__ == '__main__':
    analyze_detailed()
