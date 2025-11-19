# PROMPT4: Translation Agreement Algorithm - BREAKTHROUGH PLAN

**Date**: 2025-11-19
**Discovery**: Access to 1000+ translations via eBible corpus
**Expected Accuracy**: 80-90% (vs current 42.1%)
**Status**: Setting up eBible corpus

---

## The Breakthrough

**CRITICAL REALIZATION**: We've been trying to predict grammatical number from English (which only has Singular/Plural), when we have access to **1000+ translations** including languages that **grammatically mark** trial/dual/paucal!

### What We Have Access To

**eBible Corpus** (~500MB, 1000+ translations):
```bash
git clone --depth 1 https://github.com/BibleNLP/ebible ~/projects/ebible
```

**Trial-Marking Languages** (grammatically distinguish 3 items):
- **Samoan (smo)**: Has trial number
- **Fijian (fij)**: Has trial number
- **Tok Pisin (tpi)**: Has trial number (if available)
- **Various Austronesian**: May have trial

**Dual-Marking Languages** (grammatically distinguish 2 items):
- **Slovenian (slv)**: Has dual number (Slavic)
- **Upper Sorbian (hsb)**: Has dual number (Slavic)
- **Lower Sorbian (dsb)**: Has dual number if available

**Why This Works**:
When Samoan translates Gen 1:26 "Let us make", it MUST choose between:
- Trial pronoun (exactly 3 persons) → "kita (3)"
- Plural pronoun (many persons) → "kita (many)"

The grammatical choice reveals the intended number!

---

## From CRITICAL-FINDINGS.md

We predicted this would work:

> **Option 2: Trial-Marking Translations** (Good - 80-85% expected)
> - Fijian, Samoan, Tok Pisin grammatically mark trial
> - Check how they translated Gen 1:26, other trial contexts
> - Timeline: 3-4 weeks to populate translations

**WE CAN DO THIS NOW!**

---

## PROMPT4 Algorithm: Translation Agreement

### Core Principle

**Instead of predicting from English, CHECK how languages with grammatical number translated the verse.**

### Level 1: Trial Detection (Samoan, Fijian, Tok Pisin)

```yaml
IF verse contains pronoun or verb in Samoan/Fijian/Tok Pisin:
  PARSE morphology:
    - Trial morphology detected → Trial
    - Dual morphology detected → Dual
    - Plural morphology detected → Plural
    - Singular morphology detected → Singular
  ELSE IF pronoun form analysis:
    - Samoan "kita (trial)" vs "kita (plural)"
    - Fijian "kedaru/rau" (trial) vs "keda" (plural)

  Confidence: Very High (grammatical marking is explicit)
```

### Level 2: Dual Detection (Slovenian, Upper Sorbian)

```yaml
IF verse contains paired entities:
  CHECK Slovenian/Upper Sorbian translation:
    - Dual case/number marking → Dual
    - Plural case/number marking → Plural or Paucal

  Examples:
    - Slovenian: "dva" (2) + dual noun declension
    - Upper Sorbian: "dwaj" (2) + dual morphology

  Confidence: Very High (grammatical marking is explicit)
```

### Level 3: Translation Consensus (10+ languages)

```yaml
IF 10+ languages available:
  COUNT number patterns across languages:
    - Singular: languages using singular forms
    - Dual: languages using dual forms (if available)
    - Trial: languages using trial forms (if available)
    - Plural: languages using plural forms

  IF >70% agreement on a number value:
    RETURN majority value
    Confidence: High (cross-linguistic consensus)
  ELSE:
    RETURN "uncertain"
    Confidence: Low
```

### Level 4: English Fallback (PROMPT2)

If trial/dual languages unavailable, fall back to PROMPT2 explicit number detection.

---

## Expected Accuracy Improvements

### Current State (PROMPT2)

| Value | Accuracy | Sample Size | Why It Failed |
|-------|----------|-------------|---------------|
| Trial | 30.0% | 40 | English doesn't mark trial |
| Dual | 20.8% | 48 | English doesn't mark dual |
| Paucal | 25.0% | 20 | "Few" is ambiguous |
| Plural | 21.6% | 51 | Confuses with minorities |
| **Overall** | **42.1%** | **236** | **English insufficient** |

### Expected State (PROMPT4)

| Value | Accuracy | Data Source | Expected |
|-------|----------|-------------|----------|
| **Trial** | **80-90%** | Samoan/Fijian morphology | High confidence |
| **Dual** | **85-95%** | Slovenian/Sorbian morphology | Very high |
| **Paucal** | **50-60%** | Translation consensus + English | Moderate |
| **Plural** | **80-90%** | Translation consensus | High |
| **Overall** | **80-90%** | **Translation-based** | **Target** |

---

## Implementation Steps

### Phase 1: Setup eBible Corpus ✅ (In Progress)

```bash
# Clone repo
mkdir -p ~/projects
git clone --depth 1 https://github.com/BibleNLP/ebible ~/projects/ebible

# Verify structure
ls ~/projects/ebible/corpus/*.txt | wc -l  # Should be 1000+
```

### Phase 2: Test Language Availability

