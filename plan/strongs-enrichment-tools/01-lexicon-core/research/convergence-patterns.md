# Convergence & Divergence Patterns

**Tool:** strongs-lexicon-core
**Phase:** Research
**Created:** 2025-11-08

---

## Purpose

This document explains how to identify when lexicons agree (convergence) vs. disagree (divergence), which is CRITICAL for fair use compliance.

**Why This Matters:**
- **Fair use requires convergence grouping** (list sources that agree collectively)
- **Divergence in comparative context** (quote different views for scholarly analysis)
- **Cannot reconstruct individual lexicons** (would violate copyright)

---

## Convergence Patterns: When Lexicons Agree

### Definition

**Convergence:** When 3+ authoritative lexicons provide essentially the same information about a word (etymology, primary meaning, semantic range).

**Fair Use Approach:** List sources collectively, don't quote each individually.

### How to Detect Convergence

**Pattern 1: Identical Etymology**
```yaml
# When multiple lexicons cite same root word
Base file (Strong's): "from δύναμαι (dunamai) - to be able"
BibleHub (Thayer's): "from δύναμαι - to be able"
BibleHub (HELPS): "from 1410 /dýnamai ('able, capable')"
StudyLight (Abbott-Smith): "δύναμις from δύναμαι"

# → CONVERGENCE DETECTED
Result:
  etymology:
    root: "δύναμαι (dunamai)"
    meaning: "to be able"
    citation: "{strongs} {thayer} {helps} {abbott-smith}"
    convergence_note: "All major lexicons agree on etymology"
```

**Pattern 2: Primary Meaning Agreement**
```yaml
# When lexicons give same core definition
Strong's: "strength, power, ability"
Thayer's: "strength, power, ability"
HELPS: "power, especially achieving power"
Mounce's: "power, might, strength"

# → CONVERGENCE DETECTED
Result:
  primary_meaning: "strength, power, ability"
  lexicons_agreeing: [strongs, thayer, helps, mounce]
  confidence: "HIGH - universal agreement"
```

**Pattern 3: Semantic Range Overlap**
```yaml
# When lexicons list same usage categories
Thayer's Categories:
  1. strength, power, ability
  2. power for performing miracles
  3. moral power, excellence of soul

BDB/Others have similar 3-category split

# → CONVERGENCE ON STRUCTURE
Result:
  semantic_range_convergence: "Major lexicons identify 3 primary meanings"
  categories_agreed: 3
  note: "Semantic range structure consistent across sources"
```

### Convergence Grouping Syntax

**Correct Fair Use Pattern:**
```yaml
etymology:
  derivation: "From root δύναμαι (to be able) {strongs} {thayer} {helps} {abbott-smith}"
  convergence_note: "Etymology consistent across all major Greek lexicons"
  confidence: "HIGH"
```

**Why This is Fair Use:**
- ✅ Lists sources collectively (convergence grouping)
- ✅ Doesn't quote each lexicon's full entry
- ✅ Cannot reconstruct any single lexicon from this
- ✅ Adds transformative note (confidence assessment)

**WRONG (Copyright Violation):**
```yaml
# DON'T DO THIS - enables reconstruction
thayers_entry: "δύναμις, -εως, ἡ (δύναμαι), from Homer down..."
helps_entry: "1411 dýnamis (from 1410 /dýnamai) – properly, power..."
abbott_smith_entry: "δύναμις, -εως, ἡ [in LXX chiefly for..."

# This reproduces individual lexicons - COPYRIGHT VIOLATION!
```

---

## Divergence Patterns: When Lexicons Disagree

### Definition

**Divergence:** When authoritative sources provide different interpretations, meanings, or emphases for a word.

**Fair Use Approach:** Quote different views in comparative scholarly context (transformative analysis).

### How to Detect Divergence

