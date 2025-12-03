<<<<<<< HEAD
# TBTA Documentation Review: Degree Feature

**Date**: 2025-11-25
**Status**: Section 1 (TBTA Documentation Review) - Complete

---

## 1. Concept Definition

**Sources**: TBTA-FEATURES.md {tbta-features:21,30-31,74,83-84,121}, features-archive {degree-archive}

**Definition**: Degree marks comparison ("more than"), superlatives ("most"), and intensification ("very") on adjectives, adverbs, and verbs. Expresses gradation via morphological (suffixes -er/-est) or analytic (separate words "more"/"most") constructions.

**Applies to**: Adjectives (primary), Adverbs (secondary), Verbs (tertiary - via adjectival modification)

---

## 2. Values Supported by TBTA

### Complete Value Inventory by Part of Speech

**Sources**: DATA-STRUCTURE.md {data-structure:73}, GitHub export {github-export}, validation {degree-readme:17-44}

| Code | Value | Adj | Adv | Verb | Status |
|------|-------|-----|-----|------|--------|
| N | No Degree | ✓ | ✓ | ✓ | ✅ Confirmed |
| C | Comparative | ✓ | ✓ | ✓ | ✅ Confirmed |
| S | Superlative | ✓ | ✓ | ✓ | ✅ Confirmed |
| I/V | Intensified | I | V | I | ✅ Confirmed |
| E | Extremely Intensified | ✓ | ✓ | ✓ | ❌ Likely non-existent |
| T | 'too' (excessive) | ✓ | ✓ | ✓ | ❓ Uncertain, rare |
| L | 'less' | ✓ | ✓ | ✓ | ❓ Uncertain |
| l | 'least' | ✓ | ✓ | ✓ | ❓ See literal encoding |
| q | Equality ("as...as") | ✓ | - | - | ❌ Non-existent |
| i | Intensified Comparative | ✓ | - | - | ❌ Non-existent |
| s | Superlative of 2 items | ✓ | - | - | ❌ Non-existent |

**Note**: Adverbs use "V" instead of "I" for intensified. Verbs use field name "Adjective Degree:".

### Dual Value Encoding System

**Source**: {degree-readme:39-44}

TBTA uses **TWO encoding formats**:
1. **Standardized**: "No Degree", "Comparative", "Superlative", "Intensified"
2. **Literal quoted**: `'''least'''` (MAT 5:19), triple single quotes in YAML

**Implication**: Validation must handle both encoding types.

### Confirmed vs. Non-Existent Values

**Observed in actual data** {degree-annotations}:
- ✅ "No Degree", "Comparative", "Superlative", "Intensified", `'''least'''`

**Confirmed non-existent** {degree-readme}:
- ❌ q, i, s (adjective-only theoretical values absent from Biblical texts)

---

## 3. Gateway Features (Constraints)

**Sources**: GitHub export {github-export}, validation {degree-readme:194-207}

### Primary Constraints

**1. Part of Speech** - Determines available values (see table in §2)

**2. Gradability Constraint** (Universal Principle 9) {degree-readme:204-207}
- **Gradable**: "great", "small", "good", "early" → Can have degree
- **Non-gradable**: "justified", "dead", "perfect" → Always "No Degree"
- **Test**: Can you say "very X"? If no → not gradable
- **Example**: LUK 18:14 δεδικαιωμένος (justified) = "No Degree" despite comparative structure
- **Rule**: PREREQUISITE check (RULE 0 in Algorithm v2.0)

**3. Lexical vs. Syntactic Distinction** (Universal Principle 7) {degree-readme:194-198}
- **Syntactic** (2 words): λίαν πρωῒ "very early" → "Intensified" ✓
- **Lexical** (1 word): ὑπερεκπερισσοῦ "abundantly" → "No Degree" ✓
- **Rule**: Only syntactic modifiers get degree marking, not lexical compounds

**4. No other gateway features documented** (unlike Mood → Aspect in other features)

---

## 4. TBTA Policy: Semantic vs. Morphological

**Sources**: Validation {degree-readme:189-192,365-378}, past learnings {degree-learnings:10-14}, annotations {degree-annotations:187-192}

### Semantic Over Morphological (Universal Principle 1)

**Core policy**: TBTA prioritizes semantic meaning in context over morphological form.

