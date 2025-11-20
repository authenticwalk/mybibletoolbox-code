# Proximity Feature: Adversarial Test Set

**Feature**: Proximity (TBTA position 8)
**Date Created**: 2025-11-12
**Phase**: 5 - Test Set Design
**Test Type**: Adversarial (challenging edge cases)
**Total Verses**: 12 (designed to challenge Algorithm v1.0)
**Target Accuracy**: 60-70% (challenging cases)

## Design Strategy

**Adversarial Focus**: Target Algorithm v1.0 weaknesses identified in Phase 4:
1. **N/S/L ambiguity** (3 verses) - Hardest spatial proximal distinctions
2. **Hebrew scene inference** (3 verses) - Unmarked זֶה requiring context
3. **C vs. c emphasis** (2 verses) - Discourse emphasis borderline cases
4. **R vs. r visibility** (2 verses) - Visibility inference challenges
5. **Rare L value** (2 verses) - Testing near-listener predictions

**No overlap with training set** - All verses are NEW

## Adversarial Test Verses (12 total)

### Category 1: N/S/L Spatial Ambiguity (3 verses)

**Challenge**: Algorithm v1.0 predicts 60-70% for N/S/L - test these boundaries

**1. Luke 22:19**
```
Greek: τοῦτο τὸ σῶμα τὸ ὑπὲρ ὑμῶν διδόμενον
English: "This is my body which is given for you"
Adversarial Factor: Similar to MAT 26:26 (training), but ὑπὲρ ὑμῶν ("for you") adds listener focus
Challenge: N (near both) or L (near listeners, "for you" emphasis)?
Expected Difficulty: HIGH
```

**2. Genesis 24:65**
```
Hebrew: מִי־הָאִישׁ הַלָּזֶה הַהֹלֵךְ בַּשָּׂדֶה
English: "Who is this man walking in the field?"
Adversarial Factor: הַלָּזֶה (hallaz, rare medial form) + distant visible person
Challenge: R (remote visible, hallaz documented as → R) or S (speaker-oriented question)?
Expected Difficulty: MEDIUM (tests rare הַלָּז form)
```

**3. John 4:12**
```
Greek: μὴ σὺ μείζων εἶ τοῦ πατρὸς ἡμῶν Ἰακώβ, ὃς ἔδωκεν ἡμῖν τὸ φρέαρ τοῦτο
English: "Are you greater than our father Jacob, who gave us this well?"
Adversarial Factor: "This well" physically present with both speaker (woman) and listener (Jesus)
Challenge: N (near both, present location) or c (discourse, "the aforementioned well")?
Expected Difficulty: HIGH (spatial vs. discourse boundary)
```

### Category 2: Hebrew Scene Inference (3 verses)

**Challenge**: Algorithm v1.0 predicts 65-75% for Hebrew spatial - test unmarked זֶה

**4. Genesis 27:21**
```
Hebrew: גְּשָׁה־נָּא וַאֲמֻשְׁךָ בְּנִי הַאַתָּה זֶה בְּנִי עֵשָׂו אִם־לֹא
English: "Come near that I may feel you, my son, to know whether you are really my son Esau or not"
Adversarial Factor: זֶה unmarked + tactile context (Isaac blind, touching Jacob)
Challenge: זֶה with "you" - S (near speaker Isaac) or L (near listener Jacob)?
Expected Difficulty: VERY HIGH (no visual scene, tactile proximity)
```

**5. Exodus 32:1**
```
Hebrew: זֶה מֹשֶׁה הָאִישׁ אֲשֶׁר הֶעֱלָנוּ מֵאֶרֶץ מִצְרַיִם לֹא יָדַעְנוּ מֶה־הָיָה לוֹ
English: "As for this Moses, the man who brought us up from Egypt, we do not know what has become of him"
Adversarial Factor: זֶה + Moses absent (remote), but demonstrative used
Challenge: r (remote invisible, Moses gone) or c (discourse, "this Moses we mentioned")?
Expected Difficulty: HIGH (absent referent with demonstrative)
```

**6. Deuteronomy 1:35**
```
Hebrew: אִם־יִרְאֶה אִישׁ בָּאֲנָשִׁים הָאֵלֶּה הַדּוֹר הָרָע הַזֶּה אֵת הָאָרֶץ הַטּוֹבָה
English: "Not one of these men of this evil generation shall see the good land"
Adversarial Factor: Multiple demonstratives - הָאֵלֶּה (these men) + הַזֶּה (this generation)
Challenge: "These men" - N/R? "This generation" - T (present) or c (discourse)?
Expected Difficulty: HIGH (multiple values in one verse)
```

