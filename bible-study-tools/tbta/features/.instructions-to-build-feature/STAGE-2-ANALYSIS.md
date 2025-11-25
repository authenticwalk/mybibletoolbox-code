# Stage 2: Analysis & Hypothesis Validation

**Role**: Data Scientist / Polyglot / QA
**Input**: Feature Definition (Stage 1)
**Output**: `analysis/` (Data dumps, scripts, Scorecards)

## Goal

Quantitatively validate the feature against real-world translations _before_ writing prompts. We shift from "looking for patterns" to "testing hypotheses".

## Context

NOTE: the relative directory is /bible-study-tools/tbta/features/{feature}/
NOTE: the TBTA-DIR is /bible-study-tools/tbta/

## Execution Strategy

**Use Subagents Proactively**:

- Assign subagents to run in parallel for each section: ex (TBTA Review, Language Analysis, Theological Research, etc)
- Then Synthesize findings into the final deliverables.
- 
## Tasks

### 1. Extract TBTA Data (Output as JSONL)

**This step is done using code only.**

- **Script**: Run the canonical extractor (`python src/ingest-data/tbta/extract_feature.py --field {tbta_field} --format jsonl > ${TBTA-DIR}/features/{feature}/analysis/tbta-extract.jsonl`) 
- **Output Format** (`./analysis/tbta-extract.jsonl`): For each TBTA entry, output in JSONL format:
  ```jsonl
  {"verse": "REV.001.010", "label": "Singular", "constituent": "sound", "part": "Noun", "path": "Clause[4]/Clause[0]/NP[0]"}
  ```
  

### 2. Select Reference Dataset (100+ Verses Per Value)

** You need to do this as the LLM as this is an unstructured task**

Sources:
- ${TBTA-DIR}/features/{feature}/analysis/tbta-extract.jsonl
- context: ${TBTA-DIR}/features/{feature}/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.md
- context: ${TBTA-DIR}/features/{feature}/research/README.md


- **Goal**: Select 100+ values for each value ensuring a good balance of easy and adversarial; non-arbitrary and arbitrary (and balanced between the groupings within that); OT and NT; various literary types (history, poetry, prophecy, epistle, law, etc)

- **Output Format** (`${TBTA-DIR}/features/{feature}/analysis/reference-dataset.jsonl`): Output as JSONL with fields:
  ```jsonl
  {"verse": "GEN-001-026", "tbta_value": "Trial", "tbta_word": "us", "strongs_number": "H430", "strongs_word": "אֱלֹהִים"}
  ```
  Fields: `verse`, `tbta_value`, `tbta_word` (TBTA word used), `strongs_number`, `strongs_word`
- **Challenge**: Strong's number is not in the TBTA source but you can determine if from the Macula dataset in $DATA-DIR(default:./data)/commentary/{BOOK}/{chapter:03d}/{BOOK}.{chapter:03d}.{verse:03d}-{macula}.yaml 


### 4. Generate Translation Hypotheses

Created with LLM

Sources: 
 - `${TBTA-DIR}/features/{feature}/analysis/reference-dataset.jsonl`
 - context: ${TBTA-DIR}/features/{feature}/research/LANGUAGES.md (languages that use this feature)

- **Concept**: For each record in the reference dataset, consider which languages from Step 3 use or require this feature
- **Action**: 
  - Guess which words they would use that would translate this Strong's word to their language using the TBTA feature
  - Also guess which words they would use if TBTA was wrong and they chose another value
- **Method**: Use an LLM to generate these hypotheses
- **Output Format** (`analysis/translation-hypotheses.jsonl`):
  ```jsonl
  {"verse": "GEN-001-026", "tbta_value": "Trial", "strongs_number": "H430", "languages": ["fij", "expected_words": ["kedatou", "tou"], "alternative_words": {"Plural": ["keda",...], "Dual": ["kedaru"]},...]}
  ```

### 5. Validate Hypotheses Against Real Translations

- **Script**: Write `validate_hypotheses.py` (create if this is your first feature but make it reusable for all features - place in `src/tools/predict/` if reusable)
- **Logic**:
  1. Use the bible lookup function (`fetch_verse` or `quote-bible` skill) to get all the verses that have a TBTA value for this feature
  2. For each verse + language combination, check if any of the guessed words (from Step 4) are present in each verse
  3. Score: Hit/Miss per language and overall
- **Output**:
  - `analysis/validation-raw.jsonl`: Store the raw results as a JSONL file (detailed logs for each verse+language)
  - `analysis/scorecard.md`: Create a score card for each language and overall for how often they agree with TBTA
- **Theological Edge Cases**: Ensure adversarial test set includes:
  - Trinity contexts (Gen 1:26, Matt 28:19)
  - Incarnation contexts (John 1:14)
  - Messianic prophecies
  - Corporate solidarity (Israel as one/many)
  - These are highest-stakes errors and common failure points.

### 6. Data Coverage Verification (Critical)

