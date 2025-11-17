# Subagent Instructions: Number Systems Feature - Stage 4 Data Generation

**CRITICAL**: You are a subagent responsible for generating train/test/validate datasets for the number-systems feature. You will create both answer sheets (with TBTA values) and question sheets (translations only), but you will ONLY return paths to question sheets to the main agent.

**Goal**: Generate stratified train/test/validate splits with translation question sheets for the number-systems feature.

---

## Input Data

**Raw TBTA Data**: `bible-study-tools/tbta/features/number-systems-cursor/experiments/raw_tbta_data.yaml`

**Distribution**:
- Singular: 113,745 total (2,000 cached)
- Dual: 1,744 total (all cached)
- Trial: 496 total (all cached)
- Quadrial: 185 total (all cached)
- Paucal: 52 total (all cached)
- Plural: 55,654 total (2,000 cached)

---

## Your Tasks

### Task 1: Read and Understand Raw Data

Load `raw_tbta_data.yaml` and understand the structure:
```yaml
feature: number
value:
  - specific_value: "Singular"
    total_verses: 113745
    verses: ["GEN.001.001", "GEN.001.002", ...]
  - specific_value: "Dual"
    total_verses: 1744
    verses: [...]
```

### Task 2: Sample with Stratification

**Target Sample Size**: 100+ verses per value minimum

**Sampling Strategy**:
1. **Singular**: Sample 300 verses (small percentage of 113,745)
2. **Dual**: Use all 1,744 or sample 300 if needed
3. **Trial**: Use all 496
4. **Quadrial**: Use all 185
5. **Paucal**: Use all 52
6. **Plural**: Sample 300 verses (small percentage of 55,654)

**Stratification Criteria**:
1. **Testament Balance**: Proportional OT/NT distribution based on raw data
2. **Genre Diversity**: Include narrative, poetry, prophecy, epistle
   - Use book knowledge to classify genres (e.g., Genesis = narrative, Psalms = poetry, Romans = epistle)
3. **Book Diversity**: Avoid concentration in single book
4. **Difficulty**: Include both typical and adversarial cases

**Adversarial Cases to Include**:
- **Genesis 1:26**: Trial vs Plural ambiguity (Trinity reference) - MUST INCLUDE
- **Luke 24:13**: Dual (two disciples) - MUST INCLUDE
- **Matthew 18:20**: Paucal (two or three gather) - MUST INCLUDE
- **Acts 15:25**: Plural (apostolic council) - MUST INCLUDE
- Any verse with theological significance from ARBITRARITY-CLASSIFICATION.md

### Task 3: Split into Train/Test/Validate (40%/30%/30%)

**Split Proportions**:
- **Train**: 40% of each value
- **Test**: 30% of each value (include adversarial cases)
- **Validate**: 30% of each value (blind testing set)

**Output Answer Sheets** (WITH TBTA values):
- `train.yaml`
- `test.yaml`
- `validate.yaml`

**Format** (follow STAGES.md template):
```yaml
feature: number-systems
translation_database:
  languages: [fij, haw, smo, slv, ...]
  families: [Austronesian, Indo-European, ...]
  rationale: "Selected for dual/trial marking"
value:
  - specific_value: "Dual"
    total_verses: 523
    distribution:
      OT: 381
      NT: 142
      Books: {GEN: 50, EXO: 30, ...}
    genres:
      narrative: 400
      poetry: 50
      prophecy: 30
      epistle: 43
    verses:
      - reference: "LUK.024.013"
        tbta_value: "Dual"
        genre: "narrative"
        difficulty: "typical"
        notes: "Explicitly two disciples"
```

### Task 4: Select Representative Translations (5-10 languages)

**Languages to Select** (based on number-systems marking):

**Trial-marking languages** (Genesis 1:26 validation):
- **fij** (Fijian): Trial pronouns
- **haw** (Hawaiian): Trial pronouns
- **tpi** (Tok Pisin): Trial pronouns

**Dual-marking languages** (Luke 24:13, Mark 6:7 validation):
- **fij** (Fijian): Dual pronouns (also has trial)
- **haw** (Hawaiian): Dual pronouns (also has trial)
- **smo** (Samoan): Dual pronouns
- **slv** (Slovenian): Obligatory dual (only Slavic language with dual)

**Paucal-marking languages** (Matthew 18:20 validation):
- Check if any accessible (Warlpiri, Australian languages)
- If not available, use translations with contextual clues

