#!/usr/bin/env python3
"""
Refined Hybrid Analysis

Better understanding of mood categories:
- Indicative: Statements of fact, past events, declarations
- 'might' Potential: Hypothetical situations, conditionals, possibilities
- 'may' (permissive): Permission granted, allowance
- Obligations: Must, should, forbidden, etc.
"""

import json

def analyze_mood(idx, verse, hint):
    """
    Careful semantic analysis of each verse.
    """
    i = idx + 1
    text = verse['text'].lower()
    const = verse['constituent'].lower()
    word_pred = hint['word_prediction']
    hints_list = hint['hints']
    ylt = verse.get('translations', {}).get('eng-YLT', '').lower()

    # PRIORITY 1: Conditionals = Potential
    # "If X happens, then Y" describes hypothetical scenarios
    if 'conditional_if_lest' in hints_list:
        return "'might' Potential"

    # PRIORITY 2: Explicit "might" modal
    if 'modal_might' in hints_list:
        return "'might' Potential"

    # PRIORITY 3: Modal "may" - need to distinguish usage
    if 'modal_may' in hints_list:
        # Check if it's a conditional ("if brother may die")
        if 'conditional_if_lest' in hints_list:
            return "'might' Potential"  # Already handled above, but double-check

        # Check if it's a purpose clause ("that we may X")
        if 'that' in ylt and 'may' in ylt:
            # Purpose clauses like "that we may eat" are typically indicative
            # They express the purpose/goal, not permission or hypothesis
            return "Indicative"

        # Check if it's a permission statement
        # "You may go" or "he may enter"
        if any(perm in ylt for perm in ['you may', 'he may', 'they may', 'she may']):
            # Could be permissive, but need context
            # In narrative, often just indicative with possibility
            # In legal/command context, permissive
            if 'legal_book' in hints_list:
                return "'may' (permissive)"
            else:
                # In narrative, "may" often indicates possibility/future
                return "Indicative"

        # Default for modal_may: indicative
        return "Indicative"

    # PRIORITY 4: Negation (without conditional)
    # "did not do X" is indicative (statement of negative fact)
    if 'negation_detected' in hints_list:
        if 'conditional_if_lest' not in hints_list:
            return "Indicative"

    # PRIORITY 5: Default to indicative
    # Biblical narrative is overwhelmingly indicative mood
    return "Indicative"

def main():
    with open('../data/train-no-labels.jsonl', 'r') as f:
        verses = [json.loads(line) for line in f]
    with open('word_analysis_hints.jsonl', 'r') as f:
        hints = [json.loads(line) for line in f]

    predictions = []
    for idx, (v, h) in enumerate(zip(verses, hints)):
        pred = analyze_mood(idx, v, h)
        predictions.append(pred)

        # Show interesting cases
        if h['word_prediction'] != pred or h['hints']:
            print(f"{idx+1:3d}. {v['verse']:15s} {pred:25s} (hint: {h['word_prediction']}, {h['hints']})")

    # Write output
    with open('hybrid_hints_llm.txt', 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"\nWrote {len(predictions)} predictions")

    # Summary
    from collections import Counter
    print("\nDistribution:")
    for mood, count in Counter(predictions).most_common():
        print(f"  {mood}: {count}")

if __name__ == '__main__':
    main()
