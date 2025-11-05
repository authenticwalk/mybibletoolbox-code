# Generic TBTA Feature Implementation Template

## Purpose
This template provides a standardized approach for implementing, analyzing, or predicting ANY TBTA feature based on learnings from successful experiments (Aspect 98%, Person 100%, Mood 100%, Participant Tracking 100%).

---

## Phase 1: UNDERSTAND THE FEATURE

### Step 1.1: Feature Discovery
- [ ] Read official TBTA documentation for this feature
- [ ] Identify feature category (Noun/Verb/Clause/Phrase/Discourse)
- [ ] List all possible values (complete enumeration)
- [ ] Determine if feature is **explicit in YAML** or **must be predicted**

**Key Question**: Is this feature directly extractable from TBTA data?
- **YES** → Go to **Phase 2A: Direct Extraction** (Mood pathway - fastest)
- **NO** → Go to **Phase 2B: Prediction Framework** (Aspect/Person pathway)

### Step 1.2: Translation Impact Analysis
- [ ] Which language families need this feature? (List 3-5)
- [ ] What translation errors occur without this feature? (List 2-3 examples)
- [ ] What is the priority tier? (A=Essential, B=Important, C=Nice-to-have)

### Step 1.3: Data Availability Assessment
- [ ] How many verses in TBTA data have this feature annotated?
- [ ] Are annotations consistent across books/genres?
- [ ] What is the baseline distribution? (e.g., 90% Unmarked, 10% marked)

---

## Phase 2A: DIRECT EXTRACTION (For Explicit Features)

### Step 2A.1: Locate Feature in YAML Structure
```python
def find_feature_location(yaml_data, feature_name):
    """
    Recursively search YAML structure to find where feature is stored
    """
    # Template: Start with clause level, then VP/NP level, then word level
    pass
```

**Test with 3 sample verses** to confirm location stability

### Step 2A.2: Build Extraction Function
```python
def extract_feature(verse_yaml, feature_name):
    """
    Standard recursive tree traversal for ANY TBTA feature
    """
    results = []

    def traverse(node, context=None):
        # Pattern from Mood experiment: Check explicit fields first
        if isinstance(node, dict):
            if feature_name in node:
                results.append({
                    'value': node[feature_name],
                    'context': context,
                    'constituent': node.get('Constituent', 'N/A')
                })

            # Recursively check children
            if 'children' in node:
                for child in node['children']:
                    traverse(child, context={**context, 'parent': node.get('Part')})

        elif isinstance(node, list):
            for item in node:
                traverse(item, context)

    traverse(verse_yaml)
    return results
```

### Step 2A.3: Validate Extraction
- [ ] Run on 10 sample verses
- [ ] Compare extracted values vs manual inspection
- [ ] Check edge cases (nested structures, missing values, null handling)
- [ ] Document extraction reliability (should be 100% for explicit features)

**Success Criteria**: 100% extraction accuracy on all sampled verses

---

## Phase 2B: PREDICTION FRAMEWORK (For Implicit Features)

### Step 2B.1: Apply Rarity Principle
```python
def analyze_distribution(all_values):
    """
    Find dominant value (baseline) and marked values (special cases)
    """
    distribution = Counter(all_values)
    total = sum(distribution.values())

    for value, count in distribution.most_common():
        percentage = (count / total) * 100
        print(f"{value}: {percentage:.1f}%")

    baseline = distribution.most_common(1)[0][0]
    marked_values = [v for v, c in distribution.items() if c/total < 0.20]

    return {
        'baseline': baseline,  # Use as default (>80% accuracy)
        'marked': marked_values  # Need special triggers
    }
```

**Target**: Baseline should give you 80-90% accuracy immediately

### Step 2B.2: Build Hierarchical Decision Tree

**Template from Person/Aspect/Participant experiments**:

```python
def predict_feature(context):
    """
    Hierarchical decision tree: Most deterministic → Least deterministic
    """
    # LEVEL 1: Theological/Semantic Analysis (Most Important)
    theological_result = check_theological_factors(context)
    if theological_result['confidence'] > 0.95:
        return theological_result['value']

    # LEVEL 2: Capability/Restriction Analysis
    capability_result = check_capability(context)
    if capability_result['confidence'] > 0.90:
        return capability_result['value']

    # LEVEL 3: Discourse Context Analysis
    discourse_result = check_discourse_context(context)
    if discourse_result['confidence'] > 0.85:
        return discourse_result['value']

    # LEVEL 4: Grammatical Cues
    grammar_result = check_grammatical_cues(context)
    if grammar_result['confidence'] > 0.80:
        return grammar_result['value']

    # LEVEL 5: Baseline (Default)
    return {
        'value': BASELINE_VALUE,
        'confidence': baseline_accuracy,  # e.g., 0.85
        'method': 'baseline'
    }
```

### Step 2B.3: Discover Correlations

**Pattern from Aspect experiment**:

