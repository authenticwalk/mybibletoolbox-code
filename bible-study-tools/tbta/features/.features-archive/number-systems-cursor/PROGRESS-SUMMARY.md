# Number-Systems Feature Development Progress

**Feature**: number-systems
**Directory**: `bible-study-tools/tbta/features/number-systems-cursor/`
**Status**: Stages 1-3 Complete, Stage 4 In Progress
**Last Updated**: 2025-11-17

---

## Completed Stages

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)

**Deliverables**:
- [x] `README.md` (comprehensive feature documentation)
  - Feature definition with TBTA encoding values (S/D/T/Q/p/P)
  - Theological/linguistic context (Genesis 1:26 Trinity interpretation detailed)
  - Language family analysis (~220+ languages requiring number marking)
  - TBTA character-based encoding documentation (position 2 of noun codes)
  - Cross-linguistic translation validation strategy
  - Stage checklist integrated

**Key Findings**:
- **TBTA Values**: Singular, Dual, Trial, Quadrial, Paucal, Plural
- **Critical Verse**: Genesis 1:26 "Let us make" - Trial (Trinity) vs Plural (divine council) distinction
- **Encoding**: Position 2 of 10-position noun code in TBTA JSON
- **Scope**: Applied to nouns, pronouns, verb agreement

---

### ✅ Stage 2: Language Study (COMPLETE)

**Deliverables**:
- [x] Language family analysis integrated into README.md
- [x] Documented ~220+ languages requiring number-system marking
- [x] Identified grammatical obligatoriness vs optional marking

**Languages Identified**:
1. **Austronesian (176 languages)**: Dual (~87 Oceanic), Trial (~20-30 Oceanic), Paucal (some)
2. **Trans-New Guinea (129 languages)**: Dual (very common), Paucal (some like Yimas)
3. **Indo-European (135 languages)**: Dual (4 Slavic only: Slovenian, Upper/Lower Sorbian, Kashubian)
4. **Australian (36 languages)**: Paucal (common), Dual (varies by kinship)
5. **Afro-Asiatic (25 languages)**: Dual (Classical Hebrew/Arabic only, historical)

**Cultural Considerations**:
- Genesis 1:26 in polytheistic contexts: Risk of misunderstanding plural as multiple gods
- Islamic/Jewish communities: Non-Trinitarian interpretations
- Cults (JW, Mormon): Risk of false teaching enablement - documented in README

---

### ✅ Stage 3: Scholarly and Internet Research (COMPLETE)

**Deliverables**:
- [x] `experiments/ARBITRARITY-CLASSIFICATION.md` (comprehensive classification)
- [x] Non-arbitrary contexts identified (5 reason groups)
- [x] Arbitrary contexts classified (4 patterns, ~95% of references)

**Non-Arbitrary Contexts** (HIGH theological stakes):
1. **Trinity References** (Gen 1:26, Gen 1:27, Gen 11:7)
   - Affected values: Trial (exactly 3) vs Plural (3+)
   - Doctrines: Trinity, nature of God, creation theology
   - Denominational unity on Trinity substance
   - Cultural sensitivity: Polytheistic vs monotheistic contexts
   - Critical warnings: Never obscure Trinity, never suggest angels in creation

2. **Apostolic Authority** (Acts 15:25, Acts 15:28)
   - Affects understanding of church governance
   - Plural (apostolic council) vs other numbers
   - Interacts with Person System (clusivity: exclusive we)

3. **Paired Disciples/Witnesses** (Luke 24:13, Acts 13:2, Mark 6:7)
   - Dual (exactly 2) vs Plural (2+)
   - Witness principle (Deut 19:15, Matt 18:16)
   - Low-medium theological stakes (accuracy, not doctrine)

4. **Small Group vs Large Assembly** (Matt 18:20, Matt 26:26, Acts 2:46)
   - Paucal (few, 2-5) vs Plural (many)
   - Worship theology: Small gathering vs formal assembly
   - Denominational implications (high church vs low church/house church)

5. **Corporate Solidarity** (Israel/Church references)
   - Singular (collective) vs Plural (individuals)
   - Corporate vs individual identity/responsibility
   - Cultural: Individualist vs collectivist emphasis

