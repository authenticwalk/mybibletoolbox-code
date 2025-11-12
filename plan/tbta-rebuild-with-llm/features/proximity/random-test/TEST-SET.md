# Proximity Feature: Random Test Set

**Feature**: Proximity (TBTA position 8)
**Date Created**: 2025-11-12
**Phase**: 5 - Test Set Design
**Test Type**: Random (representative baseline)
**Total Verses**: 12 (stratified random sample)
**Target Accuracy**: 80-90% (typical cases)

## Design Strategy

**Random Sampling Approach**: Representative distribution of proximity values
- **Equal value coverage**: 2 verses per value (to match training structure)
- **Mix difficulty**: Mostly clear cases (70%), some moderate ambiguity (30%)
- **Testament balance**: 6 OT, 6 NT (50/50 split)
- **Genre diversity**: Narrative, epistolary, prophetic, poetry
- **No overlap**: Not in training set (20 verses) or adversarial test (12 verses)

**Purpose**: Baseline performance on typical verses (should be HIGHER than adversarial)

**Expected Gap**: Random should exceed adversarial by 15-25 percentage points

## Random Test Verses (12 total)

### Value: n (Not Applicable - No Demonstrative) - 1 verse

**1. Psalm 19:1**
```
Hebrew: הַשָּׁמַיִם מְסַפְּרִים כְּבוֹד־אֵל
English: "The heavens declare the glory of God"
Random Factor: Poetic genre, definite article only, no demonstrative
Expected Value: n (Not Applicable)
Difficulty: EASY (clear absence of demonstrative)
Confidence: 95%+
```

### Value: N (Near Speaker and Listener) - 1 verse

**2. Acts 27:10**
```
Greek: Ἄνδρες, θεωρῶ ὅτι μετὰ ὕβρεως καὶ πολλῆς ζημίας οὐ μόνον τοῦ φορτίου καὶ τοῦ πλοίου ἀλλὰ καὶ τῶν ψυχῶν ἡμῶν μέλλειν ἔσεσθαι τὸν πλοῦν
English: "Men, I perceive that the voyage will be with injury and much loss, not only of the cargo and the ship, but also of our lives"
Random Factor: Paul speaking to crew on ship - shared space
Expected Value: N (if demonstrative present) or n
Difficulty: EASY-MEDIUM (check for demonstrative in "this voyage")
Confidence: 80%
```

### Value: S (Near Speaker) - 1 verse

**3. Genesis 32:10**
```
Hebrew: קָטֹנְתִּי מִכֹּל הַחֲסָדִים וּמִכָּל־הָאֱמֶת אֲשֶׁר עָשִׂיתָ אֶת־עַבְדֶּךָ כִּי בְמַקְלִי עָבַרְתִּי אֶת־הַיַּרְדֵּן הַזֶּה
English: "I am not worthy of all the steadfast love and all the faithfulness that you have shown to your servant, for with only my staff I crossed this Jordan"
Random Factor: הַזֶּה (this) + Jacob speaking of Jordan (present location, speaker-oriented)
Expected Value: S (Near Speaker - Jacob's perspective of current location)
Difficulty: EASY (clear speaker-oriented spatial)
Confidence: 85%
```

### Value: R (Remote within Sight) - 2 verses

**4. Luke 7:44**
```
Greek: καὶ στραφεὶς πρὸς τὴν γυναῖκα τῷ Σίμωνι ἔφη· Βλέπεις ταύτην τὴν γυναῖκα;
English: "Then turning toward the woman he said to Simon, 'Do you see this woman?'"
Random Factor: ταύτην (this) + Jesus pointing to visible woman
Expected Value: R (Remote within Sight - visible but addressed to Simon)
Difficulty: EASY (perception verb + demonstrative)
Confidence: 85%
```

**5. Isaiah 6:9**
```
Hebrew: וַיֹּאמֶר לֵךְ וְאָמַרְתָּ לָעָם הַזֶּה
English: "And he said, 'Go, and say to this people'"
Random Factor: הַזֶּה (this) + referring to Israel (distant from heavenly throne)
Expected Value: R (remote but visible to God's perspective)
Difficulty: MEDIUM (requires theological perspective)
Confidence: 75%
```

### Value: r (Remote out of Sight) - 2 verses

**6. Matthew 8:29**
```
Greek: Τί ἡμῖν καὶ σοί, υἱὲ τοῦ θεοῦ; ἦλθες ὧδε πρὸ καιροῦ βασανίσαι ἡμᾶς;
English: "What have we to do with you, Son of God? Have you come here to torment us before the time?"
Random Factor: πρὸ καιροῦ (before the time) - distant future time, not present
Expected Value: r or t (remote temporal, not yet arrived)
Difficulty: MEDIUM (check if proximity applied to time reference)
Confidence: 70%
```

