# TBTA Master Gap Analysis
**Date**: 2025-11-15
**Analyst**: Code Review Agent
**Scope**: 14 TBTA features comprehensive TODO review

---

## Executive Summary

**Total Features Analyzed**: 14
**Critical Blockers**: 2 (Person System, Mood)
**Stage 6 Needed**: 3 (Person System, Mood, Aspect)
**Stage 5 Needed**: 1 (Participant Tracking)
**Stage 4 or Earlier**: 8 features
**Production-Ready**: 2 (Degree, Honorifics-Register)

**Estimated Total Work**: 115-172 hours (15-22 weeks at 1 feature/week pace)

---

## Critical Blockers (Stage 6 Required)

### 1. Person System - HIGHEST PRIORITY ⛔
**Current Status**: Stage 5 incomplete (71% accuracy v2.1, needs v2.2)
**Blocker Type**: Algorithm refinement + validate.yaml generation
**Impact**: Foundation for clusivity systems in 1000+ languages

**Immediate Actions**:
- [ ] Implement Algorithm v2.2 (strict Rule 2.1 trigger) - 2 hours
- [ ] Re-test on 21-verse set (target: 81%+) - 2 hours
- [ ] **USE SUBAGENT** to generate validate.yaml (100 inclusive + 100 exclusive) - 2 hours
- [ ] Proceed to Stage 6 blind validation - 8-10 hours

**Blockers**:
1. ✅ Algorithm v2.1 tested → 71.4% (FAILED 75-80% target)
2. 🔴 Algorithm v2.2 needs implementation
3. 🔴 No validate.yaml (Stage 6 blocker)

**Timeline**: 14-16 hours (1 week)
**Dependencies**: None
**Resource Needs**: Subagent for validate.yaml (blind generation)

---

### 2. Mood - HIGH PRIORITY 🟡
**Current Status**: Stage 6 validation needed (94.62% on Matthew 24)
**Blocker Type**: Comprehensive Stage 6 completion
**Impact**: Modal systems in 150+ languages

**Immediate Actions**:
- [ ] Create train/test/validate split from Matthew 24 - 2 hours
- [ ] Subagent blind testing on validate.yaml - 2 hours
- [ ] 4 peer reviews (theological, linguistic, methodological, practitioner) - 4-6 hours
- [ ] Create TRANSLATOR-IMPACT.md - 2 hours

**Outstanding Issues**:
1. Limited test corpus (Matthew 24 only, 316 verbs)
2. Rare mood coverage (optative: 0 examples, subjunctive: rare)
3. Hebrew modal system differs from Greek (may need separate tree)

**Timeline**: 10-12 hours
**Dependencies**: None
**Resource Needs**: 4 peer reviewers in parallel

---

### 3. Aspect - MEDIUM PRIORITY 🟡
**Current Status**: Stage 5 documentation incomplete (98.1% accuracy)
**Blocker Type**: Documentation before Stage 6
**Impact**: Aspectual systems worldwide

**Immediate Actions**:
- [ ] Create experiments/LEARNINGS.md (error analysis) - 4 hours
- [ ] Complete EXTERNAL-VALIDATION.md (Russian, Mandarin, Arabic) - 4 hours
- [ ] Update ../learnings/README.md (multi-factor convergence) - 2 hours
- [ ] Justify 98.1% optimality - 2 hours
- [ ] Proceed to Stage 6 - 12-20 hours

**Outstanding Issues**:
1. Small test sample (54 verbs, 10 verses from Matthew 24)
2. Missing rare aspects (perfective, progressive, iterative, cessative, completive: 0 examples)
3. Missing LEARNINGS.md documentation

**Timeline**: 24-32 hours
**Dependencies**: None
**Resource Needs**: Translation data for external validation

---

## Stage 5 Required (Testing & Refinement)

### 4. Participant Tracking - MEDIUM PRIORITY
**Current Status**: Stage 4 complete (90% v1.0), v2.0 designed but untested
**Blocker Type**: v2.0 validation on NEW test set
**Impact**: Foundation for switch-reference languages (200+ languages)

**Immediate Actions**:
- [ ] Select NEW test set (cannot reuse 12 verses from error analysis) - 2 hours
- [ ] Apply Algorithm v2.0 blindly (lock predictions) - 2 hours
- [ ] Calculate accuracy (target: 80%+ production, 85%+ ideal) - 1 hour
- [ ] Decision: v2.1 refinement or proceed to Stage 6 - varies

