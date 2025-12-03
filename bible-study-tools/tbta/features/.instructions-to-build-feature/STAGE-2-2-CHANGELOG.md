# Stage 2.2 Baseline Analysis - Change Log

**Started**: 2025-11-29
**Goal**: Test and tune instructions across diverse features

---

## Baseline Results Summary

### Mood (10 values, complex semantic distinctions)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Haiku | 41.1% |
| A: No metadata | Sonnet | 48.0% |
| B: With metadata | Sonnet | 50.0% |
| D: Prompted (summarized) | Sonnet | 59.0% |
| D: Prompted (EXACT) | Sonnet | **62.0%** |

**Key finding**: EXACT prompt wording matters (+3%)

### Polarity (4 values, simpler distinction)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Haiku | 51.0% |
| A: No metadata | Sonnet | 73.3% |
| A: No metadata | **Opus** | **85.0%** |
| A: No metadata + hints | Sonnet | 72.3% |

**Key finding**: Opus significantly better for simpler features; hints didn't help Sonnet

---

## Changes Made

### Change 1: Fixed script paths (2025-11-29)
- **Before**: `/workspace/src/tools/predict/strip_labels.py`
- **After**: `src/tools/predict/strip_labels.py`
- **Why**: `/workspace` is machine-specific; relative paths work everywhere

### Change 2: Restored EXACT Test D prompt (2025-11-29)
- **Before**: Summarized version missing INCENTIVE, CHALLENGE, QUALITY CONTROL
- **After**: Full original with all psychological framing
- **Why**: EXACT wording gave +3% on mood (59% → 62%)

### Change 3: Added opus to Test A (2025-11-29)
- **Before**: Only haiku, sonnet
- **After**: haiku, sonnet, opus
- **Why**: Opus got 85% on polarity vs 73% for sonnet - significant difference

### Change 4: Added hints variation (2025-11-29)
- **Before**: Single test per model
- **After**: Test with and without hints
- **Why**: User requested; results show hints don't always help (polarity: -1%)

### Change 5: Updated accuracy table format (2025-11-29)
- **Before**: Test name only, model unclear
- **After**: Separate Test and Model columns
- **Why**: Clarity on which model achieved which result

---

## Pending Tests

Features to test for diversity:
- [x] aspect (grammatical aspect - perfective/imperfective) ✅ TESTED
- [x] degree (comparative/superlative) ✅ TESTED
- [ ] discourse-genre (narrative/poetry/prophecy) - data too imbalanced (99.9% one class)
- [x] illocutionary-force (declarative/interrogative/imperative) ✅ TESTED
- [x] participant-tracking (first mention/routine/exiting) ✅ TESTED
- [ ] proximity-system (near/far deixis)

---

## Hypotheses to Test

1. **Model selection**: Opus better for simpler features, Sonnet better for complex?
2. **Hints value**: May help complex features but not simple ones?
3. **Prompt engineering**: More valuable for harder distinctions?
4. **Metadata value**: Strong's numbers help linguistic features?

---

## Running Log

### 2025-11-29: Additional Feature Testing

#### Degree (9 values, semantic comparison)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Haiku | 46.8% |
| A: No metadata | **Sonnet** | **55.0%** |
| A: No metadata | Opus | 52.0% |

**Finding**: Sonnet beats Opus! Haiku predicted 97% "No Degree" when GT has 47%.

GT distribution: No Degree 47, Intensified 28, Comparative 8, Superlative 7, Extremely Intensified 7

#### Participant-Tracking (6 values, discourse feature)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Sonnet | 25.5% |
| A: No metadata | Opus | 34.0% |

**Finding**: Very hard feature. Opus over-predicted "Frame Inferable" (51 vs 27 GT).

GT distribution: Frame Inferable 27, First Mention 27, Routine 23, Generic 20, Interrogative 3

#### Illocutionary-Force (7 values, sentence-level speech acts)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Haiku | 19.7% |
| A: No metadata | Sonnet | 48.1% |
| A: No metadata | **Opus** | **70.0%** |

**Finding**: Opus DOMINATES (70%)! Sentence-level classification works well.

Key errors: "Yes-No Interrogative" confused with "Content Interrogative", "Imperative" confused with "Imperative with emphasized Agent"

GT distribution: Imperative with emphasized Agent 14, Yes-No Interrogative 12, Jussive 12, Declarative 12, Suggestive 'let's' 11, Imperative 10, Content Interrogative 9

#### Aspect (9 values, grammatical aspect)
| Test | Model | Accuracy |
|------|-------|----------|
| A: No metadata | Haiku | 14.6% |
| A: No metadata | Sonnet | 25.0% |
| A: No metadata | **Opus** | **33.0%** |

**Finding**: Very hard feature. Models over-predict "Completive", under-predict "Unmarked".

Key errors: "Inceptive" often missed, "Unmarked" under-predicted, "Continuative" confused with "Imperfective"

GT distribution: Unmarked 31, Imperfective 18, Inceptive 17, Cessative 9, Continuative 9, Routinely 7, Gnomic 4, Completive 3, Habitual 2

---

## Pattern Analysis

### Model Performance by Feature Complexity

