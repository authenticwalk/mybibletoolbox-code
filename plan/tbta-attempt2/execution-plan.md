# TBTA Feature Execution Plan - Attempt 2

## Executive Summary

**Total Features**: 59 (across 15 categories)
**Current Status**: 19 features with experiments (32%), 50 documented (85%)
**Completion Target**: All Tier A features (19 features) → 100% experiment coverage
**Strategy**: 3-phase phased approach with parallel execution

---

## Current State Analysis

### Completed Features (✅ 19 total)
**Tier A** (13/19 = 68%):
- Number System, Person System, Participant Tracking, Proximity System
- Time Granularity, Aspect, Mood
- Speaker Demographics (6 features: Speaker, Listener, Attitude, Age, Age Relationship, Speech Style)
- Illocutionary Force, Discourse Genre

**Tier B** (3/20 = 15%):
- Noun List Index, Surface Realization, Polarity

**Tier C** (0/20 = 0%): None yet

### Priority Gaps (Need experiments)

**Tier A Missing** (6 features):
1. Semantic Role (NP) - Medium complexity
2. Topic NP (Clause) - Medium complexity
3. Salience Band (Clause) - High complexity (discourse-level)
4. Notional Structure (Clause) - Not fully documented
5. Alternative Analysis (Clause) - Not fully documented
6. Clause Type (Clause) - Medium complexity

**Tier B Missing** (17 features):
- Clause features: Implicit Information, Rhetorical Question, Sequence, Location in Discourse
- Phrase features: Relativized, Usage, Implicit flags
- Word features: Lexical Sense (multiple), Degree, Reflexivity

---

## Complexity & Dependency Analysis

### Complexity Classification

#### Simple (Grammatical/Lexical) - 3-5 days per feature
**Characteristics**: Word-level, morphological markers, limited context needed

1. **Degree** (Adj/Adv) - Comparative/superlative detection
2. **Reflexivity** (Verb) - Self-reference identification
3. **Clause Type** (Clause) - Declarative/interrogative/imperative
4. **Polarity** (already done, but template available)
5. **Adposition Lexical Sense** (Prep) - Case marking
6. **Conjunction Lexical Sense** (Conj) - Logical relationships
7. **Particle Types** (Particle) - Quote markers, focus, topic

#### Medium (Discourse-Sensitive) - 7-10 days per feature
**Characteristics**: Phrase-level, some context, multiple factors

8. **Semantic Role** (NP) - Agent/Patient/Theme identification
9. **Topic NP** (Clause) - Topic identification
10. **Rhetorical Question** (Clause) - Question type classification
11. **Implicit Information** (multiple) - Cultural/situational gaps
12. **Usage** (AdjP) - Attributive/predicative/substantive
13. **Sequence** (multiple phrase types) - Ordering in discourse
14. **Location in Discourse** (Clause) - Positional markers
15. **Relativized** (NP) - Relative clause marking

#### High (Multi-Dimensional) - 10-15 days per feature
**Characteristics**: Discourse-level, chapter context, theological nuance

16. **Salience Band** (Clause) - Foreground/background hierarchy
17. **Notional Structure** (Clause) - Semantic clause relationships
18. **Alternative Analysis** (Clause) - Multiple valid interpretations
19. **Participant Status** (Noun) - Activation states
20. **Evidentiality** (may be complex) - Source of information

### Dependency Map

**No dependencies** (can start immediately):
- All simple grammatical features (Degree, Reflexivity, Clause Type)
- Lexical Sense features (Adposition, Conjunction, Verb)

**Requires discourse context** (need discourse strategy first):
- Salience Band → requires discourse strategy decision
- Participant Status → builds on Participant Tracking (done)
- Notional Structure → builds on Clause Type

**Requires multiple features** (save for Phase 3):
- Alternative Analysis → requires other clause features complete
- Implicit Information → builds on Semantic Role, Topic NP

---

## 3-Phase Execution Strategy

### Phase 1: Quick Wins (Simple Features) - 4 weeks
**Goal**: Establish patterns, build confidence, create templates
**Batch Size**: 3-4 features in parallel
**Resources**: 4 agents (1 per feature)

#### Batch 1.1 (Week 1-2): Tier A Grammatical
1. **Clause Type** (Tier A) - PRIORITY
   - Complexity: Simple
   - Dependencies: None
   - Impact: Essential for translation
   - Sample availability: High (every verse)

2. **Degree** (Tier B) - Has existing analysis
   - Complexity: Simple
   - Dependencies: None
   - Impact: Important for comparison
   - Sample availability: Medium (adjectives/adverbs only)

3. **Reflexivity** (Tier B)
   - Complexity: Simple
   - Dependencies: None
   - Impact: Specialized but clear rules
   - Sample availability: Low (reflexive contexts)

