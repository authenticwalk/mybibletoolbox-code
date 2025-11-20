# Stage 3: Experimentation & Iterative Development

**Role**: Prompt Engineer / ML Engineer
**Input**: Analysis Data (Stage 2), Split Datasets
**Output**: `experiments/training/`, `PROMPT.md`, `augment_data.py`

## Goal

Develop and refine the logic to predict the feature using parallel experimental tracks. We move from "Analysis" (understanding data) to "Engineering" (building the predictor).

## Core Requirement: The "One-Pass" Evaluator

All experiments must use a standardized evaluation loop:

1.  Input: `train_questions.jsonl` (or `test_inputs.jsonl`)
2.  Process: LLM/Script generates predictions.
3.  Output: `predictions.jsonl`
4.  Score: `score_predictions.py` (compares against secret answers)
5.  **Constraint**: The agent must be able to run this loop autonomously.

## Tasks

### 1. Data Supplementation (The "Context" Builder)

**Script**: `augment_data.py`
**Goal**: Enrich the raw question data with deep context so the LLM has a fighting chance.
**Logic**:

1.  Load `train_questions.jsonl`.
2.  For each verse:
    - Load Macula/Strong's data (Source word, morphology).
    - Fetch Strong's definitions (from `strongs/` directory).
    - (Optional) Fetch Target Language translations (if available/useful).
3.  **Output**: `experiments/data/train_enhanced.jsonl` (This is the new input for experiments).

### 2. Track A: The "Baseline" (Zero-Shot)

**Goal**: Establish the floor. How well does a smart LLM do with just the definition?
**Prompt**:

- "You are a Bible translation assistant."
- "Feature Definition: {Definition from Stage 1}"
- "Verse: {Text}"
- "Task: Predict the value for this feature."
  **Action**: Run against `train_enhanced.jsonl`. Record accuracy.

### 3. Track B: The "Concise Logic" (Chain of Thought)

**Goal**: Distill the feature into a minimal set of human-readable rules.
**Process**:

- Ask LLM to analyze the high-confidence patterns from Stage 2 (Analysis).
- Draft a `PROMPT-LOGIC.md`: "If context has X and word is Y -> Z".
- **Constraint**: Keep it simple. No 100-page rulebooks.
- **Test**: Use this logic in a prompt. Measure accuracy vs Baseline.

### 4. Track C: The "Strong's Annotation" (Data Enrichment)

**Goal**: Shift logic from the _Prompt_ to the _Data_.
**Concept**: Instead of "If word is 'us'...", we annotate the Strong's definition itself.
**Action**:

1.  Identify Strong's words that are **deterministic** (100% correlation in Stage 2).
2.  Identify Strong's words that have **clear conditional rules** (e.g., "us" = Trinity if Divine).
3.  **Create Note Files**: `data/strongs/{G|H}{number}-tbta.yaml`
    ```yaml
    strongs: G1234
    tbta_feature: { feature_name }
    default_value: { most_common_value }
    rules:
      - condition: 'Speaker is God'
        value: 'Trial'
    ```
4.  **Integration**: Update `augment_data.py` to inject these notes into the prompt context.
5.  **Test**: Run prediction with these "Hinted" prompts.

### 5. Track D: Decision Tree Hints (Hybrid)

**Goal**: Use the ML insights from Stage 2.
**Action**:

1.  Take the Decision Tree rules from Stage 2 (Analysis).
2.  Inject them as "Expert Hints" into the prompt.
    - _Example_: "Hint: Historical analysis suggests that when 'language X' uses 'word Y', the value is likely 'Z'."
3.  **Test**: Measure if these hints help or confuse the LLM.

## Execution Strategy

- Run Tracks A, B, C, D in parallel (or sequential rapid iterations).
- **Compare**: Which method yields the highest accuracy on `test_inputs.jsonl`?
- **Select**: Pick the winner (or combine B+C).
- **Finalize**: Write the winning logic into `PROMPT.md`.

## Deliverables

1.  `augment_data.py` (Script)
2.  `experiments/training/baseline_results.md`
3.  `experiments/training/logic_results.md`
4.  `data/strongs/*-tbta.yaml` (The generated annotation files)
5.  `PROMPT.md` (The final best performing prompt)

**Success Criteria**:

- One method achieves >90% accuracy (or best possible given data limits).
- Logic is explainable (not a black box).
- No "Hardcoded Exceptions" in code; rules live in data or concise logic.
