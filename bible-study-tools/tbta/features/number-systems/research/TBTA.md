# TBTA Documentation Review: Number Systems

**Source**: TBTA source documentation (`tbta-source/`), GitHub repository analysis  
**Date**: 2025-01-27  
**Purpose**: Extract TBTA's definition, values, constraints, and policies for the Number System feature

---

## 1. Feature Definition

**Concept**: Number System identifies grammatical number distinctions beyond the basic singular/plural dichotomy found in English and Biblical source languages (Hebrew, Aramaic, Greek).

**TBTA Classification**: Tier A - Essential Feature (affects 1000+ languages, cannot be easily inferred)

**Location in TBTA Schema**: 
- Noun feature (Position 2 in character-based encoding)
- Applies to nouns, pronouns, and noun phrases

**Source Citations**:
- `TBTA-FEATURES.md`: Listed as Feature #1 under Noun Features
- `DATA-STRUCTURE.md`: Position 2 in noun encoding (S/D/T/P)
- `tbta-source/README.md`: Listed as essential for 1,000+ languages

---

## 2. Value Inventory

### 2.1 Complete Value List

TBTA supports **6 number values**:

| Code | Value | Definition | Source |
|------|-------|------------|--------|
| **S** | Singular | One entity | `TBTA-FEATURES.md`, `DATA-STRUCTURE.md` |
| **D** | Dual | Exactly two entities | `TBTA-FEATURES.md`, `DATA-STRUCTURE.md` |
| **T** | Trial | Exactly three entities | `TBTA-FEATURES.md`, `TRANSLATION-EDGE-CASES.md` |
| **Q** | Quadrial | Exactly four entities | `TBTA-FEATURES.md` |
| **p** | Paucal | A few entities (small inexact group, typically 3-15) | `TBTA-FEATURES.md` |
| **P** | Plural | Multiple entities (more than paucal or unspecified) | `TBTA-FEATURES.md`, `DATA-STRUCTURE.md` |

### 2.2 Value Documentation Status

**Documented Values** (from TBTA source):
- Singular: Fully documented
- Dual: Documented, Hebrew dual morphology noted
- Trial: Documented with theological significance (Genesis 1:26 Trinity reference)
- Plural: Fully documented
- Paucal: Listed but minimal documentation
- Quadrial: Listed but **contested** (see Section 4.1)

**Theoretical vs. Productive**:
- **Singular/Plural**: Productive (most common)
- **Dual**: Productive in Hebrew morphology, semantic use in other languages
- **Trial**: Productive in 172+ Austronesian languages (`tbta-source/README.md`)
- **Paucal**: Productive in some Austronesian/Oceanic languages
- **Quadrial**: **Theoretical only** - no attested grammatical quadrial in natural languages (`CRITIQUE.md`)

---

## 3. Gateway Features & Constraints

### 3.1 Part of Speech Constraint

**Constraint**: Number System applies primarily to **nouns** and **pronouns**.

**Source**: `DATA-STRUCTURE.md` - Position 2 in noun encoding schema

**Verbs**: Number agreement may exist but is not the primary feature location (verbs encode person/number through different features)

### 3.2 Related Features

