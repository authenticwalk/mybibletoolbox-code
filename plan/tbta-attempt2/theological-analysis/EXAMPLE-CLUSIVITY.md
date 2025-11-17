# Worked Example: Clusivity Feature with Theological Framework

This document demonstrates how to apply the arbitrary vs non-arbitrary framework to the Person Systems (Clusivity) feature.

---

## Step 1: Feature Analysis for Arbitrarity

### Initial Classification

**Feature**: Person Systems - Clusivity (Inclusive vs Exclusive "we")
**Overall Theological Significance**: HIGH
**Estimated Non-Arbitrary Contexts**: ~15% of first-person plural uses

### Context Categories

#### Non-Arbitrary Contexts (~15%)

1. **Trinity/Divine Speech** (~1%)
   - Gen 1:26 "Let us make man"
   - Gen 3:22 "man has become like one of us"
   - Gen 11:7 "let us go down"
   - Isaiah 6:8 "who will go for us"

2. **Prayer Contexts** (~5%)
   - Matt 6:9 "Our Father"
   - Luke 11:2 "When you pray, say: Our Father"
   - Corporate prayer passages

3. **Apostolic Authority** (~3%)
   - 1 Cor 1:23 "we preach Christ crucified"
   - 2 Cor 5:20 "we are ambassadors"
   - Apostolic "we" vs universal "we"

4. **Salvation/Justification** (~3%)
   - Rom 5:1 "we have peace with God"
   - Eph 2:18 "we both have access"
   - Who is included in salvation statements?

5. **Church Unity/Division** (~3%)
   - 1 Cor 1:13 "Is Christ divided?"
   - Eph 4:3 "unity of the Spirit"
   - Inclusive unity vs exclusive faction

#### Arbitrary Contexts (~85%)

1. **Travel Narratives** (~40%)
   - Acts "we" passages
   - Simple group movement
   - No theological implications

2. **General Exhortation** (~30%)
   - "Let us love one another"
   - No authority claims
   - Universal application regardless

3. **Historical Narrative** (~15%)
   - "We saw", "we heard"
   - Simple past events
   - No doctrinal significance

---

## Step 2: Test Set Generation with Theological Markup

### Enhanced train.yaml Structure

```yaml
feature: person-systems-clusivity
total_verses: 100
non_arbitrary_count: 15
arbitrary_count: 85

verses:
  # NON-ARBITRARY EXAMPLES
  - reference: GEN.001.026
    text: "Let us make man in our image"
    tbta_value: inclusive
    arbitrary: false
    theological_category: trinity
    doctrines_affected: [trinity, creation, imago_dei]
    stakes: critical
    alternative_perspectives:
      divine_council: "God consulting heavenly court"
      majestic_plural: "Royal we (singular God)"
      trinity: "Father, Son, Spirit creating"
    denominational_notes:
      christian: "Generally inclusive (Trinity)"
      jewish: "Often exclusive (God + angels)"
      muslim: "Majestic plural (one God)"
    translation_critical: true

  - reference: MAT.006.009
    text: "Our Father in heaven"
    tbta_value: inclusive
    arbitrary: false
    theological_category: prayer
    doctrines_affected: [prayer, community, worship]
    stakes: medium
    alternative_perspectives:
      corporate: "Praying together (inclusive)"
      instructional: "Teaching others to pray (exclusive)"
    contextual_factors:
      - "Sermon on Mount setting"
      - "Teaching disciples"
      - "Model prayer"

  - reference: 1CO.001.023
    text: "but we preach Christ crucified"
    tbta_value: exclusive
    arbitrary: false
    theological_category: apostolic_authority
    doctrines_affected: [church_authority, apostleship]
    stakes: medium
    alternative_perspectives:
      apostolic: "We apostles alone (exclusive)"
      universal: "All believers preach (inclusive)"
    pauline_usage: "Typically exclusive for apostolic we"

  # ARBITRARY EXAMPLES
  - reference: ACT.016.010
    text: "we sought to go to Macedonia"
    tbta_value: exclusive
    arbitrary: true
    theological_category: narrative
    notes: "Simple travel narrative, Luke joins Paul's group"

  - reference: HEB.010.024
    text: "let us consider how to stir up one another"
    tbta_value: inclusive
    arbitrary: true
    theological_category: exhortation
    notes: "Universal exhortation, clusivity doesn't change meaning"
```

---

## Step 3: Multi-Path Prompt Development

### PROMPT-THEOLOGICAL.md

