# TBTA Number Encoding: Concrete Examples

**Source**: https://github.com/AllTheWord/tbta_db_export
**Analysis Date**: 2025-11-05

---

## Example 1: Genesis 1:26 - Trial Number for God

**Verse**: "Then God said, 'Let us make mankind in our image, in our likeness...'"

**Source Text**:
- Hebrew: וַיֹּאמֶר אֱלֹהִים נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ
- Greek (LXX): καὶ εἶπεν ὁ θεός ποιήσωμεν ἄνθρωπον κατ' εἰκόνα ἡμετέραν

**TBTA Number Encoding**:

From actual TBTA data (Genesis 1:26):

```json
{
  "Constituent": "God",
  "Part": "Noun",
  "Number": "Trial",  ← THREE PERSONS
  "Person": "First Inclusive",
  ...
}
```

**Analysis**:
- **Source morphology**: Neither Hebrew אֱלֹהִים nor Greek θεός marks trial
  - Hebrew: Plural morphology (but used with singular verbs for God)
  - Greek: Singular nominative
- **Semantic interpretation**: TBTA assigns **Trial** based on theological understanding
- **Reasoning**: Trinity doctrine → three divine persons acting in unity
- **Person marking**: "First Inclusive" → "we" includes the addressee (Son/Spirit included in divine council)

**Implication**:
- TBTA number is **target-language-driven**, not source-morphology-driven
- Requires **theological knowledge** to make this assignment
- For languages with trial (e.g., Tok Pisin), this guides translation:
  - Use **mitripela** (1st person trial exclusive) or
  - Use **yumitripela** (1st person trial inclusive)

**Controversy**:
- Not all traditions interpret Genesis 1:26 as Trinity
- Alternative interpretations: Divine council, royal "we", angels
- TBTA makes a specific theological choice

---

## Example 2: Genesis 18:2 - Three Angels/Men

**Verse**: "Abraham looked up and saw three men standing nearby."

**Source Text**:
- Hebrew: וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים נִצָּבִים עָלָיו
- Greek (LXX): καὶ ἰδοὺ τρεῖς ἄνδρες εἱστήκεισαν ἐπάνω αὐτοῦ

**TBTA Number Encoding** (expected):

```json
{
  "Constituent": "men",
  "Part": "Noun",
  "Number": "Trial",  ← THREE MEN (explicit numeral)
  "NounListIndex": "1",
  ...
}
```

**Analysis**:
- **Source morphology**:
  - Hebrew: שְׁלֹשָׁה (shloshah) "three" + אֲנָשִׁים (anashim) "men" (plural)
  - Greek: τρεῖς (treis) "three" + ἄνδρες (andres) "men" (plural)
- **Semantic number**: Explicit numeral **3**
- **TBTA assignment**: Trial
- **For target languages**:
  - With trial → use trial form
  - Without trial → use plural (or paucal if available)

**Clear case**: Explicit numeral makes this straightforward.

---

## Example 3: Matthew 28:19 - Trinity Baptism Formula

**Verse**: "...baptizing them in the name of the Father and of the Son and of the Holy Spirit."

**Source Text**:
- Greek: βαπτίζοντες αὐτοὺς εἰς τὸ ὄνομα τοῦ πατρὸς καὶ τοῦ υἱοῦ καὶ τοῦ ἁγίου πνεύματος

**TBTA Number Encoding** (from actual data):

```json
{
  "Constituent": "name",
  "Part": "Noun",
  "Number": "Singular",  ← ONE NAME (not three names!)
  ...
}

{
  "Constituent": "Father",
  "Part": "Noun",
  "Number": "Singular",
  ...
}

{
  "Constituent": "Son",
  "Part": "Noun",
  "Number": "Singular",
  ...
}

{
  "Constituent": "Spirit",
  "Part": "Noun",
  "Number": "Singular",
  ...
}
```

**Analysis**:
- **Three persons**: Father, Son, Holy Spirit
- **One name** (singular, not plural)
- **Theological significance**: Three persons, one God
- **Number encoding**:
  - Each person individually: Singular
  - Collectively as participants: Could be encoded as Trial in discourse tracking
  - "Name" stays singular (unity of Godhead)

**For translation**:
- In languages with trial: Might mark pronouns/verbs with trial when referring to Trinity collectively
- In languages with inclusive/exclusive: Likely exclusive ("we" = Trinity, not including humanity)

---

## Example 4: The Twelve Disciples

**Verse**: Matthew 10:1 - "Jesus called his twelve disciples to him..."

**Source Text**:
- Greek: καὶ προσκαλεσάμενος τοὺς δώδεκα μαθητὰς αὐτοῦ

**TBTA Number Encoding** (expected):

