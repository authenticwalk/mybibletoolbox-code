# EXPERIMENT 001: Degree Annotation Reproduction Test

**Date**: 2025-11-07
**Researcher**: Claude (Sonnet 4.5)
**Goal**: Independently predict degree values for adjectives/adverbs/verbs, then compare with TBTA's actual annotations

---

## Methodology

Following the algorithm from LEARNINGS.md:
1. Identify adjectives, adverbs, and verbs in verse
2. Check for morphological degree markers (Greek -τερος/-τατος, Hebrew מִן)
3. Identify analytic constructions (more/most, μᾶλλον/μάλιστα)
4. Assess intensifiers (very, λίαν, σφόδρα, מְאֹד)
5. Determine construction type (comparative, superlative, equative, etc.)
6. Apply decision tree to predict: N/C/S/I/E/T/L/l/q/i/s
7. Compare with TBTA's actual annotation
8. Analyze matches/mismatches

---

## Test Verses and Predictions

### 1. JOHN 15:13 - Comparative (C)
**Verse**: "Greater love has no one than this: to lay down one's life for one's friends."
**Greek**: μείζονα ταύτης ἀγάπην οὐδεὶς ἔχει, ἵνα τις τὴν ψυχὴν αὐτοῦ θῇ ὑπὲρ τῶν φίλων αὐτοῦ

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| Greater | μείζονα | Adjective | Comparative form of μέγας | **C** (Comparative) | Synthetic comparative -ίων/-ονα form, explicit comparison "than this" |
| love | ἀγάπην | Noun | Direct object | N/A | Not degree-marked |
| no one | οὐδεὶς | Pronoun | Subject | N/A | Not degree-marked |

**Key Expectation**: μείζονα should definitively be **C** - this is a clear synthetic comparative with explicit "than" construction.

---

### 2. MATTHEW 22:36 & 22:38 - Superlative (S)
**Verse**: "Teacher, which is the greatest commandment in the Law?" ... "This is the first and greatest commandment."
**Greek**: Διδάσκαλε, ποία ἐντολὴ μεγάλη ἐν τῷ νόμῳ; ... αὕτη ἐστὶν ἡ μεγάλη καὶ πρώτη ἐντολή

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| greatest | μεγάλη (v36) | Adjective | Positive form but superlative sense | **S** (Superlative) OR **N** | Context implies superlative "which is greatest?" but morphology is positive |
| great/greatest | μεγάλη (v38) | Adjective | Positive form with definite article | **S** (Superlative) | Article + context + "first and greatest" suggests superlative interpretation |

**Key Uncertainty**: Greek uses positive form μεγάλη with superlative meaning via context and article. Does TBTA mark as **S** (semantic superlative) or **N** (morphological base form)?

---

### 3. MATTHEW 5:19 - Downward Superlative (l)
**Verse**: "Therefore anyone who sets aside one of the least of these commands... will be called least in the kingdom of heaven."
**Greek**: ὃς ἐὰν οὖν λύσῃ μίαν τῶν ἐντολῶν τούτων τῶν ἐλαχίστων... ἐλάχιστος κληθήσεται ἐν τῇ βασιλείᾳ τῶν οὐρανῶν

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| least (commands) | ἐλαχίστων | Adjective | Superlative form of μικρός/ὀλίγος | **l** (least) OR **S** | Superlative of small/little - could be 'l' (least) or just S (superlative) |
| least (called) | ἐλάχιστος | Adjective | Superlative predicate | **l** (least) OR **S** | Same form, downward superlative |

**Key Uncertainty**: Does TBTA distinguish downward superlative **l** from general superlative **S**? ἐλάχιστος is morphologically superlative but semantically "least/smallest".

---

### 4. ROMANS 5:15 & 5:17 - Intensified Comparative (i)
**Verse**: "But the gift is not like the trespass. For if the many died by the trespass of the one man, how much more did God's grace... overflow to the many!"
**Greek**: ...εἰ γὰρ τῷ τοῦ ἑνὸς παραπτώματι οἱ πολλοὶ ἀπέθανον, πολλῷ μᾶλλον ἡ χάρις τοῦ θεοῦ...

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| how much more | πολλῷ μᾶλλον | Adverb phrase | Dative of degree + comparative adverb | **i** (Intensified Comparative) | "Much more" - μᾶλλον is comparative, πολλῷ intensifies it |
| many (died) | πολλοὶ | Adjective | Positive, no degree | **N** (No Degree) | Not comparative/superlative, just "many" |
| many (overflow) | Various | Adjective | Context dependent | **N** (No Degree) | Not marked for degree |

