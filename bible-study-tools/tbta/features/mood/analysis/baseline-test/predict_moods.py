#!/usr/bin/env python3
"""
Predict mood labels for verses using LLM knowledge plus metadata.
"""

import json
import re

def analyze_context_for_mood(entry):
    """
    Analyze the entry and predict the mood based on:
    - The text context
    - Translations in multiple languages
    - Genre
    - Strong's number if available
    """

    text = entry.get('text', '')
    constituent = entry.get('constituent', '')
    genre = entry.get('genre', '')
    translations = entry.get('translations', {})
    strongs = entry.get('strongs_number', '')
    verse = entry.get('verse', '')

    # Extract the bolded word
    bold_match = re.search(r'\*\*(.*?)\*\*', text)
    bolded_word = bold_match.group(1) if bold_match else constituent

    # Analyze translations to understand the mood better
    # Look for modal verbs and imperative forms

    eng_ylt = translations.get('eng-YLT', '').lower()

    # Pattern matching for different moods

    # FORBIDDEN OBLIGATION - "shall not", "must not", "do not"
    if any(pattern in eng_ylt for pattern in ['shall not', 'must not', 'do not', "don't", 'shalt not']):
        if bolded_word in eng_ylt or constituent.lower() in eng_ylt:
            return "Forbidden Obligation"

    # MUST OBLIGATION - strong commands, "shall", "must"
    if any(pattern in eng_ylt for pattern in ['shall', 'must', 'shalt']):
        # But not "shall not"
        if 'shall not' not in eng_ylt and 'shalt not' not in eng_ylt:
            return "'must' Obligation"

    # SHOULD OBLIGATION - softer commands
    if any(pattern in eng_ylt for pattern in ['should', 'ought']):
        if 'should not' not in eng_ylt:
            return "'should' Obligation"

    # SHOULD NOT OBLIGATION
    if 'should not' in eng_ylt or 'ought not' in eng_ylt:
        return "'should not' Obligation"

    # MAY (PERMISSIVE) - permission granted
    if any(pattern in eng_ylt for pattern in ['may ', 'let ', 'allowed', 'permitted']):
        return "'may' (permissive)"

    # DEFINITE POTENTIAL - "will", "going to"
    if any(pattern in eng_ylt for pattern in ['will ', 'shall ', 'going to']):
        # Check if it's future certainty
        if any(word in eng_ylt for word in ['certainly', 'surely', 'indeed']):
            return "Definite Potential"

    # PROBABLE POTENTIAL - "would", "should" (when expressing likelihood)
    if any(pattern in eng_ylt for pattern in ['would ', 'likely', 'probably']):
        return "Probable Potential"

    # MIGHT POTENTIAL - "might", "could", "possibly"
    if any(pattern in eng_ylt for pattern in ['might ', 'could ', 'possibly', 'perhaps', 'maybe']):
        return "'might' Potential"

    # UNLIKELY POTENTIAL
    if any(pattern in eng_ylt for pattern in ['unlikely', 'hardly', 'scarcely']):
        return "Unlikely Potential"

    # Check if it's an imperative command (common in law/instruction genres)
    # Imperatives often appear as bare verbs at start of commands
    if genre in ['Law', 'Instruction', 'Command']:
        # Check for imperative markers in translations
        if bolded_word.lower() in ['go', 'come', 'do', 'take', 'bring', 'say', 'tell', 'give']:
            # Could be imperative = obligation
            return "'must' Obligation"

    # Default to Indicative for statements of fact
    return "Indicative"


def main():
    input_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl"
    output_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_zero_shot_sonnet.txt"

    predictions = []

    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            entry = json.loads(line.strip())

            # Make prediction
            mood = analyze_context_for_mood(entry)
            predictions.append(mood)

            # Debug output for first few
            if line_num <= 5:
                text = entry.get('text', '')
                verse = entry.get('verse', '')
                eng_ylt = entry.get('translations', {}).get('eng-YLT', '')
                print(f"\nEntry {line_num}: {verse}")
                print(f"Text: {text[:80]}...")
                print(f"YLT: {eng_ylt[:80]}...")
                print(f"Prediction: {mood}")

    # Write predictions to output file
    with open(output_file, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"\n\nProcessed {len(predictions)} entries")
    print(f"Output written to: {output_file}")

    # Show distribution
    from collections import Counter
    dist = Counter(predictions)
    print("\nPrediction distribution:")
    for mood, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mood}: {count}")


if __name__ == '__main__':
    main()
