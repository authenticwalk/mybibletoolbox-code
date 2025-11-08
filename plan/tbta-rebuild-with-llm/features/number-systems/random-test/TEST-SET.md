# Number Systems: Random Test Set

**Purpose**: Test algorithm v1.0 on typical cases
**Expected accuracy**: 80-90% (random typical cases should be easier than adversarial)
**Selection date**: 2025-11-08
**Random seed**: 42
**Status**: LOCKED - Do not modify after predictions begin

---

## Test Set Overview

**Total verses**: 10
**Selection method**: Random selection from diverse books, stratified by number value
**Training overlap**: None (all verses excluded from training set)
**Adversarial overlap**: None (all verses excluded from adversarial test set)

---

## Selection Strategy

**Books prioritized**: Less-represented books in training
- Training was heavy on: Genesis 1, Matthew 5/22, John 3/14/17
- Random test focuses on: Romans, Ephesians, Mark, Luke, Psalms, Exodus

**Stratification by number value** (target distribution):
- Singular: 5 verses (50%) - most common
- Plural: 3 verses (30%) - common
- Dual: 1 verse (10%) - less common
- Trial: 1 verse (10%) - rare

**Typical cases** (avoid adversarial characteristics):
- Clear morphological marking
- No theological complexity
- No collective nouns
- No fossilized duals
- Standard discourse contexts

---

## Random Test Verses

### Category: Singular (5 verses)

#### 1. Romans 1:16 - "the gospel"

**Reference**: Romans 1:16
**Greek**: Οὐ γὰρ ἐπαισχύνομαι τὸ εὐαγγέλιον
**English (ESV)**: "For I am not ashamed of the gospel"

**Rationale**:
- τὸ εὐαγγέλιον (to euangelion) - neuter singular noun
- Clear morphology: τὸ (singular article) + singular noun
- Semantic: one gospel
- Typical case: morphology matches semantics

**Expected**: Singular
**Confidence**: High

---

#### 2. Mark 2:5 - "your sins"

**Reference**: Mark 2:5
**Greek**: καὶ ἰδὼν ὁ Ἰησοῦς τὴν πίστιν αὐτῶν λέγει τῷ παραλυτικῷ· Τέκνον, ἀφίενταί σου αἱ ἁμαρτίαι
**English (ESV)**: "And when Jesus saw their faith, he said to the paralytic, 'Son, your sins are forgiven'"

**Rationale**:
- Focus on "Son" (Τέκνον, teknon) - neuter singular vocative
- Clear morphology: singular noun
- Semantic: one person addressed
- Typical case: straightforward singular address

**Expected**: Singular (for "Son")
**Confidence**: High

---

#### 3. Psalm 23:1 - "The LORD is my shepherd"

**Reference**: Psalm 23:1
**Hebrew**: יְהוָה רֹעִי
**English (ESV)**: "The LORD is my shepherd"

**Rationale**:
- יְהוָה (YHWH) - proper name, singular
- רֹעִי (roi) "my shepherd" - singular with first person singular suffix
- Semantic: one God, one shepherd
- Typical case: clear singular morphology

**Expected**: Singular (both "LORD" and "shepherd")
**Confidence**: High

---

#### 4. Luke 15:11 - "A man had two sons"

**Reference**: Luke 15:11
**Greek**: Ἄνθρωπός τις εἶχεν δύο υἱούς
**English (ESV)**: "There was a man who had two sons"

**Rationale**:
- Focus on "man" (Ἄνθρωπός, anthropos) - masculine singular
- Clear morphology: singular nominative
- Semantic: one man
- Typical case: straightforward singular subject

**Expected**: Singular (for "man")
**Confidence**: High

---

#### 5. Exodus 3:4 - "God called to him"

**Reference**: Exodus 3:4
**Hebrew**: וַיִּקְרָא אֵלָיו אֱלֹהִים
**English (ESV)**: "God called to him out of the bush"

**Rationale**:
- אֱלֹהִים (Elohim) - morphologically plural but semantically singular when referring to the one God
- Standard pattern: Elohim + singular verb = Singular
- Typical case: common pattern in Hebrew Bible

**Expected**: Singular
**Confidence**: High

---

### Category: Plural (3 verses)

#### 6. Ephesians 6:1 - "Children, obey your parents"

**Reference**: Ephesians 6:1
**Greek**: Τὰ τέκνα, ὑπακούετε τοῖς γονεῦσιν ὑμῶν
**English (ESV)**: "Children, obey your parents in the Lord"

**Rationale**:
- Τὰ τέκνα (ta tekna) - neuter plural vocative
- τοῖς γονεῦσιν (tois goneusin) - plural dative "parents"
- Clear morphology: plural articles and nouns
- Semantic: multiple children, multiple parents (two)
- Typical case: standard plural

**Expected**: Plural (both "children" and "parents")
**Confidence**: High

---

#### 7. Acts 2:37 - "they were cut to the heart"

**Reference**: Acts 2:37
**Greek**: Ἀκούσαντες δὲ κατενύγησαν τὴν καρδίαν
**English (ESV)**: "Now when they heard this they were cut to the heart"

