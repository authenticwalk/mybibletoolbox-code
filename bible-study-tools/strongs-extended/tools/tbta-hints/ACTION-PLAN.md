# TBTA Hints - Action Plan for STAGES.md v2.0 Compliance

**Based on:** AUDIT-REPORT.md (2025-11-15)
**Current Status:** Stage 1 (Planning Complete, Experiments Pending)
**Target Status:** Stage 8 (Production-Ready)
**Timeline:** 4-6 months

---

## Current Situation

### What Exists ✅

1. **Architecture** (METHODOLOGY.md, LOGIC-TREE.md)
   - 5-step LLM logic tree well-designed
   - Scalable to all 14,197 Strong's words
   - Clear validation framework

2. **Planning Documents** (/plan)
   - Comprehensive feature analysis
   - Cost-benefit calculations
   - LLM integration strategies
   - Risk analysis

3. **Tool Infrastructure**
   - Directory: `/bible-study-tools/strongs-extended/tools/tbta-hints/`
   - METHODOLOGY.md: LLM-based approach documented
   - LOGIC-TREE.md: Visual decision flow
   - METRICS.md: Expected metrics (not yet validated)

### What's Missing ❌

1. **No experiments conducted** - 0 runs (need 60-103 per STAGES.md)
2. **Only 1 approach designed** - need 3 for strategic validation
3. **Test set incomplete** - 3 words planned, need 30-50 (stratified)
4. **METRICS.md overstates** - claims "TESTED" without evidence
5. **No experiments/ directory** - will be created after experiments run

---

## Action Plan (Phased Approach)

### Phase 1: Prepare for Experimentation (2 weeks)

**Priority 1: Correct METRICS.md Status** (1 hour)

Update `/bible-study-tools/strongs-extended/tools/tbta-hints/METRICS.md`:

```yaml
# Change from:
Status: 🔄 TESTED (3 pronouns tested across 20 verses)

# Change to:
Status: 📋 PLANNED (Architecture designed, experiments pending)

# Move accuracy claims to:
Expected_Impact_After_Validation:
  Overall: "+7% expected (planning analysis, not validated)"
  Note: "Experimental validation required before production deployment"
```

---

**Priority 2: Design 2 Additional Approaches** (1 week)

Create: `/bible-study-tools/strongs-extended/tools/tbta-hints/APPROACHES.md`

**Document 3 approaches:**

**Approach A: Statistical Clustering**
```yaml
Name: "Language Family Pattern Extraction"
Hypothesis: "Languages in same family make similar translation choices"
Method:
  1. Group TBTA translations by language family (Austronesian, Indo-European, etc.)
  2. Calculate family-level pattern frequencies
  3. Extract systematic alternations (e.g., "kami" vs "tayo" in Austronesian)
  4. Apply patterns to new translations based on family membership
Data_Sources:
  - TBTA database (900+ translations)
  - Ethnologue language families
Output_Format: Family-level hint templates with frequency distributions
Expected_Strengths:
  - Fast (rule-based, no LLM calls)
  - Predictable (statistical patterns)
  - Explainable (clear family clustering)
Expected_Weaknesses:
  - Misses context-dependent patterns
  - Assumes family homogeneity (may not hold)
  - Manual rule creation for each feature
```

**Approach B: Contextual Correlation**
```yaml
Name: "Biblical Context-Driven Hints"
Hypothesis: "Biblical context (genre, theology) predicts translation better than language family"
Method:
  1. Categorize verses by theological context (Trinity, ecclesiology, etc.)
  2. Analyze translation patterns within each category
  3. Generate context-conditional hints (if Trinity → exclusive, if unity → inclusive)
  4. Apply hints based on verse context matching
Data_Sources:
  - TBTA database (900+ translations)
  - Verse metadata (genre, theological themes, cross-refs)
Output_Format: Context-conditional hint rules
Expected_Strengths:
  - Captures theological nuance
  - Context-aware predictions
  - Handles edge cases (Trinity, unity passages)
Expected_Weaknesses:
  - Requires manual context categorization
  - May miss language-specific patterns
  - Context classification subjective
```

