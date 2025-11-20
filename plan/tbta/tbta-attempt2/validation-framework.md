# TBTA Features Validation Framework

**Version**: 1.0
**Purpose**: Comprehensive validation system to ensure TBTA features meet production standards
**Date**: 2025-11-16
**Status**: Active Framework

---

## Executive Summary

This framework provides:
1. **Automated validation scripts** for file structure, stage completion, and accuracy metrics
2. **Blind testing protocols** to prevent answer contamination during validation
3. **Quality gates** between stages to prevent premature advancement
4. **Peer review coordination** using subagents with diverse expertise

All features must pass ALL critical checks before production release.

---

## Production Readiness Checklist

### Stage Completion Requirements

Features must complete ALL stages in STAGES.md to be production-ready:

- [ ] **Stage 1**: Research TBTA Documentation - README.md exists with feature definition
- [ ] **Stage 2**: Language Study - Language analysis documented in README.md
- [ ] **Stage 3**: Scholarly Research - Internet and scholarly sources integrated
- [ ] **Stage 4**: Test Set Generation - train/test/validate sets exist (≥100 verses per value)
- [ ] **Stage 5**: Hypothesis Testing - LEARNINGS.md documents iterative improvements
- [ ] **Stage 6**: Validation & Peer Review - All 4 peer reviews pass + accuracy ≥95%

### File Structure Requirements

#### Required Files

```bash
features/{feature}/
├── README.md                         # Feature documentation with stage checklist
├── experiments/
│   ├── train.yaml                    # Training set (40%)
│   ├── test.yaml                     # Test set (30%)
│   ├── validate.yaml                 # Validation set (30%)
│   ├── ANALYSIS.md                   # Up to 12 approaches analyzed
│   ├── PROMPT1.md                    # First hypothesis
│   ├── PROMPT2.md                    # Alternative approach (if needed)
│   ├── PROMPT{N}.md                  # Refined prompts (as needed)
│   ├── LEARNINGS.md                  # Iteration learnings and error analysis
│   ├── TRANSLATOR-IMPACT.md          # Real-world translation testing
│   └── TBTA-REVIEW.md                # TBTA team review request (if applicable)
└── CROSS-FEATURE-LEARNINGS.md        # Transferable patterns (shared across features)
```

#### Optional Files
```bash
features/{feature}/
└── experiments/
    ├── EXTERNAL-VALIDATION.md        # Translation validation (if applicable)
    └── predictions/
        ├── prompt1-test-predictions.yaml       # Locked predictions
        ├── prompt1-validate-predictions.yaml   # Final predictions
        └── commit-shas.yaml                    # Git commit verification
```

### Accuracy Metrics

#### Minimum Standards

From STAGES.md Stage 5:

- **Stated values** (single answer): **100% accuracy** goal
  - Caveat: Small datasets (<50 verses) cannot reliably demonstrate 100%
  - Minimum sample size: 100 verses per value

- **Dominant values** (primary + rationale): **95% accuracy** goal

#### Sample Size Requirements

From STAGES.md Stage 4:

- **Minimum**: 100 verses per value
- **Rationale**: Statistical power to distinguish algorithm quality from chance
- **Distribution**: Balanced across:
  - Testament (OT/NT proportional)
  - Genre (narrative/poetry/prophecy/epistle)
  - Book distribution (avoid concentration)
  - Difficulty (typical + adversarial cases)

### Peer Review Documentation

#### Required Reviews (Stage 6)

All 4 subagent reviews must be documented:

1. **Theological Reviewer**: Check doctrinal soundness
   - File: `experiments/reviews/theological-review.md`
   - Status: [PASS/FAIL/MATERIAL FEEDBACK]

2. **Linguistic Reviewer**: Check linguistic accuracy
   - File: `experiments/reviews/linguistic-review.md`
   - Status: [PASS/FAIL/MATERIAL FEEDBACK]

3. **Methodological Reviewer**: Check rigor
   - File: `experiments/reviews/methodological-review.md`
   - Status: [PASS/FAIL/MATERIAL FEEDBACK]

