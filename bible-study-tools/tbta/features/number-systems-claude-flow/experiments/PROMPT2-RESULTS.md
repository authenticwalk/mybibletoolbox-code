# PROMPT2 Results & Root Cause Analysis

**Version**: PROMPT2.md
**Date**: 2025-11-18
**Commit SHA**: 72850d1
**Total Verses**: 197 (Note: Only 197/236 in answer set!)

---

## Overall Performance

### Accuracy Metrics

**Overall Accuracy**: 42.1% (83/197 correct)
**Result**: ⚠️ **MAJOR FAILURE** (Target: 95%, Gap: 52.9%)
**vs PROMPT1**: Only +2.7% improvement (39.4% → 42.1%)

### Performance by Category

**By Number Value**:
- Singular: 84.0% (42/50) ⚠️ - Only good category
- Dual: 31.9% (15/47) ❌
- Trial: 45.9% (17/37) ❌
- Quadrial: 25.0% (2/8) ❌
- Paucal: 23.1% (3/13) ❌
- Plural: 9.5% (4/42) ❌ **CATASTROPHIC**

**By Confidence Level**:
- Very High: 57.0% (57/100) - Still overconfident!
- High: 60.0% (3/5)
- Low: 26.0% (19/73)
- Very Low: 21.1% (4/19)

**By Genre**:
- Epistle: 49.4% (42/85) - Worse than expected
- Narrative: 40.7% (35/86) - Failed
- Prophecy: 33.3% (5/15)
- Law: 11.1% (1/9)
- Wisdom: 0.0% (0/2)

**By Algorithm Level**:
- Level 1 (Trinity): 100.0% (1/1) ✅ **ONLY SUCCESS**
- Level 2 (Explicit numbers): 59.7% (46/77) ❌ **SHOULD BE 90%+!**
- Level 3 (Epistle patterns): 48.1% (13/27) ❌
- Level 6 (Fallbacks): 25.0% (23/92) ❌

---

## Root Cause Analysis

### CRITICAL FLAW: Wrong Referent Detection!

**The Problem**: PROMPT2 detects **any noun** in the verse, not the **actual numbered referent**.

**Example 1: 1TH.002.002**
- English: "**We** dared to tell you his **gospel**"
- PROMPT2 detected: "gospel" (abstract noun) → Predicted: **Singular**
- Actual referent: "**We**" (pronoun) → Actual: **Plural**
- ❌ Algorithm looked at wrong word!

**Example 2: 1SA.014.012**
- English: "**Jonathan and his armor-bearer**" (two specific people)
- PROMPT2 detected: "men" (generic plural) → Predicted: **Plural**
- Actual referent: "**Jonathan and his armor-bearer**" (named pair) → Actual: **Dual**
- ❌ Algorithm looked at wrong noun!

**Example 3: DAN.003.016**
- English: "**Shadrach, Meshach and Abednego** replied"
- PROMPT2 detected: No explicit number → Predicted: **Singular** (fallback)
- Actual referent: Three named people → Actual: **Trial**
- ❌ Algorithm missed the list of names!

### Why PROMPT2 Failed

**Assumption**: Number system tracks "the main counted thing in the verse"
**Reality**: Number system tracks **the main participant/subject** (grammatical subject or topic)

**What PROMPT2 Did**:
- Searched for ANY number word ("two", "three", "many") anywhere in verse
- Searched for ANY noun that matched patterns ("gospel", "believers")
- Searched for generic words ("hands", "crowd")

**What PROMPT2 Should Have Done**:
- Identify the **grammatical subject** of the main clause
- Check if subject is pronoun ("we", "they", "he") → map to number
- Check if subject is a list of names (Name1, Name2, Name3) → count them
- Check if subject has possessive paired body parts ("his hands") → dual
- Focus ONLY on the main participant, ignore other nouns

---

## Top 3 Error Patterns

### 1. Singular → Plural (34 errors, 29.8%)

**Pattern**: Epistles with plural pronouns ("we", "they", "you all") mis-classified as Singular

**Examples**:
- 1TH.002.002: "**We** dared" - Actual: Plural (we = plural pronoun)
- 1TH.002.008: "**we** cared for you" - Actual: Plural
- 1TH.001.009: "**they** themselves report" - Actual: Plural

**Root Cause**: Algorithm detected "gospel" (abstract) instead of "we" (pronoun)

**Fix for PROMPT3**: Add Level 1.5: **Pronoun Detection** (highest priority after Trinity)

### 2. Plural → Dual (21 errors, 18.4%)

**Pattern**: Narratives with two named participants mis-classified as Plural

**Examples**:
- 1SA.014.012: "**Jonathan and his armor-bearer**" - Actual: Dual (two people)
- GEN.027.023: "**his hands**" - Actual: Dual (paired body part)

**Root Cause**: Algorithm missed "X and Y" pattern, hit fallback instead

**Fix for PROMPT3**: Add **"X and Y" pattern detection** (two named entities)

### 3. Singular → Trial (10 errors, 8.8%)

**Pattern**: Verses with three named participants mis-classified as Singular

**Examples**:
- DAN.003.016: "**Shadrach, Meshach and Abednego**" - Actual: Trial (three names)
- COL.004.011: Mentions three people by name - Actual: Trial

