#!/usr/bin/env python3
"""
Baseline guided mood classifier for TBTA mood feature.

This classifier uses semantic analysis of the text, translations, and Strong's
numbers to predict grammatical mood categories.
"""

import json
import re
from collections import Counter


def classify_mood(entry):
    """
    Classify grammatical mood based on semantic meaning.

    Categories:
    - Indicative: Factual statements
    - 'must' Obligation: Strong necessity (divine commands, laws)
    - 'should' Obligation: Moderate advice
    - 'should not' Obligation: Negative advice
    - Forbidden Obligation: Strong prohibition
    - 'might' Potential: Uncertain possibility
    - 'may' (permissive): Permission granted
    - Definite Potential: Certain capability
    - Probable Potential: Likely outcome
    - Unlikely Potential: Improbable but possible
    """

    text = entry.get('text', '').lower()
    strongs = entry.get('strongs', '').lower()
    gloss = entry.get('gloss', '').lower()
    translations = entry.get('translations', {})

    # Get the bolded target word
    bold_match = re.search(r'\*\*([^*]+)\*\*', entry.get('text', ''))
    target_word = bold_match.group(1).lower() if bold_match else ''

    # Combine all translation texts for semantic analysis
    all_trans = ' '.join(translations.values()).lower()
    combined = text + ' ' + all_trans + ' ' + gloss

    # Strong prohibition patterns (Forbidden Obligation)
    forbidden_patterns = [
        r'shall not', r'shalt not', r'must not', r'do not',
        r'you shall not', r'thou shalt not', r'never',
        r'forbidden', r'prohibited', r'\bnot\s+' + re.escape(target_word)
    ]
    if any(re.search(p, combined) for p in forbidden_patterns):
        # Check context - make sure it's prohibiting the action
        if re.search(r'\b(not|never|no)\b', text):
            return 'Forbidden Obligation'

    # Strong commands (must Obligation)
    must_patterns = [
        r'\bmust\b', r'\bshall\b(?!\s+not)', r'\bcommand',
        r'\brequired\b', r'\bobliged\b', r'\bcompulsory\b'
    ]
    if any(re.search(p, combined) for p in must_patterns):
        return "'must' Obligation"

    # Negative advice (should not Obligation)
    if re.search(r'\bshould\s+not\b|\bought\s+not\b', combined):
        return "'should not' Obligation"

    # Positive advice (should Obligation)
    if re.search(r'\bshould\b|\bought\s+to\b|\badvisable\b', combined):
        return "'should' Obligation"

    # Permission (may permissive)
    permission_patterns = [
        r'\bmay\s+(?:do|be|have)\b', r'\ballowed\b', r'\bpermitted\b',
        r'\bcan\s+(?:do|be|have)\b', r'\bfree\s+to\b', r'\byou\s+may\b'
    ]
    if any(re.search(p, combined) for p in permission_patterns):
        # Make sure it's not conditional
        if not re.search(r'\bif\b|\bperhaps\b|\bmaybe\b', text):
            return "'may' (permissive)"

    # Definite potential (certain future)
    definite_patterns = [
        r'\bwill\s+certainly\b', r'\bwill\s+surely\b', r'\bshall\s+be\b',
        r'\bassured\b', r'\binevitably\b', r'\bdefinitely\s+will\b'
    ]
    if any(re.search(p, combined) for p in definite_patterns):
        return 'Definite Potential'

    # Unlikely potential
    if re.search(r'\bunlikely\b|\bimprobable\b|\bhardly\b|\bscarcely\b', combined):
        return 'Unlikely Potential'

    # Uncertain possibility (might Potential)
    might_patterns = [
        r'\bmight\b', r'\bmaybe\b', r'\bperhaps\b', r'\bpossibly\b',
        r'\bcould\s+be\b', r'\bif\s+.*\s+' + re.escape(target_word),
        r'\bif\b.*\b(might|may|could)\b'
    ]
    if any(re.search(p, combined) for p in might_patterns):
        return "'might' Potential"

    # Probable potential (likely future)
    probable_patterns = [
        r'\bwill\b(?!\s+not)', r'\bwould\b', r'\bgoing\s+to\b',
        r'\blikely\b', r'\bprobably\b', r'\bexpected\s+to\b'
    ]
    if any(re.search(p, combined) for p in probable_patterns):
        return 'Probable Potential'

    # Default: Indicative (factual statement)
    return 'Indicative'


def main():
    input_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl'
    output_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_guided.txt'

    predictions = []

    with open(input_file, 'r') as f:
        for line in f:
            entry = json.loads(line)
            prediction = classify_mood(entry)
            predictions.append(prediction)

    # Write predictions
    with open(output_file, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    # Show statistics
    print(f"Processed {len(predictions)} entries")
    print(f"Predictions written to {output_file}")
    print("\nPrediction distribution:")
    dist = Counter(predictions)
    for mood, count in sorted(dist.items(), key=lambda x: -x[1]):
        print(f"  {mood}: {count}")


if __name__ == '__main__':
    main()
