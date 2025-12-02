#!/usr/bin/env python3
"""Extract parallel examples showing He1 vs He2 style differences"""

import csv
import re

def load_verses(filepath):
    """Load all verses from CSV"""
    verses = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            verses.append({
                'id': row['ID'],
                'ref': row['Reference'],
                'text': row['Verse']
            })
    return verses

# Load data
ruth = load_verses('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data/Ruth.csv')
matthew = load_verses('/home/user/mybibletoolbox-code/plan/tbta/phase1-reverse-engineer/data/Matthew.csv')

print("="*80)
print("PARALLEL EXAMPLES: He1 (Ruth/OT) vs He2 (Matthew/NT)")
print("="*80)

# Example 1: Underscore annotations (MAJOR DIFFERENCE)
print("\n" + "="*80)
print("EXAMPLE 1: UNDERSCORE ANNOTATIONS (_implicit, _implicitActiveAgent, etc.)")
print("="*80)
print("\nHe1 (Ruth) - NO underscore annotations:")
print(f"\n  {ruth[0]['ref']}")
print(f"  {ruth[0]['text']}")
print(f"\n  {ruth[5]['ref']}")
print(f"  {ruth[5]['text']}")

print("\nHe2 (Matthew) - EXTENSIVE underscore annotations:")
matthew_implicit = [v for v in matthew if '_implicit' in v['text']][:3]
for v in matthew_implicit:
    print(f"\n  {v['ref']}")
    # Highlight underscore annotations
    text = v['text']
    parts = re.split(r'(_[a-zA-Z\-]+)', text)
    highlighted = ''
    for i, part in enumerate(parts):
        if part.startswith('_'):
            highlighted += f"**{part}**"
        else:
            highlighted += part
    print(f"  {highlighted}")

# Example 2: Pronoun handling
print("\n" + "="*80)
print("EXAMPLE 2: PRONOUN HANDLING (Natural vs Strict)")
print("="*80)

# Ruth - more natural, repetitive pronoun references
ruth_pronouns = [ruth[8], ruth[11]]  # Naomi examples
print("\nHe1 (Ruth) - More natural, accepts repetition:")
for v in ruth_pronouns:
    print(f"\n  {v['ref']}")
    print(f"  {v['text'][:200]}...")
    # Count pronoun repetitions
    pronouns = re.findall(r'\(([^)]+)\)', v['text'])
    print(f"  [Pronoun refs: {', '.join(pronouns[:10])}...]")

# Matthew - stricter, more varied
matthew_pronouns = [v for v in matthew if v['id'] in ['140', '141', '143']]  # Sermon examples
print("\nHe2 (Matthew) - Stricter, more explicit markers:")
for v in matthew_pronouns[:2]:
    print(f"\n  {v['ref']}")
    print(f"  {v['text'][:200]}...")
    # Count pronoun annotations
    pronouns = re.findall(r'\(([^)]+)\)', v['text'])
    print(f"  [Pronoun refs: {', '.join(pronouns[:10])}...]")

# Example 3: Clause bracketing
print("\n" + "="*80)
print("EXAMPLE 3: CLAUSE SEGMENTATION (Bracket usage)")
print("="*80)

print("\nHe1 (Ruth) - Moderate bracketing:")
ruth_brackets = [v for v in ruth if v['text'].count('[') >= 6][:2]
for v in ruth_brackets:
    print(f"\n  {v['ref']} [{v['text'].count('[')} brackets]")
    print(f"  {v['text'][:200]}...")

print("\nHe2 (Matthew) - Similar but with more annotations:")
matthew_brackets = [v for v in matthew if v['text'].count('[') >= 6][:2]
for v in matthew_brackets:
    print(f"\n  {v['ref']} [{v['text'].count('[')} brackets]")
    print(f"  {v['text'][:200]}...")

# Example 4: Vocabulary complexity
print("\n" + "="*80)
print("EXAMPLE 4: VOCABULARY & COMPLEXITY")
print("="*80)

print("\nHe1 (Ruth) - Simpler, more conversational:")
print(f"\n  {ruth[3]['ref']}")
print(f"  {ruth[3]['text']}")
print(f"\n  {ruth[14]['ref']}")
print(f"  {ruth[14]['text']}")

print("\nHe2 (Matthew) - More complex markers and labels:")
matthew_complex = [v for v in matthew if '(title)' in v['text'] or '(paragraph)' in v['text']][:2]
for v in matthew_complex:
    print(f"\n  {v['ref']}")
    print(f"  {v['text'][:300]}...")

# Example 5: Agent specification
print("\n" + "="*80)
print("EXAMPLE 5: AGENT SPECIFICATION")
print("="*80)

print("\nHe1 (Ruth) - Implicit agents accepted:")
print(f"\n  {ruth[16]['ref']}")
print(f"  {ruth[16]['text']}")

print("\nHe2 (Matthew) - Explicit agent markers:")
matthew_agents = [v for v in matthew if '_implicitActiveAgent' in v['text']][:3]
for v in matthew_agents:
    print(f"\n  {v['ref']}")
    # Highlight agent markers
    text = re.sub(r'(_implicitActiveAgent)', r'**\1**', v['text'])
    print(f"  {text[:250]}...")

print("\n" + "="*80)
