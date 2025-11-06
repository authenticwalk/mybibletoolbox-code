#!/usr/bin/env python3
"""
Test TBTA Mood Predictions

Tests mood identification from TBTA YAML data:
- Commands (imperatives)
- Conditionals (subjunctive)
- Statements (indicative)
- Obligations and permissions

Usage:
    python test_mood_predictions.py
"""

import yaml
import json
from pathlib import Path
from collections import defaultdict, Counter
from typing import List, Dict, Any, Tuple, Optional


class MoodAnalyzer:
    """Analyze TBTA mood data from YAML files."""

    MOOD_CATEGORIES = {
        'Indicative': ['Indicative'],
        'Imperative': ['Imperative'],
        'Obligation': ["'should' Obligation", "'must' Obligation", 'Forbidden Obligation', "'should not' Obligation"],
        'Permissive': ["'may' (permissive)"],
        'Potential': ["'might' Potential", 'Probable Potential', 'Definite Potential', 'Unlikely Potential'],
        'Subjunctive': ['Subjunctive'],  # If present
        'Optative': ['Optative'],  # If present
        'Conditional': ['Conditional'],  # If present
    }

    def __init__(self, data_dir: str = None):
        if data_dir is None:
            data_dir = "/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/.data/commentary"
        self.data_dir = Path(data_dir)
        self.moods = defaultdict(list)
        self.stats = Counter()

    def load_yaml(self, filepath: str) -> Optional[Dict]:
        """Load YAML file safely."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return None

    def extract_verbs(self, node: Any, context_info: Dict = None) -> List[Dict]:
        """Recursively extract verb nodes from clause structure."""
        if context_info is None:
            context_info = {}

        verbs = []

        if isinstance(node, dict):
            # Check if this is a VP (verb phrase) - VP contains Constituent and Mood fields
            if node.get('Part') == 'VP' and 'children' in node and isinstance(node['children'], list):
                # Extract verb from VP's children
                for child in node['children']:
                    if isinstance(child, dict):
                        constituent = child.get('Constituent')
                        mood = child.get('Mood')
                        time = child.get('Time')
                        aspect = child.get('Aspect')
                        polarity = child.get('Polarity')

                        if constituent and mood:
                            verbs.append({
                                'constituent': constituent,
                                'mood': mood,
                                'time': time,
                                'aspect': aspect,
                                'polarity': polarity,
                                'verse': context_info.get('verse'),
                                'illocutionary_force': context_info.get('illocutionary_force'),
                                'clause_type': context_info.get('clause_type'),
                            })

            # Recursively process children
            if 'children' in node and isinstance(node['children'], list):
                for child in node['children']:
                    verbs.extend(self.extract_verbs(child, context_info))

        elif isinstance(node, list):
            for item in node:
                verbs.extend(self.extract_verbs(item, context_info))

        return verbs

    def extract_clause_info(self, clause: Dict) -> Tuple[str, str]:
        """Extract IlLocutionary Force and Type from clause."""
        illocution = clause.get('Illocutionary Force', 'Unknown')
        clause_type = clause.get('Type', 'Unknown')
        return illocution, clause_type

    def process_verse(self, filepath: str) -> List[Dict]:
        """Process a single TBTA verse file."""
        data = self.load_yaml(filepath)
        if not data:
            return []

        verse = data.get('verse')
        clauses = data.get('clauses', [])
        verbs = []

        for clause in clauses:
            if isinstance(clause, dict):
                illocution, clause_type = self.extract_clause_info(clause)
                context = {
                    'verse': verse,
                    'illocutionary_force': illocution,
                    'clause_type': clause_type,
                }
                clause_verbs = self.extract_verbs(clause, context)
                verbs.extend(clause_verbs)

        return verbs

    def categorize_mood(self, mood_value: str) -> str:
        """Categorize a specific mood value."""
        for category, values in self.MOOD_CATEGORIES.items():
            if mood_value in values:
                return category
        return 'Other'

    def analyze_file(self, filepath: str) -> None:
        """Analyze a single file and record statistics."""
        verbs = self.process_verse(filepath)
        for verb in verbs:
            mood = verb['mood']
            category = self.categorize_mood(mood)
            self.moods[category].append(verb)
            self.stats[mood] += 1

    def analyze_directory(self, pattern: str = "**/*tbta.yaml", limit: int = None) -> None:
        """Analyze all TBTA files in directory."""
        files = sorted(self.data_dir.glob(pattern))
        if limit:
            files = files[:limit]

        for i, filepath in enumerate(files):
            self.analyze_file(str(filepath))
            if (i + 1) % 50 == 0:
                print(f"  Processed {i + 1}/{len(files)} files...")

    def print_mood_summary(self) -> None:
        """Print summary of moods found."""
        print("\n" + "=" * 70)
        print("MOOD STATISTICS SUMMARY")
        print("=" * 70)

        total = sum(self.stats.values())
        print(f"\nTotal verbs found: {total}\n")

        print("Moods by frequency:")
        print("-" * 70)
        for mood, count in self.stats.most_common():
            percentage = (count / total * 100) if total > 0 else 0
            print(f"  {mood:40s} {count:6d} ({percentage:5.2f}%)")

        print("\n" + "=" * 70)
        print("MOODS BY CATEGORY")
        print("=" * 70)

        for category in sorted(self.moods.keys()):
            verbs = self.moods[category]
            print(f"\n{category}: {len(verbs)} verbs")
            print("-" * 70)

            # Show sample verbs from this category
            sample_size = min(5, len(verbs))
            for verb in verbs[:sample_size]:
                print(f"  {verb['verse']:12s} | {verb['constituent']:15s} | {verb['mood']}")
                print(f"               | Time: {verb['time']:20s} Aspect: {verb['aspect']}")
                print(f"               | Force: {verb['illocutionary_force']:20s} Type: {verb['clause_type']}")

    def analyze_test_cases(self) -> None:
        """Analyze specific test cases from experiment."""
        print("\n" + "=" * 70)
        print("TEST CASE ANALYSIS")
        print("=" * 70)

        test_cases = [
            {
                'file': 'MAT/024/001/MAT-020-001-tbta.yaml',
                'verb': 'look',
                'expected_mood': "'should' Obligation",
                'test_name': 'Test 1: Obligation (MAT 24:1)',
            },
            {
                'file': 'MAT/024/006/MAT-020-006-tbta.yaml',
                'verb': 'hear',
                'expected_mood': 'Indicative',
                'test_name': 'Test 2: Indicative Future (MAT 24:6)',
            },
            {
                'file': 'MAT/024/002/MAT-020-002-tbta.yaml',
                'verb': 'see',
                'expected_mood': 'Indicative',
                'test_name': 'Test 3: Indicative Present (MAT 24:2)',
            },
        ]

        for test in test_cases:
            filepath = self.data_dir / test['file']
            if filepath.exists():
                print(f"\n{test['test_name']}")
                print("-" * 70)

                verbs = self.process_verse(str(filepath))
                target_verb = None

                for verb in verbs:
                    if verb['constituent'] == test['verb']:
                        target_verb = verb
                        break

                if target_verb:
                    actual_mood = target_verb['mood']
                    expected = test['expected_mood']
                    result = 'PASS' if actual_mood == expected else 'FAIL'

                    print(f"Result: {result}")
                    print(f"  Expected: {expected}")
                    print(f"  Actual:   {actual_mood}")
                    print(f"  Verse:    {target_verb['verse']}")
                    print(f"  Time:     {target_verb['time']}")
                    print(f"  Aspect:   {target_verb['aspect']}")
                    print(f"  Force:    {target_verb['illocutionary_force']}")
                    print(f"  Type:     {target_verb['clause_type']}")
                else:
                    print(f"Result: NOT FOUND")
                    print(f"  Verb '{test['verb']}' not found in {test['file']}")
                    print(f"  Available verbs:")
                    for verb in verbs[:5]:
                        print(f"    - {verb['constituent']}")
            else:
                print(f"\nTest file not found: {filepath}")

    def identify_mood_from_context(self, verb: Dict) -> str:
        """Attempt to identify mood from contextual features."""
        # If mood is already known, return it
        if verb.get('mood'):
            return verb['mood']

        # Level 1: Check IlLocutionary Force
        force = verb.get('illocutionary_force', '')
        if 'Imperative' in force or 'Hortative' in force:
            return 'Imperative'

        # Level 2: Check for obligation/permission words in constituent
        constituent = verb.get('constituent', '').lower()
        if any(word in constituent for word in ['must', 'should', 'may', 'can', 'ought', 'shall']):
            return 'Obligation'

        # Level 3: Check for conditional structure
        clause_type = verb.get('clause_type', '')
        time = verb.get('time', '')
        if 'Event Modifier' in clause_type and 'Future' in time:
            return 'Conditional'

        # Level 4: Default to Indicative for statements
        return 'Indicative'


def main():
    """Main test entry point."""
    print("TBTA Mood Prediction Testing")
    print("=" * 70)
    print()

    analyzer = MoodAnalyzer()

    # Analyze Matthew 24 as test corpus
    print("Analyzing Matthew 24 TBTA data...")
    print()
    analyzer.analyze_directory("MAT/024/*/*tbta.yaml", limit=None)

    # Print results
    analyzer.print_mood_summary()
    analyzer.analyze_test_cases()

    # Export results
    print("\n" + "=" * 70)
    print("EXPORTING RESULTS")
    print("=" * 70)

    output_file = Path(__file__).parent / "mood_test_results.json"
    results = {
        'total_verbs': sum(analyzer.stats.values()),
        'mood_distribution': dict(analyzer.stats),
        'categories': {
            cat: len(verbs)
            for cat, verbs in analyzer.moods.items()
        },
    }

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results exported to: {output_file}")
    print()


if __name__ == '__main__':
    main()
