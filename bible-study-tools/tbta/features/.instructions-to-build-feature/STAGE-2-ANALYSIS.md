# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. We shift from "looking for patterns" to "testing hypotheses".

## Context

NOTE: the relative directory is `/bible-study-tools/tbta/features/{feature}/`
NOTE: the TBTA-DIR is `/bible-study-tools/tbta/`

## Execution Strategy

**Use Subagents Proactively**:

- Each of these tasks should be assigned to a subagent so you don't pollute your context
- Determine which can be run in parallel as you are not blocked (ex. strongs and reason groupings are independent so can be run at the same time)

## Tasks

### 1. Extract TBTA Data (Output as JSONL)

**This step is done using code only.**

- **Script**: Run the canonical extractor:
  `python src/ingest_data/tbta/extract_feature.py --field {tbta_field} --format jsonl > ${TBTA-DIR}/features/{feature}/analysis/tbta-extract.jsonl`
- **Output Format** (`./analysis/tbta-extract.jsonl`): For each TBTA entry, output in JSONL format:
  ```jsonl
  {"verse": "REV.001.010", "label": "Singular", "constituent": "sound", "part": "Noun", "path": "Clause[4]/Clause[0]/NP[0]"}
  ```

> **TODO**: We need a solution for when the label appears more than once in a verse; we will be working towards aligning the text with the source language (Greek/Hebrew) and the representative languages (the ones who use this feature).

**TODOs for Analyst**:
- Update `features/{feature}/README.md` with the distribution of each value found in the extraction.

### 1b. Enrich with Multi-Language Verses

**Script**: `src/ingest_data/tbta/enrich_extract_with_verses.py`

- **Language Selection**:
  - Use `src/tools/fetch_verse.py` to get 2 verses (OT and NT).
  - Analyze which languages distinguish this feature well (based on `research/LANGUAGES.md`).
  - Select up to 21 languages that have diversity.
- **Execution**:
  ```bash
  python src/ingest_data/tbta/enrich_extract_with_verses.py \
    --input analysis/tbta-extract.jsonl \
    --languages eng,spa,fra,deu,por,rus,ara,zho,hin,jpn,kor,ind,tgl,vie,tha,swa,hau,yor,amh,heb,grc \
    --output analysis/tbta-extract-with-verses.jsonl
  ```
- **Output Format**: Each entry gains language keys:
  ```jsonl
  {"verse": "...", "label": "...", "eng": {"NIV": "...", "ESV": "..."}, "spa": {"RV1960": "..."}, ...}
  ```

**Quick Solution Check**:
- Is there an obvious logical solution? (e.g., "If language X uses word Y, then value is Z").
- Write a simple Python script (`analysis/logical.py`) to test this. If it yields 100% accuracy, you are done.

> **TODO**: QUICK SOLUTION CHECK - This must be really simple and written in under 100 lines of code. It must have at least 10 values that match for each IF condition so it is not overfitted. THIS is the only case where you can look at the whole data and create a plan.
>
> Example:
> ```python
> if verses[KEY_LANGUAGE].contains('word1', 'word2', 'word3', ...) then return 'value1'
> else if verses[KEY_LANGUAGE].contains...
> ```
> If so then we are done and simply write the prompt as "Call the script features/{feature}/analysis/logical.py"

### 2. Select Reference Dataset

**Role**: LLM Analyst

**Sources**:
- `${TBTA-DIR}/features/{feature}/analysis/tbta-extract.jsonl`
- `${TBTA-DIR}/features/{feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.md`
- `${TBTA-DIR}/features/{feature}/research/README.md`

**Goal**: Select 100+ values for each feature value ensuring balance:
- Easy vs. Adversarial
- Arbitrary vs. Meaningful
- OT vs. NT
- Literary types (history, poetry, prophecy, etc.)

**Data Storage**:
- Store the dataset in a structured format. You may use SQLite or AgentDB (via `npx agentdb` commands or subprocess).
- If using AgentDB, create a "lite sql db" pattern to store these entries for retrieval.

> **TODO**: Instead of creating files let's create a lite sql db using agentdb (go through the `.claude/skills/agentdb*` skills to see how to use it). Store in `features/{feature}/analysis.db`. Should be bulk inserts so we are not filling agents with 1000s of method calls.

