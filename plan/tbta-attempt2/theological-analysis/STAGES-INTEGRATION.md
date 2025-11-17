# Integration Guide: Theological Analysis with STAGES.md Workflow

This document shows how to integrate the arbitrary vs non-arbitrary theological framework into the standard TBTA feature development workflow.

---

## Modified STAGES.md for Theologically Significant Features

### Stage 1: Research TBTA Documentation (ENHANCED)

**Additional Tasks for Non-Arbitrary Features**:

- [ ] Identify theological hotspots in feature space
  - Divine speech contexts
  - Salvation/soteriological contexts
  - Trinity/Christological contexts
  - Church authority contexts
  - Prophetic/eschatological contexts

- [ ] Document denominational perspectives
  - Catholic interpretation
  - Orthodox interpretation
  - Protestant (Reformed, Arminian, etc.)
  - Other traditions (JW, LDS, etc. if relevant)

- [ ] Create initial arbitrarity classification
  ```yaml
  feature: person-systems
  theological_contexts:
    - context: Trinity_passages
      frequency: ~1%
      arbitrary: false
      stakes: high
    - context: prayer_contexts
      frequency: ~5%
      arbitrary: false
      stakes: medium
    - context: travel_narratives
      frequency: ~10%
      arbitrary: true
      stakes: none
  ```

### Stage 2: Language Study (ENHANCED)

**Additional Tasks**:

- [ ] Identify languages with theological significance
  - Languages with trial number (Trinity implications)
  - Languages with clusivity (prayer/authority implications)
  - Languages with evidentiality (prophecy implications)

- [ ] Document theological translation traditions
  - How do Bible translations in this language family handle theological passages?
  - Are there denominational Bible versions with different choices?

### Stage 3: Scholarly and Internet Research (ENHANCED)

**Additional Tasks**:

- [ ] Research theological commentaries on key verses
  - Early church fathers
  - Reformation theologians
  - Modern systematic theologians

- [ ] Document historical controversies
  - Council decisions
  - Denominational splits
  - Translation debates

- [ ] Create theological bibliography
  ```markdown
  ## Theological Sources
  - [Source 1]: Position on [doctrine]
  - [Source 2]: Alternative view on [doctrine]
  ```

### Stage 4: Generate Proper Test Set (CRITICAL ENHANCEMENT)

**Modified Requirements for Non-Arbitrary Features**:

```python
# Subagent script modification for theological features
def generate_test_set(feature_name):
    verses = collect_tbta_verses(feature_name)

    # NEW: Separate arbitrary from non-arbitrary
    arbitrary_verses = []
    non_arbitrary_verses = []

    for verse in verses:
        if is_theologically_significant(verse):
            non_arbitrary_verses.append({
                'reference': verse.ref,
                'value': verse.value,
                'theological_context': classify_theology(verse),
                'doctrines_affected': get_affected_doctrines(verse),
                'denominational_variants': get_denominational_views(verse)
            })
        else:
            arbitrary_verses.append(verse)

    # Ensure balanced sampling includes both types
    train = sample_balanced(arbitrary_verses, 0.3) + sample_all(non_arbitrary_verses, 0.5)
    test = sample_balanced(arbitrary_verses, 0.35) + sample_all(non_arbitrary_verses, 0.25)
    validate = sample_balanced(arbitrary_verses, 0.35) + sample_all(non_arbitrary_verses, 0.25)

    # NEW: Generate theological analysis template
    create_theological_template(non_arbitrary_verses)
```

**Test Set Metadata Enhancement**:
```yaml
# train.yaml with theological markup
verses:
  - reference: "GEN.001.026"
    tbta_value: "inclusive"
    arbitrary: false
    theological_significance: critical
    doctrines: [Trinity, creation]
    alternative_views:
      divine_council: "Some Jewish interpreters"
      majestic_plural: "Some Muslim interpreters"
    notes: "Requires multi-answer output"

  - reference: "ACT.016.010"
    tbta_value: "exclusive"
    arbitrary: true
    theological_significance: none
    notes: "Simple narrative we-passage"
```

### Stage 5: Propose Hypothesis and First Prompt (CRITICAL ENHANCEMENT)

**New Prompt Structure for Non-Arbitrary Cases**:

