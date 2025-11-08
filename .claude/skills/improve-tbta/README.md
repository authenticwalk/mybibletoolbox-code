# Improve TBTA - Skill Documentation

## Quick Start

**Invoke this skill by saying:** "improve tbta" or "work on tbta features"

## What This Skill Does

Manages systematic work through TBTA (The Bible Translator's Assistant) features using a structured 10-phase workflow. Each phase is executed independently to prevent context overload, with progress tracked automatically.

## How It Works

### Phased Approach

Instead of tackling everything at once, this skill:
- **Reads** the status file to identify current phase
- **Loads** only the minimal context needed for that phase
- **Executes** one phase (e.g., make predictions, analyze errors)
- **Updates** status file with progress
- **Stops** - waits for you to say "improve tbta" again

### The 10 Phases

1. **Feature Selection** - Pick next feature (15 min)
2. **Training Set Design** - Design 15-20 balanced training verses (1-2 hrs)
3. **Training Analysis** - Access TBTA, discover patterns (2-3 hrs)
4. **Algorithm Development** - Create algorithm v1.0 (1-2 hrs)
5. **Test Set Design** - Design adversarial + random tests (2-3 hrs)
6. **Make Predictions** - Apply algorithm WITHOUT checking TBTA (2-3 hrs)
7. **Validation** - Check TBTA, calculate accuracy (1-2 hrs)
8. **Error Analysis** - Debug every error exhaustively (3-5 hrs)
9. **Documentation** - Complete docs, share learnings (1-2 hrs)
10. **Peer Review** - Independent review, finalize (1-2 hrs)

**Total per feature**: ~20-24 hours spread across multiple sessions

## Current Status

As of 2025-11-08:

**In Progress:**
- **number-systems**: Phase 5 complete (test sets designed), ready for Phase 6 (predictions)
- **degree**: Phase 2 complete (training set designed), ready for Phase 3 (TBTA analysis)

**Not Started:**
- person-systems, participant-tracking, discourse-genre, proximity, polarity, verb-tam, time-granularity, surface-realization, honorifics-register, illocutionary-force

**Completion**: 0/12 features complete

## Key Planning Documents

The skill references these files:
- `/plan/tbta-rebuild-with-llm/README.md` - Project overview
- `/plan/tbta-rebuild-with-llm/METHODOLOGY-ADVERSARIAL.md` - Testing protocol
- `/plan/tbta-rebuild-with-llm/features/FEATURE-WORKFLOW-STATUS.yaml` - Status tracking
- `/plan/tbta-rebuild-with-llm/features/CROSS-FEATURE-LEARNINGS.md` - Universal patterns

## Quality Standards

The skill enforces:
- **Equal value coverage** - Training and test sets must have 2 examples per value
- **Adversarial testing** - Hard cases to find algorithm weaknesses
- **No TBTA peeking** - Predictions locked BEFORE checking TBTA
- **Exhaustive debugging** - 6-step analysis for every error
- **Per-value accuracy** - More informative than overall accuracy

## Workflow Principles

### Context Management
- **One phase at a time** - Prevents context pollution
- **Minimal loading** - Only load docs needed for current phase
- **Status-driven** - Status file is single source of truth

### Methodology
- **Training/test separation** - Strict separation prevents data leakage
- **Equal coverage** - Prevents algorithm bias toward common values
- **Locked predictions** - Git commit SHA before checking TBTA
- **Cross-feature learning** - Patterns feed back to improve methodology

## Usage Examples

### Start/continue work:
```
You: "improve tbta"
```

The skill will:
1. Check status file
2. Identify next phase for highest priority in-progress feature
3. Execute that phase only
4. Update status
5. Stop (wait for next "improve tbta")

### Example session:
```
You: "improve tbta"

Agent: "Executing Phase 6 for number-systems: Making predictions

Loaded algorithm v1.0 from training phase.
Applying to adversarial test set (12 verses)...
[predictions made]

Applying to random test set (12 verses)...
[predictions made]

Created:
- adversarial-test/PREDICTIONS-locked.md
- random-test/PREDICTIONS-locked.md

Committed: feat(tbta/number-systems): lock predictions (commit abc123)

✅ Phase 6 complete
📊 Status: number-systems now at Phase 7
🎯 Next: Phase 7 - Validation (check TBTA, calculate accuracy)

Say 'improve tbta' to continue."
```

## Success Metrics

### Per Feature
- Adversarial accuracy: 60-70% (hard cases)
- Random accuracy: 80-90% (typical cases)
- Gap: 15-25 points (proves test design)

### Overall Project
- **Q4 2025**: 5 features complete
- **Q1 2026**: All 12 features complete
- **Q2 2026**: Comprehensive validation
- **Q3 2026**: Production ready

## Timeline

- **Weeks 1-4**: Complete number-systems and degree
- **Months 2-3**: Complete core 5 features
- **Months 4-6**: Complete all 12 features
- **Month 7+**: Comprehensive validation and refinement

---

**Remember:** This skill maintains focus by working on ONE phase at a time. Trust the process - say "improve tbta" and let it guide you through systematic completion.