**Examples**:
1. **MAT 22:36**: μεγάλη (positive) + superlative question → **"Superlative"**
2. **MAT 22:38**: μεγάλη (positive) + answer to superlative → **"Superlative"**
3. **MAT 11:11**: μείζων (comparative) + "no one greater" → **"Superlative"**

**Pattern**: ¬∃y(y > X) ≡ X is maximum (negative comparative = implied superlative)

### Implied Superlatives (RULE 1)

**Patterns TBTA recognizes**:
- "No one greater than X" → Superlative
- Universal quantifier + comparative → Superlative
- Negative + comparative → Superlative

**Rule**: Check for these patterns BEFORE defaulting to morphological form.

### Target vs. Source Language

**Policy**: TBTA annotates the **target language's expression**, not source language form.
- Greek synthetic comparative may → English analytic comparative
- Hebrew periphrastic → Spanish morphological
- Annotation reflects translation, not source

### Field Names by Part of Speech

| Part of Speech | Field Name | Example Values |
|----------------|------------|----------------|
| Adjective | `Degree:` | "No Degree", "Superlative" |
| Adverb | `Degree:` | "No Degree", "Intensified" |
| Verb | `Adjective Degree:` | "No Degree" |

---

## 5. Past Learnings

**Sources**: features-archive {degree-readme:1-185}, {degree-annotations:9-22}

### Previous Implementation Results

**Status**: Phase 8 Complete - Algorithm v2.0 validated
**Accuracy**: 42.9% (v1.0) → ~71% expected (v2.0)
**Training**: 4 verses (MAT 22:36, MAT 22:38, MRK 1:35, GEN 1:1)
**Testing**: 7 adversarial verses (4 books unavailable: JHN 15, HEB, SNG)

### Four Critical Algorithm Errors (All Algorithmic, Not TBTA Errors)

| # | Verse | Issue | Fix in v2.0 |
|---|-------|-------|-------------|
| 1 | MAT 11:11 | Missed implied superlative | RULE 1: Negative comparative patterns |
| 2 | EPH 3:20 | Lexical vs syntactic confusion | RULE 4: Check word boundaries |
| 3 | MAT 5:19 | Unknown literal encoding | Step 5: Handle dual encoding |
| 4 | LUK 18:14 | No gradability check | RULE 0: Gradability prerequisite |

### Universal Principles Discovered

1. **Semantic Over Morphological** - Context overrides form
2. **Lexical vs. Syntactic** - Only syntactic modifiers get degree
3. **Dual Value Encoding** - Standardized + literal formats
4. **Gradability Constraint** - Non-gradable words = "No Degree"

### Data Availability

**Complete TBTA export**: 30/66 books (46% coverage)
**Impact**: Limited validation to available books; OT books SNG, prophets missing

---

## 6. Edge Cases

**Sources**: features-archive {degree-learnings:256-371}, {degree-readme:35-37,89-91,438-446}

### 6.1 Degree-Neutral Languages

**Languages**: Motu, Fijian, Washo, Warlpiri
**Approach**: Use conjoined comparison ("X big, Y small"), not C/S codes
**Rule**: If target is degree-neutral, do NOT use comparative/superlative codes

### 6.2 Elative vs. Relative Superlative

**Elative** (intensive, no comparison): Spanish "buenísimo" → Code **E**
**Relative** (actual comparison): Spanish "el más bueno" → Code **S**
**Distinction**: Definite article + comparison set indicates relative

### 6.3 Excessive vs. Intensive

**Excessive** (negative): "too tall" (implies problem) → Code **T**
**Intensive** (positive): "extremely tall" → Code **E**
**Test**: Does it imply negative consequence?

### 6.4 Comparative Subtypes (Theoretical - Not in Biblical Texts)

**Comparative of 2** ("the taller of the two") → Theoretical **s**, but non-existent in data
**Intensified comparative** ("much more beautiful") → Theoretical **i**, but non-existent in data
**Actual practice**: Use standard **C** (Comparative)

### 6.5 Positive Form with Comparative Meaning

**Hebrew**: Adjective + מִן (min) → Comparative despite positive morphology
**Rule**: Annotate construction, not form

### 6.6 Reduplication

