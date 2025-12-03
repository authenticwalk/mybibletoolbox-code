# TBTA Mood Prediction Method

## Translation Impact

**Impact Level: VERY HIGH ⭐⭐⭐⭐⭐ (5/5 stars)**

Mood determines whether an action is presented as fact, possibility, necessity, or command—fundamentally shaping reader understanding. Misidentifying mood can transform commands into suggestions ("you should go" vs "you must go"), facts into possibilities ("he is here" vs "he might be here"), or permissions into obligations. Languages vary enormously in mood encoding: some mark it grammatically (Greek subjunctive, Turkish evidentials), others use modal verbs (English must/should/might), still others rely on context alone.

### Why This Matters for Translation

- **94.6% of verbs are Indicative**: Most narrative is factual statement
- **5.4% use modal meanings**: These carry crucial semantic distinctions (obligation, permission, possibility)
- **11 distinct mood values**: TBTA captures semantic modality beyond traditional grammatical moods
- **Even 2-mood languages benefit**: TBTA helps decide when to add modal verbs ("must," "should," "might")

---

## Complete Value Enumeration

| Mood Value | Description | Frequency | Typical Usage |
|-----------|-------------|-----------|---------------|
| **Indicative** | Factual statements, assertions of reality | 94.62% | General narrative, declarative statements |
| **'might' Potential** | Possible but uncertain | 2.53% | Hypothetical futures, uncertain events |
| **'must' Obligation** | Strong necessity | 1.58% | Requirements, mandates |
| **Forbidden Obligation** | Strong prohibition | 0.63% | "Must not," prohibitions |
| **'should' Obligation** | Moderate obligation/advice | 0.32% | Recommendations, weaker requirements |
| **'should not' Obligation** | Negative advice | 0.32% | Advised against |
| **'may' (permissive)** | Permission granted | <0.1% | Allowed actions |
| **Probable Potential** | Likely outcome | <0.1% | Probable scenarios |
| **Definite Potential** | Certain possibility | <0.1% | Definite capability |
| **Subjunctive** | Hypothetical, conditional | Rare | Greek subjunctive constructions |
| **Optative** | Wishes, prayers | Rare | Greek optative constructions |

**Total Values**: 11 distinct mood types
**Test Data**: Matthew 24 (316 verbs, 51 verses)
**Source Languages**: Greek (morphological mood) + Hebrew (modal semantics)

---

## Quick Reference

- **Complete documentation**: See `DETAILED-RULES.md` for comprehensive interpretation rules
- **Validation**: See `VALIDATION.md` for language family mapping and testing priorities
- **Experiments**: See `experiments/` for iteration history

**See mood-README.md** (original full documentation) for decision trees, gateway features, and worked examples.

---

**Document Version**: 2.0
**Last Updated**: 2025-11-07
**Test Data**: Matthew 24 (316 verbs, 51 verses)
**Methodology**: Morphology + Semantics + Discourse Context