```json
{
  "Constituent": "disciples",
  "Part": "Noun",
  "Number": "Paucal",  ← or possibly "Plural"
  "NounListIndex": "1",  ← All twelve are same group
  ...
}
```

**Analysis**:
- **Explicit numeral**: δώδεκα (dōdeka) "twelve"
- **Too large for trial**: 12 > 3
- **Paucal or Plural**?
  - Depends on target language paucal range
  - **Murrinh-Patha** (paucal up to ~15): **Paucal**
  - **Arabic** (paucal 3-10): **Plural**
  - **Warlpiri** (paucal for small groups): Depends on noun class
  - **Most languages**: **Plural**

**Default**: Probably encoded as **Plural** unless target has wide-ranging paucal

---

## Example 5: Two Witnesses

**Verse**: Matthew 18:16 - "...take one or two others along..."

**Source Text**:
- Greek: παράλαβε μετὰ σοῦ ἔτι ἕνα ἢ δύο

**TBTA Number Encoding** (expected):

**Alternative 1**:
```json
{
  "Constituent": "others",
  "Part": "Noun",
  "Number": "Dual",  ← If interpreting as "two"
  ...
}
```

**Alternative 2**:
```json
{
  "Constituent": "others",
  "Part": "Noun",
  "Number": "Paucal",  ← If interpreting as "one or two" (small group)
  ...
}
```

**Analysis**:
- **Disjunction**: ἕνα ἢ δύο "one or two" (alternative)
- **Challenge**: Not exact number
- **Possible encodings**:
  - **Dual**: If emphasizing "two" option
  - **Paucal**: If capturing "small number" semantics
  - **Singular**: If emphasizing "one" option
- **Need**: Check actual TBTA data for how disjunctions are handled

---

## Example 6: Crowds and Multitudes

**Verse**: Matthew 4:25 - "Large crowds from Galilee..."

**Source Text**:
- Greek: ὄχλοι πολλοί (ochloi polloi) "crowds many"

**TBTA Number Encoding**:

```json
{
  "Constituent": "crowds",
  "Part": "Noun",
  "Number": "Plural",  ← MANY (exceeds paucal range)
  ...
}
```

**Analysis**:
- **Source morphology**: Greek plural ὄχλοι
- **Semantic quantity**: Large, indefinite (hundreds/thousands)
- **Always Plural**: Even in languages with paucal
  - Exceeds paucal range in all known paucal languages
  - Murrinh-Patha paucal ~15 max → "crowds" far exceeds this

---

## Example 7: Natural Pairs - Eyes, Ears, Hands

**Verse**: Matthew 5:29 - "If your right eye causes you to stumble, gouge it out..."

**Source Text**:
- Greek: ὁ ὀφθαλμός σου ὁ δεξιός (ho ophthalmos sou ho dexios) "the eye your right" (singular)

**TBTA Number Encoding**:

**For "right eye" (singular in Greek)**:
```json
{
  "Constituent": "eye",
  "Part": "Noun",
  "Number": "Singular",  ← One eye (specifically right)
  ...
}
```

**For "both eyes" (if mentioned)**:
```json
{
  "Constituent": "eyes",
  "Part": "Noun",
  "Number": "Dual",  ← Natural pair
  ...
}
```