**Languages**: Indonesian, Tagalog use reduplication for intensification
**Full reduplication** → **E** (Extremely Intensified)
**Partial reduplication** → **I** (Intensified)

### 6.7 Equative vs. Similative

**Equative** ("as tall as" - degree comparison) → Theoretical **q**, but non-existent in Biblical texts
**Similative** ("like a deer" - manner/resemblance) → **N** (No Degree)
**Actual practice**: Use **N** (No Degree)

---

## 7. Value Inventory

**Sources**: GitHub export {github-export}, validation {degree-readme:17-76}

### Complete Inventory (Theoretical vs. Actual)

| Code | Value | Theoretical | Confirmed in Data | Status |
|------|-------|-------------|-------------------|--------|
| N | No Degree | ✓ | ✓ | ✅ ~70% of cases |
| C | Comparative | ✓ | ✓ | ✅ ~15% of cases |
| S | Superlative | ✓ | ✓ | ✅ ~5% of cases |
| I/V | Intensified | ✓ | ✓ | ✅ ~5% of cases |
| `'''least'''` | Literal downward | - | ✓ | ✅ Dual encoding |
| E | Extremely Intensified | ✓ | ✗ | ❌ Likely non-existent |
| T | 'too' (excessive) | ✓ | ? | ❓ Rare, uncertain |
| L | 'less' | ✓ | ? | ❓ Uncertain |
| l | 'least' | ✓ | See literal | ❓ Use `'''least'''` |
| q | Equality | ✓ | ✗ | ❌ Non-existent |
| i | Intensified Comparative | ✓ | ✗ | ❌ Non-existent |
| s | Superlative of 2 | ✓ | ✗ | ❌ Non-existent |

**Key finding**: Schema documents 11 theoretical values, but only 5 confirmed in Biblical texts.

### Source Language Patterns

- **Greek NT**: Synthetic forms common (μείζων, μέγιστος)
- **Hebrew OT**: Exclusively periphrastic (מִן construction, no morphology)
- **Epistles**: Higher intensification frequency
- **Narrative**: More base forms, occasional comparative

---

## 8. Mixed Annotations

**Search results**: Not explicitly documented in TBTA source.

**Conclusion from dual encoding system** {degree-readme:39-44,54}:
- Each constituent receives ONE degree value (not multiple)
- Encoding format varies: standardized ("Superlative") OR literal (`'''least'''`)
- No mixed annotations documented for Degree feature

---

## 9. Summary

### Confirmed Implementation

1. **Values used**: "No Degree", "Comparative", "Superlative", "Intensified", `'''least'''`
2. **Dual encoding**: Standardized + literal formats
3. **Semantic priority**: Context overrides morphology
4. **Syntactic only**: Only syntactic modifiers get degree
5. **Gradability required**: Non-gradable = "No Degree"

### Schema vs. Reality

- **Theoretical**: 11 values (adjectives)
- **Actual**: 5 confirmed values
- **Non-existent**: q, i, s (absent from Biblical texts)
- **Uncertain**: E, T, L (need more data)

### Critical Algorithm Requirements

1. **RULE 0**: Gradability check (prerequisite)
2. **RULE 1**: Implied superlatives (negative comparative)
3. **RULE 4**: Syntactic vs. lexical (word boundaries)
4. **Step 5**: Dual encoding (standardized + literal)

### Validation Accuracy

- v1.0: 42.9% (3/7 correct)
- v2.0: ~71% expected (4 major fixes)
- All errors: Algorithmic, not TBTA annotation errors

---

## 10. Sources

### Primary TBTA Sources

- **{tbta-features}**: TBTA-FEATURES.md
- **{data-structure}**: DATA-STRUCTURE.md
- **{github-export}**: https://github.com/AllTheWord/tbta_db_export

### Archive Sources

- **{degree-archive}** / **{degree-readme}**: features-archive/degree/README.md
- **{degree-learnings}**: features-archive/degree/LEARNINGS.md
- **{degree-annotations}**: features-archive/degree/experiments/training/TBTA-ANNOTATIONS.md

---

**Document Status**: Complete (Section 1 TBTA Documentation Review)
**Lines**: 283
**Confidence**: High - all statements cited
**Limitations**: Some values unconfirmed (30/66 books available in TBTA export)
=======
# TBTA Documentation Review: Degree