**Outstanding Issues**:
1. Cannot test v2.0 on same 12 verses (introduces bias)
2. Participant extraction incompleteness (50-70% under-count)
3. Frame database incomplete (7 frames, need 200+)
4. Presupposition database minimal (4 entities)

**Timeline**: 5-15 hours (depends on v2.0 results)
**Dependencies**: None
**Resource Needs**: Subagent for blind testing

---

## Stage 4 or Earlier (Test Set Generation)

### 5. Number System - Stage 2 Complete
**Current Status**: Language study complete, Stage 3 next
**Timeline**: 18-30 hours (Stages 3-6)
**Dependencies**: None

**Critical Gap**: Dual usage patterns (0% validation accuracy)

---

### 6. Proximity System - Stage 2 In Progress
**Current Status**: Language families identified, value mapping incomplete
**Timeline**: 22-34 hours (Stages 2-6)
**Dependencies**: None

**Critical Gaps**:
1. Visibility inference rules (R vs r)
2. Person-oriented distinction (S vs L)
3. Hebrew contextual inference (unmarked זֶה)

---

### 7. Discourse Genre - Stage 1 Complete
**Current Status**: Documentation complete, Stage 2 next
**Timeline**: 30-50 hours (Stages 2-6)
**Dependencies**: None

**Critical Finding**: Only 1/9 genres validated in TBTA (11% coverage)

---

### 8. Time Granularity - Stage 1 Complete
**Current Status**: Comprehensive documentation, Stage 2 next
**Timeline**: 28-46 hours (Stages 2-6)
**Dependencies**: None

**Impact**: Obligatory in 725+ languages across 11 families

---

## Experimentation Complete (Needs Validation)

### 9. Illocutionary Force - Experiment Complete
**Current Status**: 70-90% accuracy by category, blind validation needed
**Timeline**: 20-30 hours
**Dependencies**: None

**Next Steps**: Create validate set (100+ verses), blind testing, register refinement

---

### 10. Surface Realization - Research Complete
**Current Status**: 95% correlation with Participant Tracking documented
**Timeline**: 10-20 hours
**Dependencies**: Participant Tracking (95% correlation)

**Key Insight**: Gateway feature - predictable from Participant Tracking state

---

### 11. Topic NP - Documentation Complete
**Current Status**: Methodology documented, translation validation needed
**Timeline**: 15-25 hours
**Dependencies**: Participant Tracking (95% correlation), Surface Realization

**Validation Method**: Compare TBTA with Japanese wa/ga, Korean eun/neun, Mandarin topic-comment

---

### 12. Polarity - Training Set Complete
**Current Status**: Algorithm development needed
**Timeline**: 12-20 hours
**Dependencies**: None

**Target**: <5% error rate (binary feature, should be high accuracy)

---

## Production-Ready

### 13. Degree - COMPLETE ✅
**Current Status**: Algorithm v2.0 validated (71% expected accuracy)
**Next Steps**: Full validate set (100+ verses), production deployment
**Timeline**: 5-10 hours (production readiness)

**Key Achievement**: 4 universal principles discovered

---

### 14. Honorifics-Register - COMPLETE ✅
**Current Status**: Production-ready documentation complete
**Next Steps**: Tool implementation, language-specific testing
**Timeline**: 20-30 hours (implementation)

**6 Features**: Speaker, Listener, Attitude, Age, Age Relationship, Speech Style

---

## Dependency Graph

```
┌─────────────────────────────────────────┐
│ FOUNDATIONAL FEATURES (No Dependencies) │
└─────────────────────────────────────────┘
│
├─ Person System ⛔ (Stage 5 → 6)
├─ Mood 🟡 (Stage 6)
├─ Aspect 🟡 (Stage 5 → 6)
├─ Number System (Stage 2 → 6)
├─ Proximity System (Stage 2 → 6)
├─ Discourse Genre (Stage 1 → 6)
├─ Time Granularity (Stage 1 → 6)
├─ Illocutionary Force (Validation)
├─ Polarity (Algorithm Development)
├─ Degree ✅
└─ Honorifics-Register ✅
    │
    ▼
┌──────────────────────────────────────┐
│ DEPENDENT FEATURES                   │
└──────────────────────────────────────┘
│
├─ Participant Tracking (Stage 5)
│   │
│   ├─ Depends on: Person System (optional enhancement)
│   │
│   └─> ENABLES:
│       ├─ Surface Realization (95% correlation)
│       └─ Topic NP (95% correlation)
│
├─ Surface Realization (Research → Validation)
│   └─ Depends on: Participant Tracking (95% correlation)
│       │
│       └─> ENABLES: Topic NP refinement
│
└─ Topic NP (Documentation → Validation)
    └─ Depends on: Participant Tracking, Surface Realization
```

