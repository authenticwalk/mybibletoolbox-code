# Number Systems: Adversarial Test Set (REDESIGNED)

**Purpose**: Test algorithm v1.0 with equal coverage of all number values
**Design principle**: Equal examples per value (2 each), harder ambiguous cases
**Expected accuracy**: 60-70% (challenging cases with potential disagreement)
**Selection date**: 2025-11-08 (REVISED)
**Status**: LOCKED - Do not modify after predictions begin

---

## Design Philosophy Change

**Original design flaw**: Unbalanced (5 singular, 3 plural, 1 dual, 1 trial)
- Risk: High accuracy on over-represented values, low on under-represented
- Bias: Algorithm could succeed by defaulting to most common value

**New design**: Equal coverage (2 examples per value × 6 values = 12 verses)
- Benefit: Tests algorithm's ability to distinguish ALL values
- Requirement: Each value must be tested with ambiguous/hard cases
- Focus: Verses where there could be legitimate disagreement

---

## Test Set Overview

**Total verses**: 12
**Distribution**: 2 examples per value
**Selection criteria**: Ambiguous cases, morphology-semantics conflicts, theological debates
**Training overlap**: None

---

## Category 1: Singular (2 verses)

Hard cases where singular might be confused with collective/plural

### 1. Genesis 41:40 - Collective Noun "My People"

**Reference**: Genesis 41:40
**Hebrew**: עַל־פִּיךָ יִשַּׁק כָּל־עַמִּי
**English (ESV)**: "All my people shall order themselves as you command"

**Challenge**:
- עַמִּי (ammi) "my people" - morphologically singular, semantically multiple persons
- Does TBTA mark collective as Singular (grammatical) or Plural (semantic)?
- "All my people" suggests many, but Hebrew noun is singular

**Why ambiguous**: Collective noun ambiguity - could argue either way
**Expected answer**: Singular (if TBTA follows morphology)
**Alternative**: Plural (if TBTA follows semantics)

---

### 2. Matthew 3:16 - "Heavens" Opened (Plural Morphology)

**Reference**: Matthew 3:16
**Greek**: ἠνεῴχθησαν αὐτῷ οἱ οὐρανοί
**English (ESV)**: "The heavens were opened to him"

**Challenge**:
- οἱ οὐρανοί (hoi ouranoi) - nominative plural "heavens"
- Training showed Gen 1:1 שָׁמַיִם → Singular (LXX: singular οὐρανόν)
- But here Greek has PLURAL οὐρανοί with PLURAL verb ἠνεῴχθησαν
- Does plural morphology override semantic singular?

**Why ambiguous**: Conflicts with training pattern (shamayim → singular)
**Expected answer**: Uncertain (Singular if semantic, Plural if following Greek morphology)
**Tests**: Whether TBTA prioritizes Greek morphology over Hebrew semantics

---

## Category 2: Dual (2 verses)

Hard cases where dual might be confused with singular or plural

### 3. Genesis 22:6 - "Both of Them" (Explicit Dual)

**Reference**: Genesis 22:6
**Hebrew**: וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו
**English (ESV)**: "And they went both of them together"

**Challenge**:
- שְׁנֵיהֶם (shneihem) - "both of them" / "the two of them"
- Explicitly dual with שְׁנֵי (two) + third person dual suffix
- But verb is plural: וַיֵּלְכוּ (wayelekhu)
- Does dual pronoun get Dual marking or Plural (following verb)?

**Why ambiguous**: Dual pronoun with plural verb agreement
**Expected answer**: Dual (explicit "both")
**Alternative**: Plural (verb agreement)

---

### 4. Exodus 4:11 - "Blind" (Implicit Reference to Two Eyes)

**Reference**: Exodus 4:11
**Hebrew**: וַיֹּאמֶר יְהוָה אֵלָיו מִי שָׂם פֶּה לָאָדָם אוֹ מִי־יָשׂוּם אִלֵּם אוֹ חֵרֵשׁ אוֹ פִקֵּחַ אוֹ עִוֵּר
**English (ESV)**: "Who makes him mute, or deaf, or seeing, or blind?"

**Challenge**:
- עִוֵּר (iver) "blind" - singular adjective referring to eye disability
- Semantic: blindness = loss of function of two eyes
- But no explicit dual morphology (no עֵינַיִם "eyes" mentioned)
- Does implicit paired body part get Dual or Singular?

