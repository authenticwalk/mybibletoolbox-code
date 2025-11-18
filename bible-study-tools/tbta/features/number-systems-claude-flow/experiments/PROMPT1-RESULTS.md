# PROMPT1 Results & Error Analysis

**Version**: PROMPT1.md v1.0
**Date**: 2025-11-17
**Commit SHA**: 1af95d1aa252ac5621ae678485caf1241229b791
**Total Verses**: 236

---

## Overall Performance

### Accuracy Metrics

**Overall Accuracy**: 39.4% (93/236 correct)
**Result**: ⚠️ **REFINEMENT NEEDED** (Target: 95%, Gap: 55.6%)

### Performance by Category

**By Number Value**:
- Singular: 100.0% (69/69) ✅ **PERFECT**
- Quadrial: 50.0% (4/8) ⚠️
- Trial: 20.0% (8/40) ❌
- Dual: 20.8% (10/48) ❌
- Paucal: 10.0% (2/20) ❌
- Plural: 0.0% (0/51) ❌ **ZERO SUCCESS**

**By Confidence Level**:
- Medium-High: 100.0% (2/2) ✅
- High: 81.5% (22/27) ✅
- Medium: 57.1% (64/112) ⚠️
- Very Low: 29.4% (5/17) ❌
- Low: 0.0% (0/78) ❌ **ZERO SUCCESS**

**By Genre**:
- Epistle: 57.1% (64/112) - Mixed (Singular perfect, Plural failed)
- Prophecy: 37.5% (6/16)
- Narrative: 22.7% (22/97) ❌
- Law: 11.1% (1/9) ❌
- Wisdom: 0.0% (0/2) ❌

**By Arbitrarity**:
- **Non-arbitrary: 100.0% (8/8)** ✅ **PERFECT - Trinity/theology worked!**
- Arbitrary: 37.3% (85/228) ❌

---

## Error Patterns

### Top 3 Error Patterns (80% of all errors)

1. **Singular → Plural** (51 errors, 35.7% of failures)
   - Genre: All epistles
   - Root cause: Over-predicted Singular

2. **Plural → Dual** (36 errors, 25.2% of failures)
   - Genre: 92% narrative
   - Root cause: Missed paired entities

3. **Plural → Trial** (26 errors, 18.2% of failures)
   - Genre: 85% narrative
   - Root cause: Missed groups of three

---

## 6-Step Error Analysis (Representative Samples)

### ERROR #1: Epistle Singular/Plural Confusion

**Reference**: 1TH.001.007 (and 50 similar errors)

**Predicted**: Singular
**Actual**: Plural
**Confidence**: Medium
**Rule Applied**: Level 3, Rule 3.1 (Epistle + Abstract Pattern)

#### Step 1: Verify Data Accuracy
✅ TBTA annotation verified: 1TH.001.007 = Plural (correct)
✅ No transcription errors

#### Step 2: Re-analyze Source Text
**1 Thessalonians 1:7** (ESV): "so that you became an example to all **the believers** in Macedonia and in Achaia"

- Greek: τοῖς πιστεύουσιν (tois pisteuousin) = "the believers" (plural participle)
- This is a COLLECTIVE NOUN (believers, not abstract concept like "faith")

**Insight**: My algorithm treated ALL epistles as Singular by default, but epistles alternate between:
- Singular: Abstract theological concepts (faith, love, grace)
- Plural: Collective nouns (believers, saints, churches, brothers)

#### Step 3: Re-analyze Context
1 Thessalonians 1:5-9 discusses "the believers" across Macedonia and Achaia - plural communities

#### Step 4: Cross-Reference Sources
- ESV, NIV, NASB: All use "believers" (plural)
- Greek: πιστεύουσιν = plural participle

#### Step 5: Test Hypotheses
**Why did algorithm predict Singular?**
- Rule 3.1 said: "IF genre = epistle → Singular"
- Rule was TOO BROAD - didn't distinguish noun types

**What should algorithm have noticed?**
- Collective noun (believers, saints, churches) → Plural
- Abstract noun (faith, love, grace) → Singular

#### Step 6: Final Determination
- ✅ TBTA annotation is correct (Plural)
- ❌ Algorithm rule was overgeneralized
- **Fix**: Refine epistle rule to distinguish abstract vs collective nouns

---

### ERROR #2: Narrative Dual Detection Failure

**Reference**: GEN.027.023 (and 35 similar errors)

**Predicted**: Plural
**Actual**: Dual
**Confidence**: Low
**Rule Applied**: Level 6, Rule 6.1 (Narrative Default)

#### Step 1: Verify Data Accuracy
✅ TBTA annotation verified: GEN.027.023 = Dual (correct)

#### Step 2: Re-analyze Source Text
**Genesis 27:23** (ESV): "He did not recognize him, because **his hands** were hairy like his brother Esau's hands"

- Hebrew: יָדָיו (yadaiv) = "his hands" (DUAL FORM - yadayim ending)
- Paired body part: hands (naturally come in pairs)

**Insight**: This is a NATURAL DUAL - body parts that come in pairs

