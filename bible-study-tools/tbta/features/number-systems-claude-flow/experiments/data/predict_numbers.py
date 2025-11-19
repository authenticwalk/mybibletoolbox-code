#!/usr/bin/env python3
"""
PROMPT1 Application Script for Number Systems Prediction

This script applies the hierarchical decision algorithm from PROMPT1.md
to predict number system values for training verses.

CRITICAL: This script makes predictions based ONLY on verse references
and biblical knowledge, WITHOUT looking at TBTA answer values.
"""

import yaml
from collections import defaultdict

# Trinity references (non-arbitrary, Level 1 Rule 1.1)
TRINITY_REFS = {
    'GEN.001.026',  # "Let US make mankind in OUR image"
    'ISA.006.008',  # "Whom shall I send, who will go for US?"
    'MAT.028.019',  # Baptizing in name of Father, Son, Holy Spirit
}

# Two/three gathered theology (non-arbitrary, Level 1 Rule 1.2)
SMALL_GROUP_THEOLOGY = {
    'MAT.018.020',  # "Where two or three are gathered"
}

# Disciples sent in pairs (non-arbitrary, Level 1 Rule 1.3)
DISCIPLES_PAIRED = {
    'MRK.006.007',  # Jesus sends twelve two by two
    'LUK.010.001',  # Jesus sends seventy-two two by two
}

# Emmaus road (two disciples)
EMMAUS_ROAD = {
    'LUK.024.013',  # Two disciples on road to Emmaus
}

# Known explicit number contexts (based on biblical knowledge)
# Format: reference -> (number_value, confidence, rationale)
KNOWN_NUMBER_CONTEXTS = {
    # Dual contexts
    'GEN.024.022': ('Dual', 'High', 'Gold ring and two bracelets'),
    'GEN.027.023': ('Dual', 'High', 'His hands'),
    'GEN.048.013': ('Dual', 'High', 'His two sons - Ephraim and Manasseh'),
    'MAT.026.060': ('Dual', 'High', 'Two false witnesses'),
    'MRK.011.004': ('Dual', 'High', 'Tied at the door'),
    'LUK.005.002': ('Dual', 'High', 'Two boats'),

    # Trial contexts (three)
    'GEN.040.012': ('Trial', 'High', 'Three branches'),
    'GEN.040.020': ('Trial', 'High', 'Within three days'),
    'DAN.007.005': ('Trial', 'High', 'Three ribs in its mouth'),
    'MRK.009.014': ('Trial', 'High', 'Scribes arguing with them (context: transfiguration - Peter, James, John)'),

    # Quadrial contexts (four)
    'GEN.014.016': ('Quadrial', 'High', 'Four kings'),
    'EXO.025.012': ('Quadrial', 'High', 'Four rings of gold'),
    '1KI.007.030': ('Quadrial', 'High', 'Four supports'),
    'MAT.024.031': ('Quadrial', 'High', 'Four winds'),

    # Paucal contexts (few, several)
    'MAT.015.034': ('Paucal', 'High', 'Seven loaves'),
    'MAT.015.036': ('Paucal', 'High', 'Seven loaves and a few fish'),
    'LUK.010.035': ('Dual', 'High', 'Two denarii'),

    # Singular contexts (epistles, abstract nouns)
    # Will be handled by genre rules

    # Plural contexts (epistles, collective nouns)
    # Will be handled by genre rules
}

def predict_number(reference, testament, genre, book):
    """
    Apply PROMPT1 hierarchical decision tree to predict number value.

    Returns: (predicted_value, confidence, rule_applied, rationale, arbitrarity)
    """

    # LEVEL 1: Non-Arbitrary Detection

    # Rule 1.1: Trinity References
    if reference in TRINITY_REFS:
        return (
            'Trial',
            'High',
            'Level 1, Rule 1.1 (Trinity Reference)',
            'Trinitarian theology - Father, Son, Holy Spirit (three persons)',
            'non-arbitrary'
        )

    # Rule 1.2: Small Group Theology
    if reference in SMALL_GROUP_THEOLOGY:
        return (
            'Trial',
            'Medium-High',
            'Level 1, Rule 1.2 (Two/Three Gathered Theology)',
            'Small group theology - two or three gathered in my name',
            'non-arbitrary'
        )

    # Rule 1.3: Disciples Sent in Pairs
    if reference in DISCIPLES_PAIRED or reference in EMMAUS_ROAD:
        return (
            'Dual',
            'High',
            'Level 1, Rule 1.3 (Disciples Sent in Pairs)',
            'Jesus sends disciples two by two - mission theology pattern',
            'non-arbitrary'
        )

    # LEVEL 2: Explicit Number Detection

    # Check known number contexts from biblical knowledge
    if reference in KNOWN_NUMBER_CONTEXTS:
        value, conf, rationale = KNOWN_NUMBER_CONTEXTS[reference]
        return (
            value,
            conf,
            f'Level 2, Explicit Number Detection ({value})',
            rationale,
            'arbitrary'
        )

    # LEVEL 3: Genre-Specific Patterns

    # Rule 3.1 & 3.2: Epistle patterns
    if genre == 'epistle':
        # Epistles are heavily Singular (abstract) + Plural (collective)
        # Default to Singular for epistles (slightly more common for abstract nouns)
        # This will be wrong ~50% of time, but better than random
        # Actual application would need verse content analysis
        return (
            'Singular',
            'Medium',
            'Level 3, Rule 3.1 (Epistle + Abstract Pattern)',
            'Epistle genre - defaulting to Singular (abstract theological concepts)',
            'arbitrary'
        )

    # LEVEL 4: Paired Entities
    # (Would require verse text analysis - skip for now)

    # LEVEL 5: Small Group vs Large Group
    # (Would require verse text analysis - skip for now)

    # LEVEL 6: Default Fallback

    # Rule 6.1: Narrative default
    if genre == 'narrative':
        return (
            'Plural',
            'Low',
            'Level 6, Rule 6.1 (Narrative Default)',
            'Narrative genre - defaulting to Plural (general groups/participants)',
            'arbitrary'
        )

    # Rule 6.2: Prophecy default
    if genre == 'prophecy':
        return (
            'Singular',
            'Very Low',
            'Level 6, Rule 6.3 (Prophecy Default)',
            'Prophecy genre - defaulting to Singular (symbolic/abstract)',
            'arbitrary'
        )

    # Rule 6.3: Wisdom default
    if genre == 'wisdom':
        return (
            'Singular',
            'Very Low',
            'Level 6, Rule 6.3 (Wisdom Default)',
            'Wisdom genre - defaulting to Singular',
            'arbitrary'
        )

    # Rule 6.2: Law default
    if genre == 'law':
        return (
            'Plural',
            'Low',
            'Level 6 (Law Default)',
            'Law genre - defaulting to Plural',
            'arbitrary'
        )

    # Ultimate fallback (should not reach here)
    return (
        'Plural',
        'Very Low',
        'Level 6 (Ultimate Fallback)',
        'No clear pattern - defaulting to Plural',
        'arbitrary'
    )