**Why ambiguous**: Implicit dual (eyes) vs. explicit singular (adjective)
**Expected answer**: Singular (adjective form)
**Alternative**: Dual (semantic reference to both eyes)

---

## Category 3: Trial (2 verses)

Hard cases where trial might be confused with plural or interpreted differently

### 5. Matthew 28:19 - Trinity Baptismal Formula

**Reference**: Matthew 28:19
**Greek**: βαπτίζοντες αὐτοὺς εἰς τὸ ὄνομα τοῦ Πατρὸς καὶ τοῦ Υἱοῦ καὶ τοῦ ἁγίου Πνεύματος
**English (ESV)**: "Baptizing them in the name of the Father and of the Son and of the Holy Spirit"

**Challenge**:
- Three persons explicitly listed: Father, Son, Holy Spirit
- But "name" (ὄνομα) is SINGULAR
- Training: Gen 1:26 "us" → Trial
- Here: Three separate names or one unified name?
- Do the three persons get Trial, or does the singular "name" override?

**Why ambiguous**: Singular noun (name) with three distinct referents
**Expected answer**: Uncertain (Trial for persons? Singular for "name"?)
**Tests**: Trinity marking in non-pronoun contexts

---

### 6. 1 John 5:7-8 - "Three That Bear Witness"

**Reference**: 1 John 5:7-8 (if in TBTA; alternatively use another "three" context)
**Greek**: τρεῖς εἰσιν οἱ μαρτυροῦντες
**English (ESV)**: "For there are three that testify"

**Challenge**:
- τρεῖς (treis) - explicitly "three"
- Context: Spirit, water, blood (not Trinity proper)
- Does non-Trinity "three" get Trial or Plural?
- Training focused on Trinity → Trial; does this generalize?

**Why ambiguous**: Explicit "three" but not Trinity context
**Expected answer**: Uncertain (Trial if explicit three, Plural if only Trinity gets trial)
**Tests**: Whether Trial is reserved for Trinity or applies to all groups of exactly three

---

## Category 4: Quadrial (2 verses)

Hard cases testing if quadrial exists or defaults to paucal/plural

### 7. Revelation 4:6-8 - Four Living Creatures

**Reference**: Revelation 4:6
**Greek**: τέσσαρα ζῷα
**English (ESV)**: "Four living creatures"

**Challenge**:
- τέσσαρα (tessara) - explicitly "four"
- Apocalyptic context: These four are significant (not arbitrary group)
- Does TBTA use Quadrial code, or default to Paucal/Plural?
- Is quadrial even in Biblical usage, or theoretical?

**Why ambiguous**: Unknown if quadrial is used in TBTA data
**Expected answer**: Uncertain (Quadrial if exists, Paucal if small group, Plural if default)
**Tests**: Existence of quadrial as productive value

---

### 8. Ezekiel 1:5 - Four Living Creatures (OT Parallel)

**Reference**: Ezekiel 1:5
**Hebrew**: וְדֹמוּת אַרְבַּע חַיּוֹת
**English (ESV)**: "And from the midst of it came the likeness of four living creatures"

**Challenge**:
- אַרְבַּע (arba) - explicitly "four"
- Same theological concept as Revelation 4
- Hebrew vs. Greek: Do both get same number marking?
- Multiple explicit "four" contexts: does TBTA establish quadrial pattern?

**Why ambiguous**: Same challenge as Rev 4:6, tests consistency across testaments
**Expected answer**: Uncertain (same as Rev 4:6)
**Tests**: Cross-testament consistency for quadrial

---

## Category 5: Paucal (2 verses)

Hard cases where paucal boundary with dual/plural is unclear

### 9. Mark 6:38 - "Five Loaves" (Small Specific Number)

**Reference**: Mark 6:38
**Greek**: πέντε ἄρτους καὶ δύο ἰχθύας
**English (ESV)**: "Five loaves and two fish"

**Challenge**:
- πέντε (pente) - "five" (small but more than trial)
- Does 5 count as Paucal ("a few") or Plural?
- Boundary question: Where does paucal end and plural begin?
- Different languages use different thresholds (3-10, 3-15, etc.)