```markdown
## PROMPT3.md - Theological Multi-Path Version

### Step 1: Arbitrarity Classification
Determine if this verse has theological significance:

```python
def classify_arbitrarity(verse):
    # Check for divine speech
    if speaker_is_divine():
        return "non_arbitrary", "divine_speech"

    # Check for doctrinal keywords
    if contains_doctrinal_terms(['salvation', 'justified', 'trinity']):
        return "non_arbitrary", "doctrinal"

    # Check for authority contexts
    if is_apostolic_or_prophetic():
        return "non_arbitrary", "authority"

    return "arbitrary", None
```

### Step 2A: Arbitrary Case Handling
For arbitrary cases, use standard prediction...

### Step 2B: Non-Arbitrary Case Handling
For non-arbitrary cases, generate multiple perspectives:

```yaml
primary_interpretation:
  value: [predicted_value]
  confidence: [0.0-1.0]
  theological_basis: [explanation]
  supporting_evidence: [verses, traditions]

alternative_interpretations:
  - perspective: [name]
    value: [alternative_value]
    confidence: [0.0-1.0]
    theological_basis: [explanation]
    denominational_support: [list]
    why_not_primary: [explanation]
```
```

**Error Analysis Enhancement**:

When analyzing errors in non-arbitrary contexts:

```markdown
## Error Analysis for Theological Cases

### Error Type: Theological Perspective Difference
**Verse**: [reference]
**Our Prediction**: [value]
**TBTA Value**: [value]
**Analysis**: This is not an "error" but a legitimate theological difference
**Resolution**:
  - Add as alternative perspective
  - Document denominational preference
  - NOT counted as algorithm failure

### Error Type: Missing Theological Nuance
**Verse**: [reference]
**Issue**: Algorithm missed [specific theological point]
**Resolution**:
  - Add theological check for [pattern]
  - Enhance prompt with [theological concept]
```

### Stage 6: Test Against Validate Set & Peer Review (CRITICAL ENHANCEMENT)

**Modified Peer Review for Theological Features**:

#### Subagent 7: Doctrinal Orthodoxy Reviewer (NEW)
```markdown
## Theological Orthodoxy Review Checklist

**Reviewer Context**: "I am reviewing this from an orthodox Christian perspective, checking for doctrinal accuracy and heresy prevention."

### Core Doctrine Preservation
- [ ] Trinity properly handled (no modalism, arianism, etc.)
- [ ] Christology orthodox (fully God, fully man)
- [ ] Salvation by grace maintained
- [ ] Biblical authority preserved
- [ ] No novel heresies introduced

### Multi-Perspective Fairness
- [ ] Alternative views accurately represented
- [ ] No strawman arguments
- [ ] Denominational views fairly stated
- [ ] Minority positions acknowledged where legitimate

### Red Flags
- [ ] Any interpretation enabling cult theology
- [ ] Any reading undermining core creeds
- [ ] Any option creating new doctrine
```

#### Modified Validation Metrics

For non-arbitrary cases, success is NOT just accuracy percentage:

```python
def calculate_theological_success(predictions, tbta_values, theological_metadata):
    metrics = {
        'exact_match': 0,
        'theologically_acceptable': 0,
        'includes_tbta_as_alternative': 0,
        'doctrinal_safety': 0
    }

    for pred, tbta, meta in zip(predictions, tbta_values, theological_metadata):
        # Exact match with TBTA
        if pred['primary_value'] == tbta:
            metrics['exact_match'] += 1

        # TBTA value appears in alternatives
        alternatives = [alt['value'] for alt in pred.get('alternatives', [])]
        if tbta in alternatives or pred['primary_value'] == tbta:
            metrics['includes_tbta_as_alternative'] += 1

        # Theologically acceptable (even if different from TBTA)
        if is_theologically_orthodox(pred, meta):
            metrics['theologically_acceptable'] += 1

        # Doctrinal safety (no heresy enabled)
        if not enables_false_teaching(pred, meta):
            metrics['doctrinal_safety'] += 1

    return metrics
```

**Success Criteria for Non-Arbitrary Features**:
- Exact match: >70% (lower threshold acceptable)
- TBTA in alternatives: >95% (must acknowledge TBTA perspective)
- Theologically acceptable: 100% (no heresy)
- Doctrinal safety: 100% (no false teaching enabled)