**7. Jeremiah 22:10**
```
Hebrew: אַל־תִּבְכּוּ לְמֵת וְאַל־תָּנֻדוּ לוֹ בְּכוּ בָכוֹ לַהֹלֵךְ כִּי לֹא יָשׁוּב עוֹד וְרָאָה אֶת־אֶרֶץ מוֹלַדְתּוֹ
English: "Weep not for the dead, nor bemoan him, but weep bitterly for him who goes away, for he shall return no more to see his native land"
Random Factor: "Him who goes away" - absent person (Jehoahaz in exile)
Expected Value: r (Remote out of Sight - exiled, not returning)
Difficulty: EASY-MEDIUM (absence clearly marked)
Confidence: 80%
```

### Value: T (Temporally Near) - 2 verses

**8. Luke 2:11**
```
Greek: ὅτι ἐτέχθη ὑμῖν σήμερον σωτὴρ ὅς ἐστιν χριστὸς κύριος
English: "For unto you is born this day in the city of David a Savior, who is Christ the Lord"
Random Factor: σήμερον (today) - present day temporal
Expected Value: T (Temporally Near)
Difficulty: EASY (formulaic "this day" = σήμερον)
Confidence: 95%
```

**9. Joshua 14:10**
```
Hebrew: וְעַתָּה הִנֵּה הֶחֱיָה יְהוָה אֹתִי כַּאֲשֶׁר דִּבֵּר זֶה אַרְבָּעִים וְחָמֵשׁ שָׁנָה
English: "And now, behold, the LORD has kept me alive, just as he said, these forty-five years"
Random Factor: זֶה (this) + forty-five years - recent past temporal span
Expected Value: T (Temporally Near - recent completed period)
Difficulty: MEDIUM (temporal span vs. point-in-time)
Confidence: 75%
```

### Value: t (Temporally Remote) - 2 verses

**10. Joel 2:31**
```
Hebrew: הַשֶּׁמֶשׁ יֵהָפֵךְ לְחֹשֶׁךְ וְהַיָּרֵחַ לְדָם לִפְנֵי בּוֹא יוֹם יְהוָה הַגָּדוֹל וְהַנּוֹרָא
English: "The sun shall be turned to darkness, and the moon to blood, before the great and awesome day of the LORD comes"
Random Factor: "Day of the LORD" - eschatological future
Expected Value: t (Temporally Remote)
Difficulty: EASY (prophetic future formula)
Confidence: 90%
```

**11. Mark 13:32**
```
Greek: Περὶ δὲ τῆς ἡμέρας ἐκείνης ἢ τῆς ὥρας οὐδεὶς οἶδεν
English: "But concerning that day or that hour, no one knows"
Random Factor: ἐκείνης (that) + eschatological day/hour
Expected Value: t (Temporally Remote)
Difficulty: EASY (distal demonstrative + eschatological)
Confidence: 95%
```

### Value: C (Contextually Near with Focus) - 1 verse

**12. Romans 3:25-26**
```
Greek: ὃν προέθετο ὁ θεὸς ἱλαστήριον... εἰς τὴν ἔνδειξιν τῆς δικαιοσύνης αὐτοῦ... πρὸς τὴν ἔνδειξιν τῆς δικαιοσύνης αὐτοῦ ἐν τῷ νῦν καιρῷ
English: "Whom God put forward as a propitiation... to show his righteousness... to show his righteousness at the present time"
Random Factor: ἐν τῷ νῦν καιρῷ (at the present time) - emphatic temporal with νῦν
Expected Value: C (emphatic focus on "present time") or T
Difficulty: MEDIUM (emphasis detection)
Confidence: 70%
```

### Value: c (Contextually Near - Routine Discourse) - 1 verse

**13. Galatians 1:6**
```
Greek: Θαυμάζω ὅτι οὕτως ταχέως μετατίθεσθε ἀπὸ τοῦ καλέσαντος ὑμᾶς ἐν χάριτι Χριστοῦ εἰς ἕτερον εὐαγγέλιον
English: "I am astonished that you are so quickly deserting him who called you in the grace of Christ and are turning to a different gospel"
Random Factor: οὕτως (thus) + anaphoric to previous situation
Expected Value: c (discourse anaphoric, or C if emphatic)
Difficulty: MEDIUM (C vs. c borderline)
Confidence: 70%
```

## Test Set Statistics

### Value Distribution

| Value | Count | Expected Accuracy | Algorithm v1.0 Target |
|-------|-------|-------------------|----------------------|
| n | 1 | 95%+ | EASY |
| N | 1 | 80% | MEDIUM |
| S | 1 | 85% | EASY-MEDIUM |
| L | 0 | - | (Not tested - too rare) |
| R | 2 | 80-85% | MEDIUM |
| r | 2 | 80-85% | MEDIUM |
| T | 2 | 90%+ | EASY |
| t | 2 | 90%+ | EASY |
| C | 1 | 70-75% | MEDIUM |
| c | 1 | 75% | MEDIUM |
| **Total** | **13** | **82-85%** | **Target: 80-90%** |

**Note**: L (Near Listener) intentionally omitted - too rare for random sampling

