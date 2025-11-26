# Person System: Research Summary

**Feature**: Person System (Grammatical Person + Clusivity)
**TBTA Tier**: A - Essential (affects 1,000+ languages)
**Research Date**: 2025-11-26

## Overview

Person systems encode relationships between discourse participants (speaker, addressee, other) and their grammatical representation. While 1st/2nd/3rd person distinctions are universal, the critical variation for Bible translation is **clusivity** - the inclusive/exclusive distinction in first person plural pronouns.

## Quick Facts

| Aspect | Detail |
|--------|--------|
| **TBTA Values** | 5 codes: 1 (1st ambiguous), 2 (2nd), 3 (3rd), A (1st inclusive), B (1st exclusive) |
| **Global Prevalence** | ~31.5% of languages have clusivity (WALS 200-language sample) |
| **Affected Languages** | 1,000+ languages (TBTA estimate), including 176 Austronesian in dataset |
| **Source Languages** | Hebrew, Greek, English: NO clusivity - interpretive annotations required |
| **Major Families** | Austronesian (near-universal), Australian (non-Pama-Nyungan), Dravidian, Sino-Tibetan (Mandarin) |
| **Theological Stakes** | HIGH - Trinity contexts, prayer theology, apostolic authority |
| **Encoding Position** | Position 10 in noun/pronoun encoding |

## 1. TBTA Documentation Summary

**File**: `TBTA.md` (350 lines)

**Key Findings**:
- Person System = Tier A Essential feature #2 (of 59 total features)
- 8-way system reference = interaction of person (1st/2nd/3rd) × number (singular/plural) × clusivity (inclusive/exclusive)
- Source languages (Hebrew/Greek) **lack clusivity** morphological marking - TBTA annotations are **INTERPRETIVE**
- Examples documented: Genesis 1:26 (First Inclusive + Trial Number), Acts 15:25 (First Exclusive)
- Honorifics (T-V distinction, Japanese keigo) handled by separate Speaker Demographics feature, NOT Person field

**Critical Insight**: TBTA's inclusive/exclusive distinction is the **highest-value annotation** for the 1,000+ clusivity-marking languages, as source texts and major translation languages (English, Arabic, etc.) lack the distinction.

**See**: `research/TBTA.md` for full analysis

## 2. Language Typology Summary

**File**: `LANGUAGES.md` (450 lines)

**Global Distribution** (WALS Feature 39A):
- 63 languages (31.5%): Full inclusive/exclusive distinction
- 120 languages (60%): No distinction (English-type)
- 5 languages (2.5%): Only inclusive marked
- Rare patterns: No "we" concept, "we" = "I" morphologically

**Geographic Patterns**:
- **Nearly Universal**: Austronesian (176 languages in dataset), Australian (non-Pama-Nyungan)
- **Common**: Southeast Asia (Sino-Tibetan, Austroasiatic), South Asia (Dravidian), parts of Americas (Quechuan, some Mesoamerican)
- **Rare/Absent**: Europe (ALL Indo-European lack it), Africa (most Niger-Congo, all Afro-Asiatic), Middle East (Semitic)

**Root Translation Languages**:
- **Only Indonesian/Malay** among major translation languages has clusivity (*kita* inclusive, *kami* exclusive)
- All others lack it: Hebrew, Greek, Latin, English, Spanish, German, French, Arabic, Swahili

