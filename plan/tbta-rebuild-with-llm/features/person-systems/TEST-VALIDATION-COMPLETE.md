# Person Systems: Complete Test Validation Results

**Date**: 2025-11-10
**Algorithm Tested**: v1.0 (locked at commit f373646)
**Validation Method**: Real Bible translations in clusivity-marking languages
**Languages Used**: Tagalog, Indonesian, Tok Pisin, Fijian, Cebuano
**Total Verses Validated**: 21 (11 adversarial + 10 random)

---

## Executive Summary

### Overall Accuracy
- **Adversarial Test**: 8/11 correct = **73%**
- **Random Test**: 5/10 correct (2 mixed) = **50-60%**
- **Combined**: 13/21 correct = **62%**

### Performance Against Targets
- **Adversarial Target**: 60-70% ✅ ACHIEVED (73%)
- **Random Target**: 80-90% ❌ MISSED (50-60%)
- **Gap Expected**: Random should exceed adversarial by 20-25 points
- **Gap Actual**: Adversarial exceeded random by 13-23 points ⚠️ INVERTED

### Key Finding
**The random test performed worse than the adversarial test**, contrary to expectations. This requires investigation into:
1. Whether "random" verses were actually harder than designed
2. Whether algorithm has systematic blind spots
3. Whether sampling introduced unexpected bias

---

## Adversarial Test Results (11 verses)

### Correct Predictions (8/11 = 73%)

| Verse | Prediction | Confidence | Result | Languages |
|-------|------------|------------|--------|-----------|
| Isaiah 9:6 | INCL | 40% | ✅ INCL | Tag, Ind (some variation) |
| 1 John 4:19 | INCL | 85% | ✅ INCL | Tag, Ind (unanimous) |
| Genesis 42:21 | INCL | 90% | ✅ INCL | Tag, Ind (unanimous) |
| Jeremiah 42:20 | INCL | 65% | ✅ INCL | Tag, Ind (for "our God") |
| Acts 16:10 | EXCL | 95% | ✅ EXCL | Tag, Ind (unanimous) |
| Daniel 2:36 | EXCL | 50% | ✅ EXCL | Tag, Ind (unanimous) |
| Nehemiah 2:17 | INCL | 90% | ✅ INCL | Tag, Ind (unanimous) |
| Jonah 1:14 | EXCL | 95% | ✅ EXCL | Tag, Ind (unanimous) |

### Incorrect Predictions (3/11 = 27%)

| Verse | Prediction | Confidence | Actual | Languages | Error Type |
|-------|------------|------------|--------|-----------|------------|
| Psalm 44:1 | INCL | 70% | ❌ EXCL | Tag, Ind (100% agreement) | Prayer pattern misread |
| Song of Solomon 1:4 | INCL | 70% | ❌ EXCL | Tag, Ind (100% agreement) | Chorus excludes addressee |
| James 3:1 | EXCL | 85% | ❌ INCL | Tag, Ind, Tok, Ceb (80%+ agreement) | Role distinction misread |

### Confidence Calibration (Adversarial)
- **High confidence (80-95%)**: 6 predictions, 5 correct = 83% accuracy ✅
- **Medium confidence (60-75%)**: 3 predictions, 2 correct = 67% accuracy ✅
- **Low confidence (40-50%)**: 2 predictions, 1 correct = 50% accuracy ✅

**Assessment**: Confidence calibration is accurate for adversarial test.

---

## Random Test Results (10 verses)

### Correct Predictions (5/10 = 50%)

| Verse | Prediction | Confidence | Result | Languages |
|-------|------------|------------|--------|-----------|
| Joshua 24:15 | EXCL | 95% | ✅ EXCL | Tag, Ind, Ceb (unanimous) |
| Jeremiah 3:22 | EXCL | 90% | ✅ EXCL | Tag, Ind (unanimous) |
| Mark 1:38 | INCL | 95% | ✅ INCL | Tag, Ind, Tok, Fij (unanimous) |
| Philippians 3:20 | INCL | 95% | ✅ INCL | Tag, Ind, Tok (unanimous) |
| 1 Peter 2:24 | INCL | 90% | ✅ INCL | Tag, Ind, Tok (unanimous) |

### Incorrect Predictions (3/10 = 30%)

