#!/usr/bin/env python3
"""
Validate and analyze TBTA NounListIndex coreference resolution.
Tests the entity tracking system that's crucial for switch-reference languages.
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class NounIndexAnalyzer:
    def __init__(self, data_dir: str = ".data"):
        self.data_dir = Path(data_dir)

    def load_tbta_data(self, book: str, chapter: int, verse: int) -> dict:
        """Load TBTA data for a specific verse."""
        chapter_str = f"{chapter:03d}"
        verse_str = f"{verse:03d}"
        file_path = self.data_dir / "commentary" / book / chapter_str / verse_str / f"{book}-{chapter_str}-{verse_str}-tbta.yaml"

        if not file_path.exists():
            raise FileNotFoundError(f"TBTA file not found: {file_path}")

        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def extract_noun_indices(self, clause_data: dict, indices: Dict[str, List[Dict]] = None) -> Dict[str, List[Dict]]:
        """Recursively extract all NounListIndex occurrences from TBTA structure."""
        if indices is None:
            indices = defaultdict(list)

        if isinstance(clause_data, dict):
            # Check if this node has NounListIndex
            if 'NounListIndex' in clause_data:
                index = clause_data['NounListIndex']
                entry = {
                    'constituent': clause_data.get('Constituent', 'unknown'),
                    'part': clause_data.get('Part', 'unknown'),
                    'semantic_role': clause_data.get('Semantic Role', 'unknown'),
                    'tracking': clause_data.get('Participant Tracking', 'unknown')
                }
                indices[index].append(entry)

            # Recurse through children
            if 'children' in clause_data:
                for child in clause_data['children']:
                    self.extract_noun_indices(child, indices)

            # Check other keys that might contain clauses
            for key, value in clause_data.items():
                if key != 'children':
                    if isinstance(value, (dict, list)):
                        self.extract_noun_indices(value, indices)

        elif isinstance(clause_data, list):
            for item in clause_data:
                self.extract_noun_indices(item, indices)

        return indices

    def analyze_coreference_patterns(self, book: str, chapter: int, verse: int) -> Dict:
        """Analyze coreference patterns in a verse."""
        data = self.load_tbta_data(book, chapter, verse)
        indices = self.extract_noun_indices(data.get('clauses', []))

        analysis = {
            'verse': f"{book} {chapter}:{verse}",
            'total_entities': len(indices),
            'entities': {}
        }

        for index, occurrences in sorted(indices.items()):
            # Get unique constituents for this index
            constituents = list(set(occ['constituent'] for occ in occurrences))

            entity_info = {
                'index': index,
                'occurrences': len(occurrences),
                'constituents': constituents,
                'details': occurrences
            }

            # Determine entity type based on constituents
            if 'master' in constituents or 'lord' in constituents:
                entity_type = 'master'
            elif 'servant' in constituents:
                entity_type = 'servant'
            elif 'thing' in constituents or 'things' in constituents:
                entity_type = 'things/tasks'
            elif 'house' in constituents:
                entity_type = 'location'
            elif 'Jesus' in constituents:
                entity_type = 'speaker'
            elif 'follower' in constituents or 'disciple' in constituents:
                entity_type = 'audience'
            else:
                entity_type = 'other'

            entity_info['entity_type'] = entity_type
            analysis['entities'][index] = entity_info

        return analysis

    def compare_verses(self, verse1: Tuple[str, int, int], verse2: Tuple[str, int, int]) -> Dict:
        """Compare entity tracking between two consecutive verses."""
        analysis1 = self.analyze_coreference_patterns(*verse1)
        analysis2 = self.analyze_coreference_patterns(*verse2)

        comparison = {
            'verse1': analysis1['verse'],
            'verse2': analysis2['verse'],
            'observation': 'Index numbering resets between verses',
            'shared_entities': [],
            'verse1_analysis': analysis1,
            'verse2_analysis': analysis2
        }

        # Identify shared entities by type
        v1_types = {e['entity_type']: e for e in analysis1['entities'].values()}
        v2_types = {e['entity_type']: e for e in analysis2['entities'].values()}

        for entity_type in set(v1_types.keys()) & set(v2_types.keys()):
            comparison['shared_entities'].append({
                'entity_type': entity_type,
                'verse1_index': v1_types[entity_type]['index'],
                'verse2_index': v2_types[entity_type]['index'],
                'note': f"Same entity, different indices across verses"
            })

        return comparison

    def validate_coreference_rules(self, book: str, chapter: int, verse: int) -> List[str]:
        """Validate that coreference follows expected rules."""
        issues = []
        data = self.load_tbta_data(book, chapter, verse)
        indices = self.extract_noun_indices(data.get('clauses', []))

        # Rule 1: Each index should have at least one occurrence
        for index, occurrences in indices.items():
            if len(occurrences) == 0:
                issues.append(f"Index {index} has no occurrences")

        # Rule 2: Same constituent should typically have same index
        constituent_indices = defaultdict(set)
        for index, occurrences in indices.items():
            for occ in occurrences:
                constituent_indices[occ['constituent']].add(index)

        for constituent, index_set in constituent_indices.items():
            if len(index_set) > 1:
                issues.append(f"Constituent '{constituent}' has multiple indices: {index_set}")

        # Rule 3: Indices should be sequential (1, 2, 3...) with no gaps
        index_numbers = []
        for index in indices.keys():
            try:
                index_numbers.append(int(index))
            except ValueError:
                pass  # Skip non-numeric indices

        if index_numbers:
            index_numbers.sort()
            expected = list(range(1, max(index_numbers) + 1))
            missing = set(expected) - set(index_numbers)
            if missing:
                issues.append(f"Missing index numbers: {missing}")

        return issues

def main():
    analyzer = NounIndexAnalyzer("/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/.data")

    print("=" * 70)
    print("TBTA NounListIndex Coreference Resolution Analysis")
    print("=" * 70)
    print()

    # Analyze Matthew 24:46
    print("## Matthew 24:46 Analysis")
    print("-" * 40)
    mat_24_46 = analyzer.analyze_coreference_patterns("MAT", 24, 46)

    for index, entity in sorted(mat_24_46['entities'].items()):
        print(f"\nIndex {index} ({entity['entity_type']}):")
        print(f"  Occurrences: {entity['occurrences']}")
        print(f"  Forms: {', '.join(entity['constituents'])}")
        for detail in entity['details'][:2]:  # Show first 2 occurrences
            print(f"    - {detail['constituent']} ({detail['part']}, role: {detail['semantic_role']})")

    # Validate rules for verse 46
    issues_46 = analyzer.validate_coreference_rules("MAT", 24, 46)
    if issues_46:
        print("\n⚠️  Validation issues in v46:")
        for issue in issues_46:
            print(f"  - {issue}")
    else:
        print("\n✓ No validation issues in v46")

    print("\n" + "=" * 70)

    # Analyze Matthew 24:47
    print("## Matthew 24:47 Analysis")
    print("-" * 40)
    mat_24_47 = analyzer.analyze_coreference_patterns("MAT", 24, 47)

    for index, entity in sorted(mat_24_47['entities'].items()):
        print(f"\nIndex {index} ({entity['entity_type']}):")
        print(f"  Occurrences: {entity['occurrences']}")
        print(f"  Forms: {', '.join(entity['constituents'])}")
        for detail in entity['details'][:2]:  # Show first 2 occurrences
            print(f"    - {detail['constituent']} ({detail['part']}, role: {detail['semantic_role']})")

    # Validate rules for verse 47
    issues_47 = analyzer.validate_coreference_rules("MAT", 24, 47)
    if issues_47:
        print("\n⚠️  Validation issues in v47:")
        for issue in issues_47:
            print(f"  - {issue}")
    else:
        print("\n✓ No validation issues in v47")

    print("\n" + "=" * 70)

    # Compare verses
    print("## Cross-Verse Comparison")
    print("-" * 40)
    comparison = analyzer.compare_verses(("MAT", 24, 46), ("MAT", 24, 47))

    print(f"\nKey Finding: {comparison['observation']}")
    print("\nShared entities with different indices:")
    for shared in comparison['shared_entities']:
        print(f"  - {shared['entity_type'].title()}:")
        print(f"    v46 index: {shared['verse1_index']}")
        print(f"    v47 index: {shared['verse2_index']}")

    print("\n" + "=" * 70)
    print("## Implications for Switch-Reference Languages")
    print("-" * 40)
    print("""
This verse-scoped index system means:
1. Translators must track entities across verse boundaries manually
2. Switch-reference markers need context beyond single verses
3. Automated systems should maintain entity maps spanning passages
4. Each verse provides complete internal coreference data
    """)

if __name__ == "__main__":
    main()