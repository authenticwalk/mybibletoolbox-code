#!/usr/bin/env python3
"""
TBTA Integration Test - Comprehensive Feature Analysis
Applies all 6 feature methodologies to 5 new Genesis verses
"""

import json
from collections import defaultdict, Counter

VERSES = {
    '004': 'Genesis 1:4',
    '005': 'Genesis 1:5',
    '006': 'Genesis 1:6',
    '009': 'Genesis 1:9',
    '011': 'Genesis 1:11'
}

def extract_features(element, features=None, clause_idx=0):
    """Recursively extract all grammatical features from TBTA structure"""
    if features is None:
        features = []

    if element.get('Part') in ['Noun', 'Verb', 'Adjective', 'Adverb']:
        feature = {
            'word': element.get('Constituent', ''),
            'part': element.get('Part', ''),
            'clause': clause_idx,

            # All parts of speech
            'number': element.get('Number', 'N/A'),
            'polarity': element.get('Polarity', 'N/A'),

            # Nouns
            'participant_tracking': element.get('Participant Tracking', 'N/A') if element.get('Part') == 'Noun' else 'N/A',
            'participant_status': element.get('Participant Status', 'N/A') if element.get('Part') == 'Noun' else 'N/A',
            'proximity': element.get('Proximity', 'N/A') if element.get('Part') == 'Noun' else 'N/A',

            # Verbs
            'time': element.get('Time', 'N/A') if element.get('Part') == 'Verb' else 'N/A',
            'aspect': element.get('Aspect', 'N/A') if element.get('Part') == 'Verb' else 'N/A',
            'mood': element.get('Mood', 'N/A') if element.get('Part') == 'Verb' else 'N/A',

            # Adjectives/Adverbs
            'degree': element.get('Degree', 'N/A') if element.get('Part') in ['Adjective', 'Adverb'] else 'N/A',
        }
        features.append(feature)

    if 'Children' in element:
        for child in element['Children']:
            extract_features(child, features, clause_idx)

    return features


def analyze_verse(v_code, v_name):
    """Analyze a single verse and extract all features"""
    filename = f'plan/tbta-project/tbta-data/samples/genesis_001_{v_code}.json'
    with open(filename, 'r') as f:
        data = json.load(f)

    all_features = []
    for clause_idx, clause in enumerate(data, 1):
        features = extract_features(clause, clause_idx=clause_idx)
        all_features.extend(features)

    return all_features, len(data)


def print_verse_analysis(v_code, v_name, features, num_clauses):
    """Print comprehensive analysis of a verse"""
    print(f"\n{'='*80}")
    print(f"{v_name.upper()} - {num_clauses} clauses")
    print(f"{'='*80}")

    # Nouns
    nouns = [f for f in features if f['part'] == 'Noun']
    if nouns:
        print(f"\nNOUNS ({len(nouns)}):")
        print("-" * 80)
        print(f"{'Word':<15} {'Tracking':<18} {'Status':<18} {'Num':<8} {'Pol':<12} {'Prox':<20}")
        print("-" * 80)
        for n in nouns:
            print(f"{n['word']:<15} {n['participant_tracking']:<18} {n['participant_status']:<18} "
                  f"{n['number']:<8} {n['polarity']:<12} {n['proximity']:<20}")

    # Verbs
    verbs = [f for f in features if f['part'] == 'Verb']
    if verbs:
        print(f"\nVERBS ({len(verbs)}):")
        print("-" * 80)
        print(f"{'Word':<15} {'Time':<20} {'Aspect':<15} {'Mood':<12} {'Pol':<12} {'Num':<8}")
        print("-" * 80)
        for v in verbs:
            print(f"{v['word']:<15} {v['time']:<20} {v['aspect']:<15} {v['mood']:<12} "
                  f"{v['polarity']:<12} {v['number']:<8}")

    # Adjectives
    adjs = [f for f in features if f['part'] == 'Adjective']
    if adjs:
        print(f"\nADJECTIVES ({len(adjs)}):")
        print("-" * 80)
        print(f"{'Word':<15} {'Degree':<12} {'Num':<8} {'Pol':<12}")
        print("-" * 80)
        for a in adjs:
            print(f"{a['word']:<15} {a['degree']:<12} {a['number']:<8} {a['polarity']:<12}")


def calculate_statistics(all_verse_features):
    """Calculate statistics across all verses"""
    stats = {
        'participant_tracking': Counter(),
        'participant_status': Counter(),
        'number': Counter(),
        'polarity': Counter(),
        'proximity': Counter(),
        'time': Counter(),
        'aspect': Counter(),
        'mood': Counter(),
        'degree': Counter()
    }

    for features in all_verse_features.values():
        for f in features:
            if f['part'] == 'Noun':
                stats['participant_tracking'][f['participant_tracking']] += 1
                stats['participant_status'][f['participant_status']] += 1
                stats['proximity'][f['proximity']] += 1
            if f['part'] == 'Verb':
                stats['time'][f['time']] += 1
                stats['aspect'][f['aspect']] += 1
                stats['mood'][f['mood']] += 1

            stats['number'][f['number']] += 1
            stats['polarity'][f['polarity']] += 1

            if f['part'] in ['Adjective', 'Adverb']:
                stats['degree'][f['degree']] += 1

    return stats


def print_statistics(stats, total_features):
    """Print summary statistics"""
    print(f"\n{'='*80}")
    print("SUMMARY STATISTICS ACROSS ALL 5 VERSES")
    print(f"{'='*80}")

    print(f"\nTotal features analyzed: {total_features}")

    for feature_name, counter in stats.items():
        if counter and feature_name != 'degree':  # Skip degree if no adj/adv
            print(f"\n{feature_name.upper().replace('_', ' ')}:")
            for value, count in counter.most_common():
                if value != 'N/A':
                    pct = (count / sum(counter.values())) * 100
                    print(f"  {value:<30} {count:>4} ({pct:>5.1f}%)")


def main():
    """Main analysis function"""
    print("TBTA INTEGRATION TEST")
    print("Analyzing 5 New Genesis Verses with All 6 Features")
    print("=" * 80)

    all_verse_features = {}
    total_clauses = 0
    total_features = 0

    for v_code, v_name in VERSES.items():
        features, num_clauses = analyze_verse(v_code, v_name)
        all_verse_features[v_name] = features
        total_clauses += num_clauses
        total_features += len(features)
        print_verse_analysis(v_code, v_name, features, num_clauses)

    # Calculate and print statistics
    stats = calculate_statistics(all_verse_features)
    print_statistics(stats, total_features)

    print(f"\n{'='*80}")
    print(f"Total: {len(VERSES)} verses, {total_clauses} clauses, {total_features} annotated features")
    print(f"{'='*80}")


if __name__ == '__main__':
    main()