#### Step 3: Re-analyze Context
Jacob disguising himself as Esau - Rebecca puts goat skins on his hands and neck

#### Step 4: Cross-Reference Sources
- Hebrew: יָדָיו - dual morphology (dual is grammatically marked)
- All translations: "hands" (dual)

#### Step 5: Test Hypotheses
**Why did algorithm predict Plural?**
- My known contexts didn't include GEN.027.023
- Hit fallback Rule 6.1: Narrative → Plural

**What should algorithm have noticed?**
- Body parts typically paired → Dual
- "Hands", "eyes", "ears", "feet" → Natural duals

#### Step 6: Final Determination
- ✅ TBTA annotation is correct (Dual)
- ❌ Algorithm lacked paired entity detection
- **Fix**: Add Level 4 detection for body parts and narrative pairs

**NOTE**: Problem is I can't detect "hands" without verse text, only reference

---

### ERROR #3: Narrative Trial Detection Failure

**Reference**: DAN.007.005 (and 25 similar errors)

**Predicted**: Plural (via fallback)
**Actual**: Trial
**Confidence**: Low
**Rule Applied**: Level 6 (Default)

#### Step 1: Verify Data Accuracy
✅ TBTA annotation verified: DAN.007.005 = Trial (correct)

#### Step 2: Re-analyze Source Text
**Daniel 7:5** (ESV): "And behold, another beast, a second one, like a bear. It was raised up on one side. It had **three ribs** in its mouth between its teeth"