**Pattern 1: Classical vs. Koine Semantic Shift**
```yaml
# When classical and NT usage differ significantly

LSJ (Classical): "δύναμις - physical strength, force (in Plato, Aristotle)"
Thayer's (Koine/NT): "δύναμις - miraculous power, divine ability"

# → DIVERGENCE DETECTED (diachronic)
Result:
  lexical_divergence:
    - semantic_area: "Diachronic semantic shift"
      classical_usage:
        definition: "physical strength, force"
        sources: [lsj]
        context: "Classical Greek (Plato, Aristotle)"
        citation: "{lsj-abridged}"
      koine_usage:
        definition: "miraculous power, divine ability"
        sources: [thayer, helps]
        context: "New Testament Greek"
        citation: "{thayer} {helps}"
      analysis: "Semantic shift from natural physical strength to supernatural divine power" {llm-cs45}
```

**Pattern 2: Theological Interpretation Differences**
```yaml
# When theological emphasis differs

Lexicon A: "λόγος - word, speech, discourse"
Lexicon B: "λόγος - The Word (Logos, Christ), divine reason"

# → DIVERGENCE DETECTED (theological)
Result:
  lexical_divergence:
    - semantic_area: "Theological vs. linguistic emphasis"
      linguistic_focus:
        definition: "word, speech, rational discourse"
        sources: [lsj, abbott-smith]
        context: "Linguistic/semantic analysis"
      theological_focus:
        definition: "The Word (Logos), divine reason incarnate"
        sources: [helps, tdnt-ref]
        context: "Christological interpretation (John 1:1)"
      note: "Both valid - depends on whether discussing word usage or theological concept" {llm-cs45}
```

**Pattern 3: Emphasis Differences (Subtle Divergence)**
```yaml
# When lexicons emphasize different aspects

Source A emphasizes: "inherent power"
Source B emphasizes: "power in action, manifested strength"

# → MINOR DIVERGENCE (nuance)
Result:
  lexical_divergence:
    - semantic_area: "Nuance: inherent vs. manifested"
      approach_1:
        emphasis: "inherent ability, latent power"
        sources: [abbott-smith]
      approach_2:
        emphasis: "power in action, demonstrated strength"
        sources: [helps, tdnt-ref]
      synthesis: "Both aspects present - word encompasses both latent and active power" {llm-cs45}
```

### Divergence Quotation Syntax

**Correct Fair Use Pattern:**
```yaml
lexical_divergence:
  - semantic_area: "Classical to Koine semantic development"
    classical_usage:
      meaning: "physical strength (Plato, Aristotle)" {lsj-abridged}
      period: "Classical Greek (5th-4th BCE)"
    koine_usage:
      meaning: "miraculous power, divine ability" {thayer} {helps}
      period: "Koine Greek (NT era)"
    scholarly_analysis: |
      The semantic shift from Classical to Koine reflects the word's
      application to supernatural contexts in biblical literature.
      Classical authors used δύναμις for natural physical strength,
      while NT writers extended it to divine miraculous power. {llm-cs45}
```

**Why This is Fair Use:**
- ✅ Comparative context (analyzing differences)
- ✅ Transformative analysis (scholarly commentary)
- ✅ Limited quotation (brief excerpts, not full entries)
- ✅ Cannot reconstruct lexicons from this

---

## Convergence Detection Algorithm

### Step 1: Collect All Definitions

```python
def collect_definitions(strongs_number):
    definitions = {}

    # From base file
    if base_data.has('definition'):
        definitions['strongs'] = base_data['definition']

    # From BibleHub
    if biblehub.has('thayers') and not in_base_file('thayers'):
        definitions['thayer'] = biblehub['thayers']['definition']

    if biblehub.has('helps'):
        definitions['helps'] = biblehub['helps']['definition']

    # From StudyLight
    if studylight.has('abbott_smith'):
        definitions['abbott_smith'] = studylight['abbott_smith']['definition']

    if studylight.has('mounce'):
        definitions['mounce'] = studylight['mounce']['definition']

    return definitions
```

### Step 2: Identify Overlapping Terms