4. **Translation Practitioner**: Real-world testing
   - File: `experiments/TRANSLATOR-IMPACT.md`
   - Status: [PASS/FAIL/MATERIAL FEEDBACK]

#### Review Status Definitions

- **PASS**: Non-material feedback only, proceed to production
- **MATERIAL FEEDBACK**: Issues that require prompt refinement
- **FAIL**: Critical flaws, return to Stage 5

### Git Commit Verification

#### Locked Predictions Protocol

From STAGES.md Stage 5:

Before testing any prompt against TBTA data:

```bash
# 1. Generate predictions (WITHOUT seeing TBTA answers)
# 2. Commit predictions to git
git add experiments/predictions/prompt{N}-{set}-predictions.yaml
git commit -m "feat({feature}): lock PROMPT{N} predictions before TBTA check"
git push origin {branch}

# 3. Record commit SHA
echo "prompt{N}_{set}: $(git rev-parse HEAD)" >> experiments/predictions/commit-shas.yaml
```

**Purpose**: Prevents unconscious bias from seeing correct answers before predicting.

---

## Automated Validation Scripts

### Script 1: File Structure Validator

**Purpose**: Verify all required files exist for each stage.

**Location**: `/workspace/scripts/validation/validate-file-structure.sh`

```bash
#!/bin/bash
# validate-file-structure.sh
# Usage: ./validate-file-structure.sh features/{feature}

FEATURE_DIR="$1"
ERRORS=0

# Check required files exist
required_files=(
  "README.md"
  "experiments/train.yaml"
  "experiments/test.yaml"
  "experiments/validate.yaml"
  "experiments/ANALYSIS.md"
  "experiments/LEARNINGS.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$FEATURE_DIR/$file" ]]; then
    echo "❌ MISSING: $file"
    ((ERRORS++))
  else
    echo "✅ FOUND: $file"
  fi
done

# Check for at least one prompt file
if ! ls "$FEATURE_DIR"/experiments/PROMPT*.md 1> /dev/null 2>&1; then
  echo "❌ MISSING: No PROMPT*.md files found"
  ((ERRORS++))
else
  echo "✅ FOUND: Prompt files exist"
fi

# Check peer review files
review_files=(
  "experiments/reviews/theological-review.md"
  "experiments/reviews/linguistic-review.md"
  "experiments/reviews/methodological-review.md"
  "experiments/TRANSLATOR-IMPACT.md"
)

for file in "${review_files[@]}"; do
  if [[ ! -f "$FEATURE_DIR/$file" ]]; then
    echo "⚠️  MISSING (Stage 6): $file"
  else
    echo "✅ FOUND: $file"
  fi
done

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "❌ VALIDATION FAILED: $ERRORS required files missing"
  exit 1
else
  echo ""
  echo "✅ VALIDATION PASSED: All required files present"
  exit 0
fi
```

### Script 2: Stage Checklist Validator

**Purpose**: Verify all stages in README.md are marked complete.

**Location**: `/workspace/scripts/validation/validate-stages.py`

```python
#!/usr/bin/env python3
"""
validate-stages.py
Usage: ./validate-stages.py features/{feature}/README.md
"""

import sys
import re

def validate_stages(readme_path):
    with open(readme_path, 'r') as f:
        content = f.read()

    # Find all stage checklists
    stages = {
        1: "Research TBTA Documentation",
        2: "Language Study",
        3: "Scholarly and Internet Research",
        4: "Generate a Proper Test Set",
        5: "Propose your Hypothesis and First Prompt",
        6: "Test Against Validate Set & Peer Review"
    }

    incomplete_stages = []

    for stage_num, stage_name in stages.items():
        # Find stage section
        pattern = rf"# {stage_num}\. {re.escape(stage_name)}"
        match = re.search(pattern, content)

        if not match:
            print(f"⚠️  Stage {stage_num} section not found in README")
            continue

        # Find next stage or end of file
        next_stage = stage_num + 1
        if next_stage in stages:
            next_pattern = rf"# {next_stage}\."
            next_match = re.search(next_pattern, content)
            section_end = next_match.start() if next_match else len(content)
        else:
            section_end = len(content)

        # Check section for unchecked boxes
        section = content[match.start():section_end]
        unchecked = re.findall(r'- \[ \]', section)

        if unchecked:
            print(f"❌ Stage {stage_num} incomplete: {len(unchecked)} unchecked items")
            incomplete_stages.append(stage_num)
        else:
            print(f"✅ Stage {stage_num} complete")

    if incomplete_stages:
        print(f"\n❌ VALIDATION FAILED: Stages {incomplete_stages} incomplete")
        return False
    else:
        print(f"\n✅ VALIDATION PASSED: All stages complete")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./validate-stages.py features/{feature}/README.md")
        sys.exit(1)

    success = validate_stages(sys.argv[1])
    sys.exit(0 if success else 1)
```

