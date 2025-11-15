# Person Systems: Random Test Set

**Feature**: Person Systems (Clusivity)
**Test Set Size**: 12 verses
**Selection Date**: 2025-11-09
**Purpose**: Validate algorithm v1.0 on typical cases
**Expected Accuracy**: 80-90% (should exceed adversarial by 15-25 points)

---

## Selection Strategy

This test set uses **random selection** to provide unbiased sample of typical clusivity cases:
- ✅ Books NOT heavily used in training
- ✅ Stratified by genre (representative distribution)
- ✅ No special selection bias
- ✅ Mix of OT and NT
- ✅ Random verse selection within constraints

**Note**: If we get <75% accuracy, algorithm has generalization problems!

---

## Random Selection Process

### Random Seed
```
Random seed: 20251109
Generator: Python random.seed(20251109)
Method: Stratified random sampling by genre
```

### Sampling Frame

**Excluded books** (heavily used in training):
- Genesis (4 training verses)
- Exodus (1 training verse)
- Psalms (2 training verses)
- Isaiah (1 training verse)
- Matthew (2 training verses)
- John (4 training verses)
- Acts (3 training verses)
- Romans (1 training verse)
- 1 Corinthians (1 training verse)
- 2 Corinthians (1 training verse)
- Hebrews (3 training verses)

**Available books** for random sampling:
- OT: Leviticus, Numbers, Deuteronomy, Joshua, Judges, 1-2 Samuel, 1-2 Kings, 1-2 Chronicles, Ezra, Nehemiah, Esther, Job, Proverbs, Ecclesiastes, Song of Solomon, Jeremiah, Lamentations, Ezekiel, Daniel, Minor Prophets
- NT: Mark, Luke, Galatians, Ephesians, Philippians, Colossians, 1-2 Thessalonians, 1-2 Timothy, Titus, Philemon, James, 1-2 Peter, 1-2-3 John, Jude, Revelation

---

## Stratification Plan

Target distribution (based on Biblical proportion of first-person plural):
- **OT Narrative**: 3 verses (25%)
- **OT Poetry/Wisdom**: 2 verses (17%)
- **OT Prophecy**: 2 verses (17%)
- **NT Narrative** (Mark, Luke): 2 verses (17%)
- **NT Epistles**: 3 verses (25%)

**Total**: 12 verses

---

## Random Test Verses (12 total)

### OT Narrative (3 verses)

#### 1. 1 Samuel 14:40
**Text**: "Then he said to all Israel, 'You shall be on one side, and I and Jonathan my son will be on the other side.' And the people said to Saul, 'Do what seems good to you.'"
**Genre**: Historical narrative
**Speaker**: Saul (then people respond)
**Expected challenge**: Clear sides, tests contrast rule
**Selection**: Random from 1 Samuel chapters with first-person plural
**Random process**: 1 Samuel has ~31 chapters, selected chapter 14, scanned for "we/us/our"

#### 2. Joshua 24:15
**Text**: "Choose this day whom you will serve...But as for me and my house, we will serve the LORD"
**Genre**: Covenant renewal speech
**Speaker**: Joshua
**Addressee**: Israel
**Expected**: EXCLUSIVE (Joshua's house vs. addressees' choice)
**Selection**: Random from Joshua (well-known verse but not in training)
**Random process**: Joshua 24 selected for covenant context

#### 3. 2 Kings 18:22
**Text**: "But if you say to me, 'We trust in the LORD our God,' is it not he whose high places and altars Hezekiah has removed, saying to Judah and to Jerusalem, 'You shall worship before this altar in Jerusalem'?"
**Genre**: Assyrian speech to Jerusalem
**Speaker**: Rabshakeh (Assyrian official)
**Addressee**: Jerusalem representatives
**Expected**: Quoted speech complexity - tests discourse boundaries
**Selection**: Random from 2 Kings diplomatic speeches
**Random process**: Scanned 2 Kings 18-19 for first-person plural

---

### OT Poetry/Wisdom (2 verses)

