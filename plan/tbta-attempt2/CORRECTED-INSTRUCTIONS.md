# CORRECTED TBTA INSTRUCTIONS - Anti-Cheating Edition

**Created**: 2025-11-16
**Purpose**: Prevent extraction cheating, enforce blind testing methodology
**Replaces**: Misleading "Tier 0 Check" pattern from reusable-patterns.md

---

## ❌ DELETE THIS PATTERN ENTIRELY

**From reusable-patterns.md lines 13-32**:

```markdown
### 1. **Check for Explicit Encoding FIRST (Tier 0)**
If ALWAYS present → Extract directly  ❌ THIS IS CHEATING
```

**Why it's wrong**: TBTA only covers 37% of the Bible. Even if explicit encoding exists, we need PROMPTS that work on the unlabeled 63%.

---

## ✅ THE CORRECT APPROACH

### Core Principle

**You are building a PREDICTION SYSTEM, not an extraction tool.**

**Goal**: Create prompts that can label ANY verse (whether TBTA has it or not)
**Validation**: Use TBTA's 37% coverage as answer sheets for scoring only
**Method**: NEVER look at TBTA answers during development (blind testing)

---

## BLIND TESTING MANDATORY WORKFLOW

### Stage 4: Generate Test Sets (SUBAGENT REQUIRED)

**CRITICAL**: Main agent NEVER sees answer sheets

```
Subagent 1 (Data Extractor):
├─ Reads TBTA YAML files
├─ Creates answer sheets: train.yaml, test.yaml, validate.yaml
│  (Contains verse refs + TBTA values)
├─ Creates question sheets: train_questions.yaml, etc.
│  (Contains verse refs + translations ONLY)
└─ Returns ONLY question sheet paths to main agent

Main Agent:
├─ Receives question sheets (verse text + translations)
├─ NEVER looks at answer sheets
└─ Develops prompts from question sheets only
```

### Stage 5: Develop Prompts (BLIND TO ANSWERS)

**Main Agent Workflow** (NEVER sees TBTA values):

```
Step 1: Analyze Question Sheets
- Read train_questions.yaml (verse text + translations)
- Analyze translation patterns to DISCOVER the answer
- Use theological/semantic analysis
- Develop PROMPT that predicts from verse text alone

Step 2: Lock Predictions
- Apply prompt to test_questions.yaml
- Generate predictions file
- Git commit BEFORE checking accuracy
- Timestamp lock prevents modification

Step 3: Blind Scoring
Subagent 2 (Predictor):
├─ Receives: prompt + test_questions.yaml
├─ Applies prompt to each verse
├─ Creates predictions.yaml
└─ Returns predictions file path

Subagent 3 (Scorer):
├─ Receives: predictions.yaml + test.yaml (answer sheet)
├─ Calculates accuracy
├─ Identifies error verse references
└─ Returns ONLY: accuracy % + error refs (NOT the answers)

Main Agent:
├─ Receives: "81% accuracy, errors on verses X, Y, Z"
├─ Does NOT see actual TBTA values
├─ Analyzes WHY errors occurred (without seeing answers)
└─ Refines prompt and repeats
```

**Step 4: Iterate Without Contamination**
- Main agent refines prompt based on error patterns
- Repeat blind scoring
- Continue until ≥95% accuracy

### Stage 6: Validate (Continue Blind)

```
Subagent 4 (Blind Validator):
├─ Applies final prompt to validate_questions.yaml
├─ Returns predictions file

Subagent 5 (Final Scorer):
├─ Scores against validate.yaml
├─ Returns: accuracy %, error refs
└─ Main agent sees percentage only

Main Agent:
├─ If ≥95% → Proceed to peer review
└─ If <95% → Return to Stage 5
```

---

## CHEATING DETECTION CHECKLIST

**Before finalizing ANY feature, answer these questions:**

### ❌ RED FLAGS (If ANY are "yes", approach is INVALID)

- [ ] Did you look at TBTA YAML field values during prompt development?
- [ ] Did you extract answers from TBTA character positions?
- [ ] Did you use TBTA encoding as your prediction method?
- [ ] Did you see answer sheets before locking predictions?
- [ ] Did you read test.yaml or validate.yaml during development?
- [ ] Does your "algorithm" just copy TBTA fields?

### ✅ REQUIRED (ALL must be "yes")

- [ ] Did you develop prompts from verse text + translations only?
- [ ] Did you use blind subagents for all scoring?
- [ ] Did you lock predictions (git commit) BEFORE checking accuracy?
- [ ] Can your prompt work on verses TBTA has never labeled?
- [ ] Did you NEVER see actual TBTA values during development?
- [ ] Is your final deliverable a PROMPT (not an extraction script)?

---