- **Goal**: Verify all documented feature values actually exist in TBTA data before building algorithms.
- **Script**: `verify_coverage.py`
- **Logic**:
  1.  Extract all unique feature values from TBTA dataset.
  2.  Compare against documented values from Stage 1.
  3.  Calculate coverage: `(values_found / values_documented) * 100`.
  4.  Identify missing values and their expected frequency.
- **Decision Rule**:
  - If coverage ≥ 80%: Proceed to Stage 3
  - If coverage < 80%: Document limitation, pivot to linguistic-theory approach
  - If only 1-2 values found: STOP - data likely incomplete (see `discourse-genre` lesson)
- **Output**: `experiments/analysis/coverage_report.md`

## Advanced Quantitative Analysis (Recommended)

### 7. Strong's Frequency Analysis

- **Goal**: Identify "Magic Words" that are deterministic.
- **Script**: Analyze the dataset from Step 2.
- **Logic**:
  - Count frequency of each Strong's Number.
  - specific Strong's # -> TBTA Label mapping.
  - **Highlight**: Any Strong's word that maps to a single TBTA label 100% of the time.
- **Output**: `experiments/analysis/strongs_correlation.csv`

### 8. Decision Tree Feature Importance

- **Goal**: Use "Explainable AI" to find the strongest indicators.
- **Script**: Build a Python-based Decision Tree (using `sklearn`).
- **Features**:
  - Source: Strong's Number (One-Hot encoded).
  - Target: Presence of hypothesized words (from Step 4) in available languages.
  - Morphology: Macula part-of-speech tags (if available).
- **Action**: Train tree to predict TBTA Value. Use `tree.export_text` or feature importance charts to see which words drive the decision.

### 9. Semantic Space (Embeddings)

- **Goal**: Capture context that keyword matching misses.
- **Script**: Train a lightweight classifier on text embeddings.
- **Logic**:
  - Generate embeddings for the full verse text (Source + English + Target Langs) using a multilingual model (e.g., `sentence-transformers`).
  - Concatenate with explicit features (Decision Tree output).
  - Train a classifier (e.g., Logistic Regression or XGBoost).
- **Output**: `experiments/analysis/embedding_report.md` (Does semantic context improve accuracy over keyword matching?)

### 10. Multi-Factor Convergence Analysis

- **Goal**: Identify when multiple independent factors agree, increasing prediction confidence.
- **Script**: Analyze dataset for factor convergence patterns.
- **Logic**:
  - Identify 3-5 independent factors (e.g., morphological, lexical, temporal, discourse, clause-level).
  - For each verse, count how many factors agree on the same value.
  - **Scoring**: 4-5 factors align → 95%+ confidence; 3 factors → 80-90%; 2 factors → 65-75%; 1 factor → use baseline.
- **Output**: `experiments/analysis/convergence_report.md` (Which factor combinations yield highest confidence?)

## Data Splitting & Secure Storage (Required for Stage 3)

### 11. Adversarial Test Set Curation

- **Goal**: Don't just split randomly. Ensure the test set breaks the model.
- **Action**: Manually curate 15-20 "Edge Case" verses.
- **Criteria**:
  - **Theological Criticality**: Trinity, Incarnation, Prophecy (where rules often break).
  - **Rare Values**: Values that appear <1% of the time.
  - **Morphological Mismatches**: Where form ≠ meaning (e.g., Grammatical Plural but Semantic Singular).
- **Output**: `experiments/data/adversarial_candidates.jsonl` (Force these into the Test/Validate splits).

### 12. Generate Training Splits

- **Script**: `split_data.py`
- **Inputs**: The clean dataset from Step 2/5 + Adversarial Candidates.
- **Ratios**: Train (60%), Test (20%), Validate (20%).
- **Stratification**: Ensure all TBTA values and **Adversarial/Non-Arbitrary** cases are represented in all splits.
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
4.  `experiments/analysis/convergence_report.md` (Multi-factor convergence patterns)
5.  `experiments/analysis/coverage_report.md` (Value coverage verification)
6.  `experiments/data/` (The securely split datasets)

**Success Criteria**:

- High agreement (>80%) in Non-Arbitrary contexts confirms the feature is predictable.
- Data coverage ≥80% of documented values (or documented limitation if <80%).
- Datasets are split and secret files are generated.

## Analysis Best Practices

- **Version control**: Commit analysis scripts and outputs.
- **Document assumptions**: Note what you're looking for and why.
- **Iterate quickly**: Start simple, refine as needed.
- **Share findings**: Document insights for other developers.
- **Stay focused**: Analyze what's needed, not everything possible.

### Common Analysis Tasks

- "What structure do idiom features use?"
- "How do features cite theological sources?"
- "What patterns appear in cultural context features?"
- "How do features handle missing data?"
- "What validation checks are most common?"

Place analysis results in `/plan/tbta/features/{feature-name}/analysis/` for feature-specific work.
