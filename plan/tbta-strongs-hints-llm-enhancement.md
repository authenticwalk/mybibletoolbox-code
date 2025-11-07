# Strong's Hints as LLM Context Enhancement

## Context: Existing LLM-Based TBTA Prediction

**Current approach (from plan/tbta-rebuild-with-llm/):**
- LLM analyzes verse with source text, translations, theological reasoning
- Achieves 80-100% accuracy on tested features (Genesis 1)
- Uses prompt engineering with decision trees, patterns, examples
- **Problem:** Cannot cover all edge cases in prompt (token limits, complexity)

**Proposed enhancement:**
- Add Strong's hints as additional context when predicting features
- LLM receives: source text + translations + theological context + **Strong's hints**

---

## Pros: How Strong's Hints Enhance LLM Predictions

### 1. Concrete Cross-Linguistic Evidence ★★★★★

**Current limitation:**
LLM prompt says: "Check if language uses inclusive/exclusive distinction"
- Too vague - which languages? what patterns?
- LLM might hallucinate patterns
- No grounded evidence

**With Strong's hints:**
```yaml
# Loaded with verse context
Strong's G2249 (we):
  clusivity_patterns:
    - context: "divine speech"
      evidence: "5/5 Austronesian languages use exclusive form"
      languages: ["tgl: kami", "msa: kami", "fij: keirau"]
      confidence: 0.98
```

**LLM sees:**
- Specific languages to check (Tagalog, Malay, Fijian)
- Specific words that indicate pattern ("kami" = exclusive)
- Evidence strength (5/5 agreement)
- Can validate pattern in loaded translations

**Benefit:** LLM has grounded facts, not vague instructions

---

### 2. Edge Case Coverage ★★★★★

**Current limitation:**
Prompt engineering cannot cover all edge cases:
- Trial number (rare, only ~30 instances in Bible)
- 4th person/obviative (very rare)
- Specific proximity distinctions (9-way systems)

**With Strong's hints:**
```yaml
Strong's G846 (they):
  number_edge_cases:
    - verse: "GEN.1.26"
      pattern: "Hawaiian lākou = trial (exactly 3)"
      note: "Trinity reference - rare trial number"
      confidence: 0.95
```

**Benefit:** Edge cases documented once, available for all verses with that word

---

### 3. Reduces Hallucination ★★★★☆

**Current risk:**
LLM might confidently predict patterns based on compressed training data:
- "Spanish probably uses demonstrative X here" (not grounded)
- "Tagalog likely distinguishes this with..." (guessing)

**With Strong's hints:**
```yaml
Strong's G3778 (this):
  proximity_patterns:
    - spanish: "ese" (near listener) in 87% of contexts
    - japanese: "それ" (sore) in 82% of contexts
    - NOT guessing - based on actual translations
```

**Benefit:** LLM reasoning anchored in real translation data, not speculation

---

### 4. Multi-Word Context Integration ★★★★☆

**Example verse:** "Let us make man in our image"
- Multiple words with hints: "us" (G2249), "our" (G2257), "man" (G444)

**LLM can synthesize:**
```
Hints for "us" (G2249): exclusive pattern in divine speech
Hints for "our" (G2257): trial number pattern in Trinity refs
Theological context: Trinity addressing Trinity

SYNTHESIS: Both hints + theology agree → high confidence
  - Person: First Exclusive (Trinity members only)
  - Number: Trial (exactly 3 persons)
```

**Benefit:** Multiple hints provide corroboration, increase confidence

---

### 5. Confidence Scoring ★★★★★

**With hints, LLM can calculate:**

| Scenario | Confidence | Reasoning |
|----------|------------|-----------|
| Hints + theology + context all agree | 0.95-0.98 | Strong consensus |
| Hints agree, context neutral | 0.85-0.90 | Hints reliable |
| Hints split, context unclear | 0.60-0.75 | Flag for human review |
| Hints disagree with context | 0.40-0.60 | Context overrides hints |

**Benefit:** Transparent confidence scores based on evidence convergence

---

### 6. Efficiency: Shorter Prompts ★★★★☆

**Without hints:**
- Must include extensive examples in prompt
- Token-heavy: "When translating to languages with clusivity... [500 words of examples]"