**Approach C: Hybrid LLM (Current)**
```yaml
Name: "LLM-Based Logic Tree"
Hypothesis: "LLMs synthesize patterns better than rule-based systems"
Method: 5-step LLM logic tree (see METHODOLOGY.md)
Data_Sources: 900+ TBTA translations
Output_Format: LLM-generated YAML with confidence scores
Expected_Strengths:
  - Adaptive pattern recognition
  - Handles complexity (context + language + theology)
  - Self-calibrating confidence
Expected_Weaknesses:
  - Token cost (2000-3000 tokens per analysis)
  - Less predictable than rules
  - Requires prompt engineering
```

---

**Priority 3: Develop Stratified Test Set** (1 week)

Create: `/bible-study-tools/strongs-extended/tools/tbta-hints/TEST-SET.md`

**Build test set meeting STAGES.md v2.0 requirements:**

```yaml
Total_Words: 30-50 Strong's words
Stratification_Requirements:
  By_Frequency:
    Rare (<10 occurrences): 10-15 words
      - G5387 (φιλόστοργος) - "tenderly affectionate" (1×)
      - G4862 (σύν) - rare preposition (4×)
      - G4863 (συνάγω) - "gather together" (8×)
      # ... 7-12 more rare words

    Medium (50-500 occurrences): 15-20 words
      - G3778 (οὗτος) - "this" (demonstrative, 1,380×)
      - G1565 (ἐκεῖνος) - "that" (demonstrative, 265×)
      - G3756 (οὐ) - negative particle (1,606×)
      # ... 12-17 more medium-frequency words

    High (1000+ occurrences): 5-10 words
      - G2249 (ἡμεῖς) - "we" (864×)
      - G846 (αὐτός) - "he/she/it" (5,597×)
      - G3588 (ὁ) - article (19,783×)
      # ... 2-7 more high-frequency words

  By_Word_Type:
    Pronouns: 40% (12-20 words) - highest cross-linguistic variation
    Demonstratives: 30% (9-15 words) - clear proximity patterns
    Particles: 30% (9-15 words) - polarity, mood, aspect

  Adversarial_Cases (30% of total):
    Controversial_Theology:
      - G2249 (ἡμεῖς) in Trinity passages (Gen 1:26, 3:22, 11:7)
      - G5207 (υἱός) "son" - adoptionist vs eternal sonship debates

    Lexicon_Divergence:
      - G3778 vs G1565 - proximity systems vary by language (2-way, 3-way, 9-way)
      - G3756 (οὐ) vs G3361 (μή) - negation polarity, genre-dependent

    Rare_Usage_Contexts:
      - Trial number (exactly 3 persons) - Hawaiian lākou patterns
      - 4th person/obviative - Navajo, Algonquian distinctions

    Cultural_Sensitivity:
      - G2316 (θεός) "God" - translation in Islamic contexts
      - G4151 (πνεῦμα) "Spirit" - animism concerns

Selection_Protocol:
  1. Spawn subagent to select test words (main agent blind to criteria)
  2. Subagent receives stratification requirements only
  3. Main agent receives word list WITHOUT metadata (no frequencies shown)
  4. Prevents bias toward "easy" words
  5. Test words NOT used in documentation until validation complete
```

**Document stratification matrix:**

| Word | Frequency | Type | Adversarial? | Reason |
|------|-----------|------|--------------|--------|
| G2249 | High (864×) | Pronoun | Yes | Clusivity + Trinity theology |
| G3778 | Medium (1,380×) | Demonstrative | Yes | Proximity divergence |
| G5387 | Rare (1×) | Adjective | No | Low-frequency test case |
| ... | ... | ... | ... | ... |

---

### Phase 2: Round 1 - Strategic Testing (3 weeks)

**Execute STAGES.md v2.0 Round 1:**

**2.1 Run All 3 Approaches on Small Sample**

```yaml
Experiment_Design:
  Approaches: 3 (Statistical, Contextual, LLM)
  Words_Per_Approach: 3-5 (diverse: pronoun, demonstrative, particle)
  Total_Runs: 9-15 (3 approaches × 3-5 words)

Execution:
  For_Each_Approach:
    - Create approach-specific instructions
    - Test on 3-5 diverse words
    - Save outputs: {word}.strongs-tbta-hints-approach{A|B|C}.yaml

  Parallel_Processing:
    - Run all 9-15 combinations
    - Track time per word per approach
    - Document source access methods
```

**Example words for Round 1:**
- G2249 (ἡμεῖς) - "we" (clusivity patterns, theological)
- G3778 (οὗτος) - "this" (proximity, demonstrative)
- G3756 (οὐ) - negative particle (polarity)
- G1473 (ἐγώ) - "I" (surface realization, pro-drop)
- G1565 (ἐκεῖνος) - "that" (proximity, distance)