```python
def identify_overlap(definitions):
    # Extract key terms from each definition
    # Example: "strength, power, ability" → ['strength', 'power', 'ability']

    term_sets = {}
    for source, definition in definitions.items():
        terms = extract_key_terms(definition)
        term_sets[source] = set(terms)

    # Find intersection (common terms)
    common_terms = set.intersection(*term_sets.values())

    # Find union (all terms)
    all_terms = set.union(*term_sets.values())

    # Calculate overlap percentage
    overlap_ratio = len(common_terms) / len(all_terms) if all_terms else 0

    return {
        'common_terms': list(common_terms),
        'overlap_ratio': overlap_ratio,
        'sources_agreeing': list(definitions.keys())
    }
```

### Step 3: Determine Convergence Strength

```python
def determine_convergence_strength(overlap_analysis):
    ratio = overlap_analysis['overlap_ratio']
    source_count = len(overlap_analysis['sources_agreeing'])

    if ratio >= 0.75 and source_count >= 3:
        return {
            'strength': 'STRONG',
            'confidence': 'HIGH',
            'note': f"Strong convergence across {source_count} lexicons"
        }
    elif ratio >= 0.50 and source_count >= 2:
        return {
            'strength': 'MODERATE',
            'confidence': 'MEDIUM',
            'note': f"Moderate agreement across {source_count} sources"
        }
    else:
        return {
            'strength': 'WEAK',
            'confidence': 'LOW',
            'note': "Limited convergence - check for divergence patterns"
        }
```

---

## Divergence Detection Algorithm

### Step 1: Identify Semantic Domains

```python
def identify_semantic_domains(definitions):
    """
    Group definitions by semantic domain
    """
    domains = {
        'physical': [],      # physical strength, force
        'abstract': [],      # ability, capacity
        'theological': [],   # divine power, miraculous
        'social': [],        # authority, influence
        'classical': [],     # classical usage
        'koine': []          # NT-era usage
    }

    for source, definition in definitions.items():
        # Classify definition into domain(s)
        if 'physical strength' in definition.lower():
            domains['physical'].append(source)
        if 'divine' in definition.lower() or 'miracle' in definition.lower():
            domains['theological'].append(source)
        # ... more classification

    return domains
```

### Step 2: Find Domain Splits

```python
def find_divergence(domain_analysis):
    """
    Identify where sources split into different semantic domains
    """
    divergences = []

    # Check for classical vs. koine split
    if domain_analysis['classical'] and domain_analysis['koine']:
        divergences.append({
            'type': 'diachronic_shift',
            'classical_sources': domain_analysis['classical'],
            'koine_sources': domain_analysis['koine'],
            'significance': 'SEMANTIC_SHIFT'
        })

    # Check for theological vs. linguistic split
    if domain_analysis['theological'] and len(domain_analysis['physical']) > 0:
        divergences.append({
            'type': 'theological_emphasis',
            'theological_sources': domain_analysis['theological'],
            'linguistic_sources': domain_analysis['physical'],
            'significance': 'INTERPRETATION_DIFFERENCE'
        })

    return divergences
```

### Step 3: Document Divergence

```python
def document_divergence(divergences):
    """
    Create fair use divergence documentation
    """
    documented = []

    for div in divergences:
        if div['type'] == 'diachronic_shift':
            documented.append({
                'semantic_area': 'Classical to Koine semantic development',
                'classical_usage': {
                    'sources': div['classical_sources'],
                    'definition': extract_brief_quote(div['classical_sources']),
                    'citation': format_citations(div['classical_sources'])
                },
                'koine_usage': {
                    'sources': div['koine_sources'],
                    'definition': extract_brief_quote(div['koine_sources']),
                    'citation': format_citations(div['koine_sources'])
                },
                'analysis': generate_scholarly_analysis(div)
            })

    return documented
```

---

## Examples: Real Word Analysis

### Example 1: Strong Convergence (G26 - ἀγάπη)

**Collected Definitions:**
- Strong's: "affection, benevolence, love"
- Thayer's: "love, affection, good will, benevolence"
- HELPS: "love, agape (divine love)"
- Abbott-Smith: "love, affection (esp. in NT of divine love)"

**Convergence Analysis:**
- Common terms: [love, affection, benevolence]
- Overlap ratio: 85%
- Sources agreeing: 4

**Result:**
```yaml
lexical_convergence:
  primary_meaning: "love, affection, benevolence"
  lexicons_agreeing: [strongs, thayer, helps, abbott-smith]
  confidence: "HIGH"
  convergence_note: "Strong convergence across all major Greek lexicons"
```

