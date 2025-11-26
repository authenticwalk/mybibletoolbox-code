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

## Step 1: Extract TBTA Data

```bash
python src/ingest_data/tbta/extract_feature.py --field {tbta_field} --format jsonl \
  > bible-study-tools/tbta/features/{feature}/analysis/tbta-extract.jsonl
```

**Output**: One line per TBTA annotation with verse, label, constituent, part, path.

**Immediately**: Check distribution in `features/{feature}/README.md`. Note:
- Is one value dominant (>80%)? Focus on edge cases when it's NOT that value
- Any suspicious values? (e.g., Quadrial has no linguistic basis - it's semantic, not grammatical)

---

## Step 2: LLM Baseline (CRITICAL - Do This First!)

**Before complex analysis**, test if the LLM can already solve this with a simple prompt.

1. Write a 1-3 sentence prompt describing the feature (from Stage 1 research)
2. Include max 5 key considerations as sub-bullets
3. Test on 20 samples from the extraction (diverse labels)
4. If accuracy ≥90%, you may be done - skip to Step 7

**Why**: Avoid overbuilding. The LLM may already have sufficient knowledge for common features.

---

## Step 3: Create Balanced Dataset

**This is an LLM task** - requires judgment about theological/literary diversity.

**Target sizes** (keep manageable):
- train: max 300 entries
- validate: max 100 entries
- test: max 100 entries (RESERVE - don't look at until final eval)
- leftovers: everything else

**Selection criteria** for each split:
- Balance across feature values
- Mix of OT/NT
- Mix of literary types (history, poetry, prophecy, epistles)
- Include easy AND adversarial cases
- Same verse = same split (don't leak)

**Required fields in output**:
```jsonl
{
  "verse": "GEN-001-026",
  "label": "Trial",
  "constituent": "us",
  "part": "Noun",
  "path": "...",
  "reconstructed_verse": "God said, let **us** make mankind in **our** image",
  "strongs_number": "H430",
  "strongs_word": "אֱלֹהִים",
  "dataset": {
    "split": "train",
    "section": "OT",
    "literary_type": "history",
    "difficulty": "adversarial",
    "theological_group": "TRINITY"
  }
}
```

**Key additions**:
- `reconstructed_verse`: Rebuild verse with **bolded target word(s)** - the word this annotation applies to
- `strongs_number`: Infer from constituent + verse (LLM can do this from memory)
- `theological_group`: From Stage 1 THEOLOGICALLY-SIGNIFICANT-GROUPS research

**Script**: Create `/src/tools/predict/split_datasets.py` to output entries not in any set to leftovers.jsonl

---

## Step 4: Enrich with Translations

```bash
python src/ingest_data/tbta/enrich_extract_with_verses.py \
  --input analysis/data/train.jsonl \
  --languages eng-NIV,eng-ESV,spa-RV1960,fra-LSG \
  --output analysis/data/train-enriched.jsonl
```

**Important notes**:
- Use `{lang}-{version}` codes (e.g., `eng-NIV`), not just language codes
- These match the keys returned by `fetch_verse.py`
- Select 5-10 versions that distinguish this feature well (from Stage 1 LANGUAGES.md)

**Known issue**: Versification mismatch can cause ~50% cache misses. The enrichment script handles this gracefully.

---

## Step 5: Analyze Patterns (Parallel Tasks)

Run these analyses in parallel using subagents:

### 5A: Dominant Value Analysis

When one value dominates (e.g., Singular 66%):
1. Focus on: "When is it NOT the dominant value?"
2. List all conditions where the minority value applies
3. Goal: Perfect prediction of minority cases

### 5B: Strong's Word Patterns

Analyze `strongs_number` field from train.jsonl:

1. Group entries by Strong's number
2. For each word with count ≥10:
   - Is there a consistent pattern? (e.g., "יָד (hand)" → always Dual)
   - Any exceptions? Document in `analysis/TBTA-POTENTIAL-ISSUES.md`
3. If pattern is reliable (≥95% consistent), add hint to `.data/strongs/{strongs}/...tbta-hints.yaml`

**Warning**: Low counts are overfitting. Only trust patterns with 10+ occurrences.

### 5C: Theological Grouping

Using THEOLOGICALLY-SIGNIFICANT-GROUPS.md from Stage 1:
1. Verify groupings match actual data
2. Write a brief hint (max 50 words) for each group
3. Flag any entries that don't fit their group

### 5D: Edge Case Investigation

When any pattern is <100% predictive:
- Investigate the exceptions
- Document WHY they differ
- These are valuable hints for the prompt

Example: "Singular proper names are 93% predictive" → What's the 7%? Pluralized divine names? Titles?

---

## Step 6: Quick Solution Check

Can simple rules achieve high accuracy?

```python
# analysis/logical.py
def predict(entry):
    if entry['constituent'] in BODY_PARTS:
        return 'Dual'
    if entry['constituent'] in PROPER_NAMES:
        return 'Singular'
    # ...
    return None  # Unknown - leave for LLM
```

**Three-tier approach**:
1. **Prompt rules**: General patterns (e.g., "body parts in Hebrew are typically dual")
2. **Code lists**: Exhaustive word lists when always true (e.g., 50 words that are ALWAYS dual)
3. **Strongs hints**: Per-word notes for edge cases (stored in data files)

**Key insight**: Return "Unknown" when confidence is low - let LLM handle ambiguity.

Test on validate set:
- If rules cover 100% with 100% accuracy → done, use rules
- If rules cover 80% with 100% accuracy → use rules + LLM fallback
- If rules cover <50% or accuracy <90% → skip rules, use LLM with hints

---

## Step 7: Document Results

Create `analysis/README.md`:

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
2. **Parallelism**: Steps 5A-5D can run in parallel
3. **Early exit**: If Step 2 (LLM baseline) succeeds, skip to Step 7