**With hints:**
- Prompt: "Check Strong's hints for cross-linguistic patterns"
- Hints loaded separately: 50-100 tokens per word
- **Net benefit:** Shorter prompts, more context capacity for verse analysis

---

### 7. Self-Improving System ★★★★★

**Workflow:**
```
1. LLM predicts feature using hints
2. Validation: compare with gold standard
3. Feedback loop:
   - If LLM correct but hints weak → strengthen hints
   - If LLM wrong following hints → refine hint conditions
   - If LLM correct overriding hints → document context override pattern
```

**Benefit:** System improves over time, hints refined based on performance

---

## Cons: How Strong's Hints Could Reduce Accuracy

### 1. Context Override Failures ★★★★★ (CRITICAL)

**Problem:** Hints based on typical patterns may not apply to specific verse

**Example:**
```yaml
# Strong's G2249 (we)
hint: "In epistles, apostle to church = exclusive (90% of cases)"

# But in specific verse:
EPH 4:4-6: "There is one body... one hope... one Lord..."
Context: Church unity - apostle INCLUDING readers in "we all"
Correct: INCLUSIVE (context overrides hint)
```

**Risk:** LLM might follow hint blindly
- "Hint says exclusive in epistles → I'll predict exclusive"
- Ignores theological context (unity passage)
- **Result:** Wrong prediction

**Mitigation strategies:**
1. Prompt emphasizes: "Hints are patterns, context overrides"
2. Require LLM to justify when following vs overriding hints
3. Flag low-confidence predictions for human review
4. Multi-pass: predict without hints, then with hints, compare

---

### 2. Conflicting Hints from Multiple Words ★★★★☆

**Problem:** Verse has multiple words with different hint patterns

**Example:**
```yaml
# Verse has both pronouns:
"We know that we all possess knowledge" (1CO 8:1)

Strong's G1492 (know): hint: exclusive (apostolic knowledge)
Strong's G3956 (all): hint: inclusive (everyone included)

CONFLICT: "we" exclusive or inclusive?
```

**Risk:** LLM confused by contradictory signals
- Might default to first hint
- Might try to average (nonsensical for binary features)
- Might freeze (unable to decide)

**Mitigation strategies:**
1. Hint priority rules: context > semantics > frequency
2. LLM trained to recognize conflicts and analyze why
3. Require explicit reasoning: "Hint X suggests A, but hint Y suggests B, I choose B because..."

---

### 3. Overreliance on Hints (Mental Laziness) ★★★★☆

**Problem:** LLM stops doing deep theological reasoning

**Without hints:**
```
LLM reasoning:
"Genesis 1:26 - God says 'Let us make man'
- Who is 'us'? Analyzing theology...
- Trinity doctrine: Father, Son, Spirit
- Addressing each other, not creation
- Therefore: First Exclusive, Trial number"
```

**With hints (if poorly prompted):**
```
LLM reasoning:
"Genesis 1:26 - 'us' = G2249
- Hint says: exclusive in divine speech
- Therefore: First Exclusive"
[Skips theological reasoning, misses Trial number]
```

**Risk:** Shallower analysis, missed insights
- Hints provide answer, LLM stops thinking
- Misses secondary features (Trial number)
- Reduces to hint lookup, not AI reasoning

**Mitigation strategies:**
1. Prompt structure: "First analyze WITHOUT hints, then check hints for validation"
2. Require theological reasoning regardless of hints
3. Score predictions on reasoning quality, not just correctness
4. Use hints as validation, not as primary input

---

### 4. Wrong Hints Propagate Errors ★★★☆☆

**Problem:** If hint is wrong (bad pattern extraction), all verses using that word affected

**Example:**
```yaml
# Hypothetical wrong hint:
Strong's G2249 (we):
  hint: "In Genesis, always exclusive" (WRONG - Gen 1:26 might be inclusive in some views)

Result: LLM predicts exclusive for ALL Genesis "we" instances
  - Compounds error across multiple verses
  - Harder to detect (systematic bias)
```

**Risk:** Single wrong hint → multiple wrong predictions
- Manual verse-by-verse: errors are independent
- Hints: errors are correlated (same wrong hint applied multiple times)

