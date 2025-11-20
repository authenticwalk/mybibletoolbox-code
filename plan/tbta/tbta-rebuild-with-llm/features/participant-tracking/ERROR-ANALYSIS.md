# Participant Tracking: Error Analysis (v1.0 → v2.0)

**Date**: 2025-11-11
**Algorithm v1.0**: commit cb388ca (97% training, 60-70% random test)
**Validation data**: 12 random verses, 214 participants
**Purpose**: Identify systematic errors and develop Algorithm v2.0

---

## Performance Summary

| Metric | Target | v1.0 Actual | Status |
|--------|--------|-------------|--------|
| **Training accuracy** | 90%+ | 97% (32/33) | ✅ EXCEEDS |
| **Random test accuracy** | 85-90% | 60-70% (est.) | ❌ BELOW TARGET |
| **Routine prediction** | N/A | ~85% accuracy | ✅ GOOD |
| **Generic prediction** | N/A | ~50% accuracy | ❌ POOR |
| **Frame Inferable prediction** | N/A | ~40% accuracy | ❌ POOR |

**Conclusion**: Algorithm v1.0 is NOT production-ready. Systematic errors in epistolary context and quantifier handling prevent deployment.

---

## Error Category 1: Epistolary Abstract Nouns (HIGH IMPACT)

### The Problem

**Algorithm v1.0 Rule 2.3**: Abstract nouns (grace, mercy, peace, wisdom, love, truth) → Generic (type reference)

**Actual TBTA**: In epistolary contexts (Ephesians, 2 John), abstract nouns are marked **Routine**, not Generic

### Examples of Errors

#### 2 John 1:3
**Predicted**:
- grace → Generic (abstract type)
- mercy → Generic (abstract type)
- peace → Generic (abstract type)
- truth → Generic (abstract type)
- love → Generic (abstract type)

**Actual TBTA**: ALL marked as **Routine** (28 Routine total in verse)

**Error rate**: 5/5 abstract nouns incorrectly predicted = 100% error rate on abstracts

#### Ephesians 1:6
**Predicted**:
- praise → Generic
- glory → Generic
- grace → Generic

**Actual TBTA**: ALL 10 participants marked as **Routine**

**Error rate**: 3/3 abstract nouns = 100% error

#### Ephesians 1:7
**Predicted**:
- redemption → Generic
- forgiveness → Generic
- sins → Generic
- riches → Generic
- grace → Generic

**Actual TBTA**: 17 Routine, 8 Generic, 1 Frame Inferable (26 total)
- Mixed: Some abstracts are Generic, others Routine

**Error rate**: Partial errors, context-dependent

### Root Cause Analysis

**Why the error occurred**:
1. Algorithm v1.0 treats all abstract nouns uniformly (Rule 2.3)
2. Does NOT account for genre (narrative vs. epistle vs. poetry)
3. Does NOT account for discourse function (theological exposition vs. narrative action)

**Why epistles are different**:
- Epistles engage in theological **exposition** where abstract concepts are treated as **established theological realities**
- "Grace", "mercy", "peace" in epistolary greetings/expositions are not generic types but **ongoing divine attributes/actions**
- Parallel: "God" is Routine (presupposed) → "grace of God" is also Routine (presupposed divine attribute)

### Algorithm v2.0 Fix

**New Rule 2.3b - Epistolary Abstract Noun Override** (insert BEFORE generic Rule 2.3):

```
IF genre = Epistle (EPH, PHP, COL, 1-2TH, 1-2TIM, TIT, PHM, HEB, JAS, 1-2PE, 1-3JN, JUD)
AND participant is abstract theological noun (grace, mercy, peace, love, truth, wisdom, redemption, forgiveness, salvation, righteousness, faith, hope)
AND (possessive OR definite article OR in greeting/blessing formula)
THEN → Routine (D), NOT Generic
```

**Rationale**: Epistles presuppose theological realities as ongoing/established, not generic types

**Expected impact**: Fix ~15-20 errors in Ephesians/2 John test verses

---

## Error Category 2: Universal Quantifier + Definite Article (MEDIUM IMPACT)

### The Problem

**Algorithm v1.0 Rule 2.1**: Universal quantifier (all, every, any) → Generic

