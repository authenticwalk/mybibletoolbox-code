# Migration Plan: 10-Phase Features → STAGES.md Structure

**Date**: 2025-11-14
**Purpose**: Practical steps to consolidate existing features without discarding valuable work

---

## Philosophy

**Don't throw away good work. But don't preserve bloat either.**

We're taking a **middle path**:
- ✅ Keep valuable validation and learnings
- ✅ Reorganize into STAGES.md structure
- ✅ Complete unfinished validation
- ❌ Don't preserve documentation bloat
- ❌ Don't redo work from scratch

---

## Person-Systems Migration (Priority 1)

### Current State Assessment

**What's Actually Good** ✅:
- Translation validation: 7/7 verses (100%) across 9 languages
- Adversarial test: 73% (met target 60-70%)
- Locked predictions with git commits
- Iterative algorithm refinement (v1 → v2 → v2.1)
- External validation methodology (unique!)

**What's Problematic** ❌:
- 57 files (excessive!)
- Random test: 50-60% (FAILED 80-90% target)
- Only 2 TBTA verses validated
- Algorithm v2.1 UNTESTED
- "Production ready" claim unsupported

### Migration Steps

#### Step 1: Consolidate Documentation (1-2 hours)

**From 57 files to ~10 core files:**

```
features/person-systems/
├── README.md (NEW)
│   ├── Feature overview
│   ├── STAGES.md checklist
│   ├── Link to experiments/
│   └── Production status: "In progress"
│
└── experiments/
    ├── ANALYSIS.md (CONSOLIDATE from multiple files)
    │   └── 12 approaches analyzed (merge from METHODOLOGY.md, clusivity-framework.md, etc.)
    │
    ├── train.yaml (CREATE from existing 20 training verses)
    │   └── Format: verse ref + TBTA value + translation data
    │
    ├── test.yaml (CREATE from adversarial-test + random-test)
    │   └── Combined 21 verses with TBTA values
    │
    ├── validate.yaml (FUTURE - not yet created)
    │   └── 100 verses per value (to be generated)
    │
    ├── PROMPT1.md (RENAME from training/ALGORITHM-v1.md)
    ├── PROMPT2.md (RENAME from training/ALGORITHM-v2.md)
    ├── PROMPT3.md (RENAME from training/ALGORITHM-v2.1-PRODUCTION.md)
    │
    ├── LEARNINGS.md (CONSOLIDATE)
    │   └── Merge ERROR-ANALYSIS.md, PHASE2-IMPROVEMENTS.md, existing LEARNINGS.md
    │
    ├── VALIDATION-RESULTS.md (CONSOLIDATE)
    │   └── Merge VALIDATION-RESULTS-COMPLETE.md, TEST-VALIDATION-COMPLETE.md, RESULTS files
    │
    └── EXTERNAL-VALIDATION.md (NEW)
        └── Translation validation across 9 languages (preserve this unique work!)
```

**Archive the rest**:
```
features/person-systems/archive-10-phase/
└── [move all 47 other files here]
```

#### Step 2: Test Algorithm v2.1 (2 hours)

**Currently untested! Need to validate:**

1. Load test.yaml (21 verses)
2. Apply PROMPT3.md (algorithm v2.1)
3. Calculate accuracy
4. Expected: 75-80% (up from 62% with v1.0)
5. If NOT: iterate to PROMPT4.md

**Success criteria from STAGES.md**:
- 100% on "stated values" (single answer)
- 95% on "dominant values" (primary + rationale)

#### Step 3: Investigate Random Test Failure (2-3 hours)

**Problem**: 50-60% (expected 80-90%)

**Possible causes**:
1. Overfitting to training data
2. Random sample too hard by chance
3. Test set too small (n=10)
4. Algorithm blind spots

**Action**:
1. Analyze the 5 failures in random test
2. Check if they share patterns
3. Refine PROMPT4.md to address
4. Consider expanding random sample

#### Step 4: Generate validate.yaml (Use Subagent!)

**Current gap**: No validation set

**Action**:
1. Launch subagent to access TBTA data
2. Generate 100 verses per value (200 total if 2 values)
3. Create validate.yaml in STAGES.md format
4. Main agent receives only file path, not content
5. Use for final Stage 6 validation

#### Step 5: Complete Stage 6 (Peer Review)

**Use 3 subagent reviewers:**

1. Subagent 1: Apply best prompt to validate.yaml (blind)
2. Subagent 2: Check against TBTA, report accuracy
3. Subagents 3-5: Critical peer review
   - Assume junior coder wrote this
   - Find problems
   - Be highly critical

4. Main agent: Integrate feedback
   - If accuracy < 95%, return to Step 2
   - If peer review fails, iterate on prompt

#### Step 6: Final Documentation Update

**Create canonical README.md**:

```markdown
# Person Systems Feature

## Stage Completion Status

- [x] Stage 1: Research TBTA Documentation
- [x] Stage 2: Language Study
- [x] Stage 3: Scholarly and Internet Research
- [x] Stage 4: Generate Proper Test Set
- [x] Stage 5: Propose Hypothesis and First Prompt
- [ ] Stage 6: Test Against Validate Set (IN PROGRESS)

## Current Status

**Methodology**: Migrated from 10-phase to STAGES.md structure
**Algorithm**: PROMPT3.md (v2.1) - tested at 75-80%
**Unique contribution**: External validation with 9 Bible translations
**Production status**: Awaiting Stage 6 completion

## Files

See experiments/ folder for all validation work.
See archive-10-phase/ for historical documentation.
```

### Timeline

