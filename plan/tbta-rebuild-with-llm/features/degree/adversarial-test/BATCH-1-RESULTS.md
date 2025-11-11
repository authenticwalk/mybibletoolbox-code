# Batch 1 Results: Algorithm v2.0 Testing (Verses 8-20)

**Date**: 2025-11-09
**Algorithm**: v2.0 (commit 3a3851d)
**Verses tested**: 5 of 13 (8 unavailable in TBTA export)
**Accuracy**: **40% (2/5 correct)** ❌

---

## Performance Summary

| Verses 1-7 (original) | v1.0 | v2.0 |
|-----------------------|------|------|
| Accuracy | 42.9% (3/7) | 100% (7/7) ✅ |

| Verses 8-12 (batch 1) | v2.0 |
|-----------------------|------|
| Accuracy | **40% (2/5)** ❌ |

**Overall v2.0**: 75% (9/12 verses correct)

---

## Verse-by-Verse Results

### ✅ CORRECT: Verse 18 - Matthew 18:1 "who is greatest"

**Greek**: τίς ἄρα μείζων ἐστὶν ἐν τῇ βασιλείᾳ τῶν οὐρανῶν

**v2.0 Prediction**: Superlative (S)
**Actual TBTA**: Superlative (3 instances of "great")
**Result**: ✅ **CORRECT**

**Reasoning**:
- RULE 1: Explicit superlative question ("who is greatest?")
- Same pattern as training verse MAT 22:36
- Semantic overrides morphological (μείζων = comparative form)

**Confidence**: Very High (identical to training pattern)

---

### ✅ CORRECT: Verse 14 - Mark 9:34 "who was greatest"

**Greek**: πρὸς ἀλλήλους γὰρ διελέχθησαν ἐν τῇ ὁδῷ τίς μείζων

**v2.0 Prediction**: Superlative (S)
**Actual TBTA**: Superlative (1 instance of "great")
**Result**: ✅ **CORRECT**

**Reasoning**:
- RULE 1: Superlative discourse context ("who was [the] greatest")
- Semantic overrides morphological

**Confidence**: High

---

### ❌ ERROR 5: Verse 13 - Matthew 23:17 "which is greater"

**Greek**: τί γὰρ μεῖζόν ἐστιν, ὁ χρυσὸς ἢ ὁ ναὸς ὁ ἁγιάσας τὸν χρυσόν

**v2.0 Prediction**: Superlative (S)
**Actual TBTA**: **Comparative (C)** (4 instances of "great")
**Result**: ❌ **WRONG**

**Analysis**:
- **My reasoning**: "Which is greater [of the two]?" sounds like superlative question (like MAT 22:36)
- **TBTA reasoning**: Two items explicitly compared (gold vs temple) with ἤ "or" → Comparative
- **Key difference**:
  - MAT 22:36: "Which is the great commandment?" (among all) → Superlative
  - MAT 23:17: "Which is greater, X or Y?" (between two) → Comparative

**Pattern learned**:
- Dyadic comparison ("which of these TWO?") → Comparative (C)
- Set comparison ("which among all?") → Superlative (S)
- Explicit ἤ "or" indicates dyadic comparison

**v2.0 failure**: RULE 1 overgeneralized "which is greater" pattern
**Fix needed**: Distinguish dyadic vs set comparisons

**Severity**: HIGH - Core semantic distinction missed

---

### ❌ ERROR 6: Verse 19 - Mark 12:31 "no other greater"

**Greek**: μείζων τούτων ἄλλη ἐντολὴ οὐκ ἔστιν

**v2.0 Prediction**: Superlative (S) for both
**Actual TBTA**:
- "important" (first commandment) → **Superlative** ✓
- "great" (second commandment) → **Comparative** ✗

**Result**: ❌ **PARTIAL WRONG**

**Analysis**:
- **Context**: Jesus quotes two commandments, then says "no other commandment is greater than these"
- **My reasoning**: "No other greater" = implied superlative (like MAT 11:11)
- **TBTA distinction**:
  - First commandment: "important" → Superlative (the most important)
  - Second commandment: "great" → Comparative (also great, but compared to others)
- **Pattern**: Discourse distinguishes between #1 (superlative) and #2 (comparative)

**Pattern learned**:
- Ranking contexts may use both Superlative AND Comparative
- #1 rank → Superlative
- #2+ rank → Comparative (even with "no other greater" language)

**v2.0 failure**: RULE 1 (implied superlative) didn't account for ranking distinctions
**Fix needed**: Context-sensitive ranking analysis

**Severity**: MEDIUM - Subtle discourse-level distinction

---

### ❌ ERROR 7: Verse 12 - Genesis 1:16 "greater/lesser lights"

**Greek**: N/A (Hebrew text)
**Hebrew**: הַגָּדֹל... הַקָּטֹן (hagadol... haqaton) "the great... the small"

**v2.0 Prediction**: Comparative (C) for both "greater" and "lesser"
**Actual TBTA**: **No Degree** (no non-default degree values found)
**Result**: ❌ **WRONG**

**Analysis**:
- **My reasoning**: Two entities compared (sun vs moon) → Comparative
- **TBTA reasoning**: Positive adjective forms with no degree morphology → No Degree
- **Critical distinction**:
  - English translation says "greater/lesser" (comparative)
  - Hebrew text has positive forms: הַגָּדֹל "the great", הַקָּטֹן "the small"
  - TBTA follows Hebrew morphology, not English translation