**Key Prediction**: πολλῷ μᾶλλον should be **i** for adjectives (if modifying adjectives) or possibly **C** for adverbs (since adverbs don't have 'i' code). Need to check part of speech carefully.

**Alternative Prediction**: If μᾶλλον is analyzed as adverb modifying verb, might be **C** not **i** (since adverbs lack 'i' code).

---

### 5. MARK 1:35 - Intensified (I)
**Verse**: "Very early in the morning, while it was still dark, Jesus got up..."
**Greek**: Καὶ πρωῒ ἔννυχα λίαν ἀναστὰς ἐξῆλθεν...

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| very early | πρωῒ ... λίαν | Adverb + Intensifier | πρωῒ (early) + λίαν (very) | **V** (Intensified Adverb) | λίαν is standard intensifier, modifying adverb πρωῒ. For adverbs: I→V |
| dark | ἔννυχα | Adverb | "while night, in darkness" | **N** (No Degree) | Not degree-marked |

**Key Expectation**: λίαν should trigger **V** (for adverbs) or **I** (for adjectives). Since πρωῒ is temporal adverb, expect **V**.

---

### 6. 2 CORINTHIANS 4:17 - Extremely Intensified (E)
**Verse**: "For our light and momentary troubles are achieving for us an eternal glory that far outweighs them all."
**Greek**: τὸ γὰρ παραυτίκα ἐλαφρὸν τῆς θλίψεως ἡμῶν καθ' ὑπερβολὴν εἰς ὑπερβολὴν αἰώνιον βάρος δόξης κατεργάζεται ἡμῖν

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| light | ἐλαφρὸν | Adjective | Positive form | **N** (No Degree) | Not marked for degree |
| momentary | παραυτίκα | Adjective/Adverb | Not degree-marked | **N** (No Degree) | Base form |
| eternal | αἰώνιον | Adjective | Not degree-marked | **N** (No Degree) | Inherently non-gradable |
| far outweighs / beyond all comparison | καθ' ὑπερβολὴν εἰς ὑπερβολὴν | Prepositional phrase | "According to excess unto excess" | **E** (Extremely Intensified) | Double hyperbole construction - maximum intensification |

**Key Prediction**: The phrase "καθ' ὑπερβολὴν εἰς ὑπερβολὴν" is an extreme intensification construction. If TBTA annotates this, should be **E**. However, it's a prepositional phrase, not morphological marking on adjective/adverb/verb.

**Alternative Analysis**: May be marked on the noun "βάρος" (weight) or the verb "κατεργάζεται" (achieves) if TBTA encodes the intensifying effect.

---

### 7. HEBREWS 7:7 - Downward Comparative (L)
**Verse**: "And without doubt the lesser is blessed by the greater."
**Greek**: χωρὶς δὲ πάσης ἀντιλογίας τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| lesser | ἔλαττον | Adjective | Comparative of small/less | **L** (less) OR **C** | ἐλάττων is comparative meaning "lesser/smaller/inferior" |
| greater | κρείττονος | Adjective | Comparative of good/great | **C** (Comparative) | κρείττων is irregular comparative "better/greater" |

**Key Uncertainty**: Does TBTA distinguish upward comparative **C** from downward comparative **L**?
- ἔλαττον = "lesser/smaller" (downward) → Should be **L**
- κρείττων = "greater/better" (upward) → Should be **C**

Or does TBTA treat all synthetic comparatives as **C** regardless of semantic direction?

---

### 8. MATTHEW 10:25 - Equality/Equative (q)
**Verse**: "It is enough for students to be like their teachers, and servants like their masters."
**Greek**: ἀρκετὸν τῷ μαθητῇ ἵνα γένηται ὡς ὁ διδάσκαλος αὐτοῦ καὶ ὁ δοῦλος ὡς ὁ κύριος αὐτοῦ

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|-------|------|----------|---------------|-----------|
| enough | ἀρκετὸν | Adjective | "sufficient" | **N** (No Degree) | Not comparative/superlative |
| like/as | ὡς | Conjunction | Comparison particle | N/A | Not a gradable word |
| teachers | διδάσκαλος | Noun | Not degree-marked | N/A | Noun, not adjective |

**Key Problem**: This verse doesn't have clear **q** (equative) construction on an adjective. Greek ὡς is similative/equative conjunction but doesn't mark degree on an adjective itself.

**Better verse needed**: Need "as...as" construction with adjectives (e.g., "as wise as", "as strong as").

---

### 9. GENESIS 1:1 - No Degree (N) [Hebrew baseline]
**Verse**: "In the beginning God created the heavens and the earth."
**Hebrew**: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Hebrew | Part | Analysis | My Prediction | Reasoning |
|------|--------|------|----------|---------------|-----------|
| beginning | רֵאשִׁית | Noun | Construct state | N/A | Noun |
| heavens | שָׁמַיִם | Noun | Dual/plural noun | N/A | Noun |
| earth | אָרֶץ | Noun | Singular noun | N/A | Noun |

**Note**: No adjectives in this verse. Pure **N** baseline expected if we look at English translation adjectives.

**Better verse needed**: Hebrew verse with adjective + מִן construction for comparative.

---

### 10. SONG OF SOLOMON 1:2 - Comparative (C) [Hebrew]
**Verse**: "Let him kiss me with the kisses of his mouth—for your love is more delightful than wine."
**Hebrew**: יִשָּׁקֵנִי מִנְּשִׁיקוֹת פִּיהוּ כִּי טוֹבִים דֹּדֶיךָ מִיָּיִן

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Hebrew | Part | Analysis | My Prediction | Reasoning |
|------|--------|------|----------|---------------|-----------|
| good/delightful | טוֹבִים | Adjective | Positive form + מִן construction | **C** (Comparative) | טוֹב + מִן = "better than" - Hebrew periphrastic comparative |
| wine | יַיִן | Noun | Standard of comparison | N/A | Noun in מִן construction |

**Key Expectation**: Hebrew מִן construction should definitively yield **C** (Comparative). This is the primary Hebrew comparative strategy.

---

### 11. SONG OF SOLOMON 1:8 - Superlative (S) [Hebrew]
**Verse**: "If you do not know, most beautiful of women, follow the tracks of the sheep..."
**Hebrew**: אִם־לֹא תֵדְעִי לָךְ הַיָּפָה בַנָּשִׁים...

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Hebrew | Part | Analysis | My Prediction | Reasoning |
|------|--------|------|----------|---------------|-----------|
| most beautiful | הַיָּפָה | Adjective | Definite article + adjective | **S** (Superlative) OR **N** | Article + construct/partitive ("beautiful among women") suggests superlative |
| among women | בַנָּשִׁים | Prepositional phrase | Comparison set | N/A | Establishes superlative set |

**Key Uncertainty**: Hebrew uses definite article + partitive to express superlative. Does TBTA mark this as **S**?

**Alternative**: Hebrew may use construct state pattern for clearer superlative (like "Song of Songs" = "Best Song").

---

### 12. EPHESIANS 3:20 - Extremely Intensified (E)
**Verse**: "Now to him who is able to do immeasurably more than all we ask or imagine..."
**Greek**: Τῷ δὲ δυναμένῳ ὑπὲρ πάντα ποιῆσαι ὑπερεκπερισσοῦ ὧν αἰτούμεθα ἢ νοοῦμεν

#### MY PREDICTIONS (BEFORE CHECKING TBTA):

| Word | Greek | Part | Analysis | My Prediction | Reasoning |
|------|--------|------|----------|---------------|-----------|
| immeasurably more | ὑπερεκπερισσοῦ | Adverb | Triple-compounded: ὑπέρ-ἐκ-περισσός | **E** (Extremely Intensified) | Maximum intensification - "hyper-out-abundantly" |
| able | δυναμένῳ | Verb participle | Present participle | **N** (No Degree) | Not degree-marked |
| all | πάντα | Adjective/Pronoun | Universal quantifier | **N** (No Degree) | Not degree comparison |

**Key Expectation**: ὑπερεκπερισσοῦ is extreme compound intensification, should be **E** if TBTA annotates it as adverb.

---

## Summary of Predictions

### Expected Distribution by Degree Code

| Degree Code | Count | Test Verses |
|-------------|-------|-------------|
| **N** (No Degree) | Baseline | Genesis 1:1, unmarked adjectives throughout |
| **C** (Comparative) | 4 | John 15:13 (μείζονα), Song 1:2 (מִן), Hebrews 7:7 (κρείττονος), Romans 5:15 (μᾶλλον?) |
| **S** (Superlative) | 2-3 | Matthew 22:36/38 (μεγάλη), Song 1:8 (הַיָּפָה), potentially Matthew 5:19 |
| **I** (Intensified Adj) | 0-1 | Limited in selected verses |
| **V** (Intensified Adv) | 1 | Mark 1:35 (λίαν) |
| **E** (Extremely Intensified) | 2 | 2 Cor 4:17 (ὑπερβολή x2), Eph 3:20 (ὑπερεκπερισσοῦ) |
| **T** ('too' / excessive) | 0 | Not found in selected verses - RARE in Biblical text |
| **L** ('less') | 1 | Hebrews 7:7 (ἔλαττον) |
| **l** ('least') | 1 | Matthew 5:19 (ἐλάχιστος) |
| **q** (Equality) | 0 | Matthew 10:25 not clear - need better verse |
| **i** (Intensified Comp) | 1 | Romans 5:15 (πολλῷ μᾶλλον) |
| **s** (Superlative of 2) | 0 | Not found - need specific verse |

### Key Uncertainties to Resolve

1. **Semantic vs. Morphological**: When Greek uses positive form (μεγάλη) with superlative meaning via context, does TBTA mark as **S** or **N**?

2. **Downward vs. Upward Comparison**: Does TBTA distinguish **L** (less) from **C** (more), or treat all comparatives as **C**?
   - ἔλαττον "lesser" → L or C?
   - ἐλάχιστος "least" → l or S?

3. **Intensified Comparative**: Does "much more" (πολλῷ μᾶλλον) get marked as **i** (Intensified Comparative)?
   - Complication: 'i' only exists for adjectives, not adverbs
   - If μᾶλλον is adverb: **C** not **i**
   - If modifying adjective: **i** possible

4. **Extreme Intensification Constructions**: How does TBTA handle:
   - Double hyperbole (καθ' ὑπερβολὴν εἰς ὑπερβολὴν)
   - Triple compounds (ὑπερεκπερισσοῦ)
   - Are these marked on verbs/nouns/adverbs? Which gets the **E** code?

5. **Hebrew Article + Partitive**: Does definite article + "among X" yield **S**?
   - הַיָּפָה בַנָּשִׁים "the beautiful among women"
   - Hebrew contextual superlative vs. morphological

6. **Missing Codes**: Unable to find clear Biblical examples of:
   - **T** (too / excessive) - seems rare/absent in Biblical language
   - **q** (equative "as...as") - need better verse with gradable adjective
   - **s** (superlative of 2) - need explicit "X-er of the two" construction

---

## Additional Verses Needed

To complete coverage of all 11 degree values:

### For **T** ('too' / excessive):
**Challenge**: Biblical texts rarely express excessive degree with negative implicature.
**Possible search**: Look for translations rendering Greek excess as "too much/too great" in warning contexts.
**Alternative**: May not exist in Biblical corpus - this could be a target-language-specific encoding for modern translations only.

### For **q** (Equality / equative):
**Better verse**: Philippians 2:6 - "being in the form of God, did not count equality with God..."
- Greek: ὃς ἐν μορφῇ θεοῦ ὑπάρχων οὐχ ἁρπαγμὸν ἡγήσατο τὸ εἶναι ἴσα θεῷ
- **ἴσα** = "equal/equivalent" - equative construction
**Alternative**: Matthew 20:12 - "You have made them equal to us" (ἴσους ἡμῖν)

### For **s** (Superlative of 2):
**Better verse**: John 19:11 - "the one who handed me over to you is guilty of a greater sin"
- Greek: ὁ παραδούς μέ σοι μείζονα ἁμαρτίαν ἔχει
- Comparing two entities (Pilate vs. betrayer) - is this **s** or just **C**?
**Challenge**: "Superlative of 2" is subtle - may require specific "the X-er of the two" phrasing.

---

---

## RESULTS: Actual TBTA Annotations vs. My Predictions

**NOTE**: This section to be filled in after accessing TBTA database/dataset. Expected data format:

```yaml
verse: JHN 15:13
constituents:
  - word: "greater"
    greek: "μείζονα"
    part: "adjective"
    degree: "C"
    person: "Third"
    number: "Singular"
```

### 1. JOHN 15:13 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| greater | μείζονα | **C** (Comparative) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 2. MATTHEW 22:36 & 22:38 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | Context | My Prediction |
|------|-------|---------|---------------|
| greatest | μεγάλη | v36 question | **S** or **N** (uncertain) |
| great/greatest | μεγάλη | v38 answer | **S** (Superlative) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 3. MATTHEW 5:19 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| least (commands) | ἐλαχίστων | **l** (least) or **S** |
| least (called) | ἐλάχιστος | **l** (least) or **S** |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 4. ROMANS 5:15 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| much more | πολλῷ μᾶλλον | **i** (Intensified Comp) or **C** |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 5. MARK 1:35 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| very early | λίαν | **V** (Intensified Adverb) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 6. 2 CORINTHIANS 4:17 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| beyond comparison | καθ' ὑπερβολὴν εἰς ὑπερβολὴν | **E** (Extremely Intensified) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 7. HEBREWS 7:7 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| lesser | ἔλαττον | **L** (less) or **C** |
| greater | κρείττονος | **C** (Comparative) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 8. SONG OF SOLOMON 1:2 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Hebrew | My Prediction |
|------|--------|---------------|
| good/delightful | טוֹבִים מִיָּיִן | **C** (Comparative) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 9. SONG OF SOLOMON 1:8 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Hebrew | My Prediction |
|------|--------|---------------|
| most beautiful | הַיָּפָה בַנָּשִׁים | **S** (Superlative) or **N** |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

### 10. EPHESIANS 3:20 - ⏳ AWAITING TBTA DATA

**My Predictions**:
| Word | Greek | My Prediction |
|------|-------|---------------|
| immeasurably more | ὑπερεκπερισσοῦ | **E** (Extremely Intensified) |

**TBTA Actual**: [TO BE FILLED]

**Analysis**: [TO BE FILLED]

---

## Pattern Analysis (Post-Data Collection)

### Pattern 1: [TO BE DETERMINED]

**Finding**: [TO BE FILLED]

**Evidence**: [TO BE FILLED]

**Rule**: [TO BE FILLED]

---

### Pattern 2: [TO BE DETERMINED]

**Finding**: [TO BE FILLED]

**Evidence**: [TO BE FILLED]

**Rule**: [TO BE FILLED]

---

## Refined Reproduction Algorithm

**NOTE**: To be refined after analyzing actual TBTA data. Current hypothesis based on LEARNINGS.md:

### Step 1: Identify Part of Speech

```
Determine if word is:
- Adjective → 11 degree values available (N/C/S/I/E/T/L/l/q/i/s)
- Adverb → 8 degree values available (N/C/S/V/E/T/L/l)
- Verb → 8 degree values available (N/C/S/I/E/T/L/l)
```

### Step 2: Check for Morphological Degree Marking

```
Greek:
  - Synthetic comparative (-τερος/-ίων) → C
  - Synthetic superlative (-τατος/-ιστος) → S
  - Analytic μᾶλλον → C
  - Analytic μάλιστα → S

Hebrew:
  - מִן construction → C
  - Construct state + context → S
  - Definite article + partitive → S
```

### Step 3: Check for Intensification

```
Intensifiers:
  - Standard (very, λίαν, quite, מְאֹד) → I (adj/vrb) or V (adv)
  - Maximum (extremely, σφόδρα, compounds) → E

Excessive:
  - "too" / negative implicature → T
```

### Step 4: Check for Special Constructions

```
Equative: "as...as" (ἴσα, ὡς...ὡς) → q (adjectives only)
Intensified comparative: "much more" (πολλῷ μᾶλλον) → i (adjectives only)
Downward comparison: "less/least" (ἔλαττον/ἐλάχιστος) → L/l
```

### Step 5: Default to No Degree

```
If no clear degree marking → N
```

---

## Questions for Next Experiments

### Question 1: Semantic vs. Morphological Encoding
**Status**: Critical - awaiting data

**Question**: When source language uses positive form with superlative meaning (Greek μεγάλη "great" meaning "greatest"), does TBTA:
- Code semantic value (**S** for superlative meaning)
- Code morphological form (**N** for positive form)

**Hypothesis**: TBTA likely codes semantic meaning based on target translation, not source morphology alone.

---

### Question 2: Downward Comparison Distinction
**Status**: Critical - awaiting data

**Question**: Does TBTA distinguish upward (C) from downward (L) comparison?

**Test case**: Hebrews 7:7
- ἔλαττον "lesser" → L or C?
- ἐλάχιστος "least" → l or S?

**Hypothesis**: TBTA may treat all synthetic comparatives as **C** and all synthetic superlatives as **S**, ignoring semantic direction (upward vs. downward).

**Alternative hypothesis**: TBTA distinguishes based on lexical semantics of the adjective (μείζων/greater=C, ἔλαττον/lesser=L).

---

### Question 3: Intensified Comparative Triggers
**Status**: Important - awaiting data

**Question**: What triggers **i** (Intensified Comparative)?
- "Much more" (πολλῷ μᾶλλον)
- "Far more"
- "Way more"
- Only for adjectives (not adverbs/verbs)

**Complication**: If μᾶλλον is analyzed as adverb, **i** code unavailable (adverbs lack 'i'). How is it encoded?

---

### Question 4: Extreme Intensification Boundaries
**Status**: Important - awaiting data

**Question**: What distinguishes **I** from **E**?
- λίαν "very" → I or E?
- σφόδρα "greatly/exceedingly" → I or E?
- Compounds (ὑπερεκπερισσοῦ) → E?
- Double constructions (ὑπερβολὴν εἰς ὑπερβολὴν) → E?

**Need**: Clear boundary between standard intensification (I/V) and extreme intensification (E).

---

### Question 5: Hebrew Contextual Degree
**Status**: Important - awaiting data

**Question**: How does TBTA handle Hebrew's non-morphological degree systems?
- Article + partitive = superlative? (הַיָּפָה בַנָּשִׁים)
- מִן construction = comparative? (Always C?)
- Construct state superlative? (שִׁיר הַשִּׁירִים)

**Hypothesis**: Hebrew periphrastic constructions should map to C/S when semantically clear.

---

### Question 6: Rare Degree Values in Biblical Text
**Status**: Exploratory

**Question**: Do **T** (too), **q** (equative), and **s** (superlative of 2) actually occur in Biblical texts?

**Observation**:
- **T** not found in selected verses (rare in formal/elevated Biblical register?)
- **q** requires specific "as...as" with gradable adjective (ἴσα "equal" may work)
- **s** requires explicit "X-er of the two" phrasing (may be absent or rare)

**Need**: Comprehensive search of TBTA dataset for these rare codes.

---

### Question 7: Part of Speech Ambiguity
**Status**: Methodological

**Question**: When degree construction involves multiple words (πολλῷ μᾶλλον), which word receives the degree code?
- The head adjective/adverb/verb being modified?
- The degree marker itself (μᾶλλον)?
- Both?

**Need**: Understand TBTA's annotation scope and granularity.

---

### Question 8: Translation Variance
**Status**: Exploratory

**Question**: Do different Bible translations show systematic differences in degree encoding?
- Formal equivalence (ESV, NASB) vs. dynamic equivalence (NIV, NLT)
- Older translations (KJV) vs. modern
- Language families (Germanic vs. Romance vs. Sino-Tibetan)

**Hypothesis**: Synthetic languages (German, Russian) may show more morphological C/S; analytic languages (Mandarin, Vietnamese) may show more I/E.

---

## Recommended Next Experiments

### Experiment 002: Downward Comparison Verification
**Verses to test**:
- Hebrews 7:7 (ἔλαττον "lesser")
- Matthew 5:19 (ἐλάχιστος "least")
- 1 Corinthians 15:9 (ἐλάχιστος "least of the apostles")
- John 2:10 (ἐλάσσω "inferior/worse")

**Goal**: Confirm whether TBTA uses L/l codes or treats downward as C/S.

---

### Experiment 003: Intensification Spectrum Mapping
**Verses to test**:
- Standard intensifiers: λίαν, πάνυ, מְאֹד
- Maximum intensifiers: σφόδρα, compounds, double constructions
- Compare across I vs. E boundary

**Goal**: Define clear criteria for I/V vs. E distinction.

---

### Experiment 004: Hebrew Periphrastic Degree Survey
**Verses to test**:
- Various מִן constructions (comparative)
- Various construct state patterns (superlative)
- Various article + partitive constructions (superlative)

**Goal**: Map Hebrew non-morphological degree to TBTA codes.

---

### Experiment 005: Rare Degree Code Search
**Method**:
- Grep/search entire TBTA dataset for:
  - `degree: T` (excessive)
  - `degree: q` (equative)
  - `degree: s` (superlative of 2)
  - `degree: i` (intensified comparative)

**Goal**: Find actual Biblical examples of rare codes, or confirm absence.

---

### Experiment 006: Comparative Constructions Across Languages
**Method**:
- Select 5-10 key comparative verses
- Check encoding across:
  - Synthetic languages (German, Spanish, Greek)
  - Analytic languages (English, French, Mandarin)
  - Degree-neutral languages (if any in TBTA)

**Goal**: Understand cross-linguistic variation in degree encoding.

---

## Preliminary Conclusions

### Current Understanding (Pre-Data)

Based on LEARNINGS.md and source language analysis:

1. **TBTA encodes target language form, not source morphology alone**
   - Translation-centric, not source-text-centric
   - Degree in English translation may differ from Greek/Hebrew

2. **Part of speech determines available degree values**
   - Adjectives: Full 11-value system
   - Adverbs: 8 values (no q/i/s)
   - Verbs: 8 values (no q/i/s)

3. **Morphological marking is primary indicator**
   - Greek synthetic forms (-τερος/-τατος) strongly predict C/S
   - Hebrew periphrastic constructions (מִן, construct) predict C/S
   - Intensifiers (λίαν, σφόδρα, מְאֹד) predict I/V/E

4. **Context and semantics matter**
   - Positive form with superlative meaning → S possible
   - Article + partitive → S possible
   - Comparison particle ("than", מִן) → C expected

5. **Some codes may be rare or absent in Biblical texts**
   - **T** (excessive) not found in formal Biblical register
   - **q** (equative) rare, needs specific construction
   - **s** (superlative of 2) rare or absent

### Confidence Levels (Pre-Data)

**High Confidence** (90%+ expected accuracy):
- Greek synthetic comparative → C
- Greek synthetic superlative → S
- Hebrew מִן construction → C
- Standard intensifiers → I/V
- No marking → N

**Medium Confidence** (70-90% expected accuracy):
- Analytic μᾶλλον/μάλιστα → C/S
- Extreme intensifiers → E
- Hebrew construct state → S
- Positive form with superlative context → S or N

**Low Confidence** (<70% expected accuracy):
- Downward comparison → L/l or C/S
- Intensified comparative → i or C
- Hebrew article + partitive → S or N
- Rare codes T/q/s → existence unclear

---

## Success Rate Calculation (Post-Data)

**To be filled after accessing TBTA data:**

| Category | Predictions | Matches | Mismatches | Accuracy |
|----------|-------------|---------|------------|----------|
| Comparative (C) | [#] | [#] | [#] | [%] |
| Superlative (S) | [#] | [#] | [#] | [%] |
| Intensified (I/V) | [#] | [#] | [#] | [%] |
| Extremely Intensified (E) | [#] | [#] | [#] | [%] |
| Downward (L/l) | [#] | [#] | [#] | [%] |
| Other (T/q/i/s) | [#] | [#] | [#] | [%] |
| No Degree (N) | [#] | [#] | [#] | [%] |
| **TOTAL** | [#] | [#] | [#] | [%] |

---

## Next Steps

1. ✅ Access TBTA database/dataset for test verses
2. ⏳ Fill in actual TBTA annotations in results section
3. ⏳ Calculate accuracy and analyze mismatches
4. ⏳ Identify patterns from matches/mismatches
5. ⏳ Refine algorithm based on findings
6. ⏳ Design Experiment 002 based on critical uncertainties
7. ⏳ Expand verse coverage to include all 11 degree values

---

**Experiment Status**: PREDICTIONS COMPLETE - AWAITING TBTA DATA ACCESS

**Next Action**: Locate and access TBTA database to fill in actual annotations for comparison.

**Data Access Notes**:
- Check for TBTA API or database export
- Verify data format and annotation structure
- Confirm verse references match (book/chapter/verse format)
- Identify how to query degree annotations specifically
