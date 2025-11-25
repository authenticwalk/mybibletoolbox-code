# Phase 1A Restart: Corrected Blind Testing Methodology

**Status**: Ready to Execute
**Created**: 2025-11-17
**Purpose**: Restart Phase 1A with corrected methodology - no extraction cheating

---

## Executive Summary

**Previous Attempt**: Failed - all 3 features extracted from TBTA YAML (cheating)
**Root Cause Fixed**: Misleading "Tier 0 Check" pattern deleted, blind testing enforced
**Framework Integrated**: Arbitrary/non-arbitrary for theological safety
**Ready**: All corrected methodology documents created and validated

---

## Phase 1A Features

### 1. Polarity (Affirmative/Negative)
**TBTA Position**: Position 7 (nouns) / Position 4 (verbs)
**Arbitrary Status**: Mostly arbitrary (95%)
**Non-Arbitrary Contexts**: Divine commands (imperative vs prohibition)
**Estimated Time**: 8-12 hours (translation validation)

### 2. Person System (Clusivity)
**TBTA Position**: Position 10
**Arbitrary Status**: Mixed (40% non-arbitrary)
**Non-Arbitrary Contexts**: Trinity (Gen 1:26), prayer (Matt 6:9), apostolic authority
**Estimated Time**: 12-16 hours (theological analysis required)

### 3. Number System (Trial/Dual/Plural)
**TBTA Position**: Position 2
**Arbitrary Status**: Mixed (15% non-arbitrary)
**Non-Arbitrary Contexts**: Trinity, divine unity, resurrection appearances
**Estimated Time**: 12-16 hours (theological analysis required)

**Total Phase 1A Estimate**: 32-44 hours (vs. 4 hours wasted on cheating)

---

## Mandatory Methodology Compliance

### ✅ CORRECTED-INSTRUCTIONS.md Compliance

**Before any feature work begins, ALL agents MUST**:
1. Read CORRECTED-INSTRUCTIONS.md in full
2. Understand blind testing workflow (no answer sheets during development)
3. Know cheating detection checklist by heart
4. Pass "unlabeled verse test" mentally

**Red Flags to Watch For** (immediate archival if detected):
- ❌ "Extract from TBTA position X"
- ❌ "Direct YAML extraction achieves 100% accuracy"
- ❌ "Check TBTA field to determine value"
- ❌ Reading answer sheets during development
- ❌ Seeing TBTA values before locking predictions

### ✅ STAGES.md Arbitrary/Non-Arbitrary Compliance

**Stage 3 - Required Analysis**:
1. Create `experiments/ARBITRARITY-CLASSIFICATION.md`
2. Classify all contexts (default=arbitrary, only mark non-arbitrary)
3. Identify theological stakes for non-arbitrary contexts
4. Document affected doctrines and cultural sensitivities

**Stage 4 - Test Set Requirements**:
- Include ≥2 cases of each non-arbitrary reason group
- Mark non-arbitrary verses with metadata
- Ensure balanced theological representation

**Stage 5 - Prompt Development**:
- For arbitrary: Single answer output
- For non-arbitrary: Multi-answer output (preferred + alternatives)
- Create `experiments/THEOLOGICAL-ANALYSIS.md` if non-arbitrary contexts exist

**Stage 6 - Enhanced Validation**:
- 9 additional theological checks for non-arbitrary features
- Test cases must cover all non-arbitrary contexts
- Verify no false teaching enabled

---

## Blind Testing Protocol (MANDATORY)

### Stage 4: Generate Test Sets

**Subagent 1 (Data Extractor)** - Works alone, main agent NEVER sees:
```yaml
Tasks:
  1. Read TBTA YAML files for feature
  2. Extract verse references + TBTA values
  3. Create answer sheets:
     - experiments/train.yaml (verse_ref + TBTA_value)
     - experiments/test.yaml (verse_ref + TBTA_value)
     - experiments/validate.yaml (verse_ref + TBTA_value)
  4. Fetch translations for each verse
  5. Create question sheets:
     - experiments/train_questions.yaml (verse_ref + translations ONLY)
     - experiments/test_questions.yaml (verse_ref + translations ONLY)
     - experiments/validate_questions.yaml (verse_ref + translations ONLY)
  6. Return ONLY question sheet paths to main agent
  7. Store answer sheets in experiments/ (main agent forbidden from reading)
```