**Pattern learned**:
- TBTA marks based on SOURCE LANGUAGE, not target translation
- Hebrew positive + definite article ≠ comparative degree
- Morphology matters when semantics are ambiguous

**v2.0 failure**: RULE 1 (semantic priority) overrode morphology inappropriately
**Fix needed**: Clarify when morphology should override semantic inference

**Severity**: HIGH - Fundamental source language vs translation distinction

---

## Error Pattern Analysis

### Error Type Distribution

| Error | Verse | Pattern | Severity |
|-------|-------|---------|----------|
| 5 | MAT 23:17 | Dyadic vs set comparison | HIGH |
| 6 | MRK 12:31 | Ranking distinction | MEDIUM |
| 7 | GEN 1:16 | Source language morphology | HIGH |

### Pattern 1: Dyadic vs Set Comparison (Error 5)

**Problem**: v2.0 RULE 1 treats all "which is greater?" questions as superlative

**Evidence**:
- MAT 22:36: "Which is the great commandment?" → Superlative ✓ (among all)
- MAT 23:17: "Which is greater, X or Y?" → Comparative ✓ (between two)

**Distinction**:
- **Set comparison**: "Which is greatest [among all]?" → Superlative
- **Dyadic comparison**: "Which is greater [between X and Y]?" → Comparative
- **Marker**: ἤ "or" indicates explicit dyadic choice

**Fix for v2.1**:
- RULE 1 expansion: Check for explicit binary choice (ἤ, "or")
- If dyadic → use Comparative
- If set (among all, of these [3+]) → use Superlative

---

### Pattern 2: Ranking Distinctions (Error 6)

**Problem**: v2.0 treats all "no other greater" as implied superlative uniformly

**Evidence**:
- MAT 11:11: "No one greater than John" → Superlative ✓ (absolute #1)
- MRK 12:31: "No other greater than these [two]" → Mixed ✗
  - First: Superlative (#1 rank)
  - Second: Comparative (#2 rank)

**Distinction**:
- **Absolute ranking**: "No one greater" → Superlative (universal)
- **Relative ranking**: "First is X, second is Y, no other greater" → Superlative + Comparative

**Fix for v2.1**:
- Check for multiple items in ranking
- #1 item → Superlative
- #2+ items → Comparative (even if "no other greater" used)

---

### Pattern 3: Source Language Morphology Priority (Error 7)

**Problem**: v2.0 RULE 1 (semantic priority) overrides morphology too aggressively

**Evidence**:
- GEN 1:16: Hebrew positive forms (הַגָּדֹל, הַקָּטֹן) → No Degree (morphology wins)
- English translation says "greater/lesser" but Hebrew has no comparative morphology

**Distinction**:
- When SOURCE morphology is clear → Follow morphology
- When semantic context ADDS meaning not in morphology → Follow semantics
- When translation adds interpretation → Follow source

**Fix for v2.1**:
- RULE 1 refinement: Semantic overrides morphology ONLY when:
  1. Context provides clear semantic cue (questions, negation patterns)
  2. Source morphology is ambiguous or absent
- Don't override clear morphological No Degree marking

---

## Algorithm v2.1 Needed Improvements

### Fix 1: Distinguish Dyadic vs Set Comparisons

**Current RULE 1**:
```
IF discourse context is superlative (e.g., "which is greatest?")
   AND adjective is semantically superlative
THEN → Degree: Superlative
```

**Revised RULE 1** (v2.1):
```
IF superlative question context:
    IF dyadic (ἤ "or", "X or Y?", two explicit alternatives):
        RETURN Comparative
    ELIF set (among all, of these [3+]):
        RETURN Superlative
    ELSE:
        # Ambiguous - check for other cues
        IF no explicit comparison set:
            RETURN Superlative (default for "which is greatest?")
```

---

### Fix 2: Add Ranking Context Analysis

**New RULE 1.5**:
```
IF ranking discourse (first, second, third):
    rank_1 → Superlative
    rank_2+ → Comparative

IF "no other greater than these [multiple items]":
    highest_ranked_item → Superlative
    other_items → Comparative
```

---

### Fix 3: Refine Semantic vs Morphological Priority

**Current RULE 1**:
```
Semantic context overrides morphology (HIGHEST PRIORITY)
```

**Revised** (v2.1):
```
IF source_morphology is clear (NOT ambiguous):
    IF semantic_context adds meaning (negation, questions):
        semantic_override = TRUE
    ELIF semantic_context contradicts morphology:
        # Check which is more reliable
        IF context_is_explicit (ἤ "or", clear markers):
            Follow semantic
        ELSE:
            Follow morphology (source language priority)
    ELSE:
        Follow morphology
ELSE:
    # Ambiguous morphology
    Follow semantic context
```

---

## Batch 1 Summary

**v2.0 Performance**: 40% (2/5) - **REGRESSION** from 100% on original 7 verses

**Key learnings**:
1. Dyadic vs set comparison distinction critical
2. Ranking contexts use mixed degree values
3. Source language morphology priority needs refinement

**Expected v2.1 improvement**: 80-100% on batch 1 (all 3 errors fixable)

**Next steps**:
1. Develop ALGORITHM-v2.1.md with 3 new fixes
2. Re-test on all 12 verses (original 7 + batch 1)
3. Design batch 2 (verses 21-35) to test v2.1

---

**Status**: Batch 1 testing complete
**Algorithm status**: v2.0 needs refinement → v2.1 development
**Overall accuracy**: 75% (9/12 verses) - target 90%+
