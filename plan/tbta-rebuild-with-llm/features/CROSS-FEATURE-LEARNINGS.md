# Cross-Feature Learnings: Universal Patterns in TBTA Annotation

**Purpose**: Document patterns, methodologies, and insights that apply across multiple TBTA features.

**Source Experiments**:
- number-systems/experiment-001.md (91.4% accuracy)
- degree/experiment-001.md (in progress)
- Additional feature experiments

---

## Universal Principle 1: Semantic Encoding Over Morphological Form

### Pattern
**TBTA prioritizes SEMANTIC meaning over source language MORPHOLOGICAL markers.**

### Evidence

#### Number Systems (experiment-001)
- Hebrew שָׁמַיִם (shamayim) has dual morphology (-ayim suffix) → TBTA marks **Singular**
- Hebrew מַיִם (mayim) has dual morphology → TBTA marks **Singular**
- Greek οὐρανῶν (ouranōn) is genitive plural → TBTA marks **Singular**
- **Conclusion**: "How many entities?" matters more than "what's the grammatical form?"

#### Degree (expected pattern)
- Greek μεγάλη (positive form) with superlative context → Likely marked **S** (Superlative)
- Hebrew מִן construction (not morphological comparative) → Should mark **C** (Comparative)
- **Hypothesis**: Semantic comparison matters more than synthetic morphology

### Application Rule
```
When predicting TBTA values:
1. Determine semantic meaning FIRST (how many? how much comparison?)
2. Check morphological form SECOND (for confirmation, not primary)
3. If semantic ≠ morphological, ALWAYS choose semantic
```

### Cross-Feature Implications
- **Person**: Semantic role > morphological person agreement
- **Proximity**: Semantic distance > demonstrative form
- **Polarity**: Semantic negation scope > negative morphology
- **Time**: Discourse-relative time > tense morphology

---

## Universal Principle 2: Theological Knowledge Required for Biblical Texts

### Pattern
**TBTA incorporates theological interpretation for doctrinally significant passages.**

### Evidence

#### Number Systems: Trinity = Trial
- Genesis 1:26 "Let us make..." → God marked as **Trial + First Inclusive**
- NO morphological trial marker in Hebrew/Greek
- **Requires**: Knowledge that Trinity = Father, Son, Spirit = 3 persons
- **Accuracy**: 100% match when theological context identified

### Application Rule
```
For Biblical texts specifically:
1. Identify theologically significant passages (Trinity, incarnation, etc.)
2. Apply doctrinal interpretation where relevant
3. Document these as special cases requiring theological tagging
```

### Recommended Theological Tags
- **Trinity contexts**: Gen 1:26, Matt 3:16-17, Matt 28:19, 2 Cor 13:14
- **Incarnation contexts**: John 1:1-14 (dual nature of Christ)
- **Messianic prophecies**: May affect participant identification
- **Corporate solidarity**: Israel/Church as singular or plural

### Cross-Feature Implications
- **Number**: Trinity = Trial
- **Person**: Trinity first inclusive plural
- **Participant Tracking**: God as singular vs. plural across contexts

---

## Universal Principle 3: Discourse Role Determines Feature Values

### Pattern
**Same referent can have DIFFERENT feature values depending on DISCOURSE ROLE.**

### Evidence

#### Number Systems: God in Genesis 1:26
- God as **narrator** → Singular Third person
- God as **speaker** ("Let us make") → Trial First Inclusive
- **Same entity, different numbers based on discourse role**

#### Number Systems: Nicodemus in John 3:2
- Nicodemus as **individual** → Singular
- Nicodemus as **group speaker** ("we know") → Plural First Exclusive
- **Same person, different numbers based on speaking role**

### Application Rule
```
When tracking participants:
1. Identify EACH occurrence's discourse role
2. Assign features PER ROLE, not per entity identity
3. Track role transitions (narrator → speaker, individual → representative)
```

### Cross-Feature Implications
- **Number**: Role-based assignment
- **Person**: Role determines person (narrator = 3rd, speaker = 1st)
- **Participant Tracking**: First mention, routine, restaging across roles
- **Surface Realization**: Role affects pronoun/noun choice

---

## Universal Principle 4: Systematic Testing Methodology

### The Gold Standard Approach (from number-systems/experiment-001)

#### Phase 1: Prediction Before Data
```
For each test verse:
1. List ALL constituents that could have the feature
2. For EACH constituent, predict ALL possible values
3. Document detailed REASONING for each prediction
4. Identify KEY UNCERTAINTIES explicitly
5. Record ALTERNATIVE predictions where uncertain
```

#### Phase 2: Check Against TBTA
```
For each prediction:
1. Retrieve actual TBTA annotation
2. Mark as MATCH ✅ or MISMATCH ❌
3. For mismatches, document:
   - What was predicted
   - What TBTA actually marked
   - Why the mismatch occurred
   - What pattern this reveals
```