```bash
# Test trial-marking languages
python fetch_verse.py "GEN.001.026" --lang smo,fij,tpi

# Test dual-marking languages
python fetch_verse.py "LUK.005.002" --lang slv,hsb,dsb

# Test coverage
python fetch_verse.py "MAT.018.020" --lang smo,fij,slv,hsb
```

Expected results:
- Gen 1:26: Samoan/Fijian should use **trial** for "Let us" (Trinity)
- Luk 5:2: Slovenian should use **dual** for "two boats"

### Phase 3: Re-populate All 592 Verses

Update `populate_translations.py` to fetch 15-20 languages:
- **Trial**: smo, fij, tpi
- **Dual**: slv, hsb, dsb
- **High coverage**: eng, spa, fra, deu, por
- **Original**: grc (Greek), heb (Hebrew) if available

### Phase 4: Develop PROMPT4 Algorithm

Create morphological analysis rules for:
- **Samoan trial pronouns**: kita (3), koutou (3), latou (3)
- **Fijian trial pronouns**: kedaru/rau, kemudou/dou, iratou
- **Slovenian dual**: -a ending, dva/dve forms
- **Upper Sorbian dual**: dwaj, dual declension patterns

### Phase 5: Run Predictions

```bash
# Lock predictions via git
git add experiments/train_predictions_v4.yaml
git commit -m "Lock PROMPT4 predictions (translation-based)"

# Score against train.yaml answer sheet
python score_predictions.py --prediction train_predictions_v4.yaml --answers train.yaml
```

### Phase 6: Compare to PROMPT2

Expected results:
- **PROMPT2**: 42.1% (99/236 correct)
- **PROMPT4**: 80-90% (189-212/236 correct) - Target
- **Improvement**: +38-48 percentage points

---

## Morphological Patterns to Detect

### Samoan Trial Morphology

**Pronouns** (trial = exactly 3):
```
Inclusive trial: tātou (we-3-including-you)
Exclusive trial: mātou (we-3-excluding-you)
2nd person trial: tou (you-3)
3rd person trial: lātou (they-3)
```

**Verbs**: Trial subject agreement (if detectable in text)

### Fijian Trial Morphology

**Pronouns**:
```
Inclusive trial: kedaru/kedatou
Exclusive trial: keirau/keitou
2nd person trial: kemudou/dou
3rd person trial: iratou/rau
```

### Slovenian Dual Morphology

**Nouns**: Dual case endings (nominative, genitive, etc.)
```
Masculine: -a (nom), -ov (gen)
Feminine: -i (nom), dual inflection
Neuter: -i (nom)
```

**Numerals**:
```
"dva" (2, masculine), "dve" (2, feminine/neuter)
"oba" (both)
```

### Upper Sorbian Dual Morphology

**Numerals**:
```
"dwaj" (2, masculine personal)
"dwě" (2, other genders)
```

**Nouns**: Dual endings on nouns after "dva/dwaj/dwě"

---

## Risk Analysis

### What Could Go Wrong

1. **Languages not available in eBible**:
   - Mitigation: Check coverage first, fall back to PROMPT2 for missing

2. **Morphology not detectable in plain text**:
   - Mitigation: Use pronoun forms, numeral patterns, word order

3. **Translation inconsistency**:
   - Mitigation: Require >70% consensus across languages

4. **Orthography variations**:
   - Mitigation: Build pattern dictionaries for each language

### What Could Go Right

1. **80-90% accuracy achieved**: Full production deployment (Tier 1 + Tier 2)
2. **90-95% accuracy**: Exceeds STAGES.md threshold
3. **>95% accuracy**: Publishable methodology for other TBTA features

---

## Timeline

- **Phase 1 (Setup)**: 30 minutes (eBible clone) ✅
- **Phase 2 (Test)**: 1 hour (verify language availability)
- **Phase 3 (Re-populate)**: 2-4 hours (592 verses × 15-20 languages)
- **Phase 4 (Algorithm)**: 4-6 hours (morphological pattern rules)
- **Phase 5 (Predictions)**: 2 hours (run + score)
- **Phase 6 (Comparison)**: 1 hour (analysis)

**Total**: 10-15 hours vs 3-4 weeks estimated in CRITICAL-FINDINGS.md

---

## Success Criteria

**Tier 2 Deployment** (80-85% accuracy):
- General dual/trial/paucal prediction enabled
- Mark <70% confidence predictions for human review

**Full Deployment** (90-95% accuracy):
- All contexts use algorithm prediction
- High confidence in all 6 number categories

**Publishable** (>95% accuracy):
- Methodology transferable to other TBTA features
- Demonstrates power of translation-based linguistic analysis

---

## Next Steps

1. ✅ Clone eBible corpus (in progress - background process 9ba61a)
2. ⏳ Test Samoan Gen 1:26 for trial marking
3. ⏳ Test Slovenian Luk 5:2 for dual marking
4. ⏳ Build morphological pattern dictionaries
5. ⏳ Update populate_translations.py for 15-20 languages
6. ⏳ Develop PROMPT4 algorithm
7. ⏳ Run predictions and compare to PROMPT2

---

**Status**: BREAKTHROUGH DISCOVERED - Translation agreement could solve data limitation!
**Expected Outcome**: 80-90% accuracy (vs 42.1% current)
**Timeline**: 10-15 hours of work
