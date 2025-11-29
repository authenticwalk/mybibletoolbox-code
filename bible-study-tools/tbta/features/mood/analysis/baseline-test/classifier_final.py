#!/usr/bin/env python3
"""
Final guided baseline - focuses on SEMANTIC meaning using cross-linguistic evidence.

Key insight: The simplified text + YLT translation are most reliable.
Cross-check with other translations for ambiguous cases.
"""

import json
import re
from collections import Counter


def has_conditional_structure(text, ylt):
    """Check if this is truly a conditional clause."""
    text_lower = text.lower()
    ylt_lower = ylt.lower()

    # Direct conditional markers in the simplified text
    if re.search(r'\bif\b', text_lower):
        return True

    # YLT conditional markers near the target
    if re.search(r'\bif\b.*\b(shall|will|may|might|do|doth)\b', ylt_lower[:200]):
        return True

    # Unless/lest patterns
    if any(w in ylt_lower for w in ['unless', 'lest', 'whether']):
        return True

    return False


def is_prohibition(text, ylt, translations):
    """Detect strong prohibitions (Forbidden Obligation)."""
    ylt_lower = ylt.lower()
    text_lower = text.lower()

    # Strong prohibition markers in YLT
    prohibition_patterns = [
        r'shall not', r'shalt not', r'do not', r'must not',
        r'let not', r'never', r'ye.*not'
    ]

    for pattern in prohibition_patterns:
        if re.search(pattern, ylt_lower):
            # Make sure "not" is in reasonable proximity
            return True

    return False


def is_command(text, ylt, translations):
    """Detect strong commands ('must' Obligation)."""
    ylt_lower = ylt.lower()

    # Command markers (not prohibition)
    if re.search(r'\bshall\b(?!\s*not)', ylt_lower):
        # "Shall do X" is a command
        if re.search(r'\bshall\s+(be|go|do|make|give|take|come)', ylt_lower):
            return True

    # Explicit commands
    if any(w in ylt_lower for w in ['must ', 'command', 'required']):
        return True

    return False


def is_permission(text, ylt):
    """Detect permissions ('may' permissive)."""
    ylt_lower = ylt.lower()

    # Permission markers
    if re.search(r'\bmay\s+(go|do|be|have|take)', ylt_lower):
        return True

    if re.search(r'\blet\s+(him|her|them|us)', ylt_lower):
        return True

    return False


def is_definite_future(ylt):
    """Detect assured future outcomes (Definite Potential)."""
    ylt_lower = ylt.lower()

    # Strong certainty markers
    if any(p in ylt_lower for p in ['will certainly', 'will surely', 'shall surely']):
        return True

    return False


def is_probable_future(text, ylt):
    """Detect likely future (Probable Potential) - not command."""
    ylt_lower = ylt.lower()

    # Future markers that aren't commands
    if re.search(r'\bwill\b(?!\s*not)', ylt_lower):
        # Check it's not a prohibition
        if 'shall' not in ylt_lower:  # "shall" usually = command
            return True

    return False


def classify_mood_final(entry):
    """
    Final guided classification using semantic analysis.

    Strategy:
    1. Check for specific non-indicative patterns
    2. Default to Indicative for factual narrative
    """

    text = entry.get('text', '')
    translations = entry.get('translations', {})
    ylt = translations.get('eng-YLT', '')
    verse_ref = entry.get('verse_ref', '')

    # Priority order (most specific to least specific):

    # 1. Forbidden Obligation - "shall not", "do not"
    if is_prohibition(text, ylt, translations):
        return 'Forbidden Obligation'

    # 2. Conditional = 'might' Potential
    if has_conditional_structure(text, ylt):
        return "'might' Potential"

    # 3. Permission = 'may' (permissive)
    if is_permission(text, ylt):
        return "'may' (permissive)"

    # 4. Strong command = 'must' Obligation
    if is_command(text, ylt, translations):
        return "'must' Obligation"

    # 5. Definite future = Definite Potential
    if is_definite_future(ylt):
        return 'Definite Potential'

    # 6. Probable future = Probable Potential
    if is_probable_future(text, ylt):
        return 'Probable Potential'

    # Default: Indicative (factual statements)
    # Most biblical text is narrative recounting of actual events
    return 'Indicative'


def main():
    input_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl'
    output_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_guided.txt'

    predictions = []

    with open(input_file, 'r') as f:
        for line in f:
            entry = json.loads(line)
            prediction = classify_mood_final(entry)
            predictions.append(prediction)

    # Write predictions
    with open(output_file, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    # Statistics
    print(f"Processed {len(predictions)} entries")
    print(f"Predictions written to {output_file}")
    print("\nPrediction distribution:")
    dist = Counter(predictions)
    for mood, count in sorted(dist.items(), key=lambda x: -x[1]):
        pct = 100 * count / len(predictions)
        print(f"  {mood}: {count} ({pct:.1f}%)")

    print(f"\nCategories predicted: {len(dist)} / 10")
    print(f"Categories NOT predicted:")
    all_cats = {
        'Indicative', "'must' Obligation", "'should' Obligation",
        "'should not' Obligation", 'Forbidden Obligation',
        "'might' Potential", "'may' (permissive)",
        'Definite Potential', 'Probable Potential', 'Unlikely Potential'
    }
    missing = all_cats - set(dist.keys())
    for cat in sorted(missing):
        print(f"  - {cat}")


if __name__ == '__main__':
    main()