#### Batch 1.2 (Week 3-4): Tier B Lexical
4. **Adposition Lexical Sense** (Tier B)
   - Complexity: Simple
   - Dependencies: None
   - Impact: Case marking for languages
   - Sample availability: High

5. **Conjunction Lexical Sense** (Tier B)
   - Complexity: Simple
   - Dependencies: None
   - Impact: Logical connectors
   - Sample availability: High

6. **Particle Types** (Tier B)
   - Complexity: Simple
   - Dependencies: None
   - Impact: Focus/topic marking
   - Sample availability: Medium

**Phase 1 Outcome**: 6 new features complete, templates refined, patterns documented

---

### Phase 2: Build Momentum (Medium Features) - 6 weeks
**Goal**: Tackle discourse-sensitive features, apply learnings
**Batch Size**: 2-3 features in parallel (more complex, need focus)
**Resources**: 6 agents (2 per feature for quality)

#### Batch 2.1 (Week 5-6): Tier A Priorities
1. **Semantic Role** (Tier A) - CRITICAL
   - Complexity: Medium
   - Dependencies: None (but benefits from Clause Type)
   - Impact: Essential for case languages
   - Sample availability: High (every NP)

2. **Topic NP** (Tier A) - CRITICAL
   - Complexity: Medium
   - Dependencies: Semantic Role (parallel OK)
   - Impact: Essential for topic-prominent languages
   - Sample availability: Medium

#### Batch 2.2 (Week 7-8): Tier B Context Features
3. **Rhetorical Question** (Tier B)
   - Complexity: Medium
   - Dependencies: Clause Type, Illocutionary Force
   - Impact: Important for question handling
   - Sample availability: Medium

4. **Usage** (AdjP) (Tier B)
   - Complexity: Medium
   - Dependencies: None
   - Impact: Adjective function
   - Sample availability: Medium

#### Batch 2.3 (Week 9-10): Tier B Discourse Features
5. **Sequence** (multiple: NP, VP, AdjP, AdvP) (Tier B)
   - Complexity: Medium
   - Dependencies: None
   - Impact: Word order for flexible languages
   - Sample availability: High
   - Note: Can do all 4 phrase types in parallel (same methodology)

6. **Location in Discourse** (Clause) (Tier B)
   - Complexity: Medium
   - Dependencies: None
   - Impact: Discourse markers
   - Sample availability: High

7. **Relativized** (NP) (Tier B)
   - Complexity: Medium
   - Dependencies: None
   - Impact: Relative clause handling
   - Sample availability: Medium

**Phase 2 Outcome**: 10 new features complete (7 distinct + 4 Sequence variants)

---

### Phase 3: Complex Features (Apply All Learnings) - 8 weeks
**Goal**: Complete Tier A, tackle multi-dimensional features
**Batch Size**: 1-2 features in parallel (very complex)
**Resources**: 8-10 agents (4-5 per feature: research, coding, validation, review)

#### Batch 3.1 (Week 11-13): Tier A Critical Gap - Salience Band
1. **Salience Band** (Tier A) - CRITICAL
   - Complexity: High
   - Dependencies: Discourse Genre, Clause Type
   - Impact: Essential for foreground/background
   - Sample availability: High
   - Strategy: Apply all discourse learnings
   - Special: May need discourse context decision first

#### Batch 3.2 (Week 14-16): Documentation Gaps
2. **Notional Structure** (Tier A gap)
   - Complexity: High
   - Dependencies: Clause Type, Semantic Role
   - Impact: Semantic clause relationships
   - Sample availability: High
   - Note: Need to document complete taxonomy first

3. **Alternative Analysis** (Tier A gap)
   - Complexity: High
   - Dependencies: Most other features (save for last)
   - Impact: Multiple interpretation support
   - Sample availability: Medium
   - Note: Requires mature understanding of annotation principles

#### Batch 3.3 (Week 17-18): Tier B/C Advanced
4. **Implicit Information** (Tier B)
   - Complexity: Medium-High
   - Dependencies: Semantic Role, Topic NP, Cultural knowledge
   - Impact: Important for explicitation
   - Sample availability: Medium
   - Note: Requires external cultural sources

5. **Participant Status** (Tier C)
   - Complexity: High
   - Dependencies: Participant Tracking
   - Impact: Specialized (activation theory)
   - Sample availability: Medium

**Phase 3 Outcome**: 5 more features complete, Tier A at 100%

---

## Parallel Execution Opportunities

### Highly Parallelizable (Can run simultaneously)
**Batch 1.1** (4 agents):
- Clause Type (Agent A)
- Degree (Agent B)
- Reflexivity (Agent C)
- Adposition Lexical Sense (Agent D)

**Sequence Features** (4 agents - same methodology, different data):
- NP Sequence (Agent A)
- VP Sequence (Agent B)
- AdjP Sequence (Agent C)
- AdvP Sequence (Agent D)

