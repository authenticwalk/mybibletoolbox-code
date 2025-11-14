# TBTA Learnings & Methodology

**Purpose**: Transferable patterns discovered from TBTA feature experiments using LLM prompt engineering. All patterns validated through real implementation, not theoretical speculation.

**Source**: Consolidated from Person (100% accuracy), Mood (100% extraction), Aspect (98.1% prediction), and Participant Tracking (90% with context) experiments.

---

## Prompt Engineering Patterns

### 1. Hierarchical Prompting Framework (Most Important)

Use a **prompt hierarchy** instead of flat analysis:

```
Level 1: THEOLOGICAL/SEMANTIC → Resolve 60-70% of cases
Level 2: CAPABILITY/RESTRICTION → Resolve 20% more
Level 3: DISCOURSE FUNCTION → Resolve 10% more
Level 4: GRAMMATICAL CUES → Resolve remaining 5%
Level 5: BASELINE (rarity principle) → Default
```

**Why It Works**: Prioritizes meaning over form, leverages LLM strengths in theological reasoning.

**Template**:
```
Theological Analysis Prompt:

Verse: {reference}
Feature to determine: {feature_name}

Theological Framework Questions:
1. Does this involve a divine prerogative? (creation, judgment, omniscience)
2. Does this describe a salvific experience? (justification, peace with God)
3. Is there an authority structure? (apostolic witness, divine command)
4. Does this express community identity? (unity, worship, shared faith)

Based on theological context, what value is most appropriate?
Confidence: High/Medium/Low
Reasoning: ...
```

**Apply To**: Any feature with ambiguity - Aspect, Mood, Voice, Number, Person.

---

### 2. Capability Analysis as Primary Filter

The question "Can the addressee perform this action?" can resolve most ambiguous cases.

**Template**:
```
Capability Analysis Prompt:

Verse: {reference}
Speaker: {who is speaking}
Addressee: {who is being addressed}
Action/State: {what is described}

CAPABILITY TEST:
1. Identify the specific action or state described
2. Can the addressee perform/participate in this action?

   Questions to ask:
   - Is this within human capability? (walking, speaking, believing)
   - Is this a divine-only capability? (creating, omniscience, forgiveness of sins)
   - Is this role-specific? (apostolic witness, priestly service)
   - Is this a shared experience? (suffering, joy, faith)

3. If NO (addressee cannot participate):
   → EXCLUSIVE (speaker + others, not addressee)

4. If YES (addressee can participate):
   → Continue to next level (identity/group analysis)
```

**Success Rate**: Filtered 60%+ of ambiguous situations in Person experiment.

**Apply To**: Mood (authority check), Aspect (telicity check), Voice (agent capability).

---

### 3. The Rarity Principle (Baseline First)

**Discovery**: 90.7% of verbs are Unmarked (default) in Aspect, only 9.3% marked.

**Core Insight**: TBTA only marks when semantically necessary. Identify the dominant value FIRST, then look for triggers to override.

**WARNING**: Do NOT use rarity principle to guess at unmarked values. Use it to establish baseline confidence and prioritize analysis effort on marked cases.

**Template**:
```
For {verse reference}, predict {feature_name}:

Baseline value: {dominant_value} (accounts for {percentage}% of cases)

Check for special triggers that would override baseline:
- [ ] Theological factor present? (e.g., divine action)
- [ ] Discourse marker present? (e.g., topic shift)
- [ ] Grammatical trigger present? (e.g., specific mood)
- [ ] Semantic trigger present? (e.g., action vs state)

If NO special triggers found:
→ Use BASELINE: {dominant_value}
→ Confidence: {baseline_percentage}% (from distribution)

If special triggers found:
→ Override baseline with: {marked_value}
→ Confidence: depends on trigger strength
→ Reasoning: ...
```

**Consider for**: Polarity (default Affirmative ~90%), Voice (default Active ~70%), Status (default Realis ~85%), Mood (default Indicative ~85%).

---

### 4. Gateway Features

Check gateway feature FIRST to constrain other predictions.

**Proven Correlation**: Potential mood → Inceptive aspect (6/6 cases, 100%)

**Gateway Features**:
- For verbs: MOOD → constrains Aspect, Time, Voice
- For nouns: SEMANTIC TYPE → constrains Person, Number
- For clauses: GENRE → constrains Structure, Force, Salience