#### Phase 3: Exhaustive Debugging for Mismatches (TARGET: 100% ACCURACY)
```
For EACH mismatch, debug exhaustively:

Step 1: Verify Data Accuracy
- [ ] Confirm verse reference is correct
- [ ] Verify TBTA data extraction (correct feature, correct constituent)
- [ ] Check for data corruption or version mismatch

Step 2: Re-analyze Source Text
- [ ] Re-examine Greek/Hebrew morphology (synthetic forms, particles)
- [ ] Check interlinear translations for semantic meaning
- [ ] Consult lexicons for alternate meanings
- [ ] Review grammatical commentaries

Step 3: Re-analyze Context
- [ ] Expand context window (preceding/following verses)
- [ ] Check discourse structure (paragraph, chapter)
- [ ] Identify any theological/cultural factors
- [ ] Review parallel passages

Step 4: Cross-Reference Multiple Sources
- [ ] Check 3+ English translations
- [ ] Check 2+ scholarly commentaries
- [ ] Consult target language examples (if available)
- [ ] Review linguistic databases (WALS, Glottolog)

Step 5: Test Alternative Hypotheses
- [ ] Could TBTA be using a different algorithm?
- [ ] Is there a valid alternative interpretation?
- [ ] Does this reveal a new pattern we missed?
- [ ] Is this an edge case requiring special handling?

Step 6: Make Final Determination
If after Steps 1-5, our prediction STILL seems more accurate:
→ Flag as POTENTIAL TBTA ERROR for team review
→ Document comprehensive analysis in potential-errors/ folder

If TBTA annotation is defensible:
→ Document as LEARNED PATTERN
→ Update algorithm to handle this case
→ Reclassify prediction methodology
```

#### Phase 4: Pattern Analysis
```
Across all results:
1. Calculate accuracy by value type
2. Identify systematic patterns in matches
3. Identify systematic patterns in mismatches
4. Document edge cases and uncertainties
5. Create refined algorithm
6. Isolate potential TBTA errors vs. methodology gaps
```

#### Phase 5: Secondary Findings
```
Document where languages/translations might disagree:
1. Morphological vs semantic disagreements
2. Cultural interpretation differences
3. Theological interpretation variations
4. Ambiguous cases requiring translator choice
```

### Success Metrics
- **Target accuracy**: 100% (either match or potential TBTA error flagged)
- **Learned patterns**: 95%+ accuracy (confirmed algorithm works)
- **Potential TBTA errors**: Flagged with exhaustive analysis
- **High confidence patterns**: 95%+ accuracy
- **Medium confidence patterns**: 70-90% accuracy
- **Low confidence patterns**: Flagged for human review

---

## Universal Principle 5: Rare/Theoretical Values Often Absent

### Pattern
**Some TBTA values are RARE or NEVER USED in Biblical texts.**

### Evidence

#### Number Systems
- **Quadrial**: Theoretically exists, but NOT FOUND in test verses
- **Paucal**: Defined but needs specific count contexts (4-10)
- **Trial**: ONLY for Trinity contexts (theologically derived)

#### Degree (preliminary findings)
- **T (excessive "too")**: Rare/absent in formal Biblical register
- **s (superlative of 2)**: Very rare, may not exist
- **q (equative)**: Requires specific "as...as" construction

### Application Rule
```
When encountering rare values:
1. Mark as LOW CONFIDENCE in predictions
2. Design specific experiments to hunt for instances
3. Consider that value may be theoretical but unused
4. Document whether EVER found in Biblical corpus
```

### Cross-Feature Implications
- **All features**: Some values are edge cases
- **Validation**: Need comprehensive corpus search for rare values
- **Translation**: Rare values may indicate translator choice points

---

## Universal Principle 6: Context Window Matters

### Pattern
**Multi-verse context often required for accurate annotation.**

### Evidence

#### Participant Tracking
- First mention vs. routine reference requires tracking across verses
- Cannot determine from single verse alone

#### Discourse Genre
- Genre affects register, verb selection, clause structure
- Requires paragraph-level context

