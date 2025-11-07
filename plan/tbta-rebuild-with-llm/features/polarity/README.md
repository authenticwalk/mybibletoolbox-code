# TBTA Feature: Polarity

## Translation Impact

Polarity determines whether a constituent is affirmed or negated, directly affecting lexical selection and grammatical forms across languages. Languages with strict negative concord (Spanish, Russian, Greek, Turkish) require multiple negative elements for single semantic negation ("I nothing not saw" = "I didn't see anything"), while non-NC languages (English, German) interpret double negatives as affirmative. Languages with genitive of negation (Russian, Finnish) change case marking under negation, and languages with special negative existentials (Hebrew אֵין, Russian нет, Turkish yok) use different vocabulary entirely. Without accurate polarity annotation, translations will produce ungrammatical negative concord violations, incorrect case marking, or inappropriate negative polarity items, critically affecting ~50% of languages with specialized negative systems.

## Complete Value Enumeration

TBTA uses a binary polarity distinction primarily at the noun level:

| Code | Meaning | Description | Usage |
|------|---------|-------------|-------|
| `Affirmative` | Positive | Normal positive assertion | Default, unmarked polarity |
| `Negative` | Negated | Negated existence/presence | Noun's existence/presence negated |

**Application:** Polarity is encoded at the constituent (especially noun) level rather than purely at verb level, capturing whether the noun's existence or presence is negated.

## Baseline Statistics

Expected distribution in Biblical texts (estimates based on negation frequency):

| Value | Estimate | Context |
|-------|----------|---------|
| `Affirmative` | ~85% | Default, unmarked positive assertions |
| `Negative` | ~15% | Negated constituents, negative existentials |

**Source Language Patterns:**
- Hebrew: Uses special negative existential אֵין (ein) for "there is not"
- Greek: Negative particles οὐ/μή with negative concord patterns
- Negation more frequent in teaching/prohibitive texts
- Existential negations common in narrative

**Genre Variation:**
- Legal/Prohibitive: Higher negation (20-25%)
- Narrative: Moderate negation (~15%)
- Wisdom/Teaching: Variable, contextual
- Apocalyptic: Lower negation (~10%)

## Quick Translator Test

**Critical questions to determine polarity requirements:**

1. **Does your language allow or require negative concord?**
   - Strict NC: Multiple negatives required (Russian, Spanish, Greek, Turkish)
   - Optional NC: Context-dependent (some Romance)
   - No NC (Double Negation): Two negatives = positive (English, German)

2. **Does negation affect case marking or grammatical form?**
   - Genitive of negation: Objects take genitive (Russian, Finnish)
   - Partitive case: Required with negation (Finnish)
   - No case change: Negation doesn't affect case (English, Mandarin)
   - Special negative forms: Different verb/noun forms

3. **Does your language have special negative existential constructions?**
   - Dedicated word (Hebrew אֵין, Russian нет, Turkish yok)
   - Negated copula (English "there isn't")
   - Same as verbal negation

4. **Does your language have negative polarity items (NPIs)?**
   - Special items in negative contexts (English "any", Japanese も-series)
   - No dedicated NPIs
   - Universal quantifiers in negative contexts

5. **How does your language express "no one," "nothing," "never"?**
   - Negative indefinites: Single word (English "nobody")
   - NPI + negation: Requires negative verb (Japanese "dare-mo...nai")
   - Multiple negation: NC with negative verb + pronoun (Russian, Spanish)

**Critical Indicators:**

- **Strict NC languages** → Must annotate all constituents in negation scope
- **Genitive/Partitive of negation** → Polarity affects case, not just negative marker
- **Special negative existentials** → Requires different vocabulary, not adding "not"
- **NPI languages** → Must select polarity-sensitive items (like "any" vs "some")

## Examples

**Example 1: Genesis 19:31** - Negative Existential
```yaml
Hebrew: אֵין אִישׁ בָּאָרֶץ (ein ish ba'aretz)
English: "There is not a man in the earth"
Constituent: man
Polarity: Negative
Reason: Special negative existential אֵין negates existence of men
```

**Example 2: Matthew 5:18** - Negative Quantification
```yaml
Greek: ἰῶτα ἓν ἢ μία κεραία οὐ μὴ παρέλθῃ (iōta hen ē mia keraia ou mē parelthē)
English: "Not one jot or one tittle shall pass"
Constituent: jot, tittle
Polarity: Negative
Reason: Universal negative quantification with οὐ μή (emphatic negation)
```

**Example 3: Romans 3:10** - Negative Indefinite
```yaml
Greek: οὐκ ἔστιν δίκαιος οὐδὲ εἷς (ouk estin dikaios oude heis)
English: "There is no one righteous, not even one"
Constituent: one (person)
Polarity: Negative
Reason: Negative concord (οὐκ...οὐδέ), negated existence
```

