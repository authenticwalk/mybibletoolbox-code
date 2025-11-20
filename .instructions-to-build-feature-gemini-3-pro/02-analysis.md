# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `experiments/analysis/` (Data dumps, Scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. We shift from "looking for patterns" to "testing hypotheses".

## Tasks

### 1. Data Extraction

- **Script**: Write a python script to extract the feature from the TBTA corpus.
- **Filter**: Get ~2000 verses max, distributed across values.
- **Constraint**: Must include all **Non-Arbitrary** cases identified in Stage 1.

### 2. Strong's Alignment (The "Smart" Step)

- **Challenge**: TBTA data has semantic labels but lacks the specific source word (Strong's number).
- **Action**: Update the extraction script to align TBTA verses with Macula/Strong's data (available in `.data/` or via `fetch_verse` skill).
- **Output**: A dataset linking: `Verse Ref` + `TBTA Value` + `Strong's #` + `Source Word`.

### 3. Capabilities Audit (The "ClaudeFlow" Fix)

- **Action**: Before assuming we have "Fijian", **CHECK**.
- **Script**: Write a tiny script using `fetch_verse` to query 1 OT verse (Gen 1:1) and 1 NT verse (John 1:1).
- **Output**: A list of _actually available_ language codes. Filter your target list to only these.

### 4. Hypothesis Generation

- **Concept**: Instead of asking "What did they translate?", ask "If TBTA is right, what _must_ they have translated?"
- **Action**: For each target language (e.g., Fijian), hypothesize the target word.
  - _Example_: "If TBTA says Trial for Gen 1:26, and Fijian has Trial pronouns, Fijian _should_ use 'kedatou' (inclusive trial)."
- **Method**: Use an LLM to generate these hypotheses in a `hypotheses.json` file.
  - Format: `{ "lang": "fij", "tbta_value": "Trial", "expected_words": ["kedatou", "tou"] }`

### 5. Validation Script

- **Script**: Write `validate_hypotheses.py`.
- **Logic**:
  1.  Load extracted verses (with TBTA values).
  2.  Load `hypotheses.json`.
  3.  Fetch actual translation text for the verse (using `fetch_verse`).
  4.  Check: Does the translation contain any of the `expected_words`?
  5.  Score: Hit/Miss.
- **Output**:
  - `experiments/analysis/validation_raw.jsonl`: Detailed logs.
  - `experiments/analysis/scorecard.md`: Summary by language and value.

## Advanced Quantitative Analysis (Recommended)

### 6. Strong's Frequency Analysis

- **Goal**: Identify "Magic Words" that are deterministic.
- **Script**: Analyze the dataset from Step 2.
- **Logic**:
  - Count frequency of each Strong's Number.
  - specific Strong's # -> TBTA Label mapping.
  - **Highlight**: Any Strong's word that maps to a single TBTA label 100% of the time.
- **Output**: `experiments/analysis/strongs_correlation.csv`

### 7. Decision Tree Feature Importance

- **Goal**: Use "Explainable AI" to find the strongest indicators.
- **Script**: Build a Python-based Decision Tree (using `sklearn`).
- **Features**:
  - Source: Strong's Number (One-Hot encoded).
  - Target: Presence of hypothesized words (from Step 4) in available languages.
  - Morphology: Macula part-of-speech tags (if available).
- **Action**: Train tree to predict TBTA Value. Use `tree.export_text` or feature importance charts to see which words drive the decision.

### 8. Semantic Space (Embeddings)

- **Goal**: Capture context that keyword matching misses.
- **Script**: Train a lightweight classifier on text embeddings.
- **Logic**:
  - Generate embeddings for the full verse text (Source + English + Target Langs) using a multilingual model (e.g., `sentence-transformers`).
  - Concatenate with explicit features (Decision Tree output).
  - Train a classifier (e.g., Logistic Regression or XGBoost).
- **Output**: `experiments/analysis/embedding_report.md` (Does semantic context improve accuracy over keyword matching?)

## Data Splitting & Secure Storage (Required for Stage 3)

### 9. Generate Training Splits

- **Script**: `split_data.py`
- **Inputs**: The clean dataset from Step 2/5.
- **Ratios**: Train (60%), Test (20%), Validate (20%).
- **Stratification**: Ensure all TBTA values and Non-Arbitrary contexts are represented in all splits.
- **Output Security**:
  - `experiments/data/train.jsonl` (Full data)
  - `experiments/data/test_inputs.jsonl` (Inputs Only)
  - `experiments/data/test_answers.secret.jsonl` (Answers Only - **FORBIDDEN**)
  - `experiments/data/validate_inputs.jsonl` (Inputs Only)
  - `experiments/data/validate_answers.secret.jsonl` (Answers Only - **FORBIDDEN**)

## Deliverables

1.  `experiments/analysis/raw_data.jsonl` (The dataset)
2.  `experiments/analysis/scorecard.md` (The proof of concept)
3.  `experiments/analysis/strongs_correlation.csv` (Deterministic words)
4.  `experiments/data/` (The securely split datasets)

**Success Criteria**:

- High agreement (>80%) in Non-Arbitrary contexts confirms the feature is predictable.
- Datasets are split and secret files are generated.
