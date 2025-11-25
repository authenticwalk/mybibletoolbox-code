# Degree Feature: Adversarial Test Set (REDESIGNED)

**Purpose**: Test algorithm v1.0 with equal coverage of all degree values
**Design principle**: One example per value (11 values), harder ambiguous cases
**Expected accuracy**: 50-60% (challenging cases with potential disagreement)
**Selection date**: 2025-11-08 (REVISED)
**TBTA Access**: FORBIDDEN until predictions locked
**Status**: LOCKED

---

## Design Philosophy Change

**Original design flaw**: Unbalanced (focused on comparative/intensified, missing many values)

**New design**: Equal coverage (1 example per value × 11 values = 11 verses)
- Benefit: Tests algorithm's ability to distinguish ALL degree values
- Requirement: Each value must be tested with ambiguous/hard cases
- Focus: Boundary cases where degree assignment is debatable

---

## Test Set Overview

**Total verses**: 11
**Distribution**: 1 example per degree value
**Selection criteria**: Boundary ambiguities, form-function mismatches, rare values
**Training overlap**: None

---

## Value 1: N (No Degree) - 1 verse

Hard case where base form might be confused with intensification

### 1. John 1:1 - "The Word Was God" (Predicate Nominative)

**Reference**: John 1:1
**Greek**: καὶ θεὸς ἦν ὁ λόγος
**English (ESV)**: "And the Word was God"

**Challenge**:
- θεὸς (theos) "God" - anarthrous predicate nominative
- No explicit degree marking
- But context emphasizes divine nature (could be seen as intensified/superlative)
- Does TBTA mark theological emphasis or just grammatical form?

**Why ambiguous**: Theological weight vs. grammatical form (no degree)
**Expected answer**: N (No Degree)
**Alternative**: S or I (if theological emphasis encoded)
**Confidence**: Medium

---

## Value 2: C (Comparative) - 1 verse

Hard case where comparative might be confused with superlative context

### 2. Matthew 11:11 - "No One Greater Than John"

**Reference**: Matthew 11:11
**Greek**: οὐκ ἐγήγερται ἐν γεννητοῖς γυναικῶν μείζων Ἰωάννου τοῦ βαπτιστοῦ
**English (ESV)**: "Among those born of women there has arisen no one greater than John the Baptist"

**Challenge**:
- μείζων (meizōn) - comparative form "greater"
- Context: "no one greater" = superlative meaning (John is greatest)
- Morphology (comparative) vs. semantics (superlative)
- Does TBTA follow form or function?

**Why ambiguous**: Comparative form with superlative semantic meaning
**Expected answer**: C (Comparative - morphological)
**Alternative**: S (Superlative - semantic)
**Confidence**: Low

---

## Value 3: S (Superlative) - 1 verse

Hard case where positive form is used in superlative context

### 3. Matthew 22:36 - "Which Is the Greatest Commandment?"

**Reference**: Matthew 22:36
**Greek**: ποία ἐντολὴ μεγάλη ἐν τῷ νόμῳ;
**English (ESV)**: "Teacher, which is the great commandment in the Law?"

**Challenge**:
- μεγάλη (megalē) - positive form "great" (not superlative μεγίστη)
- Question asks "which is greatest?" (superlative intent)
- Greek uses positive form where English expects superlative
- Does TBTA encode question semantics or Greek morphology?

**Why ambiguous**: Positive form in superlative question context
**Expected answer**: S (Superlative - semantic) or N (No Degree - morphological)
**Confidence**: Low

---

## Value 4: I (Intensified) - 1 verse

Hard case where intensification might overlap with extremely intensified

### 4. Acts 16:26 - "Great Earthquake"

**Reference**: Acts 16:26
**Greek**: σεισμὸς ἐγένετο μέγας
**English (ESV)**: "And suddenly there was a great earthquake"