### Moderately Parallelizable (2-3 at once)
**Batch 2.1** (2 features, 4 agents):
- Semantic Role (Agents A+B for quality)
- Topic NP (Agents C+D for quality)

### Sequential (One at a time recommended)
**Complex Tier A**:
- Salience Band → Notional Structure → Alternative Analysis
- Reason: Each builds on learnings from previous

---

## Resource Allocation Recommendations

### Phase 1: Simple Features (4 agents per batch)
```
Batch 1.1:
- Agent A: Clause Type (researcher + coder)
- Agent B: Degree (researcher + coder)
- Agent C: Reflexivity (researcher + coder)
- Agent D: Adposition (researcher + coder)

Each agent:
- Week 1: Research + data generation + first prompt
- Week 2: Iteration + validation + documentation
```

### Phase 2: Medium Features (6 agents per batch)
```
Batch 2.1 (Tier A priorities):
- Agents A+B: Semantic Role (pair for quality)
  - Agent A: Research + prompt development
  - Agent B: Validation + error analysis
- Agents C+D: Topic NP (pair for quality)
  - Agent C: Research + prompt development
  - Agent D: Validation + error analysis
- Agents E+F: Stand ready for reviews
```

### Phase 3: Complex Features (8-10 agents per batch)
```
Batch 3.1 (Salience Band):
- Agent A: Researcher (discourse literature)
- Agent B: Data Engineer (test set generation)
- Agent C: Prompt Engineer (methodology development)
- Agent D: Validator (blind testing)
- Agent E: Theological Reviewer
- Agent F: Linguistic Reviewer
- Agent G: Methodological Reviewer
- Agent H: Translation Practitioner
```

---

## Optimal Batch Sizes

### Simple Features
- **Batch size**: 3-4 features
- **Duration**: 2 weeks per batch
- **Agents**: 1 agent per feature
- **Rationale**: Fast iteration, learn patterns quickly

### Medium Features
- **Batch size**: 2-3 features
- **Duration**: 2-3 weeks per batch
- **Agents**: 2 agents per feature (paired work)
- **Rationale**: More complexity needs collaboration

### High Features
- **Batch size**: 1-2 features
- **Duration**: 3-4 weeks per feature
- **Agents**: 4-5 agents per feature (research, code, validate, review x2)
- **Rationale**: Critical quality, extensive review needed

---

## Sample Size Requirements

Following STAGES.md requirements:

**All Features**:
- Minimum: 100 verses per value
- Distribution: 40% train, 30% test, 30% validate
- Balance: OT/NT proportional, genre diversity
- Adversarial: 30% challenging cases in test set

**Special Cases**:
- Low-frequency values (<50 verses total): Document limitation, lower targets
- High-frequency values (>1000 verses): Sample strategically, ensure diversity

---

## Success Criteria by Phase

### Phase 1 Success
- ✅ 6 simple features at 95%+ accuracy
- ✅ Template refinement documented
- ✅ Parallel execution patterns proven
- ✅ Cross-feature learnings updated

### Phase 2 Success
- ✅ 10 medium features at 95%+ accuracy (including 4 Sequence variants)
- ✅ Discourse strategies validated
- ✅ Tier A at 85%+ completion (18/19 or better)
- ✅ Translation practitioner validation complete for 5+ features

### Phase 3 Success
- ✅ 5 complex features at 95%+ accuracy
- ✅ Tier A at 100% completion (19/19)
- ✅ All documentation gaps filled
- ✅ TBTA review communication for challenging features
- ✅ Production readiness checklist complete for all Tier A

---

## Risk Mitigation

### Risk 1: Low Sample Size
**Features affected**: Reflexivity, Relativized, some Particle types
**Mitigation**:
- Identify sample size during research phase
- If <50 verses: Document limitation, adjust accuracy targets
- Consider combining related values if theologically sound

### Risk 2: Discourse Context Dependency
**Features affected**: Salience Band, Participant Status, Notional Structure
**Mitigation**:
- Complete discourse strategy decision in /plan/tbta-rebuild-with-llm/discourse/ first
- Test discourse approach with Salience Band (Phase 3.1)
- Apply learnings to remaining discourse features

### Risk 3: Theological Complexity
**Features affected**: Alternative Analysis, Implicit Information
**Mitigation**:
- Engage theological reviewer early
- Check with TBTA team for annotation philosophy
- Document valid perspective differences

### Risk 4: Documentation Gaps
**Features affected**: Notional Structure, Alternative Analysis, Vocabulary Alternate
**Mitigation**:
- Research TBTA source documentation first
- May need to contact TBTA team for clarification
- Document what's discovered for future users

---

## Coordination Protocol

### Swarm Memory Keys

