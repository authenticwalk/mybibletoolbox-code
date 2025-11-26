# Quadrial Investigation - Quick Summary

## The Problem
185 entries labeled "Quadrial" but no natural language has true quadrial grammatical number.

## The Finding
**TBTA's "Quadrial" is a SEMANTIC annotation, not grammatical.**

Every Quadrial entry refers to a noun that semantically represents a group of exactly 4 items:
- "four kings" → constituent: king (marked Quadrial)
- "four rivers" → constituent: river (marked Quadrial)  
- "four sons" → constituent: son (marked Quadrial)
- "four corners" → constituent: corner (marked Quadrial)

## Evidence
1. ✅ **100% pattern match**: All 185 entries refer to groups of 4
2. ✅ **Explicit numerals**: Most verses contain the word "four"
3. ✅ **Generic nouns**: king (38x), man (26x), son (17x) - not quadrial inflections
4. ✅ **Trial parallel**: Trial entries follow same pattern (groups of 3)
5. ✅ **Source languages**: Hebrew/Greek have no quadrial morphology

## Example Breakdown

**Genesis 14:2** - "four kings: Bera king of Sodom, Birsha king of Gomorrah, Shinab king of Admah, Shemeber king of Zeboyim"
- Quadrial labels: `king` (5 instances in surrounding verses)
- Pattern: Each instance of "king" labeled Quadrial because verse lists 4 kings

**Exodus 25:26** - "Make four gold rings...at the four corners...on its four feet"  
- Quadrial labels: `ring`, `corner`, `leg` (5 total)
- Pattern: All nouns related to count of 4

**Genesis 1:26** (Trial for comparison) - "Let us make man in our image"
- Trial labels: `God` (3 instances)  
- Pattern: Trinity interpretation (3 persons)

## Verdict

| Question | Answer |
|----------|--------|
| Is data valid? | ✅ YES - correctly identifies groups of 4 |
| Is data useful? | ⚠️ QUESTIONABLE - verse already says "four" |
| Is terminology accurate? | ❌ NO - "Quadrial" implies grammatical category |
| Should it be reclassified? | ✅ YES - see recommendations |

## Recommendation

**Option 1 (BEST)**: Reclassify as Plural + semantic metadata
```yaml
label: Plural
semantic_count: 4
```

**Option 2**: Rename to "Semantic-Four" to avoid grammatical confusion

**Option 3**: Document clearly that Q/T are semantic, not grammatical

**Option 4**: Remove entirely (verse text already contains "four")

## Key Insight

TBTA mixes two different systems:
1. **Grammatical** number: S/D/P (based on Hebrew/Greek morphology)
2. **Semantic** counting: T/Q (based on actual referent count)

This creates confusion because linguistic categories are being used inconsistently.

---

**Full Report**: See `quadrial-investigation-report.md`
**Status**: Research complete, awaiting Stage 3 decision
**Date**: 2025-11-26