```markdown
# Clusivity Prediction with Theological Awareness

## Phase 1: Arbitrarity Classification

```python
def classify_theological_significance(verse):
    """
    Determine if clusivity choice has theological implications
    """

    # Check for Trinity contexts
    if is_divine_speech(verse) and has_plural_pronouns(verse):
        if verse.reference in ['GEN.1.26', 'GEN.3.22', 'GEN.11.7']:
            return 'non_arbitrary', 'trinity', 'critical'

    # Check for prayer contexts
    if contains_prayer_language(verse):
        if 'our Father' in verse.text or 'our God' in verse.text:
            return 'non_arbitrary', 'prayer', 'medium'

    # Check for apostolic authority
    if is_pauline_epistle(verse) and speaker_is_apostle(verse):
        if 'we preach' in verse.text or 'we proclaim' in verse.text:
            return 'non_arbitrary', 'authority', 'medium'

    # Check for salvation statements
    if contains_salvation_terms(verse):
        if 'we are saved' in verse.text or 'we have peace' in verse.text:
            return 'non_arbitrary', 'salvation', 'high'

    # Default to arbitrary
    return 'arbitrary', 'narrative', 'none'
```

## Phase 2A: Arbitrary Case Prediction (Standard)

For arbitrary cases, use simplified logic:

1. Is the addressee present in the action? → INCLUSIVE
2. Is the speaker distinguishing from addressee? → EXCLUSIVE
3. Default based on context type

## Phase 2B: Non-Arbitrary Case Prediction (Multi-Answer)

For non-arbitrary cases, generate theological analysis:

### Trinity Context Handler
```python
def handle_trinity_context(verse):
    return {
        'primary': {
            'value': 'inclusive',
            'confidence': 0.75,
            'rationale': 'Trinity speaking internally (Father, Son, Spirit)',
            'support': [
                'Austronesian translations use inclusive',
                'John 1:3 - all things made through the Word',
                'Consistent with Nicene Creed'
            ]
        },
        'alternatives': [
            {
                'perspective': 'Divine Council',
                'value': 'exclusive',
                'confidence': 0.20,
                'rationale': 'God addressing heavenly court',
                'support': ['Psalm 82', 'Job 1:6', 'Some Jewish interpretation'],
                'problems': ['Isaiah 44:24 - God alone created']
            },
            {
                'perspective': 'Majestic Plural',
                'value': 'inclusive',  # Note: still inclusive grammatically
                'confidence': 0.05,
                'rationale': 'Royal we (singular God speaking majestically)',
                'support': ['ANE royal texts'],
                'problems': ['Rare in Hebrew', 'Doesn\'t explain "our image"']
            }
        ],
        'translation_notes': {
            'clusivity_languages': 'Use inclusive unless denominational tradition differs',
            'study_notes': 'Explain theological options in footnote'
        }
    }
```

### Prayer Context Handler
```python
def handle_prayer_context(verse):
    # Analyze whether this is corporate or instructional
    if is_direct_prayer(verse):
        primary = 'inclusive'  # Praying together
    else:
        primary = 'exclusive'  # Teaching others to pray

    return {
        'primary': {
            'value': primary,
            'confidence': 0.65,
            'rationale': explain_prayer_context(verse)
        },
        'alternatives': [
            # ... alternative interpretation
        ]
    }
```
```

---

## Step 4: Validation Approach for Non-Arbitrary Cases

### Modified Scoring Rubric

```python
def score_theological_predictions(predictions, tbta_values, metadata):
    results = {
        'exact_match': [],
        'theologically_valid': [],
        'includes_tbta': [],
        'heresy_check': [],
        'usefulness': []
    }

    for pred, tbta, meta in zip(predictions, tbta_values, metadata):
        if meta['arbitrary']:
            # Standard scoring for arbitrary cases
            results['exact_match'].append(pred == tbta)
            results['theologically_valid'].append(True)  # No theological concern
            results['includes_tbta'].append(True)  # Not applicable
            results['heresy_check'].append(True)  # No heresy possible
            results['usefulness'].append(True)  # Simple answer sufficient

        else:
            # Enhanced scoring for non-arbitrary cases

            # 1. Exact match (less important for theological cases)
            results['exact_match'].append(pred['primary']['value'] == tbta)

            # 2. Theological validity (critical)
            valid = is_orthodox(pred['primary']) and all(
                is_orthodox(alt) for alt in pred['alternatives']
            )
            results['theologically_valid'].append(valid)

            # 3. Includes TBTA perspective (important)
            all_values = [pred['primary']['value']] + [
                alt['value'] for alt in pred['alternatives']
            ]
            results['includes_tbta'].append(tbta in all_values)

            # 4. Heresy check (critical)
            no_heresy = not enables_heresy(pred, meta)
            results['heresy_check'].append(no_heresy)

            # 5. Usefulness for translators (important)
            useful = has_clear_guidance(pred) and has_adequate_explanation(pred)
            results['usefulness'].append(useful)

    return {
        'exact_match': sum(results['exact_match']) / len(results['exact_match']),
        'theologically_valid': sum(results['theologically_valid']) / len(results['theologically_valid']),
        'includes_tbta': sum(results['includes_tbta']) / len(results['includes_tbta']),
        'heresy_check': sum(results['heresy_check']) / len(results['heresy_check']),
        'usefulness': sum(results['usefulness']) / len(results['usefulness'])
    }
```

