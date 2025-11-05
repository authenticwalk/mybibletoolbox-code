# TBTA Mood Identification - Quick Reference

## Mood Types in TBTA (Tested in Matthew 24)

### Indicative (94.62%)
- **What it is**: Statement of fact
- **When to use**: Default for most verbs
- **Time**: Can be past, present, or future
- **Examples**: "Jesus talked", "You will hear", "Disciples came"

### 'must' Obligation (1.58%)
- **What it is**: Strong necessity
- **When to use**: MANDATORY actions
- **Time**: Usually Immediate Future
- **Examples**: "You must go into fields", "Must flee immediately"

### 'might' Potential (2.53%)
- **What it is**: Possible but uncertain
- **When to use**: Conditional futures or hypotheticals
- **Time**: Usually Later Today or Future
- **Examples**: "Might deceive many", "Might appoint them", "Might think"

### 'should' Obligation (0.32%)
- **What it is**: Weak necessity/recommendation
- **When to use**: RECOMMENDED actions (not mandatory)
- **Time**: Usually Later Today
- **Examples**: "Should look at buildings"

### Forbidden Obligation (0.63%)
- **What it is**: Prohibition
- **When to use**: MUST NOT do this
- **Time**: Usually Immediate Future
- **Examples**: "Do not go into houses", "Do not flee"

### Other Moods (Rare in Test Data)
- **'should not' Obligation**: Negative recommendation (0.32%)
- **'may' Permissive**: Permission (not in test data)
- **Imperative**: Direct command (check IlLocutionary Force)
- **Subjunctive**: Hypothetical (not in test data)
- **Optative**: Wish/desire (not in test data)

## How to Extract Mood from TBTA YAML

```yaml
verse: MAT.024.001
clauses:
  - children:
      - Part: NP                    # Subject
      - Part: VP                    # LOOK HERE
        children:
          - Constituent: look       # Verb lemma
            Mood: 'should' Obligation  # <-- THE MOOD
            Time: Later Today
            Aspect: Unmarked
```

**Key Point**: Mood appears inside VP (Verb Phrase) nodes

## Quick Mood Identification

| If Mood is... | Then verb indicates... | Translation approach |
|---|---|---|
| Indicative | Fact/statement | Standard verb form; tense from Time field |
| 'must' Obligation | Requirement | Modal verb "must"; mandatory |
| 'should' Obligation | Recommendation | Modal verb "should"; advisable |
| Forbidden Obligation | Prohibition | Negative form; "do not", "must not" |
| 'might' Potential | Possibility | Modal "might"; conditional |
| Imperative | Command | Imperative form; direct order |

## Time + Mood Combinations

### Immediate Future + 'must' Obligation
= Urgent mandatory action
**Example**: "You must flee immediately"

### Later Today + 'should' Obligation
= Near-term recommendation
**Example**: "You should look at the buildings"

### Immediate Future + 'might' Potential
= Possible imminent event
**Example**: "False prophets might deceive you"

### Present + Indicative
= Current fact
**Example**: "Jesus is talking"

## Red Flags & Special Cases

1. **IlLocutionary Force = Imperative but Mood = Indicative**
   → Might be an indirect command
   → Check context for implied command

2. **Obligation in Negative Polarity**
   → 'should' + Negative = "should not"
   → 'must' + Negative = "must not"

3. **Multiple verbs in sequence**
   → Each VP has its own Mood
   → Don't assume all share same mood
   → Extract each separately

## Testing Verification

All test cases passed:
- ✓ Obligation detection (MAT 24:1)
- ✓ Indicative future (MAT 24:6)
- ✓ Indicative present (MAT 24:2)

Confidence: 100% on tested patterns

## For Translators

### When you see 'must' Obligation
→ Render as strong requirement in target language
→ Examples: Turkish "zorunda", Japanese obligation form, German "muss"

### When you see 'should' Obligation
→ Render as weak recommendation
→ Examples: Turkish "gerekli", Swahili "anapasa", Russian "должен"

### When you see Forbidden Obligation
→ Render as negative imperative
→ Examples: Spanish "no hagas", Arabic "la taf'al", Tagalog "huwag kang..."

### When you see 'might' Potential
→ Render as conditional/possible
→ Examples: Chinese "可能", Hebrew "אולי", Arabic "ربما"

## Statistical Summary (Matthew 24)

- Total verbs tested: 316
- Indicative: 299 (94.62%)
- Obligations: 9 (2.85%)
- Potential: 8 (2.53%)
- Test accuracy: 100% (3/3 cases)

## Related Documents

- `experiment-001.md` - Full experimental methodology
- `mood_identification_method.md` - Technical implementation guide
- `test_mood_predictions.py` - Python extraction script
- `mood_test_results.json` - Test results data

## Quick Script Usage

```bash
# Run mood analysis on Matthew 24
python test_mood_predictions.py

# Output includes:
# - Mood distribution by type
# - Sample verbs for each category
# - Test case validation results
# - JSON export of results
```

---

**Last Updated**: Experiment 001
**Test Corpus**: Matthew 24 (51 verses, 316 verbs)
**Status**: Validated and documented
