#!/usr/bin/env python3
"""
Stratified sampling for number systems test set generation.
Stage 4B: Sample verses with balance across multiple dimensions.
"""

import yaml
import random
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

# Load files
EXPERIMENTS_DIR = Path("/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments")
RAW_DATA_PATH = EXPERIMENTS_DIR / "raw_tbta_data.yaml"
ARBITRARITY_PATH = EXPERIMENTS_DIR / "ARBITRARITY-CLASSIFICATION.md"

# Book metadata for genre classification
BOOK_GENRES = {
    # Torah (Law + Narrative)
    'GEN': 'narrative', 'EXO': 'law', 'LEV': 'law', 'NUM': 'law', 'DEU': 'law',
    # Historical (Narrative)
    'JOS': 'narrative', 'JDG': 'narrative', 'RUT': 'narrative',
    '1SA': 'narrative', '2SA': 'narrative', '1KI': 'narrative', '2KI': 'narrative',
    '1CH': 'narrative', '2CH': 'narrative', 'EZR': 'narrative', 'NEH': 'narrative', 'EST': 'narrative',
    # Wisdom
    'JOB': 'wisdom', 'PSA': 'poetry', 'PRO': 'wisdom', 'ECC': 'wisdom', 'SNG': 'poetry',
    # Prophets
    'ISA': 'prophecy', 'JER': 'prophecy', 'LAM': 'poetry', 'EZK': 'prophecy', 'DAN': 'prophecy',
    'HOS': 'prophecy', 'JOL': 'prophecy', 'AMO': 'prophecy', 'OBA': 'prophecy',
    'JON': 'narrative', 'MIC': 'prophecy', 'NAM': 'prophecy', 'HAB': 'prophecy',
    'ZEP': 'prophecy', 'HAG': 'prophecy', 'ZEC': 'prophecy', 'MAL': 'prophecy',
    # Gospels (Narrative)
    'MAT': 'narrative', 'MRK': 'narrative', 'LUK': 'narrative', 'JHN': 'narrative',
    # Acts (Narrative)
    'ACT': 'narrative',
    # Epistles
    'ROM': 'epistle', '1CO': 'epistle', '2CO': 'epistle', 'GAL': 'epistle',
    'EPH': 'epistle', 'PHP': 'epistle', 'COL': 'epistle',
    '1TH': 'epistle', '2TH': 'epistle', '1TI': 'epistle', '2TI': 'epistle',
    'TIT': 'epistle', 'PHM': 'epistle', 'HEB': 'epistle',
    'JAS': 'epistle', '1PE': 'epistle', '2PE': 'epistle',
    '1JN': 'epistle', '2JN': 'epistle', '3JN': 'epistle', 'JUD': 'epistle',
    # Revelation (Prophecy)
    'REV': 'prophecy'
}

# OT/NT classification
OT_BOOKS = set(['GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT',
                '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR', 'NEH', 'EST',
                'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK', 'DAN',
                'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL'])

# Non-arbitrary verses (from ARBITRARITY-CLASSIFICATION.md)
NON_ARBITRARY_VERSES = {
    # Trinity references (HIGH stakes)
    'GEN.001.026': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    'GEN.001.027': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    'GEN.003.022': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    'GEN.011.007': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    'ISA.006.008': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    'MAT.028.019': {'reason_group': 'Trinity references', 'stakes': 'high', 'difficulty': 'adversarial'},
    '2CO.013.014': {'reason_group': 'Trinity references', 'stakes': 'medium', 'difficulty': 'adversarial'},

    # Apostolic authority (MEDIUM stakes)
    'ACT.015.025': {'reason_group': 'Apostolic authority', 'stakes': 'medium', 'difficulty': 'adversarial'},
    'ACT.015.028': {'reason_group': 'Apostolic authority', 'stakes': 'medium', 'difficulty': 'adversarial'},

    # Paired disciples/witnesses (LOW stakes, linguistic)
    'LUK.024.013': {'reason_group': 'Paired disciples', 'stakes': 'low', 'difficulty': 'typical'},
    'ACT.013.002': {'reason_group': 'Paired disciples', 'stakes': 'low', 'difficulty': 'typical'},
    'MRK.006.007': {'reason_group': 'Paired disciples', 'stakes': 'low', 'difficulty': 'typical'},
    'LUK.010.001': {'reason_group': 'Paired disciples', 'stakes': 'low', 'difficulty': 'typical'},

    # Small group theology (MEDIUM stakes)
    'MAT.018.020': {'reason_group': 'Small group theology', 'stakes': 'medium', 'difficulty': 'adversarial'},
    'MAT.026.026': {'reason_group': 'Small group theology', 'stakes': 'low', 'difficulty': 'typical'},
    'ACT.002.046': {'reason_group': 'Small group theology', 'stakes': 'low', 'difficulty': 'typical'},
}

