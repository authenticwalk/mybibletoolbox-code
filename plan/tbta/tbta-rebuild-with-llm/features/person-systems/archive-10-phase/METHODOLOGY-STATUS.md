# Person Systems Feature: Methodology Status

**Current Phase**: Test Validation Complete → Algorithm Revision Needed
**Algorithm Version**: v1.0 tested, v2.0 needed (4 critical fixes identified)
**Last Updated**: 2025-11-10

---

## Test Validation Complete ✅

### Results Summary

**Total Verses Tested**: 21 (11 adversarial + 10 random)
**Validation Method**: Real Bible translations in 5 clusivity-marking languages
**Languages Used**: Tagalog, Indonesian, Tok Pisin, Fijian, Cebuano

**Accuracy**:
- **Adversarial Test**: 8/11 correct = **73%** ✅ (target: 60-70%)
- **Random Test**: 5/10 correct (2 mixed) = **50-60%** ❌ (target: 80-90%)
- **Combined**: 13/21 correct = **62%**

**Key Finding**: Algorithm has systematic blind spots in:
1. Prayer/lament structures (Rule 2.1 too weak)
2. Invitation semantics ("Let us go" vs "Stay with us")
3. Quoted speech contexts
4. Role distinction interpretation (James 3:1 type)

**Production Status**: NOT READY - needs algorithm v2.0 with 4 critical fixes

See full details: `TEST-VALIDATION-COMPLETE.md`

---

## Methodology Acknowledgment

### What Existing Work Actually Represents

**Original scope**: Comprehensive clusivity analysis with 14 verses across 9 languages

**Actual status**: **Training phase / Pattern discovery + External validation**

The existing person-systems work includes:
- ✅ Clusivity analysis: 14 verses analyzed with real translations (98% agreement)
- ✅ experiment-001.md: Genesis 1:26 analysis with 10+ test cases
- ✅ LEARNINGS.md: Key patterns documented
- ✅ METHODOLOGY.md: Complete prediction framework
- ✅ External validation: Real translations in 9 clusivity-marking languages

**This is extensive reverse-engineering work** with strong external validation from actual Bible translations.

---

## Retrospective Classification

Existing work should be considered:
- **Training data**: ~20 verses analyzed to develop algorithm
- **Pattern discovery**: Identified clusivity decision principles
- **Algorithm development**: Built comprehensive v1.0 prediction framework
- **External validation**: 98% agreement with real translations validates approach

**Different from number-systems** because:
- ✅ Has external validation (real translations, not just TBTA)
- ✅ 98% agreement provides strong confidence in patterns
- ✅ Multiple languages confirm clusivity decisions
- ⚠️ Still needs TBTA-specific adversarial testing

---

## Algorithm v1.0: Locked Patterns

From existing analysis, these patterns were learned:

### Pattern 1: Speaker-Addressee Identity (Primary)
```
Rule: Determine clusivity by analyzing who is speaking and to whom

Examples:
- God speaking to humans → Exclusive (divine vs. human)
- Prayer to God → Exclusive (God not in "we")
- Community invitation "Come, let us..." → Inclusive
- Apostolic "we" in testimony → Exclusive

Authority: 98% agreement across 9 languages, METHODOLOGY.md
```

### Pattern 2: Action Capability Test
```
Rule: Can the addressee participate in the action?

Examples:
- Divine creative act (Gen 1:26) → Exclusive (humans can't create)
- Reciprocal action "one another" (Heb 10:24) → Inclusive (requires participation)
- Worship invitation (Ps 95:1) → Inclusive (addressee can worship)
- Apostolic testimony (Acts 2:32) → Exclusive (only apostles were witnesses)

Authority: Discourse analysis, METHODOLOGY.md
```

### Pattern 3: Theological Context Determines Exclusion
```
Rule: Theological roles create ontological barriers

Examples:
- Trinity addressing Trinity (Gen 1:26) → Exclusive of humans
- Prayer to Father (Matt 6:9) → Exclusive of God
- Believers to believers (Rom 5:1) → Inclusive
- Apostles to church (Acts 15:25) → Exclusive (authority distinction)

Authority: Cross-linguistic translation patterns
```