**Example 4: Psalm 14:1** - Negative Polarity
```yaml
Hebrew: אֵין אֱלֹהִים (ein elohim)
English: "There is no God"
Constituent: God
Polarity: Negative (in context: "no belief in God")
Reason: Negative existential construction with אֵין
```

**Example 5: John 1:18** - Negative with Emphasis
```yaml
Greek: θεὸν οὐδεὶς ἑώρακεν πώποτε (theon oudeis heōraken pōpote)
English: "No one has ever seen God"
Constituent: one (person)
Polarity: Negative
Reason: οὐδείς (no one) with πώποτε (ever), negative polarity
```

## Hierarchical Prompt Template (5-Level)

### Level 1: Check for Negation

```
Is there negation in this clause affecting the noun?

Source: [Greek/Hebrew text]
Translation: [English]

Check for:
- Negative particles (Greek οὐ/μή, Hebrew לֹא/אַל/אֵין)
- Negative words ("not", "no", "never", "nothing", "none")
- Negative existentials (Hebrew אֵין, specific constructions)
- Negative indefinites ("nobody", "nothing")
- Context of prohibition or denial

Answer: YES or NO
```

**Decision:** NO → `Affirmative` (default), STOP | YES → Continue to Level 2

### Level 2: Identify Negation Type

```
What type of negation is present?

Options:
A. Verbal Negation: Negates the verb/action
   - "He did not go"

B. Existential Negation: Negates existence
   - "There is no man"
   - Hebrew אֵין, Russian нет, Turkish yok

C. Constituent Negation: Negates specific noun
   - "Not the man, but the woman"
   - Noun in scope of negation

D. Negative Indefinite: Inherently negative noun/pronoun
   - "Nobody came", "Nothing happened"
   - Requires negative concord in NC languages

Identified type: [A, B, C, or D]
```

**Decision:** Continue to Level 3

### Level 3: Determine Scope of Negation

```
Is the noun within the scope of negation?

Questions:
1. Does negation apply to this specific noun?
2. Is noun the subject/object of negated verb?
3. Is noun part of negative existential ("there is no X")?
4. Is noun a negative indefinite ("nothing", "no one")?

Scope analysis:
- Noun directly negated → Polarity: Negative
- Noun outside negation scope → Polarity: Affirmative
- Unclear scope → Check syntactic position

If noun is within scope: Continue to Level 4
If noun is outside scope: Code as Affirmative, STOP
```

### Level 4: Validate Against Source Language

```
Verify polarity marking in source language.

Greek validation:
- οὐ/μή present with this noun? → Negative
- οὐδείς/μηδείς (no one/nothing) used? → Negative
- Negative concord pattern? → Multiple elements Negative
- Outside negation scope? → Affirmative

Hebrew validation:
- אֵין used with this noun? → Negative (special existential)
- לֹא with verb governing this noun? → Check scope
- Negative phrase structure? → Determine constituent involvement

Does source confirm noun is negated? YES/NO
```

### Level 5: Check Target Language Requirements

```
Validate against target language polarity system.

Target language questions:
1. Does target have strict negative concord?
   - If YES, ensure all constituents in scope marked Negative

2. Does target require genitive/partitive of negation?
   - If YES, polarity annotation affects case selection

3. Does target have special negative existentials?
   - If YES, use dedicated forms (not regular negation + copula)

4. Does target use NPIs in negative contexts?
   - If YES, select "any" not "some", "ever" not "always", etc.

5. Does target have negative indefinites?
   - If YES, use "nobody/nothing" forms appropriately

Final polarity code: [Affirmative or Negative with justification]
```

## Gateway Features (Correlations)

High-confidence quick predictions:

| Context | Predict | Confidence | Notes |
|---------|---------|------------|-------|
| No negation present | `Affirmative` | 98%+ | Default polarity |
| Hebrew אֵין + noun | `Negative` | 95%+ | Special negative existential |
| Greek οὐδείς/μηδείς | `Negative` | 95%+ | Negative indefinite pronouns |
| Greek οὐ/μή + verb + noun object | `Negative` | 85%+ | Noun in negation scope |
| English "no" + noun | `Negative` | 90%+ | Direct negative modifier |
| English "not...any" | `Negative` | 90%+ | NPI construction |
| Negative imperative | `Negative` | 85%+ | Prohibition affects arguments |
| Negative question (rhetorical) | Check context | 60% | May expect positive answer |

**Cross-feature correlations:**
- Negative Polarity + Interrogative → Often rhetorical questions
- Negative Polarity + Existential constructions → Special forms likely
- Negative Polarity in NC languages → Requires checking all constituents
- First Mention + Negative → Rare (check for "no X exists" meaning)

## Common Prediction Errors

### Error 1: Missing Negative Concord Requirements (~40% in NC languages)

**Problem:** Failing to mark all constituents as Negative in NC languages

**Example:**
- Spanish: "No vi a nadie" (Not saw to no-one = "I didn't see anyone")
- Wrong: Only mark verb as negative
- Right: Mark both verb AND "nadie" (no one) as Negative

