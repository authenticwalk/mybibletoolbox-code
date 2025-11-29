#!/usr/bin/env python3
"""
Score predictions against TBTA answer sheet.

This script compares train_predictions_v1.yaml against train.yaml
to calculate accuracy and identify errors for 6-step analysis.
"""

import yaml
from collections import defaultdict

def load_answers(answer_file):
    """Load TBTA answer sheet and build reference -> value mapping."""
    with open(answer_file) as f:
        data = yaml.safe_load(f)

    answers = {}
    for value_group in data['values']:
        tbta_value = value_group['name']
        for verse in value_group['verses']:
            ref = verse['reference']
            answers[ref] = {
                'tbta_value': tbta_value,
                'testament': verse['testament'],
                'genre': verse['genre'],
                'book': verse['book'],
                'difficulty': verse.get('difficulty', 'typical'),
                'arbitrarity': verse.get('arbitrarity', 'arbitrary')
            }

    return answers

def score_predictions(predictions_file, answers):
    """Score predictions and identify errors."""

    with open(predictions_file) as f:
        predictions = yaml.safe_load(f)

    total = len(predictions['predictions'])
    correct = 0
    errors = []

    # Statistics by category
    by_value = defaultdict(lambda: {'correct': 0, 'total': 0})
    by_confidence = defaultdict(lambda: {'correct': 0, 'total': 0})
    by_genre = defaultdict(lambda: {'correct': 0, 'total': 0})
    by_arbitrarity = defaultdict(lambda: {'correct': 0, 'total': 0})

    for pred in predictions['predictions']:
        ref = pred['reference']
        pred_value = pred['predicted_value']
        confidence = pred['confidence']

        # Get actual answer
        answer = answers[ref]
        actual_value = answer['tbta_value']
        genre = answer['genre']
        arbitrarity = answer['arbitrarity']

        # Check if correct
        is_correct = (pred_value == actual_value)

        if is_correct:
            correct += 1
        else:
            # Record error for analysis
            errors.append({
                'reference': ref,
                'predicted': pred_value,
                'actual': actual_value,
                'confidence': confidence,
                'rule_applied': pred['rule_applied'],
                'rationale': pred['rationale'],
                'genre': genre,
                'testament': answer['testament'],
                'book': answer['book'],
                'difficulty': answer['difficulty'],
                'arbitrarity': arbitrarity
            })

        # Update statistics
        by_value[actual_value]['total'] += 1
        if is_correct:
            by_value[actual_value]['correct'] += 1

        by_confidence[confidence]['total'] += 1
        if is_correct:
            by_confidence[confidence]['correct'] += 1

        by_genre[genre]['total'] += 1
        if is_correct:
            by_genre[genre]['correct'] += 1

        by_arbitrarity[arbitrarity]['total'] += 1
        if is_correct:
            by_arbitrarity[arbitrarity]['correct'] += 1

    accuracy = (correct / total) * 100

    return {
        'total': total,
        'correct': correct,
        'incorrect': total - correct,
        'accuracy': accuracy,
        'errors': errors,
        'by_value': dict(by_value),
        'by_confidence': dict(by_confidence),
        'by_genre': dict(by_genre),
        'by_arbitrarity': dict(by_arbitrarity)
    }

