# Stage 2.2: Baseline Analysis

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1) + Dataset (Stage 2.1)
**Output**: `analysis/` (Baseline predictions, Scorecards, Error analysis)

## Goal

Quantitatively measure LLM baseline performance _before_ writing prompts. Understand what the model already knows vs what needs guidance.

## SETUP

- $CURRENT-FEATURE-DIR: `/bible-study-tools/tbta/features/{feature}/`
- $ANALYSIS-DIR: $CURRENT-FEATURE-DIR/analysis
- Check that your CWD is `/bible-study-tools/tbta/features` if not warn user then load `/bible-study-tools/tbta/features/CLAUDE.md`

## Quick Reference

```
analysis/
├── data/
│   ├── train.jsonl                 # Ground truth (from Stage 2.1)
│   ├── train-no-labels.jsonl       # Input for Test B/C/D (no label field)
│   ├── train-no-decoration.jsonl   # Input for Test A (only verse,text)
│   ├── validate.jsonl              # For validation (DO NOT USE until Stage 3)
│   ├── test.jsonl                  # Final eval (DO NOT TOUCH)
│   └── leftovers.jsonl             # Remaining entries not in splits
├── baseline-test/                  # All baseline test outputs
│   ├── baseline_no_metadata_*.txt  # Test A outputs (one label per line)
│   ├── baseline_zero_shot_*.txt    # Test B outputs
│   ├── baseline_guided.txt         # Test C output
│   └── prompt_engineered.txt       # Test D output
├── COMMON-MISTAKES.md              # Error analysis
├── HIGH-LEVEL-REVIEW.md            # Final summary
└── _LEARNINGS.md                   # Debug notes (if issues)
```

## Process

You will work through these steps calling subagents as defined in each step to keep your context clear.

**CRITICAL: How to delegate to subagents**
1. Tell the subagent to READ THIS FILE FIRST: `Read /workspace/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-2-2-ANALYSIS-BASELINE.md`
2. Tell them which step to execute (e.g., "Execute Step 2")
3. Tell them the feature name and $CURRENT-FEATURE-DIR path (IMPORTANT: You must expand the variables $CURRENT-FEATURE-DIR and $ANALYSIS-DIR to their full paths when speaking to the subagent)
4. DO NOT paraphrase the instructions - let them read the original
5. When they are done, audit their work and redo up to 3 times if needed

If you have to redo a step debug the instructions and add your analysis and fix to `$ANALYSIS-DIR/_LEARNINGS.md`

---

## Preparation

Run as: Orchestrator

Ensure you have the file `$ANALYSIS-DIR/data/train.jsonl` from Stage 2.1. If not, go back to `STAGE-2-1-ANALYSIS-DATASET.md`.

**NOTE**: train.jsonl should be a **balanced** dataset from Stage 2.1. If >10,000 entries, Stage 2.1 may have put leftovers in train.jsonl by mistake.

Create stripped versions for baseline testing (limit to first 100 for quick iteration):

```bash
# Create directory for baseline outputs
mkdir -p $ANALYSIS-DIR/baseline-test

# Create train-no-decoration.jsonl (only verse + text fields, for Test A)
head -100 $ANALYSIS-DIR/data/train.jsonl | python3 -c "
import json, sys
for line in sys.stdin:
    obj = json.loads(line)
    print(json.dumps({'verse': obj['verse'], 'text': obj['text']}))
" > $ANALYSIS-DIR/data/train-no-decoration.jsonl

# Create train-no-labels.jsonl (all fields except label, for Test B/C/D)
head -100 $ANALYSIS-DIR/data/train.jsonl | python3 -c "
import json, sys
for line in sys.stdin:
    obj = json.loads(line)
    del obj['label']
    print(json.dumps(obj))
" > $ANALYSIS-DIR/data/train-no-labels.jsonl
```

---

## Step 2: Baseline Analysis

### LLM Baseline

