# Vocabulary Alternate (TBTA Clause Position 18)

**One-sentence description**: Marks clauses with complex vs simple vocabulary options to support reading-level adaptations and literacy-sensitive translations.

**Target Audience**: Bible translators working with diverse literacy levels, children's Bible creators, and translators serving low-literacy communities.

**Primary Use Case**: When translating for audiences with varying literacy levels, translators need guidance on whether to use sophisticated theological vocabulary or simpler everyday equivalents. Without this feature, translations may be inaccessible to less-educated readers or overly simplistic for educated audiences.

---

## Purpose

### What It Is

Vocabulary Alternate is a clause-level feature that identifies whether a clause can be expressed using:
- **Complex vocabulary**: Sophisticated, theological, or formal terminology
- **Simple vocabulary**: Everyday, accessible, or common language equivalents

Additionally, it tracks **coordination position** (first/middle/last in a series) to help translators maintain consistency when rendering coordinate clauses with similar vocabulary levels.

### Why It Matters

**Reading Level Adaptations**:
- Children's Bibles need simple vocabulary: "home" instead of "dwelling place"
- Study Bibles for scholars can use technical terms: "propitiation" instead of "payment for sin"
- Low-literacy translations require accessible language: "to make right with God" instead of "justification"

**Literacy Level Considerations**:
- Global literacy rates vary dramatically (50-99% by region)
- Many languages have oral-first speakers who struggle with complex written forms
- Vocabulary choice directly impacts comprehension and engagement

**Translation Consistency**:
- When translating coordinated clauses ("A and B and C"), maintaining consistent vocabulary level across the series creates natural flow
- Coordination markers (first/middle/last) help translators apply uniform simplification strategies

**Real-World Impact**:
- A translation using "tabernacle" (complex) may be incomprehensible to readers who would understand "tent of meeting" (simple)
- Theological terms like "sanctification" (complex) vs "being made holy" (simple) determine audience accessibility
- Children hearing "God dwells among us" (complex) may not grasp the meaning, while "God lives with us" (simple) is immediately clear

### Who Needs It

**Children's Bible Translators**: Primary users who systematically simplify vocabulary for young readers (ages 5-12).

**Low-Literacy Language Translators**: Essential for translating into languages where most speakers have limited formal education.

**Multi-Tier Translation Projects**: Teams producing multiple versions at different reading levels from the same source.

**Oral Bible Translators**: Communities where oral communication dominates need spoken-register vocabulary, not literary language.

### When NOT to Use This Feature

- **Single-tier translations**: If producing only one version at a fixed reading level, vocabulary choices are made consistently without needing alternates
- **Source text preservation**: When maintaining source text vocabulary is prioritized (interlinear translations)
- **Context determines vocabulary**: Many vocabulary choices depend on surrounding context, not clause-level decisions

---

## Methodology

### Phase 1: Data Extraction

**Location in TBTA Data**:

Vocabulary Alternate appears at **Position 18** in the clause annotation string:

```
c-[type]-[force]-[topic]-[speaker]-[listener]-[attitude]-[age]-[age_rel]-[style]-
  [genre]-[structure]-[salience]-[sequence]-[location]-[implicit]-[alternative]-
  [VOCABULARY]-[rhetorical]-[spares]
```

**Extraction Code Example**:

```python
def extract_vocabulary_alternate(clause_string):
    """
    Extract vocabulary alternate from TBTA clause annotation.

    Returns: {
        'level': 'complex' | 'simple',
        'coordination': 'single' | 'first' | 'middle' | 'last'
    }
    """
    parts = clause_string.split('-')
    if len(parts) < 19:
        return {'level': None, 'coordination': 'single'}

    vocab_code = parts[17]  # Position 18 (0-indexed)

    # Decode vocabulary level and coordination
    mapping = {
        'C': ('complex', 'single'),
        'c': ('complex', 'first'),
        'O': ('complex', 'middle'),
        'L': ('complex', 'last'),
        'S': ('simple', 'single'),
        's': ('simple', 'first'),
        'o': ('simple', 'middle'),
        'l': ('simple', 'last'),
    }

    return {
        'level': mapping.get(vocab_code, (None, None))[0],
        'coordination': mapping.get(vocab_code, (None, None))[1]
    }
```

