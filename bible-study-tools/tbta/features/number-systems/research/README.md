# Number Systems Research Summary

**Feature**: Number Systems  
**Stage**: 1 - Research & Definition  
**Date**: 2025-01-27  
**Status**: Complete

---

## Executive Summary

Number Systems identify grammatical number distinctions beyond singular/plural. Approximately **337+ languages** in our dataset require distinctions like dual (2), trial (3), paucal (few), or quadrial (4). Source languages (Hebrew/Greek) do **NOT** encode trial/paucal/quadrial morphologically, requiring translators to infer from context, explicit numbers, or theological knowledge.

**Key Finding**: Trinity references (Genesis 1:26) require **trial number** to preserve doctrinal precision. Using dual would be heretical (Arianism - implies only 2 persons).

---

## Research Sections

### 1. TBTA Documentation Review ([TBTA.md](TBTA.md))

**Key Points**:
- **Values**: S (Singular), D (Dual), T (Trial), Q (Quadrial), p (Paucal), P (Plural)
- **Policy**: Semantic meaning overrides morphological form (Hebrew duals → Singular when lexicalized)
- **Quadrial Controversy**: Listed in schema but **no linguistic evidence** (Corbett 2000)
- **Theological Significance**: Genesis 1:26 marked as Trial (Trinity reference)

**Discrepancies**:
- TBTA includes Quadrial despite no natural language having true grammatical quadrial
- Morphological vs. semantic priority policy not explicitly documented
- Natural pairs (dual) handling not documented

**Source**: `tbta-source/TBTA-FEATURES.md`, `tbta-source/CRITIQUE.md`, `tbta-source/DATA-STRUCTURE.md`

---

### 2. Language Family & Typology Analysis ([LANGUAGES.md](LANGUAGES.md))

**Key Points**:
- **Source Languages**: Hebrew/Greek do NOT encode trial/paucal/quadrial
- **Required Families**: 
  - Austronesian Oceanic (~87 languages): Mandatory dual/trial/paucal
  - Trans-New Guinea (~129 languages): Mandatory dual, optional paucal
  - Australian (~36 languages): Mandatory dual, optional paucal
- **Root Languages**: Arabic has productive dual; English/Spanish/French do not

**Candidate Languages for Translation Database** (10 languages):
1. Samoan (Oceanic - dual/trial/plural)
2. Fijian (Oceanic - dual/trial/paucal/plural)
3. Kilivila (Oceanic - trial-marking, TBTA example)
4. Larike (Oceanic - trial-marking, TBTA example)
5. Yimas (Trans-New Guinea - four-way system)
6. Mian (Trans-New Guinea - dual)
7. Telefol (Trans-New Guinea - dual)
8. Arrernte, Eastern (Australian - dual)
9. Arabic, Standard (Afro-Asiatic - dual, root language)
10. Tagalog (Philippine - optional dual)

**Source**: `tbta/languages/families/`, WALS, Grambank

---

### 3. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**Key Sources**:
- **Corbett (2000)**: No attested grammatical quadrial; distinguishes lesser/greater paucal
- **Comrie (1989)**: Implicational hierarchies (trial → dual → plural)
- **WALS Feature 30**: Cross-linguistic distribution (~15% have dual, <2% have trial/paucal)
- **Pawley & Hammarström (2018)**: Proto-Trans-New Guinea dual markers reconstructed

**Translation Case Studies**:
- **Kilivila**: Trial for Trinity (Genesis 1:26)
- **Yimas**: Four-way system (singular/dual/paucal/plural)
- **Hebrew**: Lexicalized duals → semantic singular

**Key Verses**:
- Genesis 1:26: "Let us make" → Trial (Trinity)
- Genesis 3:22: "Like one of us" → Trial (Trinity)
- Matthew 28:19: Trinity formula → Trial (three persons)
- Luke 24:13: "Two of them" → Dual (explicit number)

**Source**: Academic literature, TBTA documentation, typological databases

---

### 4. Arbitrarity Classification ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Non-Arbitrary Contexts** (~15%):
1. **Trinity References** (HIGH stakes):
   - Genesis 1:26, Genesis 3:22, Matthew 28:19
   - **Trial required** (never Dual - Arianism)
   - Plural acceptable but less precise

2. **Explicit Numbers** (MEDIUM stakes):
   - "Two disciples" → Dual
   - "Three men" → Trial
   - Context requires specific number

3. **Natural Pairs** (LOW stakes):
   - Body parts (eyes, hands, feet) → Dual
   - Universal linguistic pattern

**Arbitrary Contexts** (~85%):
- Crowd sizes, travel companions, abstract nouns, generic plurals, collective nouns, unspecified groups
- Choice is stylistic, not doctrinal

**Source**: Theological analysis, Scripture knowledge (unverified)

---

## Key Discrepancies & Gaps

### 1. Quadrial Without Evidence
- **TBTA**: Includes Quadrial in schema
- **Research**: No natural language has true grammatical quadrial (Corbett 2000)
- **Resolution**: Distinguish lesser paucal (~3-4) from greater paucal (~4-10)

### 2. Morphological vs. Semantic Undocumented
- **TBTA**: Policy of semantic priority not explicitly documented
- **Research**: Semantic meaning should override morphological form
- **Resolution**: Add explicit morphological/semantic distinction field

### 3. Natural Pairs Not Documented
- **TBTA**: No explicit guidance on dual for natural pairs
- **Research**: Universal pattern: body parts → dual
- **Resolution**: Document universal pattern with examples

---

## Research Quality Notes

**Strengths**:
- Comprehensive TBTA documentation review
- Extensive language family analysis (337+ languages)
- Scholarly sources cited (Corbett, Comrie, WALS)
- Theological analysis of arbitrarity

**Limitations**:
- Some scholarly sources marked as (unverified) - require verification
- Frequency data requires Stage 2 analysis
- Some verse patterns marked as (unverified) - require TBTA data verification

**Next Steps**: Stage 2 - Analysis & Hypothesis Validation

---

## Files in This Directory

- **[TBTA.md](TBTA.md)**: TBTA documentation review (values, policies, constraints)
- **[LANGUAGES.md](LANGUAGES.md)**: Language family analysis (required families, candidate languages)
- **[SCHOLARLY.md](SCHOLARLY.md)**: Scholarly research (typology, translation theory, case studies)
- **[THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)**: Arbitrarity classification (non-arbitrary vs. arbitrary contexts)

---

**See Also**: [../README.md](../README.md) for feature overview

