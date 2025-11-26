# Number Systems Feature

**Feature**: Grammatical Number
**TBTA Tier**: A (Essential)
**Stage**: 2 - Analysis Complete
**Status**: ✅ Analysis complete, ready for Stage 3 (Experimentation)
**Last Updated**: 2025-11-26

## Overview

Grammatical number encodes the count of entities: singular (1), dual (2), trial (3), paucal (few), plural (many). While English uses simple singular/plural, many target languages require finer distinctions. This feature is **theologically critical** in Trinity contexts (Genesis 1:26 "Let us...") and **contextually important** for narrative precision (dual for pairs, trial for triplets).

**Why This Matters**: 
- **172 languages** can explicitly mark trial (exactly 3 persons) for Trinity passages
- **~800 languages** have dual (exactly 2) for apostle pairs, natural pairs (hands, eyes)
- Wrong number choice can imply heresy (dual for Trinity = Arianism)

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Values** | S (Singular), D (Dual), T (Trial), P (Plural), p (Paucal) |
| **Source Languages** | Hebrew (dual morphology), Greek (S/P, dual vestigial) |
| **Critical Languages** | Austronesian (176 in dataset), Slavic (dual), Semitic (dual) |
| **Theological Stakes** | HIGH (Trinity contexts ~5%), MEDIUM (narrative precision ~10%), NONE (arbitrary ~85%) |
| **TBTA Accuracy** | 91.4% reproduction |
| **Gateway Feature** | Part of Speech (applies to Nouns, Pronouns) |

## Example: Why Number Matters

### Genesis 1:26 - "Let us make man in our image"

**Challenge**: Hebrew uses plural "us" - how many persons?

| Target Language | Number System | Translation Choice | Theological Precision |
|-----------------|---------------|-------------------|----------------------|
| Kilivila (PNG) | S/D/T/P | **Trial** ("we-three") | ✅ Explicit Trinity |
| Hawaiian | S/D/P | **Dual** ("we-two") | ❌ HERESY (Arianism - only 2 persons) |
| Hawaiian | S/D/P | **Plural** ("we-many") | ✅ Acceptable (less precise) |
| English | S/P | **Plural** ("us") | ✅ Acceptable (vague) |
| Indonesian | Optional | **No marking** | ⚠️ Ambiguous |

**Translator Guidance**: 
- **FIRST CHOICE**: Trial (if language has it) = explicit Trinity
- **SECOND CHOICE**: Plural (if no trial) = orthodox but vague
- **FORBIDDEN**: Dual = implies 2 persons (Binitarian heresy)

### Ruth 1 - "Ruth and Naomi went together"

**Challenge**: Two women - can target language be precise?

| Language | Solution |
|----------|----------|
| Slovenian (dual) | Use dual ("they-two" went) - narrative clarity |
| English (no dual) | Use plural ("they" went) - contextually clear |
| Kilivila (trial) | Use dual (not trial - trial is for 3) |

**Impact**: Dual adds narrative precision, improves reader tracking.

## Target Audience & Language Families

**High Priority** (complex number systems):
1. **Austronesian** (176 languages): Many have dual/trial/paucal
   - Hawaiian, Fijian (dual, trial suspected)
   - Indonesian (optional marking)
   - Philippine languages (various systems)
   
2. **Slavic** (Indo-European): Slovenian has productive dual
   - Russian/Polish/Czech: Singular/Plural only
   - Note: Slovenian NOT in current dataset (gap)

3. **Semitic** (Afro-Asiatic): Hebrew, Arabic have dual
   - Classical Arabic dual productive
   - Modern dialects vary

**Medium Priority** (simple systems):
4. **Romance/Germanic**: Singular/Plural only (English, Spanish, French, German)
5. **Niger-Congo**: Mostly Singular/Plural (Swahili, Akan)
6. **Other families**: Various patterns (see [research/LANGUAGES.md](research/LANGUAGES.md))

**Unique Distinctions**:
- **Trial-marking languages** (172 claimed): Can encode Trinity explicitly
- **Dual-marking languages** (~88): Can distinguish pairs from groups
- **Optional-marking languages**: May not mark number at all (isolating languages)
- **Animacy-based**: Some languages mark number on humans, not objects

## TBTA Encoding

**Character Position**: Position 2 in 10-position noun code

**Values**:
- `S` = Singular (1)
- `D` = Dual (2)
- `T` = Trial (3)
- `Q` = Quadrial (4) - **PROBLEMATIC**: No attested language has this
- `p` = Paucal (few, ~3-10)
- `P` = Plural (many, 3+)

**Policy** (inferred, undocumented):
- **Semantic priority**: Lexicalized plurals → Singular if semantically one entity
  - Example: Hebrew שָׁמַיִם (shamayim, "heavens" - dual morphology) → Marked Singular
  - Example: Greek οὐρανῶν (ouranōn, "of heavens" - plural morphology) → Marked Singular
- **Pronoun vs. Noun**: Not explicitly distinguished (gap in documentation)

**Issues**:
1. Quadrial in schema without linguistic attestation (Corbett 2000)
2. Morphological vs. semantic rule undocumented (causes ~50-100 OT ambiguities)
3. Collective noun handling not specified

## Theological Significance

### Non-Arbitrary (15% of contexts)

**1. Theological-Critical (5%)** - Doctrinal heresy if wrong:
- **Genesis 1:26, 3:22, 11:7**: "Let us..." - Trinity contexts
  - Trial preferred, Plural acceptable, Dual **FORBIDDEN**