---

**2.2 Source Access Optimization**

Document for each approach:

| Approach | Primary Source | Access Method | URL Pattern | Scalability |
|----------|----------------|---------------|-------------|-------------|
| Statistical | TBTA database | Direct query | N/A (local database) | Excellent |
| Contextual | TBTA + metadata | WebFetch | verse metadata endpoints | Good |
| LLM | TBTA translations | API calls | 900+ translation API | Good (rate limits) |

**Prioritize:** Approaches with predictable, scalable access methods

---

**2.3 Initial Broad Review Committee**

**Spawn 8-10 specialized reviewers:**

1. **Linguistic Accuracy Reviewer**
   - Questions: "Are language family groupings correct?", "Are proximity distinctions accurate?"

2. **Cross-Linguistic Validator**
   - Questions: "Do patterns hold across 50+ language families?", "Are cognates identified correctly?"

3. **Theological Context Reviewer**
   - Questions: "Are Trinity contexts identified?", "Is clusivity theologically justified?"

4. **Source Reliability Reviewer**
   - Questions: "Can all translations be accessed?", "Are TBTA citations correct?"

5. **AI Usability Reviewer**
   - Questions: "Is YAML schema consistent?", "Are inline citations present?"

6. **Pattern Convergence Reviewer**
   - Questions: "Do 3+ languages agree on pattern?", "Are divergences documented?"

7. **Confidence Calibration Reviewer**
   - Questions: "Do confidence scores match evidence?", "Are low-confidence cases flagged?"

8. **Edge Case Validator**
   - Questions: "Are trial number cases handled?", "Are 4th person patterns documented?"

9. **Cultural Sensitivity Reviewer**
   - Questions: "Are translation sensitivities noted?", "Are Islamic context concerns addressed?"

10. **Data Completeness Reviewer**
    - Questions: "Are all required YAML fields populated?", "Are skip decisions justified?"

**Track effectiveness:**

| Reviewer | Questions Asked | Issues Found | Effectiveness Score |
|----------|----------------|--------------|---------------------|
| Linguistic Accuracy | 8 | ? | (Issues / Questions) |
| Cross-Linguistic | 8 | ? | ... |
| ... | ... | ... | ... |

---

**2.4 Apply 3-Level Validation**

**Level 1 (CRITICAL - 100% Pass):**
- ✅ No fabricated translations (every example from TBTA corpus)
- ✅ Inline citations: `{lang-code}: "translation word"`
- ✅ Confidence scores justified (evidence-based)
- ✅ All sources documented (TBTA corpus cited)

**Level 2 (HIGH - Track Improvement):**
- ✅ Language family groupings accurate (Austronesian, Indo-European, etc.)
- ✅ Pattern consistency documented (5/5 vs 3/5 agreement)
- ✅ Theological context categorization appropriate
- ✅ Counter-examples documented (not hidden)

**Level 3 (MEDIUM - Track Improvement):**
- ✅ Cross-linguistic validation (50+ families checked)
- ✅ Confidence calibration validated (0.95 = 95% actual accuracy)
- ✅ Edge cases analyzed (trial number, 4th person)
- ✅ Limitations acknowledged

**Track baseline pass rates:**

| Approach | L1 Pass | L2 Pass | L3 Pass |
|----------|---------|---------|---------|
| Statistical | ?% | ?% | ?% |
| Contextual | ?% | ?% | ?% |
| LLM | ?% | ?% | ?% |

---

**2.5 Cross-Approach Evaluation**

**Create comparison table:**

| Criterion | Statistical | Contextual | LLM | Winner |
|-----------|------------|------------|-----|--------|
| Quality Score (avg /10) | ? | ? | ? | ? |
| L2 Pass Rate | ?% | ?% | ?% | ? |
| Time per word | ? min | ? min | ? min | ? |
| Source Accessibility | Excellent | Good | Good | ? |
| Scalability | High | Medium | High | ? |
| Review Issues Found | ? | ? | ? | ? |

**Decision Point:**
- **Clear Winner:** One approach 2+ points higher → Proceed to Rounds 2-5 with winner only
- **Complementary:** Multiple approaches excel at different word types → Blend best elements
- **All Insufficient:** All <7/10 average → Generate 3 NEW approaches, return to Round 1
- **Split Needed:** Incompatible value propositions → Split into multiple tools

---