### Script 3: Sample Size Validator

**Purpose**: Verify dataset meets minimum sample size requirements.

**Location**: `/workspace/scripts/validation/validate-sample-size.py`

```python
#!/usr/bin/env python3
"""
validate-sample-size.py
Usage: ./validate-sample-size.py features/{feature}/experiments
"""

import sys
import yaml
from pathlib import Path
from collections import defaultdict

MIN_VERSES_PER_VALUE = 100

def validate_sample_size(experiments_dir):
    experiments_path = Path(experiments_dir)
    errors = []

    # Check each dataset file
    for dataset in ['train.yaml', 'test.yaml', 'validate.yaml']:
        file_path = experiments_path / dataset

        if not file_path.exists():
            errors.append(f"Missing {dataset}")
            continue

        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)

        # Count verses per value
        value_counts = defaultdict(int)
        for verse in data.get('verses', []):
            value = verse.get('tbta_value', 'unknown')
            value_counts[value] += 1

        # Check minimums
        for value, count in value_counts.items():
            if count < MIN_VERSES_PER_VALUE:
                errors.append(
                    f"{dataset}: Value '{value}' has only {count} verses "
                    f"(minimum {MIN_VERSES_PER_VALUE})"
                )
                print(f"❌ {dataset}: '{value}' = {count} verses (< {MIN_VERSES_PER_VALUE})")
            else:
                print(f"✅ {dataset}: '{value}' = {count} verses")

    if errors:
        print(f"\n❌ VALIDATION FAILED:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print(f"\n✅ VALIDATION PASSED: All values meet minimum sample size")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./validate-sample-size.py features/{feature}/experiments")
        sys.exit(1)

    success = validate_sample_size(sys.argv[1])
    sys.exit(0 if success else 1)
```

### Script 4: Accuracy Calculator

**Purpose**: Calculate accuracy metrics for predictions vs TBTA.

**Location**: `/workspace/scripts/validation/calculate-accuracy.py`

```python
#!/usr/bin/env python3
"""
calculate-accuracy.py
Usage: ./calculate-accuracy.py {predictions.yaml} {validate.yaml}

Compares predictions against TBTA ground truth.
Returns accuracy percentage and error list.
"""

import sys
import yaml

def calculate_accuracy(predictions_path, validate_path):
    # Load files
    with open(predictions_path, 'r') as f:
        predictions = yaml.safe_load(f)

    with open(validate_path, 'r') as f:
        validate = yaml.safe_load(f)

    # Create lookup dict for TBTA answers
    tbta_answers = {}
    for verse in validate.get('verses', []):
        ref = verse['reference']
        tbta_answers[ref] = verse['tbta_value']

    # Compare predictions
    total = 0
    correct = 0
    errors = []

    for prediction in predictions.get('predictions', []):
        ref = prediction['reference']
        predicted = prediction['predicted_value']

        if ref not in tbta_answers:
            print(f"⚠️  Warning: {ref} not in validation set")
            continue

        actual = tbta_answers[ref]
        total += 1

        if predicted == actual:
            correct += 1
        else:
            errors.append({
                'reference': ref,
                'predicted': predicted,
                'actual': actual
            })

    accuracy = (correct / total * 100) if total > 0 else 0

    print(f"Total predictions: {total}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {len(errors)}")
    print(f"Accuracy: {accuracy:.2f}%")

    if errors:
        print(f"\nErrors:")
        for error in errors:
            print(f"  {error['reference']}: {error['predicted']} → {error['actual']}")

    # Return error list for further analysis
    return {
        'total': total,
        'correct': correct,
        'accuracy': accuracy,
        'errors': errors
    }

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./calculate-accuracy.py {predictions.yaml} {validate.yaml}")
        sys.exit(1)

    result = calculate_accuracy(sys.argv[1], sys.argv[2])

    # Exit with success only if accuracy ≥ 95%
    sys.exit(0 if result['accuracy'] >= 95 else 1)
```

