# Polarity Feature

**Definition**: Distinguishes between affirmative (positive) and negative statements or constituents.

**TBTA Classification**: Tier A (Nouns #6), Tier B (Verbs #29)

**Status**: Stage 1 Research Complete ✅ | Stage 2 Analysis Pending

---

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Universality** | Present in ALL languages (no exceptions) |
| **Source Languages** | Hebrew: 3+ particles (לֹא/אַל/אֵין), Greek: 2 systems (οὐ/μή) + emphatic (οὐ μή) |
| **TBTA Values** | Affirmative (A), Negative (N), Emphatic Affirmative (E, verbs only) |
| **Encoding** | Position 7 (nouns), Position 4 (verbs) in TBTA character codes |
| **Global Typology** | NegV (40%), [V-Neg] (15%), [Neg-V] (12%), VNeg (13%), Double (9%), Auxiliary (4%) |
| **Marking Status** | **MANDATORY** in 90%+ of languages (rarely inferable from context) |
| **Dataset Coverage** | 1,009 translations (176 Austronesian, 141 Trans-New Guinea, 135 Indo-European, etc.) |
| **Theological Stakes** | **HIGH** in 15% of negated verses (divine commands, salvific promises, Christology) |

---

## Critical Languages

**Negative Concord** (multiple negatives = single negation):
- Slavic (Russian, Czech), Romance (Spanish, French), Greek, Hungarian, Japanese

**Double Negation** (two negatives = affirmative):
- Germanic (English, German), few globally

**Negative Auxiliary Verbs** (conjugates separately from main verb):
- Uralic (Finnish *ei*), Northern Eurasia cluster

**Prohibition Strength Distinctions** (general vs. emphatic):
- Hebrew (לֹא vs. אַל), Greek (οὐ vs. μή), Tagalog (*hindi* vs. *huwag*)

---

## Examples: High-Stakes Translation Contexts

### ✅ Correct | ❌ Incorrect | ⚠️ Problematic

| Verse | Source Text | ✅ Correct Translation | ❌/⚠️ Errors to Avoid |
|-------|-------------|------------------------|----------------------|
| **Exodus 20:13** | לֹא תִרְצָח (*lo tirtzakh*) "You shall NOT murder" | **Strongest prohibition** in target language (Tagalog *huwag*, not *hindi*) | ❌ Temporal prohibition (weakens divine command)<br>❌ Affirmative (reverses meaning - heresy) |
| **John 10:28** | οὐ μὴ ἀπόλωνται (*ou mē apolōntai*) "will NEVER perish" | **Emphatic negation**: "never, no never", "absolutely not", "impossible to perish" | ⚠️ Simple negative "will not" (loses emphatic assurance)<br>❌ Conditional "might not" (undermines eternal security) |
| **Romans 1:16** | οὐκ ἐπαισχύνομαι (*ouk epaischynomai*) "not ashamed" = **LITOTES** | **Emphatic positive** if target lacks litotes: "I am PROUD of the gospel" | ⚠️ Literal "not ashamed" in non-litotes language (loses emphasis)<br>⚠️ Neutral "don't dislike" (misses passionate devotion) |
| **1 John 2:22** | "Who DENIES Jesus is the Christ" | **Preserve negative** exactly: Denial is doctrinal boundary | ❌ Weakened "fails to acknowledge" (obscures severity of heresy)<br>❌ Affirmative (reverses orthodoxy) |

---

## Target Audience

See [research/LANGUAGES.md](./research/LANGUAGES.md) for full typological analysis.

**Key Language Families** (must be handled differently):

1. **Austronesian** (176 in dataset): Particle negation, verbal/nominal distinction (Indonesian *tidak*/*bukan*)
2. **Slavic** (Indo-European subset): Strict negative concord (Russian multiple negatives = single meaning)
3. **Romance** (Indo-European subset): Position-dependent negative concord (Spanish preverbal vs. postverbal)
4. **Bantu** (Niger-Congo): Negative prefix on verbs (Swahili *ha-*)
5. **Uralic** (Finnish): Negative auxiliary verb conjugates separately (*ei* + main verb connegative)

**Critical Distinction**: Languages with **negative concord** (majority globally) vs. **double negation** (Germanic languages) require opposite handling of multiple negatives.

---

## TBTA Encoding Details

**Noun Polarity** (Position 7 of 10):
```
Position 7: Polarity
  A = Affirmative
  N = Negative
```

**Verb Polarity** (Position 4 of 9):
```
Position 4: Polarity
  A = Affirmative
  N = Negative
  E = Emphatic Affirmative (verbs only)
```

**JSON Export**:
```json
{
  "Polarity": "Affirmative"  // or "Negative", "Emphatic Affirmative"
}
```

---

## Research Findings

**See [research/README.md](./research/README.md)** for complete summary.

**Key Findings**:
- **Insufficient values**: TBTA lacks Emphatic Negative, Prohibitive, Existential Negative
- **Missing scope annotation**: Cannot distinguish "Not all X" (partial) vs. "All X not" (total)
- **Source language detail lost**: Hebrew לֹא/אַל/אֵין collapsed to single "Negative" value
- **Theological significance exists**: 15% of negated verses are non-arbitrary (divine commands, salvific promises)
- **Target language diversity**: Negative concord, asymmetric negation, litotes require different strategies

---

## Next Steps

**Stage 2**: Corpus Analysis & Translation Database
- Analyze TBTA database export for value frequencies
- Build translation database in 10 typologically diverse languages
- Map Hebrew/Greek particles to TBTA values
- Validate with parallel passages

**Stage 3**: Algorithm Development
- Train models to predict polarity from context, morphology, semantics
- Handle edge cases (litotes, rhetorical questions, scope ambiguity)

**Stage 4**: Production Documentation
- Theological review by conservative Protestant scholars
- Cross-check high-stakes verses
- Finalize annotation protocol

---

**Lines**: 75
