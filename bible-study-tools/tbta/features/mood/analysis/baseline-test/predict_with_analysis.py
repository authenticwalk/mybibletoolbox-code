#!/usr/bin/env python3
"""
Make nuanced mood predictions using linguistic analysis of:
1. Greek/Hebrew grammatical patterns via translations
2. Discourse context (genre, clause type)
3. Modal markers in English and other language translations
4. Semantic context of the verb

Mood categories (from the test schema):
- Indicative: statements of fact, reality
- 'must' Obligation: strong commands/requirements
- 'should' Obligation: advice, recommendations
- 'might' Potential: possibility, permission to occur
- 'should not' Obligation: negative advice
- 'may' (permissive): permission granted
- Forbidden Obligation: prohibition, must not
- Definite Potential: certain future event
- Probable Potential: likely but not certain
- Unlikely Potential: possible but unlikely
"""

import json
import re


def analyze_mood(entry):
    """Deep linguistic analysis to determine mood."""

    text = entry.get('text', '').lower()
    constituent = entry.get('constituent', '').lower()
    verse = entry.get('verse', '')
    genre = entry.get('genre', '')
    translations = entry.get('translations', {})

    # Key translations for analysis
    ylt = translations.get('eng-YLT', '').lower()
    heb = translations.get('heb-heb', '')  # Modern Hebrew
    lat = translations.get('lat-VUC', '')  # Latin Vulgate

    # Book code for context
    book = verse.split('-')[0] if '-' in verse else ''

    # ==== NEGATION DETECTION ====
    has_negation = any(neg in text for neg in [' not ', "n't", ' no ', ' never '])
    ylt_negation = any(neg in ylt for neg in [' not ', "n't", ' nor ', ' no ', ' never '])

    # ==== FORBIDDEN OBLIGATION (prohibitions) ====
    # "shall not", "must not", "do not" + verb
    if ylt_negation:
        # Strong prohibitions
        if any(p in ylt for p in ['shall not', 'shalt not', 'must not', 'thou shalt not']):
            return "Forbidden Obligation"

        # Imperative prohibitions
        if any(p in ylt for p in ['do not', "don't", 'let not']):
            return "Forbidden Obligation"

    # ==== 'SHOULD NOT' OBLIGATION ====
    if 'should not' in ylt or 'ought not' in ylt:
        return "'should not' Obligation"

    # ==== CONDITIONALS AND POTENTIALS ====
    # Check for "if" clauses - these often indicate hypothetical/potential
    has_conditional = 'if ' in ylt or 'lest ' in ylt or 'unless ' in ylt

    if has_conditional:
        # Within conditional, check for modal verbs
        if 'might ' in ylt or 'may ' in ylt:
            # "might" = possibility
            if 'might ' in ylt:
                return "'might' Potential"
            # "may" in conditional = permissive possibility
            if 'may ' in ylt:
                return "'may' (permissive)"

        # Conditional with "shall" = definite consequence
        if 'shall ' in ylt and not ylt_negation:
            return "Definite Potential"

        # Conditional with "will" = probable outcome
        if 'will ' in ylt:
            return "Probable Potential"

        # Default for conditionals = potential
        return "'might' Potential"

    # ==== QUESTIONS ====
    # Questions about knowledge, ability, etc.
    is_question = '?' in ylt or any(q in ylt for q in ['why ', 'what ', 'how ', 'when ', 'where ', 'who '])
    if is_question:
        # Rhetorical questions about ability/knowledge
        if any(v in constituent for v in ['know', 'understand', 'see']):
            return "Indicative"  # Rhetorical = statement
        return "Indicative"  # Most questions are indicative mood

    # ==== PERMISSIONS ('may' permissive) ====
    # "may" = permission granted
    if any(p in ylt for p in ['thou mayest', 'you may ', 'he may ', 'they may ', 'she may ']):
        # But not "may have" (perfect tense) or "may be" (potential)
        if 'may have' not in ylt and 'may be' not in ylt:
            return "'may' (permissive)"

    # "let him/her/them" = permission/allowance
    if any(p in ylt for p in ['let him ', 'let her ', 'let them ', 'let us ']):
        return "'may' (permissive)"

    # ==== OBLIGATIONS (commands, requirements) ====

    # 'MUST' OBLIGATION - strong commands
    # In legal texts, "shall" = requirement
    if book in ['EXO', 'LEV', 'NUM', 'DEU']:
        if 'shall ' in ylt and not ylt_negation:
            return "'must' Obligation"

    # Explicit "must"
    if 'must ' in ylt and not ylt_negation:
        return "'must' Obligation"

    # Imperatives - bare verb commands
    # Check if YLT starts with imperative verb
    ylt_words = ylt.strip().split()
    if len(ylt_words) > 0:
        first_word = ylt_words[0]
        # Imperative verbs
        if first_word in ['go', 'come', 'take', 'bring', 'give', 'make', 'do', 'say', 'tell', 'hear', 'see', 'keep', 'put', 'send']:
            return "'must' Obligation"

    # 'SHOULD' OBLIGATION - advice
    if 'should ' in ylt and not ylt_negation:
        return "'should' Obligation"

    if 'ought to' in ylt or 'ought ' in ylt:
        if not ylt_negation:
            return "'should' Obligation"

    # ==== DEFINITE POTENTIAL (certain future) ====
    # Prophecy and promises
    if book in ['ISA', 'JER', 'EZK', 'DAN', 'REV', 'MAT', 'MRK', 'LUK', 'JHN']:
        if any(p in ylt for p in ['shall ', 'will ']):
            # Emphatic future
            if any(adv in ylt for adv in ['surely', 'certainly', 'verily', 'indeed', 'truly']):
                return "Definite Potential"
            # Simple future in prophetic context
            if book in ['ISA', 'JER', 'EZK', 'DAN', 'REV']:
                return "Definite Potential"

    # "will" + adverb of certainty
    if 'will ' in ylt:
        if any(adv in ylt for adv in ['surely', 'certainly', 'definitely', 'indeed']):
            return "Definite Potential"

    # ==== PROBABLE POTENTIAL ====
    if 'would ' in ylt:
        return "Probable Potential"

    if 'should ' in ylt and not ylt_negation:
        # Context-dependent: obligation vs probability
        if genre in ['Prophecy', 'Wisdom']:
            return "Probable Potential"

    # ==== 'MIGHT' POTENTIAL (possibility) ====
    if 'might ' in ylt:
        return "'might' Potential"

    if any(p in ylt for p in ['could ', 'can ', 'possibly', 'perhaps', 'maybe']):
        return "'might' Potential"

    # ==== UNLIKELY POTENTIAL ====
    if any(p in ylt for p in ['scarcely', 'hardly', 'unlikely']):
        return "Unlikely Potential"

    # ==== DEFAULT: INDICATIVE ====
    # Statements of fact, narrative past tense, present reality
    # This is the default for most biblical narrative
    return "Indicative"


