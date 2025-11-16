# TBTA Attempt 2: Hive Mind Coordinated Feature Development

**Status**: Planning Phase
**Created**: 2025-11-16
**Purpose**: Systematic TBTA feature development using Hive Mind coordination

---

## Overview

This attempt uses coordinated subagents (Hive Mind pattern) to develop TBTA features following STAGES.md systematically. Each agent has specialized expertise and all coordinate through shared memory.

## Key Documents

### Planning Documents (Created)

1. **feature-inventory.yaml** - Complete inventory of 72 TBTA features with status analysis
2. **INVENTORY-SUMMARY.md** - Executive summary of feature status and recommendations
3. **reusable-patterns.md** - Identified patterns across completed features
4. **execution-plan.md** - Detailed execution strategy for Hive Mind coordination
5. **validation-framework.md** - Comprehensive validation system (THIS DOCUMENT)

### Review Templates

Located in `/templates/`:
1. **theological-review-template.md** - Divine speech, prayer, prophetic literature
2. **linguistic-review-template.md** - Genre, grammar, discourse complexity
3. **methodological-review-template.md** - Sample size, error analysis, git discipline
4. **practitioner-review-template.md** - Real-world translation testing

## Validation Framework Summary

The validation framework provides:

### 1. Automated Validation Scripts

**File Structure Validator** (`validate-file-structure.sh`):
- Checks all required files exist for each stage
- Verifies experiment files present
- Confirms peer review files exist

**Stage Checklist Validator** (`validate-stages.py`):
- Parses README.md for stage sections
- Counts unchecked boxes per stage
- Reports incomplete stages

**Sample Size Validator** (`validate-sample-size.py`):
- Verifies ≥100 verses per value in each dataset
- Checks balanced distribution
- Reports inadequate samples

**Accuracy Calculator** (`calculate-accuracy.py`):
- Compares predictions vs TBTA ground truth
- Calculates accuracy percentage
- Returns error list for analysis

### 2. Blind Testing Protocol

**Purpose**: Prevent answer contamination

**Three-Step Process**:
1. **Blind Predictor Subagent**: Applies prompt WITHOUT seeing TBTA answers
2. **Blind Scorer Subagent**: Calculates accuracy WITHOUT revealing answers
3. **Main Agent**: Analyzes errors using 6-step process BEFORE seeing answers

**Git Discipline**: All predictions locked via commit before checking TBTA

### 3. Quality Gates Between Stages

**Gate 1→2**: Research complete (README.md exists)
**Gate 2→3**: Language analysis documented
**Gate 3→4**: Scholarly research integrated
**Gate 4→5**: Test sets generated (≥100 verses per value)
**Gate 5→6**: Test accuracy ≥95%, predictions locked
**Gate 6→Production**: Validate accuracy ≥95%, all peer reviews pass

### 4. Peer Review Coordination

**Four Required Reviews**:
1. **Theological Reviewer**: Doctrinal soundness, divine speech handling
2. **Linguistic Reviewer**: Genre sensitivity, discourse complexity
3. **Methodological Reviewer**: Sample size, error analysis rigor
4. **Translation Practitioner**: Real-world translation testing

**Status Definitions**:
- **PASS**: Non-material feedback only → Proceed to production
- **MATERIAL FEEDBACK**: Issues require prompt refinement → Return to Stage 5
- **FAIL**: Critical flaws → Major rework

## Production Readiness Criteria

A feature is production-ready when ALL 8 criteria met:

1. ✅ All stages complete (STAGES.md checklist)
2. ✅ All required files present (file structure validator)
3. ✅ Sample size adequate (≥100 verses per value)
4. ✅ Validate accuracy ≥95% (accuracy calculator)
5. ✅ All peer reviews documented (4 review files exist)
6. ✅ All peer reviews pass (PASS or non-material feedback only)
7. ✅ Translation testing positive (net benefit documented)
8. ✅ Git commits verified (locked predictions throughout)

## Usage

### Run Full Validation

```bash
# Complete validation check
./scripts/validation/full-validation.sh features/{feature}
```

### Individual Checks

```bash
# File structure
./scripts/validation/validate-file-structure.sh features/{feature}

# Stage completion
./scripts/validation/validate-stages.py features/{feature}/README.md

# Sample sizes
./scripts/validation/validate-sample-size.py features/{feature}/experiments

# Accuracy
./scripts/validation/calculate-accuracy.py \
  features/{feature}/experiments/predictions/prompt{N}-validate-predictions.yaml \
  features/{feature}/experiments/validate.yaml
```

### Peer Reviews

```bash
# Use templates to structure reviews
templates/theological-review-template.md
templates/linguistic-review-template.md
templates/methodological-review-template.md
templates/practitioner-review-template.md
```

## Next Steps

1. **Architect Agent**: Design subagent coordination system
2. **Implementation**: Create validation scripts in `/workspace/scripts/validation/`
3. **Testing**: Run validation on existing features (participant-tracking, person-systems)
4. **Execution**: Begin systematic feature development using Hive Mind

## Files Created

```
/workspace/plan/tbta-attempt2/
├── README.md (this file)
├── feature-inventory.yaml
├── INVENTORY-SUMMARY.md
├── reusable-patterns.md
├── execution-plan.md
├── validation-framework.md
└── templates/
    ├── theological-review-template.md
    ├── linguistic-review-template.md
    ├── methodological-review-template.md
    └── practitioner-review-template.md
```

## Reference Documents

- **STAGES.md**: `/workspace/plan/tbta-rebuild-with-llm/features/STAGES.md`
- **REVIEW-GUIDELINES.md**: `/workspace/REVIEW-GUIDELINES.md`
- **Execution Plan**: `execution-plan.md`
- **Validation Framework**: `validation-framework.md`

---

**Status**: Validation framework complete, ready for implementation
**Next Phase**: Create validation scripts and test on existing features
