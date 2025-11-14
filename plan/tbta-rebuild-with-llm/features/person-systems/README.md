# Person Systems Feature

**Feature**: Clusivity (Inclusive vs. Exclusive first-person plural pronouns)
**Status**: Migrated from 10-phase → STAGES.md structure
**Production Status**: In Progress (requires Stage 6 completion)

---

## Stage Completion Checklist

Based on [STAGES.md](../STAGES.md):

- [x] **Stage 1: Research TBTA Documentation**
  - Comprehensive feature analysis completed
  - TBTA patterns documented
  - Theological and linguistic research conducted

- [x] **Stage 2: Language Study**
  - 200+ person-marking languages identified
  - Austronesian pattern analysis (dominant family)
  - Language family predictions documented

- [x] **Stage 3: Scholarly and Internet Research**
  - Multiple theological sources consulted
  - Cross-linguistic studies reviewed
  - Translation patterns analyzed

- [x] **Stage 4: Generate Proper Test Set**
  - ⚠️ **Partial** - Used 10-phase methodology (adversarial + random)
  - Training: 20 verses (should be 40% of larger set)
  - Test: 21 verses (11 adversarial + 10 random)
  - **Gap**: No separate validate set (100 verses per value)
  - **Structure**: Not in standard 40/30/30 split

- [x] **Stage 5: Propose Hypothesis and First Prompt**
  - ✅ Algorithm v1.0 developed and tested
  - ✅ Algorithm v2.0 refined
  - ✅ Algorithm v2.1 created (UNTESTED)
  - ✅ Iterative refinement documented
  - ✅ Predictions locked with git commits
  - ⚠️ **Accuracy**: 73% adversarial (✓), 50-60% random (✗ below 80-90% target)

- [ ] **Stage 6: Test Against Validate Set**
  - ❌ **Not Started** - No validate set exists
  - ❌ Subagent validation not performed
  - ❌ Peer review incomplete (need 3 critical reviewers)
  - ❌ Algorithm v2.1 untested
  - **Blocker**: Must generate validate.yaml first

---

## Current Status Summary

### What's Working ✅
- **Translation Validation**: 100% (7/7) - Checked against 9 person-marking languages
- **Adversarial Test**: 73% (8/11) - Meets 60-70% target
- **External Validation**: 98% agreement across 9 languages (unique contribution)
- **Methodology**: Sound hierarchical prompting framework
- **Documentation**: Now consolidated to 10 core files

### What Needs Work ❌
- **Random Test**: 50-60% (5/10) - FAILS 80-90% target
- **TBTA Validation**: Only 2 verses checked (insufficient)
- **Algorithm v2.1**: Untested despite "production ready" claim
- **Validate Set**: Doesn't exist (need 100 verses per value)
- **Peer Review**: Stage 6 not completed

---

## Methodology Note

**Original Approach**: 10-phase adversarial testing protocol
- Comprehensive but led to 57 files (documentation bloat)
- Achieved good results but incomplete validation
- Random test failure indicates overfitting or blind spots

**Current Structure**: Migrated to STAGES.md organization
- Consolidated to 10 core files in `experiments/`
- Preserved valuable work (100% translation validation, external validation)
- Archived 47+ files to `archive-10-phase/`
- **Still needs Stage 6 completion**

---

## Files Structure

### experiments/ (Core Files)
1. **ANALYSIS.md** - Approaches analyzed (12 iterations documented)
2. **train.yaml** - 20 training verses with metadata
3. **test.yaml** - 21 test verses (11 adversarial + 10 random)
4. **PROMPT1.md** - Algorithm v1.0 (73% adversarial accuracy)
5. **PROMPT2.md** - Algorithm v2.0 (refined prompts)
6. **PROMPT3.md** - Algorithm v2.1 (untested, projected 75-80%)
7. **LEARNINGS.md** - Error analysis and lessons learned
8. **VALIDATION-RESULTS.md** - Accuracy summary across all tests
9. **EXTERNAL-VALIDATION.md** - Translation validation (9 languages, 98% agreement)

### archive-10-phase/ (Historical)
- 47+ files from original 10-phase methodology
- Training sets, adversarial tests, methodology docs
- Preserved for reference but not primary documentation

---

## Quick Reference

### Feature Definition
**Clusivity**: Grammatical distinction in "we/us/our" between:
- **Inclusive**: Speaker includes addressee in "we"
- **Exclusive**: Speaker excludes addressee from "we"