```python
def find_correlations(feature_data, context_fields):
    """
    Find which context fields strongly correlate with feature values
    """
    correlations = {}

    for field in context_fields:
        correlation_table = {}

        for instance in feature_data:
            field_value = instance.get(field)
            feature_value = instance['feature']

            key = (field_value, feature_value)
            correlation_table[key] = correlation_table.get(key, 0) + 1

        # Calculate conditional probabilities
        for (field_val, feat_val), count in correlation_table.items():
            total_with_field = sum(c for (fv, _), c in correlation_table.items() if fv == field_val)
            probability = count / total_with_field

            if probability > 0.80:  # Strong correlation
                correlations[f"{field}={field_val}"] = {
                    'predicts': feat_val,
                    'confidence': probability
                }

    return correlations
```

**Check these context fields**:
- Mood (for verb features)
- Time (for aspect/mood)
- Semantic type (for aspect/voice)
- Discourse genre (for salience/structure)
- Speaker/Listener (for demographics-related features)

### Step 2B.4: Multi-Method Validation

**Pattern from Participant Tracking**:

```python
def predict_with_ensemble(context):
    """
    Use multiple independent methods, require agreement for high confidence
    """
    method1 = theological_analysis(context)
    method2 = grammatical_analysis(context)
    method3 = discourse_analysis(context)

    predictions = [method1, method2, method3]
    values = [p['value'] for p in predictions]

    if len(set(values)) == 1:
        # All agree
        return {
            'value': values[0],
            'confidence': 0.95,
            'agreement': '100%'
        }
    elif values.count(values[0]) >= 2:
        # Majority agree
        majority_value = max(set(values), key=values.count)
        return {
            'value': majority_value,
            'confidence': 0.80,
            'agreement': '66%'
        }
    else:
        # Disagree - flag for human review
        return {
            'value': None,
            'confidence': 0.50,
            'agreement': '0%',
            'note': 'Ambiguous - requires human judgment'
        }
```

### Step 2B.5: Blind Testing Protocol

**Critical for avoiding overfitting**:

```python
def blind_test(predictions, actual_data):
    """
    Test predictions WITHOUT looking at actual values first
    """
    # 1. Make predictions for all test cases
    predicted = [predict_feature(case['context']) for case in actual_data]

    # 2. NOW compare with actual values
    correct = sum(1 for p, a in zip(predicted, actual_data) if p['value'] == a['value'])
    accuracy = correct / len(actual_data)

    # 3. Analyze errors
    errors = [(p, a) for p, a in zip(predicted, actual_data) if p['value'] != a['value']]

    return {
        'accuracy': accuracy,
        'correct': correct,
        'total': len(actual_data),
        'errors': errors
    }
```

---

## Phase 3: VALIDATION & REFINEMENT

### Step 3.1: Error Categorization

For each error, categorize as:
- **Type 1: Semantic Expansion** - TBTA added implicit information not in surface text
- **Type 2: Theological Ambiguity** - Multiple valid interpretations
- **Type 3: Cultural/Historical Knowledge** - Requires external knowledge
- **Type 4: Rare Construction** - Insufficient training data

### Step 3.2: Accuracy Tiering

| Accuracy | Tier | Automation Level |
|----------|------|------------------|
| 95-100% | Tier 1 | Full automation with spot checks |
| 85-94% | Tier 2 | Automation with human review |
| 75-84% | Tier 3 | Automation with fallbacks + review |
| <75% | Tier 4 | Human-driven with AI assistance |

### Step 3.3: Documentation Requirements

Create 4 files for each feature:

**1. README.md** - Translator-facing
- What is this feature?
- Why does it matter?
- Which languages need it?
- How to use it in translation?

**2. METHOD.md** - Developer-facing
- Extraction/prediction algorithm
- Code examples
- Decision tree logic
- Correlation tables

**3. QUICK-REFERENCE.md** - All audiences
- Feature values summary
- Examples from actual verses
- Common patterns
- Edge cases

**4. EXPERIMENT-REPORT.md** - Researcher-facing
- Methodology details
- Accuracy metrics
- Error analysis
- Future improvements

---

## Phase 4: INTEGRATION

### Step 4.1: Verse-Level Integration
```python
def integrate_feature_into_verse(verse_data, feature_values):
    """
    Add feature to verse YAML maintaining SCHEMA.md compliance
    """
    verse_data[feature_name] = {
        'values': feature_values,
        'source': 'tbta' if extracted else 'predicted',
        'confidence': confidence_score,
        'method': method_name
    }
    return verse_data
```

### Step 4.2: Cross-Feature Validation
- [ ] Check consistency with related features
- [ ] Validate against Macula data where applicable
- [ ] Ensure no contradictions with theology/discourse

### Step 4.3: Query Tool Development
```python
def query_feature(feature_name, filter_criteria):
    """
    Enable queries like "find all verses with Trial number"
    """
    results = []
    for verse in all_verses:
        if matches_criteria(verse[feature_name], filter_criteria):
            results.append({
                'reference': verse['verse'],
                'value': verse[feature_name],
                'context': get_context(verse)
            })
    return results
```

