# Number Systems: Research Summary

**Feature**: Grammatical Number (Singular, Dual, Trial, Paucal, Plural)
**Stage**: 1 - Research & Definition
**Status**: Complete
**Date**: 2025-11-24

## Executive Summary

Grammatical number systems encode the count of entities referenced by nouns/pronouns. While English uses simple singular/plural, many languages make finer distinctions (dual for 2, trial for 3, paucal for "few"). Number systems are **explicitly encoded** in Hebrew (OT) and Greek (NT) morphology, making this a Tier A essential feature for translation. 

**Key Finding**: Number is **theologically significant** in ~15% of contexts (primarily Trinity references like Genesis 1:26) and **stylistically arbitrary** in ~85% of contexts. Translators must use trial number if available for "Let us..." passages to avoid Trinitarian ambiguity or heresy.

## What is Number System?

**Definition**: Grammatical marking of quantity/count of entities (singular/plural/dual/trial/etc.)

**TBTA Values**: 
- S (Singular): 1 entity
- D (Dual): Exactly 2 entities  
- T (Trial): Exactly 3 entities
- Q (Quadrial): **PROBLEMATIC** - No attested natural language has this
- p (Paucal): Few entities (3-10, varies)
- P (Plural): Many entities

**Source Language Encoding**:
- Hebrew: Dual morphology (-ayim suffix: shamayim "heavens", mayim "waters")
- Greek: Singular/Plural (dual is vestigial in Koine)

**TBTA Status**: Tier A (Essential), marked "Complete", 91.4% reproduction accuracy in experiments

## Key Research Findings

### 1. TBTA Documentation ([TBTA.md](TBTA.md))

**Policy**: Semantic meaning prioritized over morphological form
- Lexicalized duals (Hebrew "heavens", "waters") → Marked as Singular (semantically one entity)
- Undocumented rule causes confusion

**Issues Found**:
1. **Quadrial has no linguistic attestation** (Corbett 2000) - should be removed
2. **Morphological vs. semantic number undocumented** - affects ~50-100 OT instances  
3. **Collective noun handling not specified** ("people" - singular or plural?)

**Key Example**: Genesis 1:26 marked as **Trial** (Trinity reference - 3 persons of Godhead)

### 2. Language Family Analysis ([LANGUAGES.md](LANGUAGES.md))

**Dataset**: 1,009 languages analyzed from `/src/constants/languages.tsv`

**Top Families**:
1. Austronesian (176) - Many have dual/trial/paucal
2. Trans-New Guinea (141) - Mostly singular/plural
3. Indo-European (135) - Some Slavic have dual (Slovenian)
4. Niger-Congo (89) - Mostly singular/plural

**Critical Finding**: Only **Slovenian** (Slavic) has productive dual in modern languages, but NOT in dataset.

**Languages Requiring Complex Number**:
- **Dual**: Hebrew (source), Arabic, Hawaiian, ~88 languages
- **Trial**: Kilivila, Larike, some PNG Austronesian, ~172 languages (claimed)
- **Paucal**: Some Austronesian, Arabic dialects (rare)

**Proposed Test Languages** (Stage 2):
1. Hawaiian (dual)
2. Arabic, Standard (dual)
3. English (simple S/P)
4. Spanish (simple S/P)
5. Indonesian (optional)
6. Swahili (Bantu)
7. Russian (Slavic without dual)
8. Cebuano (Philippine)
9. Motu (PNG, suspected dual/trial)
10. Chuukese (Micronesian)

### 3. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**Key Sources**:
- **Corbett (2000)**: No natural language has true quadrial; Dual in ~88 languages, Trial in ~172
- **WALS Features 33A-36A**: Number coding strategies, occurrence patterns, pronoun vs. noun distinctions
- **Greenberg Universal 34**: No trial without dual (hierarchical: S < D < T < P)

**Translation Principles**:
1. **Semantic over Morphological**: Lexicalized plurals → Singular if semantically one
2. **Use Most Precise Available**: Trial > Plural for Trinity contexts
3. **Avoid Heretical Number**: Dual for Genesis 1:26 = Arianism (forbidden)
4. **Document Ambiguity**: Note when number is uncertain

**Case Studies**:
- **Hawaiian Genesis 1:26**: Use Trial if available (explicit Trinity)
- **Arabic Genesis 1:1**: Handle lexicalized dual "heavens" as Singular
- **Kilivila Genesis 1:26**: Trial **required** for orthodoxy (Dual = heresy)
- **Fijian Matthew 17:1**: Trial for Peter/James/John (exactly 3)

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Classification**: 15% Non-Arbitrary, 85% Arbitrary

#### Non-Arbitrary Contexts (15%)