**Example**:
- "Let us pray" to congregation → INCLUSIVE (speaker + listeners pray together)
- "We apostles witnessed" to crowd → EXCLUSIVE (only apostles witnessed)

### High-Accuracy Rules (95%+ confidence)
1. **Divine creative/judicial acts** → EXCLUSIVE (humans can't participate)
2. **Prayer to God** → EXCLUSIVE (God not in "our")
3. **Reciprocal actions** ("one another") → INCLUSIVE (requires mutual participation)
4. **Worship invitations** → INCLUSIVE (addressees invited to participate)
5. **Apostolic eyewitness** → EXCLUSIVE (non-apostles weren't there)

### Languages with Clusivity (200+)
- **Dominant**: Austronesian family (95% have clusivity)
- **Geographic**: Philippines, Indonesia, Pacific, PNG
- **Validation Available**: 9 languages checked

---

## Next Steps (Priority Order)

### 1. Test Algorithm v2.1 (2 hours)
- Apply PROMPT3.md to existing test.yaml (21 verses)
- Calculate actual accuracy (is it really 75-80%?)
- Compare with v1.0 results
- Document if random test improves

### 2. Analyze Random Test Failures (2-3 hours)
- Identify the 5 failed verses
- Look for common patterns
- Determine if blind spots exist
- Inform v2.2 improvements if needed

### 3. Generate validate.yaml (Use Subagent! - 2 hours)
**Critical**: Main agent must NOT see validate data
- Subagent accesses TBTA repository
- Generates 100 verses per value (200 total)
- Creates validate.yaml in experiments/
- Main agent receives only file path

### 4. Complete Stage 6 Peer Review (3-4 hours)
- Subagent 1: Apply best prompt to validate.yaml (blind)
- Subagent 2: Check against TBTA, report accuracy
- Subagents 3-5: Critical peer review (assume junior coder wrote this)
- Main agent: Integrate feedback, iterate if needed

### 5. Final Documentation Update (1 hour)
- Update README.md with final accuracy
- Mark Stage 6 complete
- Document production status
- Update RESTRUCTURING-SUMMARY.md

---

## Unique Contributions

### External Translation Validation ⭐⭐⭐
**Innovation**: Validated predictions against 9 real Bible translations
- 98% agreement across languages
- Proves real-world applicability
- Independent verification beyond TBTA
- **Method reusable** for other features with translation evidence

### Hierarchical Prompting Framework ⭐⭐⭐
**Innovation**: Theological analysis first, grammar last
- 70%+ cases resolved by theological factors alone
- Early termination strategy
- LLM-executable prompts
- Clear decision points

### Locked Predictions ⭐⭐
**Innovation**: Git commit predictions BEFORE checking TBTA
- Prevents cheating
- Documents integrity
- Shows iterative improvement (v1 → v2 → v2.1)
- **Practice should continue** for all features

---

## Critical Findings

### Random Test Failure 🚨
**Problem**: Got 50-60% (target 80-90%)
**This is backwards**: Random should beat adversarial, not lose to it!

**Implications**:
- Potential overfitting to training data
- Training set may not be representative
- Algorithm may have systematic blind spots
- Need larger validate set to diagnose

---

## Production Readiness

**Current Assessment**: ⚠️ **NOT PRODUCTION READY**

**Reasons**:
1. Random test failure (50-60% vs 80-90% target)
2. Minimal TBTA validation (only 2 verses)
3. Algorithm v2.1 untested
4. No validate set (Stage 6 incomplete)
5. Sample sizes too small (20 training, 21 test)

**To Achieve Production Ready**:
1. ✅ Test algorithm v2.1
2. ✅ Analyze and fix random test failures
3. ✅ Generate 100-verse validate set
4. ✅ Achieve 95% on validate set (per STAGES.md)
5. ✅ Complete Stage 6 peer review

**Estimated Time**: ~12-15 hours to complete

---

## Contact & Questions

For questions about person systems or clusivity feature:
- Review `experiments/ANALYSIS.md` for approach evolution
- Check `experiments/LEARNINGS.md` for error patterns
- See `experiments/EXTERNAL-VALIDATION.md` for translation evidence
- Consult `archive-10-phase/` for historical methodology

---

**Summary**: Person systems feature has strong foundation (100% translation validation, unique external validation method, sound methodology) but requires Stage 6 completion before production deployment. Random test failure indicates real issues that must be addressed. Estimated 12-15 hours to complete migration and validation.