## THE "UNLABELED VERSE" TEST

**Critical Question**:

> "If I give you a verse from Leviticus (which TBTA has never annotated), can your prompt predict the {feature} value?"

**Valid Approach**:
- ✅ YES - I have a prompt that analyzes verse text, context, translations
- ✅ The prompt works on ANY verse, regardless of TBTA coverage

**Invalid Approach (Cheating)**:
- ❌ NO - I need TBTA YAML to extract the value from position X
- ❌ My "algorithm" only works on verses TBTA has already labeled
- ❌ I'm just copying TBTA's existing annotations

---

## CORRECT INTERPRETATION OF DATA STRUCTURE

### Research Phase (Stages 1-3): CAN Look at TBTA Structure

**Purpose**: Understand the answer sheet format for validation
**What to check**: How does TBTA encode this feature?
**Example**: "Person is encoded at position 10: A=inclusive, B=exclusive"

**CRITICAL**: This is for understanding the VALIDATION format ONLY.
- ✅ Use this knowledge to create answer sheets
- ❌ NEVER use this as your prediction method

### Example of Proper Use

```markdown
## Stage 1: Research TBTA Documentation

I examined TBTA's data structure and found:
- Polarity: Encoded at position 7 (nouns) / position 4 (verbs)
- Values: + (affirmative), - (negative)

**IMPORTANT**: This tells me the ANSWER SHEET format.
My goal is to develop a PROMPT that predicts these values
from verse text alone, WITHOUT looking at TBTA YAML fields.

I will use TBTA's encoding as:
✅ Answer sheets for blind validation
❌ NOT as my prediction method
```

---

## TRANSLATION VALIDATION: THE PRIMARY METHOD

