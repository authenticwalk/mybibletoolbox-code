# Degree Feature: Training Set

**Purpose**: Learn TBTA's degree annotation patterns
**TBTA Access**: ALLOWED (this is training data)
**Selection date**: 2025-11-08
**Status**: LOCKED - These 8 verses are designated for training

---

## Training Philosophy

**Permission to learn**:
- These 8 verses can be analyzed WITH TBTA data
- Patterns discovered here inform algorithm v1.0
- No data leakage because test sets are separate and locked

**What to learn**:
1. How does TBTA encode synthetic morphology (comparatives, superlatives)?
2. How does TBTA handle semantic degree (positive form + superlative context)?
3. How does TBTA mark intensification (adverbs, compounds)?
4. How does TBTA distinguish downward comparison (L vs. l)?
5. How does TBTA handle Hebrew degree constructions?

---

## Training Set (8 verses)

### 1. John 15:13 - Clear Synthetic Comparative

**Reference**: John 15:13
**Greek**: μείζονα ταύτης ἀγάπην οὐδεὶς ἔχει
**English (ESV)**: "Greater love has no one than this"

**Morphology**: μείζονα (meizona) - comparative form of μέγας (megas)
**Expected pattern**: Synthetic comparative → C (Comparative)
**Learning goal**: Confirm synthetic morphology → straightforward mapping

---

### 2. Matthew 22:36 - Semantic Superlative (Context-Driven)

**Reference**: Matthew 22:36
**Greek**: Διδάσκαλε, ποία ἐντολὴ μεγάλη ἐν τῷ νόμῳ;
**English (ESV)**: "Teacher, which is the great commandment in the Law?"

**Morphology**: μεγάλη (megalē) - positive form of μέγας (megas)
**Context**: Question asks "which is GREATEST?" (superlative intent)
**Expected pattern**: Positive form + superlative context → S (Superlative) or N (No Degree)?
**Learning goal**: Understand semantic vs. morphological degree

---

### 3. Matthew 22:38 - Superlative Answer to Previous Question

**Reference**: Matthew 22:38
**Greek**: αὕτη ἐστὶν ἡ μεγάλη καὶ πρώτη ἐντολή
**English (ESV)**: "This is the great and first commandment"

**Morphology**: μεγάλη (megalē) - positive form + πρώτη (prōtē) "first" (superlative ordinal)
**Context**: Jesus answers the superlative question from v36
**Expected pattern**: Answer to superlative question → S (Superlative)?
**Learning goal**: Does TBTA encode discourse-level superlative semantics?

---

### 4. Mark 1:35 - Standard Intensifier

**Reference**: Mark 1:35
**Greek**: Καὶ πρωῒ ἔννυχα λίαν ἀναστὰς ἐξῆλθεν
**English (ESV)**: "And rising very early in the morning, while it was still dark, he departed"

**Morphology**: λίαν (lian) - standard intensifying adverb "very"
**Expected pattern**: Standard intensifier → I/V (Intensified/Very)
**Learning goal**: Confirm intensifiers get dedicated marking

---

### 5. Hebrews 7:7 - Upward vs. Downward Comparison

**Reference**: Hebrews 7:7
**Greek**: χωρὶς δὲ πάσης ἀντιλογίας τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται
**English (ESV)**: "It is beyond dispute that the inferior is blessed by the superior"

**Morphology**:
- ἔλαττον (elatton) "lesser/inferior" - comparative of ἐλαχύς (downward)
- κρείττονος (kreittonos) "better/superior" - comparative of ἀγαθός (upward)

**Expected pattern**:
- Downward comparative → L (Less) or C (Comparative)?
- Upward comparative → C (Comparative)?

**Learning goal**: Does TBTA distinguish directional comparison?

---

### 6. Song of Solomon 1:2 - Hebrew Comparative Construction

**Reference**: Song of Solomon 1:2
**Hebrew**: כִּֽי־טוֹבִים דֹּדֶיךָ מִיָּֽיִן
**English (ESV)**: "For your love is better than wine"

