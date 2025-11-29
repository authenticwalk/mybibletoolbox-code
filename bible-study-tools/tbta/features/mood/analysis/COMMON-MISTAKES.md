# Common Mistakes Analysis

**Date**: 2025-11-29
**Total Persistent Errors**: 53 cases where ≥3/4 models got it wrong

## Summary

| Label | Persistent Errors | % of Label | Root Cause |
|-------|------------------|------------|------------|
| 'should' Obligation | 16/16 | 100% | TBTA semantic criteria differ from LLM expectations |
| 'must' Obligation | 13/13 | 100% | Implicit obligation not recognized |
| Forbidden Obligation | 7/9 | 78% | Polarity confusion |
| 'might' Potential | 5/8 | 63% | Conditional constructions missed |
| 'may' (permissive) | 5/5 | 100% | Permission semantics unclear |
| 'should not' Obligation | 5/5 | 100% | Negative advice vs statement |
| Indicative | 2/44 | 5% | Over-predicted, rarely wrong when GT is Indicative |

## Pattern 1: 'should' Obligation (100% miss rate)

**All 16 'should' Obligation cases were missed by all models.**

| # | Verse | Text (with **bolded** word) | TBTA | Haiku | Sonnet | Guided |
|---|-------|----------------------------|------|-------|--------|--------|
| 18 | GEN-022-002 | God show Abraham mountain Abraham **sacrifice**... | 'should' | 'must' | Def.Pot | Ind |
| 23 | MRK-008-021 | Jesus say disciple disciple **understand** true... | 'should' | 'must' | 'should not' | Forb |
| 24 | MAT-005-043 | Jesus say person **love** all person... | 'should' | 'must' | 'should' | Ind |
| 28 | EPH-002-009 | so person **praise** person... | 'should' | Ind | 'should not' | Ind |

**Root Cause Analysis**:
- TBTA labels "implicit moral guidance" as 'should' Obligation
- LLMs expect explicit "you should" or advisory language
- Many are COMMANDS (Jesus says "love") but TBTA distinguishes command strength

**Resolution Options**:
1. **Definition adjustment**: Define 'should' as "moral teaching, wisdom, or implied advice even without explicit 'should'"
2. **Context pattern**: Wisdom literature (PRO, ECC) and Jesus's teachings often use 'should'
3. **Consider merging**: 'should' + 'must' into "Obligation" with strength indicator

## Pattern 2: 'must' Obligation (100% miss rate)

| # | Verse | Text | TBTA | Models Predicted |
|---|-------|------|------|------------------|
| 7 | MRK-012-019 | man **have** son woman dead... | 'must' | Ind/Def.Pot/'may'/'might' |
| 13 | DAN-003-010 | person **worship** statue gold... | 'must' | All: Indicative |
| 16 | EXO-021-034 | person **pay** person... | 'must' | 3/4: Indicative |

**Root Cause Analysis**:
- TBTA labels LEGAL requirements as 'must' even without modal verbs
- Law code context (EXO, LEV, DEU) implies obligation
- LLMs see "action happened" → Indicative

**Resolution Options**:
1. **Genre-aware prompt**: "In law codes, actions often represent obligations"
2. **Hebrew form check**: Imperfect verbs in legal context = obligation

## Pattern 3: Forbidden Obligation (78% miss rate)

| # | Verse | Text | TBTA | Models Predicted |
|---|-------|------|------|------------------|
| 9 | EXO-022-015 | man borrow animal **pay** owner... | Forbidden | 'must'/'might' mix |
| 47 | 2SA-021-004 | person **demand** David David kill... | Forbidden | All: Indicative |

**Root Cause Analysis**:
- Negative obligation context not recognized
- "Shall not" patterns missing in TBTA simplified text
- Polarity (positive vs negative) is key but subtle

**Resolution Options**:
1. Check negation markers in original
2. Pattern: "X shall not Y" → Forbidden

## Pattern 4: 'may' (permissive) (100% miss rate)

| # | Verse | Text | TBTA | Models Predicted |
|---|-------|------|------|------------------|
| 6 | GEN-019-002 | angel **sleep** at house Lot tonight... | 'may' | All: Indicative/Def.Pot |
| 50 | EXO-017-006 | person **drink** water... | 'may' | All: Indicative/'must' |

**Root Cause Analysis**:
- Permission semantics require understanding speech act
- "You may sleep here" (invitation) vs "You slept here" (fact)
- TBTA captures intended permission, LLM sees surface statement

## Recommendations

### 1. Two-Stage Classification
First: Indicative vs Non-Indicative (93% accuracy achievable)
Second: Among non-Indicative, classify subtype

### 2. Genre-Aware Approach
- **Law codes** (EXO 20-23, LEV, DEU): Assume obligation unless clearly narrative
- **Wisdom** (PRO, ECC): Assume 'should' unless clearly indicative
- **Commands of Jesus**: Check for teaching context

### 3. Simplify Label Set
Current TBTA has 10 values. Consider:
- Merge 'must' + 'should' → "Obligation" (with strength score)
- Merge 'should not' + Forbidden → "Prohibition" (with strength score)
- Drop Definite/Probable/Unlikely Potential (too rare: 14 total in 72K)

### 4. Output Format Change
Instead of single label:
```yaml
primary: Indicative
confidence: 0.6
alternates:
  - label: "'should' Obligation"
    reason: "Wisdom literature context, implicit moral teaching"
    confidence: 0.3
```

This captures uncertainty and helps translators make informed choices.