def print_results(results):
    """Print scoring results."""

    print("=" * 70)
    print("PROMPT1 SCORING RESULTS")
    print("=" * 70)
    print()
    print(f"Total Verses:    {results['total']}")
    print(f"Correct:         {results['correct']}")
    print(f"Incorrect:       {results['incorrect']}")
    print(f"ACCURACY:        {results['accuracy']:.1f}%")
    print()

    # Accuracy by number value
    print("ACCURACY BY NUMBER VALUE:")
    print("-" * 70)
    for value in sorted(results['by_value'].keys()):
        stats = results['by_value'][value]
        acc = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"  {value:15s}: {stats['correct']:3d}/{stats['total']:3d} ({acc:5.1f}%)")
    print()

    # Accuracy by confidence level
    print("ACCURACY BY CONFIDENCE LEVEL:")
    print("-" * 70)
    for conf in ['Very Low', 'Low', 'Medium', 'Medium-High', 'High', 'Very High']:
        if conf in results['by_confidence']:
            stats = results['by_confidence'][conf]
            acc = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"  {conf:15s}: {stats['correct']:3d}/{stats['total']:3d} ({acc:5.1f}%)")
    print()

    # Accuracy by genre
    print("ACCURACY BY GENRE:")
    print("-" * 70)
    for genre in sorted(results['by_genre'].keys()):
        stats = results['by_genre'][genre]
        acc = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"  {genre:15s}: {stats['correct']:3d}/{stats['total']:3d} ({acc:5.1f}%)")
    print()

    # Accuracy by arbitrarity
    print("ACCURACY BY ARBITRARITY:")
    print("-" * 70)
    for arb in sorted(results['by_arbitrarity'].keys()):
        stats = results['by_arbitrarity'][arb]
        acc = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"  {arb:20s}: {stats['correct']:3d}/{stats['total']:3d} ({acc:5.1f}%)")
    print()

    # Error summary
    print("ERROR SUMMARY:")
    print("-" * 70)
    print(f"Total Errors: {len(results['errors'])}")
    print()

    if len(results['errors']) > 0:
        # Errors by predicted → actual pattern
        error_patterns = defaultdict(int)
        for err in results['errors']:
            pattern = f"{err['predicted']} → {err['actual']}"
            error_patterns[pattern] += 1

        print("Most Common Error Patterns:")
        for pattern, count in sorted(error_patterns.items(), key=lambda x: x[1], reverse=True)[:10]:
            pct = (count / len(results['errors'])) * 100
            print(f"  {pattern:30s}: {count:3d} errors ({pct:5.1f}% of errors)")
        print()

    print("=" * 70)
    print(f"RESULT: {'✅ TARGET MET' if results['accuracy'] >= 95 else '⚠️ REFINEMENT NEEDED'}")
    if results['accuracy'] < 95:
        print(f"Target: 95%, Actual: {results['accuracy']:.1f}%, Gap: {95 - results['accuracy']:.1f}%")
    print("=" * 70)

def save_errors_for_analysis(errors, output_file):
    """Save errors in format ready for 6-step analysis."""

    error_data = {
        'feature': 'number-systems',
        'prompt_version': 'PROMPT1.md v1.0',
        'total_errors': len(errors),
        'note': 'Errors requiring 6-step analysis (STAGES.md §5)',
        'errors': errors
    }

    with open(output_file, 'w') as f:
        yaml.dump(error_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\n✅ Errors saved to {output_file} for 6-step analysis")

def main():
    """Score predictions and generate error analysis files."""

    print("Loading answer sheet (train.yaml)...")
    answers = load_answers('train.yaml')

    print(f"Loaded {len(answers)} answers")
    print()

    print("Scoring predictions (train_predictions_v1.yaml)...")
    results = score_predictions('train_predictions_v1.yaml', answers)
    print()

    print_results(results)
    print()

    # Save errors for analysis
    if results['errors']:
        save_errors_for_analysis(results['errors'], 'train_errors_v1.yaml')
    else:
        print("\n✅ NO ERRORS - Perfect accuracy!")

    print()
    print("NEXT STEPS:")
    print("1. Review errors in train_errors_v1.yaml")
    print("2. Apply 6-step error analysis to each failure")
    print("3. Create PROMPT1-RESULTS.md with findings")
    if results['accuracy'] < 95:
        print("4. Develop PROMPT2.md with refined approach")
        print("5. Iterate until ≥95% accuracy achieved")
    else:
        print("4. Create LEARNINGS.md and proceed to test set")

if __name__ == '__main__':
    main()
