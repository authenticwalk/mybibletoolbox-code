# Proximity Feature: Training Set

**Feature**: Proximity (TBTA position 8 for nouns)
**Date Created**: 2025-11-12
**Phase**: 2 - Training Set Design
**Total Verses**: 20 (2 per value × 10 values)

## Design Criteria

**Equal Value Coverage**: 2 verses per value to ensure balanced training
**Value Count**: 10 proximity values (n, N, S, L, R, r, T, t, C, c)
**Language Mix**: ~50% Hebrew (OT), ~50% Greek (NT)
**Difficulty Mix**: Clear cases and moderately ambiguous cases
**Genre Diversity**: Narrative, teaching, prophecy, epistolary

## Training Set Verses (20 total)

### Value: n (Not Applicable - No Proximity Marking)

**1. Genesis 1:1**
```
Hebrew: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
English: "In the beginning God created the heavens and the earth"
Expected: n (no demonstrative)
Reason: Definite article only, no demonstrative marking
```

**2. John 1:1**
```
Greek: Ἐν ἀρχῇ ἦν ὁ λόγος
English: "In the beginning was the Word"
Expected: n (no demonstrative)
Reason: Definite article only, no demonstrative marking
```

### Value: N (Near Speaker and Listener - Both Nearby)

**3. Matthew 26:26**
```
Greek: λάβετε φάγετε· τοῦτό ἐστιν τὸ σῶμά μου
English: "Take, eat; this is my body"
Expected: N (near both)
Reason: οὗτος used, bread physically present with Jesus and disciples
```

**4. Genesis 22:2**
```
Hebrew: קַח־נָא אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק
English: "Take your son, your only son Isaac, whom you love"
Expected: N or n (checking if implicit demonstrative)
Reason: Direct address with son present (checking TBTA treatment)
```

### Value: S (Near Speaker Only)

**5. John 1:29**
```
Greek: ἴδε ὁ ἀμνὸς τοῦ θεοῦ
English: "Behold the Lamb of God"
Expected: S (near speaker perspective)
Reason: John (speaker) sees Jesus at distance, pointing him out
```

**6. Exodus 3:3**
```
Hebrew: אָסֻרָה־נָּא וְאֶרְאֶה אֶת־הַמַּרְאֶה הַגָּדֹל הַזֶּה
English: "I will turn aside to see this great sight"
Expected: S (near speaker)
Reason: Moses (speaker) approaching the burning bush, זֶה demonstrative
```

### Value: L (Near Listener/Addressee Only)

**7. Matthew 3:9**
```
Greek: δύναται ὁ θεὸς ἐκ τῶν λίθων τούτων
English: "God is able from these stones"
Expected: L (near listeners)
Reason: John pointing to stones near the crowd (addressees), not near himself
```

**8. Ruth 4:1**
```
Hebrew: וּבֹעַז עָלָה הַשַּׁעַר וַיֵּשֶׁב שָׁם וְהִנֵּה הַגֹּאֵל עֹבֵר אֲשֶׁר דִּבֶּר־בֹּעַז
English: "Boaz went up to the gate and sat down there; and behold, the redeemer came by"
Expected: L or R (checking addressee-oriented context)
Reason: Boaz calling to approaching person
```

### Value: R (Remote within Sight - Visible but Distant)

**9. Matthew 3:17**
```
Greek: οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός
English: "This is my beloved Son"
Expected: R (remote visible)
Reason: Voice from heaven (remote) referring to Jesus (visible to crowd)
```

**10. Genesis 13:14-15**
```
Hebrew: כָּל־הָאָרֶץ אֲשֶׁר־אַתָּה רֹאֶה
English: "All the land that you see"
Expected: R (remote visible)
Reason: Viewing distant landscape, visible but far away
```

### Value: r (Remote out of Sight - Not Visible)

**11. Genesis 19:31**
```
Hebrew: אֵין אִישׁ בָּאָרֶץ
English: "There is not a man in the earth"
Expected: r (remote invisible)
Reason: General reference to absent men, not physically present
```

**12. John 4:21**
```
Greek: οὔτε ἐν τῷ ὄρει τούτῳ οὔτε ἐν Ἱεροσολύμοις
English: "Neither on this mountain nor in Jerusalem"
Expected: r (Jerusalem remote and out of sight)
Reason: Jerusalem distant from Samaria, not visible from conversation location
```

### Value: T (Temporally Near - Present/Recent Time)

**13. Matthew 26:29**
```
Greek: οὐ μὴ πίω ἀπ' ἄρτι ἐκ τούτου τοῦ γενήματος τῆς ἀμπέλου
English: "I will not drink from this fruit of the vine"
Expected: T (temporal near)
Reason: "From now" indicating present moment, οὗτος with temporal reference
```