---

## Quality Gates Between Stages

### Gate 1→2: Research Complete

**Requirements**:
- [ ] README.md exists with feature definition
- [ ] TBTA documentation reviewed
- [ ] Stage 1 checklist all checked

**Validation**:
```bash
./scripts/validation/validate-file-structure.sh features/{feature}
./scripts/validation/validate-stages.py features/{feature}/README.md
```

### Gate 2→3: Language Analysis Complete

**Requirements**:
- [ ] Language families documented in README.md
- [ ] Stage 2 checklist all checked

**Validation**: Manual review of README.md language section

### Gate 3→4: Research Complete

**Requirements**:
- [ ] Scholarly sources integrated
- [ ] Web research documented
- [ ] Stage 3 checklist all checked

**Validation**: Manual review of README.md research section

### Gate 4→5: Test Sets Generated

**Requirements**:
- [ ] train.yaml exists with ≥100 verses per value
- [ ] test.yaml exists with ≥100 verses per value
- [ ] validate.yaml exists with ≥100 verses per value
- [ ] Balanced sampling verified
- [ ] Stage 4 checklist all checked

**Validation**:
```bash
./scripts/validation/validate-file-structure.sh features/{feature}
./scripts/validation/validate-sample-size.py features/{feature}/experiments
```

### Gate 5→6: Hypothesis Validated

**Requirements**:
- [ ] Test set accuracy ≥95%
- [ ] Predictions locked via git commits
- [ ] LEARNINGS.md documents iterations
- [ ] Stage 5 checklist all checked

**Validation**:
```bash
# Verify git commits exist
git log --grep="lock PROMPT" -- features/{feature}/experiments/predictions/

# Calculate test set accuracy
./scripts/validation/calculate-accuracy.py \
  features/{feature}/experiments/predictions/prompt{N}-test-predictions.yaml \
  features/{feature}/experiments/test.yaml
```

### Gate 6→Production: Peer Review Passed

**Requirements**:
- [ ] Validate set accuracy ≥95%
- [ ] All 4 peer reviews documented
- [ ] All peer reviews marked PASS or non-material feedback only
- [ ] TRANSLATOR-IMPACT.md shows net positive benefit
- [ ] Stage 6 checklist all checked

**Validation**:
```bash
# Calculate validate set accuracy
./scripts/validation/calculate-accuracy.py \
  features/{feature}/experiments/predictions/prompt{N}-validate-predictions.yaml \
  features/{feature}/experiments/validate.yaml

# Check all review files exist
./scripts/validation/validate-file-structure.sh features/{feature}

# Manual review of peer feedback
```

---

## Blind Testing Protocol

### Purpose

Prevent answer contamination during validation by ensuring:
1. Predictor agent NEVER sees TBTA ground truth
2. Scorer agent NEVER reveals answers to main agent
3. Main agent analyzes errors WITHOUT seeing correct answers initially

### Protocol Steps

#### Step 1: Blind Prediction (Subagent)

**Subagent Role**: Predictor (has NO access to TBTA answers)

**Input**:
- Prompt file (e.g., `PROMPT3.md`)
- Dataset file with verses BUT without `tbta_value` field

