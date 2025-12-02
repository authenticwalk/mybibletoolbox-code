#!/usr/bin/env python3
"""Compare TBTA transformation styles between He1 (Ruth/OT) and He2 (Matthew/NT)"""

import csv
import re
from collections import Counter

def analyze_verse(verse_text):
    """Extract style metrics from a verse"""
    metrics = {
        'brackets': verse_text.count('['),
        'parentheses': verse_text.count('('),
        'pronouns': len(re.findall(r'\([A-Za-z\s]+\)', verse_text)),
        'implicit_markers': len(re.findall(r'_implicit', verse_text)),
        'underscore_annotations': len(re.findall(r'_[a-z]+', verse_text)),
        'clauses': verse_text.count('['),  # Brackets mark clause boundaries
        'words': len(verse_text.split()),
        'complexity': verse_text.count('[') + verse_text.count('('),
        'length': len(verse_text)
    }
    return metrics

def load_verses(filepath, limit=None):
    """Load verses from CSV"""
    verses = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break
            verses.append({
                'ref': row['Reference'],
                'text': row['Verse']
            })
    return verses

def aggregate_metrics(verses):
    """Aggregate metrics across multiple verses"""
    all_metrics = [analyze_verse(v['text']) for v in verses]

    # Calculate averages
    totals = Counter()
    for m in all_metrics:
        totals.update(m)

    count = len(all_metrics)
    averages = {k: v/count for k, v in totals.items()}

    return averages, all_metrics

def find_examples(verses, metric_fn, label, n=5):
    """Find example verses that illustrate a specific pattern"""
    scored = [(v, metric_fn(v['text'])) for v in verses]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [(v['ref'], v['text'], score) for v, score in scored[:n]]

# Load data
print("Loading Ruth (He1)...")
ruth_verses = load_verses('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data/Ruth.csv', limit=85)

print("Loading Matthew (He2)...")
matthew_verses = load_verses('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data/Matthew.csv', limit=100)

# Calculate metrics
print("\n" + "="*80)
print("AVERAGE METRICS COMPARISON")
print("="*80)

ruth_avg, ruth_metrics = aggregate_metrics(ruth_verses)
matthew_avg, matthew_metrics = aggregate_metrics(matthew_verses)

print(f"\n{'Metric':<25} {'Ruth (He1)':<15} {'Matthew (He2)':<15} {'Difference':<15}")
print("-"*70)
for metric in ['brackets', 'parentheses', 'pronouns', 'implicit_markers',
               'underscore_annotations', 'clauses', 'words', 'complexity']:
    diff = matthew_avg[metric] - ruth_avg[metric]
    pct = (diff / ruth_avg[metric] * 100) if ruth_avg[metric] > 0 else 0
    print(f"{metric:<25} {ruth_avg[metric]:<15.2f} {matthew_avg[metric]:<15.2f} {diff:+.2f} ({pct:+.1f}%)")

# Find specific examples
print("\n" + "="*80)
print("BRACKET USAGE EXAMPLES (High bracket count = more clause segmentation)")
print("="*80)

print("\nRUTH (He1) - Highest bracket usage:")
for ref, text, score in find_examples(ruth_verses, lambda t: t.count('['), 'brackets', 3):
    print(f"\n{ref} [{score} brackets]")
    print(f"  {text[:150]}...")

print("\nMATTHEW (He2) - Highest bracket usage:")
for ref, text, score in find_examples(matthew_verses, lambda t: t.count('['), 'brackets', 3):
    print(f"\n{ref} [{score} brackets]")
    print(f"  {text[:150]}...")

# Pronoun specificity
print("\n" + "="*80)
print("PRONOUN SPECIFICITY (High count = more explicit pronoun identification)")
print("="*80)

print("\nRUTH (He1) - Highest pronoun specificity:")
for ref, text, score in find_examples(ruth_verses, lambda t: len(re.findall(r'\([A-Za-z\s\']+\)', t)), 'pronouns', 3):
    print(f"\n{ref} [{score} pronoun annotations]")
    print(f"  {text[:150]}...")

print("\nMATTHEW (He2) - Highest pronoun specificity:")
for ref, text, score in find_examples(matthew_verses, lambda t: len(re.findall(r'\([A-Za-z\s\']+\)', t)), 'pronouns', 3):
    print(f"\n{ref} [{score} pronoun annotations]")
    print(f"  {text[:150]}...")

# Underscore annotations
print("\n" + "="*80)
print("UNDERSCORE ANNOTATIONS (implicit/implicit-situational/frameInferable etc.)")
print("="*80)

print("\nRUTH (He1) - Highest underscore annotation usage:")
for ref, text, score in find_examples(ruth_verses, lambda t: len(re.findall(r'_[a-z]+', t)), 'underscores', 3):
    annotations = re.findall(r'_([a-z\-]+)', text)
    print(f"\n{ref} [{score} annotations: {', '.join(set(annotations))}]")
    print(f"  {text[:150]}...")

print("\nMATTHEW (He2) - Highest underscore annotation usage:")
for ref, text, score in find_examples(matthew_verses, lambda t: len(re.findall(r'_[a-z]+', t)), 'underscores', 3):
    annotations = re.findall(r'_([a-z\-]+)', text)
    print(f"\n{ref} [{score} annotations: {', '.join(set(annotations))}]")
    print(f"  {text[:150]}...")

print("\n" + "="*80)
