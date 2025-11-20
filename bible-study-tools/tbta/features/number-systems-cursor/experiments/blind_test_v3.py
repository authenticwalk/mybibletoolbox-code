#!/usr/bin/env python3
"""
BLIND TESTING SCRIPT - Apply v3 algorithm to test set WITHOUT seeing answers.

CRITICAL: This script does NOT read test.yaml (answers).
It ONLY reads test_questions.yaml (verse references).

Process:
1. Load verse references from test_questions.yaml
2. Fetch verse texts using fetch_verse
3. Apply v3 PROMPT.md algorithm
4. Save predictions to test_predictions_LOCKED.yaml
5. Git commit (LOCK) before seeing answers
6. ONLY THEN can we score against test.yaml
"""

import yaml
import sys
from pathlib import Path
from collections import defaultdict

# Set up paths
PROJECT_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(PROJECT_ROOT / '.claude' / 'skills' / 'quote-bible' / 'scripts'))
sys.path.insert(0, str(PROJECT_ROOT))

from fetch_verse import fetch_verse, VerseFetchError

def parse_verse_ref(ref):
    """Parse USFM reference like 'GEN.001.026'."""
    parts = ref.split('.')
    return parts[0], int(parts[1]), int(parts[2])

def get_verse_text(ref):
    """Fetch English text for verse reference."""
    book, chapter, verse = parse_verse_ref(ref)
    try:
        translations = fetch_verse(book, chapter, verse)
        # Prefer NIV, ESV, NASB
        for pref in ['eng-NIV', 'eng-ESV', 'eng-NASB']:
            if pref in translations:
                return translations[pref]
        # Any English version
        for version, text in translations.items():
            if version.startswith('eng-'):
                return text
    except Exception as e:
        return None
    return None

def apply_v3_algorithm(text, ref):
    """
    Apply v3 PROMPT.md hierarchical algorithm.
    
    Returns: (predicted_value, rule_applied, confidence)
    """
    if not text:
        return 'P', 'L7: No text (default)', 'low'
    
    text_lower = text.lower()
    
    # LEVEL 1: Theological (HIGHEST PRIORITY)
    
    # Rule 1.1: Divine first-person plural (Trinity)
    if 'let us' in text_lower and any(word in text_lower for word in ['make', 'create', 'go down', 'confuse']):
        return 'T', 'L1.1: Divine first-person plural (Trinity)', 'high'
    
    # Rule 1.2: Trinity formula
    if 'father' in text_lower and 'son' in text_lower and ('spirit' in text_lower or 'holy spirit' in text_lower):
        return 'T', 'L1.2: Trinity formula', 'high'
    
    # Rule 1.3: Monotheism
    if any(phrase in text_lower for phrase in ['lord is one', 'one god', 'god alone']):
        return 'S', 'L1.3: Monotheism emphasis', 'high'
    
    # LEVEL 2: Natural Pairs
    
    # Rule 2.1: Body parts
    body_pairs = ['hands', 'eyes', 'feet', 'ears', 'arms', 'legs', 'cheeks', 'shoulders', 'knees', 'wings']
    for pair in body_pairs:
        if pair in text_lower:
            return 'D', f'L2.1: Natural pair ({pair})', 'high'
    
    # LEVEL 3: Explicit Numbers + Focus Test
    
    # Helper: Check if number is focus (simplified heuristic)
    def is_focus(num_word, entities):
        # If entities are early in sentence, likely subjects
        idx = text_lower.find(num_word)
        if idx < len(text) / 3:  # In first third of sentence
            return True
        # If followed by entity words
        after_text = text_lower[idx:idx+50]
        if any(e in after_text for e in entities):
            return True
        return False
    
    # Rule 3.1-3.4: Check explicit numbers
    
    # Four
    if 'four' in text_lower:
        if any(word in text_lower for word in ['corners', 'creatures', 'winds', 'rings', 'legs']):
            return 'Q', 'L3.4: Four (symbolic/focus)', 'high'
        if is_focus('four', ['men', 'people', 'kings']):
            return 'Q', 'L3.4: Four (focus)', 'high'
        else:
            return 'p', 'L3.6: Four (incidental)', 'medium'
    
    # Three
    if 'three' in text_lower and 'thousand' not in text_lower:
        if is_focus('three', ['men', 'people', 'days', 'sons']):
            return 'T', 'L3.3: Three (focus)', 'high'
        else:
            return 'p', 'L3.6: Three (incidental)', 'medium'
    
    # Two / both
    if 'two' in text_lower or 'both' in text_lower:
        if is_focus('two', ['men', 'people', 'disciples', 'witnesses']) or 'both of' in text_lower:
            return 'D', 'L3.2: Two (focus)', 'high'
        else:
            return 'p', 'L3.6: Two (incidental)', 'medium'
    
    # One
    if any(phrase in text_lower for phrase in [' one ', 'one of', 'a single']):
        if 'no one' not in text_lower and 'someone' not in text_lower and 'everyone' not in text_lower:
            return 'S', 'L3.1: One (focus)', 'high'
    
    # Rule 3.5-3.6: Numbers 5-10, "few"
    for num in ['five', 'six', 'seven', 'eight', 'nine', 'ten']:
        if num in text_lower:
            return 'p', f'L3.5: {num}', 'medium'
    
    if any(phrase in text_lower for phrase in ['a few', 'several', 'some ']):
        return 'p', 'L3.6: Few/several', 'medium'
    
    # Rule 3.7: Indefinite singular
    if any(word in text_lower for word in ['someone', 'anyone', 'whoever', 'no one']):
        return 'S', 'L3.7: Indefinite singular', 'medium'
    
    # LEVEL 4: Named Participants
    # (Would need NER for proper implementation - simplified here)
    
    # Count capitalized words (rough heuristic for names)
    import re
    words = text.split()
    names = [w for i, w in enumerate(words) if w and w[0].isupper() and 
             i > 0 and not words[i-1].endswith('.') and w not in 
             ['The', 'And', 'But', 'So', 'Then', 'Now', 'For', 'To', 'In', 'On', 'At']]
    
    # Filter out common words
    names = [n for n in names if len(n) > 2]
    name_count = len(set(names))
    
    if name_count == 1:
        return 'S', 'L4: One named person', 'medium'
    elif name_count == 2:
        return 'D', 'L4: Two named people', 'medium'
    elif name_count == 3:
        return 'T', 'L4: Three named people', 'medium'
    elif name_count == 4:
        return 'Q', 'L4: Four named people', 'medium'
    elif 5 <= name_count <= 10:
        return 'p', f'L4: {name_count} named people', 'medium'
    elif name_count > 10:
        return 'P', f'L4: {name_count} named people', 'medium'
    
    # LEVEL 5: Pronouns
    
    # Rule 5.2: Dual indicators
    if any(phrase in text_lower for phrase in ['you and me', 'you and i', 'between us', 'the two of them']):
        return 'D', 'L5.2: Dual phrase', 'medium'
    
    # Rule 5.1: Clear singular
    if any(pattern in text_lower for pattern in [' he ', ' she ', ' him ', ' her ']):
        if not any(pattern in text_lower for pattern in [' they ', ' them ', ' their ']):
            return 'S', 'L5.1: Singular pronoun', 'low'
    
    # Rule 5.4: Plural pronouns
    if any(pattern in text_lower for pattern in [' they ', ' them ', ' their ', 'those who']):
        # Check if it's a small group context
        if any(word in text_lower for word in ['few', 'small', 'band']):
            return 'p', 'L5.3: Small group pronoun', 'low'
        else:
            return 'P', 'L5.4: Plural pronouns', 'low'
    
    # LEVEL 6: Discourse Context
    
    # Rule 6.1: Large groups
    large_groups = ['people', 'nations', 'crowds', 'multitudes', 'households', 'disciples',
                    'brothers and sisters', 'everyone', 'all who']
    if any(group in text_lower for group in large_groups):
        return 'P', 'L6.1: Large indefinite group', 'medium'
    
    # Rule 6.2: Collective nouns (singular)
    if any(word in text_lower for word in ['church', 'nation', 'body', 'family']) and ' the ' in text_lower:
        # Check if used with singular verb (heuristic)
        if ' is ' in text_lower or ' was ' in text_lower or ' has ' in text_lower:
            return 'S', 'L6.2: Collective noun (singular)', 'low'
    
    # LEVEL 7: Default
    return 'P', 'L7: Default plural', 'low'