### Success Criteria

For Clusivity feature with ~15% non-arbitrary cases:

| Metric | Arbitrary Cases | Non-Arbitrary Cases | Overall Target |
|--------|----------------|---------------------|----------------|
| Exact Match | >90% | >70% | >87% |
| Theologically Valid | N/A | 100% | 100% |
| Includes TBTA | N/A | >95% | >95% for non-arb |
| No Heresy | N/A | 100% | 100% |
| Translator Useful | >90% | >80% | >88% |

---

## Step 5: Peer Review Focus Areas

### Theological Reviewer Checklist for Clusivity

```markdown
## Trinity Passages Review
- [ ] Gen 1:26 includes Trinity, Divine Council, and Majestic Plural options
- [ ] Theological rationales are accurate
- [ ] No modalism or arianism implied
- [ ] Creedal consistency maintained

## Prayer Contexts Review
- [ ] Corporate vs instructional prayer distinguished
- [ ] Liturgical traditions respected
- [ ] No confusion about who prays to whom

## Apostolic Authority Review
- [ ] Apostolic vs universal mission distinguished
- [ ] Church authority properly handled
- [ ] No papal/episcopal implications forced

## Salvation Statements Review
- [ ] Inclusive vs exclusive salvation carefully handled
- [ ] No universalism implied where not intended
- [ ] Covenant community properly identified
```

---

## Step 6: Production Documentation

### THEOLOGICAL-ANALYSIS.md for Clusivity

```markdown
# Theological Analysis: Person Systems (Clusivity)

## Executive Summary

Clusivity has significant theological implications in approximately 15% of first-person plural contexts. These non-arbitrary cases require multi-answer output to respect theological diversity.

## Non-Arbitrary Categories

### 1. Trinity/Divine Speech (1% of verses)

**Key Verses**: Genesis 1:26, 3:22, 11:7
**Doctrinal Impact**: Trinity vs Divine Council vs Majestic Plural
**Stakes**: CRITICAL - Core doctrine of God

**Required Output**:
```yaml
primary_answer:
  value: inclusive
  rationale: "Internal Trinity dialogue"
alternatives:
  - divine_council: {value: exclusive, support: "Jewish interpretation"}
  - majestic_plural: {value: inclusive, support: "Royal we"}
```

**Translation Guidance**:
- Clusivity languages: Default to inclusive unless tradition differs
- Footnote required explaining options

### 2. Prayer Contexts (5% of verses)

**Key Verses**: Matthew 6:9, Luke 11:2
**Doctrinal Impact**: Corporate vs Individual prayer
**Stakes**: MEDIUM - Worship practice

[Continue for each category...]

## Safeguards and Warnings

### Critical Warnings
1. **NEVER** use exclusive for Trinity contexts in orthodox Christian translation
2. **NEVER** imply angels participated in creation

### Important Warnings
1. **ALWAYS** explain clusivity choice in prayer contexts
2. **CONSIDER** denominational tradition for apostolic authority

## Denomination Matrix

| Context | Catholic | Orthodox | Protestant | JW | LDS |
|---------|----------|----------|------------|-------|------|
| Trinity | Inclusive | Inclusive | Inclusive | Exclusive | Varies |
| Prayer | Inclusive | Inclusive | Varies | Varies | Varies |
| Apostolic | Exclusive | Exclusive | Varies | Inclusive | Exclusive |
```

---

## Key Insights from This Example

1. **Not all clusivity choices are equal**: ~15% have theological significance
2. **Multi-answer is essential**: Single answers risk imposing theology
3. **Context determines approach**: Trinity vs prayer vs narrative need different handling
4. **Validation must be nuanced**: Exact match less important than theological safety
5. **Documentation is critical**: Translators need to understand the stakes

This example shows how the theological framework transforms a seemingly simple grammatical feature into a theologically-aware translation tool that respects denominational diversity while preventing heretical readings.