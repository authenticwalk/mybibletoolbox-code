---
name: improve-tbta
description: Systematically work through TBTA features using a 10-phase workflow with proper task isolation and context management. Use when user wants to improve TBTA features, work on TBTA, or continue TBTA feature work.
---

# TBTA Feature Workflow

## Overview

This skill guides systematic work through TBTA (The Bible Translator's Assistant) features using a structured 10-phase approach. Each phase is executed independently to prevent context pollution, with progress tracked in a status file.

## When to Use

Use this skill when user says:
- "improve tbta" or "improve tbta features"
- "work on tbta" or "work on the next tbta feature"
- "continue tbta feature work" or "next tbta task"

## Core Workflow: 10-Phase Approach

Each phase is a **separate task** to prevent context pollution. Agent completes one phase, updates status, and stops. User says "improve tbta" to continue.

### Phase 1: Feature Selection & Setup
**Goal**: Identify next feature to work on, load context
**Outputs**: Feature selected, initial context loaded
**Time**: 15 minutes

### Phase 2: Training Set Design
**Goal**: Design 15-20 training verses covering all values equally
**Outputs**: `training/TRAINING-SET.md` with equal value coverage
**Time**: 1-2 hours

### Phase 3: Training Analysis (TBTA Access Allowed)
**Goal**: Access TBTA for training set, discover patterns, document learnings
**Outputs**: `training/TBTA-ANNOTATIONS.md`, `training/PATTERNS-LEARNED.md`
**Time**: 2-3 hours

### Phase 4: Algorithm Development
**Goal**: Create algorithm v1.0 based on training patterns, LOCK with git commit
**Outputs**: `training/ALGORITHM-v1.md` (locked with commit SHA)
**Time**: 1-2 hours

### Phase 5: Test Set Design (Equal Value Coverage)
**Goal**: Design adversarial (hard) and random (typical) test sets with equal examples per value
**Outputs**: `adversarial-test/TEST-SET.md`, `random-test/TEST-SET.md`
**Time**: 2-3 hours

### Phase 6: Make Predictions (NO TBTA ACCESS)
**Goal**: Apply algorithm v1.0 to both test sets WITHOUT checking TBTA, LOCK predictions
**Outputs**: `adversarial-test/PREDICTIONS-locked.md`, `random-test/PREDICTIONS-locked.md` (commit SHAs)
**Time**: 2-3 hours

### Phase 7: Validation & Accuracy Calculation
**Goal**: Check TBTA for test sets, calculate accuracy overall and per-value
**Outputs**: `adversarial-test/RESULTS.md`, `random-test/RESULTS.md` with per-value breakdown
**Time**: 1-2 hours

### Phase 8: Error Analysis & Algorithm Refinement
**Goal**: Exhaustive 6-step debugging for every error, update algorithm v2.0
**Outputs**: `ERROR-ANALYSIS.md`, `ALGORITHM-v2.md`
**Time**: 3-5 hours

### Phase 9: Documentation & Cross-Feature Learning
**Goal**: Update feature README, contribute learnings to CROSS-FEATURE-LEARNINGS.md
**Outputs**: Complete feature documentation
**Time**: 1-2 hours

### Phase 10: Peer Review & Finalization
**Goal**: Have another agent review work, integrate feedback, mark complete
**Outputs**: Feature marked as complete in status file
**Time**: 1-2 hours

---

## Status Tracking

**Status file**: `/plan/tbta-rebuild-with-llm/features/FEATURE-WORKFLOW-STATUS.yaml`

This file tracks:
- Current phase for each feature
- Completed phases
- Feature status (not_started | in_progress | complete | blocked)
- Next action
- Accuracy targets and results

---

## Phase Execution Details

### Phase 1: Feature Selection & Setup

**Agent Instructions**:

1. **Read status file**: `/plan/tbta-rebuild-with-llm/features/FEATURE-WORKFLOW-STATUS.yaml`
2. **Identify next feature**:
   - Find features with `status: in_progress` → continue current phase
   - If none, find first `status: not_started` → start Phase 1
   - Priority order (if choosing new):
     1. number-systems (if not complete)
     2. degree (if not complete)
     3. person-systems
     4. participant-tracking
     5. discourse-genre
     6. proximity
     7. polarity
     8. verb-tam
     9. time-granularity
     10. surface-realization
     11. honorifics-register
     12. illocutionary-force
     13. (other features as added)

3. **Load core context** (these docs ALWAYS):
   - `/plan/tbta-rebuild-with-llm/README.md` (overview)
   - `/plan/tbta-rebuild-with-llm/METHODOLOGY-ADVERSARIAL.md` (testing protocol)
   - `/plan/tbta-rebuild-with-llm/features/CROSS-FEATURE-LEARNINGS.md` (universal patterns)

4. **Load feature-specific context**:
   - `/plan/tbta-rebuild-with-llm/features/{feature}/README.md`
   - `/plan/tbta-rebuild-with-llm/features/{feature}/METHODOLOGY-STATUS.md` (if exists)

5. **Execute current phase** (detailed instructions below for each phase)

6. **Update status file** after completing phase

7. **STOP** - Do NOT continue to next phase. Wait for user to say "improve tbta"

---

### Phase 2: Training Set Design

**Goal**: Create balanced training set with equal value coverage

**Steps**:
1. Read feature README to identify all possible values
2. Calculate: `training_verses = 2 × number_of_values` (minimum 12, maximum 30)
3. For each value, select 2 example verses:
   - Mix of Greek (NT) and Hebrew (OT)
   - Mix of clear and moderately ambiguous cases
   - Diverse books (don't over-sample from one book)
4. Create `training/TRAINING-SET.md` with template
5. Commit: `git add training/TRAINING-SET.md && git commit -m "feat(tbta/{feature}): design balanced training set ({N} values × 2 = {total} verses)"`
6. Update status file: `current_phase: 3`

---

### Phase 3: Training Analysis

**Goal**: Access TBTA, discover patterns

**Steps**:
1. Access TBTA data for training verses (method TBD - may need user assistance)
2. Create `training/TBTA-ANNOTATIONS.md`
3. Analyze patterns, create `training/PATTERNS-LEARNED.md`
4. Commit both files
5. Update status: `current_phase: 4`

---

### Phase 4: Algorithm Development

**Goal**: Formalize decision rules into algorithm v1.0

**Steps**:
1. Based on patterns, create `training/ALGORITHM-v1.md`
2. Commit: `git add training/ALGORITHM-v1.md && git commit -m "feat(tbta/{feature}): lock algorithm v1.0 based on training patterns"`
3. Record commit SHA in algorithm file
4. Update status: `current_phase: 5`

---

### Phase 5: Test Set Design

**Goal**: Design adversarial and random test sets with equal value coverage

**Steps**:
1. **Adversarial Test Set** (`adversarial-test/TEST-SET.md`):
   - 2 examples per value (same as training)
   - Hard cases: morphology-semantics conflicts, boundary ambiguities, rare values
   - NO overlap with training set

2. **Random Test Set** (`random-test/TEST-SET.md`):
   - 2 examples per value (matches adversarial structure)
   - Clearer cases: morphology aligns with semantics
   - NO overlap with training or adversarial sets

3. Commit both: `git add adversarial-test/TEST-SET.md random-test/TEST-SET.md && git commit -m "feat(tbta/{feature}): design balanced test sets with equal value coverage"`
4. Update status: `current_phase: 6`

---

### Phase 6: Make Predictions

**Goal**: Apply algorithm v1.0 WITHOUT checking TBTA, lock predictions

**CRITICAL**: Do NOT access TBTA data for test verses!

**Steps**:
1. For adversarial test set, create `adversarial-test/PREDICTIONS-locked.md`
2. For random test set, create `random-test/PREDICTIONS-locked.md`
3. Commit: `git add */PREDICTIONS-locked.md && git commit -m "feat(tbta/{feature}): lock predictions for both test sets (NO TBTA CHECKED)"`
4. Record commit SHA in both prediction files
5. Update status: `current_phase: 7`

---

### Phase 7: Validation

**Goal**: NOW check TBTA, calculate accuracy

**Steps**:
1. Access TBTA data for adversarial test verses
2. Create `adversarial-test/RESULTS.md` with overall and per-value accuracy
3. Repeat for random test set: `random-test/RESULTS.md`
4. Calculate gap: `random_accuracy - adversarial_accuracy` (expected: 15-25 points)
5. Commit results
6. Update status: `current_phase: 8`

---

### Phase 8: Error Analysis & Refinement

**Goal**: Exhaustive debugging for EVERY error, update algorithm

**Steps**:
1. For each error, apply 6-step exhaustive debugging:
   - Verify Data Accuracy
   - Re-analyze Source Text
   - Re-analyze Context
   - Cross-Reference Sources (3+ translations, LXX/Vulgate)
   - Test Hypotheses
   - Final Determination (TBTA correct OR potential error)

2. Create `ERROR-ANALYSIS.md` with all errors analyzed
3. Create `ALGORITHM-v2.md` with updated rules
4. Commit both files
5. Update status: `current_phase: 9`

---

### Phase 9: Documentation & Cross-Feature Learning

**Goal**: Complete feature documentation, share learnings

**Steps**:
1. Update feature README with summary, results, limitations
2. Update `/plan/tbta-rebuild-with-llm/features/CROSS-FEATURE-LEARNINGS.md`
3. Create `COMPLETION-SUMMARY.md`
4. Commit all documentation
5. Update status: `current_phase: 10`

---

### Phase 10: Peer Review & Finalization

**Goal**: Independent review, integrate feedback, mark complete

**Steps**:
1. **Launch peer review agent** (separate Task)
2. Address peer review feedback
3. Update status file with `status: complete`
4. Commit: `git commit -m "feat(tbta/{feature}): mark feature as complete after peer review"`
5. **STOP** - Feature complete. Next invocation will start Phase 1 on next feature.

---

## Context Management Strategy

**To prevent context pollution:**

1. **Minimize doc loading**:
   - Core docs (3 files): Always load
   - Feature-specific: Only current feature
   - Training data: Only when needed (Phase 3)
   - Test data: Only when needed (Phase 7)

2. **One phase per session**:
   - Agent completes phase → updates status → STOPS
   - User says "improve tbta" → new session, fresh context

3. **Incremental file creation**:
   - Each phase creates 1-3 files
   - Don't load all files at once
   - Reference file paths, don't load content unnecessarily

4. **Status file as single source of truth**:
   - Always check status file first
   - Status file tells agent exactly what to do next
   - No need to load all features to figure out next task

---

## Error Handling

**If agent gets stuck**:
1. Check status file for current phase
2. Reload core docs only
3. Re-read phase instructions
4. If still stuck, user can manually advance: update status file to skip phase

**If TBTA data unavailable**:
1. Document in phase notes
2. Proceed with best effort (use existing documentation)
3. Mark as "needs TBTA validation" in status

**If test sets don't meet criteria**:
1. Document issues in phase notes
2. Redesign (back to Phase 5)
3. Update status: `current_phase: 5, notes: "Redesigning for equal coverage"`

---

## Quick Start Example

**First invocation**:
```
User: "improve tbta"

Agent:
1. Read FEATURE-WORKFLOW-STATUS.yaml
2. Find: number-systems, phase 6
3. Load: methodology docs + number-systems algorithm v1.0
4. Execute: Phase 6 (make predictions WITHOUT TBTA)
5. Create: PREDICTIONS-locked.md files
6. Commit + update status
7. Report: "Phase 6 complete for number-systems. Predictions locked. Ready for Phase 7 (validation)."
8. STOP
```

**Second invocation**:
```
User: "improve tbta"

Agent:
1. Read status: number-systems, phase 7
2. Load: methodology + test sets
3. Execute: Phase 7 (check TBTA, calculate accuracy)
4. Create: RESULTS.md files
5. Commit + update status
6. Report: "Phase 7 complete. Adversarial: X%, Random: Y%. Ready for Phase 8 (error analysis)."
7. STOP
```

---

## Success Criteria

**Per-phase completion**:
- All required files created
- Files follow templates
- Equal value coverage maintained (Phases 2, 5)
- Git commits with clear messages
- Status file updated
- Agent stopped (didn't continue to next phase)

**Per-feature completion**:
- All 10 phases completed
- Accuracy targets met (adversarial 60-70%, random 80-90%, gap 15-25 points)
- Error analysis thorough (6 steps for each error)
- Documentation complete
- Peer reviewed
- Status marked as complete

**Overall project completion**:
- All 12+ features complete
- Cross-feature learnings documented
- Methodology refined based on learnings
- Ready for comprehensive validation (Phase 3 after Q1 2026)

---

**Skill Status**: Ready for activation
**Next action**: User says "improve tbta"
**Expected**: Agent loads status, identifies current phase, executes it, and STOPS