**Actual TBTA**: "All + definite article" can be:
- **Generic** (universal class): "all people" (everyone)
- **Routine** (specific complete group): "all the magicians" (specific group in king's court)

### Examples of Errors

#### Daniel 1:20
**Predicted**:
- "all matters" → Generic (universal quantifier Rule 2.1)
- "all the magicians" → Generic (universal quantifier)
- "all astrologers" → Generic (universal quantifier)

**Actual TBTA**: 12 Routine, 1 Generic (13 total)
- "all the magicians" likely **Routine** (specific group of magicians employed by the king)
- "all astrologers" may also be **Routine** (specific court astrologers)

**Error analysis**: "All + THE + noun" marks a **specific bounded group** (Routine), not universal class (Generic)

#### Esther 1:5
**Predicted**:
- "all the people" → Generic (universal quantifier)

**Actual TBTA**: 18 Routine, 4 Generic, 1 Frame Inferable (23 total)
- "all the people" context-dependent: If "all people present in Shushan" → Routine (specific group), if "all people generally" → Generic

### Root Cause Analysis

**Why the error occurred**:
1. Algorithm v1.0 treats "all" as absolute signal for Generic
2. Does NOT distinguish "all X" (bare, universal) from "all the X" (definite, bounded)
3. Does NOT check if referent is a specific complete group vs. universal class

**Linguistic principle**:
- "all people" (bare) = Generic (class of all human beings)
- "all THE people" (definite) = Routine if specific group ("all the people present"), Generic if universal ("all the people on earth")
- Definiteness + completeness = specific group (Routine)

### Algorithm v2.0 Fix

**Refined Rule 2.1 - Universal Quantifier with Definiteness Check**:

```
IF universal quantifier (all, every, any, no one, none)
THEN:
   IF bare noun (no article) → Generic (G)  # "all people", "every nation"

   ELSE IF definite article ("all the X", "every one of the X")
   THEN → Check for bounded group:
      IF context shows specific bounded group (court officials, people present, etc.)
         → Routine (D)  # "all the magicians [in the court]"
      ELSE
         → Generic (G)  # "all the people [in general]"

   ELSE → Generic (G)  # Default for ambiguous cases
```

**Implementation note**: "Bounded group" detection heuristics:
- Possessive ("all his servants")
- Locational bound ("all the people in Shushan")
- Institutional bound ("all the magicians [= court magicians]")
- Default: If ambiguous, lean Generic

**Expected impact**: Fix ~3-5 errors in Daniel, Esther verses

---

## Error Category 3: Frame Inferable Under-Prediction (MEDIUM IMPACT)

### The Problem

**Algorithm v1.0 Rule 3**: Frame Inferable based on creation, inn, household, legal, travel, meal, temple frames

**Actual TBTA**: Acts 3:10 has **9 Frame Inferable** participants (45% of verse!) - recognition/identification frame NOT captured

### Examples

#### Acts 3:10
**Actual TBTA**: 8 Routine, 3 Generic, **9 Frame Inferable** (20 total)

**Hypothesis**: Recognition scene - "they knew that it was he which sat for alms at the Beautiful gate"
- Participants are inferable from recognition context
- Identity markers inferable from prior knowledge

**Algorithm v1.0**: Did NOT have recognition frame in Rule 3.2

### Root Cause Analysis

**Why the error occurred**:
1. Algorithm v1.0 frame list is incomplete (only 7 frames: creation, inn, household, legal, travel, meal, temple)
2. Recognition/identification frame is common in narrative but not captured
3. Frame inference is richer than initially documented

**Recognition frame pattern**:
- Trigger verbs: know, recognize, realize, remember, identify
- Trigger contexts: "it was he who...", "this is the one that...", "they knew him as..."
- Expected participants: Identity markers, locations, actions that enable recognition

### Algorithm v2.0 Fix

**Expanded Rule 3.2 - Add Recognition/Identification Frame**:

```
**Recognition/identification frame**:
- Trigger verbs: know, recognize, realize, remember, see, perceive, identify
- Trigger patterns: "knew that it was X", "recognized X as Y", "this is X who...", "the same X that..."
- Expected participants:
  * Identity markers (titles, locations, actions that identify person)
  * Characteristic attributes (description that enables recognition)
  * Prior context references (places, actions mentioned for identification)
- **Example**: "they knew that it was he which **sat for alms** at the **Beautiful gate**"
  → "sat for alms" (characteristic action), "Beautiful gate" (identifying location) = Frame Inferable

**Implementation**: When recognition verb detected, mark identity/location/action descriptors as Frame Inferable
```

**Expected impact**: Fix ~5-10 errors in recognition scenes (Acts 3:10 and similar)

---

## Error Category 4: Participant Extraction Incompleteness (METHODOLOGICAL)

### The Problem

**Prediction phase**: Manually identified 50-70% of actual participants
**Actual TBTA**: Full participant extraction shows 2-3x more participants than predicted

### Examples

- Acts 2:1: Predicted 5 participants, actual 19 (under-counted by 74%)
- Acts 3:8: Predicted 4 participants, actual 13 (under-counted by 69%)
- Ephesians 3:20: Predicted 4 participants, actual 22 (under-counted by 82%)

### Root Cause

**Manual text-based extraction** missed:
- Embedded clause participants
- Complex noun phrases
- Implicit arguments
- Repeated mentions in different clauses

### Solution for Future Phases

**Not an algorithm error** - methodological issue in prediction phase
**Fix**: Use systematic YAML-based extraction from TBTA for complete participant lists
**Impact on v2.0**: Does not affect algorithm design, only validation methodology

---

## Algorithm v2.0 Development Summary

### Three Priority Fixes

**Fix 1: Epistolary Abstract Noun Rule** (HIGH IMPACT)
- Add genre detection (epistle vs. narrative)
- Override Generic rule for theological abstracts in epistolary context
- Mark as Routine (presupposed theological realities)

**Fix 2: Refined Universal Quantifier Rule** (MEDIUM IMPACT)
- Distinguish "all X" (bare, Generic) from "all the X" (definite, check for bounded group)
- Add bounded group detection (possessive, locational, institutional)
- Default: Definite + bounded → Routine, otherwise Generic

**Fix 3: Recognition Frame Addition** (MEDIUM IMPACT)
- Add recognition/identification frame to Rule 3.2
- Trigger verbs: know, recognize, realize, remember
- Expected participants: Identity markers, locations, characteristic actions

### Expected v2.0 Performance

**Estimated improvements**:
- Fix ~20 errors from epistolary abstracts (+10% accuracy)
- Fix ~5 errors from quantifier+definite (+2% accuracy)
- Fix ~8 errors from recognition frame (+4% accuracy)

**Projected v2.0 accuracy**: 75-85% on random test (vs. 60-70% v1.0)
- Still below 85-90% target, but significant improvement
- Remaining errors likely context-specific edge cases

### Algorithm v2.0 Status

**Development**: Complete (rules specified above)
**Testing**: Not yet tested (would require re-running on same 12 verses, not blind)
**Production-ready**: NO - needs validation on NEW test set (adversarial or different random sample)

---

## Lessons Learned

### Lesson 1: Genre Matters Profoundly

**Discovery**: Epistles treat abstract theological concepts as Routine (established), not Generic (types)
**Implication**: Future features should consider genre-specific rules from the start
**Application**: Person-systems, number-systems, degree may also benefit from genre-specific handling

### Lesson 2: Surface Form + Context, Not Just Surface Form

**Discovery**: "All the X" requires context (bounded group vs. universal class) to determine state
**Implication**: Simple surface form rules (Rule 2.1) are insufficient for definiteness + quantifier combinations
**Application**: Hierarchical rules need context-checking sub-rules, not just morphological patterns

### Lesson 3: Frame Inference Is Richer Than Initially Captured

**Discovery**: Recognition frames produce high Frame Inferable rates (45% in Acts 3:10)
**Implication**: Initial frame list (7 frames) was incomplete
**Application**: Future frame detection should be expanded systematically (recognition, possession, transformation, comparison frames)

### Lesson 4: Training Accuracy ≠ Test Accuracy

**Discovery**: 97% training accuracy collapsed to 60-70% test accuracy
**Cause**: Training verses did NOT include epistolary contexts (training was JHN 3:16, MRK 1:35, GEN 1:1, MAT 22:36 - all narrative)
**Lesson**: Training set must include ALL major genres (narrative, epistle, poetry, prophecy) to catch genre-specific patterns
**Application**: Future features should use genre-stratified training sets

---

## Recommendations for Phase 9-10

### For Algorithm v2.0 Validation

**Do NOT re-test on same 12 verses** - would not be blind, introduces bias
**Instead**:
1. Document v2.0 rules in ALGORITHM-v2.0.md
2. Note that v2.0 is hypothetical (not tested)
3. Recommend future validation on NEW adversarial test set with epistolary coverage

### For Completion Summary (Phase 9)

Document:
1. v1.0 achieved 97% training but only 60-70% test (genre gap)
2. Three critical errors identified and fixed in v2.0 (epistolary abstracts, quantifier+definite, recognition frame)
3. v2.0 projected 75-85% accuracy (untested)
4. Production status: NOT READY - needs adversarial validation with epistolary coverage

### For Peer Review (Phase 10)

Highlight:
1. Methodological rigor maintained (blind predictions locked)
2. Comprehensive error analysis completed
3. Algorithm v2.0 designed with targeted fixes
4. Honest assessment: v1.0 not production-ready, v2.0 untested
5. Recommend: Future session should validate v2.0 on NEW test set before production

---

**Completed**: 2025-11-11
**Status**: Error analysis complete, Algorithm v2.0 rules specified
**Next**: Phase 9 - Completion summary documenting entire feature workflow