**Context Required**: Clause-level (each clause annotated independently).

**Data Availability**: This feature is **explicitly encoded** in TBTA data - no prediction needed.

### Phase 2: Applying Vocabulary Guidance

Since Vocabulary Alternate is explicitly provided, the main task is **interpretation and application** rather than prediction.

**Decision Framework**:

#### Level 1: Determine Target Reading Level (95%+ clarity)

**Target Audiences**:
- **Children (ages 5-12)**: Use **Simple** vocabulary
- **Youth (ages 13-17)**: Use **Mixed** (prefer simpler)
- **Adults with low literacy (1-4 years education)**: Use **Simple**
- **Adults with standard literacy (5-12 years)**: Use **Complex**
- **Scholars (13+ years education)**: Use **Complex**

#### Level 2: Apply Coordination Consistency (85%+ confidence)

When translating coordinated clauses, maintain consistent vocabulary level:

```python
def apply_coordination_consistency(clauses):
    """
    Ensure coordinated clauses use consistent vocabulary level.
    """
    # Group by coordination series
    coordination_groups = group_by_coordination(clauses)

    for group in coordination_groups:
        if len(group) > 1:
            # Determine dominant vocabulary level in series
            levels = [c['vocabulary']['level'] for c in group]
            target_level = determine_target_level(levels)

            # Apply consistent level across all coordinated clauses
            for clause in group:
                clause['vocabulary']['applied_level'] = target_level

    return clauses

def determine_target_level(levels):
    """
    For mixed levels in coordination, prefer simpler option.
    """
    if 'simple' in levels:
        return 'simple'  # When in doubt, simplify
    return 'complex'
```

**Coordination Examples**:
- If three coordinated clauses are marked `c-O-L` (complex-first, complex-middle, complex-last), maintain complex vocabulary throughout
- If series is `s-o-l` (simple-first, simple-middle, simple-last), use simple vocabulary consistently
- If mixed `c-o-l` (complex-first, simple-middle, simple-last), resolve to simple for consistency

#### Level 3: Vocabulary Substitution Patterns (80%+ confidence)

**Common Complex → Simple Mappings**:

| Domain | Complex Vocabulary | Simple Vocabulary |
|--------|-------------------|------------------|
| **Dwelling** | tabernacle, dwelling place, habitation | tent, home, place to live |
| **Theology** | propitiation, atonement, expiation | payment for sin, making peace with God |
| **Theology** | sanctification, consecration | being made holy, set apart for God |
| **Theology** | justification, righteousness | being made right with God, doing right |
| **Religious** | covenant, testament | agreement, promise |
| **Movement** | depart, sojourn, traverse | leave, stay, travel |
| **Communication** | proclaim, declare, testify | tell, say, speak about |
| **Emotion** | rejoice, grieve, lament | be happy, be sad, cry out |
| **Authority** | ordained, appointed, established | chosen, put in place, set up |
| **Abstract** | redemption, salvation, deliverance | rescue, saving, being set free |

**Implementation Strategy**:

```python
# Example vocabulary substitution
def apply_vocabulary_level(clause_text, target_level, language_code):
    """
    Apply vocabulary simplification or complexification.
    """
    # Load language-specific vocabulary mappings
    vocab_map = load_vocabulary_map(language_code)

    if target_level == 'simple':
        # Replace complex terms with simple equivalents
        for complex_term, simple_term in vocab_map['complex_to_simple'].items():
            clause_text = clause_text.replace(complex_term, simple_term)

    return clause_text
```

### Phase 3: Validation

**Accuracy**: This feature is explicitly encoded in TBTA data, so no prediction accuracy applies. Validation focuses on **correct application**.

**Critical Rules**:

