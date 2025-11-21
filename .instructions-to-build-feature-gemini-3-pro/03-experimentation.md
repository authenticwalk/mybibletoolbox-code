# Stage 3: Experimentation & Iterative Development

**Role**: Prompt Engineer / ML Engineer
**Input**: Analysis Data (Stage 2), Split Datasets
**Output**: `experiments/training/`, `PROMPT.md`, `augment_data.py`

## Goal

Develop and refine the logic to predict the feature using parallel experimental tracks, then refine the winning approach.

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

### 2. Phase 1: Parallel Tracks (Find the Best Path)

**Track A: The "Baseline" (Zero-Shot)**

- **Prompt**: Just definitions and text. Establish the floor.

**Track B: The "Concise Logic" (Chain of Thought)**

- **Process**: Ask LLM to analyze Stage 2 patterns. Draft `PROMPT-LOGIC.md` ("If context X -> Y").
- **Constraint**: Minimalist rules.

**Track C: The "Strong's Annotation" (Data Enrichment)**

- **Goal**: Shift logic to data.
- **Action**: Create `data/strongs/{G|H}{number}-tbta.yaml` for deterministic words or words with clear rules (e.g., "us" = Trinity if Divine).
- **Integration**: Update `augment_data.py` to inject these notes.

**Track D: Decision Tree Hints (Hybrid)**

- **Action**: Inject Stage 2 ML insights as "Expert Hints" into the prompt.

**Selection**:

- Run all tracks on `test_inputs.jsonl`.
- Pick the clear winner.

### 3. Phase 2: Refinement (Optimize the Winner)

**Goal**: Take the winning track and polish it for production.
**Input**: The winning method from Phase 1.
**Tasks**:

1.  **Error Analysis (Train Set)**: Run the winner on `train.jsonl`. Identify remaining systematic errors.
2.  **Edge Case Handling**: Add specific logic for the hard cases identified in Stage 1 (Research).
3.  **Token Optimization**: Remove unnecessary context or instructions to improve speed/cost.
4.  **Prompt Polish**: Ensure clear, unambiguous language.

### 4. Phase 3: The "Pre-Flight" Check

- **Action**: Run the _refined_ winner against `test_inputs.jsonl` one last time.
- **Success Check**: Did accuracy improve over Phase 1?
- **Lock**: Commit the final `PROMPT.md` and any helper scripts.

## Deliverables

1.  `augment_data.py` (Script)
2.  `experiments/training/track_comparison.md` (Results of Phase 1)
3.  `experiments/training/refinement_log.md` (Results of Phase 2)
4.  `data/strongs/*-tbta.yaml` (The generated annotation files)
5.  `PROMPT.md` (The final best performing prompt)

**Success Criteria**:

- One method achieves >90% accuracy (or best possible given data limits).
- Logic is explainable (not a black box).
- Refinement phase demonstrates measurable improvement over the raw experimental track.
