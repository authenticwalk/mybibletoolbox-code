# Adversarial Test Expansion: Batch 1 (Verses 8-20)

**Focus**: Rare values, Hebrew constructions, complex patterns
**Date**: 2025-11-09
**Baseline**: v2.0 = 100% on verses 1-7
**Goal**: Find edge cases v2.0 might not handle

---

## Selection Strategy

### Rare Value Hunting (Priority)
- **E (Extremely Intensified)**: Double intensifiers, extreme constructions
- **T (Excessive "too")**: Negative implicature contexts
- **L (Less)**: Downward comparatives
- **Literal values**: Additional literal quoted strings beyond `'''least'''`

### Hebrew Constructions
- מִן (min) comparative patterns
- Construct state superlatives
- מְאֹד (meod) intensification

### Complex Semantic Patterns
- Multiple comparatives in discourse
- Elative vs superlative ambiguity
- Discourse-level degree inheritance

---

## Verse 8: 2 Corinthians 12:9 - "more gladly"

**Target value**: I or C (intensified adverb OR comparative)?

**Greek**: ἥδιστα οὖν μᾶλλον καυχήσομαι ἐν ταῖς ἀσθενείαις μου

**English (ESV)**: "Therefore I will boast all the more gladly of my weaknesses"

**Analysis**:
- ἥδιστα (hēdista) = superlative form "most gladly"
- μᾶλλον (mallon) = "more" (comparative adverb)
- **Pattern**: Superlative form + μᾶλλον ("more") = "even more gladly"

**Expected challenge**:
- Is this intensified comparative (i)? Already confirmed i doesn't exist
- Or simple comparative (C)?
- Or superlative (S) with added emphasis?

**v2.0 Prediction**: Comparative (C)
- Reasoning: μᾶλλον creates comparative meaning despite superlative morphology
- RULE 1: Semantic overrides morphological

**Confidence**: Medium (compound degree construction)

---

## Verse 9: Hebrews 7:7 - "less/inferior"

**Target value**: L (Less) or C (Comparative)?

**Greek**: χωρὶς δὲ πάσης ἀντιλογίας τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται

**English (ESV)**: "Without any dispute, the inferior is blessed by the superior"

**Analysis**:
- τὸ ἔλαττον (to elatton) = "the lesser/inferior" (comparative form)
- κρείττονος (kreittonos) = "superior/better" (comparative form)
- **Pattern**: Downward comparative vs upward comparative

**Expected challenge**:
- Does TBTA distinguish L (less) from C (comparative)?
- Or both downward/upward map to C?

**v2.0 Prediction**: Comparative (C) for both
- Reasoning: No evidence L exists separately, both are comparative

**Confidence**: Low (unknown if L value exists)

**NOTE**: This verse is in Hebrews - may not be in TBTA export

---

## Verse 10: Psalm 119:103 (LXX 118:103) - "sweeter than honey"

**Target value**: C (Comparative)

**Hebrew**: מָה נִּמְלְצוּ לְחִכִּי אִמְרָתֶךָ מִדְּבַשׁ לְפִי
**LXX Greek**: ὡς γλυκέα τῷ λάρυγγί μου τὰ λόγιά σου ὑπὲρ μέλι τῷ στόματί μου

**English (ESV)**: "How sweet are your words to my taste, sweeter than honey"

**Analysis**:
- Hebrew: No comparative morphology (מִדְּבַשׁ = "than honey" with מִן)
- Greek: ὑπέρ (hyper) "more than" + μέλι "honey"
- **Pattern**: Hebrew מִן construction (periphrastic comparative)

**v2.0 Prediction**: Comparative (C)
- RULE 3: Hebrew מִן construction → Comparative

**Confidence**: High (standard Hebrew pattern)

---

## Verse 11: Song of Solomon 5:10 - "outstanding"

**Target value**: S (Superlative) or N (No Degree)?

**Hebrew**: דּוֹדִי צַח וְאָדוֹם דָּגוּל מֵרְבָבָה

**English (ESV)**: "My beloved is radiant and ruddy, distinguished among ten thousand"

**Analysis**:
- דָּגוּל (dagul) = "distinguished/outstanding"
- מֵרְבָבָה (merevavah) = "from/among ten thousand"
- **Pattern**: Partitive construction (outstanding AMONG group)

**Expected challenge**:
- Is this superlative (one distinguished from many)?
- Or just positive form with partitive prep?

**v2.0 Prediction**: Superlative (S)
- RULE 1: Partitive construction creates superlative context
- Pattern: "Distinguished AMONG ten thousand" = most distinguished

**Confidence**: Medium (partitive superlative pattern)

**NOTE**: May not be in TBTA export (Song of Solomon)