| Verse | Prediction | Confidence | Actual | Languages | Error Type |
|-------|------------|------------|--------|-----------|------------|
| 2 Kings 18:22 | INCL | 75% | ❌ EXCL | Tag, Ind (unanimous) | Quoted speech misread |
| Ezekiel 33:10 | INCL | 90% | ❌ EXCL | Tag, Ind (unanimous) | Lament structure misread |
| Luke 24:29 | INCL | 90% | ❌ EXCL | Tag, Ind, Tok, Fij (unanimous) | Invitation semantics misread |

### Mixed/Variant Predictions (2/10 = 20%)

| Verse | Prediction | Confidence | Result | Languages | Notes |
|-------|------------|------------|--------|-----------|-------|
| Psalm 66:6 | INCL | 90% | 🟡 MIXED | Tag: EXCL (old), INCL (new); Ind: INCL | Translation evolution |
| Ephesians 2:3 | INCL | 95% | 🟡 MOSTLY INCL | 3/4 INCL, Ind v3 EXCL | Theological variation |

### Confidence Calibration (Random)
- **High confidence (85-95%)**: 8 predictions, 3 correct, 2 mixed = 38-63% accuracy ❌
- **Medium confidence (75%)**: 1 prediction, 0 correct = 0% accuracy ❌
- **Low confidence**: 0 predictions

**Assessment**: Confidence calibration failed for random test - high confidence predictions only 38-63% accurate.

---

## Error Analysis

### Error Pattern 1: Prayer/Address to God (3 errors)
**Verses**: Psalm 44:1, Jeremiah 3:22 ✅, Ezekiel 33:10

**Issue**: Algorithm inconsistently applies Rule 2.1 (Prayer to God → EXCLUSIVE)

**Successes**:
- Jeremiah 3:22 ✅ (people coming to God)
- Jonah 1:14 ✅ (sailors praying to God)

**Failures**:
- Psalm 44:1 ❌ (predicted INCL, actual EXCL) - "We have heard, O God"
- Ezekiel 33:10 ❌ (predicted INCL, actual EXCL) - Corporate lament TO God

**Pattern**: When people address/speak TO God, translations use EXCLUSIVE even in corporate contexts. Algorithm correctly identified this for Jeremiah 3:22 and Jonah 1:14, but failed for Psalm 44:1 and Ezekiel 33:10.

**Root cause**: Algorithm applied "shared experience" rule (3.1) instead of recognizing the structural pattern of addressing deity.

**Fix needed**: Strengthen Rule 2.1 - ANY speech addressed TO God (prayer, lament, petition) should default to EXCLUSIVE, regardless of whether content describes shared experience.

---

### Error Pattern 2: Invitation Semantics (2 errors)
**Verses**: Luke 24:29, Song of Solomon 1:4

**Issue**: Algorithm conflated two different invitation types:
1. **"Let us DO X together"** → INCLUSIVE (shared action)
2. **"Stay/Join WITH us"** → EXCLUSIVE (invitation to join pre-existing group)

**Successes**:
- Mark 1:38 ✅ "Let us go" - INCL (Jesus + disciples doing action together)
- Nehemiah 2:17 ✅ "Let us build" - INCL (Nehemiah + people doing action together)

**Failures**:
- Luke 24:29 ❌ "Stay with us" - predicted INCL, actual EXCL (invitation TO join existing group)
- Song of Solomon 1:4 ❌ "We will rejoice" - predicted INCL, actual EXCL (chorus excluding beloved)

**Pattern**:
- **INCLUSIVE invitations**: Speaker invites addressee to DO action together (go, build, etc.)
- **EXCLUSIVE invitations**: Speaker invites addressee to JOIN existing group (stay with us, come to us)

**Root cause**: Rule 2.5 (Worship invitation) was overapplied to all invitation-like structures.

**Fix needed**: Refine Rule 2.5 to distinguish:
- "Let us [action]" = INCLUSIVE (joint action)
- "[Action] with us" = EXCLUSIVE (join our group)

---

### Error Pattern 3: Quoted Speech (1 error)
**Verse**: 2 Kings 18:22

**Issue**: Failed to analyze nested speaker structure

