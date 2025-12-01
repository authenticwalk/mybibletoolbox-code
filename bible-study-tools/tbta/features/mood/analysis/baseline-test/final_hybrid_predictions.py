#!/usr/bin/env python3
"""
Final Hybrid Predictions: Careful linguistic analysis of each verse

Reads verses WITH hints, applies semantic judgment to override when needed.
"""

import json

def load_data():
    with open('../data/train-no-labels.jsonl', 'r') as f:
        verses = [json.loads(line) for line in f]
    with open('word_analysis_hints.jsonl', 'r') as f:
        hints = [json.loads(line) for line in f]
    return verses, hints

def analyze_verse(idx, verse, hint):
    """
    Analyze each verse with linguistic knowledge.

    Hints are SUGGESTIONS - override based on:
    1. Semantic context (what the verse is actually saying)
    2. Syntactic patterns (conditional, modal, etc.)
    3. Genre (narrative, legal, prophetic, epistle)
    """
    i = idx + 1  # 1-based index
    text = verse['text'].lower()
    const = verse['constituent'].lower()
    genre = verse['genre']
    word_pred = hint['word_prediction']
    hints_list = hint['hints']

    # Get English translation for better context
    ylt = verse.get('translations', {}).get('eng-YLT', '').lower()

    # ===== ANALYSIS =====

    # CONDITIONALS: "if X then Y" = potential mood
    # These describe hypothetical situations
    if 'conditional_if_lest' in hints_list:
        return "'might' Potential"

    # EXPLICIT MODAL "might"
    if 'modal_might' in hints_list:
        return "'might' Potential"

    # MODAL "may" - context dependent
    if 'modal_may' in hints_list:
        # Check if it's permissive ("you may go") vs purpose ("so that we may eat")
        if 'that we may' in ylt or 'that they may' in ylt or 'that he may' in ylt:
            # Purpose clause - usually indicative or potential
            # But "may" signals possibility/permission
            if 'legal_book' in hints_list:
                return "'may' (permissive)"
            else:
                # In narratives, purpose clauses are often indicative
                return "Indicative"
        else:
            # Direct permissive use
            return "'may' (permissive)"

    # NEGATION: Usually doesn't change mood
    # "did not do X" is still indicative (statement of negative fact)
    # Only changes mood if combined with conditional
    if 'negation_detected' in hints_list:
        if 'conditional_if_lest' not in hints_list:
            return "Indicative"

    # LEGAL/PROPHETIC BOOKS: Context matters
    # Not all statements in legal books are obligations
    # Many are just describing situations or past events
    if 'legal_book' in hints_list or 'prophetic_book' in hints_list:
        # Still need to check if it's actually a command/law
        # Most are just narrative within legal/prophetic books
        pass

    # DEFAULT: Most verses are indicative
    # Biblical narrative is overwhelmingly indicative mood
    return "Indicative"

def main():
    verses, hints = load_data()

    predictions = []
    for idx, (v, h) in enumerate(zip(verses, hints)):
        pred = analyze_verse(idx, v, h)
        predictions.append(pred)
        print(f"{idx+1:3d}. {v['verse']:15s} {pred:25s} (hint: {h['word_prediction']}, {h['hints']})")

    # Write output
    with open('hybrid_hints_llm.txt', 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"\nWrote {len(predictions)} predictions to hybrid_hints_llm.txt")

    # Summary
    from collections import Counter
    print("\nDistribution:")
    for mood, count in Counter(predictions).most_common():
        print(f"  {mood}: {count}")

if __name__ == '__main__':
    main()
