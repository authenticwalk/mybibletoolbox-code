# TBTA Feature Development Template

## Quick Start

**For new features**: Follow the authoritative 6-stage methodology in [STAGES.md](STAGES.md).

**For existing features**: Use [FEATURE-AUDIT-TEMPLATE.md](../../../plan/tbta-rebuild-with-llm/features/FEATURE-AUDIT-TEMPLATE.md) to assess compliance.

**Key principle**: Every feature must complete all 6 stages before production deployment.

---

## Directory Structure Standard

```
features/{feature-name}/
├── README.md                     (≤500 lines - feature overview + stage checklist)
│   ├── Purpose (50-100 lines)
│   ├── Methodology (200-300 lines, INLINE - no external refs)
│   ├── Output Schema (100-150 lines)
│   └── Related Features (50 lines)
├── experiments/
│   ├── train.yaml                (40% sample, 100+ verses per value)
│   ├── test.yaml                 (30% sample, adversarial cases)
│   ├── validate.yaml             (30% sample, blind testing)
│   ├── ANALYSIS.md               (up to 12 approaches comparison)
│   ├── PROMPT1.md                (first iteration)
│   ├── PROMPT2.md                (alternative approach)
│   ├── PROMPT3.md, ...           (refinements)
│   ├── LEARNINGS.md              (6-step error analysis)
│   ├── VALIDATION-RESULTS.md     (accuracy metrics)
│   ├── EXTERNAL-VALIDATION.md    (real translation checks - if applicable)
│   ├── CROSS-LINGUISTIC-VALIDATION.md  (Thesis approach - compare across languages)
│   ├── TRANSLATOR-IMPACT.md      (Stage 6 - real-world testing)
│   └── TBTA-REVIEW.md            (communication with TBTA team)
└── archive/                       (old iterations if migrated)
```

---

## Stage Checklist

Copy this abbreviated checklist into your feature README.md (see [STAGES.md](STAGES.md) for complete details):

### Stage 1: Research TBTA Documentation
- [ ] Review official TBTA docs for this feature
- [ ] Review existing feature analysis
- [ ] Generate README.md with feature definition + stage checklist

### Stage 2: Language Study
- [ ] Identify which language families need this feature
- [ ] Determine where feature is grammatically obligatory vs optional
- [ ] Update README.md with language analysis + target scenarios

### Stage 3: Scholarly and Internet Research
- [ ] Find scholarly articles on this subject
- [ ] Research general web information
- [ ] Update README.md with latest findings

### Stage 4: Generate Test Set with Translation Data (USE SUBAGENT - don't see answers!)
- [ ] **Philosophy**: Discover answers from what real translators did (not just TBTA validation)
- [ ] Sample size: 100+ verses per value minimum (statistical power)
- [ ] Balanced: OT/NT proportional, multiple genres, books, typical + adversarial
- [ ] **Translation Language Selection**:
  - [ ] Identify language families that grammatically mark this feature (from Stage 2)
  - [ ] Build translation database (5-10 representative translations)
  - [ ] Document in experiments/TRANSLATION-DATABASE.md
- [ ] **Dual Output Strategy**: Generate BOTH answer sheets (TBTA) AND question sheets (translations)
  - [ ] Use extract_feature.py for TBTA data (answer sheets)
  - [ ] Subagent samples with stratification + selects representative translations
  - [ ] Generate question sheets with real translation texts (NO TBTA values visible)
- [ ] Split: train (40%), test (30%), validate (30%)
- [ ] Store: train.yaml + train_questions.yaml, test.yaml + test_questions.yaml, validate.yaml + validate_questions.yaml

### Stage 5: Analyze Translations & Develop Algorithm
- [ ] **Translation Discovery Analysis** (primary source - use train_questions.yaml):
  - [ ] For each verse: Identify feature value from real translations
  - [ ] Check translation consensus (80%+ agreement = strong signal)
  - [ ] Document patterns in experiments/TRANSLATION-PATTERNS.md
  - [ ] Compare with TBTA values (train.yaml):
    - Translations AGREE with TBTA (90%+ cases) → High confidence
    - Translations DISAGREE → Investigate in DIVERGENCE-ANALYSIS.md
    - Translations UNCLEAR → Rely on TBTA (lower confidence)