**Main Agent** - NEVER sees answer sheets:
```yaml
Receives:
  - experiments/train_questions.yaml (verse text + translations)
  - experiments/test_questions.yaml (verse text + translations)
  - experiments/validate_questions.yaml (verse text + translations)

Forbidden:
  - experiments/train.yaml (ANSWER SHEET)
  - experiments/test.yaml (ANSWER SHEET)
  - experiments/validate.yaml (ANSWER SHEET)
  - Any TBTA YAML files with feature values
```

### Stage 5: Develop Prompts (Blind)

**Main Agent Workflow** (zero answer contamination):
```
Step 1: Analyze Question Sheets
├─ Read train_questions.yaml (verse text + translations)
├─ Identify encoding languages (which mark this feature?)
├─ Analyze translation patterns (what did translators choose?)
├─ Discover semantic/theological patterns
└─ Develop PROMPT from verse text analysis alone

Step 2: Lock Initial Predictions
├─ Apply prompt to test_questions.yaml
├─ Generate predictions.yaml
├─ Git commit with timestamp (LOCKED - no modifications allowed)
└─ NEVER look at test.yaml (answer sheet)

Step 3: Blind Scoring (Subagent)
Subagent 2 (Predictor):
├─ Receives: prompt + test_questions.yaml
├─ Applies prompt to each verse
├─ Creates predictions.yaml
└─ Returns predictions file path

Subagent 3 (Scorer):
├─ Receives: predictions.yaml + test.yaml (answer sheet)
├─ Calculates accuracy percentage
├─ Identifies error verse references (NOT values)
└─ Returns ONLY: "X% accuracy, errors on verses: A, B, C"

Step 4: Error Analysis (Main Agent - Still Blind)
├─ Receives: "81% accuracy, errors on MAT.006.009, GEN.001.026, etc."
├─ Does NOT see actual TBTA values
├─ Re-reads question sheets for error verses
├─ Analyzes WHY errors occurred (translation patterns)
├─ Refines prompt WITHOUT seeing answers
└─ Repeats Steps 2-4 until ≥95%
```

### Stage 6: Validate (Continue Blind)

**Final Validation** (never sees validate.yaml):
```
Subagent 4 (Blind Validator):
├─ Applies final prompt to validate_questions.yaml
├─ Returns predictions file

Subagent 5 (Final Scorer):
├─ Scores against validate.yaml (answer sheet)
├─ Returns: "X% accuracy, errors on verses: Y, Z"
└─ Main agent sees percentage only

Success Criteria:
├─ ≥95% accuracy
├─ Main agent NEVER saw answer sheets
└─ Can explain methodology without mentioning TBTA extraction
```

---

## Cheating Detection Checklist

**Before finalizing ANY feature, ALL agents answer**:

### ❌ RED FLAGS (If ANY "yes" → Feature is INVALID, must archive)

- [ ] Did you look at TBTA YAML field values during prompt development?
- [ ] Did you extract answers from TBTA character positions?
- [ ] Did you use TBTA encoding as your prediction method?
- [ ] Did you see answer sheets before locking predictions?
- [ ] Did you read test.yaml or validate.yaml during development?
- [ ] Does your "algorithm" just copy TBTA fields?

### ✅ REQUIRED (ALL must be "yes" to proceed)

- [ ] Did you develop prompts from verse text + translations only?
- [ ] Did you use blind subagents for all scoring?
- [ ] Did you lock predictions (git commit) BEFORE checking accuracy?
- [ ] Can your prompt work on verses TBTA has never labeled?
- [ ] Did you NEVER see actual TBTA values during development?
- [ ] Is your final deliverable a PROMPT (not an extraction script)?

### 🧪 THE "UNLABELED VERSE" TEST

**Critical validation**:
> "If I give you a verse from Leviticus (which TBTA has never annotated), can your prompt predict the {feature} value?"

**Valid Response**:
- ✅ YES - I have a prompt that analyzes verse text, context, translations
- ✅ The prompt works on ANY verse, regardless of TBTA coverage
- ✅ I can explain the linguistic/theological patterns without mentioning TBTA extraction

**Invalid Response** (indicates cheating):
- ❌ NO - I need TBTA YAML to extract the value from position X
- ❌ My "algorithm" only works on verses TBTA has already labeled
- ❌ I'm just copying TBTA's existing annotations

---

## Hive Mind Coordination Strategy

### Queen Coordinator Role (Me)

**Responsibilities**:
1. Spawn specialized agents via Claude Code's Task tool
2. Monitor for extraction red flags
3. Enforce blind testing protocol
4. Check cheating detection checklist before accepting work
5. Verify agents developed PROMPTS, not extraction scripts
6. Confirm "unlabeled verse test" passes
7. Coordinate arbitrary/non-arbitrary analysis