**This is the CORRECT approach** (Pattern #2 from archive)

### Why Translation Validation Works

- With ~1000 Bible translations, someone has dealt with your feature
- Languages that grammatically encode the feature reveal the answer
- 8-9 language consensus = 98% confidence
- This is DISCOVERY, not extraction from TBTA

### Correct Workflow

```
Step 1: Identify Encoding Languages
- Which language families grammatically mark {feature}?
- Example: Clusivity → Indonesian, Tagalog, Fijian, Hawaiian, Quechua, etc.

Step 2: Analyze Translations (Question Sheets)
- For each verse in train_questions.yaml:
  - Indonesian uses "kita" (inclusive) or "kami" (exclusive)?
  - Tagalog uses "tayo" (inclusive) or "kami" (exclusive)?
  - Do 8/9 translations agree?

Step 3: Discover Pattern
- 8/9 translations use inclusive → High confidence: INCLUSIVE
- This is the ACTUAL answer (what translators chose)
- Not from TBTA, from real translation decisions

Step 4: Develop Prompt
- Create prompt that identifies contexts where translators chose inclusive
- Example: "Divine speech with Father+Son+Spirit → inclusive (Trinity)"
- Test prompt on new verses

Step 5: Validate Against TBTA (Blind)
- Apply prompt to test_questions.yaml
- Compare predictions to test.yaml (answer sheet)
- Main agent sees accuracy only
```

**This is NOT cheating because**:
- You're analyzing TRANSLATIONS (question sheets), not TBTA answers
- You're discovering patterns from what translators did
- Your prompt predicts from verse context, not TBTA fields
- Works on unlabeled verses (uses linguistic patterns, not TBTA extraction)

---

## CORRECTED "DATA STRUCTURE VERIFICATION" PATTERN

**Replaces misleading "Tier 0 Check"**

### Purpose

Understand TBTA encoding for answer sheet creation ONLY.

### Application

**Stage 1 (Research Phase)**:
```
Step 1: Check TBTA YAML Structure
- How does TBTA encode this feature?
- Example: "Position 10, A=inclusive, B=exclusive"

Step 2: Determine Use Case
IF feature is PRESENT in TBTA:
  └─ Use as ANSWER SHEET for blind validation
     ❌ DO NOT extract as solution
     ✅ DO develop prediction prompts

IF feature is ABSENT in TBTA:
  └─ Develop prediction from translations only
     (No TBTA validation available)

Step 3: Create Answer Sheets
- Subagent extracts TBTA data → train.yaml, test.yaml, validate.yaml
- Main agent NEVER sees these files
- Used for blind scoring only
```

**CRITICAL RULES**:
- ✅ Check TBTA structure to understand answer format
- ✅ Create answer sheets for validation
- ❌ NEVER extract as your prediction method
- ❌ NEVER look at answer sheets during development
- ✅ ALWAYS develop prompts that work without TBTA

---

## RED FLAG PHRASES (Indicate Cheating)

If your feature documentation contains ANY of these, you're cheating:

❌ "Extract from TBTA position X"
❌ "Direct YAML extraction achieves 100% accuracy"
❌ "Check TBTA field to determine value"
❌ "Read character position X from TBTA encoding"
❌ "Use TBTA YAML as ground truth during development"
❌ "Algorithm: Extract field Y from TBTA data"

✅ **Valid phrases**:
✅ "Analyze translations to discover patterns"
✅ "Develop prompt that predicts from verse text"
✅ "Lock predictions before checking TBTA"
✅ "Blind subagent scores against answer sheet"
✅ "Prompt works on any verse (labeled or unlabeled)"
✅ "Use TBTA for validation only, not prediction"

---

## SUMMARY: THE CORRECT MENTAL MODEL

### TBTA's 37% Coverage is the ANSWER SHEET

```
Bible Verses: 100%
├─ TBTA Labeled: 37% → Use as ANSWER SHEETS (validation only)
└─ TBTA Unlabeled: 63% → This is WHY we need prediction prompts
```

### Your Goal

```
Develop PROMPTS that:
✅ Work on the 63% TBTA hasn't labeled
✅ Predict from verse text + context + translations
✅ Can be validated against TBTA's 37% (blind scoring)
✅ Achieve ≥95% accuracy on validation set

❌ NOT your goal:
❌ Copy TBTA's existing 37% annotations
❌ Extract from TBTA YAML fields
❌ Only work on verses TBTA already has
```

### The Deliverable

**NOT**: An extraction script that reads TBTA YAML
**YES**: A PROMPT that an LLM can apply to any verse

**Example Valid Deliverable**:
```markdown
## Final Prompt (v2.2)

For verse {reference}, determine person (inclusive/exclusive):

LEVEL 1 - Theological Analysis:
1. Divine speech including Father+Son+Spirit? → INCLUSIVE (Trinity)
2. Prayer to God from humans? → EXCLUSIVE (God not in "we")
3. Apostolic witness to events? → EXCLUSIVE (addressee wasn't there)

LEVEL 2 - Capability Analysis:
1. Can addressee perform/participate in this action?
2. If NO (divine-only) → EXCLUSIVE
3. If YES (human-capable) → Continue to identity analysis

[... rest of prompt ...]

This prompt works on ANY verse, regardless of TBTA coverage.
Validated against TBTA's 37% via blind testing: 81% accuracy.
```

---

## ENFORCEMENT

**This is the THIRD time this mistake has been made.**

From now on:
1. ✅ All feature work archived if cheating detected
2. ✅ Explicit note added explaining why invalid
3. ✅ Cheating detection checklist required before finalization
4. ✅ Queen coordinator monitors for extraction red flags
5. ✅ "Tier 0 Check" pattern DELETED from reusable patterns

**Zero tolerance for extraction-based approaches going forward.**

---

---

## ARBITRARY VS NON-ARBITRARY FRAMEWORK (OFFICIAL)

**Now integrated into STAGES.md** - See `/workspace/bible-study-tools/tbta/features/STAGES.md`

### Quick Reference

**Classification** (Stage 3):
- Default: arbitrary (space-saving - not stored)
- Only mark non-arbitrary when theologically significant
- Required file: `experiments/ARBITRARITY-CLASSIFICATION.md`

**Non-Arbitrary Criteria** (any one triggers non-arbitrary):
1. Affects core doctrine (Trinity, salvation, God's nature)
2. Divine speech impact (commands, promises, judgments)
3. Interpretive disambiguation (theological ambiguity)
4. Church practice/authority implications
5. Denominational differences exist

**Output Format Difference**:
```yaml
# Arbitrary (85-90% of cases):
answer: {single value}
confidence: {high/medium/low}

# Non-arbitrary (10-15% of cases):
arbitrarity: non-arbitrary
preferred: {value}
preferred_rationale: "{why}"
alternatives:
  - value: {alternative}
    problems: ["{issue1}", "{issue2}"]
    when_appropriate: "{context}"
translator_warning: "{critical guidance}"
```

**Required Files for Non-Arbitrary Features**:
1. `experiments/ARBITRARITY-CLASSIFICATION.md` (Stage 3)
2. `experiments/THEOLOGICAL-ANALYSIS.md` (Stage 5)
3. Multi-answer prompt implementation (Stage 5)

**Enhanced Validation** (Stage 6):
- 9 additional theological checks
- Test cases must include non-arbitrary contexts
- Production checklist: 9-point arbitrarity handling

**See**: `/workspace/plan/tbta-attempt2/STAGES-INTEGRATION-COMPLETE.md` for complete details

---

**Status**: Corrected instructions ready for Phase 1A restart
**Next Action**: Apply to new feature development attempts
**Prevention**: Cheating detection checklist + corrected patterns + arbitrary/non-arbitrary framework