- [ ] Create experiments/ANALYSIS.md (up to 12 approaches, weight translation + TBTA evidence)
- [ ] **First Prompt Development**:
  - [ ] Create experiments/PROMPT1.md with most likely approach
  - [ ] **LOCK PREDICTIONS** with git commit before checking TBTA
  - [ ] Apply to test set, record commit SHA in LEARNINGS.md
- [ ] **Success Criteria**: 100% accuracy for stated values (with sufficient sample ≥100)
- [ ] **Systematic Error Analysis** (6-step process for EVERY error):
  - [ ] Verify data accuracy, re-analyze source text + context
  - [ ] Cross-reference 3+ translations, consult commentaries (cite per ATTRIBUTION.md)
  - [ ] Test hypotheses: Why did algorithm fail?
  - [ ] Final determination: Is TBTA correct? Valid perspective? Potential annotation error?
- [ ] **Iterative Refinement**:
  - [ ] PROMPT2.md (different approach), PROMPT3+.md (refine winning approach)
  - [ ] Each iteration: Lock predictions → Test → Analyze errors → Refine
  - [ ] Stop when accuracy plateaus or reaches target
- [ ] Update experiments/LEARNINGS.md and ../learnings/README.md with transferable patterns

### Stage 6: Test Against Validate Set & Peer Review
- [ ] Subagent 1: Apply prompt to validate.yaml (blind - never sees answers)
- [ ] Subagent 2: Score predictions (return only accuracy + error verse refs)
- [ ] Launch 4 critical peer reviews:
  - [ ] Theological review (check doctrinal soundness)
  - [ ] Linguistic review (check genre/grammar handling)
  - [ ] Methodological review (check sample size, balanced sampling, rigor)
  - [ ] **Translation practitioner review** (real-world testing with 2-3 languages)
- [ ] Create experiments/TRANSLATOR-IMPACT.md with findings
- [ ] Create experiments/TBTA-REVIEW.md for TBTA team (if applicable)
- [ ] Integrate feedback, iterate if needed
- [ ] Production readiness: ≥95% accuracy, all reviews passed, net benefit positive

---

## Common Pitfalls

### 1. **Sample Size Too Small**
❌ **Wrong**: 20-30 verses total
✅ **Correct**: 100+ verses PER VALUE (e.g., if feature has 3 values, need 300+ verses)

**Why**: Small datasets can't distinguish algorithm quality from chance. Need statistical power.

### 2. **Looking at Answers**
❌ **Wrong**: Main agent sees test.yaml and validate.yaml with TBTA values
✅ **Correct**: Use subagent for dataset creation AND validation (blind testing)

**Why**: Prevents unconscious bias. You can't unsee the answers.

### 3. **Skipping Error Analysis**
❌ **Wrong**: "Got 92%, good enough!"
✅ **Correct**: Every failure requires 6-step systematic analysis (see STAGES.md Stage 5)

**Why**: 100% accuracy is achievable. Every error reveals a blind spot.

### 4. **No External Validation**
❌ **Wrong**: Only check against TBTA values
✅ **Correct**: Check real Bible translations when feature is observable (clusivity, tense, etc.)

**Why**: TBTA might have perspective differences. Real translations validate approach.

**Thesis approach**: Find languages with the same feature (prefer same family/source lineage), see what their Bible translations did for this verse, analyze cultural/linguistic/source factors when disagreements exist. This cross-linguistic validation informs our algorithm.

### 5. **Unbalanced Sampling**
❌ **Wrong**: All verses from Romans, all narrative genre
✅ **Correct**: Proportional OT/NT, multiple genres (narrative/poetry/prophecy/epistle), diverse books

**Why**: Algorithm must work across entire Bible, not just one context.

### 6. **No Adversarial Cases**
❌ **Wrong**: Only "easy" typical verses in test set
✅ **Correct**: Test set includes edge cases, theological ambiguity, genre boundaries

**Purpose**: Find algorithm blind spots, not just confirm what works.

### 7. **Skipping Translation Practitioner Review** (Stage 6)
❌ **Wrong**: Only validate against TBTA, assume it's useful for translators
✅ **Correct**: Test with 2-3 languages (both marking and non-marking), document real translation mistakes