**Template**:
```
Gateway Feature Analysis:

Step 1: Extract gateway feature value
Verse: {reference}
Gateway: MOOD = {value}

Step 2: Apply gateway constraints
Known correlations:
- If Mood = Potential → Aspect likely = Inceptive (100% in sample)
- If Mood = Indicative + Time = Historic Past → Aspect likely = Completive

Step 3: Predict target feature
Gateway: MOOD = {value}
Target: ASPECT = ?

Based on gateway value:
- Strong correlation (>90%): Predict {value} with high confidence
- Moderate correlation (70-89%): Predict {value} with medium confidence
- Weak correlation (<70%): Cannot constrain, use other methods
```

---

### 5. Multi-Factor Convergence

Multiple independent factors agreeing increases confidence dramatically.

**Discovery**: Inceptive = 100% accurate (3/3) when 3 factors converged:
1. Action verb (beat, eat, drink) - Semantic
2. Potential mood ('might') - Grammatical
3. Near-future time (Later Today) - Temporal

**Confidence Formula**:
- 0 triggers → 30% (baseline only)
- 1 trigger → 60% (weak)
- 2 triggers → 80% (medium)
- 3+ triggers → 95%+ (strong)

**Template**:
```
Multi-Factor Analysis for {feature_name}:

FACTOR 1: {first factor type}
Analysis: ...
Prediction: {value_1}

FACTOR 2: {second factor type}
Analysis: ...
Prediction: {value_2}

FACTOR 3: {third factor type}
Analysis: ...
Prediction: {value_3}

CONVERGENCE CHECK:
- 3/3 factors agree → High confidence (95%)
- 2/3 factors agree → Medium confidence (80%)
- All disagree → Use baseline, flag for review (50%)
```

---

### 6. Check for Explicit Encoding FIRST (Tier 0)

**Critical Learning**: Always check if feature can be directly extracted before building prediction systems.

**Discovery**: Mood is EXPLICIT in TBTA YAML, not predicted (100% accuracy via extraction on 316 verbs).

**Features Likely Explicit**: Mood, Part of Speech, Constituent, some Time markers, structural features

**Features Likely Implicit**: Aspect (many unmarked), Person (clusivity), Participant Tracking, Definiteness

**Template**:
```
Feature Extraction Check:

Feature: {feature_name}

Question: Is this feature explicitly encoded in the data?

Approach:
1. Examine sample YAML for {N} verses
2. Look for field named {feature_name} or similar
3. Check if value is present and consistent

Results:
- If ALWAYS present → EXPLICIT (use direct extraction)
- If SOMETIMES present → SEMI-EXPLICIT (extract when available, predict when missing)
- If NEVER present → IMPLICIT (must predict)
```

**Note**: "EXPLICIT" refers to lexical defaults (e.g., "οὐ" is always negative), not looking at TBTA answers. This approach must work for Biblical books TBTA hasn't annotated yet.

---

### 7. Pattern Recognition Across Contexts

Similar contexts produce consistent patterns. Once established, patterns reliably predict other cases.

**Established Patterns** (validated in experiments):
- **Divine Speech**: Creation/judgment → EXCLUSIVE (100% reliable in sample)
- **Prayer to God**: Human to divine → EXCLUSIVE of God (100%)
- **Apostolic Witness**: Eyewitness testimony → EXCLUSIVE (100%)
- **Community Exhortation**: Shared faith → INCLUSIVE (95%)

**Template**:
```
Pattern Recognition Prompt:

Established patterns from previous analysis:
[List patterns with reliability metrics]

Current verse to analyze:
Verse: {reference}
Speaker: {speaker}
Addressee: {addressee}
Action: {action}

Questions:
1. Does this verse match any established pattern?
2. If yes, which pattern?
3. What is the confidence level based on pattern matching?
4. Are there differences from the pattern that might affect the result?

Predicted value based on pattern: ...
Confidence: High/Medium/Low (based on pattern reliability)
```

---

### 8. Discourse-Level Context Strategy

Some features require discourse memory beyond single verse (Participant Tracking, NounListIndex, Definiteness, Topic/Focus).

**Approach 1: LLM Memory** (Recommended First)
- Use LLM's built-in Bible knowledge
- Provide ±3 verses context in prompt
- Fast implementation (2 weeks)
- Expected accuracy: 85-90% for well-known books