**Mitigation strategies:**
1. Confidence thresholds: don't use hints <0.70 confidence
2. Hint validation: test hints on held-out verses before deployment
3. Monitor prediction patterns: if 10 verses with same word all predicted same way, flag for review
4. Allow LLM to flag suspicious hints

---

### 5. Increased Prompt Complexity ★★★☆☆

**Problem:** Adding hints makes prompt longer, reasoning more complex

**Token cost:**
```
Base prompt: 2,000 tokens
+ Verse context: 500 tokens
+ 5 Strong's words × 100 tokens/word: 500 tokens
+ Reasoning instructions for hints: 300 tokens
Total: 3,300 tokens (65% increase)
```

**Risk:**
- Longer prompts = higher cost per prediction
- More for LLM to reason about = more opportunities for confusion
- Prompt engineering harder (must balance hints vs context)

**Mitigation:**
1. Only load hints for high-value features (not all 59)
2. Summary hints (100 tokens) vs full details (500 tokens)
3. Separate hint loading from main prediction (two-stage)

---

### 6. False Confidence from Hint Agreement ★★☆☆☆

**Problem:** LLM sees hint, assumes it's authoritative

**Example:**
```yaml
Strong's hint: "90% confidence - exclusive"
LLM: "Hint has 0.90 confidence, I'll trust it"

Reality: That 90% is from 9/10 contexts, but THIS verse is the 10th (exception case)
```

**Risk:** High-confidence hints override correct reasoning
- LLM treats 0.90 as "very reliable"
- Doesn't realize it might be in the 10% exception
- False sense of certainty

**Mitigation:**
1. Prompt clarifies: "90% means 10% are exceptions - could THIS be one?"
2. Require LLM to justify why this verse fits the 90% pattern
3. Never auto-accept hints, always reason through context

---

### 7. Context Pollution ★★☆☆☆

**Problem:** Hints from different contexts bleed into current verse

**Example:**
```yaml
Strong's G3004 (λέγω - say):
  time_hints:
    - narrative: "historic past (80%)"
    - dialogue: "present (60%)"
    - prophecy: "prophetic future (70%)"

Current verse: Epistle (different genre!)
LLM: "Uh, which hint applies? None match 'epistle'... I'll guess 'present'?"
```

**Risk:** Hints from wrong context mislead LLM
- Hints based on narrative applied to epistle
- LLM tries to force-fit hint to current context

**Mitigation:**
1. Context-conditional hints: only show hints matching current genre
2. Explicit "N/A" when hint doesn't apply
3. Teach LLM to recognize when hints are irrelevant

---

## Optimal Integration Strategy

### Approach 1: Hints as Validation (Recommended) ★★★★★

```
Workflow:
1. LLM analyzes verse WITHOUT hints
2. Generates initial prediction with reasoning
3. THEN loads Strong's hints
4. Compares prediction with hints
5. If agree: high confidence (0.95+)
6. If disagree: explain difference, choose better reasoning

Result: Hints don't drive prediction, they validate it
```

**Pros:**
- ✅ Preserves LLM's deep reasoning
- ✅ Hints catch errors ("Wait, you predicted X but all evidence says Y")
- ✅ Confidence scores meaningful (convergence = high confidence)
- ✅ Context overrides still work (LLM can explain why)

**Cons:**
- ❌ Two-pass system (more complex)
- ❌ Slightly slower (predict, then validate)

---

### Approach 2: Hints as Context (Alternative) ★★★☆☆

```
Workflow:
1. Load verse + Strong's hints together
2. LLM sees both simultaneously
3. Reasons through using all available evidence
4. Weights hints vs context vs theology

Result: Hints are one input among many
```

**Pros:**
- ✅ Single-pass (simpler)
- ✅ LLM can integrate hints naturally
- ✅ Efficient (one prediction)

