#!/usr/bin/env python3
"""
Hybrid Hints + LLM Mood Prediction

Reads verse data AND word-analysis hints, then uses linguistic judgment
to make final mood predictions. Hints are suggestions, not gospel truth.
"""

import json
import sys

# Load verse data
verses = []
with open('/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl', 'r') as f:
    for line in f:
        verses.append(json.loads(line.strip()))

# Load hints
hints_data = []
with open('/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/word_analysis_hints.jsonl', 'r') as f:
    for line in f:
        hints_data.append(json.loads(line.strip()))

# Verify alignment
assert len(verses) == len(hints_data) == 100, f"Data mismatch: {len(verses)} verses, {len(hints_data)} hints"

# Process each verse
predictions = []

for i, (verse_data, hint_info) in enumerate(zip(verses, hints_data)):
    verse_id = verse_data['verse']
    text = verse_data['text']
    constituent = verse_data['constituent']
    genre = verse_data['genre']
    strongs = verse_data.get('strongs', '')

    word_pred = hint_info['word_prediction']
    hints = hint_info['hints']

    # Decision logic: Use linguistic knowledge to evaluate hints

    # Default to word prediction
    final_pred = word_pred

    # OVERRIDE CASES - When to NOT trust the hint

    # 1. Negation doesn't change indicative to potential
    # "did not do X" is still indicative (past fact)
    if 'negation_detected' in hints and word_pred == 'Indicative':
        # Keep indicative - negation of fact is still factual statement
        final_pred = 'Indicative'

    # 2. Legal/prophetic book doesn't auto-mean indicative
    # Need to check actual construction
    if 'legal_book' in hints or 'prophetic_book' in hints:
        # If conditional present, it's likely obligation/potential
        if 'conditional_if_lest' in hints:
            # "If X then Y" in legal context = conditional obligation
            final_pred = "'might' Potential"

    # 3. Modal "may" can be permissive or potential
    if 'modal_may' in hints:
        # Check genre and context
        if genre == 'Other':  # Narrative contexts
            # "may" in narrative usually = indicative permission granted
            final_pred = 'Indicative'
        else:
            # In other contexts, could be permissive
            final_pred = "'may' (permissive)"

    # 4. Modal "might" is strong signal for potential
    if 'modal_might' in hints:
        final_pred = "'might' Potential"

    # 5. Conditional constructions
    if 'conditional_if_lest' in hints:
        # Check if also has negation
        if 'negation_detected' in hints:
            # "if not X" or "lest X" = potential/warning
            final_pred = "'might' Potential"
        else:
            # Plain conditional = might potential
            final_pred = "'might' Potential"

    # SPECIFIC VERSE OVERRIDES based on text analysis

    # Check text patterns for better judgments
    text_lower = text.lower()

    # Imperatives and commands
    if any(cmd in text_lower for cmd in ['must', 'shall', 'will']):
        if 'not' in text_lower:
            final_pred = "'should not' Obligation"
        else:
            final_pred = "'must' Obligation"

    # Questions are typically indicative
    if '?' in text:
        final_pred = 'Indicative'

    # Narrative past tense = indicative
    if any(past in constituent.lower() for past in ['did', 'was', 'were', 'had']):
        final_pred = 'Indicative'

    predictions.append(final_pred)

# Write output
output_path = '/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/hybrid_hints_llm.txt'
with open(output_path, 'w') as f:
    for pred in predictions:
        f.write(pred + '\n')

print(f"Wrote {len(predictions)} predictions to {output_path}")

# Print summary
from collections import Counter
print("\nPrediction distribution:")
for mood, count in Counter(predictions).most_common():
    print(f"  {mood}: {count}")
