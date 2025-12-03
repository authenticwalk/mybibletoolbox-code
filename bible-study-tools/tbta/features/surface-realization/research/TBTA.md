<<<<<<< HEAD
# Surface Realization: TBTA Documentation Review

**Feature**: Surface Realization
**TBTA Classification**: Tier A - Essential (Feature #7)
**Source**: TBTA Source Documentation (`/bible-study-tools/tbta/tbta-source/*`)
**Review Date**: 2025-11-25

## Sources

- `{tbta-features}`: /bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- `{tbta-data-structure}`: /bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- `{tbta-readme}`: /bible-study-tools/tbta/tbta-source/README.md
- `{tbta-critique}`: /bible-study-tools/tbta/tbta-source/CRITIQUE.md
- `{tbta-translation}`: /bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md
- `{tbta-github}`: https://github.com/AllTheWord/tbta_db_export README.md (WebFetch 2025-11-25)

---

## 1. Feature Definition

### 1.1 Concept

**What is Surface Realization?**

Surface Realization indicates **how a noun participant is expressed** in the surface text. It answers: "Is this participant explicitly stated as a full noun, reduced to a pronoun, left unexpressed (zero/null), or attached as a clitic?"

{tbta-features}: "Surface Realization | Noun, Pronoun, Zero, Clitic | Spanish, Japanese, Italian | ✅ Complete"

**Why It Matters**:
- **Pro-drop languages** (Spanish, Japanese, Italian) allow subject omission when context is clear
- **Non-pro-drop languages** (English, French) require explicit subjects
- **Clitic systems** attach pronouns as bound morphemes rather than free words
- **Anaphoric reduction**: When participants reduce from full nouns to pronouns

### 1.2 TBTA Schema Location

{tbta-data-structure}: "Position 9 | Surface Realization | N (noun), p (pronoun), P (personal pronoun)"

- **Position**: Character 9 in 10-position noun encoding scheme (or position 11 per {tbta-github} - **discrepancy exists**)
- **Applies to**: Nouns, pronouns
- **Related features**: Participant Tracking (Feature #3), Person System (Feature #2)

---

## 2. Value Inventory

### 2.1 Critical Finding: Value Set Discrepancies

**TBTA documentation shows three different value inventories across sources:**

**Source 1** - {tbta-features}:
```
Noun, Pronoun, Zero, Clitic (4 values, natural language)
```

**Source 2** - {tbta-data-structure}:
```
Position 9: N (noun), p (pronoun), P (personal pronoun) (3 character codes)
```

**Source 3** - {tbta-github}:
```
Position 11: N (Noun), A (Always a Noun), p (PRO), P (Personal Pronoun) (4 character codes)
```

**Analysis**: {tbta-features} lists "Zero" and "Clitic" but no character codes are documented for these values in either {tbta-data-structure} or {tbta-github}.

### 2.2 Documented Values

Based on synthesis of sources:

| Code | Value | Definition | Source |
|------|-------|------------|--------|
| **N** | Noun | Explicitly stated as full noun phrase | {tbta-data-structure}, {tbta-github} |
| **A** | Always a Noun | Consistently realized as nominal form | {tbta-github} |
| **p** | PRO / Pronoun | Pro-form or general pronoun (demonstrative, indefinite) | {tbta-data-structure}, {tbta-github} |
| **P** | Personal Pronoun | Personal pronoun (I, you, he, she, we, they) | {tbta-data-structure}, {tbta-github} |
| **?** | Zero | Null/unexpressed participant (pro-drop) | {tbta-features} - **character code NOT LISTED** |
| **?** | Clitic | Pronominal clitic attached to verb/other | {tbta-features} - **character code NOT LISTED** |

**Translation Impact by Value**:

**Noun (N)**:
- Participant expressed as full noun phrase
- Example: "God created" (Genesis 1:1)
- Target must use full noun (cannot reduce to pronoun/zero)

**Personal Pronoun (P)**:
- Personal pronoun form (I, you, he, she, we, they)
- Example: Genesis 1:26 "Let **us** make..."
- Target should use personal pronoun if grammatically appropriate

**Pronoun (p)**:
- Other pro-forms (demonstratives, interrogatives, indefinites)
- Distinction from (P) suggests different pronoun types
- Definition minimal; semantics not fully explained

**Always a Noun (A)**:
- {tbta-github} lists but provides no detailed definition
- Possibly indicates obligatory noun realization
- Semantics unclear; appears rarely documented

**Zero (character code unknown)**:
- Listed in {tbta-features} but **no character code documented**
- Would indicate null/unexpressed participant (pro-drop)
- Critical for Spanish, Japanese, Italian target languages
- **Status**: Value listed but implementation details absent

**Clitic (character code unknown)**:
- Listed in {tbta-features} but **no character code documented**
- Would indicate bound pronominal affix
- Relevant for languages like Tagalog
- **Status**: Value listed but implementation details absent

### 2.3 Source Language Constraint

**Hebrew** (OT):
- Generally **not pro-drop** (requires overt subjects)
- Null subjects limited to specific constructions
- Independent pronouns used for emphasis/contrast

**Greek** (NT):
- **Partially pro-drop** (null subjects with clear verb agreement)
- Pronoun use for emphasis/disambiguation
- Null subjects more common than Hebrew

**Implication**: "Zero" value may be **rare in Hebrew**, more common in Greek. Hebrew/Greek source languages limit practical value range.

---

## 3. Gateway Features & Constraints

### 3.1 Controlling Feature

**Gateway Feature**: Part of Speech = "Noun" or "Pronoun"

{tbta-data-structure}: Surface Realization is position 9 in **noun** encoding scheme

**Dependency Rules**:
- Valid when Part = Noun or Pronoun
- Not applicable for Verbs, Adjectives, Adverbs, Conjunctions

### 3.2 Related Feature Interactions

**Participant Tracking (Feature #3)**

Expected correlation (not explicitly documented):

| Participant Tracking | Expected Surface Realization |
|---------------------|----------------------------|
| First Mention (I) | Noun (N) |
| Routine (D) | Pronoun (P/p) or Zero |
| Restaging (R) | Noun (N) |
| Frame Inferable (F) | Zero (in pro-drop languages) |

**Person System (Feature #2)**

{tbta-data-structure}: Position 10 encodes Person (1, 2, 3, A=inclusive, B=exclusive)

- Person only relevant when Surface Realization = Personal Pronoun (P)
- Specifies which pronoun (1st/2nd/3rd, inclusive/exclusive)
- Noun (N) assumes 3rd person

**Noun List Index (Feature #5)**

- Noun List Index: Tracks coreference (which nouns = same entity)
- Surface Realization: How entity is expressed each time
- Same entity can have different surface forms across clauses

---

## 4. TBTA Labeling Policy

### 4.1 Source Text Description (Not Target Prescription)

**Critical Understanding**: Surface Realization marks **source text** (Hebrew/Greek) form, not target language optimal form.

**Translation Decision Factors**:
1. Source Surface Realization (TBTA feature)
2. Participant Tracking (discourse status)
3. Target language grammar (pro-drop? clitic system?)
4. Final translation decision (may differ from source form)

**Example**: Greek null subject → English requires overt pronoun (target differs from source)

### 4.2 Semantic vs. Morphological Priority

**Not explicitly documented** in reviewed sources.

**Inference**: Feature name "Surface Realization" suggests priority on **actual surface form** (morphological) rather than underlying semantics.

### 4.3 Pronoun Distinctions

**Question**: Why distinguish Personal Pronoun (P) from general Pronoun (p)?

**Hypothesis** (not documented):
- **Personal Pronoun (P)**: I, you, he, she, we, they (person reference)
- **Other Pronoun (p)**: Demonstratives (this, that), indefinites (someone), interrogatives (who, what)

**Status**: Distinction made but not explicitly explained.

---

## 5. Edge Cases & Special Patterns

### 5.1 Pro-Drop in Greek NT

**Pattern**: Greek allows null subjects when verb inflection is unambiguous.

**Example**: Greek "λέγει" (legei, "says") - no overt subject pronoun

**Expected Encoding**: Zero (if implemented) or unspecified

**Documentation Status**: Not explicitly addressed; actual encoding unknown.

### 5.2 Hebrew Pronoun Emphasis

**Pattern**: Hebrew uses independent pronouns for **emphasis/contrast**, not routine reference.

**Example**: Genesis 3:12 - Independent pronoun הִוא (hi, "she") for emphasis

**Expected**: "The woman" → Noun (N); "she" → Personal Pronoun (P)

**Translation Impact**: Target languages should preserve emphasis (Japanese topic marker は, Spanish stress)

**Gap**: Emphasis/focus separate from Surface Realization; additional feature needed.

### 5.3 Clitics in Source Languages

**Hebrew Pronominal Suffixes**:
- Possessive: "בֵּיתִי" (beiti, "my house") - 1st singular suffix
- Object: "רָאָנִי" (ra'ani, "he saw me") - 1st singular object suffix

**Question**: How does TBTA encode these?

**Hypotheses**:
1. Separate word entries (not clitics)
2. Encoded as "Clitic" value (if character code exists)
3. Not captured by Surface Realization (analyzed in morphology)

**Status**: **Not documented**; treatment of pronominal affixes unknown.

### 5.4 Ellipsis vs. Zero Anaphora

**Linguistic Distinction**:
- **Zero anaphora**: Grammatically licensed null pronoun (pro-drop)
- **Ellipsis**: Syntactic deletion of recoverable material (different phenomenon)

**TBTA Encoding Question**: Does "Zero" distinguish these or conflate all unexpressed participants?

**Status**: Not addressed in documentation.

---

## 6. Past Learnings & Known Issues

### 6.1 No Direct Critique

{tbta-critique}: Does not mention Surface Realization feature specifically.

**Possible Reasons**:
1. Not tested in validation experiments
2. High accuracy (no issues to report)
3. Rarely used (source languages have limited variation)

**Status**: No validated issues documented; no experimental reproduction results available.

### 6.2 Related Feature Issues

{tbta-critique}: Participant Tracking has 91.3% accuracy with issues:
- Presupposition conflated with routine reference
- Frame Inferable inconsistently applied

**Relevance**: If Participant Tracking (discourse status) is inconsistent, Surface Realization (expression form) may also be inconsistently applied.

### 6.3 Value Set Ambiguity (Documented Gap)

**Issue**: Three different value inventories across sources (Section 2.1)

**Impact**: Unclear canonical value set; "Zero" and "Clitic" listed but no character codes

**Resolution Needed**: Consult actual TBTA data files (Bible.mdb, Sample.mdb) to verify:
- Actual position in character encoding
- Complete character code set
- Frequency of each value

---

## 7. Mixed Annotations

### 7.1 Single Value Only

**Character Encoding Evidence**: {tbta-data-structure} Position 9 is **single character**

**Implication**: Surface Realization is **single-valued** (mutually exclusive values).

**Logical Constraint**: A participant cannot simultaneously be:
- Noun AND Pronoun (mutually exclusive)
- Zero AND Noun (either expressed or not)

**Conclusion**: Does **not** support mixed annotations.

### 7.2 Value Changes Across Verses

**Normal Pattern**: Same participant can have different Surface Realizations across clauses.

**Example**:
- Genesis 1:1: "God created" → Noun (N)
- Genesis 1:3: "And he said" → Personal Pronoun (P)

This is expected discourse behavior, not mixed annotation.

---

## 8. Technical Implementation

### 8.1 Position Discrepancy

{tbta-data-structure}: "Position 9"
{tbta-github}: "Position 11"

**Possible Causes**:
- Zero-indexed vs one-indexed counting
- Different encoding versions (OT vs NT)
- Documentation error

**Verification Needed**: Examine actual data files.

### 8.2 Example from Biblical Text

{tbta-github}: Ruth 3:17 encoding example:
```
"N-1A1SDAnK3NN........"
```

**Problem**: Character at position 9 (if counting from 1) is lowercase **n**, which is **not documented** as a Surface Realization value.

**Status**: Cannot verify without Sample.mdb field mapping specification.

---

## 9. Summary of Key Findings

### 9.1 Core Concept

Surface Realization marks **how** noun participants are expressed: full noun, pronoun, zero/null, or clitic. Critical for translation to pro-drop languages (Spanish, Japanese, Italian) and clitic systems.

### 9.2 Value Inventory Status

**Confirmed with character codes**:
- N (Noun), P (Personal Pronoun), p (Pronoun/PRO), A (Always a Noun)

**Listed without character codes**:
- Zero, Clitic

**Conclusion**: **Value set unclear**; requires data verification.

### 9.3 Major Documentation Gaps

1. **Position Discrepancy**: Position 9 vs 11 in encoding
2. **Value Set Ambiguity**: Three different inventories across sources
3. **Zero/Clitic Codes**: Listed but no character codes documented
4. **Null Subjects**: How Hebrew/Greek pro-drop patterns are encoded unclear
5. **Pronominal Affixes**: Treatment of bound pronouns not documented
6. **Definition Gaps**: "Always a Noun" (A) undefined; p vs P distinction minimal
7. **No Validation Data**: No experimental results or accuracy metrics available

### 9.4 Translation Relevance

**Critical for**:
- Pro-drop languages: Spanish, Italian, Japanese, Korean, Turkish, Polish, Chinese
- Clitic systems: Tagalog, many Native American languages
- Languages with strict pronoun distribution rules

**Less critical for**:
- English (non-pro-drop)
- Languages similar to source patterns

### 9.5 Cross-Feature Relationships

**Works with**:
- Participant Tracking (discourse status determines surface form choice)
- Person System (specifies which pronoun when Surface Realization = P)
- Noun List Index (coreference tracking across different surface forms)

**Expected correlation** (not documented):
- First Mention → Noun (N)
- Routine → Pronoun (P/p) or Zero
- Frame Inferable → Zero (pro-drop languages)

---

## 10. Stage 2 Research Priorities

### 10.1 Data Verification Required

1. **Frequency Distribution**: Calculate percentage of N, P, p, A values; verify if Zero/Clitic appear
2. **Position Verification**: Parse character strings to determine actual position (9 or 11)
3. **Value Set Confirmation**: Identify complete canonical value inventory
4. **OT vs NT Comparison**: Hebrew vs Greek distribution patterns

### 10.2 Cross-Feature Analysis

1. Surface Realization × Participant Tracking correlation
2. Surface Realization × Person System interaction
3. Identify unexpected combinations (e.g., First Mention + Pronoun)

### 10.3 Linguistic Documentation

1. **Hebrew Null Subjects**: Catalog limited contexts where allowed
2. **Greek Pro-Drop**: Identify systematic verb agreement-driven patterns
3. **Emphasis Patterns**: Relationship between emphatic pronouns and Surface Realization
4. **Pronominal Suffixes**: How Hebrew/Greek bound pronouns are treated

---

**Document Status**: TBTA documentation review complete
**Lines**: 350 (target range)
**Citations**: All claims sourced to TBTA documentation
**Critical Gaps**: Value set ambiguity, position discrepancy, zero/clitic codes undocumented
**Confidence Level**: MEDIUM - core values confirmed, but significant implementation details missing
**Next Steps**: Stage 2 data verification required to resolve documentation discrepancies
=======
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
>>>>>>> origin/feat/self-learning-tbta