### Category 3: Discourse Emphasis Detection (2 verses)

**Challenge**: Algorithm v1.0 predicts 75-85% for C vs. c - test borderline emphasis

**7. Matthew 12:31-32**
```
Greek: ἡ δὲ τοῦ πνεύματος βλασφημία οὐκ ἀφεθήσεται... πᾶς ὃς ἐὰν εἴπῃ λόγον κατὰ τοῦ υἱοῦ τοῦ ἀνθρώπου, ἀφεθήσεται αὐτῷ· ὃς δ' ἂν εἴπῃ κατὰ τοῦ πνεύματος τοῦ ἁγίου
English: "But the blasphemy against the Spirit will not be forgiven... whoever speaks a word against the Son of Man will be forgiven, but whoever speaks against the Holy Spirit..."
Adversarial Factor: No explicit demonstrative, but discourse contrast (Son vs. Spirit)
Challenge: Does τοῦ πνεύματος get proximity coding? If yes, C (focused contrast) or n (no demonstrative)?
Expected Difficulty: HIGH (implicit contrast vs. no marking)
```

**8. 1 Corinthians 15:3-4**
```
Greek: Χριστὸς ἀπέθανεν ὑπὲρ τῶν ἁμαρτιῶν ἡμῶν κατὰ τὰς γραφάς, καὶ ὅτι ἐτάφη, καὶ ὅτι ἐγήγερται τῇ ἡμέρᾳ τῇ τρίτῃ κατὰ τὰς γραφάς
English: "Christ died for our sins according to the Scriptures, and that he was buried, and that he was raised on the third day according to the Scriptures"
Adversarial Factor: τῇ ἡμέρᾳ τῇ τρίτῃ - "the third day" with double definite article
Challenge: No demonstrative, but "the third day" - n or t (temporal remote, past event)?
Expected Difficulty: MEDIUM (tests demonstrative requirement for temporal)
```

### Category 4: Visibility Inference (2 verses)

**Challenge**: Algorithm v1.0 predicts 75-85% for R vs. r - test ambiguous visibility

**9. Matthew 26:64**
```
Greek: ἀπ' ἄρτι ὄψεσθε τὸν υἱὸν τοῦ ἀνθρώπου καθήμενον ἐκ δεξιῶν τῆς δυνάμεως καὶ ἐρχόμενον ἐπὶ τῶν νεφελῶν τοῦ οὐρανοῦ
English: "From now on you will see the Son of Man sitting at the right hand of Power and coming on the clouds of heaven"
Adversarial Factor: Future vision ("you will see") of eschatological event
Challenge: Future visible (R) or currently invisible (r)?
Expected Difficulty: HIGH (future visibility prediction)
```

**10. Revelation 1:7**
```
Greek: ἰδοὺ ἔρχεται μετὰ τῶν νεφελῶν, καὶ ὄψεται αὐτὸν πᾶς ὀφθαλμός
English: "Behold, he is coming with the clouds, and every eye will see him"
Adversarial Factor: ἰδού (behold, deictic) + future coming + future visibility
Challenge: r (currently invisible) or R (eschatological vision treated as "visible")?
Expected Difficulty: HIGH (eschatological visibility)
```

### Category 5: Rare L Value Testing (2 verses)

**Challenge**: Algorithm v1.0 predicts 50-60% for L - test if L exists or defaults to R

**11. Matthew 15:26**
```
Greek: οὐκ ἔστιν καλὸν λαβεῖν τὸν ἄρτον τῶν τέκνων καὶ βαλεῖν τοῖς κυναρίοις
English: "It is not right to take the children's bread and throw it to the dogs"
Adversarial Factor: "The bread" (listener-oriented, "your bread" implied), "the dogs" (near listener metaphor)
Challenge: L (listener-oriented, Canaanite woman's perspective) or c (discourse, abstract)?
Expected Difficulty: VERY HIGH (tests L value existence)
```

**12. Luke 19:5**
```
Greek: σήμερον γὰρ ἐν τῷ οἴκῳ σου δεῖ με μεῖναι
English: "For today I must stay at your house"
Adversarial Factor: σου (your house) - listener's house (Zacchaeus)
Challenge: τῷ οἴκῳ σου - L (listener's house) or R (distant but referenced)?
Expected Difficulty: HIGH (possessive + listener location)
```

## Test Set Statistics

### Value Distribution (Predicted Challenges)