| Feature | Values | Best Model | Best Accuracy | Feature Type |
|---------|--------|------------|---------------|--------------|
| Polarity | 4 | Opus | 85% | Binary |
| **Illocutionary-Force** | 7 | **Opus** | **70%** | **Sentence-level** |
| Mood | 10 | Sonnet (prompted) | 62% | Semantic |
| Degree | 9 | Sonnet | 55% | Semantic |
| Participant-Tracking | 6 | Opus | 34% | Discourse |
| Aspect | 9 | Opus | 33% | Grammatical |

### Observations

1. **Polarity is easiest** (85% opus) - binary-like distinction (affirm/negate)
2. **Illocutionary-Force is second easiest** (70% opus) - sentence-level classification, well-defined categories
3. **Aspect & Participant-Tracking are hardest** (33-34%) - context-dependent, nuanced distinctions
4. **Opus consistently beats other models** (except Degree where Sonnet wins)
5. **Prompting helps complex semantic features** (Mood: +14% from baseline)
6. **NEW**: Sentence-level features (Illocutionary-Force) are easier than word-level features (Aspect)

### Hypothesis Refinement

| Feature Type | Recommended Approach | Evidence |
|--------------|---------------------|----------|
| Binary/Simple (Polarity) | Opus, no prompting needed | 85% |
| Sentence-level (Illocutionary-Force) | Opus, no prompting needed | 70% |
| Semantic (Degree, Mood) | Sonnet with prompting | +14% for Mood |
| Grammatical (Aspect) | Opus WITHOUT prompting | Prompting hurt -7% |
| Discourse (Participant) | Needs multi-verse context | 34% insufficient |

---

## Recommendations for Instructions

1. **Add model selection guidance**:
   - Simple/sentence-level features → Try Opus first (85%, 70%)
   - Semantic features → Use Sonnet with prompting
   - Grammatical features → May need specialized hints or prompting

2. **Flag discourse features**:
   - Participant-tracking, discourse-genre may need different approach
   - Single-verse context insufficient

3. **Keep hints optional**:
   - Didn't help Polarity (Sonnet: -1%)
   - May help harder features like Aspect - needs more testing

4. **NEW: Feature type predicts difficulty**:
   - Sentence-level > Word-level classification
   - Binary distinctions > Multi-class distinctions
   - Context-independent > Context-dependent

---

## Learnings for Instruction Improvement

### What Works
- **Opus for simpler features**: Consistently outperforms other models
- **Direct LLM prediction**: Models have significant internal knowledge
- **Clear label definitions**: Well-defined categories improve accuracy

### What Doesn't Work
- **One-size-fits-all**: Different features need different approaches
- **Single-verse context**: Insufficient for discourse features (Participant-Tracking: 34%)
- **Hints for simple features**: May actually hurt performance (-1% for Polarity)

### What Needs Testing
- ~~**Prompting for Aspect**: Complex grammatical feature may benefit from Test D approach~~ TESTED - **HURT** performance (26% vs 33%)
- **Multi-verse context**: For Participant-Tracking and similar discourse features
- **Metadata (Strong's numbers)**: May help grammatical features like Aspect

### 2025-11-29: Prompted Aspect Test Results

| Test | Model | Accuracy | Change |
|------|-------|----------|--------|
| A: No metadata | Opus | 33.0% | baseline |
| D: Prompted + metadata | Sonnet | 26.0% | **-7% worse** |
| D: Prompted + metadata | Opus | 26.0% | **-7% worse** |

**Finding**: Prompting HURT aspect performance! Unlike Mood (+14%), Aspect got worse with prompting.

**Analysis**:
- Models over-predicted "Completive" and under-predicted "Unmarked" with prompting
- The prompt's emphasis on Hebrew qatal/Greek aorist mapping may have caused over-classification
- "Unmarked" (31% of ground truth) is the hardest category - requires knowing when NOT to mark aspect
- Grammatical features may need a different approach than semantic features

**Key insight**: Prompting helps semantic features (Mood) but hurts grammatical features (Aspect)

---

## 2025-12-01: Data Quality Analysis

### Finding: Some labels may be based on Hebrew/Greek features

When analyzing errors, check if the source language (Hebrew/Greek) actually encodes the feature.

#### Degree Feature - Intensified Labels

Many "Intensified" labels don't have visible English intensifiers (very, exceedingly, etc.).

**Possible explanations:**
1. Labels based on Hebrew/Greek morphology (e.g., Hebrew intensive stems like Piel)
2. Labels based on lexical semantics in source language
3. Some may be labeling errors

**For error analysis**: Check if Hebrew/Greek source actually encodes intensity.

#### Illocutionary-Force - Yes-No vs Content Interrogative

Some "Yes-No Interrogative" labels contain WH-words in English:
- `1SA-020-032` | "Why is he put to death? **what** hath he done?"
- `HAB-002-018` | "**What** profit hath a graven image given"

**For error analysis**: Check Hebrew/Greek - the source language interrogative form determines the label, not English translation.

#### Aspect Feature - Semantic Labels

Labels like "Inceptive" and "Cessative" often lack English markers ("began", "stopped").

**Example of correct subtle label:**
- `JOS-023-001` | Cessative | "fight" → Hebrew הֵנִיחַ (heniach) means "gave rest" implying cessation

**For error analysis**: Check Hebrew/Greek verbal morphology and Aktionsart.

### Key Insight

When models consistently disagree with labels, check the source language:
- If Hebrew/Greek supports the label → model needs improvement
- If Hebrew/Greek doesn't encode the feature → label may be incorrect