---

## Verse 12: Genesis 1:16 - "greater/lesser lights"

**Target value**: C (Comparative) or S (Superlative)?

**Hebrew**: וַיַּעַשׂ אֱלֹהִים אֶת שְׁנֵי הַמְּאֹרֹת הַגְּדֹלִים אֶת הַמָּאוֹר הַגָּדֹל... וְאֶת הַמָּאוֹר הַקָּטֹן

**English (ESV)**: "God made the two great lights—the greater light... and the lesser light"

**Analysis**:
- הַגָּדֹל (hagadol) = "the great" (definite + positive form)
- הַקָּטֹן (haqaton) = "the small" (definite + positive form)
- **Pattern**: Two entities compared (sun vs moon)

**Expected challenge**:
- Morphologically positive, semantically comparative
- Is this s (superlative of 2)? Already confirmed s doesn't exist
- Or C (comparative)?

**v2.0 Prediction**: Comparative (C) for "greater", Comparative (C) for "lesser"
- RULE 1: Semantic context (two entities compared) → Comparative
- s (superlative of 2) doesn't exist → use C

**Confidence**: Medium (dyadic comparison pattern)

---

## Verse 13: Matthew 23:17 - "which is greater"

**Target value**: S (Superlative)

**Greek**: τί γὰρ μεῖζόν ἐστιν, ὁ χρυσὸς ἢ ὁ ναὸς ὁ ἁγιάσας τὸν χρυσόν

**English (ESV)**: "For which is greater, the gold or the temple that has made the gold sacred?"

**Analysis**:
- μεῖζόν (meizon) = comparative form "greater"
- **Context**: Question comparing two items
- Pattern similar to MAT 22:36 (superlative question)

**Expected challenge**:
- Morphologically comparative
- Semantically: "which is greater [of the two]?"
- Is this superlative (like v1.0 MAT 11:11 error)?

**v2.0 Prediction**: Superlative (S)
- RULE 1: Superlative question context overrides morphology
- "Which is greater [of these]?" = superlative meaning

**Confidence**: High (similar to training verse MAT 22:36)

---

## Verse 14: Mark 9:34 - "who was greatest"

**Target value**: S (Superlative)

**Greek**: ἐσιώπων· πρὸς ἀλλήλους γὰρ διελέχθησαν ἐν τῇ ὁδῷ τίς μείζων

**English (ESV)**: "They kept silent, for on the way they had argued with one another about who was the greatest"

**Analysis**:
- μείζων (meizōn) = comparative form "greater"
- **Context**: "who was [the] greatest" (among disciples)
- Pattern: Comparative form in superlative discourse

**v2.0 Prediction**: Superlative (S)
- RULE 1: "who was greatest" question creates superlative context
- Semantic overrides morphological

**Confidence**: High (standard superlative question)

---

## Verse 15: John 13:16 - "not greater"

**Target value**: C (Comparative)

**Greek**: οὐκ ἔστιν δοῦλος μείζων τοῦ κυρίου αὐτοῦ

**English (ESV)**: "A servant is not greater than his master"

**Analysis**:
- μείζων (meizōn) = comparative form "greater"
- τοῦ κυρίου = genitive of comparison "than the master"
- **Context**: Negative comparative, BUT with explicit comparison standard

**Expected challenge**:
- Negative + comparative, like MAT 11:11?
- But MAT 11:11 was "no one greater" (universal), this is "servant not greater than master" (specific comparison)

**v2.0 Prediction**: Comparative (C)
- RULE 1: Check for IMPLIED superlative
  - Pattern: "A is not greater than B" → Simple comparison (A < B or A ≤ B)
  - NOT universal ("no one greater") → NOT implied superlative
- RULE 2: Morphology + semantics agree → Comparative

**Confidence**: Medium (distinguishing universal from specific negation)

---

## Verse 16: Romans 9:12 - "greater/older"

**Target value**: C (Comparative)

**Greek**: ὁ μείζων δουλεύσει τῷ ἐλάσσονι

**English (ESV)**: "The older will serve the younger"

**Analysis**:
- μείζων (meizōn) = "greater/older" (comparative)
- ἐλάσσονι (elassoni) = "lesser/younger" (comparative)
- **Context**: Birth order (Esau/Jacob)

**v2.0 Prediction**: Comparative (C) for both
- RULE 2: Synthetic comparative + comparative semantics → C

**Confidence**: High (straightforward comparative)

---

## Verse 17: 1 Corinthians 13:13 - "greatest"

**Target value**: S (Superlative) or `'''greatest'''` (literal)?

**Greek**: νυνὶ δὲ μένει πίστις, ἐλπίς, ἀγάπη, τὰ τρία ταῦτα· μείζων δὲ τούτων ἡ ἀγάπη