**Process**: Run baseline tests using subagents, then analyze differences.

**Goal**: Understand (1) what the LLM already knows about this feature, and (2) how much guidance helps.

#### Test A: Zero-Shot Baseline (no metadata)

Run as: 2 Subagents (haiku, sonnet) in parallel

**Sample Size**: 100 entries for quick iteration.

**Task for each subagent**:
1. Read `$ANALYSIS-DIR/data/train-no-decoration.jsonl`
2. For EACH line, classify the **bolded** word using ONLY the values from `$CURRENT-FEATURE-DIR/README.md`
3. Use ONLY internal knowledge (no web tools) - think about grammar, modality, linguistic context
4. Write one label per line to the output file

**Prompt Template** (apply to each verse):
```
Label the **bolded** word in this verse with one of these {FeatureName} values:
{Value1}, {Value2}, {Value3}, ...

Verse: {text}

Return ONLY the label, nothing else.
```

**Output**: `$ANALYSIS-DIR/baseline-test/baseline_no_metadata_{model}.txt` (one label per line, 100 lines)

**How to launch** (orchestrator runs these in parallel):
```
Task(model="haiku", prompt="...Execute Test A for {feature}...")
Task(model="sonnet", prompt="...Execute Test A for {feature}...")
```

#### Test B: Zero-Shot Baseline (with metadata, no definitions)

Run as: 1 Subagent (sonnet)
Parallel: Yes (with Test A)