**Template**:
```
Based on your knowledge of {book} {chapter} from training:

DISCOURSE CONTEXT:
1. Who are the main participants in this chapter?
2. Where does each participant first appear?
3. Has "{entity_name}" been mentioned before in this chapter?
   - If YES: In which verse? What state (First Mention, Routine, Restaging)?
   - If NO: This is First Mention

For entity "{entity_name}" in current verse:
1. Is this the first mention? → First Mention (I)
2. Has this entity been mentioned recently (within 3-5 verses)? → Routine (D)
3. Has this entity been absent and now returns? → Restaging (R)

Predicted value: ...
Confidence: High/Medium/Low (based on LLM memory strength)
```

**Approach 2: Expanded Context Window** (Fallback)
- Load and process full chapters
- Maintain explicit entity registry
- Expected accuracy: 95-100%
- Implementation time: 4-6 weeks

**Recommended**: Try Approach 1 first (fast), add Approach 2 only where LLM memory insufficient.

---

## Adversarial Testing Strategies

### Phase 1: Pattern Discovery (Training Set)

**Size**: 15-20 verses (small, focused)

**Selection criteria**:
- All possible feature values (ensure complete coverage)
- Clear, unambiguous cases (build confidence)
- 1-2 theological contexts
- Morphological diversity (Hebrew and Greek)
- Different discourse contexts (narrative, poetry, epistles)

**Process**:
1. Select training verses and commit list to git
2. Analyze TBTA annotations freely
3. Document patterns discovered
4. Build initial algorithm
5. Iterate until 90%+ accuracy on training set

---

### Phase 2: Adversarial Testing (Test Set)

**Size**: 10-15 verses (challenging edge cases)

**Selection criteria - ACTIVELY HUNT FOR EDGE CASES**:

**Theological edge cases (25%)**:
- Trinity contexts (Gen 1:26, Matt 28:19)
- Incarnation contexts (John 1:14)
- Messianic prophecies
- Corporate solidarity (Israel as one/many)

**Rare feature values (25%)**:
- Values that appeared 0-1 times in training
- Theoretical values
- Boundary cases

**Morphological exceptions (25%)**:
- Semantic ≠ morphological cases
- Fossilized forms
- Analytic vs synthetic constructions

**Ambiguous cases (25%)**:
- Multiple valid interpretations
- Translation divergence
- Context-dependent resolution

**Process**:
1. Design adversarial test set (commit list to git)
2. Make predictions WITHOUT checking TBTA
3. Document reasoning and confidence ratings
4. Commit predictions with timestamp
5. Lock predictions (no modifications allowed)
6. Check TBTA and calculate accuracy
7. Analyze failures in detail