---

## Prioritization Recommendations

### Phase 1: Clear Critical Blockers (2-3 weeks)
**Priority**: Highest impact, blocking production

1. **Person System** (14-16 hours)
   - Algorithm v2.2 → 81%+ accuracy
   - Generate validate.yaml
   - Complete Stage 6

2. **Mood** (10-12 hours)
   - Complete Stage 6 validation
   - 4 peer reviews

3. **Aspect** (24-32 hours)
   - Complete Stage 5 documentation
   - Stage 6 validation

**Subtotal**: 48-60 hours

---

### Phase 2: High-Value Features (4-6 weeks)
**Priority**: Near completion, high language impact

4. **Participant Tracking** (5-15 hours)
   - Validate v2.0 on NEW test set
   - Stage 6 if successful

5. **Illocutionary Force** (20-30 hours)
   - Blind validation
   - Register refinement

6. **Surface Realization** (10-20 hours)
   - Test 95% correlation claim
   - Production validation

7. **Polarity** (12-20 hours)
   - Algorithm development
   - Testing (target: <5% error)

**Subtotal**: 47-85 hours

---

### Phase 3: Foundation Features (6-10 weeks)
**Priority**: Obligatory in 200-700+ languages, need complete workflow

8. **Number System** (18-30 hours)
   - Stages 3-6

9. **Proximity System** (22-34 hours)
   - Complete Stage 2 → Stage 6

10. **Time Granularity** (28-46 hours)
    - Stages 2-6

11. **Discourse Genre** (30-50 hours)
    - Stages 2-6

**Subtotal**: 98-160 hours

---

### Phase 4: Dependent Features (2-4 weeks)
**Priority**: Depend on Phase 1-2 completion

12. **Topic NP** (15-25 hours)
    - Requires: Participant Tracking, Surface Realization
    - Translation validation

**Subtotal**: 15-25 hours

---

### Phase 5: Production Deployment (1-2 weeks)
**Priority**: Already complete, need tooling

13. **Degree** (5-10 hours)
    - Production deployment

14. **Honorifics-Register** (20-30 hours)
    - Tool implementation

**Subtotal**: 25-40 hours

---

## Resource Requirements

### Subagents Needed
1. **Person System**: Validate.yaml generation (blind)
2. **Participant Tracking**: v2.0 blind testing
3. **All Stage 4+ features**: Test set generation
4. **All Stage 6 features**: Blind validation, peer reviews

### External Resources
1. **Translation data**: Russian, Mandarin, Arabic (Aspect validation)
2. **Published Bibles**: Japanese, Korean, Mandarin, Tagalog (Topic NP)
3. **Language family data**: WALS, Glottolog queries
4. **Peer reviewers**: 4 per feature (theological, linguistic, methodological, practitioner)

---

## Timeline Estimates

| Phase | Features | Hours | Weeks (8h/day, 5d/wk) |
|-------|----------|-------|----------------------|
| **Phase 1** | Person, Mood, Aspect | 48-60 | 1.5-2 |
| **Phase 2** | Tracking, Force, Surface, Polarity | 47-85 | 1.5-2.5 |
| **Phase 3** | Number, Proximity, Time, Genre | 98-160 | 3-5 |
| **Phase 4** | Topic NP | 15-25 | 0.5-1 |
| **Phase 5** | Degree, Honorifics tooling | 25-40 | 1-1.5 |
| **TOTAL** | 14 features | **233-370 hours** | **7-12 weeks** |

**Best Case**: 7 weeks (1 feature/day pace)
**Realistic**: 10 weeks (slower, with reviews/iterations)
**Conservative**: 15-22 weeks (1 feature/week pace)

---

## Quick Wins (High ROI, Low Effort)