**Arbitrary Contexts** (~95% of references):
- Crowd sizes and quantities (85%)
- Natural pairs in Hebrew dual form (5%)
- Travel narratives and mundane events (8%)
- Generic plural references (2%)

---

## In Progress

### 🔄 Stage 4: Generate Test Set with Translation Data (IN PROGRESS)

**Completed**:
- [x] Extracted raw TBTA data using `extract_feature.py`
- [x] `experiments/raw_tbta_data.yaml` (11,649 verses processed)
- [x] Distribution analyzed:
  - **Singular**: 113,745 verses (2,000 cached)
  - **Plural**: 55,654 verses (2,000 cached)
  - **Dual**: 1,744 verses (all cached)
  - **Trial**: 496 verses (all cached)
  - **Quadrial**: 185 verses (all cached) - interesting! These exist despite being contested
  - **Paucal**: 52 verses (all cached)
- [x] Created subagent instructions: `plan/tbta/number-systems-cursor-stage4-subagent-instructions.md`

**Remaining**:
- [ ] Subagent sampling with stratification (OT/NT balance, genre diversity, book diversity)
- [ ] Include adversarial cases (Genesis 1:26, Luke 24:13, Matthew 18:20, Acts 15:25)
- [ ] Select 5-10 representative translations:
  - Trial: Fijian (fij), Hawaiian (haw), Tok Pisin (tpi)
  - Dual: Fijian (fij), Hawaiian (haw), Samoan (smo), Slovenian (slv)
  - Paucal: Check availability (Warlpiri, Australian languages)
- [ ] Generate answer sheets (train.yaml, test.yaml, validate.yaml) - 40%/30%/30% split
- [ ] Generate question sheets (train_questions.yaml, test_questions.yaml, validate_questions.yaml)
- [ ] Document translation database in `experiments/TRANSLATION-DATABASE.md`

**Blockers**:
- Requires access to `.data/commentary/` directory with eBible translations
- May need external API calls to eBible.org or Bible.com
- Subagent invocation for blind data splitting

---

## Pending Stages

### ⬜ Stage 5: Analyze Translations & Develop Algorithm (PENDING)

**Requirements**:
- Translation discovery analysis (primary source): Use train_questions.yaml
- Check translation consensus (80%+ agreement = strong signal)
- Compare with TBTA values (train.yaml)
- Create `experiments/ANALYSIS.md` (up to 12 approaches)
- Develop `experiments/PROMPT1.md` (first iteration)
- Lock predictions with git commit before checking TBTA
- Systematic error analysis (6-step process for every error)
- Iterative refinement (PROMPT2.md, PROMPT3+.md)
- Target: 100% accuracy for stated values (with ≥100 verses per value)

**Expected Challenges**:
- Genesis 1:26: Trinity interpretation requires theological framework
- Dual vs Plural: When explicit count is ambiguous
- Paucal vs Plural: Range boundaries vary by language
- Corporate solidarity: Context-dependent singular vs plural

---

### ⬜ Stage 6: Test Against Validate Set & Peer Review (PENDING)

**Requirements**:
- Blind validation with subagent (validate.yaml predictions without seeing answers)
- 4 critical peer reviews:
  1. **Theological review**: Trinity handling, denominational respect, heresy prevention
  2. **Linguistic review**: Number system typology, genre differences
  3. **Methodological review**: Sample size (≥100/value), balanced sampling, locked predictions
  4. **Translation practitioner review**: Real-world testing with 2-3 languages
- Create `experiments/TRANSLATOR-IMPACT.md`
- Create `experiments/TBTA-REVIEW.md` if divergence exists
- Production readiness: ≥95% accuracy, all reviews passed, net benefit positive

---

## Key Insights and Decisions

### Theological Framework

**Trinity Interpretation** (Genesis 1:26):
- **Christian Orthodox Position**: Trial number if language has it (grammatically encodes Father, Son, Spirit)
- **Alternative if no trial**: Plural with footnote explaining Trinity
- **Non-Orthodox Views** documented for translator awareness:
  - Jehovah's Witnesses: REJECTED (Arian heresy)
  - Mormons/LDS: REJECTED (polytheism)
  - Jewish (non-Messianic): Valid within Judaism, NOT Christian orthodox
  - Islamic: Valid within Islam, NOT Christian orthodox