**Feature**: Degree
**Category**: Tier B - Important Features
**TBTA Status**: Documented (not yet complete)
**Applies to**: Adjectives, Adverbs, Verbs
**Source**: TBTA-FEATURES.md, DATA-STRUCTURE.md

---

## 1. Feature Definition

**Conceptual Definition**: Degree indicates the level of comparison or intensity of adjectives, adverbs, or other qualities. It marks how a property compares to a standard or expresses the intensity with which a property is manifested {tbta-features-2025}.

**Linguistic Category**: Degree is a morphosyntactic feature that can be expressed through:
- Morphological inflection (e.g., English -er, -est)
- Periphrastic constructions (e.g., "more X", "most X")
- Intensifying particles or adverbs
- Syntactic constructions (comparative phrases with "than")

---

## 2. TBTA Values

According to TBTA documentation {tbta-features-2025}, the feature appears across multiple word classes with the following values:

### 2.1 Core Values (Traditional Three-Way System)

| Value | TBTA Code | Description | Example (English) |
|-------|-----------|-------------|-------------------|
| **Positive** / **No Degree** | N | Base form, no comparison | "good", "tall" |
| **Comparative** | C | Comparison between two entities | "better", "taller" |
| **Superlative** | S | Highest/lowest degree among set | "best", "tallest" |

### 2.2 Extended Values (Intensity Modifications)

Based on current TBTA annotations (README.md data distribution), additional values exist:

| Value | Count | Percentage | Description |
|-------|-------|------------|-------------|
| **Intensified** | 848 | 2.7% | Marked intensification (very, so, etc.) |
| **Extremely Intensified** | 213 | 0.7% | Extreme intensification |
| **'too'** | 78 | 0.3% | Excessive degree |
| **'least'** | 35 | 0.1% | Inverse superlative (minimum) |
| **'less'** | 23 | 0.1% | Inverse comparative (diminution) |
| **Intensified Comparative** | 9 | <0.1% | Comparative with added intensification |
| **Superlative of 2 items** | 7 | <0.1% | Superlative used for only 2 items |
| **Equality** | 7 | <0.1% | Equative comparison (as...as) |

**Total TBTA annotations**: 30,879 instances
**No Degree**: 28,970 (93.8%) - the vast majority

### 2.3 Character Encoding

From TBTA's character-based encoding system {data-structure-2025}:

**Verb Position 6 (Degree)**:
- N = No degree
- C = Comparative
- S = Superlative
- I = Intensified

**Note**: The JSON export expands these single-character codes into descriptive values.

---

## 3. Part-of-Speech Distribution

TBTA documents Degree across three word classes {tbta-features-2025}:

### 3.1 Adjectives (Tier C, Feature #45)
- **Status**: Documented
- **Values**: Positive, Comparative, Superlative
- **Priority**: Specialized (Tier C)

### 3.2 Adverbs (Tier B, Feature #31)
- **Status**: Documented
- **Values**: Positive, Comparative, Superlative
- **Priority**: Important (Tier B)

### 3.3 Verbs (Tier B, Feature #30)
- **Status**: Documented
- **Values**: Positive, Comparative, Superlative
- **Priority**: Important (Tier B)
- **Encoding**: Position 6 in 9-position verb code

**Observation**: Degree on verbs is less common cross-linguistically than on adjectives/adverbs, suggesting this may capture intensification or auxiliary constructions rather than pure verbal comparison.

---

## 4. Gateway Features (Constraints)

**Definition**: A "Gateway Feature" is a controlling grammatical category that determines if a sub-feature is valid.

### 4.1 Part-of-Speech Constraint

**Gateway**: Part of Speech
**Rule**: Degree is only applicable to:
- Adjectives (most common)
- Adverbs
- Verbs (for degree modification/intensification)

**Not applicable to**: Nouns, Pronouns, Conjunctions, Prepositions, Particles

**Evidence**: The 93.8% "No Degree" annotation suggests the majority of constituents (especially non-gradable parts of speech) do not receive degree marking {readme-data-distribution}.

### 4.2 Gradability Constraint

**Implicit Gateway**: Semantic Gradability
**Rule**: Only gradable adjectives/adverbs can take degree marking

