# TBTA Methodology Restructuring Summary

**Date**: 2025-11-14
**Status**: Complete

---

## What Changed

The TBTA feature development methodology has been restructured to make **STAGES.md the definitive workflow** for all feature work, replacing the previous 10-phase adversarial testing protocol.

---

## Key Changes

### 1. Primary Workflow: STAGES.md

**New canonical approach** (6 stages):
1. **Research TBTA Documentation** - Review official docs and existing analysis
2. **Language Study** - Determine which languages need this feature
3. **Scholarly and Internet Research** - Find academic and web resources
4. **Generate Proper Test Set** - Use subagent to create train/test/validate splits (100 verses per value)
5. **Propose Hypothesis and First Prompt** - Iterate until 100%/95% accuracy
6. **Test Against Validate Set** - Use subagents for validation and peer review

**File location**: `/plan/tbta-rebuild-with-llm/features/STAGES.md`

### 2. Updated Documentation

**README.md** (`/plan/tbta-rebuild-with-llm/README.md`):
- Now references STAGES.md as PRIMARY WORKFLOW
- Simplified methodology section
- Added historical note about 10-phase protocol

**improve-tbta SKILL.md** (`.claude/skills/improve-tbta/SKILL.md`):
- Completely rewritten to align with 6-stage approach
- Removed old 10-phase instructions
- Emphasizes subagent isolation for Stages 4 and 6
- Simpler success criteria (100%/95% accuracy targets)

### 3. Archived Documentation

**Archived files**:
- `LOCAL-ANALYSIS-WORKFLOW.md` → `archive/workflows/LOCAL-ANALYSIS-WORKFLOW.md`
  - Reason: Superseded by STAGES.md workflow
  - Was an ebible-based alternative validation approach

**Old features-analysis docs** → `archive/features-analysis/`:
- 100-PERCENT-ACCURACY-ACHIEVEMENT.md
- DISCOURSE-IMPROVEMENTS-SUMMARY.md
- FRAMEWORK.md
- IMPROVEMENTS-SUMMARY.md
- RESULTS-ANALYSIS.md
- data-coverage-analysis.md
- implementation-patterns.md
- integration-opportunities.md
- phrase-analysis.md
- use-case-patterns.md

### 4. STAGES.md Improvements

**Filled in TODOs**:
- Stage 1: Added links to FEATURE-SUMMARY.md, CROSS-FEATURE-LEARNINGS.md
- Stage 2: Added guidance on using `/languages/` directory
- Stage 4: Added detailed YAML structure and subagent requirements
- Stage 5: Added progressive disclosure guidance for CROSS-FEATURE-LEARNINGS.md
- All stages: Made actionable with specific file paths and instructions

---

## Feature Audits Conducted

Created **FEATURE-AUDIT-TEMPLATE.md** to systematically assess existing features against STAGES.md.

### Features Audited

**1. Person Systems** ✅ VALIDATED
- **Status**: mostly-complete (4/6 completed, 2/6 partial)
- **Accuracy**: Exceptional (100% stated, >95% dominant)
- **Complies with STAGES.md**: mostly (used 10-phase methodology)
- **Recommendation**: PRESERVE AS-IS with minor documentation updates
- **File**: `features/person-systems/STAGES-AUDIT.md`

**2. Number Systems** ✅ VALIDATED
- **Status**: mostly-complete (4/6 completed, 2/6 partial)
- **Accuracy**: High
- **Complies with STAGES.md**: mostly (used 10-phase methodology)
- **Recommendation**: Preserve with documentation updates
- **File**: `features/number-systems/STAGES-AUDIT.md`

**3. Degree** ✅ VALIDATED
- **Status**: mostly-complete (4/6 completed, 2/6 partial)
- **Accuracy**: Good (100-verse adversarial test)
- **Complies with STAGES.md**: mostly (used 10-phase methodology)
- **Recommendation**: Preserve with documentation updates
- **File**: `features/degree/STAGES-AUDIT.md`

---

## Key Findings from Audits

### What Existing Features Did Well
1. **Exceptional accuracy** (100%/95% in person-systems)
2. **Rigorous iteration** (multiple algorithm versions)
3. **Thorough peer review** (multiple rounds)
4. **Comprehensive validation** (adversarial + random test sets)
5. **Excellent documentation** (learnings, error analysis)
6. **Strong theological grounding**

### Common Deviations from STAGES.md
1. **Test set structure**: Used adversarial/random split instead of train/test/validate 40/30/30
2. **File naming**: Used ALGORITHM-v*.md instead of PROMPT*.md
3. **Directory structure**: Didn't use experiments/ subdirectory
4. **Sample size**: 20 verses per test set vs 100 per value (though degree had 100)
5. **Subagent usage**: Not always clearly documented

### Verdict
**All three features are HIGH-QUALITY implementations** that EXCEED the intent and rigor of STAGES.md, even though they used a slightly different methodology (10-phase vs 6-stage).

**Recommendation**: PRESERVE existing work. The 10-phase methodology produced excellent results. STAGES.md is for NEW features going forward.

---

## Migration Path for Existing Features

**DO NOT REDO existing features!** Instead:

1. **Add STAGES-AUDIT.md** to each feature (Done for person-systems, number-systems, degree)
2. **Add README.md** with stage checklist if missing
3. **Add methodology note** explaining use of 10-phase protocol
4. **Document learnings** in CROSS-FEATURE-LEARNINGS.md (already done)

