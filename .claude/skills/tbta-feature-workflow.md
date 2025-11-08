# TBTA Feature Workflow Skill

**Purpose**: Systematically work through TBTA features from start to completion with proper task isolation and context management.

**Usage**: User says "work on the next tbta feature" and this skill handles everything.

---

## Skill Activation

This skill activates when user says:
- "work on the next tbta feature"
- "continue tbta feature work"
- "next tbta task"

---

## Core Workflow: 10-Phase Approach

Each phase is a **separate task** to prevent context pollution. Agent completes one phase, updates status, and stops. User says "work on the next tbta feature" to continue.

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

```yaml
features:
  number-systems:
    current_phase: 5  # Test Set Design
    completed_phases: [1, 2, 3, 4]
    status: in_progress
    started: 2025-11-07
    last_updated: 2025-11-08

  degree:
    current_phase: 4  # Algorithm Development
    completed_phases: [1, 2, 3]
    status: in_progress
    started: 2025-11-07
    last_updated: 2025-11-08

  person-systems:
    current_phase: 1  # Feature Selection
    completed_phases: []
    status: not_started
    started: null
    last_updated: null

  # ... other features
```

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

7. **STOP** - Do NOT continue to next phase. Wait for user to say "work on the next tbta feature"

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
4. Create `training/TRAINING-SET.md`:
   ```markdown
   # {Feature} Training Set

   **Purpose**: Learn TBTA patterns
   **TBTA Access**: ALLOWED (this is training)
   **Distribution**: 2 examples × {N} values = {total} verses

   ## Value 1: {value_name} (2 verses)

   ### Verse 1
   **Reference**: Book Chapter:Verse
   **Greek/Hebrew**: [text]
   **English**: [translation]
   **Why included**: [rationale]

   ### Verse 2
   ...

   ## Value 2: {value_name} (2 verses)
   ...
   ```

5. Commit: `git add training/TRAINING-SET.md && git commit -m "feat(tbta/{feature}): design balanced training set ({N} values × 2 = {total} verses)"`

6. Update status file: `current_phase: 3`

---

### Phase 3: Training Analysis

**Goal**: Access TBTA, discover patterns

**Steps**:
1. Access TBTA data for training verses (method TBD - may need user assistance)
2. Create `training/TBTA-ANNOTATIONS.md`:
   ```markdown
   # {Feature} Training Data from TBTA

   ## Value 1: {value_name}

   ### Verse 1 - Reference
   **TBTA Code**: {code}
   **Constituent**: {which constituent}
   **Morphology**: {Greek/Hebrew form}
   **Context**: {relevant context}

   ### Verse 2 - Reference
   ...
   ```

3. Analyze patterns, create `training/PATTERNS-LEARNED.md`:
   ```markdown
   # {Feature} Patterns Learned from Training

   ## Pattern 1: {Name}
   **Observation**: [what the pattern is]
   **Evidence**: [which verses show this]
   **Rule**: [how to apply]
   **Confidence**: [High/Medium/Low]

   ## Pattern 2: {Name}
   ...

   ## Edge Cases Identified
   - [Case 1]: [description]
   - [Case 2]: [description]
   ```

4. Commit both files

5. Update status: `current_phase: 4`

---

### Phase 4: Algorithm Development

**Goal**: Formalize decision rules into algorithm v1.0

**Steps**:
1. Based on patterns, create `training/ALGORITHM-v1.md`:
   ```markdown
   # {Feature} Algorithm v1.0

   **Status**: LOCKED
   **Date**: {date}
   **Commit SHA**: {will be added after commit}

   ## Decision Tree

   ### Rule 1: [Highest Priority]
   **Condition**: [when to apply]
   **Action**: Predict {value}
   **Confidence**: {percentage}
   **Examples**: [from training]

   ### Rule 2: [Second Priority]
   ...

   ### Default Rule
   If no rules match, predict: {default_value}

   ## Pseudocode

   ```python
   def predict_{feature}(constituent, context):
       # Rule 1
       if [condition]:
           return {value}

       # Rule 2
       if [condition]:
           return {value}

       # Default
       return {default_value}
   ```
   ```

2. Commit: `git add training/ALGORITHM-v1.md && git commit -m "feat(tbta/{feature}): lock algorithm v1.0 based on training patterns"`

3. Record commit SHA in algorithm file

4. Update status: `current_phase: 5`

---

### Phase 5: Test Set Design