**Authority**:
- Immediate archival of any work showing extraction patterns
- Zero tolerance for answer sheet contamination
- Require re-work if cheating detected

### Worker Agents (Spawned via Task Tool)

**Agent 1: Blind Data Extractor**
- Creates answer sheets (train/test/validate.yaml)
- Creates question sheets (train/test/validate_questions.yaml)
- Returns ONLY question sheet paths
- NEVER reveals answer values to main agents

**Agent 2: Theological Analyzer**
- Analyzes arbitrary vs non-arbitrary contexts
- Creates ARBITRARITY-CLASSIFICATION.md
- Identifies affected doctrines
- Documents cultural sensitivities
- Works from verse text + theological knowledge ONLY

**Agent 3: Linguistic Researcher**
- Identifies encoding languages for feature
- Analyzes translation patterns
- Discovers semantic patterns
- Creates initial prompt drafts
- Works from question sheets ONLY

**Agent 4: Blind Predictor**
- Applies prompts to question sheets
- Generates predictions
- NEVER sees answer sheets
- Returns prediction files only

**Agent 5: Blind Scorer**
- Compares predictions to answer sheets
- Calculates accuracy percentage
- Returns ONLY accuracy % and error verse refs
- NEVER reveals actual values

**Agent 6: Peer Reviewer (Theological)**
- Enhanced review for non-arbitrary features
- 9 additional theological checks
- Verifies no false teaching enabled
- Tests Trinity, divine speech, doctrinal contexts

### Coordination Protocol

**For each feature in Phase 1A**:

```
Step 1: Queen spawns agents in parallel (Claude Code Task tool)
├─ Blind Data Extractor (creates answer/question sheets)
├─ Theological Analyzer (arbitrarity classification)
└─ Linguistic Researcher (begins pattern analysis)

Step 2: Sequential blind development
├─ Main agents receive question sheets only
├─ Develop prompts from translations/patterns
├─ Lock predictions via git commit
├─ Blind Predictor applies prompt
├─ Blind Scorer returns accuracy only
└─ Iterate until ≥95%

Step 3: Non-arbitrary handling (if applicable)
├─ Theological Analyzer creates THEOLOGICAL-ANALYSIS.md
├─ Multi-answer prompt implementation
├─ Enhanced theological peer review
└─ Verify all 9 arbitrarity checklist items

Step 4: Final validation
├─ Blind validation scoring
├─ Cheating detection checklist
├─ "Unlabeled verse test"
├─ Queen approval
└─ Production ready or return to Stage 5
```

---

## Success Criteria

### Per Feature

**Minimum Requirements**:
1. ✅ Prompt developed from verse text + translations (NOT TBTA extraction)
2. ✅ Blind testing protocol followed throughout
3. ✅ All predictions locked before seeing answers
4. ✅ Validate accuracy ≥95%
5. ✅ Cheating detection checklist passes (all red flags = NO)
6. ✅ "Unlabeled verse test" passes
7. ✅ Arbitrary/non-arbitrary analysis complete (if applicable)
8. ✅ Multi-answer output for non-arbitrary contexts (if applicable)
9. ✅ No false teaching enabled

**Deliverable**:
- A PROMPT that works on ANY verse (labeled or unlabeled)
- NOT an extraction script that reads TBTA YAML

### Phase 1A Success

**Criteria**:
- All 3 features (polarity, person-system, number-system) meet per-feature criteria
- No extraction cheating detected
- Methodology validated and reusable for remaining 69 features
- Arbitrary/non-arbitrary framework demonstrated on real features

---

## Risk Mitigation

### Known Risks

**Risk 1: Extraction Temptation**
- **Likelihood**: Medium (happened 3 times before)
- **Mitigation**: Cheating detection checklist, "unlabeled verse test", queen monitoring
- **Detection**: Red flag phrases, git history review, methodology explanation test

**Risk 2: Answer Sheet Contamination**
- **Likelihood**: Medium (easy to accidentally read)
- **Mitigation**: Strict file permissions, subagent isolation, explicit forbidden file list
- **Detection**: Git history, agent logs, final deliverable inspection

**Risk 3: Oversimplification of Arbitrary/Non-Arbitrary**
- **Likelihood**: Low-Medium
- **Mitigation**: Theological analyzer agent, 9-point enhanced review, test cases
- **Detection**: Peer review, Trinity context testing, denominational review