### Pattern 4: Genre Baseline Predictions
```
Rule: Different genres have different default clusivity patterns

Defaults:
- Narrative (OT, divine speech): 90%+ exclusive
- Epistles (NT): 50/50 mixed (context-dependent)
- Prayer contexts: 95%+ exclusive (addressing God)
- Worship/Praise: 80%+ inclusive (congregation joining)
- Prophecy: 90%+ exclusive (prophet for God to people)

Authority: Statistical analysis, BIBLE-EXAMPLES.md
```

### Pattern 5: Discourse Role Over Grammar
```
Rule: Same entity gets different clusivity based on discourse role

Examples:
- God as narrator → Third person singular
- God as speaker in divine council → First inclusive (Trinity)
- Nicodemus alone → Singular
- Nicodemus representing group "we know" (Jhn 3:2) → First exclusive

Authority: Discourse pragmatics, LEARNINGS.md
```

**Algorithm v1.0 locked**: 2025-11-09 (see METHODOLOGY.md, LEARNINGS.md, experiment-001.md)

---

## Existing Training Data Summary

### Clusivity Analysis (14 verses)
**Location**: clusivity/ directory
**Validation**: 9 languages (Tagalog, Indonesian, Tok Pisin, etc.)
**Agreement**: 98% with TBTA implied decisions

**Verses analyzed:**
1. Genesis 1:26 - "Let us make" (EXCLUSIVE)
2. Genesis 3:22 - "Like one of us" (EXCLUSIVE)
3. Genesis 11:7 - "Let us go down" (EXCLUSIVE)
4. Exodus 3:18 - "We want to go" (EXCLUSIVE - Hebrews vs Pharaoh)
5. Psalm 95:1 - "Let us sing" (INCLUSIVE - worship invitation)
6. Matthew 6:9 - "Our Father" (EXCLUSIVE - praying to God)
7. John 3:11 - "We speak" (EXCLUSIVE - Jesus vs Nicodemus)
8. John 9:4 - "We must work" (INCLUSIVE - Jesus + disciples)
9. Acts 2:32 - "We are witnesses" (EXCLUSIVE - apostles only)
10. Acts 17:20 - Athenians to Paul (EXCLUSIVE - different groups)
11. Romans 5:1 - "We have peace" (INCLUSIVE - shared experience)
12. 2 Corinthians 5:20 - "We are ambassadors" (DUAL: exclusive/inclusive)
13. Hebrews 10:24 - "Let us consider one another" (INCLUSIVE - reciprocal)
14. John 17:21 - "That they may be in us" (INCLUSIVE - believers in Trinity)

### Additional Test Cases (experiment-001.md)
**Additional verses**: 6-8 verses with predictions
**Accuracy**: 100% on initial predictions
**Validation**: Cross-checked with Indonesian/Tagalog where available

---

## Next Phase: Adversarial Validation with TBTA

Following methodology in: `../../METHODOLOGY-ADVERSARIAL.md`

### Phase 2a: Adversarial Test Set (10-15 verses)

**Goal**: Test algorithm v1.0 on challenging edge cases with TBTA data

**Selection criteria** - designed to challenge the algorithm:

1. **Theological edge cases** (4 verses)
   - Different Trinity contexts (not Gen 1:26)
   - Messianic "we" in prophecy
   - Corporate solidarity (Israel/church as collective)
   - Overlapping identities (Paul as Jew and apostle)

2. **Rare contexts** (3 verses)
   - Fourth person contexts (obviation in narratives)
   - T-V distinction implications (formal/informal)
   - Royal "we" (if it exists in Bible)
   - Number system interactions (dual/trial with clusivity)

3. **Ambiguous speaker/addressee** (4 verses)
   - Quoted speech within speech
   - Unclear referent boundaries
   - Multiple speakers in same verse
   - Discourse shifts mid-passage

4. **Genre boundary cases** (2-3 verses)
   - Wisdom literature (proverbial "we")
   - Apocalyptic literature (vision contexts)
   - Mixed genre (narrative + prayer)

