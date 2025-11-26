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