**Gradable**: "tall", "good", "quickly" (can be more/less tall, good, quickly)
**Non-gradable**: "dead", "unique", "pregnant" (traditionally binary, though usage varies)

**TBTA Status**: Not explicitly documented in TBTA whether gradability is tracked separately.

---

## 5. TBTA Labeling Policy

### 5.1 Semantic vs. Morphological Priority

**Policy**: Not explicitly documented in available TBTA files.

**Critical Questions** (answers require fuller TBTA documentation):
1. Does TBTA prioritize morphological form or semantic function?
   - Example: English "more unique" - morphologically comparative, but "unique" is traditionally non-gradable
2. How are elatives handled? (e.g., "a most interesting tale" - absolute superlative)
3. How are intensifiers categorized vs. true comparatives?

**Observation from data**: The inclusion of "Intensified", "Extremely Intensified", and "'too'" as distinct values suggests TBTA recognizes semantic distinctions beyond traditional positive-comparative-superlative morphology.

### 5.2 Mixed Annotations

**Question**: Can constituents receive multiple degree values simultaneously?

**Evidence from TBTA-FEATURES.md**:
> "Mixed Annotations: Can constituents receive multiple values simultaneously? (e.g., Degree allows 'Intensified' + ''too'')"
> "Note: Some features commonly use mixed annotations (20+ instances per 100 verses), not just edge cases"

**Answer**: YES - Degree explicitly allows mixed annotations.

**Example scenario**: An adjective could be marked as both "Intensified" and "Comparative" (e.g., "very much better").

**Frequency**: The existence of "Intensified Comparative" as a separate value (9 instances) suggests this combination occurs in TBTA annotations.

---

## 6. Past Learnings & Best Practices

### 6.1 From TBTA Critique Document

The TBTA Critique document {critique-2025} does not specifically mention Degree feature issues, suggesting:
1. Degree has not been a major source of annotation inconsistency
2. OR Degree has not yet been thoroughly validated through reproduction experiments

### 6.2 Known Challenges (Inferred)

Based on the Tier B classification and "Documented but not Complete" status:

**Challenge 1**: Distinguishing intensification from comparison
- "very good" (intensified positive) vs. "better" (comparative)
- Requires semantic analysis beyond morphology

**Challenge 2**: Cross-linguistic variation in degree systems
- Some languages have morphological degree (English, Latin, Greek)
- Others use syntactic constructions (Mandarin Chinese: 更 gèng "more")
- Still others lack grammaticalized degree (many isolating languages)

**Challenge 3**: Elative vs. superlative distinction
- Relative superlative: "the tallest person" (comparison to set)
- Absolute superlative/elative: "a very tall person" (intense but not comparative)
- TBTA data suggests this distinction matters (separate "Intensified" category)

---

## 7. Edge Cases

### 7.1 Documented Edge Cases

**Superlative of 2 items** (7 instances, <0.1%)
- **Issue**: Prescriptively, comparative is used for 2 items, superlative for 3+
- **Reality**: Languages often use superlative for 2-item comparisons
- **Example**: "Which is best - chocolate or vanilla?" (2 options, superlative form)
- **TBTA Policy**: Tracks this as separate value, suggesting morphological form is preserved

**Equality** (7 instances, <0.1%)
- **Construction**: Equative comparisons ("as tall as")
- **Issue**: Technically not a "degree" but a comparison type
- **TBTA Policy**: Included in Degree feature despite being distinct from gradation
- **Cross-linguistic**: Equative has dedicated morphology in some languages (Welsh, Tagalog)

### 7.2 Rare Value Discovery

From linguistic literature (not frequency analysis):

**Potential Rare Values**:
1. **Equative**: "as X as" constructions (7 instances confirmed)
2. **Excessive degree**: "'too' X" constructions (78 instances confirmed)
3. **Elative**: Absolute superlative "very/most X" without comparison (possibly captured under "Intensified")
4. **Attenuative**: "somewhat X", "a bit X" (not explicitly listed)

**Values documented but rare**:
- 'least' (35 instances) - inverse superlative
- 'less' (23 instances) - inverse comparative
- Intensified Comparative (9 instances)

### 7.3 Hypothetical Edge Cases (Require Validation)

**Case 1**: Double comparatives/superlatives
- Forms like "more better" or "most best" (non-standard but attested)
- TBTA handling: Unknown

