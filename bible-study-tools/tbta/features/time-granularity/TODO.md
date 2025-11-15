# Time Granularity Feature - TODO

**Feature ID**: Time Granularity (Tier A, Feature #8)
**Status**: Stage 1 Complete → Stage 2 Next
**Last Updated**: 2025-11-15

---

## Current Status

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)

**Completed**:
- Reviewed official TBTA documentation (README, FEATURES, DATA-STRUCTURE, EDGE-CASES)
- Created comprehensive README.md with:
  - Feature definition and 20+ temporal distinctions
  - Theological/linguistic context
  - Language family analysis (11 families, 725+ languages)
  - Genesis narrative examples
  - TBTA encoding details
- Migrated experimental work:
  - PROMPT1.md: 6 test cases (narrative, prophecy, discourse, evidential)
  - TEMPLATE.md: 5-level hierarchical prediction template
- Integrated language family documentation into README

**Deliverables**:
- `/README.md`: Primary feature documentation
- `/experiments/PROMPT1.md`: Test passage design
- `/experiments/TEMPLATE.md`: Prediction methodology
- `/TODO.md`: This file

---

## Next Steps

### ⬜ Stage 2: Language Study

**Objective**: Review language families in `/bible-study-tools/tbta/languages/families/` to identify which grammatically encode time granularity.

**Tasks**:
- [ ] Review all language family documentation in `/languages/families/`
- [ ] Identify which families have grammatically obligatory temporal remoteness marking
- [ ] Distinguish obligatory vs optional marking systems
- [ ] Document target translation scenarios for each family
- [ ] Create language-specific guidance:
  - [ ] Austronesian: Tagalog temporal particle usage
  - [ ] Bantu: Hodiernal/pre-hodiernal systems
  - [ ] Trans-New Guinea: Deictic temporal markers
  - [ ] Quechuan: Evidential-temporal fusion
  - [ ] Mayan: Aspect-temporal interactions
- [ ] Update README.md with detailed language analysis

**Expected Duration**: 3-5 hours

**Success Criteria**:
- Clear classification of obligatory vs optional time marking by family
- Language-specific translation guidance for top 10 families
- Updated README with language study findings

---

### ⬜ Stage 3: Scholarly and Internet Research

**Objective**: Find academic articles and resources on temporal remoteness systems in Bible translation.

**Tasks**:
- [ ] Search for academic articles on graded tense systems
- [ ] Find cross-linguistic studies on temporal marking
- [ ] Research Bible translation challenges with temporal remoteness
- [ ] Document additional language examples from academic literature
- [ ] Update ATTRIBUTION.md with new sources
- [ ] Update README.md with research findings

**Target Resources**:
- Nurse (2008): Tense and Aspect in Bantu
- Bybee et al. (1994): Evolution of Grammar (tense/aspect/modality)
- Payne & Payne (1990): Yagua temporal systems
- Givón (1972): ChiBemba and Bantu grammar
- Academic journals: Journal of Translation, Journal of Linguistics

**Expected Duration**: 4-6 hours

**Success Criteria**:
- 10+ academic sources documented
- New language examples added
- ATTRIBUTION.md updated with citation codes

---

### ⬜ Stage 4: Generate Proper Test Set (SUBAGENT REQUIRED)

**CRITICAL**: Use subagent to prevent seeing TBTA answers before prediction.

**Objective**: Extract TBTA data for Time Granularity feature and create balanced test sets.

**Tasks**:
- [ ] **Subagent 1**: Extract TBTA data for time granularity feature
  - [ ] Parse TBTA character-encoded data
  - [ ] Extract all verses with time granularity values
  - [ ] Create distribution analysis (how many verses per value)
  - [ ] Identify rare vs common values
- [ ] **Subagent 2**: Create balanced sample sets
  - [ ] Stratify by testament (OT/NT proportional)
  - [ ] Stratify by genre (narrative, poetry, prophecy, epistle)
  - [ ] Stratify by book distribution (avoid single-book concentration)
  - [ ] Include adversarial cases (challenging temporal contexts)
  - [ ] Target: 100+ verses per temporal value (2000+ total)
- [ ] **Subagent 3**: Split into train/test/validate
  - [ ] Train set: 40% (for analysis and hypothesis formation)
  - [ ] Test set: 30% (for iterative refinement)
  - [ ] Validate set: 30% (for final blind validation)
  - [ ] Store in `experiments/train.yaml`, `test.yaml`, `validate.yaml`
- [ ] **Subagent 4**: Identify external validation languages
  - [ ] Find published Bible translations in:
    - Tagalog (Austronesian)
    - Yagua (Peba-Yaguan)
    - ChiBemba (Bantu)
    - Quechua (Quechuan)
  - [ ] Select 20 representative verses for cross-linguistic validation

**Expected Duration**: 6-8 hours (mostly subagent work)

**Success Criteria**:
- Balanced train/test/validate sets created
- All 20+ temporal values represented
- External validation languages identified
- Main agent has NOT seen TBTA values for test/validate sets

---

### ⬜ Stage 5: Propose Hypothesis and First Prompt

**Objective**: Analyze training data and develop first prediction prompt.

**Tasks**:
- [ ] Analyze `experiments/train.yaml` for patterns
  - [ ] Genre-time correlations
  - [ ] Explicit temporal markers
  - [ ] Verb form patterns (Greek/Hebrew)
  - [ ] Discourse frame indicators