### Phase 3: Rounds 2-5 - Refinement (8-12 weeks)

**Goal:** Refine WINNING approach until diminishing returns (<5% improvement)

**2.1 Round 2: Prompt/Method Refinement** (2-3 weeks)
- Analyze Round 1 failures
- Refine instructions to address L1, L2, L3 gaps
- Re-run 10-15 test words
- Track improvement (target: +7-15% on L2/L3)

**2.2 Round 3: Context Engineering** (2-3 weeks)
- Word type classification (theological vs grammatical)
- Coverage sweet spots (optimize depth)
- Re-run 10-15 words
- Track improvement (target: +5-10% on L2/L3)

**2.3 Round 4: Edge Case Handling** (2-3 weeks)
- Focus on adversarial test cases (30% of test set)
- Apply error correction frameworks
- Re-run adversarial words
- Track improvement (target: +5% on L3)

**2.4 Round 5: Review Committee (Continued)** (2-3 weeks)
- Continue using full 8-10 reviewer committee
- Track which reviewers find which issues
- Calculate reviewer effectiveness scores
- Prepare for optimization (Rounds 7-8)

**Stopping Rule:**
- Stop when BOTH L2 and L3 improvements <5% for consecutive round
- Example: Round 4 (+3.5% L2, +5.9% L3) → Round 5 (+2.3% L2, +2.8% L3) = **STOP**

---

### Phase 4: Rounds 6-9 - Optimization (6-8 weeks)

**6.1 Round 6: Winner Selection** (if multiple approaches refined)
- Compare all refined approaches
- Select clear winner or blend

**6.2 Rounds 7-8: Review Committee Optimization** (3-4 weeks)
- Remove low-value reviewers (0 issues found)
- Keep high-value reviewers (high issue detection rate)
- Focus questions (80 questions → 7 focused questions)
- Re-run 5-10 words with optimized committee

**6.3 Round 9: Schema/Instruction Optimization** (2-3 weeks)
- Remove unnecessary YAML fields
- Simplify instructions
- Optimize source list
- Test on 5-10 random words
- Ensure quality maintained (8.5+/10)

---

### Phase 5: Production Validation (4-6 weeks)

**7.1 Level 4 Usefulness Validation** (2-3 weeks)

**Role-play 3 practitioner scenarios:**

**Bible Translator:**
- Would you copy this to translation notes? (Yes/No)
- What data helped translation decisions?
- What mistakes did this help avoid?

**Pastor:**
- Would you use in sermon prep? (Yes/No)
- What insights for congregation?
- What was too technical/academic?

**Seminary Student:**
- Would you cite in exegetical paper? (Yes/No)
- Are sources credentialed enough?
- What strengthened your argument?

**Target:** 70%+ would use outputs in at least one scenario

---

**7.2 Full Validation Suite** (2-3 weeks)
- Apply validation to ALL 30-50 test words
- Run optimized review committee
- Adversarial testing (not just easy cases)
- Verify usefulness metrics (70%+)

**7.3 Measure Success Metrics**
- Level 1: 100% pass
- Level 2: Diminishing returns reached
- Level 3: Diminishing returns reached
- Level 4: 70%+ usefulness
- Time per word tracked
- Coverage validated

**7.4 Document Final Methodology**
- Create production-ready METHODOLOGY.md
- Select 2-3 stellar examples for publication
- Document known limitations
- Provide time estimates

---

### Phase 6: Create experiments/ Structure (After Completion)

**Only create after experiments run:**

```
/bible-study-tools/strongs-extended/tools/tbta-hints/
├── METHODOLOGY.md (updated with final approach)
├── LOGIC-TREE.md (updated)
├── METRICS.md (updated with actual data)
├── APPROACHES.md (3 approaches comparison)
├── TEST-SET.md (stratified test set)
├── AUDIT-REPORT.md (this audit)
├── ACTION-PLAN.md (this plan)
└── experiments/
    ├── round-01-strategic-testing/
    │   ├── approach-a-statistical/
    │   │   ├── G2249-kami-tayo-pattern.yaml
    │   │   ├── validation-report.md
    │   │   └── ...
    │   ├── approach-b-contextual/
    │   │   └── ...
    │   ├── approach-c-llm/
    │   │   └── ...
    │   └── cross-approach-evaluation.md
    ├── rounds-02-05-refinement/
    │   ├── round-02-prompt-refinement/
    │   ├── round-03-context-engineering/
    │   ├── round-04-edge-cases/
    │   └── round-05-review-committee/
    ├── rounds-06-09-optimization/
    │   ├── round-06-winner-selection.md
    │   ├── rounds-07-08-committee-optimization/
    │   └── round-09-schema-optimization/
    └── production-validation/
        ├── level-4-usefulness-testing/
        ├── full-validation-suite/
        └── final-methodology/
            ├── stellar-examples/
            └── production-METHODOLOGY.md
```

