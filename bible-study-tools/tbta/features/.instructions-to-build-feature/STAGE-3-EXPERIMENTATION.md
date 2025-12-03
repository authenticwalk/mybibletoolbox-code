# Stage 3: Experimentation & Iterative Development

**Role**: Prompt Engineer / ML Engineer
**Input**: Analysis Data (Stage 2), Split Datasets
**Output**: `experiments/training/`, `PROMPT.md`, `augment_data.py`

## Goal

Develop and refine the logic to predict the feature using parallel experimental tracks. We move from "Analysis" (understanding data) to "Engineering" (building the predictor).

<<<<<<< HEAD
=======
Your output will be a prompt that an LLM can use to accurately predict this feature.  
 - The shorter the better

This prompt will eventually (not now) be merged with other features prompts and we will give it
one verse at a time in the Greek/Hebrew and it needs to for each word add the value for each feature.


## Background

 - `{feature}/research/README.md` - In the first stage we did extensive research
 - `{feature}/analysis/README.md` - then we did lots of analysis
 - `{feature}/analysis/data/` - We created a dataset, you are not allowed to look at any file named *.secret.jsonl when predicting, only when testing.

There are a few ways we are solving this problem

 1. If there are 1 or 2 dominant and obvious values (>90% together) then we are looking for all the reasons (the edge cases) why something is not labelled that
 2. Typically there are "magic keys" in the translations.  For instance in number systems the dominant values are singular and plural.  Hebrew, Greek already have that so that gets us most of the way.  All we need to know is when is it not plural?  Are there any exeptions to singular
 3. Usually when there are exceptions other languages that require this feature have this.  So let's say plural needs to be TWO people when two people are speaking.  In many languages they already dealt with that such as Peter and Paul where...   So if we look at those languages they have the case of their word for two already there.
 4. Othertimes languages disagree and that could be really important
 5. Sometimes it is context or theology driven.  Let **us** make man -> well this is God, the Trinity speaking so should be three.  Or Peter and Paul where... a chapter later.. they (2 people) said.  

So we solve it as follows

### Hints

If a word is a "magic key" like "us" we add a hint to the Strong's word for us saying look at x language if they use ... then it is likely ...  If the us is God then consider it should be Trinitarian.  

If it is small enough edge case <50 we can just add the hint to every verse as well.  For instance we may know all the Trinitian verses that would need it and put the explanation on it

We did all this in stage 2 analysis but if you find missing patterns you may need to extend it (check what work they did first then improve on it)

The idea here is don't write out every condition in your prompt, move rare edge cases and anything you can break down into an exhaustive list of words in Greek|Hebrew then use hints

### Guidance

Then for the prompt we just need general guidance.  We should cover all the major edge cases for each possible value the feature can be set to.

When we are given the verse it will extract all the strongs data and all the data about this verse for us and add it to our context.

>>>>>>> origin/feat/self-learning-tbta
## Core Requirement: The "One-Pass" Evaluator

All experiments must use a standardized evaluation loop:

<<<<<<< HEAD
1.  Input: `train_questions.jsonl` (or `test_inputs.jsonl`)
2.  Process: LLM/Script generates predictions.
=======
Create a folder in experiments/v{currentIteration}

1.  Input: `analysis/data/train.jsonl` 
2.  Process: LLM generates predictions.
>>>>>>> origin/feat/self-learning-tbta
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
    - **Discourse Context**: For features requiring discourse memory (Participant Tracking, Definiteness, Topic/Focus), include ±3 verses context or use LLM's built-in Bible knowledge. Expected accuracy: 85-90% with LLM memory approach.
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
- **Capability Analysis**: Add as primary filter - "Can the addressee perform this action?" Resolves 60%+ of ambiguous cases. If addressee cannot participate → EXCLUSIVE; if can participate → continue analysis.
- **Pattern Recognition**: Document established patterns with reliability metrics (e.g., "Divine Speech → EXCLUSIVE" 100% reliable, "Prayer to God → EXCLUSIVE of God" 100%). Once validated, patterns reliably predict similar cases.

**Additional Prompt Enhancements**:

- **Surface Form Consistency**: Add validation that predictions match expected linguistic forms

  - Example: "If predicting Routine → expect pronouns/zero anaphora, NOT indefinite NPs"
  - Example: "If predicting Comparative → expect morphology (-er) OR syntax (more...than)"
  - Include surface form checks in prompt to self-correct invalid predictions

- **Part-of-Speech Constraints**: Document and enforce POS-specific value restrictions

  - Example: "Equality (q) only valid for adjectives, NOT adverbs or verbs"
  - Example: "Intensified uses 'I' for adjectives/verbs, 'V' for adverbs"
  - Add POS validation step to prompt before final prediction

- **Referent Chain Validation**: For sequential features, validate logical progression
  - Example: "Cannot predict Routine before First Mention in discourse"
  - Example: "Generic referents don't transition to Routine tracking"
  - Build state transition rules: Valid patterns (First→Routine→Routine) vs Invalid (Routine→First)

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

