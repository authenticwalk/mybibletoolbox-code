# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. Shift from "looking for patterns" to "testing hypotheses".

## SETUP

- $CURRENT-FEATURE-DIR: `/bible-study-tools/tbta/features/{feature}/`
- $ANALYSIS-DIR: $CURRENT-FEATURE-DIR/analysis
- Check that your CWD is `/bible-study-tools/tbta/features` if not warn user then load `/bible-study-tools/tbta/features/CLAUDE.md`

## Quick Reference

```
analysis/
├── data/
│   ├── train.jsonl      # max 300 entries
│   ├── validate.jsonl   # max 100 entries
│   ├── test.jsonl       # max 100 entries (DO NOT TOUCH until final eval)
│   └── leftovers.jsonl  # remaining entries not in train/validate/test
├── tbta-extract.jsonl   # full extraction
├── README.md            # results summary
└── logical.py           # optional rules script
```


## Step 2: Baseline Analysis

### LLM Baseline

**Process**: Run TWO baseline tests in parallel using subagents, then analyze the difference.

**Goal**: Understand (1) what the LLM already knows about this feature, and (2) how much guidance helps.

#### Test A: Zero-Shot Baseline (no definitions)

Run as: 3 Subagents
Parallel: Yes
Models: Haiku, Opus, Sonnet

Start a subagent with a minimal prompt that only lists the possible values without explaining them:

```
Label each highlighted word (**word**) with one of these {FeatureName} values:
{Value1}, {Value2}, {Value3}, ...

Return format: $verse\t$label (e.g., "GEN.001.001\tValue1")
```

Give it 100 diverse verses from `$ANALYSIS-DIR/data/train.jsonl`.

Save predictions to `$ANALYSIS-DIR/data/baseline_zero_shot_${modelName}.tsv`.

#### Test B: Guided Baseline (with definitions)

Run as: 1 Subagents
Parallel: Yes (with above)
Models: Sonnet

Start a second subagent (in parallel) with a structured prompt:

**Part A**: Write 1-3 sentences describing what the feature is and how to decide which label applies. Source this from Stage 1 `features/{feature}/research/README.md`.

**Part B**: List each possible value as a bullet point, with up to 5 sub-bullets explaining when to use that value.

**Example structure** (for a hypothetical "Tense" feature):
```
Tense indicates when an action occurs relative to the time of speaking.
Label each highlighted verb with the tense that matches when the action happens.

- Past:
  - Action completed before speaking time
  - Hebrew perfect aspect (qatal)
  - Narrative past events
- Present:
  - Action happening at speaking time
  - Gnomic/timeless truths
- Future:
  - Action not yet completed
  - Prophecies and predictions
  - Hebrew imperfect with future context
```

Give it the SAME 100 verses. Save predictions to `$ANALYSIS-DIR/data/baseline_guided.tsv`.

#### Analysis: Compare the Two Baselines

Create `$ANALYSIS-DIR/HIGH-LEVEL-REVIEW.md` with:

1. **Accuracy comparison**:
   | Test | Accuracy |
   |------|----------|
   | Zero-shot-Haiku | X1% |
   | Zero-shot-Sonnet | X2% |
   | Zero-shot-Opus | X3% |
   | Guided | Y% |
   | Improvement | +Z% |

2. **Where guidance helped**: Cases where zero-shot was wrong but guided was correct
   - What patterns does the LLM not know by default?
   - Which values needed the most guidance?

3. **Where guidance hurt**: Cases where zero-shot was correct but guided was wrong
   - Did the prompt introduce bias or confusion?
   - Are there values where the LLM's intuition is better than our definitions?

4. **Persistent errors**: Cases where BOTH got it wrong
   - These are the hard cases that need special handling
   - May indicate TBTA data quality issues

5. **LLM internal biases**: What does the zero-shot distribution tell us?
   - Does it over-use certain values?
   - Does it under-use rare values?

Include both prompts in the review file.

#### Review Checklist
   1. Did it get them all correct.  If so we don't need to do any further work but can mark this feature as done
   2. Debug why is it getting it wrong?  Is there a pattern to it?  
   3. Do the TBTA answers seem correct and consistent?  You want them to be right but be critical and think deeply about if there may be a data labelling issue that will block our results.  
   4. How should we go about solving it (consider the options listed in this stage 2 doc and propose which are most likely, suggest alternatives)
   5.  Is one value dominant (>80%)? Focus on edge cases when it's NOT that value
   6.  Any suspicious values? (e.g., Quadrial has no linguistic basis - it's semantic, not grammatical)
       1.  ex. In number systems it is almost always Singular or Plural. Less than 2% of the cases are the other values; therefore the task is finding out when it is not plural and why the Greek/Hebrew Singular would not be singular.

   **Formatting**: When citing examples, always **bold** the target word being classified so readers know which word is in question:
   - ✅ `LUK.005.019: "**man** could not enter house" → TBTA: Paucal`
   - ❌ `LUK.005.019: "man could not enter house" → TBTA: Paucal`

**Why**: Avoid overbuilding. The LLM may already have sufficient knowledge for common features.


