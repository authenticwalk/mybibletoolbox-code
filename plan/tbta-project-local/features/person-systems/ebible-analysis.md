# Person Systems: Clusivity - eBible Local Analysis

## Feature States Tested

**Feature**: First Person Plural Clusivity
- **Inclusive "we"**: Speaker + addressee(s) + possibly others ("we including you")
- **Exclusive "we"**: Speaker + others, but NOT addressee ("we but not you")

**Additional encoding**: Trial Number (exactly 3)
- Relevant for Genesis 1:26 where God (Trinity) speaks

## Verse Selection

### Verse 1: Genesis 1:26
**Why chosen**: Classic example of First Person Inclusive with Trial number (Trinity)
- God says "Let us make" - the "us" is the Trinity addressing each other
- Languages with clusivity must choose inclusive vs exclusive
- Languages with trial number can mark exactly 3 persons

**Sparse-checkout**: Already available at `commentary/GEN/001`

### Verse 2: Acts 15:25 (future analysis)
**Why chosen**: Shows First Person Exclusive
- Apostles writing to churches: "we" = apostles (exclusive), NOT including recipients

### Verse 3: John 11:7 (future analysis)
**Why chosen**: Jesus speaking to disciples
- "Let us go" - inclusive (Jesus + disciples)

## Languages Analyzed

1. **Tagalog (tgl)**: Philippine language with explicit clusivity
   - `tayo` = inclusive we
   - `kami` = exclusive we

2. **Indonesian (ind)**: Austronesian language with clusivity
   - `kita` = inclusive we
   - `kami` = exclusive we

3. **Swahili (swh)**: Bantu language with some clusivity marking
   - `tu-` prefix patterns

4. **English (eng)**: Control language - NO clusivity marking
   - "we/us" is ambiguous

## Analysis by Verse

### Genesis 1:26 - "Let us make mankind"