**Challenge**:
- μέγας (megas) "great" - could be intensified or just descriptive
- Context: Supernatural earthquake (prison shaking)
- Is this I (very great) or just N (great without degree)?
- Or E (extremely great - miracle context)?

**Why ambiguous**: Boundary between descriptive and intensified
**Expected answer**: I (Intensified) or N (No Degree)
**Confidence**: Low

---

## Value 5: E (Extremely Intensified) - 1 verse

Hard case testing threshold for extreme intensification

### 5. Ephesians 3:20 - Triple Compound

**Reference**: Ephesians 3:20
**Greek**: ὑπερεκπερισσοῦ
**English (ESV)**: "Far more abundantly"

**Challenge**:
- ὑπερεκπερισσοῦ (hyperekperissou) - triple compound (ὑπέρ + ἐκ + περισσός)
- Morphologically extreme
- But English translates as comparative: "far MORE abundantly"
- Does TBTA encode Greek (E) or English translation (C)?

**Why ambiguous**: Tests source vs. target language encoding philosophy
**Expected answer**: E (Greek morphology) or C (English translation)
**Confidence**: Very Low (critical test)

---

## Value 6: T ('too'/Excessive) - 1 verse

Hard case testing if "too" appears in Biblical texts

### 6. 1 Corinthians 10:13 - "Beyond Your Ability"

**Reference**: 1 Corinthians 10:13
**Greek**: ὑπὲρ ὃ δύνασθε
**English (ESV)**: "Beyond what you are able to bear"

**Challenge**:
- ὑπὲρ (hyper) "beyond" - could indicate excessive degree
- English "too much" not explicit but implied (beyond ability = excessive)
- Does TBTA use T code for implicit excess?
- Or is this just C (comparative - "more than")?

**Why ambiguous**: Implicit excess vs. explicit comparative
**Expected answer**: T (if implicit excess) or C (comparative) or N (no degree)
**Confidence**: Very Low (rare value, may not exist)

---

## Value 7: L ('less'/Downward Comparative) - 1 verse

Hard case where downward comparison might be comparative

### 7. Hebrews 7:7 - "The Inferior"

**Reference**: Hebrews 7:7
**Greek**: τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται
**English (ESV)**: "It is beyond dispute that the inferior is blessed by the superior"

**Challenge**:
- ἔλαττον (elatton) "lesser/inferior" - comparative of ἐλαχύς
- Downward direction (less/inferior vs. more/superior)
- Does TBTA distinguish L (downward) from C (general comparative)?
- Or both get C?

**Why ambiguous**: Directional distinction unclear
**Expected answer**: L (if directional) or C (if combined)
**Confidence**: Low

---

## Value 8: l ('least'/Downward Superlative) - 1 verse

Hard case where downward superlative might be regular superlative

### 8. Matthew 5:19 - "Least in the Kingdom"

**Reference**: Matthew 5:19
**Greek**: ἐλάχιστος κληθήσεται ἐν τῇ βασιλείᾳ
**English (ESV)**: "Will be called least in the kingdom of heaven"

**Challenge**:
- ἐλάχιστος (elachistos) - superlative "least"
- Downward direction (least vs. greatest)
- Does TBTA use l (downward superlative) or S (general superlative)?
- Is directional distinction encoded?

**Why ambiguous**: Downward vs. upward superlative distinction
**Expected answer**: l (if directional code exists) or S (if combined)
**Confidence**: Low

---

## Value 9: q (Equative) - 1 verse

Hard case testing if equative gets dedicated code

### 9. Matthew 10:25 - "Like His Teacher"

**Reference**: Matthew 10:25
**Greek**: ἀρκετὸν τῷ μαθητῇ ἵνα γένηται ὡς ὁ διδάσκαλος αὐτοῦ
**English (ESV)**: "It is enough for the disciple to be like his teacher"

**Challenge**:
- ὡς (hōs) "like/as" - equative particle
- "As X as Y" construction (equality comparison)
- Does TBTA distinguish q (equative) from C (comparative)?
- Or does equative lack degree marking (N)?