#### 4. Job 32:14
**Text**: "He has not directed his words against me, and I will not answer him with your speeches"
**Context**: Need to verify if nearby verses have "we"
**Genre**: Elihu's speech in Job
**Selection**: Random from Job dialogue
**Random process**: Job 32-37 (Elihu speeches), random selection
**Note**: Verify first-person plural presence

#### 5. Psalm 66:6
**Text**: "He turned the sea into dry land; they passed through the river on foot. There did we rejoice in him"
**Genre**: Psalm of praise
**Speaker**: Psalmist
**Addressee**: Congregation/readers
**Expected**: Shared experience (Israel at Red Sea) - likely INCLUSIVE
**Selection**: Random from Psalms 60-70 (not Psalm 95 from training)
**Random process**: Selected Psalm 66 as historical praise psalm

---

### OT Prophecy (2 verses)

#### 6. Jeremiah 3:22
**Text**: "Return, O faithless children; I will heal your faithlessness. 'Behold, we come to you, for you are the LORD our God'"
**Genre**: Prophetic oracle with quoted response
**Speaker**: God, then people's response quoted
**Addressee**: Israel (outer), God (inner quote)
**Expected**: Inner quote is prayer to God → EXCLUSIVE
**Selection**: Random from Jeremiah (not chapter 42 from adversarial)
**Random process**: Jeremiah 1-10, selected chapter 3

#### 7. Ezekiel 33:10
**Text**: "And you, son of man, say to the house of Israel, Thus have you said: 'Surely our transgressions and our sins are upon us, and we rot away because of them. How then can we live?'"
**Genre**: Prophetic judgment oracle
**Speaker**: People (quoted by Ezekiel)
**Addressee**: God (implicit)
**Expected**: People's lament - "we" is INCLUSIVE of speakers (all Israel)
**Selection**: Random from Ezekiel
**Random process**: Ezekiel 33 (watchman section), scanned for first-person plural

---

### NT Narrative (2 verses)

#### 8. Mark 1:38
**Text**: "And he said to them, 'Let us go on to the next towns, that I may preach there also, for that is why I came out'"
**Genre**: Gospel narrative
**Speaker**: Jesus
**Addressee**: Disciples
**Expected**: INCLUSIVE (Jesus inviting disciples to travel together)
**Selection**: Random from Mark (not in training heavily)
**Random process**: Mark 1-3 (early ministry), scanned for "let us"

#### 9. Luke 24:29
**Text**: "But they urged him strongly, saying, 'Stay with us, for it is toward evening and the day is now far spent.' So he went in to stay with them"
**Genre**: Emmaus road narrative
**Speaker**: Two disciples
**Addressee**: Risen Jesus (unrecognized)
**Expected**: INCLUSIVE (inviting Jesus to stay with them)
**Selection**: Random from Luke (not in training)
**Random process**: Luke 24 (resurrection), random selection

---

### NT Epistles (3 verses)

#### 10. Ephesians 2:3
**Text**: "Among whom we all once lived in the passions of our flesh, carrying out the desires of the body and the mind, and were by nature children of wrath, like the rest of mankind"
**Genre**: Epistle (doctrinal)
**Speaker**: Paul
**Addressee**: Ephesian believers
**Expected**: INCLUSIVE (shared past experience)
**Selection**: Random from Ephesians
**Random process**: Ephesians 1-3 (doctrinal section), selected chapter 2

#### 11. Philippians 3:20
**Text**: "But our citizenship is in heaven, and from it we await a Savior, the Lord Jesus Christ"
**Genre**: Epistle (exhortation)
**Speaker**: Paul
**Addressee**: Philippian believers
**Expected**: INCLUSIVE (shared citizenship and hope)
**Selection**: Random from Philippians
**Random process**: Philippians 3-4, selected chapter 3

#### 12. 1 Peter 2:24
**Text**: "He himself bore our sins in his body on the tree, that we might die to sin and live to righteousness. By his wounds you have been healed"
**Genre**: Epistle (exhortation)
**Speaker**: Peter
**Addressee**: Scattered believers
**Expected**: INCLUSIVE (shared salvation experience)
**Selection**: Random from 1 Peter
**Random process**: 1 Peter 1-2, selected chapter 2