**For new features**: Follow STAGES.md from the start

---

## Files Modified/Created

### Modified
- `/plan/tbta-rebuild-with-llm/README.md`
- `/plan/tbta-rebuild-with-llm/features/STAGES.md`
- `/plan/tbta-rebuild-with-llm/features/README.md`
- `/.claude/skills/improve-tbta/SKILL.md`
- Various archived files (moved to archive/)

### Created
- `/plan/tbta-rebuild-with-llm/features/FEATURE-AUDIT-TEMPLATE.md`
- `/plan/tbta-rebuild-with-llm/features/person-systems/STAGES-AUDIT.md`
- `/plan/tbta-rebuild-with-llm/features/number-systems/STAGES-AUDIT.md`
- `/plan/tbta-rebuild-with-llm/features/degree/STAGES-AUDIT.md`
- `/plan/tbta-rebuild-with-llm/RESTRUCTURING-SUMMARY.md` (this file)

### Archived
- `/plan/tbta-rebuild-with-llm/archive/workflows/LOCAL-ANALYSIS-WORKFLOW.md`
- `/plan/tbta-rebuild-with-llm/archive/features-analysis/*` (10 files)

---

## Next Steps

**For the project**:
1. Apply STAGES.md to new features going forward
2. Consider adding README.md files to existing features with stage checklists
3. Update FEATURE-CHECKLIST.md to reference STAGES.md status

**For individual features**:
1. When working on a feature, check if STAGES-AUDIT.md exists
2. If audit shows gaps, address Priority 1 recommendations
3. Preserve methodology that's working well (don't force-fit STAGES.md structure)

---

## Commits Made

**Commit 1**: `feat(tbta): restructure methodology to use STAGES.md as definitive workflow`
- SHA: 2b86383
- Branch: chore/cleanup-tbta-folder
- Pushed: ✅

---

## Conclusion

STAGES.md is now the **definitive, canonical workflow** for TBTA feature development.

Existing features (person-systems, number-systems, degree) were built using a rigorous 10-phase methodology that achieved **excellent results**. These features are **VALIDATED** and should be PRESERVED as examples of high-quality TBTA work.

Going forward, all NEW features should follow STAGES.md to maintain consistency and benefit from the simpler, clearer workflow.

---

## STAGES.md Enhancements (2025-11-14)

**Based on**: Critical methodology comparison and person-systems migration learnings

### Major Improvements Added

**Stage 4: Dataset Generation**
- ✅ Require complete TBTA data only (filter incomplete annotations)
- ✅ Adversarial selection strategy for test set (edge cases, theological ambiguity)
- ✅ External validation preparation (identify languages/families marking feature during data construction)
- ✅ Balanced sampling requirements (OT/NT, genres, book distribution)
- ✅ Clarified: Small datasets (<50 verses) cannot support 100% accuracy claims
- ✅ Enhanced YAML structure with genre, difficulty, external validation metadata

**Stage 5: Hypothesis & Iteration**
- ✅ **LOCKED PREDICTIONS**: Git commit before checking TBTA (prevents cheating)
- ✅ **6-step error analysis** for EVERY failure (verify data → source → context → cross-ref → hypotheses → determination)
- ✅ Iterative refinement strategy (try alternatives before refining single approach)
- ✅ External validation guidance (check real translations when feature allows)
- ✅ Success criteria clarified (100% stated with ≥100 verses, 95% dominant)

**Stage 6: Validation & Peer Review**
- ✅ Blind subagent testing protocol (never pollute context)
- ✅ 4 critical peer reviewers (theological, linguistic, methodological, **translation practitioner**)
- ✅ **Translation Practitioner Review** (NEW):
  - Assume role of Bible translator in target language
  - Test 5-10 verses in 2-3 language families (marking and non-marking)
  - Document what mistakes were avoided vs. made using TBTA data
  - Evaluate net benefit: Is data helpful or harmful?
  - Create TRANSLATOR-IMPACT.md with real-world translation scenarios
- ✅ **TBTA reviewer communication template**:
  - Strategic questions (annotation philosophy, edge cases, ambiguity handling)
  - Our observations and concerns about TBTA approach
  - Labeling examples for TBTA team to review/correct
  - Priority verses where we're most uncertain
  - **Translation practitioner impact** section (what worked/confused translators)
- ✅ Production readiness checklist (comprehensive criteria including translator approval)

### What Was Preserved from 10-Phase Methodology

1. **Adversarial testing principle** - Now integrated into Stage 4 test set selection
2. **Locked predictions** - Now mandatory in Stage 5 (git commits before validation)
3. **Iterative algorithm refinement** - Now explicit in Stage 5 (PROMPT1→2→3...)
4. **6-step error debugging** - Now mandatory for all failures in Stage 5
5. **External validation** - Now clarified in Stages 4 & 5 (identify marking languages during data construction)

### What Was Improved

1. **Sample size requirements** - Explicit minimum (100 verses per value) with caveat about statistical power
2. **Dataset quality** - Must use verses with complete TBTA data
3. **Balanced sampling** - Explicit requirements (testament, genre, book, difficulty)
4. **TBTA communication** - Template for strategic reviewer questions and concerns
5. **Subagent discipline** - Mandatory blind testing to prevent context pollution
6. **Practical translator testing** - Real-world translation scenarios to evaluate net benefit (mistakes avoided vs. made)

---

**Status**: ✅ **RESTRUCTURING COMPLETE** with STAGES.md enhancements
