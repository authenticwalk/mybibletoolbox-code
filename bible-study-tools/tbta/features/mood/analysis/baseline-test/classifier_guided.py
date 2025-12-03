#!/usr/bin/env python3
"""
Guided baseline mood classifier - uses value definitions + cross-linguistic analysis.

This is a GUIDED baseline that uses:
1. Explicit value definitions provided
2. Cross-linguistic evidence from 12+ translations
3. Semantic context and genre
4. Source language Strong's numbers
"""

import json
import re
from collections import Counter


def analyze_translations(translations):
    """Extract modal patterns from multilingual translations."""
    patterns = {
        'prohibition': [],
        'command': [],
        'permission': [],
        'conditional': [],
        'future': [],
        'advice': []
    }

    for lang, text in translations.items():
        text_lower = text.lower()

        # Prohibitions (strong negation)
        if any(p in text_lower for p in ['shall not', 'shalt not', 'must not', 'do not', 'nicht', 'ne pas', 'non', 'no']):
            patterns['prohibition'].append(lang)

        # Commands (imperatives)
        if any(p in text_lower for p in ['must', 'shall', 'command', 'doit', 'muss', 'debe']):
            patterns['command'].append(lang)

        # Permission
        if any(p in text_lower for p in ['may', 'can', 'let', 'allowed', 'permitted', 'peut', 'darf', 'puede']):
            patterns['permission'].append(lang)

        # Conditional
        if any(p in text_lower for p in ['if', 'unless', 'lest', 'si ', 'wenn', 'se ']):
            patterns['conditional'].append(lang)

        # Future
        if any(p in text_lower for p in ['will', 'shall', 'going to', 'sera', 'wird', 'será']):
            patterns['future'].append(lang)

        # Advice
        if any(p in text_lower for p in ['should', 'ought', 'better', 'devrait', 'sollte', 'debería']):
            patterns['advice'].append(lang)

    return patterns


def classify_mood_guided(entry):
    """
    Classify mood using guided analysis with explicit definitions.

    Definitions:
    - Indicative: Factual statements - real, actually happening/happened
    - 'must' Obligation: Strong necessity - divine commands, laws, moral imperatives
    - 'should' Obligation: Moderate advice - recommendations, suggestions
    - 'should not' Obligation: Negative advice - warnings, discouragements
    - Forbidden Obligation: Strong prohibition - explicit bans, divine prohibitions
    - 'might' Potential: Uncertain possibility - conditional, hypothetical
    - 'may' (permissive): Permission granted - allowing an action
    - Definite Potential: Certain capability - assured future outcome
    - Probable Potential: Likely outcome - probable but not certain
    - Unlikely Potential: Improbable but possible
    """

    text = entry.get('text', '')
    verse_ref = entry.get('verse_ref', '')
    genre = entry.get('genre', '')
    strongs = entry.get('strongs_number', '')
    translations = entry.get('translations', {})

    # Get target word
    bold_match = re.search(r'\*\*([^*]+)\*\*', text)
    target_word = bold_match.group(1).lower() if bold_match else ''

    # Analyze patterns across translations
    patterns = analyze_translations(translations)

    text_lower = text.lower()

    # Analyze English YLT (most literal)
    ylt = translations.get('eng-YLT', '').lower()

    # Rule 1: FORBIDDEN OBLIGATION - Strong prohibitions
    # "shall not", "do not", multiple languages show prohibition
    if len(patterns['prohibition']) >= 3:  # Cross-linguistic agreement
        # Check if it's really a prohibition, not just negation
        if any(p in ylt for p in ['shall not', 'do not', 'shalt not', 'not', 'never']):
            if any(p in text_lower for p in ['not', 'never', 'no']):
                return 'Forbidden Obligation'

    # Rule 2: Conditional contexts → 'might' Potential
    # "if X might happen" - uncertain possibility
    if len(patterns['conditional']) >= 2:
        return "'might' Potential"

    # Rule 3: Permission patterns → 'may' (permissive)
    # "you may do X" - explicitly granted permission
    # Look for "let" in English translations
    if any(p in ylt for p in ['let ', 'may ', 'can ']):
        # Make sure not conditional
        if 'if' not in text_lower and 'if' not in ylt:
            return "'may' (permissive)"

    # Rule 4: 'must' Obligation - Divine commands, laws
    # Strong necessity: "you must do X"
    if len(patterns['command']) >= 3:
        # Check for actual command markers
        if any(p in ylt for p in ['shall', 'must', 'command']):
            # Not prohibition
            if 'not' not in ylt[:100]:  # Check early in sentence
                return "'must' Obligation"

    # Rule 5: 'should' Obligation - Advice, recommendations
    if len(patterns['advice']) >= 2:
        if 'not' in ylt:
            return "'should not' Obligation"
        return "'should' Obligation"

    # Rule 6: Check for strong future certainty → Definite Potential
    if any(p in ylt for p in ['will certainly', 'will surely', 'shall surely']):
        return 'Definite Potential'

    # Rule 7: Probable future → Probable Potential
    if len(patterns['future']) >= 4:  # Strong cross-linguistic future
        if any(p in ylt for p in ['will', 'shall']):
            # Not a command
            if 'shall' in ylt and 'not' not in ylt:
                # Could be obligation
                pass
            else:
                return 'Probable Potential'

    # Default: Indicative (factual statements)
    # Most biblical narrative is factual recounting of events
    return 'Indicative'


def main():
    input_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl'
    output_file = '/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_guided.txt'

    predictions = []

    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            entry = json.loads(line)
            prediction = classify_mood_guided(entry)
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
