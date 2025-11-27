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

  - Use `src/tools/fetch_verse.py` to get 2 verses (OT and NT).
  - Analyze which languages distinguish this feature well (based on ../research/LANGUAGES.md).
  - Select up to 21 translations that have diversity storing their codes in the same format as came back from fetch_verse
    - By diversity we mean accounting for the various language families and distinct language rules
      - ex. for the feature number systems some langauges have singular/plural only while some have singular/dual/plural and others more, we want those variations
      - ex. some languages require the feature and others are more loose about it; we would want that representation as well
    - You should pick langauges your internal memory is pretty confident in translating so if we say what number system is the word "us" in God said let us make you know which word is the translation of "us" in that language and you know the linguistical rules about this feature for that word for that language.
      - 
```bash
python src/ingest_data/tbta/enrich_extract_with_verses.py \
  --input analysis/datasets.jsonl \
  --languages eng-NIV,eng-ESV,spa-RV1960,fra-LSG} \  // NOTE: use the translation version codes you made above here
  --output analysis/enriched.jsonl
```

**Important notes**:
- Use `{lang}-{version}` codes (e.g., `eng-NIV`), not just language codes
- These match the keys returned by `fetch_verse.py`
- Select 5-10 versions that distinguish this feature well (from Stage 1 features/{feature}/research/LANGUAGES.md)

**Known issue**: Versification mismatch can cause ~50% cache misses. The enrichment script handles this gracefully.

---

### Split the datasets up

Call `src/tools/predict/split_dataset.py --input analysis/enriched.jsonl --original analysis/tbta-extract.jsonl --output analysis/data`


## Step 2: Baseline Analysis

### LLM Baseline

**process**
In your main agent call a subagent to do the labelling then back in the main agent do the analysis

**Before complex analysis**, test if the LLM can already solve this with a simple prompt.

1. **Create the baseline prompt** (this is ONE prompt with two parts):

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

2. Start a subagent (so it has no memory of the answers) giving it your prompt and 100 diverse verses from `features/{feature}/analysis/data/train.jsonl`. Have it return in the format `$verse\t$label` (e.g., "GEN.001.001\tTrial").

3. Review the answers critically creating the file `analysis/HIGH-LEVEL-REVIEW.md` including your prompt
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
2. For each word with count ≥10:
   - Is there a consistent pattern? (e.g., "יָד (hand)" → always Dual)
   - Any exceptions? Document in `analysis/TBTA-POTENTIAL-ISSUES.md`
3. If pattern is reliable (≥95% consistent), upsert a file in {$DATA_DIR:default(.data)}/strongs/(G|H)${strongsNumber:fd4}/(G|H)${strongsNumber:fd4}.tbta-hints.yaml OTHERWISE continue to next word

Output your top findings and work to `analysis/STRONGS.md`

**Warning**: Low counts are overfitting. Only trust patterns with 10+ occurrences.

### 3D: Word Patterns

Analyze `word usage` to find common words across translations.  

Run `python src/ingest_data/tbta/group_by_strongs.py --input ${TBTA-DIR}/features/{feature}/analysis/data/train.jsonl --output ${TBTA-DIR}/features/{feature}/analysis/word-analysis.jsonl --no-strongs`

1. Group all entries together (no Strong's grouping)
2. Analyze word frequencies per translation code per label
3. For each word with count ≥10:
   - Is there a consistent pattern? (e.g., English "hands" → always Dual)
   - Any exceptions? Document in `analysis/TBTA-POTENTIAL-ISSUES.md`
4. Document discriminative words that reliably predict specific labels

Output your top findings and work to `analysis/WORD-ANALYSIS.md`

**Warning**: Low counts are overfitting. Only trust patterns with 10+ occurrences.

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
