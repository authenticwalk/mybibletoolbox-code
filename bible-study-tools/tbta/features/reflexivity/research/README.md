# Reflexivity Feature: Research Summary

## What is Reflexivity?

**Reflexivity** marks whether an action affects the subject itself (reflexive) or involves mutual action (reciprocal).

**Values**: `r` (Reflexive), `R` (Reciprocal), `N` (Not applicable)

**Note**: TBTA-FEATURES.md lists only 2 values but DATA-STRUCTURE.md reveals all 3.

## Research Overview

**Total**: 1800+ lines across 5 files, 27+ scholarly sources

### 1. TBTA Documentation → [TBTA.md](TBTA.md)

**Key Facts**: Position 5 in verb code, ~45 entries (0.4% of corpus)

**Critical Gaps**:
- Greek middle voice policy undefined (deponent verb handling?)
- Hebrew Hitpael/Niphal treatment unclear
- Semantic vs. morphological priority not stated

**See**: TBTA.md for complete gap analysis and policy recommendations

### 2. Language Typology → [LANGUAGES.md](LANGUAGES.md)

**Source Languages**: ✅ Both Greek (middle voice) and Hebrew (Hitpael/Niphal) mark morphologically

**Cross-Linguistic Variation**:
- WALS 47A: 56% show reflexive-intensifier identity
- WALS 106A: Reflexive-reciprocal polysemy NOT universal (Hindi distinguishes)

**Encoding Strategies**:
1. Verbal affixes (Russian -ся, Spanish *se*)
2. Reflexive pronouns (English *himself*, German *sich*)
3. Verb derivation (Hebrew Hitpael, Greek middle)
4. Zero-marking (Chinese, Japanese)

**Control Languages** (10 from dataset): Belarusian, Assamese, Arabic, Albanian, Akan, Tagalog, Ethiopian Semitic, Bengali, Mayan

**See**: LANGUAGES.md for detailed typology and language profiles

### 3. Scholarly Research → [SCHOLARLY.md](SCHOLARLY.md)

**Major Sources** (27+):
- Typology: Kemmer (1993), Haspelmath (2008, 2023), König & Siemund (2000)
- Greek: Allan (2003) - 11 middle voice types, Wallace (1996)
- Hebrew: UHG, van Wolde (2017) - Niphal as middle voice

**Translation Case Studies**:

| Verse | Construction | TBTA Value |
|-------|-------------|-----------|
| Gal 2:20 | Active + ἑαυτόν | **r** (emphatic reflexive) |
| John 13:34 | Active + ἀλλήλους | **R** (explicit reciprocal) |
| 1 Cor 13:8 | Middle voice | **N** (deponent) |

**See**: SCHOLARLY.md for all 27+ sources and 6 detailed case studies

### 4. Theological Significance → [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

**Default**: 85%+ arbitrary (stylistic)

**Non-Arbitrary (15%)** - 8 groups:

**HIGH STAKES**:
- Christological self-sacrifice (Gal 2:20, Eph 5:25) - atonement theology
- Christ's self-consecration (John 17:19) - high priestly work
- Kenosis (Phil 2:7-8) - voluntary self-emptying

**MEDIUM-HIGH**:
- Mutual love commands (John 13:34-35) - defining mark of believers
- Mutual submission (Eph 5:21) - reciprocal explicit

**MEDIUM**:
- Mutual forgiveness, encouragement, edification commands

**See**: YAML file for complete classification with doctrinal bases

## Key Findings

### Agreements Across Sections

✅ Source languages mark reflexivity morphologically
✅ Deponent verbs NOT semantically reflexive
✅ Theological stakes exist in ~15% of cases
✅ Most instances stylistically arbitrary

### Discrepancies Identified

⚠️ **Documentation**: TBTA lists 2 values, actual encoding uses 3 (includes Reciprocal)
⚠️ **Policy gap**: No middle voice interpretation policy (11 types per Allan, not all reflexive)
⚠️ **Frequency**: ~45 entries seems low; unclear if incomplete or genuinely rare

### Critical Challenges for Stage 2

1. **Deponent identification**: Need list to filter from reflexive marking
2. **Hebrew ambiguity**: Hitpael = reflexive OR reciprocal OR iterative (context-dependent)
3. **Implicit reciprocals**: When to mark plural middle as reciprocal?
4. **Data expansion**: Only 0.4% of corpus annotated
5. **Consistency check**: Verify semantic vs. morphological policy in existing data

## Stage 2 Recommendations

**Priority Actions**:
1. Create Greek deponent verb list → mark as N
2. Analyze Hitpael/Niphal patterns in existing TBTA data
3. Verify ~45 entry count and r/R/N distribution
4. Build translation database for 10 control languages
5. Test high-stakes theological passages (Gal 2:20, John 13:34, etc.)

**Algorithm Insights**:
- Source language provides strong signal (Greek middle, Hebrew Hitpael)
- BUT semantic analysis required (not all middle = reflexive)
- Theological contexts need 100% accuracy (~15% of cases)
- Target language variation high (mandatory vs. optional marking)

## Research Files

- **TBTA.md** (350 lines): Documentation review, gap analysis
- **LANGUAGES.md** (400 lines): Typology, 10 control languages
- **SCHOLARLY.md** (600 lines): 27+ sources, case studies
- **THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml** (400 lines): Arbitrary classification
- **README.md** (this file): Executive summary

**Total**: 1800+ lines, 27+ sources, comprehensive coverage

---

**Stage 1**: ✅ Complete | **Next**: Stage 2 Analysis
**Updated**: 2025-11-29