- Step 1 (Consolidate): 1-2 hours
- Step 2 (Test v2.1): 2 hours
- Step 3 (Debug random): 2-3 hours
- Step 4 (Generate validate.yaml): 2 hours (subagent)
- Step 5 (Stage 6): 3-4 hours (subagent + peer review)
- Step 6 (README): 1 hour

**Total**: ~12-15 hours to complete migration

---

## Number-Systems Migration (Priority 2)

### Current State

- 22 files (less bloated than person-systems)
- Small test sets
- Limited validation

### Migration Strategy

**Faster path** (already less bloated):

1. **Consolidate** (2 hours):
   - 22 files → 10 core files in experiments/
   - Create README.md with STAGES.md checklist
   - Archive rest

2. **Complete validation** (4-6 hours):
   - Generate validate.yaml with subagent (100 verses per value)
   - Test current algorithm
   - Iterate if needed

3. **Stage 6 peer review** (3 hours):
   - 3 critical subagent reviewers
   - Integrate feedback
   - Mark complete

**Total**: ~9-11 hours

---

## Degree Migration (Priority 3)

### Current State

- 29 files
- Has 100-verse test (GOOD!)
- But batch processing, not STAGES.md structure

### Migration Strategy

1. **Reorganize 100-verse test** (2 hours):
   - Convert batches → validate.yaml
   - Create proper train.yaml/test.yaml split
   - Consolidate 29 → 10 files

2. **Complete validation** (3-4 hours):
   - Re-test with current algorithm
   - Calculate proper accuracy
   - Iterate if needed

3. **Stage 6 peer review** (3 hours):
   - 3 critical subagent reviewers
   - Integrate feedback
   - Mark complete

**Total**: ~8-10 hours

---

## What to Preserve from 10-Phase

### Keep These Innovations

**1. External Validation (Person-Systems)** ⭐⭐⭐

**What**: Validation against 9 real Bible translations (not just TBTA)
**Why valuable**: Proves real-world applicability
**How to preserve**: Create EXTERNAL-VALIDATION.md in experiments/
**Apply to**: Clusivity, and any feature with real translation data

**2. Locked Predictions with Git Commits** ⭐⭐⭐

**What**: Git commit predictions BEFORE checking TBTA
**Why valuable**: Prevents cheating, proves integrity
**How to preserve**: Already in STAGES.md Stage 5
**Apply to**: All features

**3. Iterative Algorithm Refinement** ⭐⭐⭐

**What**: PROMPT1 → PROMPT2 → PROMPT3 until can't improve
**Why valuable**: Systematic improvement
**How to preserve**: Already in STAGES.md Stage 5 ("Repeat until cannot get better")
**Apply to**: All features

**4. 6-Step Error Debugging** ⭐⭐

**What**: Exhaustive analysis (verify data, re-analyze source, context, cross-ref, test hypotheses, determine)
**Why valuable**: Prevents superficial debugging
**How to preserve**: Add to STAGES.md Stage 5 guidance in LEARNINGS.md
**Apply to**: All features when debugging errors

**5. Adversarial Testing Concept** ⭐⭐

**What**: Include hard cases, not just random
**Why valuable**: Finds blind spots
**How to preserve**: Optional in Stage 4 - create "hard" subset in test.yaml
**Apply to**: Features with clear edge cases

---

## What to Discard

### Don't Preserve

❌ **Documentation bloat** - 50+ files is excessive
❌ **Small test sets** - 20 verses not enough
❌ **Vague success criteria** - "60-70%" too ambiguous
❌ **Competing structures** - adversarial/random vs train/test/validate
❌ **Untested algorithm claims** - v2.1 "production ready" but not validated
❌ **10-phase complexity** - Simpler 6-stage is better
❌ **Gap analysis** - Random-adversarial gap adds complexity without benefit
❌ **Fragmented information** - One README, not 20 summaries

---

## Universal Migration Template

For ANY feature built with 10-phase:

### Phase 1: Assess (1 hour)
1. Count files
2. Identify what's actually validated vs claimed
3. Check test set sizes
4. Review accuracy results critically

### Phase 2: Consolidate (2-3 hours)
1. Create experiments/ folder
2. Merge to ~10 core files
3. Archive rest to archive-10-phase/
4. Create README.md with STAGES.md checklist

### Phase 3: Complete (4-8 hours)
1. Generate validate.yaml if missing (subagent!)
2. Test current algorithm
3. Iterate to meet 100%/95% targets
4. Stage 6 peer review

### Phase 4: Document (1 hour)
1. Update README.md
2. Mark STAGES.md checklist
3. Update RESTRUCTURING-SUMMARY.md

---

## Success Metrics

**Feature is "migrated" when:**

✅ Consolidated to ≤10 core files in experiments/
✅ Has README.md with STAGES.md checklist
✅ Has validate.yaml (100 verses per value)
✅ Algorithm tested and meets 100%/95% targets (or documented why not)
✅ Stage 6 peer review completed
✅ Production status clearly stated (not misleadingly "ready")

---

## Timeline Summary

- **Person-systems**: 12-15 hours
- **Number-systems**: 9-11 hours
- **Degree**: 8-10 hours

**Total**: ~30-36 hours to migrate all 3 features

**Benefit**: Clean, validated features following STAGES.md structure

---

## Next Steps

1. Review this migration plan with user
2. Get approval to proceed
3. Start with person-systems (highest priority, most complex)
4. Use learnings to speed up number-systems and degree
5. Document migration process for future features

---

**Status**: PLAN READY
**Recommendation**: Start with person-systems migration
**Expected outcome**: 3 properly validated features with clear structure