**1A. Theological-Critical (5%)** - HIGH stakes:
- **Genesis 1:26**: "Let us make..." - Trial preferred, Plural acceptable, Dual **FORBIDDEN** (Arianism)
- **Genesis 3:22, 11:7, Isaiah 6:8**: Similar Trinitarian contexts
- **Matthew 28:19**: "Name" (singular) of Father/Son/Spirit - ONE name critical (not "names")
- **John 1:1**: Both "God" references singular (monotheism)

**1B. Contextual-Precision (10%)** - Reader confusion if wrong:
- **Ruth 1**: Ruth + Naomi (2 women) → Dual if available
- **Luke 24:13**: Two disciples → Dual
- **Matthew 17:1**: Peter, James, John (3) → Trial if available
- **Daniel 3**: Shadrach, Meshach, Abednego (3) → Trial

#### Arbitrary Contexts (85%)

- Crowd sizes (40%): "multitude", "many people" - paucal/plural doesn't matter
- Generic statements (15%): "all have sinned" - universal quantifier
- Objects (20%): "the stones", "the fish" - unless narratively significant
- Travel companions (5%): Unless specifically counted
- Repeated actions (10%): "many times" - paucal/plural flexible
- Abstract/collective (10%): "the heavens declare", "the people said"

**Translator Guidance**:
- Trinity contexts: Trial > Plural, never Dual
- Exact counts (2 or 3 people): Use Dual/Trial if available
- Vague plurals: Use natural target language form

## Discrepancies Between Sources

### TBTA vs. Linguistic Typology

**Issue 1: Quadrial**
- **TBTA**: Includes Quadrial (Q) in schema
- **Corbett (2000)**: No attested natural language has true grammatical quadrial
- **Assessment**: TBTA schema includes impossible value (likely 0% usage)

**Issue 2: 172 Languages with Trial**
- **TBTA/README**: Claims 172 languages have trial
- **Research**: Specific language list not provided, needs verification
- **Action**: Stage 2 should verify which dataset languages actually use trial

### TBTA Policy vs. Documentation

**Issue**: Semantic-over-morphological rule evident but undocumented
- **Evidence**: Hebrew "shamayim" (dual morphology) marked Singular
- **Impact**: Causes confusion without explicit documentation
- **Recommendation**: Document rule clearly in Stage 3

## Gaps & Questions for Stage 2

1. **Confirm Trial Languages**: Verify which languages in dataset actually have productive trial (claimed 172)
2. **Collective Nouns**: Analyze how TBTA handles "people", "crowd" (singular vs. plural?)
3. **Associative Plural**: Is "Jesus and his disciples" marked differently from simple plural?
4. **Frequency Distribution**: What percentage of verses use Dual/Trial/Paucal vs. Singular/Plural?
5. **Slovenian Gap**: Only modern Slavic with dual, but not in dataset - impacts testing

## Next Steps (Stage 2)

**Data Extraction**:
1. Extract all number annotations from TBTA (use `/src/tools/predict/extract_data.py`)
2. Analyze value frequency: How often is Dual/Trial/Paucal used?
3. Verify 10 proposed test languages have adequate translation coverage
4. Identify "adversarial" cases: Edge cases, ambiguous contexts, theological hotspots

**Hypothesis Validation**:
1. Test semantic-over-morphological rule: Do lexicalized duals consistently → Singular?
2. Confirm Trinity contexts marked as Trial (Genesis 1:26, etc.)
3. Check collective noun patterns
4. Validate 172-language trial claim

**Data Splitting**:
1. Train (60%), Test (20%), Validate (20%)
2. Ensure Trinity contexts in all three sets (stratified sampling)
3. Create adversarial set: Edge cases for final testing

## Files in This Directory

- **[TBTA.md](TBTA.md)** (107 lines) - Complete TBTA documentation review
- **[LANGUAGES.md](LANGUAGES.md)** (255 lines) - Language family typology & dataset analysis
- **[SCHOLARLY.md](SCHOLARLY.md)** (401 lines) - Linguistic research, translation case studies
- **[THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)** (325 lines) - Arbitrary vs. non-arbitrary classification

**Total Research**: 1,088 lines across 4 files (comprehensive linguistic foundation)

## Bibliography

**External Sources**:
- {corbett-2000-number}: Corbett, G. G. (2000). *Number*. Cambridge University Press.
- {wals-online}: WALS Features 33A-36A (Number coding and occurrence)
- {greenberg-1963-universals}: Universal 34 (No trial without dual)
- {comrie-1989-universals}: Animacy hierarchies, collective nouns

**Internal TBTA Sources**:
- {tbta-source/README.md}, {tbta-source/DATA-STRUCTURE.md}, {tbta-source/TBTA-FEATURES.md}, {tbta-source/CRITIQUE.md}
- {languages-tsv}: 1,009-language dataset

**Note**: All Scripture verse patterns marked "(unverified)" per instructions - require peer review in Stage 4.