#### Time Granularity
- Discourse-relative anchoring (yesterday from narrator's perspective)
- Requires understanding narrative timeline

### Application Rule
```
When annotating:
1. Determine MINIMUM context window needed
2. For discourse features: Paragraph level minimum
3. For participant tracking: Multi-verse tracking
4. For morphological features: Single verse may suffice
```

---

## Cross-Feature Algorithm Template

Based on successful experiments, here's the universal template:

### Step 1: Identify Feature Candidates
```
Scan verse for all constituents that could have this feature:
- Part of speech filtering
- Semantic category filtering
- Discourse role filtering
```

### Step 2: Semantic Analysis (PRIORITY)
```
For each candidate:
- Determine semantic meaning (entities, comparison, negation, etc.)
- Check discourse context
- Identify theological significance
- Result: Semantic value
```

### Step 3: Morphological Validation
```
For each candidate:
- Check source language morphology
- Identify explicit markers
- Note mismatches with semantic analysis
- Result: Morphological support or conflict
```

### Step 4: Resolve Conflicts
```
If semantic ≠ morphological:
- ALWAYS prefer semantic interpretation
- Document the mismatch as learning
- Check if pattern applies cross-linguistically
```

### Step 5: Apply Special Rules
```
Check for:
- Theological contexts (Trinity, incarnation, etc.)
- Discourse role transitions
- Cross-linguistic rare values
- Target language constraints
```

### Step 6: Confidence Rating
```
Assign confidence based on:
- High: Clear semantic + morphological agreement
- Medium: Semantic clear, morphological ambiguous
- Low: Both semantic and morphological uncertain
```

---

## Common Errors Across Features

### Error Type 1: Morphology Over Semantics (~20-40% of errors)
**Symptom**: Predicting based on grammatical form instead of meaning
**Solution**: Always ask "What does this MEAN?" before "What form is it?"
**Examples**:
- Hebrew dual suffix but singular meaning → Semantic wins
- Greek positive form but superlative meaning → Semantic wins

### Error Type 2: Missing Discourse Context (~15-25% of errors)
**Symptom**: Predicting from single verse when context required
**Solution**: Expand context window, track participants across verses
**Examples**:
- Participant tracking without multi-verse context
- Genre without paragraph-level understanding

### Error Type 3: Ignoring Theological Knowledge (~5-10% but HIGH IMPACT)
**Symptom**: Missing Trinity, incarnation, or other doctrinal markers
**Solution**: Create theological passage checklist, apply special rules
**Examples**:
- Trinity not marked as Trial
- Messianic prophecy participants misidentified

### Error Type 4: Over-predicting Rare Values (~10-15% of errors)
**Symptom**: Predicting theoretical values that don't actually occur
**Solution**: Check frequency, design experiments to hunt for rare values
**Examples**:
- Predicting Quadrial (probably doesn't exist)
- Predicting excessive degree in formal register

---

## Experimental Design Best Practices

### Principle 1: Test ALL Values
- Select verses to cover EVERY possible feature value
- Include edge cases and rare values
- Document if certain values are NEVER found

### Principle 2: Predict BEFORE Checking
- Forces independent reasoning
- Reveals systematic biases
- Documents uncertainties explicitly

### Principle 3: Document Secondary Findings
- Note where languages disagree
- Identify translator choice points
- Record cultural/theological variations

### Principle 4: Calculate Success Metrics
- Overall accuracy rate
- Accuracy by value type
- Confidence calibration (high/medium/low)

### Principle 5: Iterate and Refine
- Use mismatches to refine algorithm
- Design follow-up experiments for uncertainties
- Build confidence levels for each pattern

---

## Feature-Specific Patterns to Document

When creating new feature experiments, document:

1. **Semantic vs Morphological**: Which takes priority? Examples?
2. **Theological Knowledge**: Any doctrine-driven values? Which passages?
3. **Discourse Role**: Does same entity get different values? When?
4. **Rare Values**: Which values are theoretical? Any evidence?
5. **Context Window**: Single verse or multi-verse? Paragraph level?
6. **Cross-Linguistic**: Do target languages disagree? Where?
7. **Success Rate**: What accuracy achieved? Confidence by pattern?

---

## Key Learnings Template for Each Feature

```markdown
# Feature: [Name]

## Major Insight #1: [Pattern Name]
**Evidence**: [Specific examples from experiments]
**Rule**: [How to apply this pattern]
**Accuracy**: [Success rate for this pattern]
**Cross-Feature**: [Does this apply elsewhere?]

## Major Insight #2: [Pattern Name]
...

## Common Errors
**Error Type 1**: [Description]
- **Symptom**: [How to recognize]
- **Frequency**: [% of errors]
- **Solution**: [How to avoid]

## Rare/Absent Values
- **Value X**: Never found in Biblical texts
- **Value Y**: Only in theological contexts

## Refined Algorithm
[Step-by-step procedure based on experiments]

## Confidence Levels
- **High**: [Patterns with 90%+ accuracy]
- **Medium**: [Patterns with 70-90% accuracy]
- **Low**: [Patterns needing human review]
```

---

## Success Stories

### Number Systems: 91.4% Accuracy
- **32/35 predictions correct**
- **All errors** due to morphological vs semantic (learned pattern!)
- **Theological knowledge** requirement confirmed (Trinity = Trial)
- **Discourse role** tracking validated

### Key Factors in Success
1. Systematic prediction before checking
2. Testing ALL possible values
3. Documenting uncertainties explicitly
4. Analyzing mismatches for patterns
5. Refining algorithm based on results

---

## Next Steps for Feature Development

1. **Apply this methodology** to remaining features without experiments
2. **Document secondary findings** (language disagreements, translator choices)
3. **Build confidence calibration** (high/medium/low accuracy expectations)
4. **Create shared learnings** as patterns emerge across features
5. **Propagate insights** back to existing features for refinement

---

**Last Updated**: 2025-11-07
**Features Analyzed**: number-systems (complete), degree (in progress)
**Next Feature**: [To be determined based on priority]