**Why ambiguous**: Paucal boundary is language-dependent
**Expected answer**: Uncertain (Paucal if ≤10, Plural if general small groups)
**Tests**: Upper boundary of paucal in TBTA

---

### 10. Acts 1:15 - "About 120 Persons" (Referenced Group)

**Reference**: Acts 1:15
**Greek**: ὄχλος ὀνομάτων ὡς ἑκατὸν εἴκοσι
**English (ESV)**: "The company of persons was in all about 120"

**Challenge**:
- ἑκατὸν εἴκοσι (hekaton eikosi) - "120"
- Specific number but too large for paucal
- However, context treats as known bounded group (not generic crowd)
- Does large specific number get Plural or something else?

**Why ambiguous**: Large number but specific/bounded (not generic plural)
**Expected answer**: Plural (too large for paucal)
**Tests**: Whether specific large numbers differ from generic plurals

---

## Category 6: Plural (2 verses)

Hard cases where plural might be confused with paucal or collective singular

### 11. John 11:50 - "The Whole Nation" (Corporate Singular?)

**Reference**: John 11:50
**Greek**: ὅλον τὸ ἔθνος
**English (ESV)**: "The whole nation"

**Challenge**:
- τὸ ἔθνος (to ethnos) - singular "nation"
- But semantically refers to ALL people (plural entities)
- "Whole nation" emphasizes totality (plural members)
- Does TBTA mark Singular (grammatical) or Plural (semantic totality)?

**Why ambiguous**: Singular collective with plural semantic emphasis
**Expected answer**: Uncertain (Singular if grammatical, Plural if semantic)
**Tests**: Corporate solidarity / collective noun handling

---

### 12. Matthew 4:19 - "Fishers of Men" (Generic Plural)

**Reference**: Matthew 4:19
**Greek**: ποιήσω ὑμᾶς ἁλιεῖς ἀνθρώπων
**English (ESV)**: "I will make you fishers of men"

**Challenge**:
- ἀνθρώπων (anthrōpōn) - genitive plural "of men"
- Generic reference to humanity (not specific individuals)
- Does generic plural differ from specific plural in TBTA?
- "Men" = all mankind (very large) vs. specific group

**Why ambiguous**: Generic vs. specific plural distinction
**Expected answer**: Plural (standard)
**Tests**: Whether TBTA distinguishes generic from specific plurals

---

## Value Coverage Summary

| Value | Count | Verses |
|-------|-------|---------|
| Singular | 2 | Gen 41:40, Matt 3:16 |
| Dual | 2 | Gen 22:6, Exod 4:11 |
| Trial | 2 | Matt 28:19, 1 John 5:7-8 |
| Quadrial | 2 | Rev 4:6, Ezek 1:5 |
| Paucal | 2 | Mark 6:38, Acts 1:15 |
| Plural | 2 | John 11:50, Matt 4:19 |
| **TOTAL** | **12** | |

---

## Expected Performance

**Target accuracy**: 60-70% (7-8 correct out of 12)

**Likely challenges**:
- Quadrial verses: May not exist in TBTA → defaults to Plural (2 errors expected)
- Collective nouns: Singular vs. Plural ambiguity (1-2 errors expected)
- Paucal boundary: Uncertain threshold (1 error expected)
- Trinity non-pronoun: Unclear if Trial applies (1 error expected)

**Success benchmark**: 7-9 correct = 58-75% ✅

---

## Comparison with Random Test

Random test should also have 2 examples per value (12 total) but with clearer, less ambiguous cases.

**Expected gap**: Random 80-90% vs. Adversarial 60-70% = 15-25 points ✅

---

## Exclusions Confirmed

**Not in training set** (35 verses from experiment-001)
**Not overlapping with random test** (to be designed with same balance)

---

## Prediction Protocol

1. Apply algorithm v1.0 WITHOUT checking TBTA
2. For each verse, predict number value for specified constituent
3. Document reasoning and confidence
4. LOCK predictions (git commit)
5. Check TBTA only after predictions locked
6. Calculate accuracy by value (reveals which values algorithm handles well/poorly)

---

**Status**: ✅ Redesigned with equal value coverage
**Next step**: Make predictions using algorithm v1.0
**Target date**: 2025-11-10
