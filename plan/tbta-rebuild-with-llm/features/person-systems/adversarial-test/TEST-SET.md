# Person Systems: Adversarial Test Set

**Feature**: Person Systems (Clusivity)
**Test Set Size**: 15 verses
**Selection Date**: 2025-11-09
**Purpose**: Challenge algorithm v1.0 with edge cases
**Expected Accuracy**: 60-70% (deliberately challenging)

---

## Selection Strategy

This test set is **deliberately designed to break the algorithm** by selecting:
- ❌ Cases NOT covered clearly in training
- ❌ Verses with theological ambiguity
- ❌ Contexts where rules might conflict
- ❌ Translation-divergent passages
- ❌ Discourse complexity

**Note**: If we get >75% accuracy, the test wasn't adversarial enough!

---

## Adversarial Test Verses (15 total)

### Category 1: Theological Edge Cases (4 verses)

#### 1. Isaiah 9:6 - Messianic Names
**Text**: "For to us a child is born, to us a son is given"
**Challenge**: Who is "us"?
- Speaker: Prophet/God?
- Addressee: Israel? All humanity?
- Is this INCLUSIVE (all who receive) or EXCLUSIVE (Israel specifically)?
**Why adversarial**: Messianic prophecy with unclear scope of "us"
**Rule conflict**: Could be shared experience (Rule 3.1) OR ethnic group (Rule 3.2)
**Translation divergence**: Some versions emphasize universal, others Jewish-specific

#### 2. Psalm 44:1 - Corporate Israel
**Text**: "We have heard with our ears, O God, our fathers have told us"
**Challenge**: Corporate solidarity - Israel as collective
- Speaker: Psalmist representing all Israel (past + present)?
- "We" = current generation, "fathers" = previous generation
- Temporal dimension complicates clusivity
**Why adversarial**: Corporate identity across generations
**Rule conflict**: Shared identity (Rule 3.1) vs. discourse role (Rule 5.1)

#### 3. Numbers 23:19 - God is not a man
**Text**: "God is not man, that he should lie, not a son of man, that he should change his mind"
**Context**: Balaam's oracle - does it contain first-person plural?
**Challenge**: Need to verify if there's a "we" in this context
**Why considered**: Ontological distinction between divine and human
**Note**: May not have clusivity test - verify Hebrew text

#### 4. 1 John 4:19 - "We love because he first loved us"
**Challenge**: Who is "we" and "us"?
- Speaker: John
- Addressee: Believers
- But "us" includes all believers (including addressees)
- Does "we love" = INCLUSIVE or is John speaking for a group?
**Why adversarial**: Layered reference - "us" is inclusive but "we" subject is ambiguous
**Rule conflict**: Shared experience (inclusive) vs. epistle default

---

### Category 2: Ambiguous Speaker/Addressee (4 verses)

#### 5. Genesis 42:21 - Brothers discussing guilt
**Text**: "Then they said to one another, 'In truth we are guilty concerning our brother'"
**Challenge**:
- Speaker: Brothers (as group)
- Addressee: Each other
- "We" = all brothers (inclusive of addressees)
- But speaking about Joseph who is NOT included (and secretly present!)
**Why adversarial**: Multiple layers - inclusive of speakers, exclusive of Joseph, who is actually listening
**Rule conflict**: Who counts as addressee when speaking "to one another"?

#### 6. Jeremiah 42:20 - Prophet quoting people quoting themselves
**Text**: "For you have gone astray at the cost of your lives, for you sent me to the LORD your God, saying, 'Pray for us to the LORD our God'"
**Challenge**:
- Quoted prayer within Jeremiah's rebuke
- Inner quote: "our God" (people praying to God - should be EXCLUSIVE of God)
- Outer context: People sent Jeremiah (distinction between people and prophet?)
**Why adversarial**: Multi-level quotation, discourse boundaries unclear
**Rule testing**: Does prayer rule (2.1) apply inside quotes?

#### 7. Song of Solomon 1:4 - Multiple speakers
**Text**: "We will exult and rejoice in you; we will extol your love"
**Challenge**:
- Speaker: Daughters of Jerusalem? Bride? Chorus?
- Addressee: Beloved
- Poetry with shifting speakers throughout
**Why adversarial**: Unclear speaker identity affects clusivity determination
**Rule conflict**: Cannot apply algorithm without knowing speaker