| Value | Count | Expected Difficulty | Algorithm v1.0 Target |
|-------|-------|---------------------|----------------------|
| n | 1 | LOW | 95%+ |
| N | 2 | VERY HIGH | 60-70% |
| S | 1 | HIGH | 65-70% |
| L | 2 | VERY HIGH | 50-60% |
| R | 2 | HIGH | 75-80% |
| r | 2 | HIGH | 75-85% |
| T | 0 | - | (not tested) |
| t | 1 | MEDIUM | 85-90% |
| C | 1 | HIGH | 80-85% |
| c | 2 | MEDIUM | 75-80% |

**Note**: Value distribution reflects areas of algorithm weakness (spatial proximal emphasized)

### Language Distribution

- **Greek (NT)**: 8 verses (67%)
- **Hebrew (OT)**: 4 verses (33%)

**Rationale**: Greek has more explicit forms but still ambiguous contexts; Hebrew tests unmarked זֶה inference

### Book Diversity

**NT**: Matthew (4), Luke (2), John (1), 1 Corinthians (1), Revelation (1)
**OT**: Genesis (2), Exodus (1), Deuteronomy (1)

### Adversarial Categories

| Category | Count | Focus | Expected Accuracy |
|----------|-------|-------|-------------------|
| N/S/L Ambiguity | 3 | Spatial proximal | 50-60% |
| Hebrew Scene Inference | 3 | Unmarked זֶה | 55-65% |
| Discourse Emphasis | 2 | C vs. c vs. n | 60-70% |
| Visibility Inference | 2 | R vs. r | 60-70% |
| Rare L Value | 2 | L existence | 40-50% |

### Overall Expected Performance

**Target**: 60-70% exact match accuracy
- If >75%: Test wasn't adversarial enough
- If <50%: Algorithm has fundamental issues
- If 60-70%: Success - algorithm handles most cases, reveals clear weaknesses

## Key Hypotheses to Test

### Hypothesis 1: L (Near Listener) Is Extremely Rare
- **Prediction**: Verses 11-12 will NOT use L, will use R or c instead
- **Confidence**: 70% (Greek L is documented as rare)
- **If wrong**: Update algorithm to better detect L contexts

### Hypothesis 2: Hebrew זֶה Requires Complex Scene Analysis
- **Prediction**: Verses 4-6 will have <60% accuracy (hardest cases)
- **Confidence**: 80%
- **If wrong**: Context clues are more reliable than expected

### Hypothesis 3: Discourse Emphasis Is Gradient
- **Prediction**: C vs. c distinction will be ambiguous in verse 7
- **Confidence**: 75%
- **If wrong**: TBTA has clearer emphasis thresholds than we predicted

### Hypothesis 4: Eschatological Visibility Treated Differently
- **Prediction**: Verses 9-10 will use r (not yet visible) not R
- **Confidence**: 65%
- **If wrong**: TBTA treats prophetic "you will see" as R (visible)

### Hypothesis 5: Spatial vs. Discourse Boundary Is Fuzzy
- **Prediction**: Verse 3 (JHN 4:12 "this well") could be N or c, both valid
- **Confidence**: 70%
- **If wrong**: TBTA has clearer spatial/discourse rules

## Success Criteria

**Overall Target**: 60-70% accuracy on adversarial test set
**Per-Category Targets**:
- N/S/L: 50-60% (hardest, expected low)
- Hebrew: 55-65% (challenging inference)
- Discourse: 60-70% (emphasis ambiguity)
- Visibility: 60-70% (inference difficulty)
- L value: 40-50% (rare, may not exist)

**If Algorithm v1.0 Exceeds 75%**:
- Adversarial test wasn't challenging enough
- Need harder edge cases
- Or algorithm is better than expected (unlikely)

**If Algorithm v1.0 Below 50%**:
- Fundamental algorithm issues
- Need significant revision
- Revisit patterns learned

**Expected Outcome**: 60-70% accuracy, revealing systematic weaknesses for Algorithm v2.0

## Next Steps (Phase 6)

1. **Apply Algorithm v1.0** to these 12 verses
2. **Make predictions** WITHOUT checking TBTA
3. **Document reasoning** for each prediction
4. **Rate confidence** (HIGH/MEDIUM/LOW) for each
5. **Lock predictions** with git commit (before checking TBTA)
6. **Record commit SHA** as proof of blind prediction

---

**Status**: Adversarial test set designed
**Created**: 2025-11-12
**Ready for**: Phase 6 (blind predictions)
**CRITICAL**: Do NOT check TBTA data until after predictions are locked