**Why ambiguous**: Equative as degree category unclear
**Expected answer**: q (if distinct code) or N (no degree) or C (general comparison)
**Confidence**: Very Low (rare value)

---

## Value 10: i (Intensified Comparative) - 1 verse

Hard case testing intensified comparative as distinct category

### 10. Romans 5:15 - "Much More"

**Reference**: Romans 5:15
**Greek**: πολλῷ μᾶλλον ἡ χάρις τοῦ θεοῦ
**English (ESV)**: "Much more the grace of God"

**Challenge**:
- πολλῷ μᾶλλον (pollō mallon) - "much more" (intensifier + comparative)
- Is this i (intensified comparative) or just C (comparative)?
- Does πολλῷ "much" create a separate degree category?
- Or is intensification separate from comparison?

**Why ambiguous**: Combined intensification + comparison
**Expected answer**: i (if distinct) or C (if combined with comparative) or I+C (two marks)
**Confidence**: Very Low

---

## Value 11: s (Superlative of 2) - 1 verse

Hard case testing superlative in dyadic context

### 11. Luke 18:14 - "This Man Went Down Justified Rather Than the Other"

**Reference**: Luke 18:14
**Greek**: κατέβη οὗτος δεδικαιωμένος... παρ' ἐκεῖνον
**English (ESV)**: "This man went down to his house justified, rather than the other"

**Challenge**:
- Context: Two men (Pharisee and tax collector) - dyadic
- Comparative παρ' (par') "rather than/more than"
- Does "better of the two" get s (superlative of 2) or just C (comparative)?
- Is this category even used in TBTA?

**Why ambiguous**: Dyadic superlative vs. simple comparative
**Expected answer**: s (if dyadic superlative exists) or C (comparative)
**Confidence**: Very Low (rare value)

---

## Value Coverage Summary

| Value | Description | Verse |
|-------|-------------|-------|
| N | No Degree | John 1:1 |
| C | Comparative | Matt 11:11 |
| S | Superlative | Matt 22:36 |
| I | Intensified | Acts 16:26 |
| E | Extremely Intensified | Eph 3:20 |
| T | 'too' (Excessive) | 1 Cor 10:13 |
| L | 'less' (Downward Comp) | Heb 7:7 |
| l | 'least' (Downward Sup) | Matt 5:19 |
| q | Equative | Matt 10:25 |
| i | Intensified Comparative | Rom 5:15 |
| s | Superlative of 2 | Luke 18:14 |
| **TOTAL** | | **11** |

---

## Expected Performance

**Target accuracy**: 50-60% (5-7 correct out of 11)

**Likely challenges**:
- Rare values (T, q, i, s): May not exist in TBTA → 4 errors expected
- Directional distinction (L vs. C, l vs. S): May not be encoded → 2 errors expected
- Form-function mismatch (Matt 11:11, Matt 22:36): Ambiguous → 2 errors expected
- Source vs. target (Eph 3:20): Critical test of TBTA philosophy → 1 error expected

**High confidence** (3 verses): None (all are ambiguous)
**Medium confidence** (4 verses): N, C, S, I
**Low confidence** (7 verses): E, T, L, l, q, i, s

**Success benchmark**: 5-7 correct = 45-64% ✅

---

## Comparison with Random Test

Random test will have same 11 values but with clearer cases (morphology = semantics).

**Expected gap**: Random 70-80% vs. Adversarial 50-60% = 15-25 points ✅

---

## Prediction Protocol

1. Wait for algorithm v1.0 (from training)
2. Apply to each verse WITHOUT checking TBTA
3. Document reasoning, note ambiguities
4. Rate confidence
5. LOCK predictions (git commit)
6. Check TBTA after lock
7. Calculate accuracy overall and per value

---

**Status**: ✅ Redesigned with equal value coverage
**Next step**: Wait for algorithm v1.0, then predict
**Target date**: 2025-11-10