**Risk 4: Low Accuracy Due to Blind Testing**
- **Likelihood**: Medium (blind testing is harder)
- **Mitigation**: Translation validation (primary method), iterative refinement
- **Acceptance**: 95% threshold may take 3-5 iterations vs instant 100% from extraction

---

## Timeline Estimate

### Polarity (Mostly Arbitrary)
- Stage 1-3: 2 hours (research, arbitrarity classification)
- Stage 4: 1 hour (test set generation)
- Stage 5: 4-6 hours (prompt development, iterations)
- Stage 6: 1-2 hours (peer review)
- **Total**: 8-11 hours

### Person System (Mixed - 40% Non-Arbitrary)
- Stage 1-3: 3-4 hours (research, theological analysis)
- Stage 4: 1-2 hours (test set with non-arbitrary stratification)
- Stage 5: 6-8 hours (multi-answer prompts, ramification analysis)
- Stage 6: 2-3 hours (enhanced theological review)
- **Total**: 12-17 hours

### Number System (Mixed - 15% Non-Arbitrary)
- Stage 1-3: 3-4 hours (research, Trinity analysis)
- Stage 4: 1-2 hours (test set with theological stratification)
- Stage 5: 6-8 hours (trial/dual/plural prompts, Trinity contexts)
- Stage 6: 2-3 hours (enhanced theological review)
- **Total**: 12-17 hours

**Phase 1A Total**: 32-45 hours
**vs. Invalid Extraction Attempt**: 4 hours (but 100% wasted)

**Value Proposition**: 32-45 hours of VALID work vs infinite re-work from cheating

---

## Execution Checklist

**Pre-Launch** (Queen):
- [ ] All agents briefed on CORRECTED-INSTRUCTIONS.md
- [ ] Cheating detection checklist distributed
- [ ] Blind testing workflow understood
- [ ] "Unlabeled verse test" explained
- [ ] Arbitrary/non-arbitrary framework reviewed
- [ ] Red flag phrases memorized
- [ ] Zero tolerance policy communicated

**During Development** (Per Feature):
- [ ] Blind Data Extractor creates answer/question sheets
- [ ] Main agents receive ONLY question sheets
- [ ] Theological analysis complete (arbitrarity classification)
- [ ] Prompts developed from translations/patterns ONLY
- [ ] Predictions locked before scoring
- [ ] Blind scoring returns accuracy only
- [ ] Iterations continue until ≥95%
- [ ] Multi-answer output implemented (if non-arbitrary)
- [ ] Enhanced theological review (if non-arbitrary)

**Post-Development** (Per Feature):
- [ ] Cheating detection checklist completed
- [ ] All red flags = NO
- [ ] All requirements = YES
- [ ] "Unlabeled verse test" passes
- [ ] Validate accuracy ≥95%
- [ ] No extraction patterns in git history
- [ ] Final deliverable is PROMPT (not script)
- [ ] Queen approval granted

**Phase 1A Complete**:
- [ ] All 3 features production-ready
- [ ] No cheating detected
- [ ] Methodology proven
- [ ] Ready to scale to remaining 69 features

---

## Next Steps

### Immediate (Ready Now)

1. **Queen reads** (me):
   - ✅ CORRECTED-INSTRUCTIONS.md
   - ✅ STAGES-INTEGRATION-COMPLETE.md
   - ✅ This restart plan

2. **Spawn agents** (Claude Code Task tool):
   - Blind Data Extractor (1 agent)
   - Theological Analyzer (1 agent per feature)
   - Linguistic Researcher (1 agent per feature)
   - Blind Predictor (1 agent)
   - Blind Scorer (1 agent)
   - Peer Reviewers (4 agents per feature)

3. **Begin with Polarity** (simplest, mostly arbitrary):
   - Validate methodology on straightforward case
   - Build confidence in blind testing
   - Establish workflow before complex features

4. **Then Person System** (moderate non-arbitrary):
   - Apply arbitrary/non-arbitrary framework
   - Test multi-answer output
   - Validate theological analysis process

5. **Finally Number System** (Trinity contexts):
   - Most theologically sensitive
   - Complete non-arbitrary demonstration
   - Validate enhanced peer review

### Success Metrics

- **Quality**: ≥95% validate accuracy, zero cheating
- **Theological**: No false teaching enabled, denominational flexibility respected
- **Methodology**: Reusable for remaining 69 features
- **Efficiency**: 32-45 hours for 3 production-ready features

---

**Status**: ✅ Ready to Execute
**Decision Point**: Begin Phase 1A restart with Polarity feature?
**Confidence**: High - all methodology corrected, framework integrated, detection mechanisms in place