**Cons:**
- ❌ Risk of overreliance on hints
- ❌ Harder to debug (can't see prediction without hints)
- ❌ Context override patterns less clear

---

### Approach 3: Hybrid - Selective Hint Loading ★★★★☆

```
Workflow:
1. LLM predicts WITHOUT hints
2. Self-scores confidence
3. If low confidence (<0.75): load relevant hints
4. Re-predict with hints as additional evidence
5. Compare before/after, choose better reasoning

Result: Hints only when needed
```

**Pros:**
- ✅ Efficient (hints only for uncertain cases)
- ✅ Preserves reasoning for clear cases
- ✅ Hints act as "phone a friend" when stuck

**Cons:**
- ❌ Most complex implementation
- ❌ Requires confidence calibration

---

## Feature-by-Feature Analysis

### Features Where Hints STRONGLY Help:

| Feature | Hint Value | Why Helps | Risk Level |
|---------|------------|-----------|------------|
| **Number System** | ★★★★★ | Clear patterns (dual/trial), LLM might not know all languages | Low (patterns stable) |
| **Person/Clusivity** | ★★★★★ | Concrete evidence (kami/tayo), validates theological reasoning | Low-Medium (context can override) |
| **Proximity** | ★★★★★ | Clear demonstrative mappings (これ/それ/あれ) | Low (patterns stable) |
| **Lexical Sense** | ★★★★★ | Disambiguation crucial, hints prevent hallucination | Low (senses distinct) |

### Features Where Hints MODERATELY Help:

| Feature | Hint Value | Why Helps | Risk Level |
|---------|------------|-----------|------------|
| **Surface Realization** | ★★★☆☆ | Pro-drop patterns useful | Medium (context matters) |
| **Aspect (aktionsart)** | ★★★☆☆ | Lexical aspect baseline | Medium (realized aspect varies) |
| **Mood** | ★★★☆☆ | Modal signals useful | Medium (context determines final mood) |

### Features Where Hints COULD HURT:

| Feature | Hint Value | Why Risky | Risk Level |
|---------|------------|-----------|------------|
| **Time Granularity** | ★★☆☆☆ | Context-dominant, genre matters more | **High** (hints misleading) |
| **Participant Tracking** | ★☆☆☆☆ | Discourse-level, word hints irrelevant | **High** (wrong feature type) |
| **Speaker Demographics** | ★☆☆☆☆ | Verse-specific, no word-level patterns | **High** (no value, confuses) |

**Recommendation:** Only provide hints for ★★★★+ features, omit hints for ★★☆☆☆ and below

---

## Prompt Engineering Considerations

### Option A: Explicit Hint Priority (Clear but Verbose)

```
You are predicting TBTA features for this verse.

PRIORITY ORDER:
1. Theological context (highest priority)
2. Discourse context (narrative flow, genre)
3. Strong's hints (cross-linguistic patterns)
4. Source morphology (Greek/Hebrew grammar)

If Strong's hints conflict with context, EXPLAIN your reasoning.
If context is ambiguous and hints are strong (>0.85), follow hints.
If both are unclear, flag for human review.
```

**Pros:** Very clear, explicit prioritization
**Cons:** Verbose, adds 100+ tokens

---

### Option B: Implicit Integration (Concise but Riskier)

```
Analyze this verse considering:
- Source text and translations
- Theological/discourse context
- Strong's hints (loaded below)

Predict TBTA features with confidence scores.
```

**Pros:** Concise, trusts LLM to integrate well
**Cons:** LLM might weight hints wrong

---

### Option C: Two-Stage Validation (Best Accuracy)

```
STAGE 1 (No Hints):
Analyze verse and predict features with reasoning.

STAGE 2 (With Hints):
Now review Strong's hints below.
Compare your prediction with hints.
- If agree: boost confidence
- If disagree: explain which reasoning is stronger
Final prediction with confidence score.
```

**Pros:** Best accuracy, transparent reasoning
**Cons:** More complex, two LLM calls

---

## Quantitative Impact Estimates

### Accuracy Changes (Estimated)

**For lexical features (Number, Person, Proximity, Lexical Sense):**

| Scenario | Without Hints | With Hints (Well-Integrated) | With Hints (Poorly Integrated) |
|----------|---------------|------------------------------|--------------------------------|
| Clear context cases | 95% | 97% (+2%) | 93% (-2%) |
| Ambiguous context | 75% | 88% (+13%) | 70% (-5%) |
| Edge cases (trial, 4th person) | 60% | 85% (+25%) | 55% (-5%) |
| **Overall average** | **85%** | **92% (+7%)** | **80% (-5%)** |

**Key insight:** Hints help most on ambiguous/edge cases IF integrated well

---

**For discourse features (Participant Tracking, Salience Band):**

| Scenario | Without Hints | With Hints | Impact |
|----------|---------------|------------|--------|
| All cases | 90% | 88% (-2%) | **Slight harm** (hints irrelevant, add noise) |

**Key insight:** Don't load hints for discourse features

---

### Confidence Scoring Impact

**With hints, confidence calibration improves:**

| Prediction Confidence | Actual Accuracy (Without Hints) | Actual Accuracy (With Hints) |
|----------------------|----------------------------------|------------------------------|
| 0.95-1.00 | 92% (overconfident) | 96% (well-calibrated) |
| 0.85-0.94 | 85% (well-calibrated) | 88% (better) |
| 0.70-0.84 | 72% (well-calibrated) | 78% (better) |
| <0.70 | 58% (under-confident) | 65% (better) |

**Benefit:** Hints provide external validation, improving confidence accuracy

---

## Recommendations

### DO Use Strong's Hints For:

1. **High-value lexical features** (Number, Person, Proximity, Lexical Sense)
2. **High-frequency words** (top 300 words, not all 8,000)
3. **Validation workflow** (predict first, then check hints)
4. **Edge case handling** (trial number, 4th person, rare proximities)
5. **Confidence scoring** (hint agreement → boost confidence)

### DON'T Use Strong's Hints For:

1. **Discourse features** (Participant Tracking, Salience Band, Speaker Demographics)
2. **Context-dominant features** (Time Granularity, Illocutionary Force)
3. **Low-frequency words** (<50 occurrences, insufficient patterns)
4. **Features already in Macula** (redundant)

### Prompt Design Best Practices:

1. ✅ **Two-stage validation** (predict without, validate with hints)
2. ✅ **Explicit priority rules** (context > hints > morphology)
3. ✅ **Confidence thresholds** (only use hints >0.70 confidence)
4. ✅ **Require justification** ("I followed/overrode hint because...")
5. ✅ **Flag conflicts** (hints disagree with context → human review)

### Implementation Phasing:

**Phase 1: Lexical features only (2 months)**
- Number, Person, Proximity for top 50 pronouns
- Test impact on existing LLM predictions
- Measure accuracy change (+7% expected)

**Phase 2: Validate benefits (1 month)**
- A/B test: LLM with vs without hints
- Measure: accuracy, confidence calibration, false confidence rate
- Decision: proceed if +5% accuracy improvement

**Phase 3: Scale if beneficial (3 months)**
- Expand to top 300 words, 11 lexical features
- Integrate into production LLM workflow

---

## Conclusion

### Strong's Hints as LLM Enhancement: Net Positive IF Done Right

**Expected Impact:**
- **Accuracy:** +7% on lexical features (85% → 92%)
- **Edge cases:** +25% on rare phenomena (trial number, 4th person)
- **Confidence:** Better calibration (convergent evidence)
- **Efficiency:** Shorter prompts (hints replace examples)

**Critical Success Factors:**
1. Use validation workflow (predict first, hints second)
2. Context override allowed (hints are patterns, not rules)
3. Selective loading (only high-value features and words)
4. Quality control (validate hints before using)
5. Monitor for hint-driven errors (systematic biases)

**Risk Mitigation:**
- Never auto-accept hints (<0.85 confidence)
- Require explicit reasoning when following/overriding
- Two-stage prediction catches hint-context conflicts
- Flag low-agreement cases for human review

**Bottom Line:**
Strong's hints are **highly valuable context enhancement** for LLM-based TBTA prediction, especially for lexical features and edge cases. Key is to use them as validation/corroboration, not as primary driver of predictions.

---

**Next Step:** Proof of concept with 3 pronouns (G846, G2249, G3778) on 20 Genesis verses, comparing:
1. LLM predictions without hints (baseline)
2. LLM predictions with hints (validation mode)
3. Measure: accuracy change, confidence calibration, override rate