- [ ] All values from official TBTA enumeration (C, c, O, L, S, s, o, l)
- [ ] Coordination series consistency (all first/middle/last in a series use same level)
- [ ] Target reading level alignment (children's versions use simple, scholarly versions use complex)
- [ ] Natural language flow (substitutions sound natural, not mechanical)

**Feature-Specific Validation**:

```python
def validate_vocabulary_alternate(clause):
    """
    Validate vocabulary alternate encoding and application.
    """
    errors = []

    # 1. Valid value check
    valid_values = ['C', 'c', 'O', 'L', 'S', 's', 'o', 'l']
    if clause.vocabulary not in valid_values:
        errors.append(f"Invalid vocabulary code: {clause.vocabulary}")

    # 2. Coordination consistency check
    if clause.vocabulary in ['c', 'O', 'L']:  # Coordinated positions
        series = get_coordination_series(clause)
        levels = [c.vocabulary[0].upper() for c in series]
        if len(set(levels)) > 1:
            errors.append(f"Inconsistent vocabulary levels in coordination: {levels}")

    # 3. Reading level alignment check
    target_level = get_target_reading_level(clause.translation_project)
    applied_level = get_applied_vocabulary_level(clause)
    if not levels_compatible(target_level, applied_level):
        errors.append(f"Vocabulary level {applied_level} incompatible with target {target_level}")

    return errors
```

**Success Criteria**:
- Coordinated clauses maintain consistent vocabulary level (100% consistency)
- Target reading level matches applied vocabulary (95%+ alignment)
- Natural language equivalents used (qualitative assessment)

---

## Output Schema

**Filename Format**:

```
./bible/commentaries/{BOOK}/{CHAPTER:03d}/{VERSE:03d}/{BOOK}-{CHAPTER:03d}-{VERSE:03d}-vocabulary-alternate.yaml
```

**Example**: `./bible/commentaries/JHN/003/016/JHN-003-016-vocabulary-alternate.yaml`

**YAML Structure**:

```yaml
verse: JHN.3.16
vocabulary_alternate:
  clauses:
    - clause_id: 1
      text: "For God so loved the world"
      vocabulary:
        level: complex  # or simple
        coordination: single  # single | first | middle | last
        code: C  # Original TBTA code
      examples:
        complex: "For God so loved the world"
        simple: "God loved the people of the world so much"
      domain: theology

    - clause_id: 2
      text: "that he gave his only begotten Son"
      vocabulary:
        level: complex
        coordination: single
        code: C
      examples:
        complex: "that he gave his only begotten Son"
        simple: "that he gave his one and only Son"
      domain: theology

metadata:
  source: tbta
  version: 1.0.0
  extraction_date: 2025-11-05
```

### Examples

#### Example 1: Simple Case (Single Clause, Complex Vocabulary)

**Romans 3:25 - "propitiation"**

```yaml
verse: ROM.3.25
vocabulary_alternate:
  clause:
    level: complex
    code: C
    examples:
      complex: "Whom God set forth as a propitiation through faith in his blood"
      simple: "God sent Jesus to take the punishment for our sin through faith in his death"
    explanation: "'Propitiation' (complex) = sacrifice satisfying God's wrath. Simple: 'payment for sin'"
metadata:
  source: tbta
  target_audiences:
    complex: [adult_standard, adult_scholarly]
    simple: [children_middle, youth, adult_basic]
```

#### Example 2: Simple Case (Single Clause, Simple Vocabulary)

**Mark 1:4 - "preaching" (simplified)**

```yaml
verse: MRK.1.4
vocabulary_alternate:
  clause:
    level: simple
    code: S
    examples:
      complex: "proclaiming a baptism of repentance"
      simple: "telling people to be baptized and turn from their sins"
    note: "Simple: 'telling' vs 'proclaiming', 'turn from sins' vs 'repentance'"
metadata:
  source: tbta
```

#### Example 3: Coordination Series (Complex)

**Matthew 28:19 - Great Commission**

```yaml
verse: MAT.28.19
vocabulary_alternate:
  clauses:
    - clause_id: 1
      text: "Go therefore"
      vocabulary:
        level: complex
        coordination: first
        code: c
      examples:
        complex: "Go therefore"
        simple: "So go"

    - clause_id: 2
      text: "and make disciples of all nations"
      vocabulary:
        level: complex
        coordination: middle
        code: O
      examples:
        complex: "and make disciples of all nations"
        simple: "and help people everywhere become my followers"

    - clause_id: 3
      text: "baptizing them in the name of the Father and of the Son and of the Holy Spirit"
      vocabulary:
        level: complex
        coordination: last
        code: L
      examples:
        complex: "baptizing them in the name of the Father and of the Son and of the Holy Spirit"
        simple: "baptize them in the name of the Father and the Son and the Holy Spirit"

  coordination_note: |
    All three clauses maintain complex vocabulary level (c-O-L).
    For children's version, would use simple throughout (s-o-l):
    "So go and help people everywhere become my followers and baptize them..."

metadata:
  source: tbta
  version: 1.0.0
  coordination_consistency: maintained
```

#### Example 4: Mixed Coordination (Resolution to Simple)

**1 John 4:7 - Love command**

```yaml
verse: 1JN.4.7
vocabulary_alternate:
  clauses:
    - {id: 1, level: complex, coord: first, code: c,
       complex: "Beloved, let us love one another",
       simple: "Dear friends, let us love each other"}
    - {id: 2, level: simple, coord: middle, code: o,
       complex: "for love is from God",
       simple: "because love comes from God"}
    - {id: 3, level: simple, coord: last, code: l,
       complex: "everyone who loves has been born of God",
       simple: "everyone who loves is God's child"}

  coordination_resolution: "Mixed (c-o-l) resolved to simple for consistency"
metadata:
  source: tbta
  rationale: "When mixed, prefer simpler for natural flow"
```

#### Example 5: Domain-Specific Vocabulary (Theological)

**Ephesians 1:7 - Redemption language**

```yaml
verse: EPH.1.7
vocabulary_alternate:
  clause:
    level: complex
    code: C
    examples:
      complex: "In him we have redemption through his blood"
      simple: "Through Christ's death we are set free"
    mappings:
      redemption: "being set free"
      through_his_blood: "through his death"
      in_him: "through Christ"
metadata:
  domain: soteriology
  complexity_factors: [technical_terms, metaphorical_language, abstract_concepts]
```

---

## Related Features

### Integration with Other TBTA Features

**Correlates With**:

1. **Implicit Information (Pos 16)**: Complex vocabulary often requires cultural knowledge; simple may need explicit statements
2. **Discourse Genre (Pos 11)**: Narrative uses simpler vocabulary than expository; epistolary uses theological terms
3. **Speaker Demographics (Pos 5-6)**: Jesus to children (simple), Paul to educated churches (complex)

**Example**:
```yaml
clause:
  vocabulary: complex
  implicit_info: cultural
  genre: epistolary
  speaker: Paul

guidance: "Paul uses complex theological terms for educated audience.
          For low-literacy, simplify 'justification' → 'being made right with God'"
```

### Translation Workflow

**When to Consult**:
1. **Project Start**: Determine target reading level
2. **Draft**: Apply vocabulary alternates per clause
3. **Revision**: Check coordination consistency
4. **Testing**: Validate with target readers

**Workflow**: Target level → Extract alternates → Apply substitutions → Check consistency → Validate → Finalize

### Limitations

**Not a Silver Bullet**:
- Vocabulary complexity is context/culture-dependent
- Some concepts have no simple equivalents (need explanation)
- Reading level involves more than vocabulary (structure, concepts)

**Best Practices**:
- Use as guidance, not rigid rules
- Test with actual readers
- Provide glossaries for complex terms
- Consider multiple versions (children's, youth, adult)

---

## Summary

**Vocabulary Alternate** is a practical feature for creating **accessible, reader-appropriate** translations. By marking clauses as complex or simple, TBTA guides translators in adapting vocabulary to diverse literacy levels - from children's Bibles to scholarly study editions.

**Key Value**: Enables **multiple reading levels from one source**, serving global audiences with varying educational backgrounds and ensuring the Bible is accessible to all.

**Core Principle**: **Meet readers where they are** - sophisticated theological language for scholars, everyday language for children and new believers.