---

## New Files Required for Theological Features

### 1. experiments/THEOLOGICAL-ANALYSIS.md

Template:
```markdown
# Theological Analysis: [Feature Name]

## Non-Arbitrary Context Inventory

Total verses analyzed: [N]
Non-arbitrary verses: [M] ([X]%)
Arbitrary verses: [N-M] ([Y]%)

## Non-Arbitrary Categories

### Category 1: Trinity Contexts
**Frequency**: [X] verses
**Examples**: Gen 1:26, Gen 3:22, Gen 11:7
**Doctrines Affected**: Trinity, Divine nature
**Required Handling**: Multi-perspective output with Trinity, Divine Council, and Majestic Plural options

### Category 2: [Next Category]
...

## Denominational Perspective Matrix

| Context | Catholic | Orthodox | Reformed | Arminian | Other |
|---------|----------|----------|----------|----------|--------|
| Trinity passages | Inclusive | Inclusive | Inclusive | Inclusive | Varies |
| Prayer contexts | Inclusive | Inclusive | Varies | Varies | Varies |

## Translation Guidance by Context

### For Clusivity-Marking Languages
- Trinity: Use inclusive
- Prayer: Consider inclusive with footnote
- Authority: Use exclusive for apostolic contexts

### For Number-Marking Languages
- Trinity: Use trial if available
- Groups: Use appropriate number based on context
```

### 2. experiments/THEOLOGICAL-SAFEGUARDS.md

Template:
```markdown
# Theological Safeguards: [Feature Name]

## Critical Warnings (Prevent Heresy)

1. **NEVER** [specific prohibition]
   - Context: [where this applies]
   - Risk: [what heresy this prevents]
   - Example: [verse where this matters]

## Important Warnings (Prevent Confusion)

1. **AVOID** [specific practice]
   - Context: [where this applies]
   - Risk: [what confusion this prevents]
   - Alternative: [what to do instead]

## Automated Flags to Generate

```python
def generate_theological_warnings(verse, prediction):
    warnings = []

    if is_trinity_context(verse) and prediction == 'singular':
        warnings.append("CRITICAL: Singular would deny Trinity")

    if is_prayer_context(verse) and not explained_clusivity(prediction):
        warnings.append("IMPORTANT: Explain inclusive/exclusive choice")

    return warnings
```
```

### 3. experiments/MULTI-ANSWER-TEMPLATES.md

Pre-built templates for common theological contexts:

```yaml
# Template: Trinity Passages
trinity_template:
  structure:
    primary_answer:
      value: trial|inclusive
      theological_basis: "Trinitarian interpretation"
    alternatives:
      - divine_council:
          value: plural|exclusive
          support: "Psalm 82, Jewish interpretation"
          problems: "Isaiah 44:24 - God alone created"
      - majestic_plural:
          value: plural
          support: "Royal we in ANE texts"
          problems: "Hebrew rarely uses majestic plural"

# Template: Prayer Contexts
prayer_template:
  structure:
    primary_answer:
      value: [based on context]
    alternatives:
      - corporate_prayer:
          value: inclusive
          rationale: "Community praying together"
      - teaching_prayer:
          value: exclusive
          rationale: "Teacher instructing others"
```

---

## Workflow Decision Tree

```
Feature Development Start
    ↓
Is feature theologically significant?
    ├─ No → Standard STAGES.md workflow
    └─ Yes → Enhanced theological workflow
              ↓
         Stage 1: Flag theological contexts
              ↓
         Stage 4: Include theological metadata
              ↓
         Stage 5: Develop multi-answer prompts
              ↓
         Stage 6: Enhanced validation with theological review
              ↓
         Production: Include safeguards and warnings
```

---

## Key Takeaways

1. **Not all features are equal**: Some have massive theological implications
2. **Not all errors are equal**: Theological perspective differences aren't failures
3. **Not all accuracies are equal**: 100% exact match may be impossible and unnecessary
4. **Multi-answer is better**: Present options rather than forcing one interpretation
5. **Safeguards are essential**: Prevent heresy even if accuracy is lower

This integration ensures theological faithfulness while respecting denominational diversity and preventing false teaching.