**English (ESV)**: "So now faith, hope, and love abide, these three; but the greatest of these is love"

**Analysis**:
- μείζων (meizōn) = comparative form "greater"
- τούτων = "of these" (partitive genitive)
- **Context**: "greatest of these three" (partitive superlative)

**Expected challenge**:
- Morphologically comparative
- Semantically superlative (partitive construction)
- Will TBTA use "Superlative" or `'''greatest'''` literal?

**v2.0 Prediction**: Superlative (S)
- RULE 1: Partitive construction ("of these") creates superlative context
- Expect standardized "Superlative" (not literal - only "least" seen as literal)

**Confidence**: High (partitive superlative)

**NOTE**: May not be in TBTA export (1 Corinthians)

---

## Verse 18: Matthew 18:1 - "who is greatest"

**Target value**: S (Superlative)

**Greek**: τίς ἄρα μείζων ἐστὶν ἐν τῇ βασιλείᾳ τῶν οὐρανῶν

**English (ESV)**: "Who is the greatest in the kingdom of heaven?"

**Analysis**:
- μείζων (meizōn) = comparative form "greater"
- **Context**: Direct superlative question ("who is greatest?")

**v2.0 Prediction**: Superlative (S)
- RULE 1: Explicit superlative question overrides morphology
- Same pattern as MAT 22:36 (training verse)

**Confidence**: Very high (identical to training pattern)

---

## Verse 19: Mark 12:31 - "no other greater"

**Target value**: S (Superlative)

**Greek**: μείζων τούτων ἄλλη ἐντολὴ οὐκ ἔστιν

**English (ESV)**: "There is no other commandment greater than these"

**Analysis**:
- μείζων (meizōn) = comparative form "greater"
- οὐκ ἔστιν = "there is not"
- **Context**: Negative + comparative ("no other greater")

**v2.0 Prediction**: Superlative (S)
- RULE 1 (expanded): Implied superlative pattern
  - "No other greater than X" → X is greatest
  - Universal negation + comparative → Superlative

**Confidence**: High (v2.0 Fix 2 should handle this)

---

## Verse 20: Acts 26:22 - "small and great"

**Target value**: C (Comparative) or N (No Degree)?

**Greek**: μαρτυρόμενος μικρῷ τε καὶ μεγάλῳ

**English (ESV)**: "To this day... saying nothing but what the prophets and Moses said... testifying both to small and great"

**Analysis**:
- μικρῷ (mikrō) = "small" (positive form, dative)
- μεγάλῳ (megalō) = "great" (positive form, dative)
- **Context**: "both small and great" (merism - totality expression)

**Expected challenge**:
- No comparative morphology
- Semantic: Represents all people (high and low social status)
- Merism, not comparison

**v2.0 Prediction**: No Degree (N) for both
- RULE 5: No degree morphology, no comparative context → Default
- Not a comparison, but a merism (figure of speech)

**Confidence**: Medium (merism pattern)

**NOTE**: May not be in TBTA export (Acts)

---

## Batch 1 Summary

| Verse | Reference | Target Pattern | Expected Challenge | v2.0 Confidence |
|-------|-----------|----------------|-------------------|-----------------|
| 8 | 2 COR 12:9 | Compound degree | Superlative + μᾶλλον | Medium |
| 9 | HEB 7:7 | Downward comparative | L vs C distinction | Low |
| 10 | PSA 119:103 | Hebrew מִן | Standard comparative | High |
| 11 | SNG 5:10 | Partitive superlative | Context-based | Medium |
| 12 | GEN 1:16 | Dyadic comparison | s value (doesn't exist) | Medium |
| 13 | MAT 23:17 | Superlative question | Like training verse | High |
| 14 | MRK 9:34 | Superlative discourse | Morphology override | High |
| 15 | JHN 13:16 | Specific negation | vs universal negation | Medium |
| 16 | ROM 9:12 | Standard comparative | Straightforward | High |
| 17 | 1 COR 13:13 | Partitive superlative | Literal value? | High |
| 18 | MAT 18:1 | Superlative question | Training pattern | Very High |
| 19 | MRK 12:31 | Implied superlative | v2.0 Fix 2 test | High |
| 20 | ACT 26:22 | Merism (no degree) | Figure of speech | Medium |

**Expected available**: 4-6 verses (many from unavailable books)
**Key learnings target**: Rare values (L, E, T), literal values, dyadic patterns

---

**Status**: Batch 1 designed (verses 8-20)
**Next**: Extract TBTA data for available verses and validate predictions
**Goal**: Test v2.0 on new patterns, identify algorithm gaps