**Why**: Algorithm accuracy ≠ translator utility. Must measure net benefit (mistakes avoided vs. introduced).

### 8. **Documentation References External Standards**
❌ **Wrong**: "See SCHEMA.md for format" (forces clicking to understand)
✅ **Correct**: Inline 3-5 real verse examples with complete YAML structure

**Why**: README must be self-contained. Progressive disclosure to details, not basics.

---

## Progressive Disclosure Rules

### README.md: ≤500 lines (TBTA feature exception)
- **Section 1: Purpose** (50-100 lines) - What/Why/Who + Translation impact
- **Section 2: Methodology** (200-300 lines) - INLINE code examples, decision trees, NO external refs
- **Section 3: Output Schema** (100-150 lines) - Complete YAML structure + 3-5 real examples
- **Section 4: Related Features** (50 lines) - Cross-feature correlations

### Supplementary files: ≤400 lines each
- experiments/ANALYSIS.md, LEARNINGS.md, VALIDATION-RESULTS.md, etc.
- If any file exceeds limit, split by topic

**Rationale**: TBTA features are complex technical documentation requiring self-contained methodology. General project READMEs use 200-line limit (see `/.claude/skills/progressive-disclosure/SKILL.md`).

---

## File Naming Conventions

**Test Sets**:
- `train.yaml`, `test.yaml`, `validate.yaml` (not experiment-001.yaml)

**Prompt Iterations**:
- `PROMPT1.md`, `PROMPT2.md`, `PROMPT3.md` (clear iteration tracking)

**Analysis & Results**:
- `ANALYSIS.md` (approach comparison)
- `LEARNINGS.md` (error analysis with 6-step process)
- `VALIDATION-RESULTS.md` (accuracy metrics)
- `EXTERNAL-VALIDATION.md` (real translation checks)
- `CROSS-LINGUISTIC-VALIDATION.md` (Thesis approach - compare across languages)
- `TRANSLATOR-IMPACT.md` (Stage 6 real-world testing)
- `TBTA-REVIEW.md` (communication with TBTA team)

**Archive**:
- `archive/` (not `archive-10-phase/` or other naming)

---

## Production Readiness Criteria

Only deploy to production when ALL of these are true:

- [ ] Accuracy ≥ 95% on validate set (≥100 verses per value)
- [ ] All 4 peer reviews passed (theological, linguistic, methodological, translation practitioner)
- [ ] 6-step error analysis complete for every failure
- [ ] Locked predictions throughout (git commits present)
- [ ] External validation conducted (if feature observable in translations)
- [ ] Translation practitioner testing complete:
  - [ ] Tested with marking language(s)
  - [ ] Tested with non-marking language(s)
  - [ ] Net benefit is positive (mistakes avoided > mistakes introduced)
  - [ ] Translation teams recommend using this data
- [ ] TBTA review feedback integrated (if applicable)
- [ ] README.md documents final status
- [ ] Transferable insights added to `../learnings/README.md`

---

## Resources

**Authoritative Standards**:
- [STAGES.md](STAGES.md) - Complete 6-stage workflow
- [FEATURE-AUDIT-TEMPLATE.md](../../../plan/tbta-rebuild-with-llm/features/FEATURE-AUDIT-TEMPLATE.md) - Audit existing features
- [CROSS-FEATURE-LEARNINGS.md](../learnings/README.md) - Transferable patterns from other features

**Project Documentation** (see root for details):
- STANDARDIZATION.md - File naming, book codes, language codes
- SCHEMA.md - YAML structure, citation format, standard sections
- REVIEW-GUIDELINES.md - Validation levels, no fabrication rules
- ATTRIBUTION.md - All sources with copyright notices

**Progressive Disclosure**:
- `/.claude/skills/progressive-disclosure/SKILL.md` - General 200-line README standard
- TBTA features: 500-line exception (complex technical docs with inline methodology)

---

**Need help?** Check [STAGES.md](STAGES.md) for complete methodology or [CROSS-FEATURE-LEARNINGS.md](../learnings/README.md) for patterns from other features.