- **Critical Warnings**: Never obscure Trinity reference, never suggest angels in creation (Isaiah 44:24)

### Data Statistics

**Sample Size**:
- Total annotated verses: 11,649 (from 34 books)
- Singular dominates: 113,745 occurrences (66% of all number references)
- Plural second: 55,654 occurrences (32%)
- Dual: 1,744 (1%)
- Trial: 496 (0.3%)
- Quadrial: 185 (0.1%)
- Paucal: 52 (0.03%)

**Target for Training**: 100+ verses per value
- Singular: Sample 300 (0.26% of 113K)
- Plural: Sample 300 (0.54% of 55K)
- Dual: Use all 1,744 or sample 300
- Trial: Use all 496
- Quadrial: Use all 185
- Paucal: Use all 52

---

## Production Readiness Checklist

- [x] **Stage 1**: Research TBTA Documentation
- [x] **Stage 2**: Language Study
- [x] **Stage 3**: Scholarly & Internet Research
- [ ] **Stage 4**: Generate Test Set (raw data extracted, awaiting subagent for splits)
- [ ] **Stage 5**: Analyze Translations & Develop Algorithm
- [ ] **Stage 6**: Test Against Validate Set & Peer Review
- [ ] **Accuracy**: ≥95% on validate set
- [ ] **4 Peer Reviews**: Theological, Linguistic, Methodological, Translation Practitioner
- [ ] **Translation-Informed Development**: Question sheets with 5-10 languages
- [ ] **Arbitrarity Handling**: Multi-answer output for non-arbitrary contexts
- [ ] **Methodological Rigor**: Locked predictions, blind testing, error analysis
- [ ] **Practical Application Testing**: TRANSLATOR-IMPACT.md with net benefit analysis

---

## Next Steps (Immediate)

1. **Complete Stage 4**:
   - Invoke subagent with `/plan/tbta/number-systems-cursor-stage4-subagent-instructions.md`
   - Subagent generates train/test/validate splits
   - Subagent creates translation question sheets
   - Subagent returns only question sheet paths (maintains blindness)

2. **Proceed to Stage 5**:
   - Analyze translations from train_questions.yaml
   - Identify patterns (Trinity contexts, explicit counts, corporate solidarity)
   - Develop PROMPT1.md
   - Lock predictions before TBTA check
   - Iterate until 95%+ accuracy

3. **Complete Stage 6**:
   - Blind validation on validate set
   - 4 peer reviews
   - TRANSLATOR-IMPACT.md creation
   - Production readiness assessment

---

## Files Created

### Documentation
- `README.md` - Comprehensive feature documentation (500 lines)
- `PROGRESS-SUMMARY.md` - This file
- `plan/tbta/number-systems-cursor-stage4-subagent-instructions.md` - Subagent task specification

### Experiments
- `experiments/ARBITRARITY-CLASSIFICATION.md` - Non-arbitrary vs arbitrary classification
- `experiments/raw_tbta_data.yaml` - Extracted TBTA data (11,649 verses, 6 values)

### Pending Creation
- `experiments/TRANSLATION-DATABASE.md` - Translation selection rationale
- `experiments/train.yaml`, `test.yaml`, `validate.yaml` - Answer sheets (TBTA values)
- `experiments/train_questions.yaml`, `test_questions.yaml`, `validate_questions.yaml` - Question sheets (translations only)
- `experiments/ANALYSIS.md` - Approach comparison (up to 12 approaches)
- `experiments/PROMPT1.md`, `PROMPT2.md`, etc. - Algorithm iterations
- `experiments/LEARNINGS.md` - Error analysis with 6-step process
- `experiments/TRANSLATOR-IMPACT.md` - Real-world testing results
- `experiments/TBTA-REVIEW.md` - Communication with TBTA team (if needed)

---

**Status**: Foundation complete (Stages 1-3), data extraction complete, ready for subagent sampling and algorithm development.

**Commit**: d928a3d - "feat(tbta): number-systems-cursor Stages 1-3 complete"