### 1. Person System v2.2 Refinement
**Effort**: 4 hours
**Impact**: Unblocks Stage 6, fixes 71% → 81% accuracy
**Next Action**: Implement strict Rule 2.1 trigger today

### 2. Mood Stage 6 Validation
**Effort**: 10-12 hours
**Impact**: Production-ready for 150+ languages
**Next Action**: Create train/test/validate split

### 3. Polarity Algorithm
**Effort**: 12-20 hours
**Impact**: Binary feature, should achieve >95% easily
**Next Action**: Create 5-level decision tree

---

## Risk Assessment

### High Risk 🔴
1. **Person System v2.2 may still fail** → Iterate to v2.3 (add 8-12 hours)
2. **Mood rare value coverage** → May need genre expansion (add 20+ hours)
3. **Participant Tracking v2.0 <80%** → Develop v3.0 (add 10-20 hours)

### Medium Risk 🟡
1. **TBTA data gaps** (Discourse Genre: 1/9 values, Number: 0% dual accuracy)
2. **Cross-feature dependencies** (Topic NP requires Tracking + Surface)
3. **Translation validation access** (need published Bibles in target languages)

### Low Risk 🟢
1. **Degree, Honorifics**: Already production-ready
2. **Polarity**: Binary feature, straightforward
3. **Illocutionary Force**: 70-90% already achieved

---

## Recommended Action Plan (Next 2 Weeks)

### Week 1: Critical Blockers
**Days 1-2**: Person System v2.2 + validate.yaml generation (14-16 hours)
**Days 3-4**: Mood Stage 6 validation (10-12 hours)
**Day 5**: Aspect LEARNINGS.md documentation (8 hours)

**Deliverable**: 3 features closer to production

---

### Week 2: High-Value Features
**Days 1-2**: Participant Tracking v2.0 validation (10-15 hours)
**Days 3-5**: Polarity algorithm development + testing (12-20 hours)

**Deliverable**: 2 more features tested/validated

---

## Gaps Summary by Category

### Data Gaps
1. **Discourse Genre**: 1/9 values (11% coverage)
2. **Number System**: 0% dual accuracy
3. **Mood**: 0 optative examples, rare subjunctive
4. **Aspect**: Missing rare aspects (perfective, progressive, etc.)

### Methodological Gaps
1. **Person System**: No validate.yaml (Stage 6 blocker)
2. **Participant Tracking**: Cannot reuse test set (bias issue)
3. **Number System**: Dual usage patterns unknown

### Dependency Gaps
1. **Surface Realization**: Needs Participant Tracking validation
2. **Topic NP**: Needs both Tracking + Surface
3. **Proximity System**: Hebrew inference rules undefined

### Documentation Gaps
1. **Aspect**: Missing LEARNINGS.md, EXTERNAL-VALIDATION.md
2. **All Stage 4+ features**: No test sets generated yet

---

## Success Metrics

### Feature-Level
- **Stage 6**: ≥90-95% accuracy on validate set
- **Stage 5**: ≥80-95% on test set (feature-dependent)
- **Stage 4**: Balanced train/test/validate created
- **Peer Reviews**: 4/4 passed (theological, linguistic, methodological, practitioner)

### Project-Level
- **14/14 features production-ready**: Within 15-22 weeks
- **Zero critical blockers**: Person System, Mood resolved by Week 2
- **Cross-feature integration**: Dependencies validated (Tracking → Surface → Topic NP)
- **Translation validation**: ≥2 languages per feature

---

## Notes for Feature Owners

### Person System
**Next Reviewer**: Implement v2.2, test on 21 verses, generate validate.yaml with subagent

### Mood
**Next Reviewer**: Split Matthew 24 into train/test/validate, run Stage 6 peer reviews

### Aspect
**Next Reviewer**: Complete LEARNINGS.md error analysis, external validation (Russian, Mandarin, Arabic)

### Participant Tracking
**Next Reviewer**: Select NEW test approach (adversarial/random/cross-validation), validate v2.0 blindly

### All Stage 1-3 Features
**Next Reviewer**: Follow STAGES.md workflow sequentially, use subagents for test generation

---

**Analysis Complete**: 2025-11-15
**Total Features**: 14
**Critical Path**: Person System → Mood → Aspect (48-60 hours)
**Estimated Completion**: 7-22 weeks depending on pace and iterations
