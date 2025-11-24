# Stage 4: Validation & Peer Review

**Role**: QA / Critic / Theologian
**Input**: `PROMPT.md` (Final Candidate), `validate_inputs.jsonl`
**Output**: `experiments/validation/` (Final Reports)

## Goal
The final exam. Blind testing on held-out data and critical peer review to ensure safety and accuracy.

## Tasks

### 1. Blind Validation (The "Exam")
*   **Input**: `experiments/data/validate_inputs.jsonl` (Never before seen by the model).
*   **Logic**:
    1.  Use the final `augment_data.py` + `PROMPT.md` pipeline.
    2.  Generate predictions for the validation set.
    3.  **LOCK**: Commit `experiments/validation/final_predictions_LOCKED.jsonl` to git.
    4.  **SCORE**: Run `score_predictions.py` against `validate_answers.secret.jsonl`.
*   **Output**: `experiments/validation/final_scorecard.md`.

### 2. Error Analysis
*   **Action**: For every error in the validation set:
    1.  Retrieve the verse and context.
    2.  Analyze *why* it failed (Ambiguity? Rule gap? TBTA error?).
    3.  Categorize errors (Theological Risk vs. Stylistic Choice).
*   **Deliverable**: `experiments/validation/error_analysis.md`.

### 3. Critical Peer Review (The "Safety Check")
*   **Persona 1: The Theologian**:
    *   Review `PROMPT.md` logic for Non-Arbitrary contexts (Trinity, Divine Speech).
    *   Check `error_analysis.md` for theological failures.
*   **Persona 2: The Linguist**:
    *   Does the logic hold up cross-linguistically?
    *   Are we overfitting to English idiosyncrasies?
*   **Persona 3: The Translator**:
    *   Is this actually useful?
    *   Are the confidence scores reliable?

### 4. Production Readiness Decision
*   **Criteria**:
    *   >90% Accuracy on Validation Set (or explained limitation).
    *   100% Accuracy on Non-Arbitrary (Theological) contexts.
    *   No "Critical" errors (heresy, confusing divine commands).
*   **Action**:
    *   If PASS: Update `features/{feature}/README.md` with "Status: Production".
    *   If FAIL: Mark "Status: Research" or "Tier 1 Only" (Partial Deployment).

## Deliverables
1.  `experiments/validation/final_scorecard.md`
2.  `experiments/validation/error_analysis.md`
3.  `experiments/validation/peer_review.md`
4.  `FINAL_REPORT.md` (Executive summary for the repo owner).

**Success Criteria**:
*   A fully validated, safe feature ready for deployment.
*   Honest reporting of limitations.

