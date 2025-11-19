#!/usr/bin/env python3
"""
Apply PROMPT.md v1 algorithm to training data and measure accuracy.

This script:
1. Loads train.yaml
2. Applies the v1 classification rules
3. Compares predictions with actual TBTA values
4. Generates accuracy report and error analysis
"""

import yaml
import sys
import re
from pathlib import Path
from collections import defaultdict

# Add fetch_verse to path
PROJECT_ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(PROJECT_ROOT / '.claude' / 'skills' / 'quote-bible' / 'scripts'))

try:
    from fetch_verse import fetch_verse
except ImportError:
    print("Warning: fetch_verse not available. Using cached data only.", file=sys.stderr)
    def fetch_verse(book, chapter, verse):
        """Fallback that returns empty dict."""
        return {}

def parse_verse_ref(ref):
    """Parse USFM reference like 'GEN.001.026' into book, chapter, verse."""
    parts = ref.split('.')
    return parts[0], int(parts[1]), int(parts[2])

def get_verse_text(ref):
    """Fetch English text for verse reference."""
    book, chapter, verse = parse_verse_ref(ref)
    try:
        translations = fetch_verse(book, chapter, verse)
        # Get first English version
        for version, text in translations.items():
            if version.startswith('eng-'):
                return text
    except Exception as e:
        print(f"  Warning: Could not fetch {ref}: {e}", file=sys.stderr)
    return ""

