#!/usr/bin/env python3
"""
Hybrid Hints + LLM Analysis

Process each verse individually with linguistic analysis.
Hints are SUGGESTIONS - override when semantic context demands it.
"""

import json

# Mood labels
MOODS = [
    "Indicative",
    "'must' Obligation",
    "'should' Obligation",
    "'might' Potential",
    "'should not' Obligation",
    "'may' (permissive)",
    "Forbidden Obligation",
    "Definite Potential",
    "Probable Potential",
    "Unlikely Potential"
]

def analyze_verse(verse_data, hint_info):
    """
    Analyze a single verse and make a mood prediction.

    Args:
        verse_data: Dict with verse, text, constituent, part, genre, etc.
        hint_info: Dict with word_prediction and hints

    Returns:
        str: Predicted mood label
    """
    verse_id = verse_data['verse']
    text = verse_data['text']
    constituent = verse_data['constituent']
    part = verse_data['part']
    genre = verse_data['genre']
    path = verse_data.get('path', '')
    strongs = verse_data.get('strongs', '')

    word_pred = hint_info['word_prediction']
    hints = hint_info['hints']

    # Start with hint prediction
    pred = word_pred

    # Key patterns to check
    text_lower = text.lower()
    const_lower = constituent.lower()

    # ===== SEMANTIC ANALYSIS =====

    # 1. COMMANDS & OBLIGATIONS
    # Imperatives, commands, laws
    if any(word in const_lower for word in ['command', 'order', 'decree']):
        return "'must' Obligation"

    # 2. PROHIBITIONS
    # "Do not", "shall not", "must not"
    if any(neg in text_lower for neg in ['do not', 'shall not', 'must not', 'let not']):
        if 'legal_book' in hints:
            return "Forbidden Obligation"
        else:
            return "'should not' Obligation"

    # 3. CONDITIONALS
    # "If X then Y" constructions
    if 'conditional_if_lest' in hints:
        # Conditionals describe potential situations
        if 'legal_book' in hints:
            # Legal conditionals: "if someone does X, then Y shall happen"
            # The protasis (if-clause) describes a potential situation
            return "'might' Potential"
        else:
            return "'might' Potential"

    # 4. MODAL VERBS
    # "might", "may", "could", "would", "should"
    if 'modal_might' in hints:
        return "'might' Potential"

    if 'modal_may' in hints:
        # "may" can be permissive or potential
        # Check context
        if 'legal_book' in hints or any(word in text_lower for word in ['allow', 'permit']):
            return "'may' (permissive)"
        else:
            # In narrative, often indicative
            return "Indicative"

    # 5. NARRATIVE PAST EVENTS
    # Past tense verbs indicating completed actions
    past_markers = ['came', 'went', 'said', 'did', 'was', 'were', 'had', 'made', 'took', 'gave']
    if any(marker in const_lower for marker in past_markers):
        return "Indicative"

    # 6. STATEMENTS OF FACT
    # Declarative statements, descriptions
    if part == 'Verb' and 'negation_detected' not in hints:
        # Simple verbs without negation or modality = indicative
        if not any(hint in hints for hint in ['conditional_if_lest', 'modal_may', 'modal_might']):
            return "Indicative"

    # 7. NEGATED STATEMENTS
    # "X did not happen" is still indicative (negated fact)
    if 'negation_detected' in hints and not 'conditional_if_lest' in hints:
        # Negation without conditional = statement of negative fact
        return "Indicative"

    # Default: trust the hint
    return pred


def main():
    # Load data
    verses = []
    with open('/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl', 'r') as f:
        for line in f:
            verses.append(json.loads(line.strip()))

    hints_data = []
    with open('/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/word_analysis_hints.jsonl', 'r') as f:
        for line in f:
            hints_data.append(json.loads(line.strip()))

    assert len(verses) == len(hints_data) == 100

    # Analyze each verse
    predictions = []
    for verse_data, hint_info in zip(verses, hints_data):
        pred = analyze_verse(verse_data, hint_info)
        predictions.append(pred)

    # Write output
    output_path = '/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/hybrid_hints_llm.txt'
    with open(output_path, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"Wrote {len(predictions)} predictions to {output_path}")

    # Summary
    from collections import Counter
    print("\nPrediction distribution:")
    for mood, count in Counter(predictions).most_common():
        print(f"  {mood}: {count}")

if __name__ == '__main__':
    main()
