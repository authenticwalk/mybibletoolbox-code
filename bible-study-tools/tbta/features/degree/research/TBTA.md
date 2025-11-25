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
