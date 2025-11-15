# Thesis Approach Validation Testing

**Created**: 2025-11-15
**Purpose**: Test the new integrated thesis approach (translation-first methodology) on 3 completed features
**Goal**: Determine if translation-first analysis yields better answers than TBTA-only analysis

---

## Selected Features for Testing

### 1. Person System (Clusivity)
- **Current Accuracy**: 98% (from original algorithm)
- **Test Set**: person-system/experiments/test.yaml (if exists)
- **Languages**: Tagalog, Māori, Fijian, Samoan, Indonesian, Malay (Austronesian family)
- **Why**: Strong external validation already exists (9 languages, 7 verses)
- **Known Issues**: Documented in person-system/TODO.md

### 2. Mood
- **Current Accuracy**: 94.6% (Indicative only)
- **Test Set**: mood/experiments/test.yaml (if exists)
- **Languages**: Spanish, French, Portuguese, Italian (Romance languages with subjunctive)
- **Why**: 11 modal values, gateway features documented
- **Complexity**: Multi-value feature with linguistic nuance

### 3. Aspect
- **Current Accuracy**: 98.1%
- **Test Set**: aspect/experiments/test.yaml (if exists)
- **Languages**: Russian, Greek, Turkish, Arabic (languages with explicit aspect marking)
- **Why**: Multi-factor convergence pattern already validated
- **External Validation**: 94.7% agreement across languages

---

## Methodology

### Phase 1: Question Sheet Generation
For each feature, create `{feature}/experiments/test_questions.yaml`:
```yaml
feature: {feature-name}
translations_included: [lang1, lang2, lang3, ...]
verses:
  - reference: "GEN.001.026"
    translations:
      tgl: "{Tagalog text}"
      mri: "{Māori text}"
      fij: "{Fijian text}"
      # ... other languages
```

**Data Source**: Use existing Bible translation APIs or databases
- Tagalog: Ang Biblia (1905)
- Māori: Te Paipera Tapu (1952)
- Fijian: Na Vola Tabu (2012)
- Russian: Synodal Translation
- Spanish: Reina-Valera 1960
- Greek: Modern Greek Bible

### Phase 2: Translation-First Analysis
For each test verse:
1. **Step 1**: Read translations (from test_questions.yaml)
2. **Step 2**: Identify feature value each translation reveals
3. **Step 3**: Check for consensus (80%+ = strong signal)
4. **Step 4**: Compare with TBTA value
5. **Step 5**: Generate prediction with confidence score

**Document in**: `{feature}/experiments/TRANSLATION-ANALYSIS.md`

### Phase 3: Comparison & Validation
Compare:
- **Original Predictions**: From existing algorithm (TBTA-only)
- **New Predictions**: From translation-first methodology
- **Ground Truth**: TBTA answer sheet

**Metrics**:
- Accuracy improvement (%)
- Confidence score distribution
- Divergence resolution rate (cases where translations disagreed with TBTA)
- False positive/negative changes

---

## Expected Outcomes

### Hypothesis 1: Higher Accuracy
Translation consensus should resolve ambiguous cases where TBTA alone was uncertain.

**Test**: Compare accuracy on test sets
- Original: 98% (Person), 94.6% (Mood), 98.1% (Aspect)
- Expected: ≥98% across all three features

### Hypothesis 2: Higher Confidence
Dual-source validation (TBTA + translations) should increase confidence scores.

**Test**: Compare confidence distributions
- Original: Binary (correct/incorrect)
- Expected: Multi-level (Very High 100% consensus, High 80%+, Medium 60-80%, Low <60%)

### Hypothesis 3: Better Divergence Resolution
When translations disagree with TBTA, translation consensus should reveal true answer.

**Test**: Analyze divergence cases
- Expected: <5% of cases show disagreement
- Of those, translation consensus should identify TBTA errors or ambiguous annotations

### Hypothesis 4: Cross-Linguistic Pattern Discovery
Translation analysis should reveal linguistic patterns not visible in TBTA alone.

**Test**: Document novel insights from translation analysis
- Example: Person system trial number in Fijian "kedatou" (3 inclusive)
- Example: Aspect marking patterns in Slavic languages

---

## Implementation Plan

### Step 1: Locate Existing Test Sets (30 min)
- [ ] Find person-system/experiments/test.yaml
- [ ] Find mood/experiments/test.yaml
- [ ] Find aspect/experiments/test.yaml
- [ ] If missing, extract from validation sets or create minimal test sets

### Step 2: Select Translation Languages (30 min)
- [ ] Person System: Austronesian languages (clusivity distinction)
- [ ] Mood: Romance/Slavic languages (subjunctive/conditional)
- [ ] Aspect: Slavic/Semitic languages (explicit aspect marking)
- [ ] Document language selection rationale

### Step 3: Generate Question Sheets (2 hours)
- [ ] Extract verse references from test sets
- [ ] Fetch translations for each verse (API/database)
- [ ] Format as test_questions.yaml
- [ ] Validate formatting against STAGES.md schema

### Step 4: Translation-First Analysis (3 hours)
- [ ] Analyze Person System translations (manual or LLM)
- [ ] Analyze Mood translations
- [ ] Analyze Aspect translations
- [ ] Document consensus patterns and divergences

### Step 5: Compare Results (1 hour)
- [ ] Calculate accuracy metrics (original vs. new)
- [ ] Analyze confidence score improvements
- [ ] Document divergence resolution cases
- [ ] Identify novel linguistic patterns discovered

### Step 6: Documentation (1 hour)
- [ ] Write findings summary
- [ ] Update STAGES.md with validation results
- [ ] Recommend methodology improvements
- [ ] Decide: thesis approach as primary or optional?

**Total Estimated Time**: 8 hours

---

## Success Criteria

✅ **Minimum Viable Success**:
- Question sheets generated for all 3 features
- Translation analysis completed for all test verses
- Comparison metrics calculated
- Findings documented

✅ **Strong Success**:
- Accuracy improves by ≥1% on at least 2 features
- Confidence scores more granular (multi-level vs. binary)
- At least 1 divergence case resolved by translation consensus
- Novel linguistic pattern discovered

✅ **Exceptional Success**:
- Accuracy ≥99% across all 3 features
- Zero false positives introduced by new methodology
- Multiple TBTA annotation errors identified by translation consensus
- Clear recommendation: thesis approach should be primary methodology

---

## Risks & Mitigation

### Risk 1: Translation Data Unavailable
**Impact**: Cannot generate question sheets
**Mitigation**: Use subset of languages with available data, or use public APIs (e.g., Bible Gateway)

### Risk 2: Translation Analysis Too Time-Consuming
**Impact**: Cannot complete all 3 features
**Mitigation**: Start with Person System only, validate approach, then scale

### Risk 3: No Accuracy Improvement
**Impact**: Thesis approach may not be worth the added complexity
**Mitigation**: Still document findings, thesis approach may improve confidence even if not raw accuracy

### Risk 4: Translation Quality Varies
**Impact**: Poor translations introduce noise
**Mitigation**: Select reputable translations (SIL, Bible Society, established versions)

---

## Next Steps

1. ✅ Create this plan
2. 🔄 Locate existing test sets for 3 features
3. ⏳ Select translation languages with rationale
4. ⏳ Generate first question sheet (Person System)
5. ⏳ Run translation-first analysis on Person System
6. ⏳ Compare results and decide on next steps

---

**Status**: In Progress
**Current Step**: Locating existing test sets