**Goal**: Design adversarial and random test sets with equal value coverage

**Steps**:

1. **Adversarial Test Set** (`adversarial-test/TEST-SET.md`):
   - 2 examples per value (same as training)
   - Hard cases: morphology-semantics conflicts, boundary ambiguities, rare values, theological debates
   - Focus on verses where legitimate disagreement possible
   - NO overlap with training set

2. **Random Test Set** (`random-test/TEST-SET.md`):
   - 2 examples per value (matches adversarial structure)
   - Clearer cases: morphology aligns with semantics, less ambiguity
   - NO overlap with training or adversarial sets

3. **Template for both**:
   ```markdown
   # {Feature} {Adversarial/Random} Test Set

   **Purpose**: Test algorithm v1.0 on {hard/typical} cases
   **Design**: Equal value coverage (2 per value)
   **Expected accuracy**: {60-70% for adversarial / 80-90% for random}
   **TBTA Access**: FORBIDDEN until predictions locked

   ## Value 1: {value_name} (2 verses)

   ### Verse 1
   **Reference**: Book Chapter:Verse
   **Greek/Hebrew**: [text]
   **English**: [translation]
   **Challenge**: [what makes this hard/clear]
   **Why {adversarial/typical}**: [explanation]

   ### Verse 2
   ...
   ```

4. Commit both: `git add adversarial-test/TEST-SET.md random-test/TEST-SET.md && git commit -m "feat(tbta/{feature}): design balanced test sets with equal value coverage"`

5. Update status: `current_phase: 6`

---

### Phase 6: Make Predictions

**Goal**: Apply algorithm v1.0 WITHOUT checking TBTA, lock predictions

**CRITICAL**: Do NOT access TBTA data for test verses!

**Steps**:

1. For adversarial test set, create `adversarial-test/PREDICTIONS-locked.md`:
   ```markdown
   # {Feature} Adversarial Test Predictions (LOCKED)

   **Date**: {date}
   **Algorithm**: v1.0
   **TBTA Status**: NOT CHECKED (predictions made blind)

   ## Value 1: {value_name}

   ### Verse 1 - Reference
   **Predicted Value**: {value}
   **Reasoning**: [why this prediction]
   **Confidence**: [High/Medium/Low]
   **Alternative**: [if uncertain]

   ### Verse 2
   ...
   ```

2. For random test set, create `random-test/PREDICTIONS-locked.md` (same format)

3. Commit: `git add */PREDICTIONS-locked.md && git commit -m "feat(tbta/{feature}): lock predictions for both test sets (NO TBTA CHECKED)"`

4. Record commit SHA in both prediction files

5. Update status: `current_phase: 7`

---

### Phase 7: Validation

**Goal**: NOW check TBTA, calculate accuracy

**Steps**:

1. Access TBTA data for adversarial test verses

2. Create `adversarial-test/RESULTS.md`:
   ```markdown
   # {Feature} Adversarial Test Results

   ## Overall Accuracy
   **Total**: {correct} / {total} = {percentage}%
   **Expected**: 60-70%
   **Status**: {✅ Met expectations / ⚠️ Below expectations}

   ## Per-Value Accuracy

   | Value | Correct | Total | Accuracy |
   |-------|---------|-------|----------|
   | {value1} | {n} | 2 | {%} |
   | {value2} | {n} | 2 | {%} |
   | ... | | | |

   ## Error Breakdown

   ### Verse Reference - {Value}
   **Predicted**: {prediction}
   **Actual (TBTA)**: {actual}
   **Error Type**: [morphology conflict / boundary case / rare value / etc.]

   ## Error Categories
   - **Morphology conflicts**: {count} errors
   - **Boundary ambiguities**: {count} errors
   - **Rare values**: {count} errors
   - **Other**: {count} errors
   ```

3. Repeat for random test set: `random-test/RESULTS.md`

4. Calculate gap: `random_accuracy - adversarial_accuracy`
   - Expected: 15-25 points
   - If gap < 15: Test sets not different enough
   - If gap > 30: Adversarial too hard or random too easy

5. Commit results

6. Update status: `current_phase: 8`

---

### Phase 8: Error Analysis & Refinement

**Goal**: Exhaustive debugging for EVERY error, update algorithm

**Steps**:

1. For each error, apply 6-step exhaustive debugging:
   ```
   1. Verify Data Accuracy - Confirm verse, feature, constituent
   2. Re-analyze Source Text - Morphology, lexicons, commentaries
   3. Re-analyze Context - Discourse, theology, parallels
   4. Cross-Reference Sources - 3+ translations, LXX/Vulgate
   5. Test Hypotheses - Alternative algorithms, edge cases
   6. Final Determination - TBTA correct (learn) OR potential error (flag)
   ```

2. Create `ERROR-ANALYSIS.md`:
   ```markdown
   # {Feature} Error Analysis

   ## Error 1: Reference - {Predicted} vs {Actual}

   ### Exhaustive Analysis
   1. **Data verified**: ✅ Verse correct, feature correct
   2. **Source analysis**: [morphology details]
   3. **Context analysis**: [discourse, theology]
   4. **Cross-references**:
      - Translation 1: [form]
      - Translation 2: [form]
      - LXX/Vulgate: [form]
   5. **Hypothesis**: [what algorithm missed]
   6. **Determination**: ✅ TBTA CORRECT - Algorithm needs update

   ### Pattern Learned
   **New Rule**: [what to add to algorithm]

   ## Error 2: Reference
   ...

   ## Summary of Learnings

   ### New Patterns Discovered
   1. [Pattern]: [description]
   2. [Pattern]: [description]

   ### Algorithm Gaps Identified
   1. [Gap]: [description]
   2. [Gap]: [description]
   ```

3. Create `ALGORITHM-v2.md`:
   ```markdown
   # {Feature} Algorithm v2.0

   **Previous**: v1.0 ({accuracy}% adversarial, {accuracy}% random)
   **Updated**: {date}
   **Changes**: Based on {N} error analyses

   ## New Rules Added

   ### Rule {N+1}: [From Error Analysis]
   **Trigger**: [condition]
   **Action**: [prediction]
   **Rationale**: [why this fixes error]

   ## Modified Rules

   ### Rule {X}: [Modified]
   **Old**: [previous version]
   **New**: [updated version]
   **Reason**: [why changed]

   ## Updated Decision Tree
   [Full algorithm with new rules]
   ```

4. Commit both files

5. Update status: `current_phase: 9`

---

### Phase 9: Documentation & Cross-Feature Learning

**Goal**: Complete feature documentation, share learnings

**Steps**:

1. Update feature README with:
   - Summary of results
   - Link to training, test results
   - Algorithm final version
   - Known limitations
   - Recommendations for translators

2. Update `/plan/tbta-rebuild-with-llm/features/CROSS-FEATURE-LEARNINGS.md`:
   - Add any universal patterns discovered
   - Note feature-specific edge cases
   - Contribute to methodology improvements

3. Create `COMPLETION-SUMMARY.md`:
   ```markdown
   # {Feature} Completion Summary

   ## Statistics
   - Training verses: {N}
   - Adversarial accuracy: {%}
   - Random accuracy: {%}
   - Algorithm versions: {N}
   - Errors debugged: {N}
   - New patterns: {N}

   ## Key Discoveries
   1. [Discovery]: [description]
   2. [Discovery]: [description]

   ## Contributions to TBTA Project
   - Universal patterns: [list]
   - Methodology improvements: [list]
   - Tools developed: [list]

   ## Recommendations
   - For translators: [guidance]
   - For future features: [lessons]
   ```

4. Commit all documentation

5. Update status: `current_phase: 10`

---

### Phase 10: Peer Review & Finalization

**Goal**: Independent review, integrate feedback, mark complete

**Steps**:

1. **Launch peer review agent** (separate Task):
   ```
   Review the {feature} work:
   - Check methodology followed correctly
   - Verify equal value coverage in all sets
   - Validate error analysis thoroughness
   - Test algorithm logic
   - Check documentation completeness

   Provide structured feedback in PEER-REVIEW.md
   ```

2. Address peer review feedback:
   - Fix any issues identified
   - Update documentation if needed
   - Re-run tests if algorithm changed

3. Update status file:
   ```yaml
   {feature}:
     current_phase: 10
     completed_phases: [1,2,3,4,5,6,7,8,9,10]
     status: complete
     completed: {date}
     final_accuracy_adversarial: {%}
     final_accuracy_random: {%}
   ```

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
   - User says "work on the next tbta feature" → new session, fresh context

3. **Incremental file creation**:
   - Each phase creates 1-3 files
   - Don't load all files at once
   - Reference file paths, don't load content unnecessarily

