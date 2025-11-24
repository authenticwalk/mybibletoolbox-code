# Number Systems: TBTA Documentation Review

**Feature**: Number System
**Source**: TBTA Source Documentation (`/bible-study-tools/tbta/tbta-source/*`)
**Review Date**: 2025-11-24

## 1. Concept Definition

**What is Number System?**

{tbta-source/DATA-STRUCTURE.md}: "Number System: Beyond singular/plural: Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), Plural (P)"

Number System refers to grammatical marking of quantity/count of entities referenced by nouns and pronouns. While English primarily distinguishes singular vs plural, many languages make finer distinctions.

## 2. TBTA Values

{tbta-source/TBTA-FEATURES.md}: "Number System | Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), Plural (P) | Hawaiian, Samoan, Slovenian | ✅ Complete"

**Complete Value Inventory from TBTA**:

| Code | Value | Meaning | Status |
|------|-------|---------|--------|
| S | Singular | Exactly 1 entity | Standard - all languages |
| D | Dual | Exactly 2 entities | Documented - 88 languages (Austronesian, Semitic) |
| T | Trial | Exactly 3 entities | Documented - 172 languages (Polynesian, Melanesian) |
| Q | Quadrial | Exactly 4 entities | **PROBLEMATIC** - see section 5 |
| p | Paucal | Few entities (3-10, varies) | Documented - some Austronesian |
| P | Plural | Many entities (>3 typically) | Standard - all languages |

{tbta-source/DATA-STRUCTURE.md}: Character encoding position 2 for Nouns encodes Number with these single-character codes.

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

## 5. Edge Cases

### 5.1 Quadrial Category - Problematic

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

### 5.3 Collective Nouns

**Not explicitly addressed** in reviewed documentation.

**Question**: How are collective nouns handled?
- "People" (collective) - Singular or Plural?
- Hebrew "עַם" (am, "people/nation") - Singular or Plural?
- Context-dependent agreement?

**Status**: Not listed in TBTA documentation (requires data analysis in Stage 2).

## 6. Past Learnings

### 6.1 Validated Experiment Results

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

| Value | Theoretical | Productive (Expected in Data) | Languages with Feature |
|-------|-------------|-------------------------------|------------------------|
| Singular | Yes | HIGH (100%) | All languages |
| Dual | Yes | MEDIUM (5-10%) | Hebrew, Greek, Slovenian, Austronesian (88 langs) |
| Trial | Yes | LOW (1-3%) | Kilivila, Larike, some Austronesian (172 langs) |
| Quadrial | Documented | **NONE** (0%) | None attested {critique} |
| Paucal | Yes | LOW (1-5%) | Some Austronesian, Arabic dialects |
| Plural | Yes | HIGH (40-50%) | All languages |

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
- Corbett, Greville G. (2000). *Number*. Cambridge University Press. {corbett-2000-number}

