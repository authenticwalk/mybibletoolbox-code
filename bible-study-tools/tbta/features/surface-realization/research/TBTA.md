# TBTA Documentation Review: Surface Realization

**Feature**: Surface Realization
**TBTA Tier**: A (Essential - affects 1000+ languages)
**TBTA Status**: ✅ Complete
**Documentation Date**: 2025-11-29
**Sources**: {tbta-features-2025}, {tbta-data-structure-2025}

---

## 1. Concept Definition

### What is Surface Realization?

**Surface Realization** refers to how underlying semantic or grammatical arguments (participants, referents) are **expressed at the surface level** of language. It addresses the fundamental question: "When referring to a participant, does the language use a **full noun phrase**, a **pronoun**, a **clitic**, or **nothing at all** (zero/null)?"

**Source**: {tbta-features-2025}: "Surface Realization: Noun, Pronoun, Zero, Clitic"

This feature is **NOT** about:
- Word choice (lexical selection)
- Word order (that's handled separately)
- Voice/valency changes (that's handled by semantic roles)

This feature **IS** about:
- The **form** of nominal reference (NP vs pronoun vs zero vs clitic)
- How participants are **encoded** on the surface
- What **overt material** appears (or doesn't appear) to refer to entities

---

## 2. TBTA Value Inventory

### Values Listed in TBTA Documentation

According to {tbta-features-2025}, TBTA supports the following values:

| Value | Description | Source Citation |
|-------|-------------|----------------|
| **Noun** | Full noun phrase (NP) | {tbta-features-2025} |
| **Pronoun** | Independent pronoun word | {tbta-features-2025} |
| **Zero** | Null/dropped argument | {tbta-features-2025} |
| **Clitic** | Bound pronominal form | {tbta-features-2025} |

**Note**: The TBTA-FEATURES.md document lists these four values explicitly. The DATA-STRUCTURE.md provides additional detail on encoding.

### Character-Based Encoding

According to {tbta-data-structure-2025}, Surface Realization occupies **Position 9** in the 10-position noun code string:

| Position | Feature | Example Values |
|----------|---------|----------------|
| 9 | Surface Realization | N (noun), p (pronoun), P (personal pronoun) |

**Source**: {tbta-data-structure-2025}: "| 9 | Surface Realization | N (noun), p (pronoun), P (personal pronoun) |"

**Observation**: The character encoding shows **three** values (N, p, P), while the feature list shows **four** values (Noun, Pronoun, Zero, Clitic). This suggests:
- "N" = Full Noun
- "p" = Generic pronoun
- "P" = Personal pronoun (subtype)
- Zero is likely encoded by absence or a different mechanism
- Clitic is not shown in this example encoding (may use different code or context-dependent)

**Action Item for Stage 2**: Examine actual TBTA data files to determine:
1. How "Zero" is encoded (null field? special character?)
2. How "Clitic" is distinguished from bound pronouns
3. Whether pronoun subtypes (personal vs other) are consistently distinguished

---

## 3. Gateway Features and Constraints

### What Controls This Feature?

**Gateway Feature**: **Part of Speech** (specifically, applies to Nouns/Noun Phrases)

**Evidence**: Surface Realization appears in Position 9 of the **Noun code** string, not the Verb code string.

**Source**: {tbta-data-structure-2025}: "Example: Noun Codes (10 positions)" - Surface Realization is Position 9

### Scope of Application

Surface Realization applies to:
- **Nouns** (as shown in the 10-position code)
- **Noun Phrases** (referential expressions)
- **Arguments** (subject, object, etc.)

Surface Realization does NOT apply to:
- Verbs (different encoding structure)
- Adjectives/Adverbs (no surface realization dimension)
- Non-referential elements

**Constraint**: This feature is **noun-specific** and tracks how nominal arguments are realized in surface syntax.

---

## 4. TBTA Annotation Policy

### Semantic vs Morphological Priority

**Question**: Does TBTA prioritize semantic meaning over morphological form?

**Answer**: **Context-dependent** - varies by feature and linguistic category.

For Surface Realization specifically:
- **Morphological form** appears to be primary (Noun vs Pronoun vs Zero vs Clitic is a **surface** distinction)
- **Semantic content** (what the referent is) is handled by other features (Participant Tracking, Noun List Index)

**Evidence**: The feature is called "Surface **Realization**" - emphasis on how something is **realized** (expressed), not what it **means**.

### Part-of-Speech Rules

**Question**: Do pronouns vs nouns follow different logic?

**Answer**: Surface Realization **tracks** this distinction. The values themselves (Noun vs Pronoun) encode the POS choice.

**Implication**: This feature is **descriptive** of the surface choice already made, not **prescriptive** about which to use.

---

## 5. Example Languages

According to {tbta-features-2025}, the following example languages are listed for Surface Realization:

| Language | Family | Relevance |
|----------|--------|-----------|
| **Spanish** | Romance (Indo-European) | Pro-drop language; allows null subjects |
| **Japanese** | Japonic | Topic-prominent; extensive zero anaphora |
| **Italian** | Romance (Indo-European) | Pro-drop language; rich verb agreement |

**Source**: {tbta-features-2025}: "Surface Realization | Noun, Pronoun, Zero, Clitic | Spanish, Japanese, Italian"

**Analysis**: These three languages represent **diverse surface realization strategies**:
1. **Spanish/Italian**: Pro-drop with rich verbal inflection
2. **Japanese**: Radical pro-drop (subject and object) without inflection

This suggests TBTA chose languages with **high variation** in surface realization to illustrate the feature's necessity.

---

## 6. Past Learnings and Policy Evolution

### What Has TBTA Learned?

**Status**: {tbta-features-2025} marks Surface Realization as "✅ Complete"

This indicates:
- TBTA has **finished** annotating this feature across their corpus
- Policy is **stable** (not under active revision)
- Data generation and validation are **complete**

### Best Practices (Inferred)

From the complete status, we infer:
1. **Clear decision criteria** exist for distinguishing Noun/Pronoun/Zero/Clitic
2. **Annotator consistency** has been achieved
3. **Edge cases** have been resolved

**Action Item for Stage 2**: Review TBTA's actual annotated data to discover:
- How they handle ambiguous cases
- Whether they distinguish pronoun subtypes consistently
- How clitics are identified (phonological? syntactic?)

---

## 7. Edge Cases and Special Considerations

### Known Edge Cases

Based on linguistic literature and TBTA's scope, potential edge cases include:

#### 7.1 Clitic vs Affix

**Challenge**: How to distinguish bound pronouns (clitics) from verbal agreement morphology?

- **Clitics**: Phonologically bound but syntactically independent (e.g., Romance object clitics)
- **Affixes**: Morphologically integrated (e.g., Bantu subject prefixes)

**TBTA Approach**: Not explicitly documented in available sources.

**Hypothesis**: TBTA likely considers:
- **Clitics** = Can move or appear in different positions
- **Affixes** = Fixed to verb template

#### 7.2 Zero vs Implicit

**Challenge**: When is a referent "zero" vs "implicit" vs "inferable from context"?

**TBTA Context**: TBTA has a separate **Implicit Flag** feature (Tier B) for phrases and clauses.

**Distinction**:
- **Zero (Surface Realization)**: Grammatically licensed null argument
- **Implicit (Implicit Flag)**: Semantically inferable but not syntactically active

**Example**:
- "It's raining" - expletive "it" is **overt**, not zero
- Spanish "_Llueve_" (rains) - subject is **zero**, not implicit

#### 7.3 Pro-drop vs Null Anaphora

**Distinction**:
- **Pro-drop**: Language allows subject/object to be null when recoverable
- **Null anaphora**: Specific discourse-based dropping of referents

**TBTA Approach**: Surface Realization likely tracks **all** zeros, regardless of licensing mechanism.

#### 7.4 Demonstratives and Pronouns

**Challenge**: Are demonstratives (this, that) considered "pronouns" or "nouns"?

**Linguistic Consensus**: Demonstratives pattern with pronouns when used alone, with determiners when modifying nouns.

**TBTA Approach**: Not explicitly stated.

**Action Item for Stage 2**: Check whether TBTA codes demonstrative pronouns as "Pronoun" or distinguishes them.

#### 7.5 Null Possessors

**Example**: "I saw **his** car" - possessor is pronominal
vs. "I saw **the** car" - possessor is null/implicit

**Question**: Does Surface Realization apply to **embedded** possessors, or only to clause-level arguments?

**Hypothesis**: TBTA likely applies Surface Realization to **all nominal positions** where participants appear, including possessors.

---

## 8. Theoretical vs Productive Values

### All Values Are Productive

All four values (Noun, Pronoun, Zero, Clitic) are **productive** across languages:

| Value | Productivity | Evidence |
|-------|-------------|----------|
| **Noun** | Universal | All languages have full NPs |
| **Pronoun** | Universal | All languages have pronouns |
| **Zero** | ~70% of languages | Pro-drop is majority typologically {wals-2013} |
| **Clitic** | ~40% of languages | Common in Romance, Slavic, many others |

**Source for typology**: Cross-linguistic data from WALS Feature 101A (to be detailed in Stage 2).

**Implication**: All four values are **expected** to appear frequently in TBTA's annotated corpus.

---

## 9. Mixed Annotations

### Can Multiple Values Co-occur?

**Question**: Can a single constituent have multiple Surface Realization values simultaneously?

**Answer**: **No** - Surface Realization is **mutually exclusive**.

**Reasoning**:
- A referent is **either** a full NP **or** a pronoun **or** zero **or** a clitic
- These are **alternative encodings** of the same underlying argument
- Unlike features like "Degree" (which can be mixed: Intensified + 'too'), Surface Realization is a **single choice**

**Exception**: Clitic doubling constructions

#### Clitic Doubling Edge Case

In some languages (Spanish, Romanian, Albanian), a clitic **co-occurs** with a full NP:

**Spanish Example**:
```
Lo    vi       a  Juan
him   I-saw   to Juan
"I saw Juan"
```

Here, both **clitic** ("lo") and **full NP** ("Juan") appear.

**TBTA Handling**: Unknown from available documentation.

**Hypotheses**:
1. **Option A**: Mark the NP as "Noun" and the clitic as "Clitic" (two separate annotations)
2. **Option B**: Mark the NP as "Clitic-doubled" (mixed annotation)
3. **Option C**: Mark the NP as "Noun" and ignore the clitic (treat as verbal morphology)

**Action Item for Stage 2**: Examine Spanish corpus data to determine TBTA's approach.

---

## 10. Relationship to Other TBTA Features

### Related Features

Surface Realization interacts with several other TBTA features:

#### 10.1 Participant Tracking (Tier A)

**Relationship**: Participant Tracking indicates **discourse status** (First Mention, Routine, Restaging), which often **predicts** Surface Realization choice.

**Correlation**:
- **First Mention** → typically **Noun** (full NP)
- **Routine** → often **Pronoun** or **Zero**
- **Restaging** → typically **Noun** (reintroduce with full NP)

**Source**: Discourse literature (Givón 1983, Lambrecht 1994) + TBTA implementation

#### 10.2 Noun List Index (Tier A)

**Relationship**: Noun List Index tracks **coreference** (which mentions refer to the same entity).

**Interaction**: Surface Realization specifies **how** an entity is mentioned; Noun List Index specifies **which** entity is mentioned.

**Example**:
- "**John** went home. **He** ate dinner."
  - "John" = Surface Realization: **Noun**, Noun List Index: **1**
  - "He" = Surface Realization: **Pronoun**, Noun List Index: **1** (same entity)

#### 10.3 Person System (Tier A)

**Relationship**: Person (1st, 2nd, 3rd) is relevant primarily for **Pronouns**, not full Nouns.

**Constraint**:
- If Surface Realization = **Pronoun**, then Person must be specified
- If Surface Realization = **Noun**, then Person is usually 3rd (or N/A for generic)

#### 10.4 Proximity System (Tier A)

**Relationship**: Proximity (near speaker, near listener, remote) applies to **demonstratives**.

**Interaction**:
- Demonstrative pronouns ("this", "that") have both Surface Realization = **Pronoun** and Proximity value
- Demonstrative determiners ("this car") modify a Noun

---

## 11. Data Structure and Parsing

### Position in Noun Code

**Position**: 9 out of 10
**Format**: Single character

**Source**: {tbta-data-structure-2025}: "| 9 | Surface Realization | N (noun), p (pronoun), P (personal pronoun) |"

### Example Encoding

**Hypothetical Noun Code**: `MSN1IAN--3`

Breaking down position 9 (the 9th character):
- Position 1: M (Masculine)
- Position 2: S (Singular)
- Position 3: N (Nominative case)
- Position 4: 1 (Noun List Index = 1)
- Position 5: I (First Mention)
- Position 6: A (not specified in example)
- Position 7: N (not specified in example)
- Position 8: - (not specified)
- **Position 9: -** (not specified - would be N/p/P)
- Position 10: 3 (Third person)

**Note**: Actual encoding may vary; this is illustrative based on documentation.

---

## 12. Summary of TBTA Policy

### Key Takeaways

1. **Four Values**: Noun, Pronoun, Zero, Clitic
2. **Tier A Feature**: Essential for 1000+ languages
3. **Complete Status**: TBTA has finished annotating this feature
4. **Noun-Specific**: Applies to nominal arguments (Position 9 of Noun codes)
5. **Mutually Exclusive**: One value per referent (except possible clitic doubling)
6. **Surface-Based**: Tracks morphological form, not semantic content
7. **Example Languages**: Spanish, Japanese, Italian (diverse pro-drop strategies)

### Open Questions for Stage 2

1. How does TBTA encode "Zero" in the character string? (Empty position? Special char?)
2. How are clitics distinguished from affixes? (Phonological? Syntactic criteria?)
3. Does TBTA distinguish pronoun subtypes consistently? (Personal vs demonstrative vs interrogative?)
4. How are clitic doubling constructions handled? (Separate annotations? Mixed?)
5. What criteria determine "Pronoun" vs "Clitic"? (Movement? Prosody? Morphology?)
6. Does Surface Realization apply to embedded possessors, or only clause-level arguments?

---

## 13. Discrepancies and Notes

### Documentation Inconsistencies

#### Inconsistency 1: Number of Values

- **TBTA-FEATURES.md** lists: "Noun, Pronoun, Zero, Clitic" (4 values)
- **DATA-STRUCTURE.md** lists: "N (noun), p (pronoun), P (personal pronoun)" (3 values, no Zero or Clitic)

**Assessment**: The character encoding example may be **incomplete** or **simplified**. Full documentation likely exists in the TBTA database schema (not yet accessed).

**Resolution**: Treat the **TBTA-FEATURES.md** list as authoritative (4 values). Assume encoding uses additional characters or mechanisms for Zero/Clitic.

#### Inconsistency 2: Pronoun Subtypes

- **DATA-STRUCTURE.md** distinguishes "p (pronoun)" vs "P (personal pronoun)"
- **TBTA-FEATURES.md** does not mention pronoun subtypes

**Assessment**: TBTA may track pronoun types (personal, demonstrative, interrogative, etc.) as **subtypes** of the broader "Pronoun" value.

**Resolution**: Assume "Pronoun" is the **primary value**, with possible subtypes (to be confirmed in Stage 2).

---

## 14. Citation Codes

All sources referenced in this document:

| Citation Code | Full Reference |
|---------------|----------------|
| {tbta-features-2025} | `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md` (2025-11-14) |
| {tbta-data-structure-2025} | `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md` (2025-11-14) |
| {tbta-readme-2025} | `/workspace/bible-study-tools/tbta/tbta-source/README.md` (2025-11-14) |

**External sources** (to be cited in SCHOLARLY.md):
- {wals-2013} = Dryer (2013), WALS Feature 101A: Expression of Pronominal Subjects
- {givon-1983} = Givón, T. (1983), Topic Continuity in Discourse
- {lambrecht-1994} = Lambrecht, K. (1994), Information Structure and Sentence Form

---

**End of TBTA Documentation Review**