**Feature Status**:
- `hive/phase1/batch1-status` → Progress on Batch 1.1
- `hive/phase1/batch2-status` → Progress on Batch 1.2
- `hive/phase2/batch{n}-status` → Phase 2 progress
- `hive/phase3/batch{n}-status` → Phase 3 progress

**Learnings**:
- `hive/learnings/simple-features` → Patterns from Phase 1
- `hive/learnings/medium-features` → Patterns from Phase 2
- `hive/learnings/complex-features` → Patterns from Phase 3

**Templates**:
- `hive/templates/simple-feature-template` → Refined from Phase 1
- `hive/templates/medium-feature-template` → Refined from Phase 2
- `hive/templates/complex-feature-template` → Refined from Phase 3

### Daily Standups (Async)
Each agent stores progress:
```yaml
agent: {agent-id}
feature: {feature-name}
phase: {phase-number}
day: {day-of-phase}
status: {on-track | blocked | needs-review}
blockers: [list]
learnings: [list]
next: {what's next}
```

---

## Timeline Summary

| Phase | Duration | Features | Outcome |
|-------|----------|----------|---------|
| **Phase 1** | 4 weeks | 6 simple | Quick wins, templates |
| **Phase 2** | 6 weeks | 10 medium | Momentum, discourse |
| **Phase 3** | 8 weeks | 5 complex | Tier A complete |
| **TOTAL** | **18 weeks** | **21 features** | **40 total (68%)** |

**Tier A Completion**: Week 16 (100% of 19 critical features)
**Overall Completion**: 40/59 features (68%) → 19 current + 21 new

---

## Recommended Next Actions

1. **Immediate** (This week):
   - ✅ Review this execution plan
   - [ ] Decide on discourse strategy (if not done) → See /plan/tbta-rebuild-with-llm/discourse/OVERVIEW.md
   - [ ] Initialize swarm for Phase 1, Batch 1.1
   - [ ] Spawn 4 agents for Clause Type, Degree, Reflexivity, Adposition

2. **Week 1**:
   - [ ] Agents complete Stage 1-3 (Research, Language Study, Scholarly Research)
   - [ ] Generate test sets (Stage 4) via subagents
   - [ ] Daily progress updates to swarm memory

3. **Week 2**:
   - [ ] Agents complete Stage 5 (Hypothesis, First Prompt, Iteration)
   - [ ] Lock predictions, validate against test sets
   - [ ] Error analysis using 6-step process

4. **Week 3-4**:
   - [ ] Complete Stage 6 (Validate set, Peer Review)
   - [ ] Launch Batch 1.2 (parallel with reviews)
   - [ ] Update CROSS-FEATURE-LEARNINGS.md

5. **Month 2** (Phase 2):
   - [ ] Apply Phase 1 templates to medium features
   - [ ] Focus on Tier A priorities (Semantic Role, Topic NP)
   - [ ] Translation practitioner validation for completed features

---

## Success Metrics

### Quantitative
- **Accuracy**: 95%+ on validate sets (100 verses minimum)
- **Coverage**: 100% Tier A (19 features) by Week 16
- **Documentation**: 100% features with README.md
- **Experiments**: 40+ features with experiment directories

### Qualitative
- **Template Quality**: Refined through 3 phases
- **Cross-Feature Learnings**: Comprehensive patterns documented
- **Translation Impact**: Positive feedback from practitioner testing
- **TBTA Alignment**: High agreement on annotation philosophy

---

## Appendix: Feature Quick Reference

### Tier A (Essential) - 19 features
**Completed (13)**:
- Number, Person, Participant Tracking, Proximity, Time Granularity
- Aspect, Mood, Illocutionary Force, Discourse Genre
- Speaker, Listener, Speaker Attitude, Speaker Age, Speaker-Listener Age, Speech Style

**Phase 1-2 (3)**:
- Clause Type, Semantic Role, Topic NP

**Phase 3 (3)**:
- Salience Band, Notional Structure, Alternative Analysis

### Tier B (Important) - 20 features
**Completed (3)**:
- Noun List Index, Surface Realization, Polarity

**Phase 1 (3)**:
- Degree, Adposition Lexical Sense, Conjunction Lexical Sense

**Phase 2 (7)**:
- Rhetorical Question, Usage, Sequence (x4), Location in Discourse, Relativized

**Phase 3 (1)**:
- Implicit Information

**Not Scheduled Yet (6)**:
- Lexical Sense (Verb), Reflexivity (moved to Phase 1), Target T/A/M, Participant Types

### Tier C (Nice-to-Have) - 20 features
**Phase 3 (1)**:
- Participant Status

**Not Scheduled (19)**:
- Remaining specialized features (Noun Classifiers, Directionals, etc.)

---

**Created**: 2025-11-16
**Version**: 1.0
**Status**: Ready for review and execution