**Person System** (Feature #2):
- Interacts with number: First person plural can be inclusive/exclusive
- Example: Genesis 1:26 combines Trial number + First Inclusive person (`DATA-STRUCTURE.md`)

**Participant Tracking** (Feature #3):
- May affect number interpretation (collective vs. individual)
- Not a gateway feature (number can exist independently)

**Surface Realization** (Feature #7):
- Pronoun vs. noun may follow different number logic (see Section 5.2)

---

## 4. TBTA Policy & Labeling Rules

### 4.1 Semantic vs. Morphological Priority

**Policy**: TBTA prioritizes **semantic meaning** over morphological form.

**Evidence**:
```yaml
Genesis 1:1 - הַשָּׁמַיִם (ha-shamayim, "the heavens")
Hebrew Form: Dual morphology (-ayim suffix)
TBTA Number: Singular
Rationale: Lexicalized dual (semantically singular concept)
Source: CRITIQUE.md Section 3.2

Genesis 1:2 - הַמָּיִם (ha-mayim, "the waters")
Hebrew Form: Dual morphology (-ayim suffix)  
TBTA Number: Singular
Rationale: Lexicalized dual (semantically singular concept)
Source: CRITIQUE.md Section 3.2

Matthew 5:3 - οὐρανῶν (ouranōn, "of heavens")
Greek Form: Genitive Plural
TBTA Number: Singular
Rationale: Semantic singular concept despite plural morphology
Source: CRITIQUE.md Section 3.2
```

**Impact**: 
- Correct semantic choice but **undocumented** decision process
- Translators may be confused by morphological plural marked as semantic singular
- TBTA lacks explicit "morphological vs. semantic" distinction field

### 4.2 Part-of-Speech Rules

**Nouns**: Follow semantic meaning (see Section 4.1)

**Pronouns**: 
- Documentation unclear on pronoun-specific rules
- May follow morphology more closely than nouns (not explicitly stated)
- First person plural pronouns interact with Person System (inclusive/exclusive)

**Source**: `DATA-STRUCTURE.md` - Number applies to nouns; pronoun behavior not explicitly documented

### 4.3 Quadrial Controversy

**Issue**: TBTA schema includes Quadrial (Q) despite no natural language having true grammatical quadrial.

**TBTA Documentation**: Quadrial listed as valid value (`TBTA-FEATURES.md`)

**Linguistic Reality** (from `CRITIQUE.md`):
- **No attested grammatical quadrial** in any language (Corbett 2000)
- Sursurunga: Has "greater paucal" (4+) not true quadrial
- Marshallese: Rhetorical use only, not grammatical

**TBTA Rationale**: Not documented - category included "just in case" without validation (`CRITIQUE.md` Section 3.1)

**Impact**: 
- Clutters schema with impossible value
- Misrepresents languages with greater paucal systems
- Should distinguish lesser paucal (~3-4) from greater paucal (~4-10)

---

## 5. Past Learnings & Policy Evolution

### 5.1 Genesis 1:26 - Trial Number for Trinity

**TBTA Annotation**: Trial (exactly 3 persons)

**Rationale**: 
- Divine first-person plural ("Let us make")
- Theological significance: Trinity (Father, Son, Holy Spirit)
- Prevents heretical dual (2 persons) or generic plural (many persons)

**Source**: `TRANSLATION-EDGE-CASES.md` Example 1, `DATA-STRUCTURE.md` example

**Translation Impact**: 
- 172+ Austronesian languages require trial number marking
- Without TBTA, translators might use dual or plural, losing theological precision
- Guides translators in Kilivila (Papua New Guinea), Larike (Maluku), and other trial-number languages

### 5.2 Hebrew Dual Morphology Handling

**Pattern**: Hebrew lexicalized duals marked as semantic singular

**Examples**:
- `שָׁמַיִם` (shamayim, "heavens") - dual morphology, singular meaning
- `מָּיִם` (mayim, "waters") - dual morphology, singular meaning

**Policy**: Semantic overrides morphological (consistent application)

**Documentation Gap**: Policy not explicitly stated in TBTA documentation (`CRITIQUE.md` Section 3.2)

---

## 6. Edge Cases & Special Handling

### 6.1 Lexicalized Duals (Hebrew)

**Pattern**: Morphologically dual forms semantically singular

**Handling**: Marked as Singular in TBTA

**Frequency**: ~50-100 instances throughout OT (`CRITIQUE.md` Section 3.2)

**Examples**: See Section 4.1

### 6.2 Collective Nouns

**Pattern**: Morphologically plural forms referring to singular concepts

**Handling**: Marked as Singular (semantic priority)

**Example**: "heavens" (Greek plural, semantic singular)

### 6.3 Natural Pairs

**Pattern**: Body parts, paired items (eyes, hands, feet)

**TBTA Handling**: Not explicitly documented

**Linguistic Expectation**: Should be Dual in dual-marking languages

**Source**: Not found in TBTA documentation (gap identified)

### 6.4 Mixed Annotations

**Question**: Can constituents receive multiple number values simultaneously?

**TBTA Documentation**: Not explicitly addressed

**Linguistic Possibility**: Some languages may require multiple number markers (e.g., dual + paucal distinctions)

**Note**: Unlike Degree feature (which allows mixed annotations), Number System appears to be mutually exclusive

---

## 7. Coverage & Frequency

### 7.1 Value Frequency (from TBTA data)

**Not Documented**: TBTA source documentation does not provide frequency data

**Expected Distribution** (based on linguistic typology):
- Singular: ~70% (most common)
- Plural: ~25% (second most common)
- Dual: Rare (Hebrew morphology, semantic pairs)
- Trial: ~1% (Trinity references, explicit "three")
- Paucal: ~0.5% (small groups)
- Quadrial: ~0.5% (if used, likely misclassified paucal)

**Source**: Frequency estimates not from TBTA documentation (requires Stage 2 analysis)

### 7.2 Verse Coverage

**TBTA Coverage**: 11,649 verses across 34 books (~37% of Bible)

**Number System Coverage**: Not specified (assumed complete for covered verses)

**Source**: `tbta-source/COVERAGE.md`, `tbta-source/README.md`

---

## 8. Discrepancies & Gaps

### 8.1 Quadrial Without Evidence

**Discrepancy**: Schema includes Quadrial despite no linguistic attestation

**Source**: `CRITIQUE.md` Section 3.1

**Recommendation**: Distinguish lesser paucal (~3-4) from greater paucal (~4-10) instead

### 8.2 Morphological vs. Semantic Undocumented

**Gap**: Policy of semantic priority not explicitly documented

**Impact**: Confusing for annotators and translators

**Source**: `CRITIQUE.md` Section 3.2

**Recommendation**: Add explicit morphological/semantic distinction field

### 8.3 Natural Pairs Not Documented

**Gap**: No explicit guidance on dual-marking for natural pairs (eyes, hands)

**Impact**: Inconsistent handling possible

**Source**: Gap identified in review (not in TBTA documentation)

---

## 9. Summary

### 9.1 TBTA Definition

**Concept**: Grammatical number distinctions beyond singular/plural

**Values**: S (Singular), D (Dual), T (Trial), Q (Quadrial), p (Paucal), P (Plural)

**Priority**: Semantic meaning over morphological form

### 9.2 Key Policies

1. **Semantic Priority**: Overrides morphological form (Hebrew duals → Singular)
2. **Theological Significance**: Trial for Trinity references (Genesis 1:26)
3. **Quadrial Controversy**: Listed but not linguistically attested

### 9.3 Documentation Gaps

1. Morphological vs. semantic distinction not explicit
2. Natural pairs (dual) handling not documented
3. Quadrial rationale not provided
4. Frequency data not available in documentation

---

**Next Steps**: See `LANGUAGES.md` for language family analysis and `SCHOLARLY.md` for typological research.

