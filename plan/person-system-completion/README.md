# Person-System Feature Completion Plan

**Feature**: person-system (clusivity)
**Start Date**: 2025-11-16
**Assigned Agent**: Hive Mind Feature Developer
**Status**: Stage 5 → Stage 6 completion

## Archive Status Assessment

### What Archive Completed
- ✅ Stages 1-3: Research, language study, scholarly analysis
- ✅ Stage 4: Training data (20 verses), test data (21 verses)
- ✅ Stage 5 (partial): Algorithms v1.0, v2.0, v2.1, v2.2 developed
- ✅ External validation: 98% agreement (9 languages, 7 verses)
- ✅ Locked predictions methodology established

### What Archive Left Incomplete
- ❌ Algorithm v2.2 (PROMPT4.md): **UNTESTED** despite "production ready" claim
- ❌ validate.yaml: **DOES NOT EXIST** (need 100 verses per value = 200 total)
- ❌ Stage 6: **NOT STARTED** (blind validation, 4 peer reviews)
- ❌ Random test failure: 50-60% (below 80-90% target) - needs root cause analysis

## Completion Strategy

### Phase 1: Test v2.2 Algorithm (2 hours)
**Goal**: Verify PROMPT4.md achieves claimed 81% accuracy

**Subagent Task**:
- Apply PROMPT4.md (v2.2) to test.yaml (21 verses)
- Compare predictions with TBTA values
- Calculate accuracy, identify errors
- Document results in `/plan/person-system-completion/v2.2-test-results.md`

**Success Criteria**: ≥80% accuracy (17/21 correct)

### Phase 2: Generate Validate Set (3 hours)
**Goal**: Create 200-verse validation set via blind subagent

**CRITICAL**: Main agent must NOT see validate.yaml contents

**Subagent Task**:
- Access TBTA data repository at `.data/`
- Run `extract_feature.py --field "Person" --max-per-value 100`
- Sample 100 Inclusive + 100 Exclusive verses
- Stratify by: OT/NT, genre, book distribution
- Include adversarial cases (quoted speech, nested references)
- Create `experiments/validate.yaml`
- Return ONLY file path to main agent (no contents)

**Success Criteria**: 200 verses with balanced distribution

### Phase 3: Blind Validation (2 hours)
**Goal**: Test best algorithm on validate set without seeing answers

**Subagent 1 (Predictor)**:
- Read validate.yaml
- Apply best algorithm (v2.2 or refined)
- Generate predictions file
- Lock predictions with git commit
- Return ONLY predictions file path

**Subagent 2 (Scorer)**:
- Load validate.yaml (has TBTA answers)
- Load predictions file
- Calculate accuracy (overall, by value)
- Identify error verse references (NO DETAILS)
- Return: accuracy % + error refs only

**Main Agent**:
- Receive accuracy report
- Analyze error patterns (without seeing answers)
- Decide: proceed or iterate

**Success Criteria**: ≥95% accuracy for production readiness

### Phase 4: Peer Review (8 hours, parallel)
**Goal**: 4 critical reviews assuming junior wrote this

**Subagent 3 (Theological Reviewer)**:
- Review algorithm for theological soundness
- Check: Divine speech, prayer, Trinity references handled correctly?
- Test edge cases: Does Rule 2.1 respect God's transcendence?
- Document findings in `/person-system/peer-reviews/theological-review.md`

**Subagent 4 (Linguistic Reviewer)**:
- Review algorithm for clusivity theory compliance
- Check: Definitions match Comrie, Cysouw, linguistic literature?
- Test: Does algorithm handle discourse roles (speaker/addressee)?
- Document findings in `/person-system/peer-reviews/linguistic-review.md`

**Subagent 5 (Methodological Reviewer)**:
- Check sample sizes (200 validate + 20 train + 21 test = adequate?)
- Verify locked predictions (git commits present?)
- Review blind testing integrity
- Check 6-step error analysis rigor
- Document findings in `/person-system/peer-reviews/methodological-review.md`

**Subagent 6 (Translation Practitioner)**:
- Test algorithm with 2-3 person-marking languages
- Pick 10 verses from validate set
- Translate using TBTA clusivity data
- Document: What helped? What confused? Mistakes avoided/made?
- Create `/person-system/peer-reviews/translator-impact.md`

**Success Criteria**: All 4 reviews passed with non-material feedback only

### Phase 5: Integration & Documentation (3 hours)
**Goal**: Finalize all documentation and production status

**Tasks**:
- Integrate peer review feedback
- Update README.md with final accuracy
- Document methodology in consolidated form
- Create production readiness report
- Update hive memory with learnings

## Timeline

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| 1. Test v2.2 | 2 hrs | Archive data |
| 2. Generate validate | 3 hrs | Phase 1 passes |
| 3. Blind validation | 2 hrs | Phase 2 complete |
| 4. Peer reviews (4x parallel) | 8 hrs | Phase 3 passes |
| 5. Integration | 3 hrs | Phase 4 complete |
| **Total** | **18 hrs** | Sequential + parallel |

## Success Metrics

### Accuracy Targets
- ✅ Test set (21 verses): ≥80% (v2.2 claims 81%)
- ✅ Validate set (200 verses): ≥95% (production threshold)
- ✅ External validation: ≥90% (already 98% on 7 verses)

### Peer Review
- ✅ Theological: No doctrinal errors
- ✅ Linguistic: Theory-compliant
- ✅ Methodological: Rigorous testing
- ✅ Practitioner: Net benefit positive

### Documentation
- ✅ All experiments/ files complete
- ✅ README.md production status
- ✅ Peer review findings integrated
- ✅ Hive learnings documented

## Risks & Mitigations

### Risk 1: v2.2 fails to meet 80%
**Mitigation**: Iterate to v2.3 using error analysis

### Risk 2: Validate set accuracy <95%
**Mitigation**: Refine algorithm, expand training set

### Risk 3: Peer reviews identify critical flaws
**Mitigation**: Iterate Stage 5, re-test

## Current Status

- [x] Archive data copied to working directory
- [ ] Phase 1: Test v2.2
- [ ] Phase 2: Generate validate.yaml
- [ ] Phase 3: Blind validation
- [ ] Phase 4: Peer reviews (4x)
- [ ] Phase 5: Integration

**Next Action**: Spawn subagent to test v2.2 on test.yaml