def classify_verse(text, ref):
    """
    Apply PROMPT.md v1 algorithm to classify verse.
    
    Returns: (predicted_value, rule_applied, confidence)
    """
    text_lower = text.lower()
    
    # LEVEL 1: Explicit Cardinal Numbers
    
    # Rule 1.6: "Few", "Several", "Some"
    if re.search(r'\b(a few|several|some)\b', text_lower):
        if any(word in text_lower for word in ['fish', 'loaves', 'men', 'people', 'days']):
            return ('p', 'L1.6: Few/Several/Some', 'high')
    
    # Rule 1.5: Numbers 5-10
    for num_word, num_val in [('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10)]:
        if num_word in text_lower:
            return ('p', f'L1.5: {num_word}', 'high')
    
    # Rule 1.4: Cardinal "Four"
    if 'four' in text_lower:
        return ('Q', 'L1.4: four', 'high')
    
    # Rule 1.3: Cardinal "Three"
    if 'three' in text_lower:
        return ('T', 'L1.3: three', 'high')
    
    # Rule 1.2: Cardinal "Two"
    if any(word in text_lower for word in ['two', 'both', 'pair']):
        return ('D', 'L1.2: two/both/pair', 'high')
    
    # Rule 1.1: Cardinal "One"
    if re.search(r'\b(one|a single|alone)\b', text_lower):
        # Check it's not "no one" or "anyone"
        if not re.search(r'\b(no one|anyone|someone|everyone)\b', text_lower):
            return ('S', 'L1.1: one/single/alone', 'high')
    
    # LEVEL 2: Natural Pairs
    
    # Rule 2.1: Body part pairs
    body_pairs = ['hands', 'eyes', 'feet', 'ears', 'arms', 'legs', 'cheeks', 'shoulders']
    if any(pair in text_lower for pair in body_pairs):
        return ('D', f'L2.1: natural pair', 'high')
    
    # LEVEL 3: Theological Contexts
    
    # Rule 3.1: Divine first-person plural (Trinity)
    if re.search(r'let us (make|go|create)', text_lower):
        # Check for creation or judgment context
        if any(word in text_lower for word in ['make', 'create', 'image', 'confuse', 'go down']):
            return ('T', 'L3.1: divine plural (Trinity)', 'high')
    
    # Rule 3.2: Explicit Trinity formula
    if re.search(r'father.*son.*spirit|father.*son.*holy spirit', text_lower):
        return ('T', 'L3.2: Trinity formula', 'high')
    
    # Rule 3.3: Monotheism emphasis
    if re.search(r'(the lord.*is one|one god|god alone)', text_lower):
        return ('S', 'L3.3: monotheism', 'high')
    
    # LEVEL 4: Named Individuals
    
    # Count proper names (capitalized words not at sentence start)
    # This is a simplified heuristic
    words = text.split()
    proper_names = []
    for i, word in enumerate(words):
        # Skip first word (sentence start)
        if i == 0:
            continue
        # Skip if after period (new sentence)
        if i > 0 and words[i-1].endswith('.'):
            continue
        # Check if capitalized (proper name heuristic)
        if word and word[0].isupper() and not word.isupper():
            # Remove punctuation
            clean_word = re.sub(r'[^\w]', '', word)
            if clean_word and len(clean_word) > 1:
                proper_names.append(clean_word)
    
    name_count = len(set(proper_names))  # Unique names
    if name_count == 1:
        return ('S', 'L4.1: one named person', 'medium')
    elif name_count == 2:
        return ('D', 'L4.2: two named people', 'medium')
    elif name_count == 3:
        return ('T', 'L4.3: three named people', 'medium')
    elif name_count == 4:
        return ('Q', 'L4.4: four named people', 'medium')
    elif name_count >= 5:
        if name_count <= 10:
            return ('p', f'L4.5: {name_count} named people', 'medium')
        else:
            return ('P', f'L4.5: {name_count} named people', 'medium')
    
    # LEVEL 5: Grammatical Cues
    
    # Rule 5.2: Dual implications
    if any(phrase in text_lower for phrase in ['you and me', 'you and i', 'between you and me', 'between us', 'the two of them', 'they both']):
        return ('D', 'L5.2: dual implication', 'medium')
    
    # Rule 5.1: Singular pronouns (as main reference)
    # Very weak signal - only if no other plurals present
    singular_pattern = r'\b(he|she|it)\s+(said|went|was|did)'
    plural_pattern = r'\b(they|them|their)\b'
    if re.search(singular_pattern, text_lower) and not re.search(plural_pattern, text_lower):
        return ('S', 'L5.1: singular pronoun', 'low')
    
    # Rule 5.3: Plural pronouns
    if re.search(plural_pattern, text_lower):
        return ('P', 'L5.3: plural pronouns', 'low')
    
    # LEVEL 6: Context
    
    # Rule 6.2: Large indefinite groups
    large_groups = ['people', 'nations', 'crowds', 'household', 'households', 'brothers and sisters', 
                    'disciples', 'apostles', 'those who', 'everyone', 'whoever', 'all who']
    if any(group in text_lower for group in large_groups):
        return ('P', 'L6.2: large group', 'medium')
    
    # Rule 6.1: Small groups
    if any(phrase in text_lower for phrase in ['all those with', 'his men', 'the company']):
        return ('p', 'L6.1: small group', 'low')
    
    # LEVEL 7: Default
    return ('P', 'L7.1: default plural', 'low')

def main():
    # Load training data
    train_file = Path(__file__).parent.parent.parent / 'train.yaml'
    with open(train_file, 'r') as f:
        train_data = yaml.safe_load(f)
    
    print("=" * 80)
    print("NUMBER SYSTEMS ALGORITHM v1 - TRAINING SET EVALUATION")
    print("=" * 80)
    print()
    
    # Track statistics
    total_verses = 0
    correct_predictions = 0
    predictions_by_value = defaultdict(lambda: {'total': 0, 'correct': 0})
    errors = []
    
    # Process each category
    for category in train_data['value']:
        true_value = category['specific_value']
        # Map to TBTA codes
        value_map = {
            'Singular': 'S',
            'Dual': 'D',
            'Trial': 'T',
            'Quadrial': 'Q',
            'Paucal': 'p',
            'Plural': 'P'
        }
        true_code = value_map.get(true_value, '?')
        
        for verse_info in category['verses']:
            ref = verse_info['reference']
            total_verses += 1
            predictions_by_value[true_code]['total'] += 1
            
            # Fetch verse text
            text = get_verse_text(ref)
            if not text:
                print(f"[SKIP] {ref}: No text available")
                continue
            
            # Classify
            pred_code, rule, confidence = classify_verse(text, ref)
            
            # Check if correct
            is_correct = (pred_code == true_code)
            if is_correct:
                correct_predictions += 1
                predictions_by_value[true_code]['correct'] += 1
            else:
                errors.append({
                    'ref': ref,
                    'text': text[:80] + "..." if len(text) > 80 else text,
                    'true': true_code,
                    'predicted': pred_code,
                    'rule': rule,
                    'confidence': confidence
                })
            
            # Progress indicator
            if total_verses % 50 == 0:
                print(f"Processed {total_verses} verses...", file=sys.stderr)
    
    # Calculate overall accuracy
    overall_accuracy = (correct_predictions / total_verses * 100) if total_verses > 0 else 0
    
    print("\n" + "=" * 80)
    print("OVERALL RESULTS")
    print("=" * 80)
    print(f"Total Verses:      {total_verses}")
    print(f"Correct:           {correct_predictions}")
    print(f"Incorrect:         {total_verses - correct_predictions}")
    print(f"Overall Accuracy:  {overall_accuracy:.1f}%")
    print()
    
    # Per-category breakdown
    print("=" * 80)
    print("PER-CATEGORY ACCURACY")
    print("=" * 80)
    print(f"{'Value':<10} {'Total':<8} {'Correct':<10} {'Accuracy':<10}")
    print("-" * 80)
    
    for value in ['S', 'D', 'T', 'Q', 'p', 'P']:
        stats = predictions_by_value[value]
        if stats['total'] > 0:
            acc = (stats['correct'] / stats['total'] * 100)
            print(f"{value:<10} {stats['total']:<8} {stats['correct']:<10} {acc:.1f}%")
    print()
    
    # Error analysis
    print("=" * 80)
    print(f"ERROR ANALYSIS ({len(errors)} errors)")
    print("=" * 80)
    print()
    
    # Group errors by pattern
    error_patterns = defaultdict(list)
    for error in errors:
        pattern = f"{error['true']} misclassified as {error['predicted']}"
        error_patterns[pattern].append(error)
    
    # Show most common error patterns
    print("Most Common Error Patterns:")
    print()
    sorted_patterns = sorted(error_patterns.items(), key=lambda x: len(x[1]), reverse=True)
    
    for pattern, pattern_errors in sorted_patterns[:10]:  # Top 10 patterns
        print(f"\n{pattern} ({len(pattern_errors)} occurrences):")
        print("-" * 60)
        
        # Show first 3 examples
        for error in pattern_errors[:3]:
            print(f"  {error['ref']}")
            print(f"    Text: {error['text']}")
            print(f"    Rule: {error['rule']} (confidence: {error['confidence']})")
            print()
    
    # Save detailed errors to file
    error_file = Path(__file__).parent / 'errors_v1.yaml'
    with open(error_file, 'w') as f:
        yaml.dump({
            'version': 'v1',
            'total_errors': len(errors),
            'overall_accuracy': f"{overall_accuracy:.1f}%",
            'errors': errors
        }, f, default_flow_style=False, allow_unicode=True)
    
    print(f"\nDetailed errors saved to: {error_file}")
    
    # Write summary
    summary_file = Path(__file__).parent / 'RESULTS.md'
    with open(summary_file, 'w') as f:
        f.write(f"# Algorithm v1 - Training Set Results\n\n")
        f.write(f"**Date**: 2025-11-19\n")
        f.write(f"**Dataset**: train.yaml ({total_verses} verses)\n\n")
        f.write(f"## Overall Performance\n\n")
        f.write(f"- **Accuracy**: {overall_accuracy:.1f}%\n")
        f.write(f"- **Correct**: {correct_predictions}/{total_verses}\n")
        f.write(f"- **Errors**: {len(errors)}\n\n")
        f.write(f"## Per-Category Accuracy\n\n")
        f.write(f"| Value | Total | Correct | Accuracy |\n")
        f.write(f"|-------|-------|---------|----------|\n")
        for value in ['S', 'D', 'T', 'Q', 'p', 'P']:
            stats = predictions_by_value[value]
            if stats['total'] > 0:
                acc = (stats['correct'] / stats['total'] * 100)
                f.write(f"| {value} | {stats['total']} | {stats['correct']} | {acc:.1f}% |\n")
        f.write(f"\n## Error Patterns\n\n")
        for pattern, pattern_errors in sorted_patterns[:5]:
            f.write(f"### {pattern} ({len(pattern_errors)} errors)\n\n")
            for error in pattern_errors[:3]:
                f.write(f"- **{error['ref']}**: {error['text']}\n")
                f.write(f"  - Predicted: {error['predicted']} (Rule: {error['rule']})\n\n")
    
    print(f"Summary saved to: {summary_file}")
    
    print()
    print("=" * 80)
    if overall_accuracy >= 95:
        print("✅ TRAINING ACCURACY ≥95% - Ready for refinement or testing")
    else:
        print("⚠️  TRAINING ACCURACY <95% - Needs refinement")
    print("=" * 80)

if __name__ == '__main__':
    main()