**Honorific Systems** (Distinct from Clusivity):
- Japanese keigo (extreme complexity - sonkeigo, kenjōgo, teineigo)
- Korean speech levels
- T-V distinction (European: Spanish *tú*/*usted*, French *tu*/*vous*, German *du*/*Sie*)
- Note: Javanese has BOTH clusivity (Austronesian) AND honorifics (cultural)

**Proposed Languages for Stage 2**:
1. Tagalog (Austronesian - TBTA example, *tayo*/*kami*)
2. Indonesian (Austronesian - major regional language, *kita*/*kami*)
3. Fijian (Oceanic - complex with 4 numbers)
4. Hawaiian (Polynesian - 4-way system with dual clusivity)
5. Vietnamese (Austroasiatic - TBTA example, *chúng ta*/*chúng tôi*)
6. English (Indo-European - baseline, no clusivity)
7. Spanish (Indo-European - major translation language)
8. Swahili (Niger-Congo - African representative)
9. Alyawarr (Australian Arandic - has I/E distinction unlike related Arrernte)
10. Mandarin Chinese (Sino-Tibetan - major language, *zánmen*/*wǒmen*)

**See**: `research/LANGUAGES.md` for full typological analysis

## 3. Scholarly Research Summary

**File**: `SCHOLARLY.md` (500+ lines)

**27+ Sources** covering:

**Clusivity Typology**:
- Cysouw (2013) WALS Feature 39A - baseline typology
- Filimonova (2005) *Clusivity* edited volume - comprehensive case studies
- Siewierska (2004) *Person* - 700+ language survey

**Grammatical Features**:
- Corbett (2000) *Number*, (2006) *Agreement*, (2012) *Features* - interaction with number systems
- Comrie (1989) *Language Universals* - animacy hierarchy, person reference

**Honorifics & Politeness** (Separate from Clusivity):
- Brown & Levinson (1987) *Politeness* - T-V distinction, honorific theory
- Brown & Gilman (1960) - "power and solidarity" dynamics
- Ide (1989) - Japanese *wakimae* (discernment) vs. volitional politeness

**Specialized Person Systems**:
- Clements (1975), Hagège (1974) - logophoric pronouns (West African)
- Obviative systems - Algonquian "fourth person" (proximate/obviative)

**Biblical Languages**:
- Hebrew grammar sources - confirm no clusivity in Biblical Hebrew
- Greek grammar sources - confirm no clusivity in Koine Greek

**Bible Translation**:
- SIL International (1999) - NT clusivity decisions, documented translation variation
- TIPs database - multiple examples (Luke 9:33 debate, Matthew 6:9 correction)

**Translation Case Studies**:

1. **Genesis 1:26** ("Let us make"): Trial number + First Inclusive (Trinitarian) for Kilivila, Larike, Fijian
2. **Acts 15:25** ("It seemed good to us"): First Exclusive (apostles, not congregation) - documented TBTA example
3. **Matthew 6:9** ("Our Father"): First Exclusive (excluding God) - early missionaries used inclusive (error, corrected)
4. **1 Corinthians 1:1**: Debate - Pickett/Cowan say inclusive (Paul + readers), SIL says exclusive (Paul + Sosthenes)

**Key Insight**: Translators disagree on clusivity even with guidance - demonstrates critical need for TBTA verse-level annotations.

**See**: `research/SCHOLARLY.md` for full bibliography and case studies

## 4. Theological Significance Summary

**File**: `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` (500 lines)

**Default Classification**: 85% arbitrary (straightforward person marking)

**Non-Arbitrary Contexts**: 15% (clusivity precision required)

### 1A: Non-Arbitrary-Theological (5% - HIGH stakes)

**Trinity Contexts**:
- Genesis 1:26, 3:22, 11:7 - "Let us" in divine speech - First Inclusive preferred (intra-Trinitarian dialogue)
- Isaiah 6:8 - Mixed "I"/"us" - First Inclusive preferred (threefold "Holy" = Trinity)
- Stakes: Heretical alternatives (divine council, polytheism, Binitarianism) must be avoided

**Prayer Theology**:
- Matthew 6:9-13 / Luke 11:2-4 - "Our Father" - **MUST** be First Exclusive (excluding God, the addressee)
- Stakes: Inclusive form is heretical (implies God prays to himself) - early missionary error documented

**Apostolic Authority**:
- Acts 15:25, 15:28 - Jerusalem Council - First Exclusive (apostles excluding congregation)
- Stakes: Wrong choice implies congregation participated in apostolic decision-making

### 1B: Non-Arbitrary-Contextual (10% - MEDIUM stakes)

**Epistolary "We"** (Pauline letters with co-authors):
- 1 Corinthians, 2 Corinthians, Philippians, Colossians, 1-2 Thessalonians
- NO single answer - varies by context within same letter
- Requires verse-by-verse analysis: Paul alone? Paul + co-authors? Paul + readers?

**Disciple Speech to Jesus**:
- Luke 9:33 - documented translation variation (some exclusive, some inclusive)
- Contextual determination needed

**Hebrews Exhortations**:
- "Let us..." passages - First Inclusive (author + readers together)

### Arbitrary Contexts (85%)

- Third person narratives (60%) - no clusivity
- Second person commands (20%) - no clusivity (honorifics handled separately)
- First person singular (10%) - no clusivity
- Generic statements (5%) - stylistic choice

**See**: `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for full classification

## 5. Key Discrepancies and Debates

### Between TBTA and Research

**Genesis 1:26 Person**: TBTA says "First Inclusive" (per DATA-STRUCTURE.md), but theological interpretation varies:
- Inclusive = intra-Trinitarian dialogue (Trinity members addressing each other)
- Alternative: Exclusive interpretation possible if different theological framework
- **Resolution needed**: Confirm Trinitarian interpretation rationale

### Between Translation Experts

**1 Corinthians 1:1 Clusivity**: SIL (1999) says exclusive, Pickett/Cowan say inclusive - demonstrates ongoing debate even among experts

**Luke 9:33 ("Good for us to be here")**: Multiple translations made opposite choices (some inclusive of Jesus, some exclusive)

### Between Christian Traditions

**Trinity Contexts**: All Christian traditions (Protestant, Catholic, Orthodox) affirm Trinitarian interpretation of Genesis 1:26, but clusivity mechanics (inclusive vs. exclusive encoding) not explicitly discussed in traditional theology

**Recommended Action**: Stage 2 theological review with multi-denominational input

## 6. Critical Gaps Identified

1. **Verse-Level Annotation Coverage**: Need exhaustive list of all first person plural verses requiring clusivity determination (estimated 5-15% of Bible)

2. **Decision Tree**: Create algorithmic decision tree for inclusive vs. exclusive determination based on discourse participants

3. **Epistolary Analysis**: Systematic analysis of Pauline "we" in each letter context

4. **Frequency Data**: Stage 2 should validate estimated percentages (85% arbitrary, 15% non-arbitrary)

5. **Cross-Denominational Review**: Theological consensus on Trinity clusivity encoding

6. **Obviative/Logophoric**: TBTA doesn't encode these (Algonquian, West African) - consider adding for languages that require it?

## 7. Recommended Next Steps (Stage 2)

1. **Data Analysis**: Extract all first person plural contexts from TBTA annotations, validate clusivity assignments

2. **Frequency Study**: Confirm percentages for inclusive, exclusive, ambiguous contexts

3. **Translation Validation**: Test TBTA annotations against published translations in clusivity-marking languages (Tagalog, Malay, Fijian Bibles)

4. **Theological Review**: Convene panel (biblical scholars, systematic theologians, translators) to review Trinity contexts and prayer theology clusivity

5. **Decision Algorithm**: Create decision tree for clusivity determination based on discourse participant analysis

6. **Epistolary Mapping**: Analyze each Pauline epistle's "we" usage systematically

7. **Expansion**: Consider adding logophoric/obviative annotations for languages requiring them

## 8. Bibliography Summary

**Typological Databases**:
- WALS Feature 39A (Cysouw) - clusivity typology
- WALS Feature 40A - verbal inflection
- Grambank GB167 - logophoric pronouns
- APiCS Feature 15 - clusivity in creoles

**Major Monographs**:
- Siewierska (2004) *Person*
- Corbett (2000) *Number*, (2006) *Agreement*, (2012) *Features*
- Comrie (1989) *Language Universals*
- Filimonova (2005) *Clusivity* (edited volume)

**Bible Translation**:
- SIL International (1999) - NT clusivity decisions
- TIPs database - translation examples

**Full Bibliography**: See `research/SCHOLARLY.md`

---

**Research Complete**: All four research files completed
**Total Lines**: ~2,000 lines across four files
**Sources**: 27+ scholarly sources, 4 typological databases, 4+ translation case studies
**Next Stage**: Data analysis, frequency validation, theological review
