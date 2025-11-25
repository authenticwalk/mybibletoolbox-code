# Number Systems: TBTA Documentation Review

**Feature**: Number System  
**TBTA Classification**: Tier A - Essential (affects 1000+ languages)  
**Source**: TBTA Source Documentation (`/bible-study-tools/tbta/tbta-source/*`)  
**Review Date**: 2025-11-24

## 1. Feature Definition

### 1.1 Concept

**What is Number System?**

{tbta-source/DATA-STRUCTURE.md}: "Number System: Beyond singular/plural: Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), Plural (P)"

Number System refers to grammatical marking of quantity/count of entities referenced by nouns and pronouns. Beyond the basic singular/plural dichotomy found in English and Biblical source languages (Hebrew, Aramaic, Greek), many target languages require finer distinctions.

{tbta-source/README.md}: Listed as Tier A Essential feature - "Cannot be easily inferred from context" in 1,000+ languages.

### 1.2 TBTA Schema Location

**Where is it encoded?**

- **Noun feature**: Position 2 in 10-character encoding scheme
- **Applies to**: Nouns, pronouns, noun phrases
- **Source**: {tbta-source/DATA-STRUCTURE.md} - Character-based encoding

**Related to**: Person System (Feature #2), Participant Tracking (Feature #3)

## 2. Value Inventory

### 2.1 Complete Value List

{tbta-source/TBTA-FEATURES.md}: "Number System | Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), Plural (P) | Hawaiian, Samoan, Slovenian | ✅ Complete"

TBTA supports **6 number values**:

| Code | Value    | Meaning             | Source                          | Example Languages                        |
| ---- | -------- | ------------------- | ------------------------------- | ---------------------------------------- |
| S    | Singular | Exactly 1 entity    | {tbta-source/TBTA-FEATURES.md}  | All languages                            |
| D    | Dual     | Exactly 2 entities  | {tbta-source/DATA-STRUCTURE.md} | Hebrew, Arabic, Slovenian, Hawaiian      |
| T    | Trial    | Exactly 3 entities  | {tbta-source/README.md}         | Kilivila, Larike, Fijian (172 languages) |
| Q    | Quadrial | Exactly 4 entities  | {tbta-source/TBTA-FEATURES.md}  | **NONE** - see Section 5.1               |
| p    | Paucal   | Few entities (3-10) | {tbta-source/TBTA-FEATURES.md}  | Some Austronesian/Oceanic                |
| P    | Plural   | Many entities (>3)  | {tbta-source/DATA-STRUCTURE.md} | All languages                            |

{tbta-source/DATA-STRUCTURE.md}: Character encoding position 2 for Nouns encodes Number with these single-character codes.

### 2.2 Value Documentation Status

**Fully Documented** (with morphology/examples):

- Singular (S): Universal
- Dual (D): Hebrew dual morphology (-ayim suffix) documented
- Trial (T): Genesis 1:26 Trinity reference documented
- Plural (P): Universal

**Minimally Documented**:

- Paucal (p): Listed but minimal examples
- Quadrial (Q): Listed but **contested** - no linguistic evidence

### 2.3 Theoretical vs. Productive Values

**From TBTA documentation and linguistic literature**:

| Value    | Theoretical | Productive (Expected Data %) | Languages                                  |
| -------- | ----------- | ---------------------------- | ------------------------------------------ |
| Singular | Yes         | HIGH (40-50%)                | All languages                              |
| Plural   | Yes         | HIGH (40-50%)                | All languages                              |
| Dual     | Yes         | MEDIUM (5-10%)               | Hebrew, Greek (rare), Austronesian, Slavic |
| Trial    | Yes         | LOW (1-3%)                   | 172 Austronesian/Oceanic languages         |
| Paucal   | Yes         | LOW (1-5%)                   | Some Austronesian                          |
| Quadrial | Listed      | **ZERO (0%)**                | **NONE** - no attested language            |

**Source for Quadrial critique**: {tbta-source/CRITIQUE.md} Section 3.1 cites Corbett (2000)

**Note**: Actual frequencies to be validated in Stage 2 data analysis.

## 3. Gateway Features & Constraints

**Controlling Feature**: Part of Speech

{tbta-source/DATA-STRUCTURE.md}: Number applies to:

- Nouns (position 2 in 10-position code)
- Pronouns (same encoding, position 2)
- Verbs (agreement - not directly encoded in TBTA verb positions)

**Dependency Rules**:

- Number is **valid** when Part = Noun, Pronoun, or elements with nominal features
- Number is **not applicable** for Verbs, Adjectives (except in agreement contexts not tracked by TBTA)

## 4. TBTA Labeling Policy

### 4.1 Semantic vs Morphological Priority

{tbta-source/CRITIQUE.md}: "Issue: Morphologically plural forms marked as singular without documentation"

**Evidence from CRITIQUE.md**:

```yaml
Genesis 1:1 - הַשָּׁמַיִם (ha-shamayim, "the heavens")
Hebrew Form: Dual morphology (-ayim suffix)
TBTA Number: Singular
Note: Missing explanation of discrepancy

Genesis 1:2 - הַמָּיִם (ha-mayim, "the waters")
Hebrew Form: Dual morphology (-ayim suffix)
TBTA Number: Singular
Note: Missing explanation

Matthew 5:3 - οὐρανῶν (ouranōn, "of heavens")
Greek Form: Genitive Plural
TBTA Number: Singular
Note: Missing explanation
```

**Policy (inferred but undocumented)**:

- **Priority**: Semantic meaning over morphological form
- **Lexicalized plurals/duals**: Treated as Singular if referent is conceptually one entity
- **Example**: "heavens" (single sky), "waters" (single body of water) → Singular despite morphology

### 4.2 Part-of-Speech Specific Rules

**Not explicitly documented** in reviewed files. Based on examples:

- **Nouns**: Follow semantic number (see above)
- **Pronouns**: Likely follow morphological form (not explicitly stated)
- **Personal pronouns**: Number tracks referent count

**Gap**: No explicit documentation distinguishing pronoun vs noun handling.

## 5. Edge Cases & Special Patterns

### 5.1 Quadrial Category - No Linguistic Evidence

{tbta-source/CRITIQUE.md}: "3.1 Quadrial Category Without Linguistic Evidence"

**Issue**:

```yaml
TBTA Schema: Q: Quadrial (exactly 4)

Linguistic Reality (Corbett 2000):
  - No attested grammatical quadrial in any language
  - Sursurunga: Has "greater paucal" (4+) not true quadrial
  - Marshallese: Rhetorical use only, not grammatical
```

**Assessment**:

- {critique}: "Clutters schema with impossible value"
- {critique}: "Should distinguish lesser paucal (~3-4) from greater paucal (~4-10)"
- **Impact**: Value defined but likely has 0% usage in actual data

### 5.2 Morphological vs Semantic Ambiguity

{tbta-source/CRITIQUE.md}: "Morphological vs. semantic number undocumented"

**Problem**:

- **Hebrew lexicalized duals**: -ayim suffix (שמים shamayim "heavens", מים mayim "waters")
- **Greek pluralia tantum**: Words like οὐρανοί "heavens" - morphologically plural, semantically singular
- **TBTA decision**: Mark as Singular (semantically correct)
- **Documentation gap**: Rule not explicit, causes confusion

**Frequency**: {critique}: "Affects Hebrew lexicalized duals throughout OT (~50-100 instances)"

### 5.3 Natural Pairs - Dual Encoding

**Pattern**: Body parts naturally occurring in pairs use dual morphology in Hebrew.

{tbta-source/DATA-STRUCTURE.md} Examples:

- עֵינַיִם (einayim) "eyes" - dual morphology
- יָדַיִם (yadayim) "hands" - dual morphology
- רַגְלַיִם (raglayim) "feet" - dual morphology
- אָזְנַיִם (oznayim) "ears" - dual morphology

**Translation Impact**:

- Dual-marking target languages should use dual for body part pairs
- Using plural sounds unnatural and may confuse readers
- Theological significance: LOW (grammatical accuracy, not doctrine)

**Status**: Pattern documented but not systematically analyzed.

### 5.4 Collective Nouns - Ambiguity

**Not explicitly addressed** in reviewed documentation.

**Question**: How are collective nouns handled?

- "People" (collective) - Singular or Plural?
- Hebrew "עַם" (am, "people/nation") - Singular or Plural?
- Greek λαός (laos, "people"), ὄχλος (ochlos, "crowd")
- Context-dependent agreement?

**Examples needing analysis**:

- Exodus 19:8 "All the people answered" - collective or distributive?
- Matthew 5:1 "When he saw the crowds" - how many? (arbitrary)

**Status**: Not listed in TBTA documentation (requires data analysis in Stage 2).

## 6. Past Learnings & Policy Evolution

### 6.1 Genesis 1:26 - Trial for Trinity (Critical Finding)

{tbta-source/DATA-STRUCTURE.md} Documents Trinity reference:

```json
{
  "Constituent": "God",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Participant Tracking": "Routine"
}
```

**Context**: Genesis 1:26 "Let us make man in our image"

**TBTA Decision**: Marked as **Trial** (exactly 3 persons)

- Theological interpretation: Trinity (Father, Son, Holy Spirit)
- Critical for trial-marking languages (Kilivila, Larike, Fijian)
- Using Dual would be heretical (Arianism - implies only 2 persons)

**Impact**:

- Trial > Plural (preferred for precision)
- Plural acceptable (orthodox but less precise)
- Dual forbidden (heretical)

**See**: Section 9 for full Trinity reference analysis.

### 6.2 Validated Experiment Results

{tbta-source/CRITIQUE.md}: "6.3 Number Systems Experiment"

**Accuracy**: 91.4% reproduction

**Issues Found**:

1. {critique}: "Morphological vs. semantic number undocumented"
2. {critique}: "Quadrial in schema without attestation"
3. {critique}: "Hebrew dual handling inconsistent"

**Interpretation**:

- Core algorithm is sound (91.4% accuracy)
- Documentation gaps cause confusion
- Schema includes theoretically impossible values

## 7. Value Inventory: Theoretical vs Productive

**From Linguistic Literature (not frequency data)**:

| Value    | Theoretical | Productive (Expected in Data) | Languages with Feature                            |
| -------- | ----------- | ----------------------------- | ------------------------------------------------- |
| Singular | Yes         | HIGH (100%)                   | All languages                                     |
| Dual     | Yes         | MEDIUM (5-10%)                | Hebrew, Greek, Slovenian, Austronesian (88 langs) |
| Trial    | Yes         | LOW (1-3%)                    | Kilivila, Larike, some Austronesian (172 langs)   |
| Quadrial | Documented  | **NONE** (0%)                 | None attested {critique}                          |
| Paucal   | Yes         | LOW (1-5%)                    | Some Austronesian, Arabic dialects                |
| Plural   | Yes         | HIGH (40-50%)                 | All languages                                     |

**Note**: Actual frequencies require data analysis (Stage 2).

## 8. Mixed Annotations

**Not mentioned** in TBTA documentation for Number System.

**Assessment**: Number is typically a **single value** feature - a noun/pronoun is either Singular, Dual, Trial, or Plural, not multiple simultaneously.

**Possible exception**: Ambiguous contexts where number is unspecified - but this would likely be encoded as "Unspecified", not as multiple values.

**Status**: Does not appear to use mixed annotations (unlike Degree feature which allows "Intensified" + "'too'").

## 9. Trinity Reference (Genesis 1:26)

{tbta-source/DATA-STRUCTURE.md}: "Trinity Reference (Genesis 1:26)"

```json
{
  "Constituent": "God",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Participant Tracking": "Routine"
}
```

**Key Example**: Genesis 1:26 "Let us make man in our image"

- TBTA marks as **Trial** (exactly 3 persons)
- Theological interpretation: Trinity (Father, Son, Holy Spirit)
- Critical for Christian orthodox translation

**Impact**: Trial number has both **linguistic** (some Austronesian languages) and **theological** (Trinity) significance.

## 10. Summary

**Feature**: Number System (grammatical count of entities)

**Values**: S (Singular), D (Dual), T (Trial), Q (Quadrial - problematic), p (Paucal), P (Plural)

**Policy**:

- Semantic priority over morphology (undocumented but evident)
- Lexicalized duals/plurals → Singular if semantically one entity
- Hebrew/Greek special cases handled case-by-case

**Issues**:

- Quadrial has no linguistic attestation
- Morphological vs semantic rule undocumented
- Collective noun handling not specified
- Pronoun vs noun rules not distinguished

**Status**: TBTA Tier A - Essential feature, marked as "Complete" (68% of Tier A complete overall)

**Accuracy**: 91.4% reproduction in experiments {critique}

**Coverage**: 11,649 verses across 34 books (~37% of Bible) {tbta-source/README.md}

**Key Languages**: Hebrew (Dual in OT), Greek (Dual rare in NT), Target languages with Trial/Paucal systems

## Bibliography

All sources from `/bible-study-tools/tbta/tbta-source/`:

- {tbta-source/README.md} - TBTA overview
- {tbta-source/DATA-STRUCTURE.md} - Technical encoding details
- {tbta-source/TBTA-FEATURES.md} - Feature catalog
- {tbta-source/CRITIQUE.md} - Validated issues from experiments

**External Source Cited in CRITIQUE.md**:

- Corbett, Greville G. (2000). _Number_. Cambridge University Press. {corbett-2000-number}
