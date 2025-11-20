#!/usr/bin/env python3
"""
Cross-Linguistic Analysis - Find the ground truth from target languages.

This script:
1. Fetches translations in languages that grammatically mark number distinctions
2. Analyzes what forms they use (dual/trial/plural pronouns)
3. Compares across languages to find agreement/disagreement
4. Validates against TBTA values
5. Reports which languages are available and what they show

Target languages (from TRANSLATION-DATABASE.md):
- Fijian (fij): Has dual + trial (obligatory)
- Hawaiian (haw): Has dual + trial (obligatory)
- Samoan (smo): Has dual (obligatory)
- Slovenian (slv): Has obligatory dual
- Tok Pisin (tpi): Has trial marking
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(PROJECT_ROOT / '.claude' / 'skills' / 'quote-bible' / 'scripts'))
sys.path.insert(0, str(PROJECT_ROOT))

from fetch_verse import fetch_verse, filter_by_languages


def main():
    print("=" * 80)
    print("CROSS-LINGUISTIC ANALYSIS - The Ground Truth")
    print("=" * 80)
    print()
    print("Fetching translations in languages with number marking:")
    print("  - Fijian (fij): dual + trial")
    print("  - Hawaiian (haw): dual + trial")
    print("  - Samoan (smo): dual")
    print("  - Slovenian (slv): dual")
    print("  - Tok Pisin (tpi): trial")
    print()
    
    # Load test predictions and actuals
    with open('test_predictions_LOCKED.yaml', 'r') as f:
        pred_data = yaml.safe_load(f)
    
    predictions = {p['reference']: p for p in pred_data['predictions']}
    
    with open('test.yaml', 'r') as f:
        test_data = yaml.safe_load(f)
    
    # Build actuals map
    actuals = {}
    value_map = {'Singular': 'S', 'Dual': 'D', 'Trial': 'T', 'Quadrial': 'Q', 'Paucal': 'p', 'Plural': 'P'}
    for category in test_data['value']:
        true_value = value_map[category['specific_value']]
        for verse in category['verses']:
            actuals[verse['reference']] = true_value
    
    # Target languages
    target_langs = ['fij', 'haw', 'smo', 'slv', 'tpi']
    
    # Also get English for comparison
    all_langs = target_langs + ['eng']
    
    # Analysis results
    results = []
    lang_availability = defaultdict(int)
    
    print("Fetching translations for sample verses...")
    print()
    
    # Process first 20 verses from our predictions
    sample_refs = list(predictions.keys())[:20]
    
    for i, ref in enumerate(sample_refs, 1):
        print(f"[{i}/20] {ref}")
        
        book, chapter, verse = ref.split('.')
        chapter, verse = int(chapter), int(verse)
        
        try:
            # Fetch all translations
            all_translations = fetch_verse(book, chapter, verse)
            
            # Filter to our target languages + English
            translations = filter_by_languages(all_translations, all_langs)
            
            # Track which languages are available
            available_langs = []
            for lang in target_langs:
                lang_versions = {k: v for k, v in translations.items() if k.startswith(f'{lang}-')}
                if lang_versions:
                    available_langs.append(lang)
                    lang_availability[lang] += 1
            
            # Get English for reference
            eng_text = None
            for k, v in translations.items():
                if k.startswith('eng-'):
                    eng_text = v
                    break
            
            # Record results
            result = {
                'reference': ref,
                'tbta_value': actuals.get(ref, '?'),
                'predicted_value': predictions[ref]['predicted_value'],
                'english_text': eng_text[:100] + "..." if eng_text and len(eng_text) > 100 else eng_text,
                'available_languages': available_langs,
                'translations': {}
            }
            
            # Store first translation for each language
            for lang in available_langs:
                for k, v in translations.items():
                    if k.startswith(f'{lang}-'):
                        result['translations'][lang] = v[:150] + "..." if len(v) > 150 else v
                        break
            
            results.append(result)
            
        except Exception as e:
            print(f"  Error: {e}")
    
    print()
    print("=" * 80)
    print("LANGUAGE AVAILABILITY")
    print("=" * 80)
    for lang in target_langs:
        count = lang_availability[lang]
        pct = (count / len(sample_refs) * 100) if sample_refs else 0
        print(f"  {lang}: {count}/{len(sample_refs)} ({pct:.1f}%)")
    
    print()
    print("=" * 80)
    print("CROSS-LINGUISTIC EVIDENCE")
    print("=" * 80)
    print()
    
    # Save detailed results
    output = {
        'analysis': 'cross-linguistic-validation',
        'target_languages': target_langs,
        'sample_size': len(sample_refs),
        'language_availability': dict(lang_availability),
        'results': results
    }
    
    with open('cross_linguistic_analysis.yaml', 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"✅ Detailed results saved to: cross_linguistic_analysis.yaml")
    print()
    
    # Show examples where we have target language translations
    print("EXAMPLES WITH TARGET LANGUAGE TRANSLATIONS:")
    print("=" * 80)
    
    for result in results[:10]:
        if result['available_languages']:
            print(f"\n{result['reference']}:")
            print(f"  TBTA Value: {result['tbta_value']}")
            print(f"  Predicted: {result['predicted_value']}")
            print(f"  English: {result['english_text']}")
            print(f"  Available in: {', '.join(result['available_languages'])}")
            for lang, text in result['translations'].items():
                print(f"    {lang}: {text}")
    
    print()
    print("=" * 80)
    print("NEXT STEP: Linguistic Analysis")
    print("=" * 80)
    print("Now we need to:")
    print("1. Analyze pronoun forms in Fijian/Hawaiian/Samoan")
    print("2. Identify dual markers (rau, kāua, etc.)")
    print("3. Identify trial markers (ratou, kākou, etc.)")
    print("4. Compare with TBTA values")
    print("5. Report agreement/disagreement")
    print()

if __name__ == '__main__':
    main()