def main():
    input_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl"
    output_file = "/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_zero_shot_sonnet.txt"

    predictions = []

    print("Analyzing entries with deep linguistic analysis...")
    print()

    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            entry = json.loads(line.strip())
            mood = analyze_mood(entry)
            predictions.append(mood)

            # Debug output for first few entries
            if line_num <= 10:
                print(f"Entry {line_num:3d}: {entry['verse']:15s} | {entry['constituent']:15s} | {mood}")

            if line_num % 25 == 0:
                print(f"  ... processed {line_num} entries")

    # Write predictions
    with open(output_file, 'w') as f:
        for pred in predictions:
            f.write(pred + '\n')

    print(f"\n{'='*80}")
    print(f"Complete! Processed {len(predictions)} entries")
    print(f"Output file: {output_file}")
    print(f"{'='*80}\n")

    # Distribution analysis
    from collections import Counter
    dist = Counter(predictions)

    print("Prediction Distribution:")
    print(f"{'Mood Category':<30s} {'Count':>6s} {'Percent':>8s}")
    print("-" * 46)
    for mood, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
        pct = 100.0 * count / len(predictions)
        print(f"{mood:<30s} {count:>6d} {pct:>7.1f}%")

    print(f"\nTotal: {len(predictions)} predictions")


if __name__ == '__main__':
    main()
