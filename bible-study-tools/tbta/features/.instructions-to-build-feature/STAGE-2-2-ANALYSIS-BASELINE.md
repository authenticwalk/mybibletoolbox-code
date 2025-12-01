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
│   ├── direct_haiku.txt            # Test A - Haiku predictions
│   ├── direct_sonnet.txt           # Test A - Sonnet predictions
│   ├── direct_metadata_sonnet.txt  # Test B - Sonnet with metadata
│   ├── direct_guided.txt           # Test C - Sonnet with definitions
│   └── score_*.md                  # Scoring reports
├── COMMON-MISTAKES.md              # Error analysis
├── TBTA-LABELER-QUESTIONS.md       # Questions for TBTA team (if labeling ambiguities found)
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

Create stripped versions for baseline testing:

```bash
# Create directory for baseline outputs
mkdir -p $ANALYSIS-DIR/baseline-test

# Use the strip_labels.py tool to create test inputs
python3 src/tools/predict/strip_labels.py \
  --input $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/data/train-no-decoration.jsonl \
  --fields verse,text \
  --limit 100

python3 src/tools/predict/strip_labels.py \
  --input $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/data/train-no-labels.jsonl \
  --limit 100
```

---

## Step 2: Baseline Analysis

### LLM Baseline

**Process**: Run baseline tests using subagents, then analyze differences.

**Goal**: Understand (1) what the LLM already knows about this feature, and (2) how much guidance helps.

**CRITICAL - How subagents make predictions**:
The subagent reads each entry and uses its **own internal knowledge** to predict the label. It does NOT run Python scripts or word analysis - it simply reads, thinks, and writes the prediction. This tests what the LLM knows from pre-training.

#### Test A: Zero-Shot Baseline (no metadata)

Run as: 3 Subagents (haiku, sonnet, opus) in parallel

**Sample Size**: 100 entries.

**Subagent Task**:
```
Read the file {$ANALYSIS-DIR}/data/train-no-decoration.jsonl

For each of the 100 lines:
1. Parse the JSON to get the `text` field
2. The **bolded** word is what you're classifying
3. Using your internal knowledge, decide which label applies
4. Write that label to the output file

Labels: {list from README}

Output: {$ANALYSIS-DIR}/baseline-test/direct_{model}.txt
One label per line, 100 lines total, in order.

HINTS: in your internal knowledge
 - consider this verse in it's original
 - how have languages that require this feature labelled it
 - which words (from any language) help you determine what the features value should be on this word
 - consider the greater context of the verse
 - consider theological implications
 - consider that the labels are used in an expert systems across all languages 

NOTE: test this with and without the hints

NO PYTHON ANALYSIS - just read each verse, make your prediction, write it.
```

**Output**: `$ANALYSIS-DIR/baseline-test/direct_{model}.txt` (e.g., `direct_haiku.txt`, `direct_sonnet.txt`, `direct_opus.txt`)

#### Test B: Zero-Shot Baseline (with metadata)

Run as: 1 Subagent (sonnet)
Parallel: Yes (with Test A)