**Process**:
```python
# predictor_agent.py
# Load validate.yaml but strip TBTA answers
with open('validate.yaml', 'r') as f:
    data = yaml.safe_load(f)

verses_without_answers = []
for verse in data['verses']:
    verses_without_answers.append({
        'reference': verse['reference'],
        'text': verse.get('text', ''),
        'genre': verse.get('genre', ''),
        'difficulty': verse.get('difficulty', '')
    })

# Apply prompt to each verse
predictions = []
for verse in verses_without_answers:
    predicted_value = apply_prompt(prompt, verse)
    predictions.append({
        'reference': verse['reference'],
        'predicted_value': predicted_value,
        'reasoning': "..." # Optional
    })

# Save predictions
with open('predictions.yaml', 'w') as f:
    yaml.dump({'predictions': predictions}, f)
```

**Output**:
- `experiments/predictions/prompt{N}-{set}-predictions.yaml`

**Git Lock**:
```bash
git add experiments/predictions/prompt{N}-{set}-predictions.yaml
git commit -m "feat({feature}): lock PROMPT{N} predictions before TBTA check"
git push
echo "prompt{N}_{set}: $(git rev-parse HEAD)" >> experiments/predictions/commit-shas.yaml
```

**Return to Main Agent**: ONLY the file path, no content

#### Step 2: Blind Scoring (Different Subagent)

**Subagent Role**: Scorer (HAS access to TBTA answers)

**Input**:
- Predictions file from Step 1
- Full validate.yaml with TBTA ground truth

**Process**:
```python
# scorer_agent.py
# Load predictions and ground truth
with open('predictions.yaml', 'r') as f:
    predictions = yaml.safe_load(f)

with open('validate.yaml', 'r') as f:
    ground_truth = yaml.safe_load(f)

# Calculate accuracy WITHOUT revealing answers
results = calculate_accuracy(predictions, ground_truth)

# Return ONLY statistics + error references (no answers)
output = {
    'accuracy': results['accuracy'],
    'total': results['total'],
    'correct': results['correct'],
    'error_references': [e['reference'] for e in results['errors']]
    # DO NOT include predicted/actual values
}
```

**Output**:
- Accuracy percentage
- Total count
- List of error verse references ONLY (no values shown)

**Return to Main Agent**: Statistics + error references WITHOUT answers

#### Step 3: Error Analysis (Main Agent)

**Main Agent Role**: Analyst (learns from errors WITHOUT initial answer exposure)

**Input**:
- List of error verse references
- Access to Bible text, translations, commentaries
- NO access to TBTA values yet

**Process - 6-Step Error Analysis** (from STAGES.md):

For each error reference:

1. **Re-analyze source text** (Greek/Hebrew)
2. **Re-analyze context** (surrounding verses)
3. **Check translations** (3+ versions)
4. **Form hypothesis** about what value SHOULD be
5. **THEN check TBTA** answer
6. **Document learning** in LEARNINGS.md

**Output**: LEARNINGS.md with error analysis

#### Step 4: Verification

Only AFTER analysis, main agent verifies:

```bash
# Now main agent can see predictions vs actual
./scripts/validation/calculate-accuracy.py \
  experiments/predictions/prompt{N}-validate-predictions.yaml \
  experiments/validate.yaml
```

### Subagent Coordination Template

**Main Agent Task**:
```python
# Launch blind prediction subagent
Task(
    "Blind Predictor",
    f"""
    Apply PROMPT{N}.md to validate.yaml WITHOUT seeing TBTA answers.

    1. Load validate.yaml and strip tbta_value field
    2. Apply prompt to each verse
    3. Save predictions to predictions.yaml
    4. Git commit with message: "feat({feature}): lock PROMPT{N} predictions"
    5. Return ONLY the commit SHA

    DO NOT show me any predictions or answers.
    """,
    "tester"
)

# Launch blind scorer subagent
Task(
    "Blind Scorer",
    f"""
    Compare predictions.yaml to validate.yaml ground truth.

    1. Load both files
    2. Calculate accuracy
    3. Identify error references
    4. Return ONLY: accuracy percentage + list of error verse references

    DO NOT show predicted or actual values.
    """,
    "tester"
)
```

---

## Peer Review Coordination

### Review Template Structure

Each peer review should use this template:

```markdown
# {Review Type} Review: {Feature Name}

**Reviewer**: Subagent assuming {specific persona}
**Date**: YYYY-MM-DD
**Prompt Version**: PROMPT{N}.md
**Validation Accuracy**: {X}%

## Review Assumptions

I am reviewing this work assuming the author is a junior who may have:
- {specific blind spots for this persona}
- {common errors this persona would catch}

## Critical Issues (Must Fix)

1. {Issue description}
   - **Evidence**: {specific examples}
   - **Impact**: {what breaks if not fixed}
   - **Recommendation**: {how to fix}

## Material Feedback (Should Fix)

1. {Issue description}
   - **Evidence**: {examples}
   - **Impact**: {quality degradation}
   - **Recommendation**: {improvement}

## Non-Material Observations

- {Minor points for consideration}

## Overall Assessment

- **Status**: [PASS / MATERIAL FEEDBACK / FAIL]
- **Recommendation**: {proceed to production / return to Stage 5 / major rework}
```

### Review 1: Theological Review

**Persona**: Assume author has theological blind spots

**Focus Areas**:
- [ ] Handles divine speech correctly
- [ ] Accounts for prayer contexts
- [ ] Works in prophetic literature
- [ ] Addresses key doctrinal distinctions
- [ ] No theological oversimplifications
- [ ] No category errors

**Template**: `/workspace/plan/tbta-attempt2/templates/theological-review-template.md`

### Review 2: Linguistic Review

**Persona**: Assume author missed linguistic nuances

**Focus Areas**:
- [ ] Handles genre differences
- [ ] Distinguishes grammar vs semantics
- [ ] Accounts for discourse complexity
- [ ] Handles quoted speech
- [ ] Works with multiple speakers
- [ ] Narrative vs direct address distinction

**Template**: `/workspace/plan/tbta-attempt2/templates/linguistic-review-template.md`

### Review 3: Methodological Review

**Persona**: Assume author cut corners

**Focus Areas**:
- [ ] Sample size adequate (n≥100 per value)
- [ ] Balanced sampling (OT/NT, genres)
- [ ] Error analysis rigorous (6-step process)
- [ ] Locked predictions discipline (git commits)
- [ ] External validation attempted (if applicable)

**Template**: `/workspace/plan/tbta-attempt2/templates/methodological-review-template.md`

### Review 4: Translation Practitioner

**Persona**: Bible translator in target language

**Focus Areas**:
- [ ] Data actually useful for translation
- [ ] Helpful vs confusing annotations
- [ ] Potential translation mistakes identified
- [ ] Algorithm guidance matches real challenges
- [ ] Works for both marking and non-marking languages

**Template**: `/workspace/plan/tbta-attempt2/templates/practitioner-review-template.md`

### Parallel Review Execution

**Main Agent Coordination**:

```python
# Launch all 4 peer reviews in parallel
reviews = [
    Task(
        "Theological Reviewer",
        f"""
        Review {feature} PROMPT{N}.md for theological soundness.
        Use template: templates/theological-review-template.md

        Assume author is junior with potential blind spots:
        - May not handle divine speech correctly
        - May miss prayer context implications
        - May oversimplify doctrinal distinctions

        Test edge cases and return review file.
        """,
        "reviewer"
    ),

    Task(
        "Linguistic Reviewer",
        f"""
        Review {feature} PROMPT{N}.md for linguistic accuracy.
        Use template: templates/linguistic-review-template.md

        Assume author missed nuances:
        - Genre differences
        - Discourse complexity
        - Quoted speech handling

        Return review file.
        """,
        "reviewer"
    ),

    Task(
        "Methodological Reviewer",
        f"""
        Review {feature} methodology for rigor.
        Use template: templates/methodological-review-template.md

        Assume author cut corners:
        - Check sample size adequacy
        - Verify error analysis depth
        - Confirm git commit discipline

        Return review file.
        """,
        "reviewer"
    ),

    Task(
        "Translation Practitioner",
        f"""
        Test {feature} from translator perspective.
        Use template: templates/practitioner-review-template.md

        Translate 5-10 verses using TBTA data:
        - What mistakes avoided?
        - What mistakes made?
        - Net benefit analysis

        Return TRANSLATOR-IMPACT.md
        """,
        "reviewer"
    )
]

# Wait for all reviews to complete
# Analyze feedback and categorize as:
# - CRITICAL (must fix)
# - IMPORTANT (should fix)
# - NICE-TO-HAVE (consider)
```

