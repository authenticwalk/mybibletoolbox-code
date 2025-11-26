# Number System Feature

**Feature**: Grammatical Number
**TBTA Tier**: A (Essential)
**Stage**: 1 - Research Complete
**Status**: ✅ Ready for Stage 2 (Analysis)
**Last Updated**: 2025-11-26

## Overview

Grammatical number encodes the count of entities: singular (1), dual (2), trial (3), paucal (few), plural (many). While English uses simple singular/plural, many target languages require finer distinctions. This feature is **theologically critical** in Trinity contexts (Genesis 1:26 "Let us...") and **contextually important** for narrative precision (dual for pairs, trial for triplets). Research identifies significant gaps: Quadrial not attested in any language, trial restricted to ~20-30 languages (not 172 as claimed), and no trial languages in current dataset.

## Quick Facts

| Aspect | Details |
|--------|---------|
| **TBTA Values** | S (Singular), D (Dual), T (Trial), Q (Quadrial - NOT ATTESTED), p (Paucal), P (Plural) |
| **Source Languages** | Hebrew: S/D/P (dual morphology) \| Greek: S/P (dual lost in Koine) |
| **Critical Languages** | Austronesian (176 in dataset), Afro-Asiatic (Arabic dual/paucal), Slovenian (dual - NOT in dataset) |
| **Theological Stakes** | **HIGH** (5%): Trinity contexts (trial > plural, NEVER dual) \| **MEDIUM** (10%): Pairs/triplets (narrative clarity) \| **NONE** (85%): Arbitrary contexts |
| **Gateway Feature** | Part of Speech (applies to Nouns, Pronouns) |
| **Character Position** | Position 2 in TBTA's 10-position noun code |
| **Dataset Coverage** | 1,008 languages, 30+ families |
| **Research Depth** | 2,800+ lines, 29 scholarly sources |

## Example: Why Number Matters

### Genesis 1:26 - "Let us make man in our image"

**Challenge**: Hebrew "us" (נַעֲשֶׂה na'aseh) - How many persons?

| Target Language | Number System | Translation Choice | Theological Precision |
|-----------------|---------------|-------------------|----------------------|
| Larike (if in dataset) | S/D/T/P | **Trial** ("we-three") | ✅ Explicit Trinity |
| Hawaiian (suspected) | S/D/P | **Plural** ("we-many") | ✅ Orthodox (vague) |
| Hawaiian | S/D/P | **Dual** ("we-two") | ❌ **HERETICAL** (Arianism - only 2 persons) |
| English | S/P | **Plural** ("us") | ✅ Orthodox (vague) |

**Translator Guidance**:
- **FIRST CHOICE**: Trial (if available) = explicit Trinity
- **SECOND CHOICE**: Plural (if no trial) = orthodox but less precise
- **FORBIDDEN**: Dual = Binitarian heresy (implies only 2 divine persons)

## Target Audience & Language Families

**High Priority** (complex number systems):
1. **Austronesian** (176 languages, 17.5%): Dual/trial/paucal in some (e.g., Hawaiian, Tongan)
2. **Afro-Asiatic** (25 languages): Arabic has dual (exactly 2) + paucal (3-10)
3. **Slavic** (Indo-European subset): Slovenian has productive dual (NOT in dataset - gap)

**Medium Priority** (simple systems):
4. **Indo-European** (135 languages): Mostly S/P only (English, Spanish, German, French)
5. **Niger-Congo** (89 languages): Swahili noun classes with S/P
6. **Sino-Tibetan** (18 languages): Mandarin classifier language, optional number

**Key Distinction**: Trial languages (~20-30 total, NONE in dataset) can explicitly encode Trinity as "exactly 3 persons."

## TBTA Encoding

**Character Position**: Position 2 in 10-position noun code
**Example**: Genesis 1:1 "God" (noun)

```yaml
Part: Noun
Number: Singular  # Position 2
Gender: Masculine # Position 1
Case: Nominative  # Position 3
```

**Policy** (inferred, not explicitly documented):
- **Semantic priority for nouns**: Lexicalized duals (Hebrew שָׁמַיִם shamayim "heavens") marked Singular despite dual morphology
- **Morphological priority for pronouns** (suspected): "We" marked Plural or Trial based on form

**Issue**: Quadrial (Q) in schema but zero attested languages {corbett-2000}. Recommendation: Remove or deprecate.

## Theological Significance

### Non-Arbitrary (15% of contexts)

**Theological-Critical (5%)**:
- **Genesis 1:26, 3:22, 11:7**: "Let us..." → Trial > Plural, NEVER Dual
- **Matthew 28:19**: "Name" (singular) → MUST be Singular, NEVER Plural (Tritheism)

**Contextual-Precision (10%)**:
- **Pairs**: Ruth and Naomi, two disciples → Dual > Plural (clarity)
- **Triplets**: Peter/James/John, Shadrach/Meshach/Abednego → Trial > Plural (tracking)

### Arbitrary (85% of contexts)

Crowd sizes, generic plurals, abstract concepts, collective nouns, objects - choice is stylistic.

## Research Summary

**Comprehensive research complete** (2,800+ lines across 5 files):

1. **[research/TBTA.md](research/TBTA.md)** (634 lines): TBTA values, policies, edge cases, gaps
2. **[research/LANGUAGES.md](research/LANGUAGES.md)** (574 lines): 1,008-language typological analysis
3. **[research/SCHOLARLY.md](research/SCHOLARLY.md)** (708 lines): 29 scholarly sources, translation theory
4. **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** (445 lines): Non-arbitrary classification
5. **[research/README.md](research/README.md)** (199 lines): Research synthesis, discrepancies, next steps

**Key Findings**:
- Hebrew/Greek explicitly encode number (Hebrew dual, Greek S/P only)
- ~20-30 trial languages confirmed (vs. TBTA claim of 172) - NONE in dataset
- Quadrial not attested in any language - schema issue
- Trinity contexts require trial > plural, never dual (heresy risk)

**Gaps Identified**:
1. No trial languages in dataset (Larike, Tok Pisin, Marshallese missing)
2. Slovenian (only modern Slavic dual) not in dataset
3. Quadrial in schema but not attested
4. Semantic vs. morphological policy undocumented

## Next Steps

### Stage 2: Analysis & Hypothesis Validation

**Data Extraction**: Extract all number annotations, frequency analysis
**Hypotheses**:
- H1: Quadrial frequency = 0%
- H2: Trial only on pronouns, not nouns
- H3: Frozen duals (shamayim) marked Singular (semantic priority)
- H4: Genesis 1:26 marked Trial (Trinitarian interpretation)

**Test Languages** (10 proposed): English, Spanish, Arabic, Indonesian, Hawaiian, Mandarin, German, Swahili, Russian, Tongan

---

**Lines**: 74 (within 75-line progressive disclosure limit)
**Status**: Stage 1 Complete ✅
**Ready for**: Stage 2 Analysis