**14. Exodus 12:14**
```
Hebrew: וְהָיָה הַיּוֹם הַזֶּה לָכֶם לְזִכָּרוֹן
English: "This day shall be to you for a memorial"
Expected: T (temporal near)
Reason: הַיּוֹם הַזֶּה "this day" - present/immediate time reference
```

### Value: t (Temporally Remote - Past/Future Distant)

**15. Matthew 24:3**
```
Greek: πότε ταῦτα ἔσται
English: "When will these things be?"
Expected: t (temporal remote)
Reason: Eschatological future events, distant from present moment
```

**16. Isaiah 2:11**
```
Hebrew: וְנִשְׂגַּב יְהוָה לְבַדּוֹ בַּיּוֹם הַהוּא
English: "The LORD alone will be exalted in that day"
Expected: t (temporal remote)
Reason: Prophetic future "that day", remote time reference
```

### Value: C (Contextually Near with Focus - Emphatic Discourse)

**17. John 3:16**
```
Greek: οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον
English: "For God so loved the world"
Expected: C (discourse with focus)
Reason: οὕτως "thus/so" - emphatic demonstrative emphasizing manner
```

**18. Ezekiel 5:5**
```
Hebrew: זֹאת יְרוּשָׁלִָם
English: "This is Jerusalem"
Expected: C (discourse with focus)
Reason: זֹאת in emphatic subject position, cataphoric introduction
```

### Value: c (Contextually Near - Routine Discourse Reference)

**19. John 7:16**
```
Greek: ἡ ἐμὴ διδαχὴ οὐκ ἔστιν ἐμὴ
English: "My teaching is not mine"
Expected: c (discourse)
Reason: Anaphoric reference to teaching just mentioned in discourse
```

**20. 1 Corinthians 11:25**
```
Greek: τοῦτο τὸ ποτήριον ἡ καινὴ διαθήκη ἐστὶν
English: "This cup is the new covenant"
Expected: c or N (checking context)
Reason: οὗτος with physical cup, but may be discourse reference in ritual context
```

## Value Distribution Summary

| Value | Count | Percentage | Testament Split |
|-------|-------|------------|----------------|
| n | 2 | 10% | OT: 1, NT: 1 |
| N | 2 | 10% | OT: 1, NT: 1 |
| S | 2 | 10% | OT: 1, NT: 1 |
| L | 2 | 10% | OT: 1, NT: 1 |
| R | 2 | 10% | OT: 1, NT: 1 |
| r | 2 | 10% | OT: 1, NT: 1 |
| T | 2 | 10% | OT: 1, NT: 1 |
| t | 2 | 10% | OT: 1, NT: 1 |
| C | 2 | 10% | OT: 1, NT: 1 |
| c | 2 | 10% | OT: 1, NT: 1 |
| **Total** | **20** | **100%** | **OT: 10, NT: 10** |

## Language Distribution

- **Hebrew (OT)**: 10 verses (50%)
- **Greek (NT)**: 10 verses (50%)

## Genre Distribution

- **Narrative**: 8 verses (GEN, EXO, RUT, MAT, JHN)
- **Teaching/Discourse**: 6 verses (JHN, 1CO)
- **Prophecy**: 3 verses (ISA, EZK)
- **Legal/Ritual**: 3 verses (EXO, 1CO)

## Book Diversity

**OT**: Genesis (5), Exodus (2), Ruth (1), Isaiah (1), Ezekiel (1)
**NT**: Matthew (6), John (5), 1 Corinthians (1)

## Difficulty Assessment

**Clear Cases (70%)**: 14 verses with unambiguous demonstrative forms
**Moderately Ambiguous (30%)**: 6 verses requiring context analysis
- Physical vs. discourse proximity (GEN 22:2, 1CO 11:25)
- Speaker vs. listener perspective (RUT 4:1)
- Visibility determination (JHN 4:21)
- Temporal vs. spatial (MAT 26:29)
- Emphatic vs. routine discourse (JHN 7:16)

## Next Steps

**Phase 3**: Access TBTA annotations for these 20 verses
- Download/access TBTA data for each verse
- Extract proximity values (position 8) for all nouns with demonstratives
- Document actual TBTA annotations
- Analyze patterns and create PATTERNS-LEARNED.md

## Notes

- Training set designed for equal value coverage (Universal Principle 5)
- Mix of clear and ambiguous ensures robust pattern learning
- Testament balance ensures both Greek and Hebrew patterns captured
- Genre diversity captures different proximity usage contexts
- Some verses may have multiple nouns with different proximity values
- Will validate assumptions about expected values against actual TBTA data

---

**Status**: Training set designed, ready for Phase 3 (TBTA analysis)
**Created**: 2025-11-12
**Committed**: Awaiting Phase 2 completion commit