---

## Planning Documents Status

### Keep in /plan (Archive Reference)

**Files:**
- `/plan/tbta-strongs-hints-approach.md` (32 KB - comprehensive planning)
- `/plan/tbta-strongs-hints-evaluation.md` (feature analysis)
- `/plan/tbta-strongs-hints-limitations.md` (risk analysis)
- `/plan/tbta-strongs-hints-llm-enhancement.md` (LLM integration)
- `/plan/tbta-strongs-hints-summary.md` (27 KB - executive summary)

**Status:** ✅ Excellent planning documents, keep for reference

**Note:** These are **planning phase** documents, not experimental results. They should remain in `/plan` as historical context for decision-making.

**Do NOT:**
- Move to experiments/ (they're not experiments)
- Delete (valuable analysis and reasoning)
- Claim as "experimental validation" (they're theoretical analysis)

---

## Timeline Summary

| Phase | Duration | Deliverable | STAGES.md Stage |
|-------|----------|-------------|-----------------|
| **Phase 1: Preparation** | 2 weeks | APPROACHES.md, TEST-SET.md, updated METRICS.md | Stage 1.3-1.4 |
| **Phase 2: Round 1** | 3 weeks | 9-15 experiments, cross-approach evaluation | Stage 2 |
| **Phase 3: Rounds 2-5** | 8-12 weeks | Refined approach, diminishing returns reached | Stage 3 |
| **Phase 4: Rounds 6-9** | 6-8 weeks | Optimized methodology, committee refined | Stages 4-6 |
| **Phase 5: Production** | 4-6 weeks | Validated methodology, stellar examples | Stages 7-8 |
| **Phase 6: Structure** | 1 week | experiments/ directory created | Documentation |
| **TOTAL** | **24-31 weeks (6-8 months)** | Production-ready tool | All stages |

---

## Success Criteria

### Per STAGES.md v2.0:

**Stage 1 (Preparation):**
- ✅ 3 approaches designed with clear hypotheses
- ✅ 30-50 word test set (stratified by frequency, type, adversarial)
- ✅ Blind subagent test set selection

**Stage 2 (Round 1):**
- ✅ 9-15 runs across 3 approaches
- ✅ Source access optimization documented
- ✅ 8-10 reviewer committee effectiveness tracked
- ✅ Winner selected (clear winner, blend, or new approaches)

**Stage 3 (Rounds 2-5):**
- ✅ Refinement to diminishing returns (<5% improvement)
- ✅ 20-45 runs total
- ✅ L2/L3 at natural quality ceiling

**Stages 4-6 (Optimization):**
- ✅ Review committee optimized (8-10 → 3-4 reviewers)
- ✅ Schema/instructions streamlined
- ✅ Quality maintained (8.5+/10)

**Stages 7-8 (Production):**
- ✅ 100% Level-1 validation
- ✅ Level-2/3 at diminishing returns
- ✅ 70%+ Level-4 usefulness validation
- ✅ 2-3 stellar examples published
- ✅ Methodology reproducible

---

## Next Steps (Immediate)

### Week 1:
1. Update METRICS.md status (1 hour)
2. Create APPROACHES.md with 3 approaches (3 days)
3. Review APPROACHES.md with stakeholders

### Week 2:
1. Create TEST-SET.md with stratified test set (3 days)
2. Spawn subagent for blind test word selection (1 day)
3. Finalize test set (30-50 words documented)

### Week 3-5:
1. Execute Round 1 (9-15 experiments)
2. Apply 3-level validation
3. Run review committee (8-10 reviewers)
4. Cross-approach evaluation
5. Select winner or blend

### Weeks 6+:
1. Proceed to Rounds 2-5 if winner identified
2. OR generate 3 new approaches if all insufficient
3. Continue through production validation

---

**Action Plan Complete**
**Status:** Ready for execution (pending stakeholder approval)
**Next Review:** After Phase 1 complete (APPROACHES.md, TEST-SET.md created)
