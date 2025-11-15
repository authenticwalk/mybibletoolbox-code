# Strong's Extended Enrichment: Production Workflow (STAGES)

**Status:** Production-Ready Methodology
**Based on:** 80+ experiments across lexicon-core, web-insights, and TBTA-hints tools
**Last Updated:** 2025-11-14
**Quality Standard:** 100% Level-1 validation, 80%+ Level-2, 60%+ Level-3

---

## Overview: Single-Tool-to-Completion Methodology

**CRITICAL PRINCIPLE:** Take ONE tool to full production readiness before starting the next.

This workflow synthesizes proven methodologies from `/plan/strongs-enrichment-tools/` experiments:
- **80+ documented experiments** across 4 improvement cycles
- **7+ proven best practices** validated across theological, grammatical, and rare words
- **3-level validation framework** ensuring zero fabrication and fair-use compliance
- **Multi-discipline search strategy** discovering specialized coverage (e.g., virtue ethics)

---

## Proven Best Practices (From /plan Research)

### 1. Word Type Classification Drives Strategy

**Source:** `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/EXPERIMENTS-COMPARISON.md`

**Discovery:** Word type matters MORE than frequency for extraction value.

**Classification Matrix:**

| Word Type | Frequency | Coverage Pattern | Strategy |
|-----------|-----------|------------------|----------|
| **Theological** | Very Rare (1-10) | **High** (significance > frequency) | Full extraction, LSJ emphasis, confidence markers |
| **Theological** | Medium (50-500) | **Very High** (richest data tier) | Full extraction, 5-8 categories, TDNT/Trench |
| **Grammatical** | Ultra-High (1000+) | **Low** (functional, minimal lexical) | Statistics-focused, morphology primary |

**Evidence:**
- G5287 ὑπόστασις (5 occurrences, theological): ~35 data points, MOST EXTENSIVE LSJ
- G0846 αὐτός (5,597 occurrences, pronoun): ~15 data points, HELPS absent
- **Ratio:** Rare theological term has **2.3x MORE data** than ultra-high-frequency grammatical term

---

### 2. Convergence & Divergence Patterns (Fair Use)

**Source:** `/plan/strongs-enrichment-tools/01-lexicon-core/research/convergence-patterns.md`

**Discovery:** Fair use requires convergence grouping vs divergence in comparative context.

**Convergence (When 3+ Lexicons Agree):**
```yaml
etymology:
  derivation: "From δύναμαι (to be able) {strongs} {thayer} {helps} {abbott-smith}"
  convergence_note: "Etymology consistent across all major Greek lexicons"
  confidence: "HIGH"
```

**Divergence (When Lexicons Disagree):**
```yaml
lexical_divergence:
  - semantic_area: "Classical to Koine semantic development"
    classical_usage:
      definition: "physical strength, force" {lsj-abridged}
      context: "Plato, Aristotle"
    koine_usage:
      definition: "miraculous power, divine ability" {thayer} {helps}
      context: "New Testament usage"
```

---

### 3. 90% Coverage Sweet Spot (Pareto Optimal)

**Source:** `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/cycle-04/`

**Discovery:** Morphological coverage sweet spot = 90% (not 100%).

**Evidence:**
- **100% coverage** (Cycle 2): 15 min for 49 forms
- **85% coverage** (Cycle 3): 8 min for 10 forms
- **90% coverage** (Cycle 4): 10 min for 15 forms

**ROI:** Cycle 4 achieves 37% time savings with 2% quality loss

---

### 4. Multi-Discipline Search Strategy

**Source:** `/plan/strongs-enrichment-tools/03-web-insights/experiments/EXPERIMENTS-COMPLETE-SUMMARY.md`

**Discovery:** Coverage is discipline-specific. Rare words may excel in specialized disciplines.

**Case:** G2160 εὐτραπελία (hapax) - Found 12 sources in **virtue ethics** discipline

**Search Disciplines:**
1. Bible Study Platforms
2. Theological Disciplines
3. Linguistic Analysis
4. Translation Practitioner
5. Specialist Disciplines (philosophy, ethics, cultural studies)