def parse_verse_ref(ref):
    """Parse BOOK.chapter.verse into components."""
    parts = ref.split('.')
    return {
        'book': parts[0],
        'chapter': int(parts[1]),
        'verse': int(parts[2]),
        'testament': 'OT' if parts[0] in OT_BOOKS else 'NT',
        'genre': BOOK_GENRES.get(parts[0], 'unknown')
    }

def classify_verse(ref, value):
    """Classify a verse across all stratification dimensions."""
    parsed = parse_verse_ref(ref)

    # Check if non-arbitrary
    is_non_arbitrary = ref in NON_ARBITRARY_VERSES
    non_arb_info = NON_ARBITRARY_VERSES.get(ref, {})

    return {
        'reference': ref,
        'tbta_value': value,
        'testament': parsed['testament'],
        'genre': parsed['genre'],
        'book': parsed['book'],
        'difficulty': non_arb_info.get('difficulty', 'typical'),
        'arbitrarity': 'non-arbitrary' if is_non_arbitrary else 'arbitrary',
        'reason_group': non_arb_info.get('reason_group', None),
        'stakes': non_arb_info.get('stakes', None)
    }

def stratified_sample(verses_by_value, targets):
    """
    Perform stratified sampling with multiple dimension balancing.

    targets = {
        'Dual': 120,
        'Trial': 100,
        'Paucal': 52,  # All verses (low frequency)
        'Singular': 150,
        'Plural': 150,
        'Quadrial': 20
    }
    """
    sampled = {}
    statistics = {}

    for value, target_count in targets.items():
        if value not in verses_by_value:
            print(f"WARNING: {value} not found in data")
            continue

        available_verses = verses_by_value[value]
        total_available = len(available_verses)

        print(f"\n=== Sampling {value}: Target {target_count}, Available {total_available} ===")

        # Classify all verses
        classified = [classify_verse(ref, value) for ref in available_verses]

        # Separate non-arbitrary (must include ALL)
        non_arbitrary = [v for v in classified if v['arbitrarity'] == 'non-arbitrary']
        arbitrary = [v for v in classified if v['arbitrarity'] == 'arbitrary']

        print(f"  Non-arbitrary: {len(non_arbitrary)} (mandatory)")
        print(f"  Arbitrary: {len(arbitrary)} (sampling pool)")

        # For Paucal: use all verses if count < target
        if total_available <= target_count:
            selected = classified
            print(f"  Using ALL {len(selected)} verses (below target)")
        else:
            # Start with all non-arbitrary
            selected = non_arbitrary[:]
            remaining_slots = target_count - len(non_arbitrary)

            if remaining_slots > 0:
                # Stratify arbitrary verses by testament
                ot_verses = [v for v in arbitrary if v['testament'] == 'OT']
                nt_verses = [v for v in arbitrary if v['testament'] == 'NT']

                # Target 77% OT / 23% NT
                ot_target = int(remaining_slots * 0.77)
                nt_target = remaining_slots - ot_target

                # Sample with replacement if needed
                ot_sample = random.sample(ot_verses, min(ot_target, len(ot_verses)))
                nt_sample = random.sample(nt_verses, min(nt_target, len(nt_verses)))

                # If one testament falls short, fill from the other
                if len(ot_sample) < ot_target and len(nt_verses) > nt_target:
                    extra_needed = ot_target - len(ot_sample)
                    extra_nt = random.sample(nt_verses, min(nt_target + extra_needed, len(nt_verses)))
                    nt_sample = extra_nt
                elif len(nt_sample) < nt_target and len(ot_verses) > ot_target:
                    extra_needed = nt_target - len(nt_sample)
                    extra_ot = random.sample(ot_verses, min(ot_target + extra_needed, len(ot_verses)))
                    ot_sample = extra_ot

                selected.extend(ot_sample)
                selected.extend(nt_sample)

        # Shuffle to mix non-arbitrary and arbitrary
        random.shuffle(selected)

        # Calculate statistics
        ot_count = len([v for v in selected if v['testament'] == 'OT'])
        nt_count = len([v for v in selected if v['testament'] == 'NT'])
        genre_counts = defaultdict(int)
        book_counts = defaultdict(int)
        difficulty_counts = defaultdict(int)

        for v in selected:
            genre_counts[v['genre']] += 1
            book_counts[v['book']] += 1
            difficulty_counts[v['difficulty']] += 1

        statistics[value] = {
            'total': len(selected),
            'testament': {'OT': ot_count, 'NT': nt_count},
            'testament_pct': {'OT': f"{ot_count/len(selected)*100:.1f}%", 'NT': f"{nt_count/len(selected)*100:.1f}%"},
            'genres': dict(genre_counts),
            'books': dict(book_counts),
            'book_count': len(book_counts),
            'difficulty': dict(difficulty_counts),
            'non_arbitrary_count': len([v for v in selected if v['arbitrarity'] == 'non-arbitrary'])
        }

        sampled[value] = selected

        print(f"  Final sample: {len(selected)} verses")
        print(f"    Testament: OT {ot_count} ({ot_count/len(selected)*100:.1f}%), NT {nt_count} ({nt_count/len(selected)*100:.1f}%)")
        print(f"    Books: {len(book_counts)} different books")
        print(f"    Non-arbitrary: {statistics[value]['non_arbitrary_count']}")

    return sampled, statistics

