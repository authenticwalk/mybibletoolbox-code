#!/usr/bin/env python3
"""
Analyze TBTA CSV data to extract evidence for transformation rules.
Finds supporting and contradicting examples for each rule.
"""

import csv
import re
import os
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
TSV_PATH = os.path.join(DATA_DIR, "verses-raw.tsv")

@dataclass
class Evidence:
    ref: str
    verse: str
    pattern_match: str
    
@dataclass 
class RuleAnalysis:
    name: str
    pattern: str
    supporting: List[Evidence] = field(default_factory=list)
    contradicting: List[Evidence] = field(default_factory=list)

def load_tsv_data(tsv_path: str) -> List[Tuple[str, str]]:
    """Load reference and verse text from TSV."""
    results = []
    try:
        with open(tsv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                ref = row.get('reference', '')
                verse = row.get('verse', '')
                if ref and verse:
                    results.append((ref, verse))
    except Exception as e:
        print(f"Error loading {tsv_path}: {e}")
    return results

def load_csv_data(csv_path: str) -> List[Tuple[str, str]]:
    """Load reference and verse text from CSV (fallback)."""
    results = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ref = row.get('Reference', '')
                verse = row.get('Verse', '')
                if ref and verse:
                    results.append((ref, verse))
    except Exception as e:
        print(f"Error loading {csv_path}: {e}")
    return results

def analyze_all_files() -> List[Tuple[str, str]]:
    """Load all data from TSV or CSV files."""
    # Try TSV first (preferred)
    if os.path.exists(TSV_PATH):
        data = load_tsv_data(TSV_PATH)
        print(f"Loaded {len(data)} verses from verses-raw.tsv")
        return data

    # Fallback to CSV files
    all_data = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.csv'):
            filepath = os.path.join(DATA_DIR, filename)
            data = load_csv_data(filepath)
            all_data.extend(data)
            print(f"Loaded {len(data)} verses from {filename}")
    print(f"\nTotal: {len(all_data)} verses")
    return all_data

# Rule 1: Coreference Resolution
def find_coreference_resolution(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of pronoun → noun replacement."""
    analysis = RuleAnalysis(
        name="Coreference Resolution",
        pattern="that man|that woman|that person|that family|that group"
    )
    
    # Supporting: "that man", "that woman", "that person", "that family"
    pattern = re.compile(r'\b(that\s+(man|woman|person|family|group|boy|girl|people|thing|country|town|place))\b', re.IGNORECASE)
    
    for ref, verse in data:
        matches = pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:200], str(matches[:3])))
            
    # Contradicting: remaining pronouns (he, she, they, it)
    pronoun_pattern = re.compile(r'\b(he|she|they|it|him|her|them)\b(?!\s*\()', re.IGNORECASE)
    for ref, verse in data:
        # Skip if "he", "she" is in parentheses or part of speech marking
        matches = pronoun_pattern.findall(verse)
        if matches and 'that ' not in verse.lower():
            analysis.contradicting.append(Evidence(ref, verse[:200], str(matches[:3])))
            
    return analysis

# Rule 2: Clause Segmentation  
def find_clause_segmentation(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of sentence splitting."""
    analysis = RuleAnalysis(
        name="Clause Segmentation",
        pattern="Multiple sentences per verse"
    )
    
    for ref, verse in data:
        # Supporting: verse has multiple sentences (multiple periods not at abbreviations)
        sentence_count = len(re.findall(r'\.(?:\s+[A-Z"]|\s*$)', verse))
        if sentence_count >= 3:
            analysis.supporting.append(Evidence(ref, verse[:250], f"{sentence_count} sentences"))
            
    # Contradicting: compound sentences with "and" joining verbs
    compound_pattern = re.compile(r'\w+ed\s+and\s+\w+ed', re.IGNORECASE)
    for ref, verse in data:
        if compound_pattern.search(verse):
            analysis.contradicting.append(Evidence(ref, verse[:200], compound_pattern.search(verse).group()))
            
    return analysis

# Rule 3: Explicit Relativization
def find_explicit_relativization(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of bracketed relative clauses."""
    analysis = RuleAnalysis(
        name="Explicit Relativization",
        pattern="[who/which/that...]"
    )
    
    # Supporting: bracketed relative clauses
    rel_pattern = re.compile(r'\[(?:who|which|that|where|whose|what)[^\]]+\]', re.IGNORECASE)
    for ref, verse in data:
        matches = rel_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:300], str(matches[:2])))
            
    # Contradicting: unbracketed relative clauses
    unbracketed = re.compile(r'(?<!\[)(who|which)\s+(?:was|were|is|are|had|have)\b', re.IGNORECASE)
    for ref, verse in data:
        if unbracketed.search(verse) and '[who' not in verse and '[which' not in verse:
            analysis.contradicting.append(Evidence(ref, verse[:200], unbracketed.search(verse).group()))
            
    return analysis

# Rule 4: Deixis Marking
def find_deixis_marking(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of person marking in parentheses."""
    analysis = RuleAnalysis(
        name="Deixis Marking", 
        pattern="I(Speaker), you(Addressee), we(Group)"
    )
    
    # Supporting: parenthetical person markers
    deixis_pattern = re.compile(r'(I|you|we|my|your|our)\s*\([^)]+\)', re.IGNORECASE)
    for ref, verse in data:
        matches = deixis_pattern.findall(verse)
        if matches:
            full_matches = re.findall(r'((?:I|you|we|my|your|our)\s*\([^)]+\))', verse, re.IGNORECASE)
            analysis.supporting.append(Evidence(ref, verse[:300], str(full_matches[:3])))
            
    # Contradicting: unmarked first/second person
    unmarked = re.compile(r'\b(I|you|we)\b(?!\s*\()', re.IGNORECASE)
    for ref, verse in data:
        if unmarked.search(verse) and '(' not in verse:
            analysis.contradicting.append(Evidence(ref, verse[:200], unmarked.search(verse).group()))
            
    return analysis

# Rule 5: LDV Substitution
def find_ldv_substitution(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of word pairings like family/clan."""
    analysis = RuleAnalysis(
        name="LDV Substitution",
        pattern="simple/complex pairings"
    )
    
    # Supporting: L2 pairings with slash
    ldv_pattern = re.compile(r'\b(\w+)/(\w+)\b')
    for ref, verse in data:
        matches = ldv_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:250], str(matches[:3])))
            
    return analysis

# Rule 6: Subordinate Bracketing
def find_subordinate_bracketing(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of subordinate clauses in brackets."""
    analysis = RuleAnalysis(
        name="Subordinate Bracketing",
        pattern="[in order to...], [if...], [when...]"
    )
    
    # Supporting: purpose, conditional, temporal clauses in brackets
    sub_pattern = re.compile(r'\[(in\s+order\s+to|if|when|because|so\s+that|before|after)[^\]]+\]', re.IGNORECASE)
    for ref, verse in data:
        matches = sub_pattern.findall(verse)
        if matches:
            full = re.findall(r'\[(?:in\s+order\s+to|if|when|because|so\s+that|before|after)[^\]]+\]', verse, re.IGNORECASE)
            analysis.supporting.append(Evidence(ref, verse[:300], str(full[:2])))
            
    # Contradicting: unbracketed subordinate clauses
    unbracketed = re.compile(r'(?<!\[)(in order to|because|so that)\s+\w+', re.IGNORECASE)
    for ref, verse in data:
        if unbracketed.search(verse) and '[' not in verse:
            analysis.contradicting.append(Evidence(ref, verse[:200], unbracketed.search(verse).group()))
            
    return analysis

# Rule 7: Quote Framing
def find_quote_framing(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of speech introduction patterns."""
    analysis = RuleAnalysis(
        name="Quote Framing",
        pattern='X said, ["quote"]'
    )
    
    # Supporting: said/told with bracketed quotes
    quote_pattern = re.compile(r'(said|told|asked|replied|answered)[^\[]*\["[^"]*"\]', re.IGNORECASE)
    for ref, verse in data:
        if quote_pattern.search(verse):
            analysis.supporting.append(Evidence(ref, verse[:300], quote_pattern.search(verse).group()[:100]))
            
    # Also check for opening bracket after speech verbs
    bracket_quote = re.compile(r'(said|told|asked),?\s*\[', re.IGNORECASE)
    for ref, verse in data:
        if bracket_quote.search(verse) and '[' in verse:
            if ref not in [e.ref for e in analysis.supporting]:
                analysis.supporting.append(Evidence(ref, verse[:300], bracket_quote.search(verse).group()))
    
    return analysis

# Rule 8: Imperative Marking
def find_imperative_marking(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of imperative verb marking."""
    analysis = RuleAnalysis(
        name="Imperative Marking",
        pattern="You(Addressee) (imp) verb"
    )
    
    # Supporting: (imp) marker
    imp_pattern = re.compile(r'\(imp\)', re.IGNORECASE)
    for ref, verse in data:
        if imp_pattern.search(verse):
            # Get context around (imp)
            match = re.search(r'.{0,30}\(imp\).{0,30}', verse)
            context = match.group() if match else '(imp)'
            analysis.supporting.append(Evidence(ref, verse[:300], context))
            
    return analysis

# Rule 9: Hyphenated Verbs
def find_hyphenated_verbs(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of hyphenated compound verbs."""
    analysis = RuleAnalysis(
        name="Hyphenated Verbs",
        pattern="run-away, sit-down, stand-up"
    )
    
    # Supporting: hyphenated verbs
    hyph_pattern = re.compile(r'\b([a-z]+-[a-z]+)\b', re.IGNORECASE)
    for ref, verse in data:
        matches = hyph_pattern.findall(verse)
        # Filter for verb-particle patterns
        verb_particles = [m for m in matches if any(p in m.lower() for p in ['away', 'down', 'up', 'out', 'in', 'back', 'off', 'over'])]
        if verb_particles:
            analysis.supporting.append(Evidence(ref, verse[:250], str(verb_particles[:3])))
            
    # Contradicting: inflected forms like "ran-away"
    inflected = re.compile(r'\b(ran|went|came|sat|stood|lay|fell)-\w+\b', re.IGNORECASE)
    for ref, verse in data:
        if inflected.search(verse):
            analysis.contradicting.append(Evidence(ref, verse[:200], inflected.search(verse).group()))
            
    return analysis

# Rule 10: Modal Decomposition
def find_modal_decomposition(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of modal verb expansion."""
    analysis = RuleAnalysis(
        name="Modal Decomposition",
        pattern="can → is able, must → has to"
    )
    
    # Supporting: "is able", "has to", "was able"
    modal_pattern = re.compile(r'\b(is|was|are|were)\s+able\s+\[?to\b', re.IGNORECASE)
    for ref, verse in data:
        if modal_pattern.search(verse):
            analysis.supporting.append(Evidence(ref, verse[:250], modal_pattern.search(verse).group()))
            
    # Also check "has to", "have to"
    must_pattern = re.compile(r'\b(has|have|had)\s+to\s+\[?\w+', re.IGNORECASE)
    for ref, verse in data:
        if must_pattern.search(verse):
            if ref not in [e.ref for e in analysis.supporting]:
                analysis.supporting.append(Evidence(ref, verse[:250], must_pattern.search(verse).group()))
    
    # Contradicting: bare "can", "must", "could"
    bare_modal = re.compile(r'\b(can|must|could|would|should)\s+\w+', re.IGNORECASE)
    for ref, verse in data:
        if bare_modal.search(verse) and 'able' not in verse.lower():
            analysis.contradicting.append(Evidence(ref, verse[:200], bare_modal.search(verse).group()))
            
    return analysis

# Rule 11: Demonym → Description
def find_demonym_conversion(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of demonyms converted to descriptions."""
    analysis = RuleAnalysis(
        name="Demonym → Description",
        pattern="Moabite → [who was from Moab]"
    )
    
    # Supporting: "[who was from X]" or "[who was in X's family]"
    demonym_pattern = re.compile(r'\[who\s+(?:was|were)\s+(?:from|in)[^\]]+\]', re.IGNORECASE)
    for ref, verse in data:
        matches = demonym_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:300], str(matches[:2])))
            
    # Contradicting: bare demonyms like "Moabite", "Ephrathite"  
    demonym_bare = re.compile(r'\b(\w+ite|Jew|Greek|Roman|Egyptian)\b(?!\s*\[)', re.IGNORECASE)
    for ref, verse in data:
        match = demonym_bare.search(verse)
        if match and '[who' not in verse:
            analysis.contradicting.append(Evidence(ref, verse[:200], match.group()))
            
    return analysis

# Rule 12: Implicit Information / Gap-filling
def find_implicit_info(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find examples of added implicit information."""
    analysis = RuleAnalysis(
        name="Gap-filling (Implicit Info)",
        pattern="(implicit-info), (footnote), (implicit-subaction)"
    )
    
    # Supporting: explicit markers
    implicit_pattern = re.compile(r'\((implicit[^)]*|footnote|background)\)', re.IGNORECASE)
    for ref, verse in data:
        matches = implicit_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:300], str(matches[:3])))
            
    # Also check for underscore variants (_implicit, _paragraph, etc.)
    underscore_pattern = re.compile(r'_(\w*implicit\w*|paragraph|background)', re.IGNORECASE)
    for ref, verse in data:
        matches = underscore_pattern.findall(verse)
        if matches:
            if ref not in [e.ref for e in analysis.supporting]:
                analysis.supporting.append(Evidence(ref, verse[:300], str(matches[:3])))
            
    return analysis

# Additional patterns discovered

def find_yahweh_substitution(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find LORD → Yahweh substitution."""
    analysis = RuleAnalysis(
        name="Yahweh Substitution",
        pattern="LORD → Yahweh"
    )
    
    # Supporting: "Yahweh" usage
    for ref, verse in data:
        if 'Yahweh' in verse:
            analysis.supporting.append(Evidence(ref, verse[:200], 'Yahweh'))
            
    # Contradicting: "LORD" remaining
    for ref, verse in data:
        if 'LORD' in verse:
            analysis.contradicting.append(Evidence(ref, verse[:200], 'LORD'))
            
    return analysis

def find_number_formatting(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find number formatting patterns."""
    analysis = RuleAnalysis(
        name="Number Formatting",
        pattern="word numbers → digits (two → 2)"
    )
    
    # Supporting: single digits 1-9 or "10" used
    digit_pattern = re.compile(r'\b([1-9]|10)\b(?!\s*[:\.])')
    for ref, verse in data:
        matches = digit_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:200], str(matches[:3])))
            
    # Contradicting: word numbers
    word_num = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten)\b', re.IGNORECASE)
    for ref, verse in data:
        if word_num.search(verse):
            analysis.contradicting.append(Evidence(ref, verse[:200], word_num.search(verse).group()))
            
    return analysis

def find_passive_to_active(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Find passive voice handling."""
    analysis = RuleAnalysis(
        name="Passive → Active Voice",
        pattern="was done by X → X did"
    )
    
    # Look for "by" phrases indicating passive construction
    passive_pattern = re.compile(r'\b(was|were|been|being)\s+\w+ed\s+by\b', re.IGNORECASE)
    for ref, verse in data:
        if passive_pattern.search(verse):
            analysis.contradicting.append(Evidence(ref, verse[:200], passive_pattern.search(verse).group()))
            
    return analysis


# NEW: Title Pattern Analysis
def find_title_patterns(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Analyze (title) usage - should describe action, not traditional names."""
    analysis = RuleAnalysis(
        name="Title Patterns",
        pattern="(title) Descriptive action statement"
    )

    title_pattern = re.compile(r'\(title\)\s*([^.]+\.)', re.IGNORECASE)
    for ref, verse in data:
        match = title_pattern.search(verse)
        if match:
            title_content = match.group(1).strip()
            analysis.supporting.append(Evidence(ref, verse[:200], title_content[:80]))

    return analysis


# NEW: Addressee Pattern Analysis
def find_addressee_patterns(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Analyze addressee marking - should prefer generic (people) over specific."""
    analysis = RuleAnalysis(
        name="Addressee Patterns",
        pattern="you(people) vs you(Disciples)"
    )

    # Generic addressees (preferred)
    generic_pattern = re.compile(r'you\((people|person|man|woman)\)', re.IGNORECASE)
    # Specific addressees (less preferred)
    specific_pattern = re.compile(r'you\((disciples|followers|apostles|pharisees)\)', re.IGNORECASE)

    for ref, verse in data:
        if generic_pattern.search(verse):
            match = generic_pattern.search(verse)
            analysis.supporting.append(Evidence(ref, verse[:150], match.group()))
        if specific_pattern.search(verse):
            match = specific_pattern.search(verse)
            analysis.contradicting.append(Evidence(ref, verse[:150], match.group()))

    return analysis


# NEW: Hyphenated Verb Base Form Analysis
def find_hyphenated_base_form(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Analyze hyphenated verbs - should be base form only."""
    analysis = RuleAnalysis(
        name="Hyphenated Verb Base Form",
        pattern="go-up (not went-up)"
    )

    # Base forms (correct)
    base_pattern = re.compile(r'\b(go|sit|stand|come|run|throw|fall|lie|walk|turn|get)-\w+\b', re.IGNORECASE)
    # Inflected forms (violations)
    inflected_pattern = re.compile(r'\b(went|sat|stood|came|ran|threw|fell|lay|walked|turned|got)-\w+\b', re.IGNORECASE)

    for ref, verse in data:
        if base_pattern.search(verse):
            match = base_pattern.search(verse)
            analysis.supporting.append(Evidence(ref, verse[:150], match.group()))
        if inflected_pattern.search(verse):
            match = inflected_pattern.search(verse)
            analysis.contradicting.append(Evidence(ref, verse[:150], match.group()))

    return analysis


# NEW: Underscore Marker Analysis
def find_underscore_markers(data: List[Tuple[str, str]]) -> RuleAnalysis:
    """Analyze underscore marker usage."""
    analysis = RuleAnalysis(
        name="Underscore Markers",
        pattern="_implicit, _implicitActiveAgent, etc."
    )

    marker_pattern = re.compile(r'_(\w+)')
    for ref, verse in data:
        matches = marker_pattern.findall(verse)
        if matches:
            analysis.supporting.append(Evidence(ref, verse[:200], str(matches[:5])))

    return analysis


def print_analysis(analysis: RuleAnalysis, max_examples: int = 5):
    """Print formatted analysis results."""
    print(f"\n{'='*60}")
    print(f"## {analysis.name}")
    print(f"Pattern: {analysis.pattern}")
    print(f"\n### Supporting Examples ({len(analysis.supporting)} found)")
    
    for i, ev in enumerate(analysis.supporting[:max_examples]):
        print(f"  {i+1}. **{ev.ref}**: {ev.pattern_match}")
        
    if analysis.contradicting:
        print(f"\n### Contradicting Examples ({len(analysis.contradicting)} found)")
        for i, ev in enumerate(analysis.contradicting[:3]):
            print(f"  {i+1}. NOT **{ev.ref}**: {ev.pattern_match}")

def generate_rules_md(analyses: List[RuleAnalysis]) -> str:
    """Generate updated RULES.md content with references."""
    lines = []
    lines.append("# TBTA Verse Rules (Evidence-Based)")
    lines.append("")
    lines.append("> **Goal**: NIV → Controlled Natural Language for universal translation")
    lines.append("> **Model**: Claude Opus 4.5")
    lines.append("> **Date**: 2024-12-02")
    lines.append("")
    lines.append("## Source Strategy")
    lines.append("")
    lines.append("**Base**: Copy NIV text, **except**:")
    lines.append("- Pronouns (resolve to nouns)")
    lines.append("- Compound sentences (segment)")
    lines.append("- Idioms (decompose to meaning)")
    lines.append("- Passives (convert to active where possible)")
    lines.append("- Complex vocabulary (apply LDV substitution)")
    lines.append("")
    lines.append("**Incorporate from**:")
    lines.append('- **Hebrew**: "Yahweh" for יהוה (not NIV\'s "LORD")')
    lines.append("- **Greek/Hebrew**: Implicit cultural context `(implicit-info)`")
    lines.append("- **Scholarly sources**: Historical footnotes `(footnote)`")
    lines.append("- **Semantic analysis**: Clause boundaries, participant tracking")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    for analysis in analyses:
        # Get top 5 supporting refs
        supporting_refs = [e.ref for e in analysis.supporting[:5]]
        contradicting_refs = [e.ref for e in analysis.contradicting[:3]]
        
        ref_str = ", ".join(supporting_refs) if supporting_refs else "N/A"
        if contradicting_refs:
            ref_str += "; NOT " + ", ".join(contradicting_refs)
            
        lines.append(f"### {analysis.name}")
        lines.append(f"**Evidence**: ({ref_str})")
        lines.append(f"**Pattern**: `{analysis.pattern}`")
        lines.append(f"**Stats**: {len(analysis.supporting)} supporting, {len(analysis.contradicting)} contradicting")
        lines.append("")
        
    return "\n".join(lines)

def main():
    print("Loading TBTA CSV data...")
    data = analyze_all_files()
    
    print("\n" + "="*60)
    print("ANALYZING TRANSFORMATION RULES")
    print("="*60)
    
    analyses = []
    
    # Core transforms
    analyses.append(find_coreference_resolution(data))
    analyses.append(find_clause_segmentation(data))
    analyses.append(find_explicit_relativization(data))
    analyses.append(find_deixis_marking(data))
    analyses.append(find_ldv_substitution(data))
    
    # Notation patterns
    analyses.append(find_subordinate_bracketing(data))
    analyses.append(find_quote_framing(data))
    analyses.append(find_imperative_marking(data))
    
    # Lexical rules
    analyses.append(find_hyphenated_verbs(data))
    analyses.append(find_modal_decomposition(data))
    analyses.append(find_demonym_conversion(data))
    analyses.append(find_implicit_info(data))
    
    # Additional patterns
    analyses.append(find_yahweh_substitution(data))
    analyses.append(find_number_formatting(data))
    analyses.append(find_passive_to_active(data))

    # NEW patterns from blind testing
    analyses.append(find_title_patterns(data))
    analyses.append(find_addressee_patterns(data))
    analyses.append(find_hyphenated_base_form(data))
    analyses.append(find_underscore_markers(data))

    for analysis in analyses:
        print_analysis(analysis)
        
    # Generate updated RULES.md
    rules_content = generate_rules_md(analyses)
    output_dir = os.path.dirname(__file__)
    with open(os.path.join(output_dir, "RULES-EVIDENCED.md"), 'w') as f:
        f.write(rules_content)
    print(f"\n\nGenerated RULES-EVIDENCED.md")
    
    # Also output detailed evidence file
    with open(os.path.join(output_dir, "EVIDENCE-DETAILED.md"), 'w') as f:
        f.write("# Detailed Evidence for TBTA Rules\n\n")
        for analysis in analyses:
            f.write(f"## {analysis.name}\n\n")
            f.write(f"### Supporting Examples ({len(analysis.supporting)} total)\n\n")
            for i, ev in enumerate(analysis.supporting[:10]):
                f.write(f"{i+1}. **{ev.ref}**\n")
                f.write(f"   - Match: `{ev.pattern_match}`\n")
                f.write(f"   - Context: {ev.verse[:150]}...\n\n")
            if analysis.contradicting:
                f.write(f"\n### Contradicting Examples ({len(analysis.contradicting)} total)\n\n")
                for i, ev in enumerate(analysis.contradicting[:5]):
                    f.write(f"{i+1}. **{ev.ref}**\n")
                    f.write(f"   - Match: `{ev.pattern_match}`\n")
                    f.write(f"   - Context: {ev.verse[:150]}...\n\n")
            f.write("---\n\n")
    print("Generated EVIDENCE-DETAILED.md")

if __name__ == "__main__":
    main()

