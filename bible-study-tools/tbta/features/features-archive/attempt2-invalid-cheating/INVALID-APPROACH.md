# INVALID APPROACH - DO NOT REPLICATE

**Date**: 2025-11-16
**Attempt**: Hive Mind Phase 1A
**Features**: polarity, person-system, number-system
**Status**: ❌ INVALID - Violated fundamental TBTA methodology

---

## Why This Approach is Invalid

### The Fundamental Error

These features **extracted answers directly from TBTA YAML** instead of **developing prediction prompts**. This violates the core purpose of TBTA feature development.

### What We Did Wrong

**Polarity Feature**:
- ❌ Extracted polarity from TBTA YAML position 7 (nouns) / position 4 (verbs)
- ❌ Celebrated "100% accuracy" by copying TBTA's answers
- ❌ Created NO prediction capability for unlabeled verses

**Person-System Feature**:
- ❌ Extracted person from TBTA YAML position 10
- ❌ Used TBTA encoding as the solution instead of validation
- ⚠️ Did develop some prediction prompts, but contaminated by seeing answers

**Number-System Feature**:
- ❌ Identified TBTA position 2 as explicit encoding
- ❌ Treated extraction as the goal instead of prediction development

### Why This is Cheating

**The Real Goal**: TBTA only covers **37% of the Bible** (11,649 verses across 34 books). We need to:
1. Use TBTA's 37% as **answer sheets for validation only**
2. Develop **prompts that predict from verse text alone**
3. Apply those prompts to the **other 63% of the Bible** that TBTA hasn't labeled

**What We Did Instead**: We just copied TBTA's existing answers for the 37% it covers, which:
- Provides ZERO value (TBTA already has those answers)
- Creates NO capability to label the remaining 63%
- Violates blind testing methodology (we saw the answers during development)

---

## Source of Miscommunication

### The Problematic Pattern

From `/workspace/plan/tbta-attempt2/reusable-patterns.md`:

```markdown
### 1. **Check for Explicit Encoding FIRST (Tier 0)**
**Pattern**: Always verify if feature can be directly extracted before building prediction systems.

**Application**:
Step 0: Before designing algorithms, check TBTA YAML structure
- If ALWAYS present → Extract directly ❌ THIS IS WRONG
```

**Why This Pattern is Misleading**:
- It promotes extraction as a valid solution
- It confuses "checking data structure" with "solving the problem"
- It led agents to think copying TBTA = success

### What the Pattern SHOULD Say

```markdown
### Data Structure Verification (Research Phase Only)

**Purpose**: Understand how TBTA encodes this feature (for validation purposes)

**Application**:
Step 0 (Research Phase): Check TBTA YAML structure
- If PRESENT: Use as answer sheet for blind validation
- If ABSENT: Develop prediction from translations only

**CRITICAL**: NEVER extract as the solution. Always develop prompts that predict from verse text.
```

---

## The Correct Approach

### Stages 1-3: Research (CAN look at TBTA for understanding)
- Understand how TBTA encodes the feature
- Study language families that require it
- Research scholarly literature

### Stage 4: Generate Test Sets (CRITICAL - Must use subagent)
**Main agent NEVER sees answer sheets**:

1. **Subagent** extracts TBTA data → `train.yaml`, `test.yaml`, `validate.yaml` (answer sheets)
2. **Subagent** extracts translations → `train_questions.yaml`, etc. (question sheets)
3. **Main agent** receives ONLY question sheets (verse text + translations)
4. Main agent NEVER looks at answer sheets

### Stage 5: Develop Prompts (BLIND to answers)
**Main agent workflow**:
1. Read question sheets (verse text + translations)
2. Analyze translation patterns to discover answers
3. Develop PROMPT that predicts from verse text alone
4. Lock predictions (git commit BEFORE checking accuracy)
5. **Blind subagent** applies prompt to test set
6. **Scorer subagent** compares predictions to answer sheet
7. **Main agent** receives ONLY accuracy % (NOT the actual answers)
8. If <95% accuracy: analyze errors, refine prompt, repeat

### Stage 6: Validate (Continue blind testing)
- Apply final prompt to validate set (never seen before)
- Score against answer sheet
- Only after ≥95% accuracy: conduct peer reviews

---

## Lessons Learned

### For Future Attempts

1. **Delete "Tier 0 Check" pattern** - It's misleading and promotes cheating
2. **Emphasize blind testing from the start** - Main agent NEVER sees answer sheets
3. **Goal is PROMPTS, not extraction** - Final deliverable is a prompt that works on any verse
4. **TBTA is validation only** - Use for scoring, never for development
5. **Translation analysis is discovery** - Use translations to figure out the answer, not TBTA

### Red Flags to Watch For

❌ "Extract from TBTA position X"
❌ "Direct extraction achieves 100% accuracy"
❌ "Check TBTA field to determine value"
❌ "Use TBTA encoding as ground truth during development"

✅ "Analyze translations to discover patterns"
✅ "Develop prompt that predicts from verse text"
✅ "Lock predictions before checking TBTA"
✅ "Blind subagent scores against answer sheet"

---

## Impact of This Failure

**Time Wasted**: 4 hours of parallel agent execution
**Features Invalidated**: 3 (polarity, person-system, number-system)
**Lessons Learned**: Critical - will prevent future failures

**This is the THIRD time this mistake was made**, indicating the instructions need clearer emphasis on:
1. NEVER look at TBTA answers during development
2. Goal is PREDICTION, not extraction
3. Blind testing is mandatory, not optional

---

## Action Items

1. ✅ Archive invalid attempts
2. ✅ Document why approach is wrong
3. ⏳ Fix reusable-patterns.md to remove Tier 0 pattern
4. ⏳ Create corrected instructions emphasizing blind methodology
5. ⏳ Add explicit "CHEATING DETECTION" checklist
6. ⏳ Start over with proper blind testing from Stage 4

---

**Archived**: 2025-11-16
**Reason**: Violated blind testing methodology by extracting answers from TBTA instead of developing prediction prompts
**Prevention**: Remove "Tier 0 Check" pattern, emphasize blind testing, add cheating detection checklist
