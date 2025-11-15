# Participant Tracking: Algorithm v2.0 (Hypothetical)

**Date created**: 2025-11-11
**Based on**: v1.0 error analysis (ERROR-ANALYSIS.md)
**Status**: ⚠️ HYPOTHETICAL - NOT TESTED
**Purpose**: Incorporate 3 critical fixes from v1.0 validation
**Testing status**: UNTESTED - requires validation on NEW test set

---

## Overview

Algorithm v2.0 incorporates three critical fixes identified from v1.0 validation:

1. **Epistolary abstract noun rule** - Genre-specific handling for theological concepts
2. **Refined universal quantifier rule** - Definiteness + bounded group detection
3. **Recognition frame addition** - Expanded frame inference for identification scenes

**Projected performance**: 75-85% accuracy (vs. 60-70% v1.0)
**Production-ready**: NO - untested, requires validation

---

## Changes from v1.0

### Change 1: Add Rule 2.0 - Genre Detection (NEW)

**Insert BEFORE Rule 1 (Interrogative)**

```
Rule 0: Genre Detection (Context Pre-Processing)

IF book_code IN [EPH, PHP, COL, 1TH, 2TH, 1TIM, 2TIM, TIT, PHM, HEB, JAS, 1PE, 2PE, 1JN, 2JN, 3JN, JUD, ROM, 1CO, 2CO, GAL]
THEN genre = "Epistle"

ELSE IF book_code IN [PSA, PRO, ECC, SNG, JOB, LAM]
THEN genre = "Poetry/Wisdom"

ELSE IF book_code IN [ISA, JER, EZE, DAN, HOS, JOL, AMO, OBA, JON, MIC, NAH, HAB, ZEP, HAG, ZEC, MAL]
THEN genre = "Prophecy"

ELSE
THEN genre = "Narrative"
```

**Rationale**: Genre affects participant tracking patterns. Epistles presuppose theological realities, narratives introduce them.

---

### Change 2: Add Rule 2.3b - Epistolary Abstract Noun Override (NEW)

**Insert AFTER Rule 2.2 (Negative existentials), BEFORE Rule 2.3 (Abstract concepts)**

```
Rule 2.3b: Epistolary Abstract Noun Override (HIGH PRIORITY)

IF genre = "Epistle"
AND participant is abstract theological noun
    [grace, mercy, peace, love, truth, wisdom, redemption, forgiveness, salvation,
     righteousness, faith, hope, glory, praise, power, riches, blood (theological)]
AND (possessive OR definite article OR in greeting/blessing formula)
THEN → Routine (D), SKIP Rule 2.3

ELSE → Continue to Rule 2.3
```

**Rationale**: Epistles treat theological abstracts as established realities (Routine), not generic types. Parallel to God presupposition.

**Examples**:
- "his grace" (EPH 1:6) → Routine (possessive + epistle)
- "the glory" (EPH 1:6) → Routine (definite + epistle)
- "Grace be with you" (2JN 1:3) → Routine (greeting formula + epistle)
- "everlasting life" (JHN 3:16 - narrative) → Generic (type reference, NOT epistle)

---

### Change 3: Refine Rule 2.1 - Universal Quantifier with Definiteness

**REPLACE existing Rule 2.1**

```
OLD Rule 2.1:
IF universal quantifier (whosoever, whoever, anyone, everyone, all, every, any)
THEN → Generic (G)

NEW Rule 2.1: Universal Quantifier with Bounded Group Check

IF universal quantifier (whosoever, whoever, anyone, everyone, all, every, any, no one, none)
THEN:
   IF bare noun (no article)
      → Generic (G)  # "all people", "every nation", "anyone"

   ELSE IF definite article ("all the X", "every one of the X")
   THEN:
      // Check for bounded group
      IF possessive ("all his X", "all their X")
         → Routine (D)  # "all his servants" = specific group

      ELSE IF locational bound ("all the X in [place]")
         → Routine (D)  # "all the people in Shushan" = specific bounded group

      ELSE IF institutional/role bound AND definite
         → Routine (D)  # "all the magicians [= court magicians]", "all the elders [= council]"

      ELSE IF negation + definite
         → Generic (G)  # "not all the people" = class negation

      ELSE
         → Generic (G)  # Default: ambiguous cases lean Generic

   ELSE
      → Generic (G)  # Default
```