**Context**: Assyrian commander (Rabshakeh) quoting hypothetical response from Jerusalem
- Outer speaker: Rabshakeh (Assyrian, hostile)
- Inner quote: "We trust in the LORD our God" (Jerusalem's hypothetical words)

**Prediction**: INCLUSIVE (Jerusalem representatives including people)
**Actual**: EXCLUSIVE (excludes Rabshakeh, the outer speaker)

**Pattern**: In quoted speech, clusivity is determined by the INNER quote's perspective, but the outer speaker context matters when they're explicitly excluded from the group.

**Fix needed**: Add rule for quoted speech - when hostile/outsider quotes in-group speech, the quote will use EXCLUSIVE to distinguish the quoted group from the quoter.

---

### Error Pattern 4: Role Distinction Misread (1 error - different direction)
**Verse**: James 3:1

**Issue**: Algorithm predicted EXCLUSIVE (teachers as separate class), but translations use INCLUSIVE

**Prediction**: EXCLUSIVE (Rule 3.3 - hierarchical authority creates distinction)
**Actual**: INCLUSIVE (James includes self and potential teachers in warning)

**Pattern**: When speaker:
- Includes themselves in the role ("we who teach")
- Addresses people who might hold that role
- Uses humble/warning tone (not asserting superiority)
→ Translators choose INCLUSIVE to show community, not hierarchy

**Fix needed**: Refine Rule 3.3 - role distinction only triggers EXCLUSIVE when speaker:
- Asserts authority OVER addressees
- Excludes addressees from the role
- Creates hierarchical separation

Don't apply when speaker humbly includes self and invites addressees into accountability.

---

## Cross-Linguistic Validation Strength

### Language Agreement Levels

**100% Agreement (Strong Evidence)**:
- Psalm 44:1 - EXCL (Tag, Ind unanimous)
- 1 John 4:19 - INCL (Tag, Ind unanimous)
- Genesis 42:21 - INCL (Tag, Ind unanimous)
- Acts 16:10 - EXCL (Tag, Ind unanimous)
- Daniel 2:36 - EXCL (Tag, Ind unanimous)
- Jonah 1:14 - EXCL (Tag, Ind unanimous)
- Joshua 24:15 - EXCL (Tag, Ind, Ceb unanimous)
- 2 Kings 18:22 - EXCL (Tag, Ind unanimous)
- Jeremiah 3:22 - EXCL (Tag, Ind unanimous)
- Ezekiel 33:10 - EXCL (Tag, Ind unanimous)
- Mark 1:38 - INCL (Tag, Ind, Tok, Fij unanimous)
- Luke 24:29 - EXCL (Tag, Ind, Tok, Fij unanimous)
- Philippians 3:20 - INCL (Tag, Ind, Tok unanimous)
- 1 Peter 2:24 - INCL (Tag, Ind, Tok unanimous)

**80-99% Agreement (Strong but with variation)**:
- James 3:1 - INCL (4 major trans vs 1 minor)
- Jeremiah 42:20 - INCL for "our God" (5 of 6 trans)

**Mixed/Evolution (Weak Evidence)**:
- Psalm 66:6 - Old trans EXCL, modern trans INCL
- Ephesians 2:3 - Most INCL, some theological EXCL
- Isaiah 9:6 - Mostly INCL, one outlier EXCL

### Reliability Assessment

**Highest confidence**: When 4+ unrelated language families agree (e.g., Tag + Ind + Tok + Fij)
**High confidence**: When Tag + Ind agree consistently
**Medium confidence**: When 80%+ of translations agree
**Low confidence**: When translations vary by age or theology

---

## Algorithm Performance by Rule

### Rule Success Rates

| Rule | Verses Tested | Correct | Accuracy | Notes |
|------|---------------|---------|----------|-------|
| 2.1 Prayer to God | 4 | 2 | 50% | ❌ Needs strengthening |
| 2.3 We/you contrast | 1 | 1 | 100% | ✅ Works well |
| 2.4 Reciprocal | 1 | 1 | 100% | ✅ Works well |
| 2.5 Invitation | 4 | 2 | 50% | ⚠️ Needs semantic refinement |
| 2.6 Narrative "we" | 1 | 1 | 100% | ✅ Works well |
| 3.1 Shared experience | 8 | 5 | 63% | ⚠️ Overrides other rules incorrectly |
| 3.3 Authority | 1 | 0 | 0% | ❌ Needs complete revision |

### Rules Needing Revision

**Priority 1 - Critical Fixes**:
1. **Rule 2.1 (Prayer to God)**: Make this a stronger/earlier rule that overrides "shared experience"
   - ANY speech TO God → EXCLUSIVE (even if corporate/shared content)
   - Psalm 44:1, Ezekiel 33:10 failures show this must override Rule 3.1

2. **Rule 2.5 (Invitation)**: Split into two sub-rules:
   - 2.5a: "Let us [action]" → INCLUSIVE (joint action)
   - 2.5b: "[Action] with/to us" → EXCLUSIVE (join our group)
   - Luke 24:29 failure shows semantic distinction matters

**Priority 2 - Refinement**:
3. **Rule 3.3 (Authority)**: Only apply when speaker asserts superiority
   - James 3:1 failure shows humble self-inclusion → INCLUSIVE

4. **Rule 3.1 (Shared experience)**: Should not override prayer/address patterns
   - Currently too dominant, needs to yield to structural rules

**Priority 3 - New Rules**:
5. **Add Rule for Quoted Speech**: When outsider quotes in-group speech → EXCLUSIVE
   - 2 Kings 18:22 failure suggests this pattern

---

## Confidence Calibration Analysis

### By Prediction Confidence Level

| Confidence | Predictions | Correct | Accuracy | Expected | Delta |
|------------|-------------|---------|----------|----------|-------|
| 90-95% | 10 | 7 | 70% | 90%+ | -20% ❌ |
| 85% | 2 | 1 | 50% | 85% | -35% ❌ |
| 70-75% | 4 | 2 | 50% | 70%+ | -20% ❌ |
| 65% | 1 | 1 | 100% | 65% | +35% |
| 40-50% | 2 | 1 | 50% | 45% | +5% |

**Finding**: Algorithm is overconfident
- High-confidence predictions (85-95%) only achieved 50-70% accuracy
- Expected 85-95%, actual 50-70% = **20-35 point confidence gap**

**Recommendation**: Reduce all confidence levels by 20-25 points OR fix systematic errors that are causing high-confidence failures.

---

## Unexpected Finding: Random Test Difficulty

### Why Did Random Test Underperform?

**Expected**: Random test 80-90%, Adversarial test 60-70%
**Actual**: Random test 50-60%, Adversarial test 73%

**Possible explanations**:

1. **Selection bias in random test**: The "random" verses happened to include multiple prayer/lament verses that exposed systematic Rule 2.1 weakness
   - Jeremiah 3:22 (prayer)
   - Ezekiel 33:10 (lament to God)
   - 2 Kings 18:22 (quoted speech)
   - Luke 24:29 (invitation semantics)

2. **Adversarial test well-designed**: The adversarial test happened to focus on patterns the algorithm handles well:
   - Narrative "we" (Acts 16:10) ✅
   - Clear invitations (Nehemiah 2:17) ✅
   - Explicit prayers (Jonah 1:14) ✅

3. **Algorithm has systematic blind spots** that correlate with common verse types:
   - Prayer/lament structure (common in Psalms, Prophets)
   - Invitation semantics (common in Gospels)
   - Quoted speech (common in narrative)

**Implication**: The algorithm may perform worse on "normal" Bible verses than on specially-selected hard cases, because normal verses include many prayers/laments that exploit the Rule 2.1 weakness.

---

## Validation Methodology Assessment

### Strengths
✅ Used 5+ clusivity-marking languages (Tagalog, Indonesian, Tok Pisin, Fijian, Cebuano)
✅ Checked multiple translations per language when available
✅ Cross-linguistic agreement provides strong ground truth
✅ Independent validation (predictions locked before checking translations)

### Limitations
⚠️ Some verses had limited language coverage (only Tag + Ind)
⚠️ Old vs. new translation variation in some verses (Psalm 66:6)
⚠️ Theological variation possible (Ephesians 2:3)
⚠️ Could not access TBTA to compare with original annotations

### Reliability Tiers
- **Tier 1 (Highest)**: 4+ unrelated languages agree (10 verses)
- **Tier 2 (High)**: Tag + Ind agree unanimously (14 verses)
- **Tier 3 (Medium)**: 80%+ translations agree (2 verses)
- **Tier 4 (Low)**: Translations vary (3 verses)

**Overall assessment**: Validation methodology is sound. Translation agreement provides reliable ground truth superior to any single annotation system.

---

## Comparison with Training Set Performance

### Training vs. Test Performance

| Metric | Training Set | Test Set | Delta |
|--------|--------------|----------|-------|
| Total verses | 7 | 21 | +14 |
| Accuracy | 100% | 62% | -38% ❌ |
| High-confidence accuracy | 100% | 50-70% | -30-50% ❌ |

**Finding**: Severe overfitting to training data

**Evidence**:
- Training: 100% (7/7 verses)
- Test: 62% (13/21 verses)
- **38-point accuracy drop** indicates algorithm learned training examples rather than underlying patterns

**This is a classic machine learning problem**: Model memorizes training data but fails to generalize.

---

## Algorithm v2.0 Recommendations

### Critical Fixes (Must Implement)

1. **Strengthen Prayer Rule (2.1)**:
   ```
   IF speech is addressed TO deity (prayer, lament, petition, praise to God)
   THEN → EXCLUSIVE (speaker excludes deity from "we/us")
   PRIORITY: HIGHEST (override "shared experience")
   ```

2. **Split Invitation Rule (2.5)**:
   ```
   IF "Let us [action]" (hortatory subjunctive)
   THEN → INCLUSIVE (speaker invites addressee to joint action)

   IF "[Action] with us" OR "Come/stay to us" (locative)
   THEN → EXCLUSIVE (speaker invites addressee to join pre-existing group)
   ```

3. **Revise Authority Rule (3.3)**:
   ```
   IF speaker claims authority OVER addressees (not WITH them)
   AND speaker excludes addressees from role
   THEN → EXCLUSIVE

   IF speaker humbly includes self in role/warning
   AND addressees are potential role-holders
   THEN → INCLUSIVE
   ```

4. **Downgrade Shared Experience Rule (3.1)**:
   ```
   Shared experience → INCLUSIVE
   EXCEPT when overridden by:
   - Prayer structure (Rule 2.1)
   - We/you contrast (Rule 2.3)
   - Quoted speech patterns
   ```

### Additional Rules to Add

5. **Quoted Speech Rule (NEW)**:
   ```
   IF outsider/hostile party quotes in-group speech
   AND quoter is explicitly excluded from in-group
   THEN → EXCLUSIVE (in-group excludes quoter)
   ```

6. **Lament Structure Rule (NEW)**:
   ```
   IF corporate lament addressed TO God
   THEN → EXCLUSIVE (people exclude God even in shared suffering)
   ```

### Confidence Calibration Adjustments

Reduce all confidence levels by 20 points until systematic errors are fixed:
- Current 95% → New 75%
- Current 85-90% → New 65-70%
- Current 70-75% → New 50-55%
- Current 40-50% → New 20-30%

OR fix the systematic errors and re-validate before claiming high confidence.

---

## Production Readiness Assessment

### Current Status: **NOT READY** ❌

**Reasons**:
1. ❌ Test accuracy 62% is below production threshold (need 80%+)
2. ❌ Confidence calibration broken (high confidence only 50-70% accurate)
3. ❌ Systematic errors in common patterns (prayer, invitation, quoted speech)
4. ❌ Algorithm overfits training data (38-point accuracy drop)
5. ❌ Random test underperformed (50-60% vs 80-90% target)

### Requirements for Production Approval

**Minimum requirements**:
- [ ] Test accuracy ≥ 80% (current: 62%)
- [ ] High-confidence accuracy ≥ 85% (current: 50-70%)
- [ ] Random test ≥ 80% (current: 50-60%)
- [ ] Adversarial test ≥ 60% (current: 73% ✅)
- [ ] Confidence calibration within 10% (current: -20 to -35%)
- [ ] No systematic blind spots in common patterns

**Current achievement**: 1/6 requirements met

**Estimated work needed**:
- Implement 4 critical rule fixes
- Re-test on same test set (should improve to ~75-80%)
- Design and test additional random sample (validate generalization)
- Re-calibrate confidence levels
- Estimated timeline: 1-2 weeks of focused work

---

## Success Assessment vs. Original Goals

### Original Adversarial Methodology Goals

**Goal 1**: Design adversarial test set to find weaknesses
- ✅ **ACHIEVED** - Test set successfully identified errors

**Goal 2**: Achieve 60-70% on adversarial test
- ✅ **ACHIEVED** - 73% accuracy (within range)

**Goal 3**: Achieve 80-90% on random test
- ❌ **MISSED** - Only 50-60% accuracy

**Goal 4**: Show 20-25 point gap (random >> adversarial)
- ❌ **INVERTED** - Adversarial exceeded random by 13-23 points

### Unexpected Discovery

The methodology successfully discovered that the algorithm has **systematic blind spots in common verse patterns** (prayer, lament, invitation semantics) that are MORE prevalent in "normal" verses than in carefully-selected adversarial cases.

**This is actually a valuable finding** - it shows the algorithm is weaker than training performance suggested, which is critical to know before production deployment.

---

## Lessons Learned

### Methodology Lessons

1. ✅ **Blind prediction locking works**: Git commit of predictions before validation prevents data leakage
2. ✅ **Cross-linguistic validation is powerful**: Agreement across 4+ languages provides reliable ground truth
3. ✅ **Adversarial testing finds real errors**: 3 errors in adversarial set revealed algorithm weaknesses
4. ⚠️ **"Random" sampling needs care**: Random test happened to hit systematic blind spots

### Algorithm Lessons

1. ❌ **Training accuracy ≠ Test accuracy**: 100% → 62% shows severe overfitting
2. ❌ **High confidence ≠ High accuracy**: 95% confidence only achieved 70% accuracy
3. ❌ **Prayer pattern is underweighted**: Rule 2.1 needs to be stronger/earlier in hierarchy
4. ❌ **Invitation semantics are more complex**: "Let us go" ≠ "Stay with us"
5. ✅ **Some rules work well**: Reciprocal (2.4), We/you contrast (2.3), Narrative (2.6) all 100%

### Feature Development Lessons

1. ✅ **Methodology is sound**: Train → Lock → Test → Validate process works
2. ❌ **Cannot claim "COMPLETE" without test validation**: Training validation is insufficient
3. ✅ **Test failures are valuable**: Each error reveals algorithm weaknesses
4. ⚠️ **May need iteration**: Algorithm v1.0 → v2.0 → v2.1 until test accuracy acceptable

---

## Next Steps

### Immediate (This Session)

1. ✅ Complete test validation (DONE)
2. ⏳ Create algorithm v2.0 with critical fixes
3. ⏳ Update feature status to ~65% complete (training 100%, test validation 100%, algorithm needs revision)
4. ⏳ Commit all validation results
5. ⏳ Update FEATURE-STATUS-SUMMARY

### Short-term (Next Session)

1. Implement algorithm v2.0 with 4 critical rule fixes
2. Re-test on same 21 verses to measure improvement
3. Target: 75-80% accuracy after fixes
4. Re-calibrate confidence levels based on actual performance

### Medium-term (Before Production)

1. Design new random test set (20 verses) avoiding previous test verse patterns
2. Make blind predictions with algorithm v2.0
3. Validate new random test
4. Target: 80%+ on new random test
5. If achieved → production ready
6. If not → algorithm v2.1 iteration

---

## Conclusion

The test validation phase has been **highly successful at discovering algorithm weaknesses**, even though the results show the algorithm is not yet production-ready.

**Key achievements**:
- ✅ Validated 21 verses across 5 clusivity-marking languages
- ✅ Achieved adversarial test target (73% vs 60-70% target)
- ✅ Identified 4 systematic error patterns with clear fixes
- ✅ Demonstrated cross-linguistic validation methodology
- ✅ Proved blind prediction methodology prevents overfitting detection

**Key limitations**:
- ❌ Missed random test target (50-60% vs 80-90% target)
- ❌ Overall test accuracy 62% (need 80% for production)
- ❌ High-confidence predictions only 50-70% accurate
- ❌ Algorithm overfits training data (38-point drop)

**Honest assessment**:
This feature is approximately **65% complete**:
- Training phase: 100% ✅
- Test design: 100% ✅
- Test validation: 100% ✅
- Algorithm refinement: 0% ⏳ (v2.0 needs implementation and re-testing)
- Production approval: 0% ⏳ (pending 80%+ test accuracy)

**The critical discovery**: Algorithm has systematic blind spots in prayer/lament structures and invitation semantics that are MORE common in normal verses than in adversarial cases. This explains why random test underperformed and shows why test validation is essential before production deployment.

---

**Status**: Test validation COMPLETE, algorithm revision REQUIRED
**Grade**: B (excellent methodology, algorithm needs significant fixes before production)
**Recommendation**: Implement algorithm v2.0 with 4 critical fixes, then re-validate