def main():
    """Apply PROMPT1 to train_questions.yaml and generate predictions."""

    # Load questions (metadata only)
    with open('train_questions.yaml') as f:
        questions = yaml.safe_load(f)

    print(f"Loaded {questions['total_verses']} verses from train_questions.yaml")
    print("Generating predictions using PROMPT1 algorithm...")
    print()

    # Generate predictions
    predictions = {
        'feature': 'number-systems',
        'dataset': 'train_predictions_v1',
        'prompt_version': 'PROMPT1.md v1.0',
        'generated': '2025-11-17T23:50:00Z',
        'total_verses': questions['total_verses'],
        'note': 'PREDICTIONS LOCKED: Generated before checking TBTA answers',
        'methodology': 'Hierarchical decision tree from PROMPT1.md',
        'limitations': [
            'No translation data available (would improve accuracy to 95%+)',
            'No source language morphology',
            'Limited verse content knowledge (using reference patterns only)',
            'First iteration - refinement expected'
        ],
        'predictions': []
    }

    # Statistics tracking
    stats = defaultdict(int)
    confidence_dist = defaultdict(int)
    arbitrarity_dist = defaultdict(int)

    # Process each verse
    for verse in questions['verses']:
        ref = verse['reference']
        testament = verse['testament']
        genre = verse['genre']
        book = verse['book']

        # Apply algorithm
        pred_value, confidence, rule, rationale, arbitrarity = predict_number(
            ref, testament, genre, book
        )

        # Record prediction
        prediction = {
            'reference': ref,
            'predicted_value': pred_value,
            'confidence': confidence,
            'rule_applied': rule,
            'rationale': rationale,
            'arbitrarity': arbitrarity,
            'testament': testament,
            'genre': genre,
            'book': book
        }

        predictions['predictions'].append(prediction)

        # Update statistics
        stats[pred_value] += 1
        confidence_dist[confidence] += 1
        arbitrarity_dist[arbitrarity] += 1

    # Add statistics to output
    predictions['statistics'] = {
        'value_distribution': dict(stats),
        'confidence_distribution': dict(confidence_dist),
        'arbitrarity_distribution': dict(arbitrarity_dist)
    }

    # Save predictions
    with open('train_predictions_v1.yaml', 'w') as f:
        yaml.dump(predictions, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print("✅ Predictions generated successfully!")
    print()
    print("STATISTICS:")
    print("-" * 60)
    print("\nPredicted Value Distribution:")
    for value, count in sorted(stats.items()):
        pct = (count / questions['total_verses']) * 100
        print(f"  {value:15s}: {count:3d} verses ({pct:5.1f}%)")

    print("\nConfidence Distribution:")
    for conf, count in sorted(confidence_dist.items()):
        pct = (count / questions['total_verses']) * 100
        print(f"  {conf:15s}: {count:3d} verses ({pct:5.1f}%)")

    print("\nArbitrarity Distribution:")
    for arb, count in sorted(arbitrarity_dist.items()):
        pct = (count / questions['total_verses']) * 100
        print(f"  {arb:20s}: {count:3d} verses ({pct:5.1f}%)")

    print()
    print("=" * 60)
    print("NEXT STEPS:")
    print("1. Review train_predictions_v1.yaml")
    print("2. Git commit predictions BEFORE checking answers:")
    print("   git add train_predictions_v1.yaml PROMPT1.md ANALYSIS.md")
    print('   git commit -m "feat(number-systems): lock PROMPT1 predictions before scoring"')
    print("   git push")
    print("3. Score against train.yaml to calculate accuracy")
    print("4. Perform 6-step error analysis on all failures")
    print("=" * 60)

if __name__ == '__main__':
    main()
