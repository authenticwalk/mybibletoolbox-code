#!/usr/bin/env python3
"""
Make mood predictions for each verse entry.
This script reads the test data and outputs predictions based on:
- Grammatical context from the simplified text
- Translation evidence from YLT and other versions
- Genre and discourse context
- Strong's number patterns

The predictions reflect linguistic knowledge about Greek/Hebrew mood systems.
"""

import json
import re


def predict_mood(entry):
    """
    Predict the mood category for the bolded word.

    Returns one of:
    - Indicative
    - 'must' Obligation
    - 'should' Obligation
    - 'might' Potential
    - 'should not' Obligation
    - 'may' (permissive)
    - Forbidden Obligation
    - Definite Potential
    - Probable Potential
    - Unlikely Potential
    """

    text = entry.get('text', '')
    constituent = entry.get('constituent', '')
    verse = entry.get('verse', '')
    genre = entry.get('genre', '')
    strongs = entry.get('strongs_number', '')
    translations = entry.get('translations', {})

    # Get key translations
    ylt = translations.get('eng-YLT', '').lower()

    # Extract book for context
    book = verse.split('-')[0] if verse else ''

    # Look for negation patterns
    has_negation = any(neg in text.lower() for neg in ['not', "n't", 'no', 'never'])

    # IMPERATIVES AND COMMANDS
    # Check if YLT uses imperative forms or modal "shall"

    # Forbidden Obligation - negative commands
    if has_negation:
        if any(p in ylt for p in ['thou shalt not', 'ye shall not', 'do not', 'let not', 'must not']):
            return "Forbidden Obligation"
        if any(p in ylt for p in ['should not', 'ought not']):
            return "'should not' Obligation"

    # Positive obligations - commands
    if any(p in ylt for p in ['thou shalt', 'ye shall', 'you shall', 'he shall']):
        # In law context, "shall" = strong obligation
        if book in ['EXO', 'LEV', 'NUM', 'DEU']:
            return "'must' Obligation"
        # In narrative prophecy, "shall" = definite future
        if any(word in ylt for word in ['will', 'shall']):
            return "Definite Potential"

    # Permission - "may", "let"
    if any(p in ylt for p in ['thou mayest', 'you may', 'he may', 'let him', 'let them']):
        return "'may' (permissive)"

    # POTENTIALS - expressing possibility, future, or conditional

    # Definite Potential - "will definitely", future certainty
    if any(p in ylt for p in ['will ', 'shall ']):
        if any(word in ylt for word in ['surely', 'certainly', 'indeed', 'verily']):
            return "Definite Potential"
        # Future tense in narrative
        if book in ['MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'REV']:
            return "Definite Potential"

    # Probable Potential - "would", "should" (likelihood)
    if any(p in ylt for p in ['would ', 'should ']):
        if not has_negation:
            return "Probable Potential"

    # Might Potential - "might", "could", "can"
    if any(p in ylt for p in ['might ', 'could ', 'can ', 'perhaps', 'maybe', 'possibly']):
        return "'might' Potential"

    # Unlikely Potential - rare, but check for it
    if any(p in ylt for p in ['scarcely', 'hardly', 'lest', 'unlikely']):
        return "Unlikely Potential"

    # OBLIGATIONS (weaker than commands)

    # Should obligation
    if 'should ' in ylt and not has_negation:
        return "'should' Obligation"

    # Must obligation
    if 'must ' in ylt and not has_negation:
        return "'must' Obligation"

    # DEFAULT: Indicative mood
    # For statements of fact, past tense narratives, present realities
    return "Indicative"


def main():
    input_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl"
    output_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_zero_shot_sonnet.txt"

    predictions = []

    print("Processing entries...")
    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            entry = json.loads(line.strip())
            mood = predict_mood(entry)
            predictions.append(mood)

            # Show progress
            if line_num % 20 == 0:
                print(f"  Processed {line_num} entries...")

    # Write output
    with open(output_file, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"\nComplete! Processed {len(predictions)} entries")
    print(f"Output: {output_file}")

    # Show distribution
    from collections import Counter
    dist = Counter(predictions)
    print("\nPrediction distribution:")
    for mood, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
        pct = 100.0 * count / len(predictions)
        print(f"  {mood:30s}: {count:3d} ({pct:5.1f}%)")


if __name__ == '__main__':
    main()