Same as Test A, but provide the full JSON context (translations, Strong's numbers, genre, etc).

**Task**:
1. Read `$ANALYSIS-DIR/data/train-no-labels.jsonl`
2. For EACH line, classify using the metadata to inform your decision

**Prompt Template**:
```
Label the **bolded** word in this verse with one of these {FeatureName} values:
{Value1}, {Value2}, {Value3}, ...

Data:
{full json entry}

Return ONLY the label, nothing else.
```

**Output**: `$ANALYSIS-DIR/baseline-test/baseline_zero_shot_sonnet.txt`

#### Test C: Guided Baseline (with definitions)

Run as: 1 Subagent (sonnet)
Parallel: Yes (with above)

**Build a structured prompt**:

**Part A**: Write 1-3 sentences describing what the feature is and how to decide which label applies. Source from `$CURRENT-FEATURE-DIR/research/README.md`.

**Part B**: List each possible value as a bullet point, with up to 5 sub-bullets explaining when to use that value.

**Prompt Template**:
```
{Part A}

{Part B}

Data:
{full json entry}

Label the **bolded** word. Return ONLY the label.
```

**Output**: `$ANALYSIS-DIR/baseline-test/baseline_guided.txt`

#### Test D: Prompt Engineering (Optional)

Add psychological framing to Test C prompt:

```
[PERSONA]
You are a senior Bible Translator fluent in languages that use ${FEATURE-NAME}
[STAKES]
This is critical. If we get this wrong, we'll hit $5K/month in new expenses as all the work will have to be redone
[METHODOLOGY]
Take a deep breath and work through this step by step:
1. Analyze what the feature is
2. Consider the differences between languages that use it
3. Figure out all the edge cases you need to account for
4. Predict with high confidence
[TASK]
{Test C prompt here}
```

**Output**: `$ANALYSIS-DIR/baseline-test/prompt_engineered.txt`

---

## Scoring (Orchestrator runs this)

Score predictions using inline Python (no external scripts required):

```bash
cd $ANALYSIS-DIR && python3 << 'EOF'
import json
from collections import Counter

# Load ground truth (first 100 entries)
with open('data/train.jsonl', 'r') as f:
    ground_truth = [json.loads(line)['label'] for i, line in enumerate(f) if i < 100]

def score_predictions(pred_file, gt):
    with open(pred_file, 'r') as f:
        preds = [line.strip() for line in f if line.strip()]
    min_len = min(len(preds), len(gt))
    correct = sum(1 for i in range(min_len) if preds[i] == gt[i])
    errors = [(i+1, gt[i], preds[i]) for i in range(min_len) if preds[i] != gt[i]]
    return {'accuracy': correct/min_len*100, 'correct': correct, 'total': min_len, 'errors': errors}

# Score all baseline files
files = [
    ('baseline-test/baseline_no_metadata_haiku.txt', 'Haiku (no metadata)'),
    ('baseline-test/baseline_no_metadata_sonnet.txt', 'Sonnet (no metadata)'),
    ('baseline-test/baseline_zero_shot_sonnet.txt', 'Sonnet (with metadata)'),
    ('baseline-test/baseline_guided.txt', 'Sonnet (guided)'),
]

print("=" * 60)
print("BASELINE SCORING RESULTS")
print("=" * 60)
for fname, label in files:
    try:
        result = score_predictions(fname, ground_truth)
        print(f"\n{label}: {result['accuracy']:.1f}% ({result['correct']}/{result['total']})")
        print("  First 5 errors:")
        for idx, gt_l, pred_l in result['errors'][:5]:
            print(f"    Line {idx}: Expected '{gt_l}' got '{pred_l}'")
    except FileNotFoundError:
        print(f"\n{label}: NOT FOUND")

print(f"\n\nGround Truth Distribution:")
for label, count in Counter(ground_truth).most_common():
    print(f"  {label}: {count}")
EOF
```

---

## Error Analysis

Create `$ANALYSIS-DIR/COMMON-MISTAKES.md` covering:

**Repeated Mistakes**: Group same mistakes into unique groups
- Table format: | Verse | Text (with **bold** word) | TBTA Label | Haiku | Sonnet | Guided |
- Debug root cause:
  - Label ambiguity (e.g., must/should overlap)
  - Human labelling inconsistency in TBTA
  - Differences in how feature is implemented across languages
  - LLM biases or assumptions
- Suggest resolution approaches:
  - Prompt edits (prefer simple over complex)
  - Adding notes to specific verses/strongs (up to 100 edge cases acceptable)
  - Alternative output format: dominant-answer + alternate-answers with rationale

**One-offs**: Same format but note small sample size caveat

---

## Analysis: Compare Baselines

Create `$ANALYSIS-DIR/HIGH-LEVEL-REVIEW.md` with:

1. **Accuracy comparison**:
   | Test | Accuracy |
   |------|----------|
   | No metadata - Haiku | X1% |
   | No metadata - Sonnet | X2% |
   | With metadata - Sonnet | X3% |
   | Guided - Sonnet | Y% |
   | Improvement (best vs worst) | +Z% |

2. **Where guidance helped**: Cases where zero-shot was wrong but guided was correct
   - What patterns does the LLM not know by default?
   - Which values needed the most guidance?

3. **Where guidance hurt**: Cases where zero-shot was correct but guided was wrong
   - Did the prompt introduce bias or confusion?

4. **Persistent errors**: Cases where ALL tests got it wrong
   - May indicate TBTA data quality issues

5. **LLM internal biases**:
   - Does it over-use certain values?
   - Does it under-use rare values?

Include prompts used in the review file.

---

## Review Checklist

1. Did any test achieve 100%? If so, feature may be done
2. Is there a pattern to the errors?
3. Do TBTA answers seem correct and consistent? (Be critical - data quality issues block progress)
4. How should we solve it? (prompt edits, edge case notes, different output format)
5. Is one value dominant (>80%)? Focus on edge cases for minority values
6. Any suspicious values with no linguistic basis?

**Formatting**: Always **bold** the target word in examples:
- ✅ `LUK.005.019: "**man** could not enter house" → TBTA: Paucal`
- ❌ `LUK.005.019: "man could not enter house" → TBTA: Paucal`

**Why**: Avoid overbuilding. The LLM may already have sufficient knowledge for common features.
