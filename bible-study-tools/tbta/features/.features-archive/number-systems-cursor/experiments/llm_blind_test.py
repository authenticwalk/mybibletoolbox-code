#!/usr/bin/env python3
"""
LLM-Based Blind Testing - Apply v3 PROMPT.md naturally using LLM pattern recognition.

This script:
1. Fetches verse texts
2. Saves them to a file for LLM batch processing  
3. LLM (Claude) applies v3 PROMPT.md algorithm naturally
4. Generates predictions based on pattern recognition (not hard-coded rules)

This is the PROPER way - testing if PROMPT.md is clear enough for an LLM to follow.
"""

import yaml
import sys
import json
import random
from pathlib import Path

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(PROJECT_ROOT / '.claude' / 'skills' / 'quote-bible' / 'scripts'))
sys.path.insert(0, str(PROJECT_ROOT))

from fetch_verse import fetch_verse

def main():
    print("=" * 80)
    print("LLM-BASED BLIND TESTING - v3 Algorithm")
    print("=" * 80)
    print()
    print("This script prepares verses for LLM prediction using v3 PROMPT.md")
    print("The LLM will apply the algorithm naturally (pattern recognition)")
    print("NOT using hard-coded rules (that was wrong!)")
    print()
    
    # Load test questions
    with open('test_questions.yaml', 'r') as f:
        data = yaml.safe_load(f)
    
    verse_refs = [v['reference'] for v in data['verses']]
    
    # Sample 50 verses (manageable for LLM batch processing)
    random.seed(42)
    sample = random.sample(verse_refs, 50)
    
    print(f"Total test verses: {len(verse_refs)}")
    print(f"Sample size: {len(sample)}")
    print()
    
    # Fetch verse texts
    print("Fetching verse texts...")
    verses_with_text = []
    
    for i, ref in enumerate(sample, 1):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(sample)}")
        
        book, chapter, verse = ref.split('.')
        chapter, verse = int(chapter), int(verse)
        
        try:
            translations = fetch_verse(book, chapter, verse)
            # Prefer NIV, ESV, NASB
            text = None
            for pref in ['eng-NIV', 'eng-ESV', 'eng-NASB']:
                if pref in translations:
                    text = translations[pref]
                    break
            if not text:
                for k, v in translations.items():
                    if k.startswith('eng-'):
                        text = v
                        break
            
            if text:
                verses_with_text.append({
                    'reference': ref,
                    'text': text
                })
        except Exception as e:
            print(f"  Warning: Failed to fetch {ref}: {e}")
    
    print(f"  Progress: {len(sample)}/{len(sample)}")
    print(f"✅ Fetched {len(verses_with_text)} verses successfully")
    print()
    
    # Save for LLM processing
    output = {
        'feature': 'number-systems',
        'algorithm': 'v3',
        'note': 'Verses prepared for LLM blind testing',
        'instruction': 'Apply prompts/v3/PROMPT.md to each verse naturally',
        'methodology': 'LLM pattern recognition, not hard-coded rules',
        'total_verses': len(verses_with_text),
        'verses': verses_with_text
    }
    
    with open('verses_for_llm_prediction.yaml', 'w') as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"✅ Verses saved to: verses_for_llm_prediction.yaml")
    print()
    print("=" * 80)
    print("NEXT STEP:")
    print("=" * 80)
    print("LLM (Claude) will now apply v3 PROMPT.md to each verse naturally.")
    print("This tests if the algorithm is clear enough for LLM pattern recognition.")
    print()
    print("Process:")
    print("1. LLM reads v3 PROMPT.md (algorithm)")
    print("2. For each verse, LLM applies algorithm using pattern recognition")
    print("3. Generates predictions naturally (not hard-coded rules)")
    print("4. Saves predictions to test_predictions_LOCKED.yaml")
    print("5. Git commit (lock) before seeing test.yaml")
    print("=" * 80)

if __name__ == '__main__':
    main()