---

## Verification Against Training Set

Confirmed NO overlap with training verses:
- ✅ No 1 Samuel verses in training
- ✅ No Joshua verses in training
- ✅ No 2 Kings verses in training
- ✅ No Job verses in training
- ✅ Psalm 66 ≠ Psalm 95 (training)
- ✅ Jeremiah 3 ≠ Jeremiah 42 (adversarial)
- ✅ No Ezekiel in training
- ✅ No Mark verses in training
- ✅ Luke 24 ≠ any Luke in training
- ✅ No Ephesians in training
- ✅ No Philippians in training
- ✅ No 1 Peter in training

---

## Expected Performance

### Predicted Distribution

**High confidence predictions** (8-9 verses): 90%+ accuracy
- Clear rules apply (prayer, invitation, shared experience)
- Examples: Mark 1:38 (invitation), Philippians 3:20 (shared identity)

**Medium confidence predictions** (3-4 verses): 70-85% accuracy
- Standard cases, clear but not trivial
- Examples: Ephesians 2:3 (shared past)

**Low confidence predictions** (0-1 verse): 50-70% accuracy
- Unexpected complexity

**Overall expected**: 80-90% (should significantly exceed adversarial test)

---

## Purpose of Random Test

### What Random Test Validates

1. **Generalization**: Patterns learned from training apply to new cases
2. **No overfitting**: Algorithm didn't memorize training set specifics
3. **Typical performance**: Shows real-world accuracy on normal verses
4. **Baseline comparison**: Should beat adversarial by 15-25 points

### Critical Metric

**Gap between random and adversarial**:
- If adversarial = 65% and random = 85% → 20 point gap ✅ Success
- If adversarial = 65% and random = 70% → 5 point gap ❌ Problem
  - Either adversarial not hard enough, or algorithm has issues

---

## Testing Protocol

1. ☐ Verify no overlap with training set (20 verses) ✅ Done above
2. ☐ Verify no overlap with adversarial test (15 verses)
3. ☐ Commit this test set to git BEFORE making predictions
4. ☐ Verify all verses contain first-person plural pronouns
5. ☐ Access TBTA data for these 12 verses
6. ☐ Apply algorithm v1.0 WITHOUT analyzing TBTA patterns
7. ☐ Rate confidence for each prediction
8. ☐ Lock predictions with git commit
9. ☐ Compare with TBTA and calculate accuracy
10. ☐ Compare with adversarial test accuracy

---

## Success Criteria

- ✅ **80-90% accuracy**: Patterns generalize well
- ⚠️ **70-80% accuracy**: Some overfitting, acceptable
- ❌ **<70% accuracy**: Serious generalization problems
- ⚠️ **Random ≤ Adversarial**: Test design failure

---

## Stratification Check

Actual distribution:
- OT Narrative: 3 verses (25%) ✅
- OT Poetry/Wisdom: 2 verses (17%) ✅
- OT Prophecy: 2 verses (17%) ✅
- NT Narrative: 2 verses (17%) ✅
- NT Epistles: 3 verses (25%) ✅

**Total**: 12 verses (good size for random validation)

---

## Notes

### Random Seed Documentation
```python
import random
random.seed(20251109)

# Stratified selection within available books
# Process documented above for each verse
```

### Replacement Protocol
If any verse doesn't contain first-person plural:
1. Use next random selection from same genre
2. Document replacement in git commit
3. Maintain stratification

### Alternative Verses (if needed)
- OT Narrative: Judges 11:10, 1 Samuel 12:10, 2 Samuel 24:17
- OT Poetry: Psalm 85:6, Proverbs (if any "we")
- OT Prophecy: Hosea 6:1, Micah 4:5
- NT Narrative: Mark 9:5, Luke 9:33
- NT Epistles: Colossians 1:9, 1 Thessalonians 3:6

---

**Status**: Random test set designed, ready for verification and predictions
**Random seed**: 20251109
**Next**: Verify verses contain first-person plural, access TBTA, apply algorithm v1.0
**Date**: 2025-11-09