**Case 2**: Suppletive forms
- English "good/better/best", "bad/worse/worst"
- Question: Does TBTA track suppletion separately or just degree?

**Case 3**: Periphrastic vs. synthetic
- "more beautiful" vs. "beautifuller"
- "most beautiful" vs. "beautifullest"
- TBTA likely marks semantic degree regardless of formation strategy

---

## 8. Value Inventory (Complete)

### 8.1 Theoretical Values (From Linguistic Literature)

Based on cross-linguistic typology:

1. **Positive** (base form)
2. **Comparative** (superiority: more X)
3. **Superlative** (highest degree: most X)
4. **Equative** (equality: as X as)
5. **Inverse Comparative** (inferiority: less X)
6. **Inverse Superlative** (minimum: least X)
7. **Elative** (absolute superlative: very X)
8. **Excessive** (too X)
9. **Attenuative** (somewhat X, a bit X)

### 8.2 TBTA Productive Values (From Data)

Values with >1% occurrence (productive):
1. **No Degree** (93.8%) - dominant category
2. **Intensified** (2.7%) - substantial usage
3. **Comparative** (1.3%)
4. **Superlative** (0.9%)

Values with <1% occurrence (rare but attested):
5. **Extremely Intensified** (0.7%)
6. **'too'** (0.3%) - excessive degree
7. **'least'** (0.1%) - inverse superlative
8. **'less'** (0.1%) - inverse comparative
9. **Intensified Comparative** (<0.1%) - mixed annotation
10. **Superlative of 2 items** (<0.1%) - edge case
11. **Equality** (<0.1%) - equative

---

## 9. Source Language Encoding

### 9.1 Koine Greek

**Morphological Encoding**: YES - Greek has explicit degree morphology {hebrew-greek-biblical-2025}

**Formation**:
- **Comparative**: Add -τερος (-teros) to masculine stem (e.g., μέγας → μείζων "greater")
- **Superlative**: Add -τατος (-tatos) or -ιστος (-istos) to stem (e.g., μέγας → μέγιστος "greatest")

**Frequency in NT**: Superlatives are RARE in New Testament Greek {greek-nt-2025}
- Most frequent superlatives: πρῶτος (first), ἔσχατος (last)
- Comparative often used with superlative meaning (elative sense)

**Key Pattern**: Greek allows comparative forms to function as superlatives or elatives:
- Comparative as regular adjective
- Comparative as superlative
- Superlative as regular adjective
- Superlative as comparative
- Both as elative (intensified form)

**Implication**: Morphology does NOT determine semantics in NT Greek - context is crucial.

### 9.2 Biblical Hebrew

**Morphological Encoding**: NO - Hebrew does NOT have dedicated degree morphology {hebrew-grammar-2025}

**Formation Strategies** (periphrastic):
1. **Comparative**: Use preposition מִן (min) "from/than"
   - Example: "David is taller than Saul" = "David is tall from/than Saul"
2. **Superlative**: Use definite article or construct state
   - "the good of the land" = "the best of the land"
   - "song of songs" = "the best/greatest song"
3. **Elative**: Genitive construction
   - "mighty of God" = "very mighty"

**Modern Hebrew** vs. **Biblical Hebrew**:
- Modern Hebrew HAS developed comparative/superlative paradigm
- Biblical Hebrew did NOT have this system
- Implication: OT degree marking is interpretive, not morphological

### 9.3 Source Language Summary

| Feature | Greek | Hebrew |
|---------|-------|--------|
| **Morphological Degree** | YES | NO |
| **Comparative Morphology** | -τερος | מִן (periphrastic) |
| **Superlative Morphology** | -τατος/-ιστος | Construct/article |
| **Elative** | Comp/Superl used as elative | Genitive construct |
| **Frequency** | Rare in NT | Periphrastic only |
| **Ambiguity** | High (form ≠ function) | Moderate (contextual) |

**CRITICAL IMPLICATION**: Source language degree is EXPLICITLY encoded in Greek morphology but requires INTERPRETATION in Hebrew syntax. TBTA must handle both morphological and periphrastic systems.

---

## 10. Discrepancies & Open Questions

### 10.1 Documentation Gaps