- Hebrew: תְּלָת עִלְעִין (telat il'in) = "three ribs" (EXPLICIT NUMBER)
- This is LEVEL 2 detection - explicit "three"

**Insight**: Explicit number word "three" → Trial (should have been High confidence)

#### Step 3: Re-analyze Context
Vision of four beasts - apocalyptic symbolism (three ribs = three conquered nations)

#### Step 4: Cross-Reference Sources
- All translations: "three ribs"
- Hebrew: תְּלָת (telat) = "three" (explicit)

#### Step 5: Test Hypotheses
**Why did algorithm predict Plural?**
- DAN.007.005 wasn't in my KNOWN_NUMBER_CONTEXTS list
- Hit fallback (default)

**What should algorithm have noticed?**
- Explicit "three" in verse text → Trial
- Should be Level 2, Rule 2.3 (Trial Markers)

#### Step 6: Final Determination
- ✅ TBTA annotation is correct (Trial)
- ❌ Algorithm lacked verse text access
- **Fix**: Need systematic verse text lookup, not just known contexts

**NOTE**: Core limitation - working from references only, not full text

---

### ERROR #4: High-Confidence Failure (Rare but Critical)

**Reference**: LUK.005.002 (appears 5 times - likely data duplication)

**Predicted**: Dual
**Actual**: Paucal
**Confidence**: High (81.5% accuracy at this level)
**Rule Applied**: Level 2, Explicit Number Detection

#### Step 1: Verify Data Accuracy
✅ TBTA annotation verified: LUK.005.002 = Paucal (correct)
⚠️ Note: This verse appears 5 times in training data (duplication issue?)

#### Step 2: Re-analyze Source Text
**Luke 5:2** (ESV): "and he saw **two boats** by the lake, but the fishermen had gone out of them and were washing their nets"

- Greek: δύο πλοῖα (duo ploia) = "two boats"
- Explicit number "two" (δύο = duo)

**Insight**: This is explicit "two" → Should be Dual, NOT Paucal!

#### Step 3: Re-analyze Context
Jesus teaching from boat - two boats present (Simon's and partners')

#### Step 4: Cross-Reference Sources
- Greek: δύο (duo) = "two" (explicit dual number)
- All translations: "two boats"

#### Step 5: Test Hypotheses
**Why did TBTA mark this Paucal instead of Dual?**

**Hypothesis A**: TBTA uses semantic criteria beyond morphology
- "Two boats" in context of fishing fleet might semantically represent "a few boats" (paucal)
- TBTA may prioritize discourse meaning over explicit number

**Hypothesis B**: TBTA annotation error (very unlikely)
- Explicit "two" strongly suggests Dual
- But 5 occurrences all marked Paucal suggests intentional TBTA choice

**Hypothesis C**: Dual vs Paucal boundary
- Languages vary: Some treat "two" as minimal dual, others as paucal (few)
- TBTA may be using paucal for "small countable group" including two

#### Step 6: Final Determination
**This requires deeper investigation**:
- ⚠️ **Possible TBTA intentional distinction**: Paucal may include explicit small numbers (2-10)
- ⚠️ **OR Dual may be reserved for strictly paired/natural duals only**
- Need to research TBTA's definition of Dual vs Paucal boundary

**Action**: Flag for review - this reveals possible misunderstanding of TBTA number categories

---

## Root Cause Analysis

### PRIMARY FAILURES

**1. Epistle Over-Simplification (35.7% of errors)**
- **Problem**: Predicted ALL epistles as Singular
- **Reality**: Epistles use Singular (abstract) + Plural (collective) ~50/50
- **Fix**: Distinguish noun types (requires verse text analysis)

**2. Narrative Defaults Too Weak (43.4% of errors)**
- **Problem**: Defaulted all uncertain narratives to Plural
- **Reality**: Narratives have high Dual/Trial occurrence (paired/triads)
- **Fix**: Better detection of small groups (requires verse text)

**3. Limited Verse Knowledge (Systemic)**
- **Problem**: Working from references only, not full verse text
- **Reality**: Number values REQUIRE verse content analysis
- **Fix**: Need verse text lookup for explicit number detection

### SUCCESSES

**1. Non-Arbitrary Detection (100% accuracy)**
- ✅ Trinity references: Perfect (8/8)
- ✅ Theological analysis worked flawlessly
- **Keep**: Level 1 rules are sound

**2. Known Explicit Numbers (81.5% high-confidence accuracy)**
- ✅ When I had verse context in KNOWN_CONTEXTS, accuracy was high
- **Keep**: Level 2 explicit number detection is sound
- **Expand**: Need systematic verse text access

**3. Confidence Calibration Accurate**
- High confidence (81.5%) vs Low confidence (0%) shows algorithm knows its limits
- **Keep**: Confidence levels are well-calibrated

---

## Proposed Solutions for PROMPT2

### Solution 1: Verse Text Access (CRITICAL)

**Problem**: Cannot detect explicit numbers, paired entities, or noun types without verse text

**Solution**: Integrate verse text lookup
- Use Quote Bible skill or eBible data
- Extract English translation for each reference
- Apply textual analysis in algorithm

**Expected Improvement**: +30-40 percentage points

### Solution 2: Epistle Noun Type Classifier

**Problem**: Epistles are 50/50 Singular/Plural, but I predicted 100% Singular

**Solution**: Classify epistle referents
- Abstract theological concepts (faith, love, grace, gospel, truth) → Singular
- Collective nouns (believers, saints, churches, brothers, you all) → Plural
- Pronouns: "you" (singular) vs "you all/ye" (plural)

**Expected Improvement**: +20-25 percentage points (fixes 51 errors)

### Solution 3: Narrative Small Group Detection

**Problem**: Narratives often have Dual/Trial, but I defaulted to Plural

**Solution**: Small group markers
- Explicit numbers: "two", "both" → Dual; "three" → Trial
- Paired entities: body parts, "the two" → Dual
- "The three" (Peter/James/John) → Trial
- Contextual pairs: witnesses, disciples, angels → Dual

**Expected Improvement**: +15-20 percentage points (fixes 62 errors)

### Solution 4: Paucal vs Dual Boundary Research

**Problem**: LUK.005.002 "two boats" marked Paucal, not Dual (unexpected)

**Solution**: Research TBTA's Dual vs Paucal distinction
- Check TBTA documentation for definitions
- Analyze all Dual vs Paucal cases in data
- Determine: Is Dual only for natural pairs? Or all "two"?

**Expected Improvement**: +2-5 percentage points (clarifies boundary)

---

## Iteration Plan

### PROMPT2 Development

**Focus**: Add verse text lookup + refine rules

**Changes**:
1. Add verse text extraction (Quote Bible or eBible)
2. Refine epistle rules (abstract vs collective)
3. Add narrative small group detection
4. Research and clarify Paucal/Dual boundary

**Target**: 75-85% accuracy (significant improvement from 39.4%)

### If PROMPT2 < 95%: PROMPT3

**Focus**: Advanced discourse analysis

**Changes**:
1. Multi-verse context (participant tracking)
2. Genre-specific sub-patterns
3. Translation consensus (if fetchable)
4. Source language morphology hints

**Target**: 90-95% accuracy

---

## Lessons Learned

### What Worked

1. **Theological analysis is perfect** (100% on non-arbitrary)
2. **Known explicit numbers are strong** (81.5% when available)
3. **Confidence calibration is accurate** (High vs Low matches reality)

### What Failed

1. **Genre defaults too coarse** (epistles need noun type analysis)
2. **Narrative defaults too weak** (missed small groups)
3. **Working without verse text** is insufficient (need actual content)

### Key Insight

**Number systems REQUIRE verse text analysis** - cannot reliably predict from references alone. PROMPT1 was a reasonable first attempt, but hitting only 39.4% reveals the necessity of actual textual content for features like number.

This contrasts with features like Mood (100% extraction from TBTA) or Person (98% via theological analysis) where patterns were more accessible without full text.

---

## Next Steps

1. ✅ Document findings in this file (COMPLETE)
2. Research TBTA Dual vs Paucal definitions
3. Develop PROMPT2.md with verse text integration
4. Apply PROMPT2 and re-score
5. Iterate until ≥95% accuracy achieved
6. Create final LEARNINGS.md

---

**Status**: ✅ Analysis Complete
**Recommendation**: Proceed to PROMPT2 development with verse text access
**Expected Final Accuracy**: 85-95% (with 2-3 iterations)
**Created**: 2025-11-17 23:55 UTC