**Document Selection** in `experiments/TRANSLATION-DATABASE.md`:
```markdown
# Translation Database for Number-Systems Feature

## Selected Languages

### Trial-Marking Languages
- **Fijian (fij)**: Austronesian, Oceanic. Has dual + trial + paucal. Direct from English.
- **Hawaiian (haw)**: Austronesian, Polynesian. Has dual + trial. Direct from source texts.
- **Tok Pisin (tpi)**: Austronesian creole. Has trial pronouns (mitripela, yumitripela).

### Dual-Marking Languages
- **Fijian (fij)**: (see above)
- **Hawaiian (haw)**: (see above)
- **Samoan (smo)**: Austronesian, Polynesian. Has dual pronouns.
- **Slovenian (slv)**: Indo-European, Slavic. Obligatory dual for count 2.

## Availability
Check eBible.org and Bible.com for these translations. If not available, substitute with similar language family translations.
```

### Task 5: Generate Question Sheets (Translations Only)

For each split (train, test, validate), generate question sheets:

**Data Source**: `.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-ebible.yaml`

**Note**: The `.data` directory may not have all translations. Use what's available. If eBible data is not accessible, note this and generate placeholder question sheets for now.

**Output Format**:
```yaml
# train_questions.yaml (or test_questions.yaml, validate_questions.yaml)
feature: number-systems
translations_included: [fij, haw, smo, slv, tpi]
verses:
  - reference: "LUK.024.013"
    translations:
      fij: "{Fijian text}"
      haw: "{Hawaiian text}"
      smo: "{Samoan text}"
      slv: "{Slovenian text}"
      tpi: "{Tok Pisin text}"
  - reference: "GEN.001.026"
    translations:
      fij: "{Fijian text}"
      haw: "{Hawaiian text}"
      smo: "{Samoan text}"
      slv: "{Slovenian text}"
      tpi: "{Tok Pisin text}"
```

**If Translation Data Not Available**: Generate placeholder question sheets noting that translation texts need to be fetched:
```yaml
feature: number-systems
translations_included: [fij, haw, smo, slv, tpi]
note: "Translation texts need to be fetched from eBible.org or Bible.com APIs"
verses:
  - reference: "LUK.024.013"
    translations: {}
    note: "Fetch from .data/commentary/LUK/024/003/LUK-024-013-ebible.yaml"
```

---

## Critical Rules for Subagent

1. **DO NOT** show TBTA values in question sheets
2. **DO NOT** return answer sheet paths to main agent
3. **DO** generate both answer sheets and question sheets
4. **DO** return ONLY question sheet paths to main agent
5. **DO** include Genesis 1:26, Luke 24:13, Matthew 18:20 in test set
6. **DO** ensure 100+ verses per value in total dataset
7. **DO** balance OT/NT proportionally
8. **DO** diversify across genres and books

---

## What to Return to Main Agent

**Return ONLY**:
```
Generated question sheets:
- bible-study-tools/tbta/features/number-systems-cursor/experiments/train_questions.yaml
- bible-study-tools/tbta/features/number-systems-cursor/experiments/test_questions.yaml
- bible-study-tools/tbta/features/number-systems-cursor/experiments/validate_questions.yaml

Generated translation database documentation:
- bible-study-tools/tbta/features/number-systems-cursor/experiments/TRANSLATION-DATABASE.md

Answer sheets (with TBTA values) stored but NOT returned to main agent:
- bible-study-tools/tbta/features/number-systems-cursor/experiments/train.yaml
- bible-study-tools/tbta/features/number-systems-cursor/experiments/test.yaml
- bible-study-tools/tbta/features/number-systems-cursor/experiments/validate.yaml
```

**DO NOT show main agent**:
- Contents of answer sheets (train.yaml, test.yaml, validate.yaml)
- TBTA values for test or validate sets
- Any predictions or analysis that would leak answers

---

## Success Criteria

- [ ] 100+ verses per value sampled
- [ ] Train/test/validate split 40%/30%/30%
- [ ] OT/NT balance proportional
- [ ] Genre diversity (narrative, poetry, prophecy, epistle)
- [ ] Book diversity (no single book >30%)
- [ ] Adversarial cases included (Genesis 1:26, Luke 24:13, Matthew 18:20, Acts 15:25)
- [ ] 5-10 representative translations selected
- [ ] Translation database documented
- [ ] Question sheets generated (translations only, NO TBTA values)
- [ ] Answer sheets generated but NOT shown to main agent
- [ ] Only question sheet paths returned to main agent

---

**Start Work**: Begin by reading `raw_tbta_data.yaml` and understanding the distribution, then proceed with sampling and splitting.