---

### 5. 5-Part Error Correction Structure

**Source:** `/plan/strongs-enrichment-tools/03-web-insights/experiments/exp4-error-correction/`

**Structure:**
1. **Error Statement** - Clear, non-mocking
2. **Classification** - Name fallacy type
3. **Multi-Layered Refutation** - Minimum 4 evidence types
4. **Expert Validation** - Authority pyramid (2+ sources, 1 HIGH/VERY HIGH)
5. **Correct Alternative** - Better methodology, biblical usage

**Tone:** Gracious, pedagogical (explain WHY wrong, teach methodology)

---

### 6. Multi-Perspective Framework

**Source:** `/plan/strongs-enrichment-tools/03-web-insights/experiments/exp5-cultural-debate/`

**For scholarly disagreements:**
- Document all major positions fairly
- Each position: advocates, arguments, strengths, considerations
- **Bias Detection Tests** (all 3 must pass):
  1. Reversal Test
  2. Respect Test
  3. Evidence Test

**Key:** Tool equips translators to navigate debates, not resolve them

---

### 7. 3-Level Validation Framework

**Source:** `/plan/strongs-enrichment-tools/01-lexicon-core/validation/quality-checklist.md`

**Level 1: CRITICAL (Must Pass 100%)**
- No fabricated data
- Inline citations: `content {source}`
- No percentages/numeric predictions
- Base file read FIRST
- All sources in ATTRIBUTION.md

**Level 2: HIGH PRIORITY (Must Pass 80%+)**
- Etymology from 2+ lexicons
- Semantic categories appropriate for frequency
- Usage statistics match sources exactly
- Convergence/divergence documented

**Level 3: MEDIUM PRIORITY (Must Pass 60%+)**
- Cross-reference codes extracted
- Diachronic analysis when relevant
- Fair use compliant
- Related words documented

**Decision Matrix:**

| L1 | L2 | L3 | Decision |
|----|----|----|----------|
| <100% | - | - | **REJECT** |
| 100% | <80% | - | **REVIEW** |
| 100% | 80-89% | 60%+ | **ACCEPT** |
| 100% | 90%+ | 80%+ | **EXCELLENT** |

---

## Stage-by-Stage Workflow

### STAGE 1: Tool Selection & Scoping (2-3 hours)

**Process:**
1. Select ONE tool for full production
2. Read schema/README
3. Identify word classification strategy
4. Select 5 diverse test words

**Output:** Tool selected, test words chosen

---

### STAGE 2: Initial Experiments (Cycle 1) (8-12 hours)

**Process:**
1. For each test word:
   - Read base Strong's file FIRST
   - Execute extraction per schema
   - Apply validation checklist
   - Document learnings

2. Document patterns (what worked, failed, time)

**Output:** 5 initial outputs, documented learnings

---

### STAGE 3: Methodology Refinement (Cycle 2-4) (12-20 hours)

**Cycle 2:** Prompt refinement
**Cycle 3:** Context engineering
**Cycle 4:** Edge case handling

**Apply proven patterns:**
- Word type classification
- Convergence/divergence
- 90% coverage sweet spot
- Multi-discipline search
- 5-part error correction
- Multi-perspective framework
- 3-level validation

**Output:** Refined methodology, improved outputs, time optimizations

---

### STAGE 4: Schema & Template Finalization (Cycle 5) (4-6 hours)

**Process:**
1. Adjust schema based on experiments
2. Create templates:
   - Standard extraction
   - Error correction (5-part)
   - Multi-perspective (bias detection)
   - Skip decision
3. Update validation checklist

**Output:** Finalized schema, 4 templates, validation checklist

---

### STAGE 5: Peer Review (Cycle 6) (6-8 hours)

**Process:**
1. Subagent review (external evaluator)
2. Expert spot-check
3. Implement feedback

**Output:** Peer review report, updated outputs

---

### STAGE 6: Production Validation (Cycle 7) (4-6 hours)

**Process:**
1. Run full validation (L1: 100%, L2: 80%+, L3: 60%+)
2. Measure success metrics
3. Document final methodology