**Root Cause**: Algorithm missed comma-separated name lists

**Fix for PROMPT3**: Add **"X, Y and Z" pattern detection** (three named entities)

---

## Why Level 2 (Explicit Numbers) Only Got 59.7%?

**Expected**: 90%+ (explicit "two", "three", "four" should be easy!)
**Actual**: 59.7% (46/77)

**Problem**: Detecting numbers in WRONG CONTEXT

**Example Failures**:
- "**We** had **two** options" - Detected "two" but referent is "we" (plural), not "options" (dual)
- "**They** went to **three** cities" - Detected "three" but referent is "they" (plural), not "cities" (trial)

**Solution**: Numbers must apply to the **grammatical subject**, not any noun phrase!

---

## Proposed Solutions for PROMPT3

### Solution 1: Pronoun Detection (CRITICAL - Fixes 34+ errors)

**Priority**: HIGHEST (before explicit numbers!)

**Add Level 1.5: Pronoun Analysis**
```
IF main subject is pronoun:
  - "I", "me", "my" → Singular
  - "he", "she", "it", "him", "her" → Singular
  - "we", "us", "our" → Plural
  - "they", "them", "their" → Plural (unless context shows 2-4)
  - "you" → Check context:
    * "you all", "you who" → Plural
    * Singular context → Singular
```

**Expected Impact**: +20-25 percentage points (fixes epistles!)

### Solution 2: Named Entity Lists (Fixes 31+ errors)

**Add before explicit number detection**:
```
IF text contains list of proper names:
  - "Name1 and Name2" → Dual (two people)
  - "Name1, Name2 and Name3" → Trial (three people)
  - "Name1, Name2, Name3 and Name4" → Quadrial (four people)
  - "Name1, Name2, ... (5-10 names)" → Paucal
  - "Name1, Name2, ... (11+ names)" → Plural
```

**Expected Impact**: +15-20 percentage points (fixes narratives/prophecy!)

### Solution 3: Subject Identification

**Change algorithm fundamentally**:
- Step 1: Identify grammatical subject (pronoun, named entity, or noun phrase)
- Step 2: Apply number detection ONLY to the subject
- Step 3: Ignore all other nouns in the verse

**Expected Impact**: +10-15 percentage points (reduces noise!)

### Solution 4: Explicit Number Refinement

**Change from**:
- Search for "two" anywhere in verse

**Change to**:
- Search for "two" modifying the SUBJECT:
  * "**two men** came" → Dual (subject is "two men")
  * "He brought **two gifts**" → Singular (subject is "he", not gifts)

**Expected Impact**: +10-15 percentage points (reduces false positives!)

---

## Lessons Learned

### What Worked
1. ✅ Trinity detection: Still 100% (1/1)
2. ✅ Singular pronouns: When detected, were accurate

### What Failed
1. ❌ **Referent identification**: Looked at wrong nouns
2. ❌ **Epistle collective nouns**: Should have looked at "we"/"they" instead
3. ❌ **Narrative pairs**: Missed "X and Y" patterns completely
4. ❌ **Named entity lists**: Didn't count comma-separated names

### Key Insight

**Number systems are GRAMMATICAL, not LEXICAL!**

- Number tracks the **grammatical subject** of the clause
- Pronouns are the #1 indicator ("we" → Plural, "he" → Singular)
- Named lists must be counted (Shadrach, Meshach, Abednego = 3 = Trial)
- Explicit numbers ONLY count if they modify the subject
- All other nouns in the verse are IRRELEVANT to number value!

This is why PROMPT1 and PROMPT2 both failed - they were doing **lexical search** (find words) instead of **grammatical analysis** (identify subject, analyze its number)

---

## PROMPT3 Strategy

**Complete Redesign Required**:

1. **NEW Level 1: Pronoun Subject** (HIGHEST PRIORITY)
   - Detect "I/he/she" → Singular
   - Detect "we/they" → Plural
   - Handles 80%+ of epistles!

2. **NEW Level 2: Named Entity Lists**
   - "Name1 and Name2" → Dual
   - "Name1, Name2 and Name3" → Trial
   - Handles 50%+ of narratives/prophecy!

3. **REFINED Level 3: Explicit Numbers on Subject**
   - "Two men came" → Dual (number modifies subject)
   - "He saw two birds" → Singular (number doesn't modify subject)
   - Only 59.7% now, should reach 85%+ with this fix

4. **Keep Level 4-6** from PROMPT2 (epistle abstract, body parts, fallbacks)

**Expected PROMPT3 Accuracy**: 80-90%
**If still < 95%**: May need PROMPT4 with discourse analysis

---

## Next Steps

1. ✅ Document findings in PROMPT2-RESULTS.md (COMPLETE)
2. Develop PROMPT3.md with pronoun/subject analysis
3. Apply PROMPT3 to train set
4. Re-score and iterate until ≥95%
5. Test on test set

---

**Status**: ✅ Analysis Complete
**Recommendation**: Major redesign for PROMPT3 - focus on grammatical subjects
**Expected Final Accuracy**: 85-95% (with 2-3 more iterations)
**Created**: 2025-11-18 05:50 UTC