**Rationale**: "All + definite" marks complete specific groups (Routine) vs. universal classes (Generic). Requires context check.

**Examples**:
- "all people" (bare) → Generic ✅
- "all the magicians" (definite + institutional) → Routine (court magicians) ✅
- "all his servants" (possessive) → Routine (his specific servants) ✅
- "all the people in Shushan" (locational) → Routine (specific population) ✅
- "all the people" (ambiguous) → Generic (default) ⚠️

---

### Change 4: Expand Rule 3.2 - Add Recognition/Identification Frame

**ADD to existing Rule 3.2 frame list**

```
Rule 3.2: Frame-based inference (Recognition frame ADDED)

[... existing frames: creation, inn, household, legal, travel, meal, temple ...]

**Recognition/Identification Frame** (NEW):
- Trigger verbs: know, recognize, realize, remember, see, perceive, identify, recall
- Trigger patterns:
  * "knew that it was X"
  * "recognized X as Y"
  * "this is X who/that..."
  * "the same X that..."
  * "X, whom they had seen..."
- Expected participants (Frame Inferable):
  * Identity markers: Titles, roles, descriptions used for identification
  * Identifying locations: "at the gate", "in the temple" (where person was known)
  * Characteristic actions: "who sat for alms", "who had been lame" (identifying actions)
  * Prior context references: Information that enables recognition

- **Example**: "they knew that it was he which sat for alms at the Beautiful gate" (ACT 3:10)
  → "he" = Routine (continued reference)
  → "alms" = Frame Inferable (characteristic action identifying him)
  → "Beautiful gate" = Frame Inferable (location where he was known)
  → Recognition frame makes identity markers inferable

**Implementation heuristic**:
IF recognition verb (know, recognize, realize, remember)
AND relative clause or identity description follows
THEN mark descriptive elements as Frame Inferable (identity markers, locations, actions)
```

**Rationale**: Recognition scenes heavily use frame inference - people infer participant identity from contextual cues.

**Expected impact**: Fix ~5-10 errors in Acts 3:10 and similar recognition scenes.

---

## Full Algorithm v2.0 (Hierarchical Rules)

### Rule 0: Genre Detection (NEW)
- Detect genre: Epistle, Narrative, Poetry/Wisdom, Prophecy
- Use genre for context-specific overrides

### Rule 1: Interrogative (unchanged from v1.0)
- Question context, interrogative pronouns → Interrogative

### Rule 2: Generic (modified)
- **2.1**: Universal quantifiers WITH definiteness + bounded group check (MODIFIED)
- **2.2**: Negative existentials (unchanged)
- **2.3b**: Epistolary abstract noun override (NEW)
- **2.3**: Abstract concepts as types (unchanged, but now after 2.3b)
- **2.4**: Vocative/role titles (unchanged)
- **2.5**: Proverbial/wisdom generic (unchanged)
- **2.6**: Hypothetical/conditional (unchanged)

### Rule 3: Frame Inferable (expanded)
- **3.1**: Relational inference (unchanged)
- **3.2**: Frame-based inference WITH recognition frame added (EXPANDED)
- **3.3**: Temporal frames (unchanged)
- **3.4**: Definite on first mention (unchanged)

### Rule 4: First Mention vs. Routine (unchanged from v1.0)
- **4A**: First Mention (indefinite, proper names, novel)
- **4B**: Routine (repeated, pronouns, definite established, main participants, **God presupposition**, established context, post-question continuation)

---

## Expected Performance (Projected, Untested)

### v1.0 vs. v2.0 Comparison

| State | v1.0 Accuracy | v2.0 Projected | Improvement |
|-------|---------------|----------------|-------------|
| **Routine** | ~85% | ~90% | +5% (epistolary abstracts fixed) |
| **Generic** | ~50% | ~70% | +20% (quantifier+definite fix, epistolary fix) |
| **Frame Inferable** | ~40% | ~60% | +20% (recognition frame added) |
| **First Mention** | N/A (0 in test) | N/A | - |
| **Interrogative** | N/A (0 in test) | N/A | - |
| **Overall** | 60-70% | 75-85% | +15% |

### Error Reductions