4. **Status file as single source of truth**:
   - Always check status file first
   - Status file tells agent exactly what to do next
   - No need to load all features to figure out next task

---

## Agent Prompt Template

When this skill activates, use this prompt:

```
You are working on the TBTA Features project using the 10-phase workflow.

**Current Task**: {phase_name} for {feature_name}

**Context loaded**:
- Methodology: METHODOLOGY-ADVERSARIAL.md
- Cross-feature learnings: CROSS-FEATURE-LEARNINGS.md
- Feature README: features/{feature}/README.md

**Your objectives for this phase**:
{phase_specific_objectives}

**Deliverables**:
{list_of_files_to_create}

**Constraints**:
- Stay focused on THIS phase only
- Do NOT proceed to next phase
- Equal value coverage required for all test sets
- Harder verses preferred for adversarial sets
- Follow methodology exactly
- Update status file when done
- Commit work to git

**After completion**:
1. Create/update all required files
2. Git commit with descriptive message
3. Update FEATURE-WORKFLOW-STATUS.yaml
4. STOP and report completion to user
5. User will say "work on the next tbta feature" to continue

Begin Phase {N}: {phase_name}
```

---

## Status File Format

`/plan/tbta-rebuild-with-llm/features/FEATURE-WORKFLOW-STATUS.yaml`:

```yaml
workflow_version: "1.0"
last_updated: "2025-11-08"

# Priority order for new features
priority_queue:
  - number-systems
  - degree
  - person-systems
  - participant-tracking
  - discourse-genre
  - proximity
  - polarity
  - verb-tam
  - time-granularity
  - surface-realization
  - honorifics-register
  - illocutionary-force

# Feature statuses
features:
  number-systems:
    status: in_progress  # not_started | in_progress | complete
    current_phase: 5
    completed_phases: [1, 2, 3, 4]
    started: "2025-11-07"
    last_updated: "2025-11-08"
    notes: "Test sets designed, ready for predictions"

  degree:
    status: in_progress
    current_phase: 4
    completed_phases: [1, 2, 3]
    started: "2025-11-07"
    last_updated: "2025-11-08"
    notes: "Algorithm v1.0 being developed"

  person-systems:
    status: not_started
    current_phase: 1
    completed_phases: []
    started: null
    last_updated: null
    notes: "Has existing documentation, needs workflow"

  # Additional features...

# Global statistics
statistics:
  features_complete: 0
  features_in_progress: 2
  features_not_started: 10
  total_features: 12
  completion_percentage: 0
```

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

## Quick Start

**First invocation**:
```
User: "work on the next tbta feature"

Agent:
1. Read FEATURE-WORKFLOW-STATUS.yaml
2. Find: number-systems, phase 5
3. Load: methodology docs + number-systems README
4. Execute: Phase 5 (Test Set Design)
5. Create: adversarial-test/TEST-SET.md, random-test/TEST-SET.md
6. Commit + update status
7. Report: "Phase 5 complete for number-systems. Ready for Phase 6 (predictions)."
8. STOP
```

**Second invocation**:
```
User: "work on the next tbta feature"

Agent:
1. Read status: number-systems, phase 6
2. Load: methodology + algorithm v1.0
3. Execute: Phase 6 (make predictions WITHOUT TBTA)
4. Create: PREDICTIONS-locked.md files
5. Commit + update status
6. Report: "Phase 6 complete. Predictions locked. Ready for Phase 7 (validation)."
7. STOP
```

---

## Success Criteria

**Per-phase completion**:
- [ ] All required files created
- [ ] Files follow templates
- [ ] Equal value coverage maintained (Phases 2, 5)
- [ ] Git commits with clear messages
- [ ] Status file updated
- [ ] Agent stopped (didn't continue to next phase)

**Per-feature completion**:
- [ ] All 10 phases completed
- [ ] Accuracy targets met (adversarial 60-70%, random 80-90%, gap 15-25 points)
- [ ] Error analysis thorough (6 steps for each error)
- [ ] Documentation complete
- [ ] Peer reviewed
- [ ] Status marked as complete

**Overall project completion**:
- [ ] All 12+ features complete
- [ ] Cross-feature learnings documented
- [ ] Methodology refined based on learnings
- [ ] Ready for comprehensive validation (Phase 3 after Q1 2026)

---

**Skill Status**: Ready for activation
**Next action**: User says "work on the next tbta feature"
**Expected**: Agent loads status, identifies Phase 5 for number-systems, executes test set design
