#!/usr/bin/env python3
"""
Detect Number Marking - Extract grammatical number from target languages.

This analyzes Hawaiian and Tok Pisin translations to detect dual/trial marking.
"""

import yaml
import sys
import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(PROJECT_ROOT))

from src.ingest_data.ebible.ebible_fetcher import fetch_verses_from_ebible

# Tok Pisin number markers (VERY EXPLICIT!)
TOK_PISIN_MARKERS = {
    'tupela': 'D',  # two-pela = Dual
    'tripela': 'T',  # three-pela = Trial
    'fopela': 'Q',   # four-pela = Quadrial
    'faivpela': 'p', # five-pela = Paucal
    'sikispela': 'p', # six-pela = Paucal
    'sevenpela': 'p', # seven-pela = Paucal
}

# Hawaiian dual/trial pronouns
HAWAIIAN_DUAL_PRONOUNS = [
    'kāua', 'māua',  # we-2 (inclusive/exclusive)
    'ʻolua', 'olua',  # you-2
    'lāua', 'laua',   # they-2
]

HAWAIIAN_TRIAL_PRONOUNS = [
    'kākou', 'kakou', 'mākou', 'makou',  # we-3
    'ʻoukou', 'oukou',  # you-3
    'lākou', 'lakou',   # they-3
]

def detect_tok_pisin_number(text):
    """Detect number marking in Tok Pisin text."""
    text_lower = text.lower()
    
    for marker, value in TOK_PISIN_MARKERS.items():
        if marker in text_lower:
            return value, f'tok_pisin_{marker}'
    
    return None, None

def detect_hawaiian_number(text):
    """Detect number marking in Hawaiian text."""
    text_lower = text.lower()
    
    # Check for dual pronouns
    for pronoun in HAWAIIAN_DUAL_PRONOUNS:
        if pronoun.lower() in text_lower:
            return 'D', f'hawaiian_{pronoun}'
    
    # Check for trial pronouns
    for pronoun in HAWAIIAN_TRIAL_PRONOUNS:
        if pronoun.lower() in text_lower:
            return 'T', f'hawaiian_{pronoun}'
    
    return None, None

def analyze_verse(book, chapter, verse, tbta_value):
    """Analyze a single verse across languages."""
    try:
        result = fetch_verses_from_ebible(book, chapter, verse)
        
        if not result or 'translations' not in result:
            return None
        
        translations = result['translations']
        
        # Get translations
        eng = next((v for k, v in translations.items() if k.startswith('eng-')), None)
        haw = next((v for k, v in translations.items() if k.startswith('haw-')), None)
        tpi = next((v for k, v in translations.items() if k.startswith('tpi-')), None)
        heb = next((v for k, v in translations.items() if k.startswith('heb-')), None)
        
        # Detect number marking
        evidence = {}
        
        if tpi:
            number, marker = detect_tok_pisin_number(tpi)
            if number:
                evidence['tok_pisin'] = {'value': number, 'marker': marker, 'text': tpi[:100]}
        
        if haw:
            number, marker = detect_hawaiian_number(haw)
            if number:
                evidence['hawaiian'] = {'value': number, 'marker': marker, 'text': haw[:100]}
        
        return {
            'reference': f'{book}.{chapter:03d}.{verse:03d}',
            'tbta_value': tbta_value,
            'english': eng[:100] if eng else None,
            'available': {
                'hawaiian': haw is not None,
                'tok_pisin': tpi is not None,
                'hebrew': heb is not None,
            },
            'evidence': evidence,
        }
        
    except Exception as e:
        print(f"Error processing {book}.{chapter}.{verse}: {e}")
        return None

def main():
    print("=" * 80)
    print("CROSS-LINGUISTIC NUMBER MARKING DETECTION")
    print("=" * 80)
    print()
    
    # Load TBTA values
    with open('test.yaml', 'r') as f:
        test_data = yaml.safe_load(f)
    
    value_map = {'Singular': 'S', 'Dual': 'D', 'Trial': 'T', 'Quadrial': 'Q', 'Paucal': 'p', 'Plural': 'P'}
    
    # Get sample from each category
    sample_verses = []
    for category in test_data['value']:
        tbta_value = value_map[category['specific_value']]
        # Take first 5 from each category
        for verse_info in category['verses'][:5]:
            ref = verse_info['reference']
            book, ch, vs = ref.split('.')
            sample_verses.append((book, int(ch), int(vs), tbta_value))
    
    print(f"Analyzing {len(sample_verses)} verses across all categories...")
    print()
    
    # Analyze
    results = []
    agreement_stats = defaultdict(int)
    disagreement_cases = []
    
    for i, (book, ch, vs, tbta_value) in enumerate(sample_verses, 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(sample_verses)}")
        
        analysis = analyze_verse(book, ch, vs, tbta_value)
        if analysis and analysis['evidence']:
            results.append(analysis)
            
            # Check agreement
            detected_values = [ev['value'] for ev in analysis['evidence'].values()]
            if detected_values:
                if all(v == tbta_value for v in detected_values):
                    agreement_stats['agree'] += 1
                else:
                    agreement_stats['disagree'] += 1
                    disagreement_cases.append(analysis)
    
    print(f"  Progress: {len(sample_verses)}/{len(sample_verses)}")
    print()
    
    # Report
    print("=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"Verses with detectable marking: {len(results)}")
    print(f"Agreement with TBTA: {agreement_stats['agree']}")
    print(f"Disagreement with TBTA: {agreement_stats['disagree']}")
    print()
    
    # Show examples
    print("=" * 80)
    print("EXAMPLES OF DETECTED MARKING")
    print("=" * 80)
    
    for result in results[:10]:
        print(f"\n{result['reference']} - TBTA: {result['tbta_value']}")
        print(f"English: {result['english']}")
        for lang, ev in result['evidence'].items():
            agree = '✅' if ev['value'] == result['tbta_value'] else '❌'
            print(f"{agree} {lang}: {ev['value']} (marker: {ev['marker']})")
            print(f"   {ev['text']}...")
    
    if disagreement_cases:
        print()
        print("=" * 80)
        print(f"DISAGREEMENTS ({len(disagreement_cases)} cases)")
        print("=" * 80)
        
        for case in disagreement_cases[:5]:
            print(f"\n{case['reference']} - TBTA says: {case['tbta_value']}")
            print(f"English: {case['english']}")
            for lang, ev in case['evidence'].items():
                print(f"  {lang} says: {ev['value']} (marker: {ev['marker']})")
                print(f"   {ev['text']}...")
    
    # Save
    output = {
        'analysis': 'cross-linguistic-number-marking',
        'total_analyzed': len(sample_verses),
        'with_evidence': len(results),
        'agreement': dict(agreement_stats),
        'results': results,
        'disagreements': disagreement_cases,
    }
    
    with open('number_marking_analysis.yaml', 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print()
    print(f"\n✅ Full analysis saved to: number_marking_analysis.yaml")
    print()
    print("=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)
    print("""
Tok Pisin is EXPLICIT:
  - tupela = TWO (dual)
  - tripela = THREE (trial) 
  - Grammatically required marking!

Hawaiian uses pronouns:
  - lāua/laua = they-2 (dual)
  - kākou/kakou = we-3 (trial)
  - Grammatically required forms!

These languages are telling us the GROUND TRUTH!
""")

if __name__ == '__main__':
    main()