**Output:** Validation report, success metrics, production-ready docs

---

### STAGE 7: Production Deployment (Ongoing)

**Process:**
1. Prioritize words (high/medium/low priority)
2. Execute systematically with templates
3. Monitor quality, iterate if needed

**Stopping Rule:** <5% gain per cycle (diminishing returns)

**Output:** Production outputs at scale

---

## Cross-Applicable TBTA Techniques

From `/bible-study-tools/tbta/features/STAGES.md`:

1. **Locked Predictions** - Commit before checking sources (prevents bias)
2. **6-Step Error Analysis** - Rigorous debugging (verify, re-analyze, test hypotheses)
3. **Subagent Blind Validation** - Never see answers during development
4. **Critical Peer Review** - 4 adversarial subagents (theological, linguistic, methodological, practitioner)
5. **Adversarial Test Sets** - Edge cases, ambiguity, controversial scholarship
6. **Translation Impact Testing** - Role-play actual translator scenarios
7. **Progressive Disclosure** - README ≤200 lines, topics ≤400 lines

---

## Tool-Specific Applications

### Lexicon-Core
- Word type classification
- 90% morphology coverage
- Skip controversy for grammatical
- Genre distribution for high-freq

**Time:** Grammatical 47 min, Theological 59 min

### Web-Insights
- Multi-discipline search
- 5-part error correction
- Multi-perspective framework
- Bias detection

**Time:** Standard 2-3h, Error correction 4-5h, Multi-perspective 5-6h

### TBTA-Hints
- Pattern extraction 900+ translations
- Confidence calibration
- Language family clustering

**Success:** +7% overall accuracy, +25% edge case accuracy

---

## Success Metrics

**Per Tool:**
- 100% Level-1 validation
- 80%+ Level-2 validation
- 60%+ Level-3 validation
- Methodology documented
- Stellar examples published

**Production:**
- Zero fabrication
- All sources credentialed/cited
- Fair-use compliant
- Time targets met
- Coverage validated

---

## Common Pitfalls (From 80+ Experiments)

1. Not reading Tool 1 first → Duplication
2. Single-discipline search → Missing specialized coverage
3. Forcing rare word content → Fabrication
4. Skipping word classification → Wrong strategy
5. Incomplete error corrections → No teaching value
6. Biased multi-perspective → Fail bias tests
7. 100% morphology pursuit → Pareto sub-optimal
8. Unverified credentials → Can't assign authority
9. Multiple tools parallel → Context overload, no production quality

---

## Timeline

**Per Tool:** 6-9 weeks to production
**Sequential:** 18-27 weeks for 3 tools at production quality

**Production Deployment:**
- High-priority (~300): 8-12 weeks
- Medium (~800): 20-30 weeks
- Low (~400): 10-15 weeks

---

## References

**Source Documents:**
- `/plan/strongs-comprehensive-strategy.md` - Strategic overview
- `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/EXPERIMENTS-COMPARISON.md` - Word type patterns
- `/plan/strongs-enrichment-tools/01-lexicon-core/research/` - Convergence, extraction methods
- `/plan/strongs-enrichment-tools/01-lexicon-core/validation/quality-checklist.md` - Validation framework
- `/plan/strongs-enrichment-tools/03-web-insights/RESEARCHER-WORKFLOW.md` - Production workflow
- `/plan/strongs-enrichment-tools/03-web-insights/experiments/EXPERIMENTS-COMPLETE-SUMMARY.md` - 5 adversarial experiments

**Key Models:**
- G5287 (rare theological): Confidence markers, LSJ emphasis
- G846 (ultra-high grammatical): 90% coverage, skip optimizations
- G1411 (error correction): 5-part structure, authority pyramid
- G4151 (multi-perspective): Scholarly disagreement, bias detection
- G1577 (cultural debate): Post-colonial sensitivity, decision frameworks

**Total Research Base:** 80+ experiments, 6,361 lines of methodology

---

**Research Completion:** TODO-1 (CRITICAL) ✅ COMPLETE
**Last Updated:** 2025-11-14