#### 8. Acts 16:10 - "We" sections begin
**Text**: "When he had seen the vision, immediately we sought to go on into Macedonia"
**Challenge**:
- Sudden shift to first-person plural (Luke's travel narrative)
- Speaker: Luke (author) + Paul + companions
- Addressee: Readers (who were not present)
- Clear EXCLUSIVE, but tests narrative "we" in historical account
**Why adversarial**: Shifts from third person to first person suddenly
**Expected**: EXCLUSIVE (author's travel group), but narrative shift is noteworthy

---

### Category 3: Rare/Complex Contexts (4 verses)

#### 9. Daniel 2:36 - Royal "we" or plural?
**Text**: "This was the dream. Now we will tell the king its interpretation"
**Challenge**:
- Speaker: Daniel
- But uses plural "we" - is this:
  a) Royal "we" (singular speaker using plural)
  b) Daniel + God (prophetic "we")
  c) Daniel + companions
**Why adversarial**: Tests whether royal "we" exists, or if alternative explanation applies
**Rule testing**: If royal "we" exists, what is clusivity classification?

#### 10. Nehemiah 2:17 - Leader to people
**Text**: "Then I said to them, 'You see the trouble we are in, how Jerusalem lies in ruins. Come, let us build the wall of Jerusalem'"
**Challenge**:
- First "we" = inclusive (Nehemiah + people in trouble together)
- Second "us" = inclusive (invitation to build together)
- But Nehemiah is leader - any authority distinction?
**Why adversarial**: Tests transition from shared problem to shared action
**Expected**: Both INCLUSIVE, but tests consistency within single verse

#### 11. Galatians 4:28 - "Now you, brothers, like Isaac, are children of promise"
**Challenge**: Need to find nearby "we" context
- Paul shifts between "you" and "we" throughout Galatians
- Tests Pauline ambiguity pattern (Rule 5.2)
**Why adversarial**: Paul's complex rhetorical "we/you" shifts

#### 12. James 3:1 - "Not many of you should become teachers, my brothers, for you know that we who teach will be judged with greater strictness"
**Challenge**:
- Speaker: James
- Addressee: Brothers (believers)
- "We who teach" = subset of addressees (teachers only)
- Is this EXCLUSIVE (teachers vs. non-teachers) or INCLUSIVE (if addressees include teachers)?
**Why adversarial**: Subset reference - not all addressees are teachers
**Rule conflict**: Shared group (inclusive) vs. role distinction (exclusive)

---

### Category 4: Genre Boundary Cases (3 verses)

#### 13. Ecclesiastes 4:9 - Wisdom proverb
**Text**: "Two are better than one, because they have a good reward for their toil"
**Challenge**:
- Does this contain first-person plural? (Check Hebrew)
- If so, is it generic "we" (any two people) or specific?
- Wisdom literature uses generic statements
**Why adversarial**: Generic/proverbial "we" is different from specific discourse "we"
**Note**: May not have clusivity test - verify text

#### 14. Revelation 11:8 - Apocalyptic vision
**Text**: "And their dead bodies will lie in the street of the great city...where their Lord was crucified"
**Context**: Check if there's first-person plural in this vision context
**Challenge**: Apocalyptic visions have different discourse structure
- Prophet as observer
- Heavenly voices
- Visionary "we"
**Why adversarial**: Genre shift from normal discourse patterns

#### 15. Jonah 1:14 - Sailors' prayer
**Text**: "Therefore they called out to the LORD, 'O LORD, let us not perish for this man's life'"
**Challenge**:
- Speaker: Pagan sailors
- Addressee: The LORD (YHWH)
- Action: Prayer not to perish
- "Us" = sailors (not including God who is addressed)
**Why adversarial**: Tests prayer rule (2.1) with non-Israelite speakers
**Expected**: EXCLUSIVE (prayer to God), but pagan context is unusual in training
**Rule testing**: Does prayer rule apply universally or only for believer prayers?

---

## Why These Verses Are Adversarial

### Challenges to Algorithm v1.0

1. **Rule conflicts** (5 verses): Multiple rules could apply with different results
   - Isaiah 9:6, Psalm 44:1, Jeremiah 42:20, James 3:1, Nehemiah 2:17

