# Verb Reflexivity (TBTA Verb Position 7)

**Target Audience:** Bible translators, linguists, pastors working with languages that require reflexive marking

**Primary Use Case:** When translating verbs into Romance, Slavic, or other languages with reflexive pronouns/particles, translators need to know whether the verb's action affects the subject itself (reflexive) or another entity (non-reflexive). Without this distinction, translators may omit required reflexive pronouns or incorrectly add them where inappropriate.

---

## Purpose

### What is Reflexivity?

Reflexivity is a grammatical property that indicates whether a verb's action loops back to affect the subject itself:

- **Not Reflexive (N)**: Action affects someone/something else → "He washed the disciples' feet"
- **Reflexive**: Action affects the subject itself → "He washed himself" or "He sat down"

TBTA further distinguishes between two types of reflexive constructions:

- **Reflexive Intransitive (R)**: Verb becomes intransitive, subject-focused → "arise," "sit down," "turn around"
- **Reflexive Transitive (r)**: Verb retains object but action returns to subject → "wash oneself," "prepare oneself," "defend oneself"

### Why It Matters for Translation

Many languages **require** explicit reflexive marking that doesn't exist in English glosses:

**Spanish Example:**
- Non-reflexive: "lavó los pies" (he washed the feet)
- Reflexive: "se lavó" (he washed himself)
- Missing "se" = grammatical error

**Russian Example:**
- Non-reflexive: "он готовил еду" (he prepared food)
- Reflexive: "он готовился" (he prepared himself - with -ся suffix)
- Wrong suffix = wrong meaning

**French Example:**
- Non-reflexive: "il lève la main" (he raises his hand)
- Reflexive: "il se lève" (he gets up - lit. "he raises himself")
- Missing "se" = incomplete sentence

### Translation Errors Prevented

**Error Type 1: Missing Reflexive Pronoun**
- ❌ *French*: "Il assis" (incorrect - missing reflexive)
- ✅ *French*: "Il s'assit" (correct - "He sat down")