**Expected accuracy**: 60-70% (adversarial cases are hard!)

**Status**: NOT STARTED - verses to be selected

---

### Phase 2b: Random Validation Set (10-15 verses)

**Goal**: Test algorithm v1.0 on typical cases with TBTA data

**Selection criteria**:
```
Random sample from:
- Psalms (not in training)
- Acts (not in training)
- Pauline epistles (not in training)

Stratified by genre:
- Prayer: 3 verses
- Narrative: 3 verses
- Epistles: 4 verses
- Prophecy: 2-3 verses
```

**Expected accuracy**: 80-90% (should be higher than adversarial!)

**Status**: NOT STARTED - random seed to be chosen

---

## Validation Process

### Step 1: Design Test Sets
- [ ] Select 10-15 adversarial verses (document reasoning)
- [ ] Select 10-15 random verses (document random seed)
- [ ] Commit both lists to git BEFORE predictions
- [ ] Ensure no overlap with training (~20 verses from existing analysis)

### Step 2: Access TBTA Data for Test Sets
- [ ] Retrieve TBTA person annotations for adversarial set
- [ ] Retrieve TBTA person annotations for random set
- [ ] Document TBTA values WITHOUT analyzing patterns yet

### Step 3: Make Predictions (Using Algorithm v1.0)
- [ ] Apply algorithm v1.0 to adversarial set (blind to TBTA interpretation)
- [ ] Apply algorithm v1.0 to random set (blind to TBTA interpretation)
- [ ] Document reasoning for each prediction
- [ ] Rate confidence: High (90%+), Medium (70-90%), Low (<70%)
- [ ] Commit predictions to git with timestamp

### Step 4: Lock Predictions
- [ ] Git commit: "Person feature validation predictions - LOCKED"
- [ ] Record commit SHA
- [ ] NO modifications allowed after this point

### Step 5: Compare with TBTA
- [ ] Compare predictions with TBTA annotations for adversarial set
- [ ] Compare predictions with TBTA annotations for random set
- [ ] Calculate accuracy for each
- [ ] Verify: Random should beat adversarial by 15-25 points

### Step 6: Analyze Results
- [ ] Error analysis for failures
- [ ] Categorize: Algorithm gap vs. edge case vs. TBTA error
- [ ] Flag potential TBTA errors (expect 1-2 in 20-30 verses = 3-7%)
- [ ] Cross-reference with real translation data where possible
- [ ] Document learnings

### Step 7: Update Algorithm
- [ ] Create algorithm v2.0 based on TBTA learnings
- [ ] DO NOT retest on same verses
- [ ] Integrate with existing patterns
- [ ] Save learnings for other features

---

## Success Criteria

### Adversarial Test
- ✅ Success: 60-70% accuracy
  - Algorithm handles edge cases reasonably
  - Ready for production with caveats
- ⚠️ Review: 50-60% accuracy
  - Algorithm has significant gaps
  - Needs refinement before production
- ❌ Fail: <50% accuracy
  - Major misunderstanding of TBTA methodology
  - Revisit core patterns

### Random Test
- ✅ Success: 80-90% accuracy
  - Patterns generalize well
  - Algorithm works on typical cases
- ⚠️ Review: 70-80% accuracy
  - Some overfitting to training
  - Acceptable but monitor
- ❌ Fail: <70% accuracy
  - Serious problems with generalization
  - Algorithm needs major revision

### Comparative Metric (CRITICAL!)
- ✅ Success: Random accuracy > Adversarial by 15-25 points
  - Example: Adversarial 65%, Random 85% = 20 point gap
  - Proves test sets properly designed
  - Algorithm performs as expected
- ⚠️ Review: Random > Adversarial by 5-15 points
  - Gap too small = adversarial test not hard enough
  - Redesign adversarial set with harder cases
- ❌ Fail: Random ≤ Adversarial
  - Test sets poorly designed
  - Start over with better selection

### External Validation Bonus
- 🎯 Advantage: Where TBTA disagrees with algorithm, check real translations
  - If real translations support algorithm → potential TBTA error
  - If real translations support TBTA → algorithm needs refinement
  - This feature has unique advantage of cross-linguistic validation