- **Matthew 28:19**: "Name" (singular) of Father/Son/Spirit - Must be singular (not "names")
- **Isaiah 6:8**: "Whom shall I send, who will go for us?" - Trinitarian interpretation

**2. Contextual-Precision (10%)** - Reader confusion if imprecise:
- **Ruth 1**: Ruth + Naomi (2 women) - Dual if available
- **Luke 24:13**: Two disciples on Emmaus road - Dual
- **Matthew 17:1**: Peter, James, John (3 disciples) - Trial if available
- **Daniel 3**: Shadrach, Meshach, Abednego (3 friends) - Trial

### Arbitrary (85% of contexts)

- Crowd sizes: "multitude", "many people" (paucal vs. plural doesn't matter)
- Objects: "the stones", "the fish" (unless narratively significant)
- Generic statements: "all have sinned" (universal quantifier)
- Abstract plurals: "the heavens declare" (lexicalized plural)
- Collective nouns: "the people said" (singular or plural acceptable)

**Key Insight**: Most number choices are stylistic. Focus algorithm on non-arbitrary contexts.

## Research Summary

**Comprehensive research complete** (1,088 lines across 4 files):

1. **[research/TBTA.md](research/TBTA.md)**: TBTA documentation review, values, policies, edge cases
2. **[research/LANGUAGES.md](research/LANGUAGES.md)**: 1,009-language analysis, typology, 10 proposed test languages
3. **[research/SCHOLARLY.md](research/SCHOLARLY.md)**: Linguistic typology (Corbett, WALS), translation case studies
4. **[research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: Arbitrary vs. non-arbitrary classification

**Key Findings**:
- Hebrew/Greek explicitly encode number (morphology)
- Austronesian most complex (dual/trial/paucal)
- Trinity contexts require trial > plural, never dual
- 91.4% TBTA reproduction accuracy (strong baseline)
- Quadrial should be removed (no attestation)

**Gaps Identified**:
1. 172 trial-language claim needs verification (Stage 2)
2. Slovenian (only modern Slavic dual) not in dataset
3. Collective noun handling undocumented
4. Associative plural ("X and company") not analyzed

See [research/README.md](research/README.md) for full summary.

## Stage 2 Analysis Results

**Data extracted**: 171,876 annotations from TBTA. See [analysis/README.md](analysis/README.md) for full details.

**Distribution** (confirms Stage 1 predictions):
- Singular: 66.2% (most common)
- Plural: 32.4%
- Dual: 1.0% (body parts, pairs)
- Trial: 0.3% (rare)
- **Quadrial: 0.1% - CONFIRMED SUSPICIOUS** (should be 0%)
- Paucal: 0.03%

**LLM Baseline**: 76% accuracy on 100 diverse samples

**Key Error Patterns**:
| Error Type | Frequency | Root Cause |
|-----------|-----------|------------|
| Paucal → Plural | 41.7% | Unclear criteria for "few" |
| Quadrial → Plural | 12.5% | No linguistic basis for quadrial |
| Trinity inconsistency | 8.3% | TBTA labels vary (some Trial, some Plural) |

**TBTA Data Quality Issues Identified**:
1. **Trinity passages inconsistent**: GEN.1.26 → Trial, but GEN.11.7 → Plural
2. **Quadrial category**: 185 uses but no attested language has grammatical quadrial
3. **Paucal boundary unclear**: Only 52 natural occurrences (0.03%)
4. **Lexicalized dual exceptions**: PSA.19.1 "heavens" marked Plural (should be Singular)

**Files Created**:
- `analysis/data/train.jsonl` - Training set (331 entries, stratified)
- `analysis/data/validate.jsonl` - Validation set (100 entries) - Labels hidden
- `analysis/data/test.jsonl` - Test set (96 entries) - RESERVED
- `analysis/data/leftovers.jsonl` - Remaining TBTA data (171,260 entries)
- `analysis/HIGH-LEVEL-REVIEW.md` - LLM baseline analysis
- `analysis/EDGE-CASES.md` - When NOT Singular/Plural
- `analysis/TBTA-QUALITY.md` - Data quality issues, questions for TBTA team
- `analysis/STRONGS.md` - Strong's word pattern analysis
- `analysis/WORD-ANALYSIS.md` - Translation word patterns
- `analysis/reason-groupings-with-hints.jsonl` - Theological hints for verses

## Next Steps

### Stage 3: Experimentation

**Algorithm Development**:
- Baseline: Simple majority (Singular or Plural based on morphology)
- Logic-based: Rules for Trinity, dual-pairs, trial-triplets
- Translation consensus: What do dual/trial languages do in parallel texts?
- Strong's annotation: Do certain Hebrew/Greek words predict number?

**Target Accuracy**: >92% (beat TBTA's 91.4% baseline)

### Stage 4: Validation & Peer Review

**Peer Review Required**:
- Theologian: Validate Trinity interpretations, denominational variations
- Linguist: Confirm trial/dual language claims, typology accuracy
- Translator: Practical guidance review, edge case handling

## Related Features

- **Person System**: Often co-encodes with number (singular vs. plural persons)
- **Participant Tracking**: Interacts with number (first mention vs. routine reference)
- **Part of Speech**: Gateway feature (number applies to nouns, pronouns)

## Questions?

See:
- [../README.md](../README.md) - Main TBTA overview
- [research/README.md](research/README.md) - Research summary
- [../features/README.md](../features/README.md) - Feature catalog
- [.instructions-to-build-feature/STAGE-1-RESEARCH.md](../.instructions-to-build-feature/STAGE-1-RESEARCH.md) - Research methodology

---

**Status**: Stage 2 complete ✅
**Ready for**: Stage 3 Experimentation