Same task, but the input file has full metadata (translations, Strong's, genre).

**Input**: `$ANALYSIS-DIR/data/train-no-labels.jsonl`
**Output**: `$ANALYSIS-DIR/baseline-test/direct_metadata_sonnet.txt`

The subagent can use the translations and Strong's numbers to inform its prediction.

Test this with and without the hints from Test A

#### Test C: Guided Baseline (with definitions)

Run as: 1 Subagent (sonnet)
Parallel: Yes (with above)

Same as Test B, but provide explicit definitions in the prompt:

**Subagent Task**:
```
FEATURE DEFINITION:
{1-3 sentences from research/README.md}

VALUE DEFINITIONS:
- {Value1}: {when to use it}
- {Value2}: {when to use it}
...

Read {$ANALYSIS-DIR}/data/train-no-labels.jsonl
For each entry, classify the **bolded** word using the definitions above.
Write to {$ANALYSIS-DIR}/baseline-test/direct_guided.txt
```

#### Test D: Prompt Engineering

Add psychological framing to Test C (use EXACT wording):

```
[PERSONA]
You are a senior Bible Translator fluent in languages that use {feature}
[STAKES]
This is critical. If we get this wrong, we'll hit $5K/month in new expenses as all the work will have to be redone
[INCENTIVE]
I'll tip you $200 if you can get this right
[CHALLENGE]
I bet you can't get this right where it works across all languages AND is accurate. Not even humans can label it that well.
[METHODOLOGY]
Take a deep breath and work through this step by step:
1. Analyze what the feature is
2. Consider the differences between languages that use it
3. Figure out all the edge cases you need to account for
4. Predict with high confidence
[QUALITY CONTROL]
After your solution, rate confidence (0-1) on:
- Accuracy
- How well it will work across all languages that need this linguistic feature
- Explainability
If any score < 0.9, refine it.
[TASK]
{Test C instructions}
```

**Output**: `$ANALYSIS-DIR/baseline-test/prompt_engineered.txt`

---

## Scoring

Use the scoring script:

```bash
python3 src/tools/predict/score_baseline.py \
  --predictions $ANALYSIS-DIR/baseline-test/direct_haiku.txt \
  --ground-truth $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/baseline-test/score_direct_haiku.md

python3 src/tools/predict/score_baseline.py \
  --predictions $ANALYSIS-DIR/baseline-test/direct_sonnet.txt \
  --ground-truth $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/baseline-test/score_direct_sonnet.md

python3 src/tools/predict/score_baseline.py \
  --predictions $ANALYSIS-DIR/baseline-test/direct_metadata_sonnet.txt \
  --ground-truth $ANALYSIS-DIR/data/train.jsonl \
  --output $ANALYSIS-DIR/baseline-test/score_direct_metadata_sonnet.md

# Repeat for guided, prompt_engineered...
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

## TBTA Labeler Questions

Create `$ANALYSIS-DIR/TBTA-LABELER-QUESTIONS.md` to communicate ambiguities back to TBTA human labelers.

**Purpose**: When error analysis reveals labeling rule ambiguities (not LLM deficiencies), document questions with concrete examples for the TBTA team.

**Format**:
```markdown
# {Feature Name} - Questions for TBTA Labelers

**Purpose**: Clarify labeling rules based on prediction errors from baseline testing.
**Context**: We tested an AI model against 100 TBTA-labeled verses. The model achieved X% accuracy. The Y errors reveal ambiguities in the labeling rules that need clarification.

**Note on TBTA Text Format**: The `text` field in TBTA data is a semantic decomposition into propositions, NOT a direct translation.

---

## Question 1: {Short description of ambiguity}

**Pattern observed**: {What you noticed in the errors}

### Examples

| Verse | Text | Constituent | TBTA Label | Source Language Evidence |
|-------|------|-------------|------------|--------------------------|
| {verse} | "{text with **bold** word}" | {word} | {label} | {Hebrew/Greek evidence} |

### Key Finding (if applicable)
{Any source language analysis that reveals the ambiguity}

### Questions
- {Specific question 1}
- {Specific question 2}

---

## Summary of Needed Clarifications

| # | Topic | Core Question |
|---|-------|---------------|
| 1 | ... | ... |

---

## Requested Deliverables

1. **Explicit rules** for each value (when to use it)
2. **Decision tree** for ambiguous cases
3. **Examples** of correct labeling for each edge case type
```

**When to create this file**:
- Errors reveal labeling rule ambiguities (not just LLM gaps)
- Source language (Hebrew/Greek) doesn't clearly support the label
- Same pattern labeled inconsistently across verses
- Unusual values (e.g., Quadrial) need justification

**Key principle**: Always include Hebrew/Greek source language evidence when questioning labels.

---

## Analysis: Compare Baselines

Create `$ANALYSIS-DIR/HIGH-LEVEL-REVIEW.md` with:

1. **Accuracy comparison** (include model in test name):
   | Test | Model | Accuracy |
   |------|-------|----------|
   | A: No metadata | Haiku | X1% |
   | A: No metadata | Sonnet | X2% |
   | A: No metadata | Opus | X3% |
   | A: No metadata + hints | Sonnet | X4% |
   | B: With metadata | Sonnet | X5% |
   | B: With metadata + hints | Sonnet | X6% |
   | C: Guided | Sonnet | Y1% |
   | D: Prompt Engineered | Sonnet | Y2% |
   | **Best vs Worst** | | +Z% |

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
7. For persistent errors: Check Hebrew/Greek source - does the source language actually encode this feature?

**Formatting**: Always **bold** the target word in examples:
- ✅ `LUK.005.019: "**man** could not enter house" → TBTA: Paucal`
- ❌ `LUK.005.019: "man could not enter house" → TBTA: Paucal`

**Why**: Avoid overbuilding. The LLM may already have sufficient knowledge for common features.