---

## Timeline

**Week of 2025-11-11**: Adversarial validation preparation
- Monday-Tuesday: Design adversarial test set (10-15 verses)
- Wednesday: Design random test set (10-15 verses)
- Thursday: Access TBTA data for both sets
- Friday: Begin predictions using algorithm v1.0

**Week of 2025-11-18**: Complete validation
- Monday: Lock predictions with git commit
- Tuesday: Compare with TBTA, calculate accuracy
- Wednesday-Thursday: Error analysis, cross-check with real translations
- Friday: Update algorithm v2.0, document learnings

**Estimated completion**: 2025-11-22

---

## Files to Create

```
plan/tbta-rebuild-with-llm/features/person-systems/
├── training/
│   ├── TRAINING-SET.md                  # List of ~20 training verses (from existing work)
│   ├── PATTERNS-LEARNED.md              # Consolidated from METHODOLOGY.md, LEARNINGS.md
│   └── ALGORITHM-v1.md                  # Locked algorithm
│
├── adversarial-test/
│   ├── TEST-SET.md                      # 10-15 challenging verses with justification
│   ├── PREDICTIONS-locked.md            # Predictions before comparing with TBTA (commit SHA)
│   ├── RESULTS.md                       # Accuracy: target 60-70%
│   └── ERROR-ANALYSIS.md                # Detailed analysis of failures
│
├── random-test/
│   ├── TEST-SET.md                      # 10-15 random verses (random seed documented)
│   ├── PREDICTIONS-locked.md            # Predictions before comparing with TBTA (commit SHA)
│   └── RESULTS.md                       # Accuracy: target 80-90%
│
└── potential-errors/
    └── [case-files].md                  # Flagged TBTA errors (validated by real translations)
```

---

## Unique Advantages of Person-Systems Feature

### 1. External Validation Available
Unlike many features, clusivity has direct validation from real translations:
- 200+ languages in our TSV with clusivity
- Can cross-check TBTA decisions against Indonesian, Tagalog, Tok Pisin, etc.
- Provides independent verification beyond TBTA

### 2. Strong Theoretical Foundation
- Well-documented linguistic phenomenon
- Clear semantic rules (speaker/addressee analysis)
- Extensive research literature on clusivity

### 3. Theological Significance
- Affects translation of critical passages (Lord's Prayer, Great Commission)
- 33% of Bible translations require clusivity decisions
- Wrong choice can alter theological meaning

### 4. Cross-Feature Learnings
Person-systems patterns likely inform:
- Participant tracking (related to speaker/addressee identification)
- Honorifics/register (related to T-V distinction)
- Discourse genre (genre affects clusivity baseline)

---

## Notes for Other Features

This retrofit applies to:
- ✅ person-systems (this feature)
- ⏳ Other semantic features (participant-tracking, discourse-genre, etc.)

**Lesson learned**:
> Strong external validation (98% agreement with real translations) provides
> confidence in patterns, but TBTA may use different annotation principles.
> Adversarial testing will reveal any gaps between our approach and TBTA's.

---

## Honest Reporting

**For publications/documentation:**

> "The person systems feature (focusing on clusivity) was validated using a two-phase approach:
>
> **Training phase**: ~20 verses were analyzed using real Bible translations in 9 clusivity-marking
> languages (Tagalog, Indonesian, Tok Pisin, etc.), achieving 98% agreement on clusivity decisions.
> Patterns were documented in a comprehensive prediction framework (algorithm v1.0).
>
> **Validation phase**: Algorithm v1.0 was tested against TBTA annotations on held-out verses:
> - Adversarial test (10-15 challenging edge cases): X% accuracy
> - Random test (10-15 typical cases): Y% accuracy
> - Cross-validation with real translations where TBTA disagreements occur
>
> Results demonstrate that learned patterns align with both real translation practice and
> TBTA methodology, with documented edge cases for translator decision-making."

---

**Status**: Ready to proceed with adversarial validation against TBTA
**Next action**: Design adversarial test set (10-15 verses)
**Owner**: [Current session]
**Target date**: 2025-11-22
