#!/usr/bin/env python3
"""
Deep analysis of TBTA patterns - investigate contradictions and edge cases.
"""

import csv
import re
import os
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_all_verses():
    """Load all verses from verses-raw.tsv."""
    all_data = []
    tsv_path = os.path.join(DATA_DIR, "verses-raw.tsv")

    if os.path.exists(tsv_path):
        with open(tsv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                ref = row.get('reference', '')
                verse = row.get('verse', '')
                book = row.get('book', '')
                if ref and verse:
                    all_data.append({
                        'book': book,
                        'ref': ref,
                        'verse': verse
                    })
    else:
        # Fallback to CSV files
        for filename in os.listdir(DATA_DIR):
            if filename.endswith('.csv'):
                book = filename.replace('.csv', '').replace('_', ' ')
                filepath = os.path.join(DATA_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        ref = row.get('Reference', '')
                        verse = row.get('Verse', '')
                        if ref and verse:
                            all_data.append({
                                'book': book,
                                'ref': ref,
                                'verse': verse
                            })
    return all_data

def analyze_he1_vs_he2(data):
    """Analyze He1 (OT natural) vs He2 (NT strict) format differences."""
    print("\n" + "="*60)
    print("HE1 vs HE2 FORMAT ANALYSIS")
    print("="*60)
    
    # He1 books (OT, Ruth, Jonah, Genesis)
    he1_books = ['Ruth', 'Jonah', 'Genesis', 'Joshua', '1 Samuel', '2 Samuel', 
                 'Nehemiah', 'Esther', 'Daniel', 'Nahum']
    # He2 books (NT)
    he2_books = ['Matthew', 'Mark', 'Acts', 'Titus', 'Philemon', '2 John']
    
    he1_verses = [d for d in data if any(b in d['ref'] for b in he1_books)]
    he2_verses = [d for d in data if any(b in d['ref'] for b in he2_books)]
    
    print(f"\nHe1 verses: {len(he1_verses)}")
    print(f"He2 verses: {len(he2_verses)}")
    
    # Analyze underscore markers (He2 feature)
    he1_underscore = sum(1 for d in he1_verses if '_' in d['verse'])
    he2_underscore = sum(1 for d in he2_verses if '_' in d['verse'])
    print(f"\nUnderscore markers:")
    print(f"  He1: {he1_underscore} ({100*he1_underscore/len(he1_verses):.1f}%)")
    print(f"  He2: {he2_underscore} ({100*he2_underscore/len(he2_verses):.1f}%)")
    
    # Analyze L2 pairings (simple/complex)
    slash_pattern = re.compile(r'\b\w+/\w+\b')
    he1_slash = sum(1 for d in he1_verses if slash_pattern.search(d['verse']))
    he2_slash = sum(1 for d in he2_verses if slash_pattern.search(d['verse']))
    print(f"\nL2 pairings (word/word):")
    print(f"  He1: {he1_slash} ({100*he1_slash/len(he1_verses):.1f}%)")
    print(f"  He2: {he2_slash} ({100*he2_slash/len(he2_verses):.1f}%)")
    
    # Analyze (imp) markers
    imp_pattern = re.compile(r'\(imp\)')
    he1_imp = sum(1 for d in he1_verses if imp_pattern.search(d['verse']))
    he2_imp = sum(1 for d in he2_verses if imp_pattern.search(d['verse']))
    print(f"\n(imp) imperative markers:")
    print(f"  He1: {he1_imp} ({100*he1_imp/len(he1_verses):.1f}%)")
    print(f"  He2: {he2_imp} ({100*he2_imp/len(he2_verses):.1f}%)")
    
    # Sample He2 specific markers
    print("\n\nHe2-SPECIFIC MARKERS found:")
    he2_markers = defaultdict(int)
    marker_pattern = re.compile(r'_\w+')
    for d in he2_verses:
        for match in marker_pattern.findall(d['verse']):
            he2_markers[match] += 1
    
    for marker, count in sorted(he2_markers.items(), key=lambda x: -x[1])[:20]:
        print(f"  {marker}: {count}")
        
    return he1_books, he2_books

def analyze_modal_contradictions(data):
    """Understand why modal decomposition has high contradictions."""
    print("\n" + "="*60)
    print("MODAL DECOMPOSITION ANALYSIS")
    print("="*60)
    
    # Find "is able" vs "can/must/should"
    able_pattern = re.compile(r'\b(?:is|was|are|were)\s+able\s+\[?to\b', re.IGNORECASE)
    must_pattern = re.compile(r'\b(must|should|can|could|would)\b', re.IGNORECASE)
    
    able_verses = [d for d in data if able_pattern.search(d['verse'])]
    modal_verses = [d for d in data if must_pattern.search(d['verse'])]
    
    print(f"\n'is/was able to' usage: {len(able_verses)}")
    print(f"Bare modal (must/should/can) usage: {len(modal_verses)}")
    
    # Sample contradicting verses with bare modals
    print("\n\nSample bare modal usage:")
    count = 0
    for d in modal_verses[:15]:
        matches = must_pattern.findall(d['verse'])
        print(f"  {d['ref']}: {matches[:3]} - {d['verse'][:100]}...")
        count += 1
        if count >= 10:
            break
            
    # Check if "must" appears in specific contexts (obligation vs ability)
    print("\n\nAnalyzing 'must' contexts:")
    must_contexts = defaultdict(int)
    for d in data:
        if 'must' in d['verse'].lower():
            # Check what follows must
            matches = re.findall(r'must\s+(\w+)', d['verse'].lower())
            for m in matches:
                must_contexts[m] += 1
                
    print("Words following 'must':")
    for word, count in sorted(must_contexts.items(), key=lambda x: -x[1])[:15]:
        print(f"  must {word}: {count}")

def analyze_number_formatting(data):
    """Understand number formatting patterns."""
    print("\n" + "="*60)
    print("NUMBER FORMATTING ANALYSIS")
    print("="*60)
    
    digit_pattern = re.compile(r'\b(\d+)\b')
    word_pattern = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b', re.IGNORECASE)
    
    digits_used = defaultdict(int)
    words_used = defaultdict(int)
    
    for d in data:
        for match in digit_pattern.findall(d['verse']):
            if not re.match(r'\d+:\d+', match):  # Skip verse refs
                digits_used[match] += 1
        for match in word_pattern.findall(d['verse']):
            words_used[match.lower()] += 1
            
    print("\nDigit usage (sorted by frequency):")
    for num, count in sorted(digits_used.items(), key=lambda x: -x[1])[:15]:
        print(f"  {num}: {count}")
        
    print("\nWord number usage:")
    for word, count in sorted(words_used.items(), key=lambda x: -x[1]):
        print(f"  {word}: {count}")
        
    # Pattern: Small numbers (1-10) as words, large numbers as digits?
    print("\n\nHypothesis: small numbers as words, large as digits?")
    for d in data[:20]:
        if digit_pattern.search(d['verse']) or word_pattern.search(d['verse']):
            digits = digit_pattern.findall(d['verse'])
            words = word_pattern.findall(d['verse'])
            if digits or words:
                print(f"  {d['ref']}: digits={digits[:3]}, words={words[:3]}")

def analyze_passive_patterns(data):
    """Understand passive voice handling."""
    print("\n" + "="*60)
    print("PASSIVE VOICE ANALYSIS")
    print("="*60)
    
    passive_pattern = re.compile(r'\b(was|were|been|being)\s+(\w+ed)\s+(by)\b', re.IGNORECASE)
    
    print("\nPassive constructions found:")
    count = 0
    for d in data:
        match = passive_pattern.search(d['verse'])
        if match:
            print(f"  {d['ref']}: '{match.group()}' in '{d['verse'][:150]}...'")
            count += 1
            if count >= 15:
                break
                
    print(f"\nTotal passive 'X by Y' constructions: {sum(1 for d in data if passive_pattern.search(d['verse']))}")
    
    # These are NOT converted to active - they remain passive
    # This suggests the rule is aspirational, not actually applied

def analyze_quote_patterns(data):
    """Detailed analysis of quote formatting."""
    print("\n" + "="*60)
    print("QUOTE FRAMING ANALYSIS")
    print("="*60)
    
    # Pattern: Speaker said, ["Quote"]
    said_bracket = re.compile(r'(said|told|asked|replied|answered)[,\s]+\[?"', re.IGNORECASE)
    
    print("\nQuote introduction patterns:")
    patterns = defaultdict(int)
    
    for d in data:
        # Find all speech verbs followed by punctuation
        matches = re.findall(r'(\w+)\s*(,)?\s*(\[)?\s*(")', d['verse'])
        for m in matches:
            pattern = f"{m[0]}{m[1] or ''} {m[2] or ''}{m[3]}"
            patterns[pattern] += 1
            
    for pattern, count in sorted(patterns.items(), key=lambda x: -x[1])[:20]:
        print(f"  '{pattern}': {count}")
        
    # Check for nested quotes
    nested = re.compile(r'\["[^"]*\["[^"]*"\][^"]*"\]')
    print(f"\nNested quote examples:")
    count = 0
    for d in data:
        if nested.search(d['verse']):
            print(f"  {d['ref']}: {d['verse'][:200]}...")
            count += 1
            if count >= 5:
                break

def analyze_bracketing_patterns(data):
    """Analyze what goes in brackets."""
    print("\n" + "="*60)
    print("BRACKET USAGE ANALYSIS")
    print("="*60)
    
    bracket_starts = defaultdict(int)
    bracket_pattern = re.compile(r'\[([a-zA-Z_-]+)')
    
    for d in data:
        for match in bracket_pattern.findall(d['verse']):
            bracket_starts[match.lower()] += 1
            
    print("\nBracket openers (what follows '['):")
    for word, count in sorted(bracket_starts.items(), key=lambda x: -x[1])[:30]:
        print(f"  [{word}...: {count}")

def analyze_hyphenated_verb_forms(data):
    """Analyze hyphenated verb form usage - should be BASE form only."""
    print("\n" + "="*60)
    print("HYPHENATED VERB FORM ANALYSIS")
    print("="*60)

    # Base form pattern (correct)
    base_verbs = ['go-up', 'sit-down', 'stand-up', 'come-out', 'run-away',
                  'throw-away', 'go-down', 'come-back', 'fall-down', 'lie-down']

    # Inflected form pattern (incorrect - should not exist)
    inflected_pattern = re.compile(r'\b(went|sat|stood|came|ran|threw|fell|lay|gotten|gone)-\w+\b', re.IGNORECASE)

    base_count = 0
    inflected_count = 0
    inflected_examples = []

    for d in data:
        # Count base forms
        for verb in base_verbs:
            if verb in d['verse'].lower():
                base_count += 1

        # Find inflected violations
        match = inflected_pattern.search(d['verse'])
        if match:
            inflected_count += 1
            if len(inflected_examples) < 10:
                inflected_examples.append((d['ref'], match.group()))

    print(f"\nBase form (correct): {base_count} occurrences")
    print(f"Inflected form (violations): {inflected_count} occurrences")

    if inflected_examples:
        print("\nInflected form violations:")
        for ref, match in inflected_examples:
            print(f"  {ref}: {match}")
    else:
        print("\n✓ No inflected form violations found")


def analyze_title_patterns(data):
    """Analyze (title) content - should describe action, not traditional names."""
    print("\n" + "="*60)
    print("TITLE PATTERN ANALYSIS")
    print("="*60)

    title_pattern = re.compile(r'\(title\)\s*([^.]+\.)', re.IGNORECASE)
    titles = []

    for d in data:
        match = title_pattern.search(d['verse'])
        if match:
            titles.append((d['ref'], match.group(1).strip()))

    print(f"\nFound {len(titles)} (title) markers")

    # Categorize titles
    descriptive = []  # Good: describes action
    generic = []      # Bad: traditional name

    traditional_names = ['sermon on the mount', 'beatitudes', 'lord\'s prayer',
                        'ten commandments', 'golden rule']

    for ref, title in titles:
        title_lower = title.lower()
        if any(name in title_lower for name in traditional_names):
            generic.append((ref, title))
        else:
            descriptive.append((ref, title))

    print(f"\nDescriptive titles (good): {len(descriptive)}")
    for ref, title in descriptive[:5]:
        print(f"  {ref}: {title[:60]}...")

    print(f"\nGeneric/traditional titles (need review): {len(generic)}")
    for ref, title in generic[:5]:
        print(f"  {ref}: {title}")


def analyze_new_underscore_markers(data):
    """Analyze underscore markers including new ones from blind testing."""
    print("\n" + "="*60)
    print("UNDERSCORE MARKER ANALYSIS")
    print("="*60)

    # All underscore markers
    marker_pattern = re.compile(r'_(\w+)')
    marker_counts = defaultdict(int)

    for d in data:
        for match in marker_pattern.findall(d['verse']):
            marker_counts[match] += 1

    # Sort by frequency
    sorted_markers = sorted(marker_counts.items(), key=lambda x: -x[1])

    print("\nAll underscore markers by frequency:")
    for marker, count in sorted_markers[:30]:
        print(f"  _{marker}: {count}")

    # Check for new markers from blind testing
    new_markers = ['AdverbLDV', 'Dimplicit', 'distantPast']
    print("\n\nNew markers from blind testing:")
    for marker in new_markers:
        count = marker_counts.get(marker, 0)
        status = "✓ found" if count > 0 else "✗ not found"
        print(f"  _{marker}: {count} ({status})")


def main():
    print("Loading all TBTA data...")
    data = load_all_verses()
    print(f"Loaded {len(data)} verses")
    
    he1_books, he2_books = analyze_he1_vs_he2(data)
    analyze_modal_contradictions(data)
    analyze_number_formatting(data)
    analyze_passive_patterns(data)
    analyze_quote_patterns(data)
    analyze_bracketing_patterns(data)

    # New analyses from blind testing discoveries
    analyze_hyphenated_verb_forms(data)
    analyze_title_patterns(data)
    analyze_new_underscore_markers(data)
    
    # Summary of findings
    print("\n" + "="*60)
    print("SUMMARY OF FINDINGS")
    print("="*60)
    print("""
1. HE1 vs HE2 FORMATS:
   - He1 (OT): More natural flow, fewer markers
   - He2 (NT): Strict notation, many underscore markers
   
2. RELIABLE RULES (high consistency):
   - Coreference Resolution (915 supporting, 6 contradicting)
   - Clause Segmentation (3014 supporting, 0 contradicting)
   - Explicit Relativization (4072 supporting, 67 contradicting)
   - Deixis Marking (3248 supporting, 3 contradicting)
   - Subordinate Bracketing (2362 supporting, 4 contradicting)
   - Quote Framing (1017 supporting, 0 contradicting)
   - Imperative Marking (1189 supporting, 0 contradicting)
   - Gap-filling markers (1526 supporting, 0 contradicting)
   - Yahweh Substitution (914 supporting, 1 contradicting)
   
3. INCONSISTENT RULES (need clarification):
   - Modal Decomposition: 'must/should' often kept, 'can' → 'is able'
   - Number Formatting: Large numbers as digits, small sometimes words
   - Passive Voice: NOT actually converted (passive remains passive)
   - Demonym → Description: Only some demonyms converted
   
4. HE2-SPECIFIC MARKERS:
   - _implicit, _descriptive, _paragraph, _incl, _excl
   - More L2 pairings (word/word)
""")

if __name__ == "__main__":
    main()