- [ ] Review `learnings/README.md` for transferable patterns from other features
- [ ] Create `experiments/ANALYSIS.md`:
  - [ ] Document 8-12 different prediction approaches
  - [ ] Rank by expected accuracy
  - [ ] Identify strengths/weaknesses of each
- [ ] Develop `experiments/PROMPT1.md` (if not already created, refine existing)
  - [ ] 5-level hierarchical template (genre → markers → verb form → rules → discourse)
  - [ ] Clear decision rules at each level
  - [ ] Examples for each decision point
- [ ] **Git commit and lock predictions** before checking TBTA
- [ ] Test PROMPT1 against `experiments/test.yaml`
  - [ ] Subagent generates blind predictions
  - [ ] Subagent scores against TBTA
  - [ ] Return only accuracy scores (not individual predictions)
- [ ] Analyze errors using 6-step process:
  1. Categorize error types
  2. Identify common patterns
  3. Check if rule-based or context-dependent
  4. Propose refinements
  5. Test refinements on subset
  6. Iterate until 95%+ accuracy on test set

**Expected Duration**: 10-15 hours

**Success Criteria**:
- PROMPT1 achieves 95%+ accuracy on test set
- All error patterns documented and addressed
- Git history shows locked predictions before TBTA check

---

### ⬜ Stage 6: Test Against Validate Set & Peer Review

**Objective**: Final validation on unseen data with multi-reviewer assessment.

**Tasks**:
- [ ] **Subagent 1** (Prediction): Generate blind predictions on `validate.yaml`
  - Use finalized PROMPT from Stage 5
  - NO access to TBTA values
  - Git commit predictions before scoring
- [ ] **Subagent 2** (Scoring): Score predictions against TBTA
  - Return accuracy only (not individual results)
  - Break down by temporal value (ancient past, recent past, etc.)
  - Identify systematic errors
- [ ] **Main agent**: Analyze errors
  - Review error patterns
  - Document cases where TBTA may be incorrect
  - Note ambiguous cases requiring human judgment
- [ ] **Subagent 3** (Theological Reviewer): Check theological soundness
  - Review predictions for Genesis creation (ancient past required)
  - Review eschatological passages (remote future required)
  - Verify timeless present for doctrinal statements
- [ ] **Subagent 4** (Linguistic Reviewer): Check linguistic accuracy
  - Verify language family requirements met
  - Check aspect-tense interactions
  - Validate evidential-temporal fusion cases
- [ ] **Subagent 5** (Methodological Reviewer): Verify scientific rigor
  - Confirm blind prediction protocol followed
  - Check statistical validity of test sets
  - Review documentation completeness
- [ ] **Subagent 6** (Translation Practitioner): Test with real scenarios
  - Apply predictions to actual translation work
  - Identify practical challenges
  - Document translation impact
- [ ] Create `experiments/TRANSLATOR-IMPACT.md`
  - Document how predictions improve translation quality
  - Provide before/after examples
  - Note remaining challenges
- [ ] Refine based on all reviewer feedback
- [ ] Mark production ready when:
  - [ ] Validate set accuracy ≥ 90%
  - [ ] All reviewers approve
  - [ ] Translator impact documented
  - [ ] External language validation complete (2-3 languages minimum)

**Expected Duration**: 12-20 hours (includes multi-reviewer coordination)

**Success Criteria**:
- Validate set accuracy ≥ 90%
- Theological, linguistic, methodological reviews pass
- Translation practitioner confirms utility
- Production-ready status achieved

---

## Success Metrics

### Stage-Specific Metrics

- **Stage 2**: Language families classified (obligatory vs optional marking)
- **Stage 3**: 10+ academic sources documented
- **Stage 4**: Balanced test sets created, external validation ready
- **Stage 5**: Test set accuracy ≥ 95%
- **Stage 6**: Validate set accuracy ≥ 90%, all reviews pass

### Overall Feature Metrics

- **Coverage**: All 20+ temporal values testable
- **Accuracy**: 90%+ on unseen data
- **Utility**: Translation practitioner confirms improvement
- **Documentation**: Complete README, experiments, learnings
- **Validation**: External language cross-check successful

---

## Risks and Mitigation

### Risk: TBTA Data Incomplete
- **Impact**: Cannot validate all 20+ temporal values
- **Mitigation**: Document coverage gaps, use linguistic theory for unvalidated values

### Risk: Temporal Ambiguity
- **Impact**: Some contexts genuinely ambiguous
- **Mitigation**: Document acceptable confidence ranges, flag ambiguous cases

### Risk: Language-Specific Variation
- **Impact**: One-size-fits-all predictions may not work
- **Mitigation**: Create language-family-specific guidance

### Risk: Context Dependency
- **Impact**: Temporal marking depends on broader discourse
- **Mitigation**: Integrate with discourse genre and other features

---

## Notes for Next Researcher

**Key Insights**:
1. Time granularity is obligatory in 150+ languages - not optional
2. Genre is the strongest predictor (narrative → past, teaching → timeless)
3. Explicit temporal markers override genre defaults (95%+ confidence)
4. Aspect-based systems (Mayan, Chinese) need different approach
5. Evidential-temporal fusion (Quechuan) requires integrated analysis

**Critical Files**:
- README.md: Feature documentation
- experiments/TEMPLATE.md: 5-level prediction hierarchy
- experiments/PROMPT1.md: Test cases for 6 passage types
- TODO.md: This file

**Next Immediate Action**: Stage 2 - Language study in `/languages/families/`

---

**Last Updated**: 2025-11-15
**Stage**: 1 Complete → 2 Next
**Researcher**: Claude Code Agent