> **TODO**: We should vectorize all the rows including all the languages with their verses; but *not* the answer we are trying to predict which is the feature's value.

> **TODO**: This is missing the new fields we added like verses. Also want to add to each translation which is the word(s) that are very likely the translation of the word(s) this feature refers to as field `word`. However only do this if confident otherwise leave that field null/unset.

### 3. Strong's Number Analysis

**Script**: `src/ingest_data/tbta/group_by_strongs.py`

- **Goal**: Correlate TBTA values with underlying Greek/Hebrew words and find "magic words" that predict labels.
- **Execution**:
  ```bash
  # Full analysis with Strong's grouping
  python src/ingest_data/tbta/group_by_strongs.py \
    --input analysis/tbta-extract-with-verses.jsonl \
    --output analysis/strongs-analysis.jsonl

  # Word-only analysis (no Strong's grouping)
  python src/ingest_data/tbta/group_by_strongs.py \
    --input analysis/tbta-extract-with-verses.jsonl \
    --output analysis/word-analysis.jsonl \
    --no-strongs
  ```
- **Analyst Task**:
  - Analyze `analysis/strongs-analysis.jsonl`.
  - Look for patterns: "When Strong's H1234 is present, value is usually X."
  - Note exceptions and edge cases.
  - Review the `top_patterns` field for discriminative words (>90% confidence).
  - If a strong hint exists, write to `$DATA_DIR/strongs/{strongs_number}/{strongs_number}.tbta-hints.yaml`

### 4. Logical Reason & Grouping Analysis

**Script**: `src/ingest_data/tbta/group_by_reasons.py`

- **Goal**: Group verses by theological or logical reason (e.g., "Trinity", "Generic Plural").
- **Execution**:
  ```bash
  python src/ingest_data/tbta/group_by_reasons.py \
    --input analysis/tbta-extract.jsonl \
    --output analysis/grouped-by-reason.jsonl
  ```
  Or with custom groupings:
  ```bash
  python src/ingest_data/tbta/group_by_reasons.py \
    --input analysis/tbta-extract.jsonl \
    --groups research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml \
    --output analysis/grouped-by-reason.jsonl
  ```
- **Analyst Task**:
  - Review `features/{feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`.
  - Analyze the grouped output.
  - Identify missing groups (check UNSET verses).
  - Update the JSONL with a `hint` field for each group (generic principle, not verse-specific).
  - Run `src/tools/append_to_verses.py --input analysis/grouped-with-hints.jsonl --feature {feature}` to apply these hints.
  - Use `--dry-run` first to preview changes.

> **TODO**: Update the instructions that when we labelled the data with the reason code of why it is in a dataset we use a code ex. TRINITY. Each reason should be max 500 verses.

### 5. Language Family Analysis

- **Goal**: Determine if the feature correlates with linguistic families rather than theological meaning.
- **Analysis**:
  - Group results by language family (Romance, Germanic, Semitic, etc.).
  - Does the feature behave consistently within families?
  - Differentiate "theological necessity" from "linguistic convention."

### 6. Co-occurrence Analysis

- **Goal**: Identify if this feature triggers only when other features are present.
- **Analysis**:
  - Check for correlation with other TBTA fields in the same verse (e.g., "Passive Voice", "Plural").
  - Use statistical counts to find high-probability co-occurrences.

### 7. AgentDB Learning (Optional)

- Explore `npx agentdb` capabilities to train a model on the dataset if logical rules are insufficient.
- See `.claude/skills/agentdb-learning/SKILL.md` for decision transformer or Q-learning approaches.

### 8. Semantic Space (Embeddings)

- **Goal**: Capture context that keyword matching misses.
- **Script**: Train a lightweight classifier on text embeddings (using `agentdb` or standard ML libs).
- **Output**: `analysis/embedding_report.md`

### 9. Multi-Factor Convergence Analysis

- **Goal**: Identify when multiple independent factors agree.
- **Logic**:
  - Identify 3-5 independent factors (morphological, lexical, temporal, etc.).
  - Count agreement.
  - **Scoring**: 4-5 factors = 95% confidence.
- **Output**: `analysis/convergence_report.md`