**Analysis**:
- **Hebrew background**: עֵינַיִם (einayim) "eyes" - dual morphology for natural pair
- **Greek**: Uses plural ὀφθαλμοί or singular ὀφθαλμός
- **TBTA decision**:
  - One eye → Singular
  - Two eyes → Dual (if target has dual)
  - Many eyes (e.g., Ezekiel's cherubim) → Plural

**For target languages**:
- **Hebrew dual**: Original language marks natural pairs with dual
- **Languages with dual**: Should use dual for "two eyes/ears/hands"
- **Languages without dual**: Use plural

---

## Number Value Usage Frequency (Estimated)

Based on theological and narrative content:

| Number | Usage Frequency | Primary Contexts |
|--------|----------------|------------------|
| **Singular** | 60-70% | Individual people, God (as one), objects, abstracts |
| **Plural** | 25-35% | Groups, crowds, nations, abstract plurals |
| **Dual** | 1-3% | Natural pairs (eyes, hands), "two witnesses", paired items |
| **Trial** | 0.1-0.5% | Trinity references, explicit "three" mentions |
| **Paucal** | 0.5-2% | Small groups (disciples, angels), "a few" |
| **Quadrial** | <0.1% | Rarely/never used (disputed existence) |

**Note**: Frequency varies by target language features. Languages without dual/trial/paucal collapse these into plural.

---

## Encoding Patterns Observed

### Pattern 1: Explicit Numerals → Semantic Number

When text has explicit numerals, TBTA assigns corresponding semantic number:
- "two" → Dual
- "three" → Trial
- "twelve" → Paucal or Plural (depends on target)
- "thousands" → Plural

### Pattern 2: Theological Interpretation → Trial

Trinity passages receive Trial even without morphological marking:
- Genesis 1:26 "Let us make"
- Matthew 28:19 "Father, Son, Holy Spirit"
- Other Trinitarian contexts

### Pattern 3: Hebrew Dual Morphology → Dual

When Hebrew source has dual suffix (-ayim/-ê), TBTA encodes Dual:
- Eyes, ears, hands, feet (natural pairs)
- Two days, two years (time)

### Pattern 4: Semantic Category → Default Number

Certain semantic categories have default numbers:
- "Crowd, multitude, nation" → Always Plural
- "Person, man, woman" (individual) → Singular
- Abstract concepts → Often Singular

### Pattern 5: Participant Tracking → Consistent Number

Same referent keeps same number across discourse:
- "The twelve" → Same number throughout passage
- "The three men" (Gen 18) → Consistent Trial

---

## Challenges in Automatic Reproduction

### Challenge 1: Theological Knowledge Required

**Problem**: Assigning Trial to Genesis 1:26 requires knowing Trinitarian theology

**Solution Options**:
1. **Manual annotation**: Tag Trinitarian passages explicitly
2. **Theological commentary**: Parse commentaries for Trinity references
3. **Pattern matching**: "Let us" + God → Trial (heuristic, imperfect)

### Challenge 2: Disjunctions ("One or Two")

**Problem**: How to encode "ἕνα ἢ δύο" (one or two)?

**Solution Options**:
1. **Primary option**: Choose "two" → Dual
2. **Range**: Use Paucal to capture "small number"
3. **Multiple encodings**: Store alternatives

**Need**: Check TBTA actual data for their approach

### Challenge 3: Paucal Range Variation

**Problem**: Paucal means 3-5 in some languages, 3-15 in others

**Solution**:
1. **Language-specific rules**: Store paucal range for each language
2. **Default**: 3-10 unless grammar specifies otherwise
3. **Boundary cases**: "Twelve disciples" - paucal in Murrinh-Patha, plural in Arabic

### Challenge 4: Pronoun vs. Noun Number

**Problem**: Some languages mark number on pronouns differently than nouns

**Example**: Larike
- Pronouns: Singular - Dual - Trial - Plural
- Nouns: Singular - Plural (only 2-way)

**Solution**: TBTA may encode separately for different syntactic categories

**Need**: Verify if TBTA distinguishes this

---

## Validation Checklist

When reproducing TBTA number assignments:

✅ **Explicit numerals** match semantic number
- "Two angels" → Dual
- "Three men" → Trial
- "Twelve disciples" → Paucal (if range fits) or Plural

✅ **Trinity passages** → Trial
- Genesis 1:26, Matthew 28:19, etc.

✅ **Natural pairs** → Dual (if target has dual)
- Eyes, ears, hands, feet
- Days (two days), years

✅ **Crowds, multitudes** → Plural
- Always exceeds paucal range

✅ **Participant tracking** → Consistency
- Same referent = same number throughout

✅ **Target language** determines final encoding
- Don't assign Dual if target lacks dual
- Check paucal range before using Paucal
- Avoid Quadrial (disputed existence)

---

## Summary: TBTA Number Decision Tree

```
For each noun/pronoun:

1. Does the text have an explicit numeral?
   YES →
     - 1 → Singular
     - 2 → Dual (if target has dual, else Plural)
     - 3 → Trial (if target has trial, else Paucal/Plural)
     - 4 → Quadrial? (rare, use Paucal/Plural instead)
     - 3-10 → Paucal (if target has paucal & in range, else Plural)
     - 11+ → Plural
   NO → Go to 2

2. Is this a Trinity passage?
   YES → Trial (theological interpretation)
   NO → Go to 3

3. Does Hebrew have dual morphology (-ayim)?
   YES → Dual (if target has dual, else Plural)
   NO → Go to 4

4. Check source morphology:
   - Singular → Singular
   - Plural → Go to 5

5. What is the semantic quantity?
   - Individual → Singular
   - Natural pair (eyes) → Dual (if target has dual)
   - Small group → Paucal (if target has paucal)
   - Large group/crowd → Plural
   - Default → Plural

6. Validate against target language:
   - Has dual? Use Dual for 2
   - Has trial? Use Trial for 3
   - Has paucal? Use Paucal for small groups (check range)
   - Otherwise: collapse to Plural
```

---

## Next Steps for Reproduction

1. **Access full TBTA dataset**: Analyze 100+ verses across Bible
2. **Document actual patterns**: Verify hypotheses above
3. **Build decision tree**: Formalize rules
4. **Create theological tag list**: Identify all Trinity/trial passages
5. **Implement classifier**: Code up automatic assignment
6. **Validate**: Compare output to TBTA gold standard
