# Number Systems Feature - Final Summary

**Date**: 2025-11-20
**Status**: Production (Tier 1 only) - Research Complete
**Best Accuracy**: 42.1% (all contexts) | 89.5% (high-confidence)

## All Approaches Attempted

### v1 (PROMPT1): Reference-Only Baseline
- **Accuracy**: 39.4%
- **Approach**: Verse reference + TBTA definition
- **Result**: Established non-arbitrary detection works (100% Trinity)

### v2 (PROMPT2): English Text Analysis
- **Accuracy**: **42.1%** ← BEST
- **Approach**: Verse text + explicit numbers + genre
- **Result**: Hit ceiling - English insufficient for 6 categories
- **Deployed**: Tier 1 (high-confidence contexts only)

### v3 (PROMPT3): Grammatical Subject Analysis
- **Accuracy**: 31.0% (WORSE than v2)
- **Approach**: Identify grammatical subject + analyze
- **Result**: Confirmed ceiling, not algorithm problem

### v4: Greek/Hebrew Morphology (Macula)
- **Status**: ABANDONED (wrong approach)
- **Discovery**: TBTA tracks SEMANTIC participants, not grammatical morphology
- **Example**: LUK 5:2 "fishermen" = Greek PLURAL (grammar) but TBTA PAUCAL (semantics)

### v5: Translation Agreement (eBible)
- **Status**: ABANDONED (insufficient data)
- **Issue**: Only 1 trial language available (Tok Pisin)
  - Samoan, Fijian, Slovenian, Upper Sorbian NOT in eBible
  - Tok Pisin uses trial rarely (2 instances)
  - GEN 1:26 uses "yumi" (ambiguous) NOT "yumitripela" (trial)
- **Need**: Multiple trial/dual languages for agreement threshold

## Fundamental Limitation Identified

**TBTA Number tracks SEMANTIC PARTICIPANTS** ("how many people/things being talked about")

**English grammatically marks only 2 categories**:
- Singular (book, boat)
- Plural (books, boats)

**TBTA requires 6 categories**:
- Singular, Dual (2), Trial (3), Paucal (few), Plural (many), Quadrial (4)

**We cannot distinguish these from English alone** because:
- "Two boats" → English = Plural, but TBTA could be Dual OR Paucal
- "Three men" → English = Plural, but TBTA could be Trial OR Paucal
- "Few disciples" → English = Plural, but TBTA could be Paucal OR Plural

## Why Greek/Hebrew Morphology Doesn't Solve It

Greek/Hebrew mark GRAMMATICAL number, but TBTA annotates SEMANTIC participants:

**Example (LUK 5:2)**:
- Greek morphology: "ἁλεεῖς" (fishermen) = **PLURAL**
- TBTA annotation: "person" (the fishermen) = **PAUCAL** (small group fishing)
- TBTA annotation: "boat" (two boats) = **DUAL** (exactly 2 boats)

Greek says "plural fishermen", but TBTA says "paucal people doing the fishing".

## What Works (89.5% Tier 1)

1. **Trinity contexts (100%)**:  Gen 1:26, Gen 3:22, Gen 11:7 → Trial
2. **Epistle abstract nouns (84%)**: faith, grace, love → Singular
3. **Explicit "four" (62.5%)**: Quadrial detection

## Path to 95% Accuracy

Would require ONE of:

1. **TBTA annotation guidelines** - Understand their semantic criteria
2. **Multiple trial/dual translations** - Samoan + Fijian + Slovenian (not in eBible)
3. **Statistical ML** - Train on 10,000+ annotated verses (accept 70-80% ceiling)
4. **Annotator agreement study** - How do human annotators decide Dual vs Paucal?

## Production Status

**DEPLOYED**: Tier 1 (high-confidence contexts)
**ACCURACY**: 89.5% on 19 verses (8.1% of dataset)
**VALUE**: Prevents 17 theological translation errors

**NOT DEPLOYED**: Tier 2 (general prediction)
**ACCURACY**: 42.1% overall insufficient for production

## Investigations Complete

All reasonable approaches exhausted with available data:
- ✅ English text analysis (v1-v3)
- ✅ Greek/Hebrew morphology (v4) - wrong data type
- ✅ Translation agreement (v5) - languages unavailable

**Conclusion**: 42.1% represents fundamental English-only data ceiling, not algorithmic failure.
