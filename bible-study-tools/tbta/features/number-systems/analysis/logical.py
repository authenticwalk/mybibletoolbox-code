#!/usr/bin/env python3
"""
Number Systems Logical Classifier
=================================

A simple rule-based classifier for TBTA Number System feature.

Based on the data analysis:
- Singular: 66.2% of annotations
- Plural: 32.4%
- Dual: 1.0% (body parts, paired items)
- Trial: 0.3% (Trinity contexts, triplets)
- Quadrial: 0.1% (SHOULD BE 0% - no linguistic attestation)
- Paucal: 0.03%

Rules derived from constituency patterns:
1. Body parts in pairs → Dual (hand, foot, eye, leg, ear)
2. Proper names/God references → Singular (Jesus, Yahweh, David, God)
3. Collective nouns → Plural (israelite, people, etc.)
4. Default → Based on context or Singular
"""

import json
import sys
from pathlib import Path
from collections import Counter

# Body parts that come in pairs - should be DUAL
DUAL_CONSTITUENTS = {
    'hand', 'hands', 'foot', 'feet', 'eye', 'eyes', 'ear', 'ears',
    'leg', 'legs', 'arm', 'arms', 'wing', 'wings', 'horn', 'horns',
    'shoulder', 'shoulders', 'knee', 'knees', 'cheek', 'cheeks',
    'side', 'sides', 'nostril', 'nostrils', 'lip', 'lips'
}

# Proper nouns/divine names - should be SINGULAR
SINGULAR_CONSTITUENTS = {
    'jesus', 'christ', 'yahweh', 'god', 'lord', 'david', 'moses',
    'paul', 'peter', 'abraham', 'isaac', 'jacob', 'mary', 'joseph',
    'spirit', 'father', 'son', 'pharaoh', 'king', 'man', 'woman',
    'child', 'son', 'daughter', 'servant', 'lord'
}

# Collective/group terms - should be PLURAL
PLURAL_CONSTITUENTS = {
    'israelite', 'israelites', 'people', 'peoples', 'nations',
    'disciples', 'apostles', 'pharisees', 'scribes', 'priests',
    'elders', 'soldiers', 'servants', 'children', 'sons', 'daughters',
    'men', 'women', 'brothers', 'sisters', 'gentiles', 'jews'
}


def predict(entry: dict) -> str:
    """
    Predict number label based on constituent word.

    Args:
        entry: Dict with 'constituent', 'part', 'verse' keys

    Returns:
        Predicted label: Singular, Dual, Trial, Plural, Paucal
    """
    constituent = entry.get('constituent', '').lower().strip()

    # Rule 1: Body parts in pairs → Dual
    for dual_word in DUAL_CONSTITUENTS:
        if dual_word in constituent:
            return 'Dual'

    # Rule 2: Proper names → Singular
    for singular_word in SINGULAR_CONSTITUENTS:
        if singular_word in constituent:
            return 'Singular'

    # Rule 3: Collective nouns → Plural
    for plural_word in PLURAL_CONSTITUENTS:
        if plural_word in constituent:
            return 'Plural'

    # Rule 4: Default → Singular (66% baseline)
    return 'Singular'


def evaluate(data_file: Path):
    """Evaluate classifier on dataset."""
    correct = 0
    total = 0
    predictions = Counter()
    actuals = Counter()

    with open(data_file, 'r') as f:
        for line in f:
            entry = json.loads(line)
            actual = entry['label']
            predicted = predict(entry)

            predictions[predicted] += 1
            actuals[actual] += 1

            if predicted == actual:
                correct += 1
            total += 1

    accuracy = correct / total if total > 0 else 0
    return accuracy, predictions, actuals


def main():
    """Run evaluation on train, validate, test sets."""
    base_dir = Path(__file__).parent / 'data'

    print("=" * 60)
    print("NUMBER SYSTEMS LOGICAL CLASSIFIER EVALUATION")
    print("=" * 60)

    for split in ['train', 'validate', 'test']:
        data_file = base_dir / f'{split}.jsonl'
        if not data_file.exists():
            print(f"\n{split}: File not found")
            continue

        accuracy, predictions, actuals = evaluate(data_file)
        print(f"\n{split.upper()}:")
        print(f"  Accuracy: {accuracy:.1%}")
        print(f"  Predictions: {dict(predictions)}")
        print(f"  Actuals:     {dict(actuals)}")

    print("\n" + "=" * 60)
    print("ANALYSIS")
    print("=" * 60)
    print("""
Note: This classifier uses simple constituent word matching.
On the balanced test set, accuracy is limited because:
1. The balanced sample over-represents rare labels (Trial, Quadrial)
2. Simple word matching doesn't capture context

On the FULL dataset:
- Majority baseline (Singular): 66.2%
- This classifier likely achieves ~70-75% by catching:
  - Dual body parts
  - Plural collective nouns
  - Singular proper names

For production use:
- Consider embedding-based classifier for complex cases
- Use this as a baseline/sanity check
- Focus classifier effort on Dual/Trial detection (rare but important)
""")


if __name__ == "__main__":
    main()