### 6. Track E: Translation Consensus (The "Thesis" Approach)

**Goal**: Use the "Wisdom of the Crowd" from existing translators.
**Concept**: If 3+ languages grammatically encode the feature, their consensus is likely the truth.
**Action**:

1.  Feed the LLM the verse in 3-5 languages that _grammatically encode_ the feature (identified in Stage 1).
2.  **Prompt**: "Here is the verse in Fijian (distinguishes Dual/Plural). Fijian uses 'kedatou' (Trial). What does this imply for the feature?"
3.  **Test**: Measure accuracy on `test_inputs.jsonl` (especially for implicit features).
4.  **Note**: This track often achieves >98% accuracy for implicit features like Person/Number.

## Confidence Scoring Requirement

**All predictions must include confidence levels**:

```jsonl
{"verse": "GEN.1.26", "prediction": "Trial", "confidence": "high", "reasoning": "3 factors converge"}
{"verse": "GEN.2.4", "prediction": "Singular", "confidence": "medium", "reasoning": "morphology clear, context ambiguous"}
{"verse": "GEN.3.22", "prediction": "Plural", "confidence": "low", "reasoning": "theological debate, translations diverge"}
```

**Confidence Calibration Targets**:

- High confidence predictions: Should achieve 95%+ accuracy
- Medium confidence predictions: Should achieve 80%+ accuracy
- Low confidence predictions: Should achieve 60%+ accuracy

**If calibration fails** (e.g., high confidence only hits 70%), revise confidence criteria.

## Error Pattern Documentation

After each test iteration, categorize errors by type:

**Error Types** (from archived feature learnings):

1. **Theological Misunderstanding**: Prediction doesn't match theological context
2. **Morphological ≠ Semantic**: Following form instead of meaning
3. **Discourse Factor Missed**: Ignoring context beyond single verse
4. **Gateway Feature Ignored**: Predicting without checking constraining features
5. **Baseline Override Without Evidence**: Predicting marked value without 2-3 triggers
6. **Pattern Overgeneralization**: Applying pattern to dissimilar context

**Document in**: `experiments/training/error_patterns.md`

**Format**:

```markdown
## Error Type: Theological Misunderstanding

Count: 3 errors (15% of failures)

Example: GEN.1.26 - Predicted Plural, correct was Trial
Root cause: Missed that creation is exclusively God's work
Fix: Add theological context question to Level 1 prompt

## Error Type: Morphological ≠ Semantic

Count: 2 errors (10% of failures)
...
```

**Use error patterns to refine prompts systematically**, not random iteration.

## Execution Strategy

- Run Tracks A, B, C, D in parallel (or sequential rapid iterations).
- **Compare**: Which method yields the highest accuracy on `test_inputs.jsonl`?
- **Select**: Pick the winner (or combine B+C).
- **Finalize**: Write the winning logic into `PROMPT.md`.

## Deliverables

1.  `augment_data.py` (Script)
2.  `experiments/training/baseline_results.md`
3.  `experiments/training/logic_results.md`
4.  `experiments/training/error_patterns.md` (Categorized error analysis)
5.  `experiments/training/confidence_calibration.md` (High/Medium/Low accuracy rates)
6.  `data/strongs/*-tbta.yaml` (The generated annotation files)
7.  `PROMPT.md` (The final best performing prompt with confidence scoring)

**Success Criteria**:

- One method achieves >90% accuracy (or best possible given data limits).
- Confidence calibration within ±5% of targets (High: 95%, Medium: 80%, Low: 60%).
- Logic is explainable (not a black box).
- No "Hardcoded Exceptions" in code; rules live in data or concise logic.
- Error patterns documented and systematically addressed.

<<<<<<< HEAD
=======


## OTHER
#### Phase 3: Persist hints to Strong's files

```bash
python src/tools/append_to_strongs.py \
  --input ${TBTA-DIR}/features/{feature}/analysis/strongs-hints.jsonl \
  --feature {FeatureName} \
  --tool tbta-hints
```

This creates/updates `$DATA_DIR/strongs/{strongs}/{strongs}-tbta-hints.yaml` files.

**Key insight**: Variable patterns often become predictable with context. Look for:
- Preceding words (numerals, quantifiers): "two **men**" → Dual
- Following modifiers: "**sons** of Zebedee" (2 sons → Dual)
- Translation morphology in other languages (see 3D)

**Warning**: Low counts are overfitting. Only trust patterns with 5+ occurrences.


**Phase 3: Persist hints to verse files**

```bash
python src/tools/append_to_verses.py \
  --input ${TBTA-DIR}/features/{feature}/analysis/reason-groupings-with-hints.jsonl \
  --feature {FeatureName} \
  --tool tbta-hints
```

This creates/updates `$DATA_DIR/commentary/{BOOK}/{CCC}/{VVV}/{BOOK}-{CCC}-{VVV}-tbta-hints.yaml` files.
>>>>>>> origin/feat/self-learning-tbta
