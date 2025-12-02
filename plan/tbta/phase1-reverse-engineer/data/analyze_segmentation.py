#!/usr/bin/env python3
"""
Analyze TBTA Verse column for clause segmentation patterns.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

def extract_sentences(verse_text):
    """Extract individual sentences from verse text."""
    # Remove embedded markup like (title), (paragraph), _implicit, etc.
    # But preserve the core sentence structure

    # Split by period followed by space or end of string
    sentences = re.split(r'\.\s+|\.$', verse_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def count_verbs(sentence):
    """Count verbs in a sentence (simple heuristic)."""
    # Look for common verb patterns
    verbs = re.findall(r'\b(?:is|are|was|were|be|been|being|have|has|had|do|does|did|will|would|can|could|shall|should|may|might|must|move|live|go|come|see|know|born|rule|call|study|follow|teach|sit)\b', sentence.lower())
    return len(verbs)

def has_conjunction_start(sentence):
    """Check if sentence starts with a conjunction."""
    sentence = sentence.strip()
    # Remove markup at start
    sentence = re.sub(r'^\([^)]+\)\s*', '', sentence)
    sentence = re.sub(r'^\[[^\]]+\]\s*', '', sentence)

    return bool(re.match(r'^(And|But|Or|So|Then|For|Yet|Because|Since|While|When|After|Before)\b', sentence, re.IGNORECASE))

def analyze_csv(filepath):
    """Analyze a single CSV file for segmentation patterns."""
    examples = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            reference = row.get('Reference', '')
            verse = row.get('Verse', '')

            if not verse:
                continue

            sentences = extract_sentences(verse)

            # Analyze this verse
            analysis = {
                'reference': reference,
                'verse': verse,
                'sentence_count': len(sentences),
                'sentences': sentences,
                'conjunction_starts': sum(1 for s in sentences if has_conjunction_start(s)),
                'avg_verbs_per_sentence': sum(count_verbs(s) for s in sentences) / len(sentences) if sentences else 0
            }

            examples.append(analysis)

    return examples

def main():
    data_dir = Path('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data')

    # Analyze Ruth and Matthew
    print("=" * 80)
    print("ANALYZING RUTH (He1 - Natural Style)")
    print("=" * 80)
    ruth_examples = analyze_csv(data_dir / 'Ruth.csv')

    # Show examples with high sentence segmentation
    print("\n### High Segmentation Examples (5+ sentences):")
    for ex in ruth_examples[:50]:  # First 50 verses
        if ex['sentence_count'] >= 5:
            print(f"\n{ex['reference']} ({ex['sentence_count']} sentences):")
            for i, sent in enumerate(ex['sentences'], 1):
                conj_marker = " [CONJ]" if has_conjunction_start(sent) else ""
                print(f"  {i}. {sent[:100]}...{conj_marker}" if len(sent) > 100 else f"  {i}. {sent}{conj_marker}")

    # Show examples with conjunction starts
    print("\n### Examples with Conjunction-Started Sentences:")
    for ex in ruth_examples[:50]:
        if ex['conjunction_starts'] >= 2:
            print(f"\n{ex['reference']} ({ex['conjunction_starts']} conjunction starts):")
            for i, sent in enumerate(ex['sentences'], 1):
                if has_conjunction_start(sent):
                    print(f"  {i}. {sent[:100]}..." if len(sent) > 100 else f"  {i}. {sent}")

    print("\n" + "=" * 80)
    print("ANALYZING MATTHEW (He2 - Strict Style)")
    print("=" * 80)
    matthew_examples = analyze_csv(data_dir / 'Matthew.csv')

    # Show examples with high sentence segmentation
    print("\n### High Segmentation Examples (5+ sentences):")
    for ex in matthew_examples[:50]:  # First 50 verses
        if ex['sentence_count'] >= 5:
            print(f"\n{ex['reference']} ({ex['sentence_count']} sentences):")
            for i, sent in enumerate(ex['sentences'], 1):
                conj_marker = " [CONJ]" if has_conjunction_start(sent) else ""
                print(f"  {i}. {sent[:100]}...{conj_marker}" if len(sent) > 100 else f"  {i}. {sent}{conj_marker}")

    # Show examples with conjunction starts
    print("\n### Examples with Conjunction-Started Sentences:")
    for ex in matthew_examples[:50]:
        if ex['conjunction_starts'] >= 2:
            print(f"\n{ex['reference']} ({ex['conjunction_starts']} conjunction starts):")
            for i, sent in enumerate(ex['sentences'], 1):
                if has_conjunction_start(sent):
                    print(f"  {i}. {sent[:100]}..." if len(sent) > 100 else f"  {i}. {sent}")

    # Statistics
    print("\n" + "=" * 80)
    print("STATISTICS")
    print("=" * 80)

    ruth_stats = {
        'total_verses': len(ruth_examples),
        'avg_sentences_per_verse': sum(ex['sentence_count'] for ex in ruth_examples) / len(ruth_examples),
        'verses_with_conjunction_starts': sum(1 for ex in ruth_examples if ex['conjunction_starts'] > 0),
        'avg_verbs_per_sentence': sum(ex['avg_verbs_per_sentence'] for ex in ruth_examples) / len(ruth_examples)
    }

    matthew_stats = {
        'total_verses': len(matthew_examples),
        'avg_sentences_per_verse': sum(ex['sentence_count'] for ex in matthew_examples) / len(matthew_examples),
        'verses_with_conjunction_starts': sum(1 for ex in matthew_examples if ex['conjunction_starts'] > 0),
        'avg_verbs_per_sentence': sum(ex['avg_verbs_per_sentence'] for ex in matthew_examples) / len(matthew_examples)
    }

    print(f"\nRuth (He1):")
    for key, value in ruth_stats.items():
        print(f"  {key}: {value:.2f}")

    print(f"\nMatthew (He2):")
    for key, value in matthew_stats.items():
        print(f"  {key}: {value:.2f}")

if __name__ == '__main__':
    main()