---

## Complete Validation Workflow

### Full Feature Validation

```bash
#!/bin/bash
# full-validation.sh
# Usage: ./full-validation.sh features/{feature}

FEATURE="$1"
echo "Validating feature: $FEATURE"

# Stage completion
echo "=== Checking stage completion ==="
python scripts/validation/validate-stages.py "$FEATURE/README.md" || exit 1

# File structure
echo "=== Checking file structure ==="
./scripts/validation/validate-file-structure.sh "$FEATURE" || exit 1

# Sample sizes
echo "=== Checking sample sizes ==="
python scripts/validation/validate-sample-size.py "$FEATURE/experiments" || exit 1

# Accuracy on validate set
echo "=== Checking validate set accuracy ==="
LATEST_PROMPT=$(ls -1 "$FEATURE"/experiments/PROMPT*.md | tail -1 | sed 's/.*PROMPT\([0-9]*\).*/\1/')
python scripts/validation/calculate-accuracy.py \
  "$FEATURE/experiments/predictions/prompt${LATEST_PROMPT}-validate-predictions.yaml" \
  "$FEATURE/experiments/validate.yaml" || exit 1

# Peer reviews exist
echo "=== Checking peer reviews ==="
for review in theological linguistic methodological; do
  if [[ ! -f "$FEATURE/experiments/reviews/${review}-review.md" ]]; then
    echo "❌ Missing ${review} review"
    exit 1
  fi
done

if [[ ! -f "$FEATURE/experiments/TRANSLATOR-IMPACT.md" ]]; then
  echo "❌ Missing TRANSLATOR-IMPACT.md"
  exit 1
fi

echo ""
echo "✅ FULL VALIDATION PASSED"
echo "Feature is PRODUCTION READY"
```

---

## Summary: Production Readiness Criteria

A feature is production-ready when:

1. ✅ **All stages complete** (STAGES.md checklist)
2. ✅ **All required files present** (file structure validator)
3. ✅ **Sample size adequate** (≥100 verses per value)
4. ✅ **Validate accuracy ≥95%** (accuracy calculator)
5. ✅ **All peer reviews documented** (4 review files exist)
6. ✅ **All peer reviews pass** (PASS or non-material feedback only)
7. ✅ **Translation testing positive** (net benefit documented)
8. ✅ **Git commits verified** (locked predictions throughout)

**Only when all 8 criteria met**: Mark feature as production-ready.

---

## Appendices

### Appendix A: Error Classification

Common error categories from 6-step analysis:

1. **Data Errors**: TBTA annotation incorrect (rare)
2. **Prompt Errors**: Algorithm missed a pattern
3. **Context Errors**: Insufficient surrounding verse analysis
4. **Genre Errors**: Different rule for this genre
5. **Theological Errors**: Doctrinal nuance missed
6. **Edge Case Errors**: Adversarial case not covered

### Appendix B: Iteration Tracking

Track prompt evolution in LEARNINGS.md:

```markdown
## Prompt Evolution

### PROMPT1 (v1.0)
- **Approach**: {description}
- **Test Accuracy**: {X}%
- **Key Errors**: {patterns}
- **Learning**: {what didn't work}

### PROMPT2 (v2.0)
- **Approach**: {different approach}
- **Test Accuracy**: {X}%
- **Key Errors**: {patterns}
- **Learning**: {what changed}

### PROMPT3 (v2.1)
- **Approach**: {refined v2.0}
- **Test Accuracy**: {X}%
- **Validate Accuracy**: {X}%
- **Status**: Production candidate
```

### Appendix C: External Validation (When Applicable)

If feature has observable translation differences:

1. Identify marking languages (e.g., clusivity in Austronesian)
2. Find Bible translations in those languages
3. Check predictions against translator decisions
4. Document agreement rate (target: 95%+)
5. Note systematic divergences

---

**Framework Status**: Active
**Next Review**: After first feature completes Stage 6
**Maintainer**: TBTA Hive Mind Validation Team