---

## Phase 5: DEPLOYMENT

### Step 5.1: Performance Optimization
- [ ] Batch processing for multiple verses
- [ ] Cache frequently-accessed data
- [ ] Optimize recursive traversal
- [ ] Parallelize independent predictions

### Step 5.2: Error Handling
```python
def safe_predict(context):
    try:
        result = predict_feature(context)
        return result
    except KeyError as e:
        return {'value': BASELINE, 'confidence': 0.85, 'error': 'missing_field'}
    except ValueError as e:
        return {'value': None, 'confidence': 0.0, 'error': 'invalid_data'}
```

### Step 5.3: Monitoring & Feedback Loop
- [ ] Track prediction accuracy on new data
- [ ] Collect user corrections
- [ ] Re-train models with feedback
- [ ] Update documentation with new patterns

---

## Success Checklist

### Minimum Viable Implementation
- [ ] Feature values enumerated
- [ ] Extraction/prediction function working
- [ ] Tested on 10+ verses with >80% accuracy
- [ ] README.md created
- [ ] Integrated with verse YAML format

### Production-Ready Implementation
- [ ] Tested on 100+ verses with documented accuracy
- [ ] All 4 documentation files created
- [ ] Error categorization complete
- [ ] Query tool functional
- [ ] Cross-feature validation passed

### Excellent Implementation
- [ ] Tested on 500+ verses
- [ ] Multiple validation methods agree
- [ ] Transferable patterns documented
- [ ] Language-specific guidance provided
- [ ] Integration with translation workflows

---

## Feature-Specific Adaptations

### For Noun Features (Number, Person, Proximity, etc.)
- Priority: Semantic/ontological analysis
- Check: Referent type, discourse tracking, theological category
- Common correlations: Semantic type, discourse status, speaker identity

### For Verb Features (Time, Aspect, Mood, etc.)
- Priority: Mood as gateway feature
- Check: Mood → Time → Aspect hierarchy
- Common correlations: Discourse genre, semantic class, telicity

### For Clause Features (Force, Demographics, Genre, etc.)
- Priority: Discourse context and speech act
- Check: Speaker/listener roles, genre, discourse structure
- Common correlations: Theological context, dialogue vs narrative

### For Phrase Features (Semantic Role, Relativization, etc.)
- Priority: Syntactic structure and discourse function
- Check: Phrase type, head properties, discourse prominence
- Common correlations: Case marking, word order, definiteness

---

## Anti-Patterns to Avoid

❌ **Don't**: Start with complex ML models
✅ **Do**: Start with simple rules, add complexity only if needed

❌ **Don't**: Ignore the rarity principle
✅ **Do**: Use the dominant value as baseline (instant 80-90% accuracy)

❌ **Don't**: Analyze features in isolation
✅ **Do**: Check correlations with mood, genre, semantics, theology

❌ **Don't**: Look at actual data before making predictions
✅ **Do**: Blind testing prevents overfitting

❌ **Don't**: Force decisions on ambiguous cases
✅ **Do**: Flag ambiguity, provide multiple readings, lower confidence

❌ **Don't**: Skip error categorization
✅ **Do**: Systematic error analysis reveals fixable patterns

❌ **Don't**: Treat all features equally
✅ **Do**: Tier by confidence, automate high-confidence only

---

## Template Usage Examples

**Example 1: Implementing "Voice" Feature**
1. Phase 1: Voice = Active/Passive/Middle, Tier A priority, affects 50+ languages
2. Phase 2A: Check if explicit in YAML → YES → Extract directly
3. Phase 3: Validate on 100 verses → 98% accuracy
4. Phase 4: Integrate, build query "find all passive divine passives"
5. Phase 5: Deploy with Tier 1 automation

**Example 2: Implementing "Definiteness" Feature**
1. Phase 1: Definite/Indefinite, Tier B priority, affects article languages
2. Phase 2B: Not explicit → Predict from discourse tracking + theological uniqueness
3. Level 1: Theological uniqueness (THE Messiah) → Definite
4. Level 2: Discourse tracking (First Mention vs Routine) → guide decision
5. Level 3: Article presence in target languages
6. Phase 3: 85% accuracy on 50 verses → Tier 2 automation with review

---

## Conclusion

This template provides a proven, systematic approach for implementing ANY TBTA feature based on patterns from successful experiments achieving 98-100% accuracy.

**Key Success Factors**:
1. Check for explicit encoding first (Mood pathway)
2. Use rarity principle (baseline = 80-90% accuracy)
3. Hierarchical decisions (theology → semantics → grammar)
4. Multi-method validation (require agreement)
5. Blind testing (prevents overfitting)
6. Error categorization (systematic improvement)
7. Tiered automation (confidence-based deployment)

Follow this template, adapt to feature-specific needs, and you will achieve high-accuracy TBTA feature reproduction.