**Gap 1**: Morphological vs. Semantic Priority
- Question: Does TBTA mark Greek comparative morphology even when functioning as elative?
- Impact: Affects accuracy of semantic vs. formal annotation

**Gap 2**: Gradability Classification
- Question: Does TBTA have a separate gradability feature or database?
- Impact: Without gradability info, cannot predict which adjectives accept degree

**Gap 3**: Aktionsart Interaction (for Verbs)
- Question: How does verbal degree interact with verb classes?
- Impact: Degree on accomplishment verbs may differ from states
- Related: TBTA Critique notes absence of Aktionsart classification {critique-2025}

### 10.2 Policy Clarifications Needed

**Policy 1**: Elative Handling
- Current: Possibly subsumed under "Intensified"
- Question: Should elatives be separated from comparatives/superlatives?
- Linguistic basis: Semantically distinct (intensity vs. comparison)

**Policy 2**: Equative Status
- Current: Listed as "Equality" (7 instances)
- Question: Should equative be separate feature or part of degree?
- Linguistic basis: Equatives are comparison of equality, not gradation

**Policy 3**: Mixed Annotations Protocol
- Current: Allowed (e.g., "Intensified Comparative")
- Question: What are valid combinations?
- Need: Explicit list of permitted mixed values

### 10.3 Cross-Feature Dependencies

**Dependency 1**: Part of Speech
- Degree requires knowing POS first
- Question: Is there a validation rule preventing degree on non-gradable POS?

**Dependency 2**: Lexical Sense (Features #22-24)
- Some word senses are gradable, others are not
- Example: "fair" (gradable: "fair complexion") vs. "fair" (non-gradable: "fair trial")
- Question: Does TBTA coordinate degree with lexical sense?

**Dependency 3**: Usage (Feature #28)
- Attributive vs. predicative adjectives may differ in degree acceptability
- Some languages restrict degree to predicative position
- Question: Is there interaction tracked?

---

## 11. Summary Assessment

### 11.1 TBTA Strengths

1. **Granular Value Set**: Goes beyond traditional 3-way system (positive/comparative/superlative)
2. **Intensity Distinctions**: Recognizes intensified, extremely intensified, excessive ('too')
3. **Rare Forms Tracked**: Documents inverse forms ('less', 'least'), equatives, edge cases
4. **Mixed Annotations**: Explicitly allows combinations (e.g., intensified comparative)
5. **Multi-POS Application**: Covers adjectives, adverbs, verbs

### 11.2 Documentation Gaps

1. **Policy Unclear**: Semantic vs. morphological priority not documented
2. **Gradability Unstated**: No explicit gradability classification
3. **Formation Strategy**: Doesn't document morphological vs. periphrastic
4. **Hebrew Interpretation**: No discussion of how periphrastic Hebrew degree is identified
5. **Greek Ambiguity**: No policy for Greek forms with multiple semantic functions

### 11.3 Readiness for Algorithm Development

**Current State**: Tier B - Documented but not complete
**Data Available**: 30,879 annotations with 11 distinct values
**Schema Clarity**: MEDIUM - values are clear, but policies are implicit

**Recommendation for Stage 2**:
1. Review sample TBTA annotations to infer unstated policies
2. Validate source language encoding rules (especially Hebrew interpretation)
3. Clarify elative vs. comparative/superlative distinction
4. Document gradability assumptions

---

## 12. Citations

All information in this document is sourced from TBTA documentation files:

**Primary Sources**:
- {tbta-features-2025}: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {data-structure-2025}: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {readme-data-distribution}: `/workspace/bible-study-tools/tbta/features/degree/README.md`
- {critique-2025}: `/workspace/bible-study-tools/tbta/tbta-source/CRITIQUE.md`

**External Research** (for source language analysis):
- {hebrew-grammar-2025}: Gesenius' Hebrew Grammar (Section 133 on adjective comparison)
- {hebrew-greek-biblical-2025}: Biblical language morphology studies
- {greek-nt-2025}: New Testament Greek grammar references

---

**Document Status**: TBTA Documentation Review Complete
**Lines**: 520
**Coverage**: Complete review of all available TBTA degree documentation
**Gaps Identified**: 5 major policy clarifications needed
**Readiness**: Adequate for Stage 2 (Translation Database) with noted caveats
>>>>>>> origin/feat/self-learning-tbta