def split_datasets(sampled_verses, split_ratios=(0.4, 0.3, 0.3)):
    """Split into train/test/validate with stratification."""
    train_ratio, test_ratio, validate_ratio = split_ratios

    train = {}
    test = {}
    validate = {}

    for value, verses in sampled_verses.items():
        n = len(verses)
        train_n = int(n * train_ratio)
        test_n = int(n * test_ratio)
        # validate gets the remainder

        # Shuffle again for split randomness
        shuffled = verses[:]
        random.shuffle(shuffled)

        train[value] = shuffled[:train_n]
        test[value] = shuffled[train_n:train_n+test_n]
        validate[value] = shuffled[train_n+test_n:]

        print(f"{value}: Train {len(train[value])}, Test {len(test[value])}, Validate {len(validate[value])}")

    return train, test, validate

def generate_yaml_files(train, test, validate, output_dir):
    """Generate 6 YAML files (3 answer sheets + 3 question sheets)."""

    def create_answer_sheet(dataset, name):
        """Create answer sheet with TBTA values."""
        data = {
            'feature': 'number-systems',
            'dataset': name,
            'generated': datetime.utcnow().isoformat() + 'Z',
            'total_verses': sum(len(verses) for verses in dataset.values()),
            'values': []
        }

        for value, verses in sorted(dataset.items()):
            value_data = {
                'name': value,
                'count': len(verses),
                'distribution': {
                    'OT': len([v for v in verses if v['testament'] == 'OT']),
                    'NT': len([v for v in verses if v['testament'] == 'NT'])
                },
                'genres': dict(defaultdict(int)),
                'books': dict(defaultdict(int)),
                'verses': []
            }

            # Calculate genre and book counts
            genre_counts = defaultdict(int)
            book_counts = defaultdict(int)
            for v in verses:
                genre_counts[v['genre']] += 1
                book_counts[v['book']] += 1

            value_data['genres'] = dict(genre_counts)
            value_data['books'] = dict(book_counts)

            # Add verse entries
            for v in verses:
                verse_entry = {
                    'reference': v['reference'],
                    'tbta_value': v['tbta_value'],
                    'testament': v['testament'],
                    'genre': v['genre'],
                    'book': v['book'],
                    'difficulty': v['difficulty'],
                    'arbitrarity': v['arbitrarity']
                }

                if v['reason_group']:
                    verse_entry['reason_group'] = v['reason_group']
                if v['stakes']:
                    verse_entry['theological_stakes'] = v['stakes']

                value_data['verses'].append(verse_entry)

            data['values'].append(value_data)

        return data

    def create_question_sheet(dataset, name):
        """Create question sheet WITHOUT TBTA values (for blind testing)."""
        data = {
            'feature': 'number-systems',
            'dataset': name + '_questions',
            'generated': datetime.utcnow().isoformat() + 'Z',
            'total_verses': sum(len(verses) for verses in dataset.values()),
            'note': 'QUESTION SHEET: TBTA values intentionally omitted for blind testing',
            'verses': []
        }

        # Flatten all verses
        all_verses = []
        for verses in dataset.values():
            all_verses.extend(verses)

        # Sort by reference for easier lookup
        all_verses.sort(key=lambda v: v['reference'])

        for v in all_verses:
            verse_entry = {
                'reference': v['reference'],
                'testament': v['testament'],
                'genre': v['genre'],
                'book': v['book'],
                # NOTE: No tbta_value here - that's the answer!
                'translations': 'TO_BE_FETCHED'  # Placeholder for translation data
            }

            data['verses'].append(verse_entry)

        return data

    # Generate all 6 files
    files_created = []

    # Train
    train_answer = create_answer_sheet(train, 'train')
    train_question = create_question_sheet(train, 'train')
    train_answer_path = output_dir / 'train.yaml'
    train_question_path = output_dir / 'train_questions.yaml'
    with open(train_answer_path, 'w') as f:
        yaml.dump(train_answer, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    with open(train_question_path, 'w') as f:
        yaml.dump(train_question, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    files_created.extend([str(train_answer_path), str(train_question_path)])

    # Test
    test_answer = create_answer_sheet(test, 'test')
    test_question = create_question_sheet(test, 'test')
    test_answer_path = output_dir / 'test.yaml'
    test_question_path = output_dir / 'test_questions.yaml'
    with open(test_answer_path, 'w') as f:
        yaml.dump(test_answer, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    with open(test_question_path, 'w') as f:
        yaml.dump(test_question, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    files_created.extend([str(test_answer_path), str(test_question_path)])

    # Validate
    validate_answer = create_answer_sheet(validate, 'validate')
    validate_question = create_question_sheet(validate, 'validate')
    validate_answer_path = output_dir / 'validate.yaml'
    validate_question_path = output_dir / 'validate_questions.yaml'
    with open(validate_answer_path, 'w') as f:
        yaml.dump(validate_answer, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    with open(validate_question_path, 'w') as f:
        yaml.dump(validate_question, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    files_created.extend([str(validate_answer_path), str(validate_question_path)])

    return files_created

def main():
    print("="*80)
    print("STAGE 4B: Stratified Sampling for Number Systems Test Set")
    print("="*80)

    # Load raw TBTA data
    print(f"\nLoading raw data from {RAW_DATA_PATH}")
    with open(RAW_DATA_PATH) as f:
        raw_data = yaml.safe_load(f)

    # Extract verse lists by value
    verses_by_value = {}
    for value_entry in raw_data['value']:
        value_name = value_entry['specific_value']
        verses = value_entry['verses']
        verses_by_value[value_name] = verses
        print(f"  {value_name}: {len(verses)} verses")

    # Define sampling targets (per TEST-SET-PLAN.md)
    targets = {
        'Singular': 150,
        'Dual': 120,
        'Trial': 100,
        'Paucal': 52,  # Use all (low frequency)
        'Plural': 150,
        'Quadrial': 20
    }

    # Perform stratified sampling
    print("\n" + "="*80)
    print("STRATIFIED SAMPLING")
    print("="*80)
    sampled, statistics = stratified_sample(verses_by_value, targets)

    # Split into train/test/validate
    print("\n" + "="*80)
    print("TRAIN/TEST/VALIDATE SPLIT (40%/30%/30%)")
    print("="*80)
    train, test, validate = split_datasets(sampled)

    # Generate YAML files
    print("\n" + "="*80)
    print("GENERATING YAML FILES")
    print("="*80)
    files = generate_yaml_files(train, test, validate, EXPERIMENTS_DIR)

    print("\nFiles created:")
    for f in files:
        print(f"  ✓ {f}")

    # Generate sampling report
    report_path = EXPERIMENTS_DIR / "SAMPLING-REPORT.md"
    with open(report_path, 'w') as f:
        f.write("# Number Systems Feature - Sampling Report\n\n")
        f.write(f"**Date**: {datetime.utcnow().isoformat()}Z\n")
        f.write(f"**Analyst**: Claude Sonnet 4.5 (Analyst Agent)\n\n")
        f.write("---\n\n")
        f.write("## Executive Summary\n\n")

        total_sampled = sum(len(verses) for verses in sampled.values())
        f.write(f"Successfully generated stratified test sets with {total_sampled} total verses ")
        f.write(f"across 6 number values, split into train/test/validate datasets.\n\n")

        f.write("### Dataset Sizes\n\n")
        f.write("| Dataset | Verses | Percentage |\n")
        f.write("|---------|--------|------------|\n")
        train_count = sum(len(v) for v in train.values())
        test_count = sum(len(v) for v in test.values())
        validate_count = sum(len(v) for v in validate.values())
        f.write(f"| Train | {train_count} | {train_count/total_sampled*100:.1f}% |\n")
        f.write(f"| Test | {test_count} | {test_count/total_sampled*100:.1f}% |\n")
        f.write(f"| Validate | {validate_count} | {validate_count/total_sampled*100:.1f}% |\n")
        f.write(f"| **Total** | **{total_sampled}** | **100%** |\n\n")

        f.write("---\n\n")
        f.write("## Sampling Statistics by Value\n\n")

        for value in sorted(statistics.keys()):
            stats = statistics[value]
            f.write(f"### {value}\n\n")
            f.write(f"- **Total sampled**: {stats['total']} verses\n")
            f.write(f"- **Testament**: OT {stats['testament']['OT']} ({stats['testament_pct']['OT']}), ")
            f.write(f"NT {stats['testament']['NT']} ({stats['testament_pct']['NT']})\n")
            f.write(f"- **Books**: {stats['book_count']} different books\n")
            f.write(f"- **Non-arbitrary**: {stats['non_arbitrary_count']} verses\n")
            f.write(f"- **Genres**: {', '.join(f'{g}={c}' for g, c in sorted(stats['genres'].items()))}\n")
            f.write(f"- **Difficulty**: {', '.join(f'{d}={c}' for d, c in sorted(stats['difficulty'].items()))}\n")
            f.write("\n")

        f.write("---\n\n")
        f.write("## Files Generated\n\n")
        f.write("### Answer Sheets (WITH TBTA values)\n")
        f.write("- `train.yaml` - Training set with answers\n")
        f.write("- `test.yaml` - Test set with answers\n")
        f.write("- `validate.yaml` - Validation set with answers\n\n")
        f.write("### Question Sheets (WITHOUT TBTA values - for blind testing)\n")
        f.write("- `train_questions.yaml` - Training questions only\n")
        f.write("- `test_questions.yaml` - Test questions only\n")
        f.write("- `validate_questions.yaml` - Validation questions only\n\n")
        f.write("**NOTE**: Question sheets intentionally omit TBTA values to maintain blind testing protocol.\n\n")

        f.write("---\n\n")
        f.write("## Quality Metrics\n\n")
        f.write("### Success Criteria (from TEST-SET-PLAN.md)\n\n")
        f.write("| Metric | Target | Actual | Status |\n")
        f.write("|--------|--------|--------|--------|\n")

        # Check sample sizes
        for value in targets.keys():
            if value in statistics:
                actual = statistics[value]['total']
                target = targets[value]
                status = "✅" if actual >= min(target, verses_by_value.get(value, [9999]).__len__()) else "⚠️"
                f.write(f"| {value} sample size | ≥{target} | {actual} | {status} |\n")

        # Testament balance (check for overall dataset)
        total_ot = sum(stats['testament']['OT'] for stats in statistics.values())
        total_nt = sum(stats['testament']['NT'] for stats in statistics.values())
        ot_pct = total_ot / (total_ot + total_nt) * 100
        nt_pct = total_nt / (total_ot + total_nt) * 100
        testament_ok = "✅" if 72 <= ot_pct <= 82 else "⚠️"
        f.write(f"| Testament balance | 77% OT ±5% | {ot_pct:.1f}% OT / {nt_pct:.1f}% NT | {testament_ok} |\n")

        # Book diversity
        all_books = set()
        for stats in statistics.values():
            all_books.update(stats['books'].keys())
        book_ok = "✅" if len(all_books) >= 20 else "⚠️"
        f.write(f"| Book diversity | ≥20 books | {len(all_books)} books | {book_ok} |\n")

        # Non-arbitrary inclusion
        total_non_arb = sum(stats['non_arbitrary_count'] for stats in statistics.values())
        non_arb_ok = "✅" if total_non_arb >= 10 else "⚠️"
        f.write(f"| Non-arbitrary verses | ≥10 | {total_non_arb} | {non_arb_ok} |\n")

        f.write("\n---\n\n")
        f.write("## Next Steps\n\n")
        f.write("1. **Translation Data Acquisition** (Stage 4C):\n")
        f.write("   - Fetch translations for all verses in question sheets\n")
        f.write("   - Use languages: fij, tpi, haw, smo, slv, wbp, bis, ind, spa\n")
        f.write("   - Populate `translations` field in question sheets\n\n")
        f.write("2. **Algorithm Development** (Stage 5):\n")
        f.write("   - Use `train_questions.yaml` for prompt development\n")
        f.write("   - Lock predictions before viewing `train.yaml` answer sheet\n\n")
        f.write("3. **Validation** (Stage 6):\n")
        f.write("   - Run algorithm on `test_questions.yaml`\n")
        f.write("   - Compare predictions to `test.yaml` answers\n")
        f.write("   - Final verification on `validate_questions.yaml` vs `validate.yaml`\n\n")
        f.write("---\n\n")
        f.write("**Status**: Sampling Complete ✅\n")
        f.write(f"**Generated**: {datetime.utcnow().isoformat()}Z\n")

    print(f"\n✓ Sampling report: {report_path}")

    # Return question sheet paths only (per instructions)
    question_sheets = [
        str(EXPERIMENTS_DIR / 'train_questions.yaml'),
        str(EXPERIMENTS_DIR / 'test_questions.yaml'),
        str(EXPERIMENTS_DIR / 'validate_questions.yaml')
    ]

    print("\n" + "="*80)
    print("QUESTION SHEET PATHS (for return):")
    print("="*80)
    for qs in question_sheets:
        print(f"  {qs}")

    return ','.join(question_sheets)

if __name__ == '__main__':
    result = main()
    print(f"\nRETURN VALUE: {result}")