**Morphology**: מִן (min) construction - standard Hebrew comparative "X is better THAN Y"
**Expected pattern**: Hebrew מִן comparative → C (Comparative)
**Learning goal**: Confirm Hebrew comparative constructions map to C

---

### 7. Song of Solomon 1:8 - Hebrew Superlative (Article + Partitive)

**Reference**: Song of Solomon 1:8 (checking exact construction)
**Note**: May substitute with clearer Hebrew superlative example if needed
**Expected pattern**: Hebrew article + partitive → S (Superlative)
**Learning goal**: Understand Hebrew superlative encoding

---

### 8. Genesis 1:1 - No Degree (Baseline)

**Reference**: Genesis 1:1
**Hebrew**: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
**English (ESV)**: "In the beginning, God created the heavens and the earth"

**Morphology**: No degree marking on any constituent
**Expected pattern**: No degree morphology → N (No Degree)
**Learning goal**: Establish baseline for absence of degree

---

## Training Process

### Phase 1: TBTA Data Retrieval (ALLOWED)

For each of the 8 training verses:
1. Access TBTA database/export
2. Retrieve degree annotations for all constituents
3. Match Greek/Hebrew text to TBTA annotations
4. Document actual TBTA values

**Outcome**: `TBTA-ANNOTATIONS.md` file with all training data

---

### Phase 2: Pattern Analysis

Analyze training data to answer:

1. **Synthetic morphology**: Do comparatives/superlatives map directly?
   - Greek -τερος → C?
   - Greek -τατος → S?
   - Hebrew מִן → C?

2. **Semantic degree**: Does context override morphology?
   - Positive form + superlative question → S?
   - Or does TBTA only mark morphological degree?

3. **Intensification**: How are intensifiers marked?
   - λίαν → I or V?
   - Are there multiple intensification levels (I, V, E)?

4. **Directional comparison**: Are L/C distinguished?
   - ἔλαττον "lesser" → L (Less) or C (Comparative)?
   - κρείττονος "greater" → C?

5. **Hebrew patterns**: Do Hebrew constructions follow Greek patterns?
   - מִן comparative → same as Greek C?
   - Hebrew superlative → same as Greek S?

**Outcome**: `PATTERNS-LEARNED.md` file documenting insights

---

### Phase 3: Algorithm Development

Based on patterns, create decision rules:

```markdown
Algorithm v1.0: Degree Feature

Rule 1: Synthetic Morphology (High confidence)
[Based on training data]

Rule 2: Semantic Interpretation
[Based on training data]

Rule 3: Intensification
[Based on training data]

Rule 4: Directional Comparison
[Based on training data]

Rule 5: Hebrew Constructions
[Based on training data]

Rule 6: Default
[Based on training data]
```

**Outcome**: `ALGORITHM-v1.md` file with locked decision rules

---

## Success Criteria for Training

**Training successful if**:
- ✅ All 8 verses have TBTA annotations retrieved
- ✅ Patterns identified for all major degree categories
- ✅ Algorithm v1.0 documented with clear decision rules
- ✅ Confidence levels assigned to each rule

**Red flags**:
- ❌ TBTA data unavailable for multiple verses (need new training verses)
- ❌ No clear patterns emerge (need more training data)
- ❌ Conflicting patterns (need deeper analysis or theological context)

---

## Next Steps After Training

1. **Lock algorithm v1.0** (git commit with SHA)
2. **Apply to adversarial test set** (predict WITHOUT checking TBTA)
3. **Apply to random test set** (predict WITHOUT checking TBTA)
4. **Lock predictions** (git commit with SHA)
5. **Check TBTA for test sets** (calculate accuracy)
6. **Error analysis** (update algorithm v2.0 if needed)

---

## Files to Create

After training phase:
1. ✅ `TRAINING-SET.md` (this file)
2. ⏳ `TBTA-ANNOTATIONS.md` (TBTA data for 8 verses)
3. ⏳ `PATTERNS-LEARNED.md` (insights from analysis)
4. ⏳ `ALGORITHM-v1.md` (locked decision rules)

---

**Status**: ✅ Training set locked
**Next action**: Access TBTA for these 8 verses ONLY
**Target date**: 2025-11-09