**Error Type 2: Incorrect Reflexive Addition**
- ❌ *Spanish*: "Él se lavó los pies de los discípulos" (incorrect - implies washing his own feet)
- ✅ *Spanish*: "Él lavó los pies de los discípulos" (correct - washing others' feet)

**Error Type 3: Wrong Voice/Form**
- ❌ *Greek translation to Russian*: Using active voice instead of middle voice equivalent
- ✅ Using reflexive particle (-ся) to approximate Greek middle voice meaning

---

## Methodology

### Phase 1: Data Extraction

Reflexivity is **explicitly encoded** in TBTA data - no prediction needed.

**Location in TBTA Data:**
```python
# Found at: clauses[i]['children'][VP_index]['children'][verb_index]['Reflexivity']
def extract_reflexivity(verse_yaml):
    """
    Extract reflexivity from verb in TBTA YAML structure

    Returns: 'N' (Not Reflexive), 'R' (Reflexive intransitive),
             'r' (Reflexive transitive), or None
    """
    for clause in verse_yaml.get('clauses', []):
        for child in clause.get('children', []):
            # Find Verb Phrase (VP) nodes
            if child.get('Part') == 'VP':
                for verb in child.get('children', []):
                    if verb.get('Part') == 'Verb':
                        reflexivity = verb.get('Reflexivity')
                        if reflexivity:
                            return reflexivity
    return None
```

**Context Required:** Verse-level (individual verb basis)

**Example Extraction:**
```yaml
# John 13:4 - "Jesus... girded himself with a towel"
verse: JHN.013.004
clauses:
  - children:
      - Part: VP
        children:
          - Constituent: gird
            Part: Verb
            Reflexivity: r           # ← Reflexive transitive
            Time: Historic Past
            Aspect: Unmarked
            Mood: Indicative
```

### Phase 2: Interpretation (No Prediction Needed)

Since reflexivity is explicit in TBTA, no prediction algorithm is required. However, understanding the distinction helps with application:

**Decision Tree for Application:**

1. **Value = N (Not Reflexive)**
   - Use normal transitive/intransitive verb form
   - No reflexive pronoun needed
   - Action affects external object or no object

2. **Value = R (Reflexive Intransitive)**
   - Verb becomes subject-focused
   - Often motion/position verbs (sit, arise, turn)
   - Romance: Use reflexive pronoun + intransitive verb
   - Slavic: Add reflexive particle -ся/-się
   - Greek: Often corresponds to middle voice

3. **Value = r (Reflexive Transitive)**
   - Verb retains transitive structure but action returns to subject
   - Often grooming/preparation verbs (wash, clothe, prepare)
   - Romance: Use reflexive pronoun + transitive verb
   - Slavic: Add reflexive particle -ся/-się
   - English: May add "oneself" for clarity

### Phase 3: Validation

**Accuracy:** Explicit data (100% accurate to TBTA encoding)

**Critical Validation Rules:**
- [ ] Value must be one of: N, R, r
- [ ] Reflexive verbs (R/r) should correlate with Greek middle voice or Hebrew Niphal/Hithpael stems
- [ ] Not Reflexive (N) is the default for most verbs

**Cross-Feature Consistency:**
- Check against source language morphology (Greek voice, Hebrew stem)
- Verify semantic appropriateness (is action logically reflexive?)
- Compare with Surface Realization (does pronoun support reflexive reading?)

---

## Output Schema

**File Location:**
```
.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml
```

**YAML Structure:**
```yaml
verse: JHN.013.004
clauses:
  - children:
      - Part: VP
        children:
          - Constituent: gird
            Part: Verb
            Reflexivity: r
            Time: Historic Past
            Aspect: Unmarked
            Mood: Indicative
            Polarity: Affirmative
```

### Examples from Scripture

#### Example 1: Reflexive Transitive (r) - "Gird Oneself"

**John 13:4** - "He... girded himself with a towel"

```yaml
Constituent: gird
Reflexivity: r        # Reflexive transitive
```

**Translation Applications:**
- **Spanish**: "se ciñó con una toalla" (reflexive pronoun "se")
- **French**: "il se ceignit d'un linge" (reflexive pronoun "se")
- **Russian**: "он опоясался полотенцем" (-ся reflexive suffix)
- **German**: "er gürtete sich mit einem Schurztuch" (reflexive pronoun "sich")
- **Greek source**: περιεζώσατο (middle voice - action for oneself)

**Why it matters:** Without reflexive marking, these languages would suggest Jesus girded *someone else*, not himself.

---

#### Example 2: Reflexive Intransitive (R) - "Sit Down"

**Luke 22:14** - "He sat down, and the apostles with him"

```yaml
Constituent: sit
Reflexivity: R        # Reflexive intransitive
```

**Translation Applications:**
- **Spanish**: "se sentó" (reflexive "se" + sentar)
- **French**: "il s'assit" (reflexive "s'" + asseoir)
- **Italian**: "si sedette" (reflexive "si" + sedere)
- **Russian**: "он сел" (perfective verb, inherently reflexive)
- **German**: "er setzte sich" (reflexive "sich")

**Why it matters:** In Romance languages, "sit" without reflexive pronoun is transitive (= "to seat someone"). The reflexive makes it intransitive (= "to seat oneself/sit down").

---

#### Example 3: Not Reflexive (N) - "Wash Another's Feet"

**John 13:5** - "He began to wash the disciples' feet"

```yaml
Constituent: wash
Reflexivity: N        # Not reflexive
```

**Translation Applications:**
- **Spanish**: "lavó los pies" (NO reflexive - action on others)
- **French**: "il lava les pieds" (NO reflexive)
- **Russian**: "он умыл ноги" (NO -ся suffix)
- **German**: "er wusch die Füße" (NO reflexive pronoun)

**Contrast with:** "He washed himself" → Reflexivity: r
- Spanish: "se lavó"
- French: "il se lava"
- Russian: "он умылся" (with -ся)

**Why it matters:** Using reflexive here would change meaning to "He washed himself" instead of "He washed the disciples' feet."

---

#### Example 4: Reflexive Transitive (r) - "Prepare Oneself"

**1 Peter 1:13** - "Gird up the loins of your mind"

```yaml
Constituent: prepare
Reflexivity: r        # Reflexive transitive (metaphorical)
```

**Translation Applications:**
- **Spanish**: "ceñid vuestros lomos" → "preparaos" (reflexive imperative)
- **French**: "ceignez les reins de votre intelligence" → "préparez-vous"
- **Russian**: "препояшьте чресла" → "приготовьтесь" (with -ся)

**Why it matters:** The command is to prepare *oneself*, not to prepare something external. Reflexive marking makes this clear.

---

#### Example 5: Reflexive Intransitive (R) - "Turn Around"

**Mark 8:33** - "He turned around and looked at his disciples"

```yaml
Constituent: turn
Reflexivity: R        # Reflexive intransitive
```

**Translation Applications:**
- **Spanish**: "se volvió" (reflexive pronoun obligatory)
- **French**: "il se tourna" (reflexive pronoun obligatory)
- **Italian**: "si voltò" (reflexive pronoun obligatory)
- **Russian**: "он обернулся" (verb with -ся)
- **German**: "er wandte sich um" (reflexive "sich")

**Why it matters:** Without reflexive, "turn" could mean "to turn something" rather than "to turn oneself around."

---

## Language-Specific Applications

### Romance Languages (Spanish, French, Italian, Portuguese, Romanian)

**Obligatory reflexive pronouns:** me, te, se (Spanish/French/Italian)

**Key verbs requiring reflexives:**
- sentarse (sit down), levantarse (get up), volverse (turn around)
- lavarse (wash oneself), vestirse (dress oneself), prepararse (prepare oneself)

**Application:**
- R or r → Use reflexive pronoun (se sentó, il s'assit, si sedette)
- N → No reflexive pronoun

---

### Slavic Languages (Russian, Polish, Czech, Ukrainian, Bulgarian)

**Reflexive particle:** -ся/-сь (Russian), się (Polish)

**Examples:**
- мыть → мыться (wash → wash oneself)
- готовить → готовиться (prepare → prepare oneself)
- садиться (sit down - inherently reflexive)

**Application:**
- R or r → Add -ся/-сь or się suffix
- N → No reflexive suffix

---

### Germanic Languages (German, Dutch, Afrikaans)

**Reflexive pronoun:** sich (German), zich (Dutch)

**Examples:**
- Er setzte sich (He sat down) - needs "sich"
- Er wusch die Füße (He washed the feet) - no "sich"

**Application:**
- R or r → Use sich/zich
- N → No reflexive pronoun

---

### Greek Source Text Correlation

**Greek Middle Voice ≈ TBTA Reflexive**

Greek voices:
1. Active: Subject acts on external object
2. Middle: Subject acts on/for itself (reflexive/benefactive)
3. Passive: Subject receives action

**TBTA mapping:**
- Greek middle voice → Often R or r in TBTA
- Helps identify NT verbs needing reflexive marking

---

### Hebrew Source Text Correlation

**Hebrew reflexive stems:**
1. **Niphal**: Passive/reflexive/reciprocal (multiplex meaning)
2. **Hithpael**: Primarily reflexive/reciprocal

**TBTA disambiguation:**
- Niphal → R/r if reflexive, N if passive
- Hithpael → Usually R or r
- Clarifies ambiguous Hebrew verb stems for target language

---

## Related Features

### Correlates with Greek Voice

**Strong correlation:**
- Greek Middle Voice → TBTA R or r (reflexive)
- Greek Active Voice → TBTA N (not reflexive)
- Greek Passive Voice → TBTA N (usually, unless reflexive passive)

**Use case:** When translating into languages with voice distinctions (like Greek's middle voice), TBTA reflexivity helps map source to target.

---

### Correlates with Hebrew Verb Stems

**Correlation patterns:**
- Hebrew Hithpael → TBTA R or r
- Hebrew Niphal → May be R/r (reflexive) or N (passive)
- Hebrew Qal → Usually N

**Use case:** Disambiguates multiplex Hebrew stems for clearer target language rendering.

---

### Interaction with Surface Realization

**Related feature:** Surface Realization (Noun/Pronoun/Zero)

If a verse has:
- Reflexivity: r
- Surface Realization: Pronoun

This indicates an explicit reflexive pronoun in the source text (e.g., "himself," "themselves").

**Use case:** Helps identify when reflexive is explicit in source vs. implicit in verb morphology.

---

### Integration with Macula Data

**Macula provides:**
- Greek voice (Active/Middle/Passive)
- Hebrew stem (Qal/Niphal/Hithpael/etc.)
- Lemma and morphology

**TBTA provides:**
- Cross-linguistic reflexivity classification
- Intransitive vs. transitive reflexive distinction

**Combined use:**
1. Check Macula for source language voice/stem
2. Check TBTA for target language reflexivity requirement
3. Map source morphology to target language construction

**Example workflow:**
```
Macula: Greek middle voice (ἐστράφη)
TBTA: Reflexivity R (intransitive reflexive)
Target (Spanish): Use "se volvió" (reflexive pronoun + preterite)
```

---

## Frequency and Coverage

**Expected Distribution:**
- N (Not Reflexive): 85-90% - Most verbs
- R (Intransitive): 5-8% - Motion verbs (sit, arise, turn)
- r (Transitive): 5-7% - Grooming verbs (wash, clothe, prepare)

**High-Priority Languages (Obligatory reflexive):**
- Spanish (110M), French (80M), Russian (150M), Portuguese (220M), Italian (60M), German (90M), Polish (40M)

**Total Impact:** 750M+ Bible users in languages requiring reflexive information

---

## Translation Workflow Integration

**When to check reflexivity:**
1. Parse source text syntax
2. Check TBTA reflexivity for each verb
3. Apply target language reflexive rules

**Key questions:**
- Does target language require reflexive marking? → Consult TBTA for every verb
- TBTA says "R" but no reflexive in English? → Add reflexive in target (Greek/Hebrew encode in morphology)
- R vs. r difference? → R = intransitive (sit, arise), r = transitive (wash oneself, prepare oneself)

---

## Limitations and Edge Cases

**1. Reflexivity vs. Reciprocity**
- TBTA doesn't distinguish reflexive ("they washed themselves") from reciprocal ("they washed one another")
- Solution: Check Greek ἑαυτούς (reflexive) vs. ἀλλήλους (reciprocal), or Hebrew context

**2. Middle Voice Ambiguity**
- Greek middle voice = reflexive, benefactive, or deponent (active meaning)
- TBTA may mark all as R/r
- Solution: Consult Greek grammar for semantic nuance

**3. Passive-Reflexive Overlap**
- Some languages use reflexive for passive (Spanish "se habla" = "is spoken")
- TBTA focuses on true reflexive
- Solution: Target language may need passive construction instead

**4. Inherently Reflexive Verbs**
- Some verbs always reflexive in target language (Spanish "quejarse," French "se souvenir")
- TBTA marks based on Greek/Hebrew source
- Solution: Target language lexicon determines final form

---

## Summary

**Reflexivity is critical for accurate Bible translation because:**

1. **Grammatical Requirement**: 750M+ speakers in languages with obligatory reflexive marking
2. **Meaning Distinction**: Prevents errors like "washed the feet" vs. "washed himself"
3. **Voice Mapping**: Helps translate Greek middle voice and Hebrew reflexive stems
4. **Cross-linguistic Consistency**: Provides unified reflexivity marking across languages

**Key Takeaways:**
- **N (Not Reflexive)**: Default, no special marking needed (85-90% of verbs)
- **R (Reflexive Intransitive)**: Motion/position verbs requiring reflexive pronouns (5-8%)
- **r (Reflexive Transitive)**: Grooming/preparation verbs requiring reflexive pronouns (5-7%)
- **Explicit in TBTA**: No prediction needed, direct extraction from YAML data
- **High accuracy**: Directly encoded by TBTA linguistic experts

**For tool developers:** Implement extraction function to pull Reflexivity field from VP → Verb nodes

**For translators:** Consult reflexivity for every verb when working in Romance, Slavic, or Germanic target languages

---

**Document Status:** Complete
**Lines:** 496
**Last Updated:** 2025-11-05
**Source:** TBTA Official Documentation + Cross-linguistic Analysis