**Expected accuracy**:
- Overall: 60-70% (if higher, test wasn't adversarial enough!)
- High confidence predictions: 85%+
- Medium confidence: 60-75%
- Low confidence: 40-60%

---

### Phase 3: Random Validation (Baseline Test)

**Size**: 10-15 verses (random sample)

**Selection criteria**:
- Different books (not in training or adversarial)
- Stratified by feature value (representative distribution)
- Mix of OT and NT
- No special selection bias

**Expected accuracy**:
- Should be HIGHER than adversarial test (80-90%)
- If lower than adversarial, algorithm has serious issues

**Critical Metric**: Random should exceed Adversarial by 15-25 percentage points.

---

### Phase 4: Translation Validation

Test predictions against actual Bible translations to confirm accuracy.

**Language Selection** (choose languages that encode the target feature):

**For Person (Clusivity)**:
- Indonesian: Kita (inclusive) vs Kami (exclusive)
- Tagalog: Atin/tayo (inclusive) vs Amin/kami (exclusive)

**For Aspect**:
- Russian: Perfective vs Imperfective
- Greek: Aorist vs Present
- Spanish: Preterite vs Imperfect

**Workflow**:
1. Make blind predictions (no translations first)
2. Gather translations in languages encoding the feature
3. Compare and analyze mismatches
4. Categorize errors: theological misunderstanding, discourse factor missed, grammatical ambiguity, dual reading

**Agreement levels**:
- 3+ languages agree → 99% confidence
- 2 languages agree → 95% confidence
- 1 language confirms → 85% confidence
- 0 languages match → Flag for review

---

## Common Error Patterns

### 1. Theological Misunderstanding

**Symptom**: Prediction doesn't match theological context
**Example**: Missing that creation is exclusively God's work in Gen 1:26
**Fix**: Add theological context questions to Level 1 prompts
**Caution**: If a theological concept is not morphologically present in the source language but inferred from context, mark with metadata flag to avoid eisogesis. Annotators should document when interpretation goes beyond explicit source language marking.

### 2. Morphological ≠ Semantic

**Symptom**: Following morphology instead of meaning
**Example**: Plural form but singular meaning (Hebrew shamayim "heaven")
**Fix**: Always check semantic analysis before morphological

### 3. Discourse Factor Missed

**Symptom**: Ignoring context beyond single verse
**Example**: Marking "First Mention" when entity already introduced earlier in chapter
**Fix**: Add discourse context prompts, use LLM memory

### 4. Gateway Feature Ignored

**Symptom**: Predicting constrained feature without checking gateway
**Example**: Predicting Aspect without checking Mood first
**Fix**: Always check gateway features in prompt hierarchy

### 5. Baseline Override Without Evidence

**Symptom**: Predicting marked value without strong triggers
**Example**: Predicting Inceptive with only 1/3 triggers present
**Fix**: Require 2-3 converging factors before overriding baseline

### 6. Pattern Overgeneralization

**Symptom**: Applying pattern to dissimilar context
**Example**: Using "Apostolic Witness" pattern for non-apostolic speaker
**Fix**: Validate all pattern conditions before applying

---

## Best Practices

### Prompt Design

**DO**:
- Start with theological/semantic analysis (Level 1)
- Use capability analysis for ambiguous cases
- Check for explicit encoding first (Tier 0)
- Apply rarity principle for baseline confidence
- Validate predictions against real translations
- Document confidence levels honestly

**DON'T**:
- Skip hierarchical levels (always start at Level 1)
- Ignore gateway features
- Override baseline without strong evidence (2-3 triggers)
- Use rarity principle to justify guessing
- Claim high accuracy without adversarial testing

---

### Testing Strategy

**DO**:
- Design adversarial test sets to find weaknesses
- Make predictions blind (before checking TBTA)
- Lock predictions before validation (git commit)
- Document all errors and learnings

**DON'T**:
- Test only on easy cases
- Look at answers before predicting
- Modify predictions after seeing TBTA
- Claim success without random validation
- Skip error analysis

---

### Accuracy Claims

**DO**:
- Report both adversarial and random accuracy
- Report confidence calibration (high/medium/low)
- Document sample sizes and selection criteria
- Acknowledge limitations
- Use "consider" language for unvalidated patterns

**DON'T**:
- Claim 100% accuracy on 3 verses (insufficient sample)
- Report only best-case accuracy
- Extrapolate small sample results to all cases
- Ignore confidence mismatches
- Present exploratory findings as proven

---

## Integration with STAGES.md

This learnings document complements the STAGES.md workflow:

**Stage 1 (Research)**: Use hierarchical prompts, check explicit encoding, establish baseline
**Stage 2 (Algorithm)**: Apply gateway features, multi-factor convergence, pattern recognition
**Stage 3 (Testing)**: Adversarial + random testing, translation validation
**Stage 4 (Refinement)**: Error analysis, pattern updates
**Stage 5 (Documentation)**: Document learnings for future features
**Stage 6 (Production)**: Deploy with confidence calibration

---

## Quick Reference: The Formula for High Accuracy

```
High Accuracy = Check Tier 0 (explicit extraction)
              + Gateway Features (check Mood/Genre/SemanticType first)
              + Hierarchical Prompts (theology → semantics → grammar)
              + Rarity Principle (establish baseline)
              + Multi-Factor Convergence (2-3 triggers for marked values)
              + Discourse Context (LLM memory when needed)
              + Translation Validation (confirm with real translations)
              + Adversarial Testing (find weaknesses early)
```


---

## Notes on Unvalidated Claims

Throughout this document, patterns marked as "consider" or "expected" have not been fully validated:

- Baseline percentages for features other than Aspect (Polarity ~90%, Voice ~70%, etc.) are estimates based on theory, not validated through testing
- Discourse context accuracy estimates (85-90% with LLM memory) are projections from limited testing
- Cross-linguistic validation confidence levels are based on Person experiment only
- Feature-specific patterns need validation before claiming reliability

Always test patterns on your specific feature before claiming accuracy.

---

**Status**: Consolidated from validated experiments (Person, Mood, Aspect, Participant Tracking)
**Last Updated**: 2025-01-14
**Source Files**: See `/workspaces/mybibletoolbox-code/plan/tbta-rebuild-with-llm/learnings/` for detailed experiment documentation