**Divergence Detected:**
```yaml
lexical_divergence:
  - semantic_area: "General vs. theological emphasis"
    general_love:
      sources: [strongs, abbott-smith]
      emphasis: "General affection and benevolence"
    divine_love:
      sources: [helps, thayer]
      emphasis: "Distinctly Christian/divine love, agape"
    synthesis: "Word used for both general affection and specifically divine self-sacrificial love" {llm-cs45}
```

### Example 2: Significant Divergence (G3056 - λόγος)

**Collected Definitions:**
- LSJ (Classical): "speech, discourse, rational account (Plato, Aristotle)"
- Thayer's: "word, speech; The Word (Logos, John 1:1)"
- HELPS: "The Word, Jesus Christ as divine expression"
- Abbott-Smith: "word, speech, reason, discourse"

**Divergence Analysis:**
```yaml
lexical_divergence:
  - semantic_area: "Linguistic vs. Christological interpretation"
    linguistic_focus:
      definition: "word, speech, rational discourse" {lsj} {abbott-smith}
      context: "General linguistic usage, classical philosophy"
      sources: [lsj, abbott-smith]

    christological_focus:
      definition: "The Word, Logos, divine reason incarnate in Christ" {helps} {thayer}
      context: "Theological interpretation (John 1:1, 1:14)"
      sources: [helps, thayer]

    analysis: |
      λόγος exhibits both general linguistic usage (word/speech) and
      specific theological application (The Word = Christ). Classical
      Greek emphasized rational discourse and philosophical reasoning.
      NT writers, especially John, appropriated the term for
      Christological purposes, identifying Jesus as the Logos -
      God's ultimate self-expression. {llm-cs45}
```

### Example 3: Diachronic Shift (G1411 - δύναμις)

**Collected Definitions:**
- LSJ (Classical): "strength, power, force (natural, physical)"
- Thayer's: "power, ability, esp. for performing miracles"
- HELPS: "power, achieving power (especially miraculous)"

**Convergence + Divergence:**
```yaml
lexical_convergence:
  primary_meaning: "power, strength, ability"
  lexicons_agreeing: [lsj, thayer, helps]
  confidence: "HIGH"

lexical_divergence:
  - semantic_area: "Diachronic semantic shift (Classical → Koine)"
    classical_usage:
      definition: "natural physical strength, force" {lsj-abridged}
      period: "Classical Greek (5th-4th BCE)"
      context: "Used by Plato, Aristotle for natural power"

    koine_usage:
      definition: "miraculous power, divine ability" {thayer} {helps}
      period: "Koine Greek (NT era)"
      context: "Applied to supernatural divine power in NT"

    semantic_shift: |
      Classical authors used δύναμις for natural physical or political
      power. NT writers extended the semantic range to include
      supernatural miraculous power, particularly divine ability to
      perform signs and wonders. The core concept of "power" remains,
      but the domain shifted from natural to supernatural. {llm-cs45}
```

---

## Fair Use Checklist

### For Convergence Documentation

- [ ] Multiple lexicons cited collectively (not individually reproduced)
- [ ] Convergence note adds transformative analysis
- [ ] Cannot reconstruct any single lexicon from output
- [ ] Inline citations present: `{source1} {source2} {source3}`
- [ ] Confidence level assessed (HIGH/MEDIUM/LOW)

### For Divergence Documentation

- [ ] Different views quoted in comparative context
- [ ] Scholarly analysis explains significance of difference
- [ ] Limited quotation (brief excerpts, not full entries)
- [ ] Transformative purpose (analyzing semantic shifts, theological emphases)
- [ ] Cannot reconstruct any single lexicon from output

---

## Next Steps

1. Apply these patterns in experiments (5 test words)
2. Validate convergence/divergence detection algorithms
3. Refine based on real-world testing
4. Document edge cases and exceptions

**See Also:**
- `source-inventory.md` - What data is available
- `extraction-methods.md` - How to extract data
- `../experiments/` - Test convergence/divergence detection on real words
