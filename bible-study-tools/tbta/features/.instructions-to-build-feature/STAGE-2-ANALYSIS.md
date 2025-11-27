# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. Shift from "looking for patterns" to "testing hypotheses".

## Context

- Relative directory: `/bible-study-tools/tbta/features/{feature}/`
- TBTA-DIR: `/bible-study-tools/tbta/`
- Config auto-detects `.data/` in project root (or set `MYBIBLE_DATA_DIR`)

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

---

## Step 1: Create Dataset

### Extract Data

```bash
python src/ingest_data/tbta/extract_feature.py --field {tbta_field} --format jsonl --with-text \
  > bible-study-tools/tbta/features/{feature}/analysis/tbta-extract.jsonl
```

**Output**: One line per TBTA annotation with verse, label, constituent, part, path.

- Update `features/{feature}/README.md` with the distribution of each value found in the extraction.

---


### Create Balanced Dataset

**This is an LLM task** - requires judgment about theological/literary diversity.

**Output File** - bible-study-tools/tbta/features/{feature}/analysis/datasets.jsonl (created using the edit file, write to file or other write tools by the LLM; Do **not** write a script to do this as you need to add fields that require your custom logic to each line)

**Target sizes** (keep manageable):
- train: max 300 entries
- validate: max 100 entries
- test: max 100 entries (RESERVE - don't look at until final eval)


**Selection criteria** for each split:
- Balance across feature values
- Mix of OT/NT
- Mix of literary types (history, poetry, prophecy, epistles)
- Include easy AND adversarial cases
- Same verse = same split (don't leak)

**Required fields in output**:

The following is showing too many newlines to make this file easier for me to read, in your output it will proper jsonl

```jsonl
{
  "verse": "GEN-001-026",
  "label": "Trial",
  "constituent": "us",
  "part": "Noun",
  "reconstructed_verse": "God said, let **us** make mankind in our image",
  "strongs_number": "H430",
  "strongs_word": "אֱלֹהִים",
  "dataset": {
    "split": "train",
    "section": "OT",
    "literary_type": "history",
    "difficulty": "adversarial",
    "theological_group": "TRINITY"
  }
}\n
{ 
  "verse": "GEN-001-026",
  "label": "Trial",
  "constituent": "us",
  "part": "Noun", (TODO: fix this example, I want to show that the same verse goes into the same dataset)
  "reconstructed_verse": "God said, let us make mankind in **our** image",
  "strongs_number": "H430", (FIX this)
  "strongs_word": "אֱלֹהִים", (fix this)
  "dataset": {
    "split": "train",  // IMPORTANT: notice that this is the same dataset as above b/c it is the same verse but the next word to solve
    "section": "OT",
    "literary_type": "history",
    "difficulty": "adversarial",
    "theological_group": "TRINITY"
  }
}
```

**Key additions**:
- `strongs_number`: Infer from constituent + verse (LLM can do this from memory)
- `theological_group`: From Stage 1 THEOLOGICALLY-SIGNIFICANT-GROUPS research: You will need to read that file first and create a list of your codes for consistency

**Script**: Create `/src/tools/predict/split_datasets.py` to output entries not in any set to leftovers.jsonl

---
### Enrich with Translations

#### Step 1: Fetch sample verses to validate language selection

Use `src/tools/fetch_verse.py` to get 2 verses (1 OT, 1 NT) that clearly demonstrate this feature:

```bash
python src/tools/fetch_verse.py GEN.001.026  # Example OT verse with feature
python src/tools/fetch_verse.py MAT.004.019  # Example NT verse with feature
```

#### Step 2: Validate language choices against actual translations

Read `../research/LANGUAGES.md` to get the list of languages that encode this feature.

With the sample verses in front of you, validate each language:
1. Can you identify which word is the target constituent in that language?
2. Does the translation show the morphological marking LANGUAGES.md claims?
3. Do you know the grammatical rules for this feature in that language well enough to use it as a hint?

**Example validation** (for number systems with GEN.001.026 "let **us** make"):
- Arabic: نَحْنُ (naḥnu) - yes, I can identify "us" and know Arabic dual/plural rules ✓
- Hawaiian: If I can't identify which word is "us" or don't know Hawaiian number morphology → skip

#### Step 3: Select translations

**Selection criteria**:
- **MUST INCLUDE**: Languages from LANGUAGES.md where you validated you can identify the word and know the rules
- **LIMIT**: English/gateway languages to 2-3 max (they typically don't encode the feature)

**Anti-pattern**: Including many English translations when English doesn't mark this feature. If LANGUAGES.md says Arabic has dual morphology, include Arabic - not 10 English versions.

```bash
python src/ingest_data/tbta/enrich_extract_with_verses.py \
  --input analysis/datasets.jsonl \
  --languages {validated-codes} \  # Only languages you validated above
  --output analysis/enriched.jsonl
```

**Important notes**:
- Use `{lang}-{version}` codes (e.g., `eng-NIV`), not just language codes
- These match the keys returned by `fetch_verse.py`
- **Validate after enrichment**: Confirm the languages you selected actually appear in the output

**Known issue**: Versification mismatch can cause ~50% cache misses. The enrichment script handles this gracefully.

---

### Split the datasets up

Call `src/tools/predict/split_dataset.py --input analysis/enriched.jsonl --original analysis/tbta-extract.jsonl --output analysis/data`


## Step 2: Baseline Analysis

### LLM Baseline

**Process**: Run TWO baseline tests in parallel using subagents, then analyze the difference.

**Goal**: Understand (1) what the LLM already knows about this feature, and (2) how much guidance helps.

#### Test A: Zero-Shot Baseline (no definitions)

Start a subagent with a minimal prompt that only lists the possible values without explaining them:

```
Label each highlighted word (**word**) with one of these {FeatureName} values:
{Value1}, {Value2}, {Value3}, ...

Return format: $verse\t$label (e.g., "GEN.001.001\tValue1")
```

Give it 100 diverse verses from `features/{feature}/analysis/data/train.jsonl`.

Save predictions to `analysis/data/baseline_zero_shot.tsv`.

#### Test B: Guided Baseline (with definitions)

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

Give it the SAME 100 verses. Save predictions to `analysis/data/baseline_guided.tsv`.

#### Analysis: Compare the Two Baselines

Create `analysis/HIGH-LEVEL-REVIEW.md` with:

1. **Accuracy comparison**:
   | Test | Accuracy |
   |------|----------|
   | Zero-shot | X% |
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

---

## Step 3: Analyze Patterns (Parallel Tasks)

Run these analyses in parallel using subagents:

### 3A: Dominant Value Analysis

**Datasource** analysis/data/train.secret.jsonl and analysis/data/leftovers.secret.jsonl

**Output** analysis/EDGE-CASES.md

When one value dominates (e.g., Singular 66%):
1. Focus on: "When is it NOT the dominant value?"
2. List all conditions where the minority value applies; trying to group them into most common to least common with examples for each

### 3B: TBTA label quality

**Datasource** 
 - analysis/data/train.secret.jsonl
 - analysis/data/leftovers.secret.jsonl
 - analysis/HIGH-LEVEL-REVIEW.md
 - research/README.md (and potentially the subfiles)

**Output** analysis/TBTA-QUALITY.md

Do a critical review of the TBTA labels.  Verify your work don't just theorize they are wrong.  

Be careful of broad assumptions like in research there is no FOUR person number system but TBTA has it; consider instead why they may have done it such as for translating the remaining 4000 langauges that are not yet documented they may encounter a langauge that does require it, labelling it as four is harmless in that langauges with only 3 will just call it plural.

Be sure to include qualifying questions asked very respectfully for the TBTA team to clear up confusion; providing examples for each.

### 3C: Strong's Word Patterns

Analyze `strongs_number`

Run `python src/ingest_data/tbta/group_by_strongs.py --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl --output ${TBTA-DIR}/features/{feature}/analysis/strongs-analysis.jsonl`


1. Group entries by Strong's number
2. For each word with count ≥5:
   - Is there a consistent pattern? (e.g., "יָד (hand)" → always Dual)
   - If variable, is there a **contextual pattern**? (e.g., H376 "man" varies but is predictable from the preceding numeral: "two men" → Dual, "three men" → Trial)
   - Any exceptions? Document in `analysis/TBTA-POTENTIAL-ISSUES.md`
3. If pattern is reliable (≥95% consistent), upsert a file in {$DATA_DIR:default(.data)}/strongs/(G|H)${strongsNumber:fd4}/(G|H)${strongsNumber:fd4}.tbta-hints.yaml OTHERWISE continue to next word

Output your top findings and work to `analysis/STRONGS.md`

**Key insight**: Variable patterns often become predictable with context. Look for:
- Preceding words (numerals, quantifiers): "two **men**" → Dual
- Following modifiers: "**sons** of Zebedee" (2 sons → Dual)
- Translation morphology in other languages (see 3D)

**Warning**: Low counts are overfitting. Only trust patterns with 5+ occurrences.

### 3D: Translation Morphology Patterns

Analyze word forms across translations to find morphological hints.

Run `python src/ingest_data/tbta/group_by_strongs.py --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl --output ${TBTA-DIR}/features/{feature}/analysis/word-analysis.jsonl --no-strongs`

**CRITICAL**: Verify your data includes the languages from `research/LANGUAGES.md` that encode this feature.

If data only has English (or other languages that don't encode this feature), **STOP** and re-enrich with the languages from `research/LANGUAGES.md`.

1. Group all entries together (no Strong's grouping)
2. For languages that encode this feature, look for form-based patterns:
   - Example: Arabic dual suffix (-ān) → if present, classify as Dual
   - Example: Hebrew -ayim suffix → Dual
3. For each discriminative form with count ≥5:
   - Is there a consistent pattern?
   - Document in `analysis/WORD-ANALYSIS.md`

**Example hint format**:
```
If {language} translation uses {form}, classify as {label}
```

**Warning**: Low counts are overfitting. Only trust patterns with 5+ occurrences.

### Logical Reason Analysis

**Goal**: Identify theological/grammatical reasons why verses get specific labels, then add hints to edge cases.

**Rationale**: Writing prompts with endless edge cases is confusing. Instead, add verse-specific hints for rare patterns (<500 occurrences).

**Notes**:
- You have memorized the entire Bible and can mostly rely on your accuracy
- Limit each reason group to maximum 500 verses

**Phase 1: Group verses by reason**

```bash
python src/ingest_data/tbta/group_by_reasons.py \
  --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl \
  --output ${TBTA-DIR}/features/{feature}/analysis/reason-groupings.jsonl
```

The script outputs groups WITHOUT hints:
```json
{"reason": "TRINITY", "description": "...", "count": 45, "verses": ["GEN.001.026", "GEN.003.022", ...]}
{"reason": "UNSET", "description": "Needs manual review", "count": 120, "verses": [...]}
```

**Phase 2: Add hints (LLM task)**

- [ ] Read `features/${feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for context
- [ ] Review each group in `reason-groupings.jsonl`
- [ ] For UNSET verses: determine which reason group they belong to, or create new groups
- [ ] Add a `"hint"` field to each group (max 250 words)
- [ ] Save as `analysis/reason-groupings-with-hints.jsonl`

**Required transformation** - add `hint` field to each group:
```json
{"reason": "TRINITY", "hint": "Trinitarian context often uses plural forms...", "description": "...", "count": 45, "verses": [...]}
{"reason": "DIVINE_SPEECH", "hint": "Direct divine speech typically uses...", "description": "...", "count": 30, "verses": [...]}
```

**Hint guidelines**:
- Generic enough to apply to all verses in the group (not verse-specific)
- Explains the theological/grammatical principle (e.g., "Trinitarian verses often use plural because...")
- Avoid absolute language like "must" - these are hints, not rules
- Include edge case considerations where relevant

**Phase 3: Persist hints to verse files**

```bash
python src/tools/append_to_verses.py \
  --input ${TBTA-DIR}/features/{feature}/analysis/reason-groupings-with-hints.jsonl \
  --feature {FeatureName} \
  --tool tbta-hints
```

This creates/updates `$DATA_DIR/commentary/{BOOK}/{CCC}/{VVV}/{BOOK}-{CCC}-{VVV}-tbta-hints.yaml` files.

**Validation checklist**:
- [ ] Do you agree with TBTA's labels? Note disagreements in `analysis/TBTA-QUALITY.md`
- [ ] Are there verses missing from groups that should be included?
- [ ] Are there verses in groups where the hint doesn't apply?


## Step 7: Document Results

**Input**:
 - review all the markdown files in the analysis director
  
Create `analysis/README.md` linking to the subfiles for more details:

```markdown
# {Feature} Analysis

## Distribution
- Value A: X% (N entries)
- Value B: Y% (N entries)

## Dataset Sizes
- Train: N | Validate: N | Test: N

## Key Findings
1. [Pattern 1]: [accuracy]% confidence
2. [Pattern 2]: [accuracy]% confidence

## Suspicious Data
- [Any TBTA labeling concerns]

## Recommended Approach
- [ ] Simple rules (logical.py)
- [ ] LLM with hints
- [ ] Hybrid approach
```

Update `features/{feature}/README.md` with summary linking to analysis.

---

## Anti-Patterns to Avoid

1. **Overfitting**: Don't trust patterns with <10 occurrences
2. **Ignoring edge cases**: The 7% exceptions matter more than the 93% rule
3. **Complex scripts for simple tasks**: If LLM baseline works, use it
4. **Touching test set**: Only for FINAL evaluation
5. **Huge datasets**: Keep train ≤300, validate/test ≤100 - more is not better
6. **Semantic vs. Grammatical confusion**: Quadrial/Trial in TBTA are often semantic (groups of 3/4), not grammatical number

---

## Execution Strategy

1. **Subagents**: Each major step should use a subagent to avoid context pollution
2. **Parallelism**: Run substeps in parallel if they don't reply on each other
3. **Early exit**: If(LLM baseline) succeeds, skip to Step 7