#### Source (Hebrew)
Hebrew: נַֽעֲשֶׂ֥ה (na'aseh) - "let us make" (cohortative plural)
- Grammatically plural first person
- Hebrew does NOT mark clusivity or trial number
- The plurality is theologically interpreted as Trinity

#### Translations

**Tagalog (tgl-ULB)**:
```
Sinabi ng Diyos, "Gawin natin ang tao ayon sa ating wangis, ayon sa ating
larawan. Hayaan silang mamahala sa isda sa dagat..."
```
- **Analysis**: Uses "**natin**" (genitive form of *tayo*)
- **Grammatical form**: `tayo` = First Person Plural INCLUSIVE
- **Number**: Plural (Tagalog doesn't have grammatical trial)
- **Clusivity**: INCLUSIVE - implies the Trinity members are addressing each other
- **Interpretation**: The "us" includes all members of the Trinity being spoken to

**Indonesian (ind-ind)**:
```
Kemudian Allah berkata, "Marilah Kita menciptakan manusia supaya menyerupai
Kita dan mencerminkan sifat-sifat Kita..."
```
- **Analysis**: Uses "**Kita**" (capitalized for deity)
- **Grammatical form**: `kita` = First Person Plural INCLUSIVE
- **Clusivity**: INCLUSIVE - members of Trinity addressing each other
- **Note**: Consistently uses `Kita` three times, reinforcing the inclusive reading

**Swahili (swh-ONEN)**:
```
Ndipo Mungu akasema, "Tufanye mtu kwa mfano wetu, kwa sura yetu..."
```
- **Analysis**: Uses "**Tu-**" prefix on verb "fanye" (make)
- **Grammatical form**: `tu-` = First Person Plural (generally inclusive in discourse)
- **Clusivity**: Likely INCLUSIVE based on context
- **Note**: Swahili doesn't mark clusivity as explicitly as Tagalog/Indonesian

**English (eng-LSV)**:
```
And God says, "Let Us make man in Our image, according to Our likeness..."
```
- **Analysis**: Uses "**Us**" and "**Our**"
- **Grammatical form**: First Person Plural - ambiguous
- **Clusivity**: NOT MARKED - English cannot distinguish inclusive/exclusive
- **Interpretation**: Theological tradition interprets as Trinity, but grammar doesn't encode it

**English (eng-KJVCPB)**:
```
And God said, Let us make man in our image, after our likeness...
```
- **Analysis**: Same as eng-LSV
- **Clusivity**: NOT MARKED

**German (deu-TKW)**:
```
Da sprach Gott: Laßt uns Menschen machen nach unserem Bilde, uns ähnlich...
```
- **Analysis**: Uses "**uns**" (us, dative/accusative) and "**unserem**" (our, dative)
- **Grammatical form**: First Person Plural - ambiguous
- **Clusivity**: NOT MARKED - German lacks clusivity distinction
- **Note**: Similar to English in ambiguity

#### TBTA Annotation

From `.data/commentary/GEN/001/026/GEN-001-026-tbta.yaml`:

```yaml
- Constituent: God
  LexicalSense: A
  NounListIndex: '1'
  Part: Noun
  SemanticComplexityLevel: '1'
  Number: Trial              # ← Exactly 3 persons!
  Participant Tracking: Routine
  Person: First Inclusive     # ← Inclusive!
  Polarity: Affirmative
  Surface Realization: Noun
```

**Key TBTA encoding**:
1. **Number: Trial** - Exactly 3 persons (Trinity)
2. **Person: First Inclusive** - "We" includes all persons being addressed

**Validation**: ✅ **PERFECT MATCH**

The TBTA encoding aligns with:
- Tagalog's choice of `tayo` (inclusive)
- Indonesian's choice of `kita` (inclusive)
- Theological interpretation of Trinity addressing each other

## Cross-Language Patterns

### Pattern 1: Clusivity-Marking Languages Agree on INCLUSIVE

**Languages**: Tagalog, Indonesian
**Consensus**: Both explicitly choose INCLUSIVE forms
- Tagalog: `natin` (from `tayo`)
- Indonesian: `Kita`

**Reasoning**:
- The context is God addressing God (Trinity)
- "Let us make" = members of Trinity proposing action TO each other
- Therefore: inclusive ("we including you [other Trinity members]")
- NOT exclusive ("we but not you")

### Pattern 2: Non-Clusivity Languages Show Ambiguity

**Languages**: English, German
**Pattern**: Use generic plural pronouns that don't distinguish
- English: "us/our"
- German: "uns/unserem"

**Implication**: Translators working in clusivity-marking languages MUST make an interpretive choice that English/German translators never face

### Pattern 3: Swahili's Intermediate Position

**Language**: Swahili
**Pattern**: Uses `tu-` prefix which is generally inclusive in discourse
**Note**: Swahili doesn't mark clusivity as rigidly as Austronesian languages, but discourse patterns favor inclusive reading here

## TBTA Validation

### What TBTA Got Right

1. ✅ **Person: First Inclusive** - Correctly identified the clusivity
   - Matches Tagalog explicit grammar
   - Matches Indonesian explicit grammar
   - Represents the theological interpretation that clusivity-marking languages must encode

2. ✅ **Number: Trial** - Correctly identified exactly 3 persons
   - This is implicit in Hebrew (plural could be 2+)
   - Made explicit for languages with trial number systems
   - Theologically accurate (Trinity)

### What TBTA Encoded That Isn't Surface-Visible

1. **Trial number**: Hebrew only shows plural, not specific count
   - TBTA made explicit: "3 persons" (Trinity)
   - Helps translators in languages with dual/trial/paucal/plural distinctions

2. **Clusivity**: Hebrew doesn't mark inclusive/exclusive
   - TBTA made explicit: "First Inclusive"
   - Helps translators in ~700+ languages with clusivity

### Why This Matters

**For translators into Austronesian languages**:
- MUST choose between two grammatically distinct forms
- Wrong choice = grammatically incorrect or theologically misleading

**Example error scenarios**:
- ❌ Using `kami` (exclusive) would imply God is speaking to someone OUTSIDE the Trinity
- ✅ Using `tayo/kita` (inclusive) correctly represents intra-Trinitarian speech

## Theological Implications

### Trinity Doctrine and Clusivity

The choice of INCLUSIVE in Genesis 1:26 has theological weight:

1. **Confirms plurality within Godhead**
   - "We" is not royal plural (that would be exclusive)
   - "We" includes the persons being addressed

2. **Supports Trinitarian interpretation**
   - Number: Trial (3) aligns with Father, Son, Holy Spirit
   - Person: Inclusive aligns with mutual indwelling

3. **Contrasts with other "we" passages**
   - When God says "we" to angels → exclusive (God + angels, not addressing angels)
   - When God says "we" within Trinity → inclusive (as here)

## Recommendations

### For Translators Working in Clusivity Languages

**When encountering Genesis 1:26**:
1. ✅ **Use INCLUSIVE form** (`tayo`, `kita`, etc.)
2. ✅ If your language has trial number, **use trial**
3. ✅ Add footnote explaining Trinitarian interpretation if culturally unfamiliar

**Common pitfalls to avoid**:
1. ❌ Don't use exclusive form (implies God speaking to non-divine audience)
2. ❌ Don't use dual number if available (Trinity is 3, not 2)
3. ❌ Don't default to indefinite plural (obscures the specific "3 persons")

### For AI Systems Assisting Translation

**Key context needed**:
1. Target language's clusivity system (if any)
2. Target language's number system (singular/dual/trial/plural/etc.)
3. Theological context (Trinity doctrine)
4. Discourse participants (God addressing God)

**Prediction heuristic**:
```
IF target_language.has_clusivity:
    IF speaker == God AND addressee == God:
        USE inclusive_form
    ELIF speaker == God AND addressee == humans:
        USE exclusive_form (usually)
```

## Data Files Referenced

- **TBTA**: `.data/commentary/GEN/001/026/GEN-001-026-tbta.yaml`
- **eBible**: `.data/commentary/GEN/001/026/GEN.001.026-translations-ebible.yaml`
- **Macula**: (Not analyzed in this document, but available)

## Coverage

- **Verse fragments tested**: 1 (Genesis 1:26)
- **Languages analyzed**: 6 (Tagalog, Indonesian, Swahili, English-2, German)
- **Language families**: Austronesian (2), Bantu (1), Germanic (3)
- **Feature states confirmed**: Inclusive (demonstrated), Exclusive (pending Acts 15:25)
- **Data points**: 6 translations analyzed

## Next Steps

To complete this analysis:

1. **Add Acts 15:25** - Example of EXCLUSIVE clusivity
   - Apostles writing to churches
   - "We" = apostles only (exclusive)

2. **Add John 11:7** - Another INCLUSIVE example
   - Jesus to disciples: "Let us go"
   - "We" includes disciples (inclusive)

3. **Expand language coverage**
   - Add Fijian, Malay, Samoan (more Austronesian)
   - Add Algonquin, Cree (Algic family with clusivity)
   - Add Mayan languages (if clusivity is marked)

4. **Test edge cases**
   - Mixed audiences (God speaking to angels AND humans)
   - Rhetorical "we" (author including reader)

---

**Conclusion**: TBTA's encoding of "First Inclusive" for Genesis 1:26 is validated by actual translation choices in clusivity-marking languages (Tagalog, Indonesian). This demonstrates the value of TBTA data for AI-assisted Bible translation into the 700+ languages that grammatically mark clusivity.