2. **Ambiguous participants** (4 verses): Unclear who speaker/addressee is
   - Song of Solomon 1:4, Genesis 42:21, Daniel 2:36, Galatians 4:28

3. **Rare contexts** (3 verses): Not well-represented in training
   - Royal "we" (Daniel 2:36), Apocalyptic (Revelation 11:8), Wisdom (Ecclesiastes 4:9)

4. **Genre boundaries** (3 verses): Different from training genres
   - Wisdom, Apocalyptic, Pagan prayer

5. **Theological complexity** (4 verses): Multiple valid interpretations
   - Isaiah 9:6, Numbers 23:19, 1 John 4:19, Psalm 44:1

6. **Discourse complexity** (4 verses): Multi-level or shifting discourse
   - Jeremiah 42:20, Acts 16:10, Genesis 42:21, Song of Solomon 1:4

---

## Expected Performance

### Predicted Accuracy Distribution

**High confidence predictions** (4-5 verses): 80-90% accuracy
- Clear cases even if adversarial (e.g., Jonah 1:14 - prayer rule)

**Medium confidence predictions** (5-6 verses): 50-70% accuracy
- Genuine ambiguity or rule conflicts

**Low confidence predictions** (4-5 verses): 30-50% accuracy
- Multiple valid interpretations, may mark as AMBIGUOUS

**Overall expected**: 60-70% (target adversarial range)

---

## Verses Specifically Excluded from Training

Verified these were NOT in training set:
- ✅ Isaiah 9:6 (not in clusivity analysis)
- ✅ Psalm 44:1 (different from Psalm 95:1)
- ✅ Numbers 23:19 (not analyzed)
- ✅ 1 John 4:19 (different from 1 John 1:1)
- ✅ Genesis 42:21 (not in Genesis training verses)
- ✅ Jeremiah 42:20 (no Jeremiah in training)
- ✅ Song of Solomon 1:4 (not in training)
- ✅ Acts 16:10 (different from Acts 2:32, 15:25, 17:20)
- ✅ Daniel 2:36 (not in training)
- ✅ Nehemiah 2:17 (not in training)
- ✅ Galatians 4:28 (not in training)
- ✅ James 3:1 (not in training)
- ✅ Ecclesiastes 4:9 (not in training)
- ✅ Revelation 11:8 (not in training)
- ✅ Jonah 1:14 (not in training)

---

## Testing Protocol

1. ☐ Verify no overlap with training set (20 verses)
2. ☐ Commit this test set to git BEFORE making predictions
3. ☐ Verify all verses actually contain first-person plural pronouns
4. ☐ Access TBTA data for these 15 verses
5. ☐ Apply algorithm v1.0 WITHOUT analyzing TBTA patterns
6. ☐ Rate confidence for each prediction
7. ☐ Lock predictions with git commit
8. ☐ Compare with TBTA and calculate accuracy
9. ☐ Error analysis for failures
10. ☐ Update algorithm v2.0

---

## Success Criteria

- ✅ **60-70% accuracy**: Algorithm handles edge cases reasonably well
- ⚠️ **50-60% accuracy**: Significant gaps, needs refinement
- ❌ **<50% accuracy**: Major problems with algorithm
- ⚠️ **>75% accuracy**: Test wasn't adversarial enough! Need harder cases

---

## Notes

### Verification Needed
Some verses may not contain first-person plural pronouns. Need to verify:
- Numbers 23:19 (check Hebrew)
- Ecclesiastes 4:9 (check Hebrew)
- Revelation 11:8 (check Greek)
- Galatians 4:28 context (find nearby "we")

**Action**: Before predictions, verify all 15 verses actually test clusivity

### Replacement Candidates
If any verse doesn't work, alternatives:
- Judges 11:7 (Jephthah)
- 1 Samuel 8:19 (Israel demands king)
- Ezekiel 20:32 (corporate Israel)
- Luke 1:1 (preface with "us")
- Philippians 1:3 (Paul's "we" in thanksgiving)

---

**Status**: Test set designed, ready for verification and predictions
**Next**: Verify verses, access TBTA, apply algorithm v1.0
**Date**: 2025-11-09
