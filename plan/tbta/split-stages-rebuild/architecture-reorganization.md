# TBTA Rebuild Architecture: LLM vs Script Classification

## Executive Summary

This document analyzes the 6 tasks mentioned in the rebuild plan and classifies each as either LLM-driven or script-driven, with clear reasoning and directory placement recommendations.

**Key Finding**: The original plan conflates two distinct workflows:
1. **TBTA Ingestion** (once): Import existing TBTA data into our system
2. **LLM Prediction Development** (per feature): Build LLM-based predictors for new features

These should be **completely separate** systems with different tools.

---

## Task Classification

### Task 1: Extract TBTA to JSONL
**File**: `extract_tbta_to_jsonl.py` (hypothetical, doesn't exist yet)

**Classification**: ✅ **SCRIPT**

**Reasoning**:
- **Deterministic**: Transform TBTA JSON → JSONL (structured → structured)
- **No semantic understanding**: Just data format conversion
- **Well-defined rules**: Read JSON, flatten/transform, write JSONL
- **Reusable**: Every TBTA feature uses same extraction logic

**Implementation**:
- **Location**: `/src/ingest_data/tbta/extract_to_jsonl.py`
- **Purpose**: One-time ingestion of TBTA data
- **Already exists**: Partial implementation in `tbta_processor.py` (converts to YAML)
- **Action**: Extend existing `tbta_processor.py` to also output JSONL format

**Usage Pattern**:
```bash
# One-time ingestion per feature
python src/ingest_data/tbta/extract_to_jsonl.py --field Clusivity --output features/clusivity/data/raw.jsonl
```

---

### Task 2: Select Reference Values
**File**: `select_reference_values.py` (hypothetical)

**Classification**: ⚠️ **HYBRID → LLM WORKFLOW**

**Reasoning**:
- **Requires judgment**: "Select 100+ values using criteria (adversarial, non-arbitrary, balanced, covering edge cases)"
- **Semantic understanding**: What makes a case "adversarial"? What is "non-arbitrary"?
- **Context-dependent**: Needs to understand theological significance, linguistic complexity
- **Not algorithmic**: Cannot be reduced to simple rules

**Original Intent**: The rebuild plan says *"you will need to use a smart LLM agent for this as strongs number is not in the TBTA source"*

**Implementation**:
- **NOT a standalone script** - this is an LLM workflow
- **Location**: Part of **Stage 4** in STAGES.md (Generate Test Set)
- **Tool**: LLM agent with access to:
  - TBTA data (via `extract_feature.py` from `tbta_processor.py`)
  - Quote Bible skill (to fetch translations)
  - Strong's data (if needed)

**Usage Pattern**:
```
# User invokes LLM workflow (not a script)
"Generate test set for Clusivity feature following STAGES.md Stage 4"

# LLM agent:
1. Runs extract_feature.py to get all TBTA verses
2. Analyzes theological significance (non-arbitrary vs arbitrary)
3. Stratifies by testament, genre, difficulty
4. Selects balanced sample
5. Outputs train.yaml, test.yaml, validate.yaml
```

**Why not a script?**:
- Identifying "adversarial" cases requires understanding theological/linguistic nuance
- Determining "non-arbitrary" contexts needs semantic analysis (Trinity references, divine speech, etc.)
- Balancing across genre/difficulty requires judgment calls

---

### Task 3: Discover Languages
**File**: `discover_languages.py` (hypothetical)

**Classification**: ⚠️ **HYBRID → LLM WORKFLOW**

**Reasoning**:
- **Original plan**: "foreach record... consider which languages from above use or require this feature"
- **Requires semantic understanding**: Which languages grammatically mark clusivity? Dual number? Evidentiality?
- **Not in TBTA data**: TBTA doesn't tell you which languages need which features
- **Linguistic knowledge required**: Must know typology of 1000+ languages

**Implementation**:
- **NOT a standalone script** - this is an LLM workflow
- **Location**: Part of **Stage 2** in STAGES.md (Language Study)
- **Tool**: LLM agent with access to:
  - Quote Bible skill (to sample verses and discover available translations)
  - Web search (to research language families)
  - Linguistic databases (if available)

**Usage Pattern**:
```
# User invokes LLM workflow
"Perform language study for Clusivity feature (STAGES.md Stage 2)"

# LLM agent:
1. Research which language families mark clusivity (Austronesian, etc.)
2. Use Quote Bible to sample verses → discover available languages
3. Filter to languages that grammatically mark this feature
4. Document in README.md
```

**Why not a script?**:
- No database of "which languages mark which features" exists in our system
- Requires linguistic research (language typology)
- Needs judgment: "Does Tagalog mark clusivity?" (yes), "Does Spanish?" (no)

---

### Task 4: Guess Translation Words
**File**: `guess_translation_words.py` (hypothetical)

**Classification**: 🤖 **LLM WORKFLOW**

**Reasoning**:
- **Original plan**: "guess which words they would use that would translate this strongs word to their language"
- **100% semantic understanding**: This is lexical prediction across 1000+ languages
- **No algorithmic approach**: Cannot write rules for "what Tagalog word translates Hebrew אֱלֹהִים"
- **Requires linguistic knowledge**: Morphology, syntax, lexicon of target languages

**Implementation**:
- **NOT a script** - pure LLM workflow
- **Location**: Part of **Stage 4-5** in STAGES.md (optional validation step)
- **Tool**: LLM agent with access to:
  - Strong's data
  - Quote Bible skill (to fetch actual translations)
  - Translation pattern analysis

**Usage Pattern**:
```
# LLM workflow (if needed for validation)
"Analyze translation patterns for clusivity in Tagalog/Fijian/Samoan"

# LLM agent:
1. Fetch verse translations from Quote Bible skill
2. Identify which words mark clusivity in each language
3. Build pattern database (e.g., Tagalog: "tayo" = inclusive, "kami" = exclusive)
4. Use for validation/refinement
```

**Why not a script?**:
- Requires understanding of 1000+ language grammars
- No programmatic way to "guess" translations
- Better approach: **fetch actual translations** via Quote Bible skill, analyze them

**KEY INSIGHT**: We don't need to *guess* - we can **look up actual translations** using Quote Bible skill!

---

### Task 5: Score TBTA Accuracy
**File**: `score_tbta_accuracy.py` (hypothetical)

**Classification**: ✅ **SCRIPT** (but with important caveats)

**Reasoning**:
- **Deterministic**: Compare predictions vs TBTA ground truth
- **Well-defined**: Load predictions file, load answers file, calculate accuracy
- **No semantic understanding**: Just counting matches/mismatches
- **Reusable**: Every feature uses same scoring logic

**Implementation**:
- **Location**: `/src/tools/predict/score_predictions.py`
- **Purpose**: Generic scoring tool for any TBTA feature
- **Reusable across features**: Works for clusivity, degree, discourse-genre, etc.

**Usage Pattern**:
```bash
# Score predictions against ground truth
python src/tools/predict/score_predictions.py \
  --predictions features/clusivity/experiments/test_predictions.yaml \
  --answers features/clusivity/experiments/test.yaml \
  --output features/clusivity/experiments/scoring_report.yaml
```

**CAVEAT**: This is a **helper script** for the LLM workflow, not a standalone tool. The LLM agent calls this during Stage 5-6 validation.

---

### Task 6: Validate Predictions
**File**: `validate_predictions.py` (hypothetical)

**Classification**: ⚠️ **HYBRID → LLM WORKFLOW + SCRIPTS**

**Reasoning**:
- **Ambiguous task**: What does "validate" mean?
  - Just check accuracy? (script)
  - Analyze errors and recommend fixes? (LLM)
  - Compare with external translations? (LLM + Quote Bible skill)

**Implementation Options**:

**Option A: Simple Validation (Script)**
- **File**: `/src/tools/predict/validate_format.py`
- **Purpose**: Check prediction file format is valid
- **Checks**: Required fields present, value types correct, verse references valid

**Option B: Comprehensive Validation (LLM Workflow)**
- **Location**: Part of **Stage 6** in STAGES.md (Peer Review)
- **Tool**: LLM agent performs:
  - Error analysis (6-step process)
  - Theological review
  - Linguistic review
  - Methodological review
  - Translation practitioner impact testing

**Recommendation**: Split into two tools:
1. **Script**: `/src/tools/predict/validate_format.py` (format validation)
2. **LLM Workflow**: Stage 6 in STAGES.md (comprehensive peer review)

---

## Directory Structure Recommendations

### Current Structure Issues

The scripts mentioned in the plan don't exist yet. We need to organize them properly:

```
src/
├── ingest_data/          # One-time TBTA import (existing)
│   └── tbta/
│       ├── tbta_processor.py      # ✅ EXISTS: Convert TBTA → YAML
│       ├── extract_feature.py     # ✅ EXISTS: Extract feature to YAML
│       └── extract_to_jsonl.py    # ❌ TODO: Add JSONL output option
│
└── tools/
    └── predict/          # ❌ CREATE: Reusable prediction tools
        ├── score_predictions.py    # Generic accuracy scoring
        ├── validate_format.py      # Format validation
        └── README.md               # How to use these tools
```

### Proposed New Structure

```
src/
├── ingest_data/tbta/              # TBTA ingestion only (one-time)
│   ├── tbta_processor.py          # Convert TBTA → YAML (existing)
│   ├── extract_feature.py         # Extract feature data (existing)
│   └── README.md                  # Ingestion documentation
│
└── tools/predict/                 # Reusable prediction helpers
    ├── score_predictions.py       # Score predictions vs ground truth
    ├── validate_format.py         # Validate prediction file format
    ├── stratify_sample.py         # Stratified sampling helper
    └── README.md                  # Tool usage guide
```

**Key Principle**:
- `/src/ingest_data/tbta/` = One-time TBTA import scripts
- `/src/tools/predict/` = Reusable helpers for LLM prediction workflows
- Feature-specific work lives in `/plan/tbta-rebuild-with-llm/features/{feature}/`

---

## What Should Be LLM Workflows (Not Scripts)

The following are **LLM workflows** that should NOT be standalone scripts:

### 1. Select Reference Values (Task 2)
**Why**: Requires judgment about adversarial cases, non-arbitrary contexts, theological significance

**Where**: STAGES.md Stage 4 (Generate Test Set)

**Tools needed**:
- `extract_feature.py` (to get TBTA data)
- Quote Bible skill (optional: fetch translations)
- LLM judgment for stratification

### 2. Discover Languages (Task 3)
**Why**: Requires linguistic knowledge of which languages mark which features

**Where**: STAGES.md Stage 2 (Language Study)

**Tools needed**:
- Web search (research language families)
- Quote Bible skill (discover available translations)
- Linguistic analysis

### 3. Guess Translation Words (Task 4)
**Why**: Impossible to algorithmically predict translations; better to **fetch actual translations**

**Where**: STAGES.md Stage 4-5 (optional validation)

**Tools needed**:
- Quote Bible skill (fetch real translations)
- Pattern analysis (what words mark this feature)

### 4. Comprehensive Validation (Task 6)
**Why**: Error analysis, theological review, peer review require human-like judgment

**Where**: STAGES.md Stage 6 (Peer Review)

**Tools needed**:
- `score_predictions.py` (accuracy calculation)
- LLM-based error analysis
- Multi-agent peer review

---

## What Should Be Scripts

The following are **deterministic scripts** that should be created:

### 1. Score Predictions (Task 5)
**File**: `/src/tools/predict/score_predictions.py`

**Purpose**: Compare predictions vs ground truth, calculate accuracy

**Usage**:
```bash
python src/tools/predict/score_predictions.py \
  --predictions test_predictions.yaml \
  --answers test.yaml \
  --output scoring_report.yaml
```

**Output**:
```yaml
feature: clusivity
total_verses: 150
correct: 148
accuracy: 98.67%
errors:
  - verse: "GEN.001.026"
    predicted: "inclusive"
    actual: "exclusive"
  - verse: "MAT.028.019"
    predicted: "exclusive"
    actual: "inclusive"
```

### 2. Validate Format (Task 6, partial)
**File**: `/src/tools/predict/validate_format.py`

**Purpose**: Check prediction file structure is valid

**Checks**:
- Required fields present (`verse`, `feature`, `value`)
- Verse references valid (USFM format)
- Values match allowed values for this feature
- No duplicate verses

### 3. Stratified Sampling (Helper for Task 2)
**File**: `/src/tools/predict/stratify_sample.py`

**Purpose**: Helper for LLM to perform stratified sampling

**Usage**:
```bash
python src/tools/predict/stratify_sample.py \
  --input raw_tbta_data.yaml \
  --train-split 0.4 \
  --test-split 0.3 \
  --validate-split 0.3 \
  --stratify-by testament,genre \
  --output-dir experiments/data/
```

**Note**: This script does the mechanical work of splitting; **LLM still decides** which verses are adversarial, non-arbitrary, etc.

---

## Implementation Priority

### Phase 1: Core Scripts (Immediate)
1. ✅ `tbta_processor.py` - **EXISTS**, no changes needed
2. ✅ `extract_feature.py` - **EXISTS**, no changes needed
3. ❌ `score_predictions.py` - **CREATE** (highest priority)
4. ❌ `validate_format.py` - **CREATE** (medium priority)

### Phase 2: Helper Scripts (As Needed)
5. ❌ `stratify_sample.py` - **CREATE** (low priority, LLM can do manually)

### Phase 3: LLM Workflows (Ongoing)
6. **STAGES.md** - Already documented, LLM agents follow this
7. Feature-specific work - Happens in `/plan/tbta-rebuild-with-llm/features/{feature}/`

---

## Critical Realizations

### 1. We Already Have Most Tools Needed

**Existing Tools**:
- ✅ `tbta_processor.py` - Ingest TBTA data
- ✅ `extract_feature.py` - Extract feature-specific data
- ✅ Quote Bible skill - Fetch translations for validation

**Missing Tools** (small gaps):
- ❌ `score_predictions.py` - Trivial to write (100 lines)
- ❌ `validate_format.py` - Simple validation logic

### 2. Most "Scripts" Are Actually LLM Workflows

The rebuild plan conflates:
- **Scripts** (deterministic tools)
- **LLM workflows** (judgment-based processes)

**Key Tasks That Are LLM Workflows**:
- Selecting adversarial test cases (requires judgment)
- Discovering languages that mark features (requires linguistic knowledge)
- Analyzing translation patterns (requires semantic understanding)
- Comprehensive validation (requires error analysis + peer review)

### 3. Don't Over-Engineer

We don't need:
- ❌ `guess_translation_words.py` - Just use Quote Bible skill to fetch actual translations
- ❌ `discover_languages.py` - LLM does this research in Stage 2
- ❌ `select_reference_values.py` - LLM does stratification in Stage 4

We DO need:
- ✅ `score_predictions.py` - Mechanical accuracy calculation
- ✅ `validate_format.py` - Format checking

---

## Recommended Actions

### 1. Create Missing Scripts (Immediate)

**File**: `/src/tools/predict/score_predictions.py`
- Compare predictions vs ground truth
- Calculate accuracy percentages
- List errors for LLM analysis

**File**: `/src/tools/predict/validate_format.py`
- Check prediction file structure
- Validate verse references
- Check value enumerations

### 2. Document LLM Workflows (Already Done)

**File**: `/bible-study-tools/tbta/features/STAGES.md`
- ✅ Stage 1: Research TBTA Documentation
- ✅ Stage 2: Language Study (includes "discover languages")
- ✅ Stage 3: Scholarly Research
- ✅ Stage 4: Generate Test Set (includes "select reference values")
- ✅ Stage 5: Develop Algorithm (includes translation analysis)
- ✅ Stage 6: Validate & Peer Review (includes comprehensive validation)

### 3. Clarify Directory Purposes

**`/src/ingest_data/tbta/`**: One-time TBTA ingestion
- Convert TBTA export → our YAML format
- Extract feature data for analysis
- **Run once per TBTA update**

**`/src/tools/predict/`**: Reusable prediction helpers
- Scoring, validation, sampling helpers
- Called by LLM agents during feature development
- **Generic across all TBTA features**

**`/plan/tbta-rebuild-with-llm/features/{feature}/`**: Feature-specific work
- LLM-driven experiments
- Training/test/validate data
- Algorithm development
- **One directory per feature**

---

## Summary

| Task | Classification | Location | Reasoning |
|------|---------------|----------|-----------|
| 1. Extract TBTA to JSONL | ✅ Script | `/src/ingest_data/tbta/` | Deterministic data conversion |
| 2. Select Reference Values | 🤖 LLM Workflow | STAGES.md Stage 4 | Requires judgment (adversarial, non-arbitrary) |
| 3. Discover Languages | 🤖 LLM Workflow | STAGES.md Stage 2 | Requires linguistic research |
| 4. Guess Translation Words | 🤖 LLM Workflow | STAGES.md Stage 4-5 | Use Quote Bible instead of guessing |
| 5. Score TBTA Accuracy | ✅ Script | `/src/tools/predict/` | Deterministic accuracy calculation |
| 6. Validate Predictions | ⚠️ Hybrid | Script (format) + LLM (comprehensive) | Format check = script, error analysis = LLM |

**Key Insight**: The rebuild plan describes an **LLM-driven development process** with **script-based helpers**, not a collection of standalone scripts. Most "tasks" are actually stages in an LLM workflow (STAGES.md), with minimal scripting needed for mechanical operations like scoring.

**Next Steps**:
1. Create `/src/tools/predict/score_predictions.py` (30 min)
2. Create `/src/tools/predict/validate_format.py` (30 min)
3. Update documentation to clarify LLM workflows vs scripts
4. Remove any misconception that we need 6 complex scripts

**Total New Code**: ~200 lines (2 simple scripts)