**Fix 1 (Epistolary abstracts)**: ~20 errors fixed
- 2JN 1:3: 5 errors (grace, mercy, peace, truth, love)
- EPH 1:6: 3 errors (praise, glory, grace)
- EPH 1:7-8: ~8 errors (various abstracts)
- EPH 3:20: ~4 errors (power, etc.)

**Fix 2 (Quantifier+definite)**: ~5 errors fixed
- DAN 1:20: 2-3 errors ("all the magicians", "all astrologers")
- EST 1:5: 1-2 errors ("all the people")

**Fix 3 (Recognition frame)**: ~8 errors fixed
- ACT 3:10: 5-8 errors (identity markers, locations in recognition scene)

**Total projected**: ~33 errors fixed out of ~85 errors (39% error reduction)

---

## Limitations and Unknowns

### Limitation 1: Untested Hypothesis

**Status**: Algorithm v2.0 is **hypothetical** - rules specified but NOT tested
**Risk**: Fixes may introduce new errors or not work as expected
**Requirement**: Must be validated on NEW test set (not same 12 verses - would introduce bias)

### Limitation 2: Genre-Specific Rules May Over-Correct

**Risk**: Epistolary abstract rule may mark TOO many abstracts as Routine
**Example**: "a wisdom" (indefinite) might still be First Mention, not Routine
**Mitigation**: Rule 2.3b requires possessive OR definite article OR greeting formula (avoids indefinite abstracts)

### Limitation 3: Bounded Group Detection Is Heuristic

**Challenge**: "all the magicians" requires knowing if specific (court magicians) or universal (all magicians everywhere)
**Solution**: Heuristic checks (possessive, locational, institutional) may not cover all cases
**Remaining ambiguity**: Some "all the X" cases will still be ambiguous

### Limitation 4: Recognition Frame Detection Requires Parsing

**Challenge**: Identifying "recognition verb + relative clause + identity marker" requires syntactic parsing
**Implementation complexity**: May require access to TBTA clause structure, not just surface form
**Fallback**: If parsing unavailable, recognition frame may be under-applied

---

## Validation Requirements for v2.0

### Do NOT Test on Same 12 Verses

**Why**: Testing on same verses used for error analysis introduces bias
- Algorithm was designed to fix errors in those specific verses
- Would artificially inflate accuracy

### Required: NEW Test Set

**Option 1**: Adversarial test (10 verses from Phase 5 design)
- Includes epistolary verses (Ephesians, Colossians, etc.)
- Includes definite+quantifier cases
- Includes recognition scenes

**Option 2**: NEW random sample
- Select 12 NEW verses with epistolary coverage
- Use different random seed
- Ensure genre balance (narrative 50%, epistle 30%, poetry 15%, prophecy 5%)

**Option 3**: Cross-validation
- Divide original 215 TBTA verses into train/test splits
- Test v2.0 on held-out verses

---

## Production Readiness Assessment

**Algorithm v1.0**: ❌ NOT production-ready (60-70% accuracy, systematic epistolary errors)

**Algorithm v2.0**: ⚠️ **CONDITIONALLY** production-ready
- **IF** validated on NEW test set and achieves 80%+ accuracy → Production candidate
- **IF NOT** validated → Remains hypothetical, NOT production-ready

**Recommendation**:
1. Document v2.0 as proposed improvement
2. Mark feature as "IN DEVELOPMENT" (not complete)
3. Future session: Validate v2.0 on adversarial test or NEW random sample
4. If v2.0 achieves 80%+, mark as production-ready

---

## Summary

**Algorithm v2.0 Status**: Designed but untested

**Key improvements**:
1. ✅ Genre detection (epistle vs. narrative)
2. ✅ Epistolary abstract noun override (grace, mercy, peace → Routine in epistles)
3. ✅ Refined quantifier+definite handling (bounded group detection)
4. ✅ Recognition frame added (identity markers, locations in recognition scenes)

**Projected performance**: 75-85% accuracy (vs. 60-70% v1.0)

**Next steps**:
- Phase 9: Document v2.0 as hypothetical improvement in completion summary
- Phase 10: Peer review should note v2.0 is untested
- Future: Validate v2.0 on NEW test set before production deployment

---

**Created**: 2025-11-11
**Based on**: v1.0 error analysis (3 critical fixes)
**Testing status**: ⚠️ UNTESTED - hypothetical only
**Validation required**: NEW test set (adversarial or different random sample)
**Production-ready**: NO - pending validation