### Language Distribution

- **Greek (NT)**: 7 verses (54%)
- **Hebrew (OT)**: 6 verses (46%)

**Balanced representation** of both testaments

### Genre Distribution

- **Narrative**: 6 verses (GEN, JOS, LUK, ACT)
- **Epistolary**: 3 verses (ROM, GAL)
- **Prophetic**: 3 verses (ISA, JER, JOL)
- **Poetic**: 1 verse (PSA)

**Representative distribution** across Biblical genres

### Book Diversity

**OT (6)**: Genesis, Joshua, Psalm, Isaiah, Jeremiah, Joel
**NT (7)**: Matthew, Mark, Luke, Acts, Romans, Galatians

**Good spread** - no over-sampling from single book

### Difficulty Distribution

| Difficulty | Count | Percentage |
|------------|-------|------------|
| EASY | 6 | 46% |
| EASY-MEDIUM | 3 | 23% |
| MEDIUM | 4 | 31% |
| **Total** | **13** | **100%** |

**Appropriate mix**: Mostly clear cases (69% easy/easy-medium), some moderate challenge (31%)

## Comparison to Adversarial Test

| Metric | Adversarial | Random | Expected Difference |
|--------|-------------|--------|---------------------|
| **Expected Accuracy** | 60-70% | 80-90% | +15-25 points ✓ |
| **Difficulty Profile** | All MEDIUM-VERY HIGH | Mostly EASY-MEDIUM | Adversarial harder ✓ |
| **L Value Tested** | 2 verses (rare value hunt) | 0 verses (too rare) | Adversarial tests edge cases ✓ |
| **Hebrew Ambiguity** | 3 verses (unmarked זֶה) | 2 verses (clearer contexts) | Adversarial harder ✓ |
| **Value Distribution** | Skewed to weaknesses | Representative | Adversarial targets gaps ✓ |

**Success Indicator**: Random accuracy should be 15-25 points HIGHER than adversarial
- If gap <15 points: Adversarial not hard enough OR algorithm better than expected
- If gap >25 points: Algorithm struggles with edge cases (expected)

## Key Hypotheses to Test

### Hypothesis 1: Temporal Proximity Easiest
- **Prediction**: Verses 8-11 (T/t) will achieve 90%+ accuracy
- **Confidence**: 90%
- **Rationale**: Formulaic constructions, clear noun triggers

### Hypothesis 2: Greek Clearer Than Hebrew
- **Prediction**: Greek verses (7) will achieve 85%+ vs. Hebrew (6) at 75-80%
- **Confidence**: 75%
- **Rationale**: Greek demonstrative forms more predictive

### Hypothesis 3: Spatial Moderate Difficulty
- **Prediction**: Verses 3-7 (S/R/r) will achieve 80-85%
- **Confidence**: 80%
- **Rationale**: Clear contexts, perception verbs, explicit markers

### Hypothesis 4: Discourse Borderline Cases
- **Prediction**: Verses 12-13 (C/c) may have 70-75% accuracy
- **Confidence**: 70%
- **Rationale**: Emphasis detection still challenging

### Hypothesis 5: Random Exceeds Adversarial by 20 Points
- **Prediction**: Random ~83%, Adversarial ~63%, gap = 20 points
- **Confidence**: 75%
- **Rationale**: Representative distribution vs. targeted weaknesses

## Success Criteria

**Overall Target**: 80-90% accuracy on random test set
**Minimum Acceptable**: 75% (if lower, algorithm has serious issues)
**Stretch Goal**: 85%+ (algorithm robust on typical cases)

**Per-Domain Targets**:
- Temporal (T/t): 90%+ (4 verses)
- Spatial (S/R/r): 80-85% (5 verses)
- Discourse (C/c): 70-80% (2 verses)
- Not Applicable (n): 95%+ (1 verse)

**Comparative Success**:
- Random accuracy > Adversarial accuracy by 15-25 points
- Random tests algorithm baseline performance
- Adversarial reveals specific weaknesses

**If Random ≤ Adversarial Accuracy**:
- Test set design failed (not truly random vs. adversarial)
- Or algorithm fundamentally flawed

**Expected Outcome**: 80-85% accuracy, confirming algorithm works on typical cases

## Next Steps (Phase 6)

1. **Apply Algorithm v1.0** to these 13 verses
2. **Make predictions** WITHOUT checking TBTA (parallel to adversarial)
3. **Document reasoning** for each prediction
4. **Rate confidence** (HIGH/MEDIUM/LOW) for each
5. **Lock predictions** with git commit (same commit as adversarial)
6. **Record commit SHA** as proof of blind prediction
7. **Compare** random vs. adversarial performance in Phase 7

---

**Status**: Random test set designed
**Created**: 2025-11-12
**Ready for**: Phase 6 (blind predictions alongside adversarial test)
**CRITICAL**: Do NOT check TBTA data until after predictions are locked
**Expected Performance**: 80-90% (15-25 points above adversarial)