def main():
    print("=" * 80)
    print("BLIND TESTING - v3 Algorithm on Test Set")
    print("=" * 80)
    print()
    print("🔒 CRITICAL: This script does NOT access test.yaml (answers)")
    print("   Only reading test_questions.yaml (verse references)")
    print()
    
    # Load test questions (verse references ONLY)
    print("Loading test_questions.yaml...")
    with open('test_questions.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    verse_refs = [v['reference'] for v in data['verses']]
    print(f"✅ Loaded {len(verse_refs)} verse references")
    print()
    
    # Generate predictions
    print("Generating predictions (this will take a while - fetching verses)...")
    print()
    
    predictions = []
    stats = defaultdict(int)
    
    for i, ref in enumerate(verse_refs, 1):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(verse_refs)} ({i/len(verse_refs)*100:.1f}%)")
        
        # Fetch verse text
        text = get_verse_text(ref)
        
        if not text:
            pred_value, rule, confidence = 'P', 'L7: No text (default)', 'low'
        else:
            pred_value, rule, confidence = apply_v3_algorithm(text, ref)
        
        predictions.append({
            'reference': ref,
            'predicted_value': pred_value,
            'rule_applied': rule,
            'confidence': confidence
        })
        
        stats[pred_value] += 1
    
    print(f"  Progress: {len(verse_refs)}/{len(verse_refs)} (100.0%)")
    print()
    print("✅ Predictions complete!")
    print()
    
    # Show prediction distribution
    print("Prediction Distribution:")
    print("-" * 40)
    for value in ['S', 'D', 'T', 'Q', 'p', 'P']:
        count = stats[value]
        pct = count / len(predictions) * 100
        print(f"  {value}: {count:4d} ({pct:5.1f}%)")
    print()
    
    # Save predictions
    output_file = 'test_predictions_LOCKED.yaml'
    output = {
        'feature': 'number-systems',
        'algorithm': 'v3',
        'date': '2025-11-19',
        'note': '🔒 LOCKED PREDICTIONS - Generated BEFORE seeing test.yaml',
        'methodology': 'Blind testing - predictions made without access to answers',
        'total_predictions': len(predictions),
        'prediction_stats': dict(stats),
        'predictions': predictions
    }
    
    with open(output_file, 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"✅ Predictions saved to: {output_file}")
    print()
    print("=" * 80)
    print("NEXT STEPS - CRITICAL:")
    print("=" * 80)
    print("1. Review predictions (optional)")
    print("2. git add test_predictions_LOCKED.yaml")
    print("3. git commit -m 'test(tbta): Lock blind predictions for test set'")
    print("4. git push")
    print()
    print("🚨 ONLY AFTER COMMIT can you run scoring script!")
    print("   (This proves predictions were made before seeing answers)")
    print()
    print("5. THEN run: python score_test_predictions.py")
    print("=" * 80)

if __name__ == '__main__':
    main()