**Solution:** Check if target language has strict NC, mark all elements in scope

### Error 2: Confusing Verbal vs. Constituent Negation (~25% of errors)

**Problem:** Not determining which constituents are in negation scope

**Example:**
- "Not all disciples fled" (negates "all", not "disciples")
- Wrong: Mark "disciples" as Negative
- Right: Scope is on quantifier "all", not noun itself

**Solution:** Analyze syntactic scope carefully, determine what is negated

### Error 3: Missing Special Negative Existentials (~20% in affected languages)

**Problem:** Using regular negation instead of dedicated negative existential

**Example:**
- Hebrew: אֵין (ein) "there is not" ≠ לֹא (lo) "not"
- Wrong: Translate as "it is not that there is a man"
- Right: Use special negative existential form

**Solution:** Check for dedicated negative existential words/constructions

### Error 4: Incorrect NPI Selection (~15% of errors)

**Problem:** Not using negative polarity items in negative contexts

**Example:**
- English: "I didn't see anything" (not "something")
- Wrong: "I didn't see something" (grammatically awkward/wrong meaning)
- Right: Use "anything" (NPI) in negative context

**Solution:** Identify NPIs required by target language, use in negative contexts

### Error 5: Genitive/Partitive Case Errors (~30% in Russian/Finnish)

**Problem:** Not changing case marking under negation

**Example:**
- Russian: "У меня нет книги" (genitive) not "книгу" (accusative)
- Wrong: Keep accusative case under negation
- Right: Use genitive case with negated objects

**Solution:** Check if target language requires case change under negation

## Validation Approach

**How to test polarity predictions:**

1. **Source Language Validation**
   - Greek: Check for οὐ/μή particles, οὐδείς/μηδείς
   - Hebrew: Look for אֵין (existential), לֹא (verbal), אַל (prohibitive)
   - Verify syntactic scope of negation

2. **Scope Analysis**
   - Determine which constituents are within negation scope
   - Check verb arguments (subject, object, obliques)
   - Verify negative indefinites require negation

3. **Target Language Requirements**
   - NC languages: Check all constituents in scope
   - Genitive/Partitive: Verify case changes
   - Special existentials: Confirm dedicated forms used
   - NPIs: Validate appropriate items selected

4. **Cross-Validation**
   - Negative + Existential → Check for special forms
   - Negative + Quantifier → Verify scope correctly analyzed
   - Negative + Interrogative → Check rhetorical function
   - Negative Concord → Ensure consistency across all elements

5. **Sample Testing**
   - Test 50-100 negative constructions across genres
   - Compare to TBTA gold standard
   - Check NC compliance in NC languages
   - Verify case marking in genitive-of-negation languages
   - Target: <5% error rate for polarity (binary feature)

**Error Rate Expectations:**
- Without methodology: 25-30% error rate
- With source + scope checking: <5% error rate
- NC languages without proper checking: 40-50% errors

## Language Family Patterns

**Negative Concord Languages** (strict NC):
- Slavic: Russian, Polish, Czech, Bulgarian
- Romance: Spanish, Italian, Portuguese, Romanian; French (optional)
- Greek: Ancient and Modern Greek
- Turkic: Turkish, Azerbaijani, Uzbek
- Uralic: Finnish, Hungarian (with negative auxiliary)

**Non-NC Languages** (double negation = affirmative):
- Germanic: Standard English, German, Dutch, Swedish
- Sino-Tibetan: Mandarin Chinese, Cantonese

**NPI Languages**:
- Japanese: も (mo) series NPIs
- Korean: Similar NPI system
- English: "any," "ever," "at all"

**Genitive/Partitive of Negation**:
- Russian: Direct objects → genitive under negation
- Finnish: Partitive case required
- Estonian: Similar to Finnish

**Special Negative Existentials**:
- Hebrew: אֵין (ein) "there is not"
- Russian: нет (net) "there is not"
- Turkish: yok "there is not"
- Arabic: ليس (laysa) negative copula

## Detailed Documentation

For comprehensive linguistic analysis, see:
- **[negative-concord.md](negative-concord.md)** - Detailed analysis of NC systems, cross-linguistic patterns
- **[existentials.md](existentials.md)** - Negative existential constructions, special forms
- **[npis.md](npis.md)** - Negative polarity items, licensing environments

## Summary

Polarity is critical for accurate negation across diverse language systems. The binary TBTA distinction (Affirmative/Negative) applied at constituent level captures whether nouns are affirmed or negated. Key challenges include strict negative concord languages (Spanish, Russian, Greek) requiring multiple negative markings, genitive-of-negation languages (Russian, Finnish) changing case under negation, special negative existentials (Hebrew אֵין, Russian нет), and NPI selection (English "any" vs "some"). Validation requires checking source language negation (Greek οὐ/μή, Hebrew אֵין/לֹא), determining syntactic scope, and verifying target language requirements (NC compliance, case changes, special existentials, NPI selection). Affects ~50% of languages with specialized negative systems.
