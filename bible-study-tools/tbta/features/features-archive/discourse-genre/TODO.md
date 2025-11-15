# Discourse Genre Feature - TODO

**Feature ID**: Discourse Genre (Tier A, Feature #14)
**Status**: Stage 1 Complete → Stage 2 Next
**Last Updated**: 2025-11-15

---

## Current Status

### ✅ Stage 1: Research TBTA Documentation (COMPLETE)

**Completed**:
- Reviewed official TBTA documentation
- Reviewed prior experimental work in `/plan/tbta-rebuild-with-llm/features/discourse-genre/`
- Created comprehensive README.md with:
  - Feature definition (genre as gateway feature)
  - 9 complete genre value definitions
  - Translation impact analysis
  - Language-specific implications (obligatory vs optional)
  - Genre-tense correlation findings
  - Experimental work summary
- Migrated experimental work to new structure:
  - experiments/EXPERIMENT1.md (Matthew 24 analysis)
  - training/ALGORITHM-v1.md (prediction algorithm)
  - training/PATTERNS-LEARNED.md (10 critical discoveries)
  - training/CRITICAL-FINDING.md (TBTA data limitations)

**Key Findings**:
1. Genre determines grammaticality in 150+ languages
2. Only 1 of 9 genres validated in TBTA sample (11% coverage)
3. Matthew 24 analysis: 90%+ tense-genre correlation
4. Strong predictors: Illocutionary force, tense, participant tracking
5. Algorithm v1.0 ready for testing (linguistic-theory-based)

**Deliverables**:
- `/README.md`: Primary feature documentation
- `/experiments/EXPERIMENT1.md`: Matthew 24 comprehensive analysis
- `/training/ALGORITHM-v1.md`: Prediction algorithm with confidence levels
- `/training/PATTERNS-LEARNED.md`: Key learnings from analysis
- `/training/CRITICAL-FINDING.md`: TBTA data gap documentation
- `/TODO.md`: This file

---

## Next Steps

### ⬜ Stage 2: Language Study

**Objective**: Review language families to identify genre-tense systems and create language-specific guides.

**Tasks**:
- [ ] Review all language family documentation in `/bible-study-tools/tbta/languages/families/`
- [ ] Identify families with obligatory genre-tense marking:
  - [ ] Austronesian: Register and particle changes
  - [ ] Bantu: Narrative tense restrictions
  - [ ] Japonic: Distinct verb forms per genre
  - [ ] Romance: Genre-specific tense (passé simple, imparfait)
  - [ ] Sino-Tibetan: Aspect particle variation
- [ ] Document genre marking strategies:
  - [ ] Explicit grammatical markers (Japanese registers, French tenses)
  - [ ] Subtle markers (English style, discourse particles)
  - [ ] Minimal/no marking (context-dependent languages)
- [ ] Create language-specific translation guides:
  - [ ] French: Passé simple (narrative only), imparfait (background), présent (teaching)
  - [ ] Japanese: ta-form (narrative), desu/masu (teaching), archaic (legal)
  - [ ] Hebrew: wayyiqtol (narrative only), qatal (other genres)
  - [ ] Bantu: Tense-genre mapping by language
- [ ] Update README.md with detailed language analysis

**Expected Duration**: 4-6 hours

**Success Criteria**:
- Language families classified by genre-marking obligation
- Top 10 languages have genre-specific guides
- README updated with language study findings

---

### ⬜ Stage 3: Scholarly and Internet Research

**Objective**: Find academic resources on discourse genre in Bible translation.

**Tasks**:
- [ ] Search for academic articles on genre-tense systems
- [ ] Find cross-linguistic studies on discourse genre
- [ ] Research Bible translation challenges with genre
- [ ] Document language examples from academic literature
- [ ] Update ATTRIBUTION.md with new sources
- [ ] Update README.md with research findings

**Target Resources**:
- Fleischman (1989): Tense and Narrativity
- Hopper (1979): Aspect and Foregrounding in Discourse
- Longacre (1983): Grammar of Discourse
- Martin (1992): English Text - System and Structure
- Journal of Translation, Journal of Linguistics

**Expected Duration**: 4-6 hours

**Success Criteria**:
- 10+ academic sources documented
- Cross-linguistic genre patterns identified
- ATTRIBUTION.md updated

---

### ⬜ Stage 4: Generate Proper Test Set (SUBAGENT REQUIRED)

**CRITICAL**: Use subagent to prevent seeing TBTA answers.

**Objective**: Extract TBTA data and create balanced test sets for all 9 genres.

**Tasks**:
- [ ] **Subagent 1**: Extract TBTA discourse genre data
  - [ ] Parse TBTA character-encoded data
  - [ ] Extract all verses with genre values
  - [ ] Create distribution analysis (verses per genre)
  - [ ] Identify genre coverage (which of 9 genres have data)
  - [ ] Note: Current sample shows only "Climactic Narrative Story"
- [ ] **Subagent 2**: Create balanced sample sets
  - [ ] Stratify by book type (narrative, epistle, poetic, prophetic, legal)
  - [ ] Stratify by testament (OT/NT proportional)
  - [ ] Include adversarial cases:
    - Genre boundaries (shifts within chapter)
    - Mixed genres (teaching within narrative)
    - Unusual genre (poetry in prophetic books)
  - [ ] Target: 100+ verses per genre (if available)
- [ ] **Subagent 3**: Split into train/test/validate
  - [ ] Train set: 40% (for algorithm refinement)
  - [ ] Test set: 30% (for iterative testing)
  - [ ] Validate set: 30% (for final blind validation)
  - [ ] Store in `experiments/train.yaml`, `test.yaml`, `validate.yaml`
- [ ] **Subagent 4**: Cross-linguistic validation prep
  - [ ] Identify Bible translations with explicit genre marking:
    - French (genre-specific tenses documented)
    - Japanese (genre registers in Bible translations)
    - Hebrew (genre comparison with source text)
  - [ ] Select 20 representative verses per language

**Data Limitation Contingency**:
- If TBTA has <9 genres: Document gaps, use linguistic theory for missing
- If only narrative: Validate algorithm on narrative, theorize others
- If mixed coverage: Prioritize validated genres, document confidence levels

**Expected Duration**: 6-8 hours

**Success Criteria**:
- TBTA data extracted and analyzed
- Test sets created (balanced as data allows)
- Main agent has NOT seen answers for test/validate
- Cross-linguistic validation prepared

---

### ⬜ Stage 5: Refine Prediction Algorithm

**Objective**: Test ALGORITHM-v1, analyze errors, create v2 with TBTA validation.

**Tasks**:
- [ ] Test ALGORITHM-v1 on `experiments/train.yaml`
  - [ ] Apply book-type classification rules
  - [ ] Check genre assignment accuracy
  - [ ] Document correct predictions
  - [ ] Document errors and edge cases
- [ ] Analyze errors using 6-step process:
  1. **Categorize**: Genre misclassification, book-type error, edge case?
  2. **Pattern**: Systematic (rule needs fixing) or random (acceptable variance)?
  3. **Rule vs Content**: Can fix with better rule, or needs content analysis?
  4. **Refinement**: Propose algorithm improvements
  5. **Test**: Validate refinements on subset
  6. **Iterate**: Repeat until 95%+ on train set
- [ ] Create ALGORITHM-v2:
  - [ ] Incorporate TBTA-validated patterns
  - [ ] Refine book-type classification
  - [ ] Add content analysis helpers where needed
  - [ ] Update confidence levels based on TBTA
  - [ ] Document changes from v1
- [ ] Test ALGORITHM-v2 on `experiments/test.yaml`
  - [ ] Subagent generates blind predictions
  - [ ] Subagent scores against TBTA
  - [ ] Return accuracy only (not individual results)
  - [ ] Iterate until 95%+ accuracy
- [ ] Create `experiments/ERROR-ANALYSIS.md`:
  - [ ] Document error patterns
  - [ ] Identify TBTA ambiguities
  - [ ] Note acceptable uncertainty ranges
- [ ] Git commit and lock v2 predictions before validate set

**Expected Duration**: 10-12 hours

**Success Criteria**:
- ALGORITHM-v2 achieves 95%+ on test set
- All error patterns documented
- Locked predictions in git history

---

### ⬜ Stage 6: Test Against Validate Set & Peer Review

**Objective**: Final validation on unseen data with multi-reviewer assessment.

**Tasks**:
- [ ] **Subagent 1** (Prediction): Generate blind predictions on `validate.yaml`
  - Use ALGORITHM-v2
  - NO access to TBTA values
  - Git commit predictions before scoring
- [ ] **Subagent 2** (Scoring): Score against TBTA
  - Return accuracy only
  - Break down by genre value
  - Identify systematic errors
- [ ] **Main agent**: Analyze errors
  - Review error patterns
  - Document TBTA ambiguities
  - Note cases requiring human judgment
- [ ] **Subagent 3** (Theological Reviewer): Check theological soundness
  - Verify narrative sections correctly marked
  - Check teaching passages (Sermon on Mount, parables)
  - Validate prophetic oracle marking
  - Ensure legal sections distinguished from narrative
- [ ] **Subagent 4** (Linguistic Reviewer): Check linguistic accuracy
  - Verify genre-tense correlations
  - Check language family requirements
  - Validate genre boundary detection
- [ ] **Subagent 5** (Methodological Reviewer): Verify rigor
  - Confirm blind prediction protocol
  - Check statistical validity
  - Review documentation completeness
- [ ] **Subagent 6** (Translation Practitioner): Real-world testing
  - Apply to actual translation work
  - Test with French Bible (genre-tense matching)
  - Test with Japanese Bible (register matching)
  - Document translation impact
- [ ] Create `experiments/TRANSLATOR-IMPACT.md`:
  - Before/after examples
  - Translation quality improvements
  - Remaining challenges
- [ ] Cross-linguistic validation:
  - [ ] French: Compare genre assignments to tense choices
  - [ ] Japanese: Compare to register usage
  - [ ] Hebrew: Compare NT genre to OT genre patterns
- [ ] Refine based on all reviewer feedback
- [ ] Mark production ready when:
  - [ ] Validate set accuracy ≥ 90%
  - [ ] All reviewers approve
  - [ ] Translation practitioner confirms utility
  - [ ] Cross-linguistic validation passes (2 languages minimum)

**Expected Duration**: 12-18 hours

**Success Criteria**:
- Validate set accuracy ≥ 90%
- All peer reviews pass
- Translation practitioner confirms improvement
- Cross-linguistic validation successful
- Production-ready status

---

## Success Metrics

### Stage-Specific

- **Stage 2**: Language families classified, top 10 languages have guides
- **Stage 3**: 10+ academic sources documented
- **Stage 4**: Test sets created (coverage documented if <9 genres)
- **Stage 5**: Test set accuracy ≥ 95%
- **Stage 6**: Validate set accuracy ≥ 90%, all reviews pass

### Overall Feature

- **Coverage**: All available genres testable
- **Accuracy**: 90%+ on unseen data
- **Utility**: Translation practitioner confirms genre-tense improvement
- **Documentation**: Complete README, experiments, algorithm, learnings
- **Cross-linguistic**: 2+ languages validated

---

## Risks and Mitigation

### Risk: TBTA Data Incomplete (Currently 1/9 Genres)
- **Impact**: Cannot validate 8 of 9 genre values
- **Mitigation**: Document coverage, use linguistic theory, mark confidence low for unvalidated

### Risk: Genre Ambiguity
- **Impact**: Some passages genuinely ambiguous (teaching in narrative frame)
- **Mitigation**: Document acceptable ranges, mark boundary cases, allow multiple genres

### Risk: Book-Type Oversimplification
- **Impact**: Books have mixed genres (Pentateuch = narrative + legal)
- **Mitigation**: Algorithm handles mixed classifications, refine based on TBTA

### Risk: Language-Specific Variation
- **Impact**: Genre marking varies widely across languages
- **Mitigation**: Create family-specific guides, document obligatory vs optional

---

## Notes for Next Researcher

**Key Insights from Experimental Work**:

1. **Genre is THE gateway feature** - determines grammaticality in 150+ languages
2. **Tense-genre correlation is 90%+** - knowing genre predicts tense reliably
3. **Strong predictors**: Illocutionary force > tense > participant tracking
4. **French is the test case**: Clear genre-tense restrictions, use for validation
5. **Hebrew wayyiqtol is genre-specific**: ONLY narrative, grammatically impossible elsewhere

**Critical Files**:
- README.md: Feature documentation
- experiments/EXPERIMENT1.md: Matthew 24 analysis (48% teaching, 24% prophetic, 12% narrative)
- training/ALGORITHM-v1.md: Prediction algorithm with confidence levels
- training/PATTERNS-LEARNED.md: 10 critical discoveries about genre
- training/CRITICAL-FINDING.md: TBTA data gap (1/9 genres observed)

**TBTA Data Status**:
- Observed: "Climactic Narrative Story" only (100% of sample)
- Expected: 9 genre values (Climactic, Background, Procedural, Expository, Poetic, Hortatory, Prophetic, Legal, Epistolary)
- Coverage: 11% (1/9 validated)
- Algorithm approach: Use TBTA where available, linguistic theory elsewhere

**Next Immediate Action**:
Stage 2 - Language study in `/languages/families/` to document genre-tense systems.

**Testing Priority**:
French Bible (genre-tense explicit) > Japanese (genre-register) > Hebrew (compare source text genre)

---

**Last Updated**: 2025-11-15
**Stage**: 1 Complete → 2 Next
**Researcher**: Claude Code Agent
**Experimental Work**: Available in /experiments/ and /training/