**Rationale**:
- Implied subject "they" - plural (the crowd)
- κατενύγησαν (katenugēsan) - aorist passive plural
- Context: Peter addressing the crowd (many people)
- Typical case: plural subject with plural verb

**Expected**: Plural (for the implied "they")
**Confidence**: High

---

#### 8. Psalm 103:20 - "you his angels"

**Reference**: Psalm 103:20
**Hebrew**: בָּרְכוּ יְהוָה מַלְאָכָיו
**English (ESV)**: "Bless the LORD, O you his angels"

**Rationale**:
- מַלְאָכָיו (mal'akhav) "his angels" - plural with third person singular suffix
- בָּרְכוּ (barkhu) - plural imperative
- Semantic: multiple angels
- Typical case: straightforward plural

**Expected**: Plural
**Confidence**: High

---

### Category: Dual (1 verse)

#### 9. Exodus 21:18 - "two men quarrel"

**Reference**: Exodus 21:18
**Hebrew**: וְכִי־יְרִיבֻן אֲנָשִׁים
**English (ESV)**: "When men quarrel"

**Rationale**:
- Context suggests two men (legal case requires two parties)
- אֲנָשִׁים (anashim) - plural form, but context = exactly two
- Semantic: dyadic conflict (requires two parties)
- Test: Does TBTA mark contextual dual or just plural?

**Expected**: Dual or Plural (uncertain - depends on TBTA policy)
**Confidence**: Medium

---

### Category: Trial (1 verse)

#### 10. Genesis 18:2 - "three men"

**Reference**: Genesis 18:2
**Hebrew**: וַיִּשָּׂא עֵינָיו וַיַּרְא וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים
**English (ESV)**: "He lifted up his eyes and looked, and behold, three men were standing in front of him"

**Rationale**:
- שְׁלֹשָׁה אֲנָשִׁים (shloshah anashim) "three men" - explicitly three
- Semantic: exactly three entities
- Theological: Often interpreted as divine visitation (Trinity or YHWH + 2 angels)
- Test: Does TBTA mark explicit "three" as Trial?

**Expected**: Trial (if TBTA uses trial for explicit threesomes)
**Confidence**: Medium-Low (uncertain if trial is only for implicit or also explicit)

---

## Exclusions Confirmed

**Not in training set** (35 verses from experiment-001):
- None of these 10 verses overlap with training

**Not in adversarial set** (10 verses):
- None of these 10 verses overlap with adversarial test

**Total unique verses**: 55 (35 training + 10 adversarial + 10 random)

---

## Expected Performance

**Target accuracy**: 80-90% (8-9 correct out of 10)

**High confidence predictions** (7 verses):
- Romans 1:16, Mark 2:5, Psalm 23:1, Luke 15:11, Exodus 3:4 (Singular)
- Ephesians 6:1, Acts 2:37 (Plural)

**Medium confidence predictions** (2 verses):
- Psalm 103:20 (Plural angels - should be straightforward)
- Exodus 21:18 (Dual vs. Plural - context-dependent)

**Low confidence predictions** (1 verse):
- Genesis 18:2 (Trial vs. Plural - tests trial boundary)

**Likely error candidates**:
1. Exodus 21:18 - May mark Plural instead of Dual
2. Genesis 18:2 - May mark Plural instead of Trial

If algorithm gets 8-9/10 = 80-90% ✅ SUCCESS

---

## Comparison with Adversarial Set

**Design philosophy**:
- **Adversarial**: Edge cases, theological complexity, morphological exceptions, ambiguity
- **Random**: Typical cases, clear morphology, standard contexts, representative distribution

**Expected gap**: Random should beat adversarial by 15-25 points
- Adversarial: 60-70% (6-7 correct)
- Random: 80-90% (8-9 correct)
- Gap: 15-25 points ✅

If random ≤ adversarial, test sets poorly designed ❌

---

## Prediction Protocol

**Step 1**: Apply algorithm v1.0 to each verse WITHOUT checking TBTA
**Step 2**: Document reasoning for each prediction
**Step 3**: Rate confidence (High/Medium/Low)
**Step 4**: Commit predictions to git with timestamp
**Step 5**: LOCK predictions (no modifications after commit)
**Step 6**: Check TBTA and calculate accuracy
**Step 7**: Compare with adversarial accuracy

---

## Files to Create Next

After locking this test set:
1. `PREDICTIONS-locked.md` - Predictions before checking TBTA (with commit SHA)
2. `RESULTS.md` - Accuracy after checking TBTA

---

## Random Seed Documentation

**Seed**: 42
**Selection process**:
1. Listed all books in Bible
2. Excluded heavily-used books in training (Genesis 1, Matthew 5/22, John 3/14/17)
3. Used random seed 42 to select diverse books
4. From each book, selected verses with clear number marking
5. Stratified by expected number value distribution

**Reproducibility**: Using seed 42, this exact set can be regenerated

---

**Status**: ✅ Test set designed and locked
**Next step**: Make predictions using algorithm v1.0 (after adversarial predictions)
**Target date**: 2025-11-10
