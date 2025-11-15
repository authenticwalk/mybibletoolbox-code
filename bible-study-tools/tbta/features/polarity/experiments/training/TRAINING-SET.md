# Polarity Training Set

**Feature**: Polarity (Affirmative vs. Negative)
**Values**: 2 (Affirmative, Negative)
**Training verses**: 14 (7 Affirmative + 7 Negative)
**Design principle**: Equal value coverage with diverse negation types

**Date**: 2025-11-13
**Status**: Phase 2 - Training set designed
**Next**: Phase 3 - Access TBTA for training analysis

---

## Design Rationale

Polarity is a binary feature affecting ~50% of languages with specialized negative systems. Training set designed to cover:

1. **Negation types**: Existential (אֵין/nет), verbal (οὐ/μή), negative indefinites (οὐδείς)
2. **Source languages**: Hebrew (OT) and Greek (NT) patterns
3. **Syntactic diversity**: Subjects, objects, negative concord, prohibitions
4. **Special constructions**: Negative existentials, NPIs, genitive of negation triggers

**Equal coverage**: 7 Affirmative (clear cases) + 7 Negative (diverse negation patterns)

---

## Training Verses

### AFFIRMATIVE (7 verses)

**Purpose**: Establish baseline positive assertion patterns

#### 1. Genesis 1:1 (Hebrew)
```yaml
Reference: GEN 1:1
Hebrew: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
English: "In the beginning God created the heavens and the earth"
Constituents: God, heavens, earth
Expected Polarity: Affirmative (all)
Reason: No negation, baseline positive assertion
Morphology: No negative particles present
Context: Creation narrative, positive statement of fact
```

#### 2. Matthew 5:14 (Greek)
```yaml
Reference: MAT 5:14
Greek: Ὑμεῖς ἐστε τὸ φῶς τοῦ κόσμου
English: "You are the light of the world"
Constituents: You (disciples), light, world
Expected Polarity: Affirmative (all)
Reason: Positive identity statement, no negation
Morphology: No negative particles (οὐ/μή absent)
Context: Sermon on the Mount, positive declaration
```

#### 3. John 3:16 (Greek)
```yaml
Reference: JOH 3:16
Greek: οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον
English: "For God so loved the world"
Constituents: God, world
Expected Polarity: Affirmative (all)
Reason: Positive statement of divine love
Morphology: No negation present
Context: Key theological verse, affirmative tone throughout
```

#### 4. Psalm 23:1 (Hebrew)
```yaml
Reference: PSA 23:1
Hebrew: יְהוָה רֹעִי לֹא אֶחְסָר
English: "The LORD is my shepherd; I shall not want"
Constituents: LORD, shepherd
Expected Polarity: Affirmative (LORD, shepherd)
Reason: Positive statements about God (verb "want" has negation, not nouns)
Morphology: לֹא negates verb "want" only, not the nouns
Context: Confidence psalm, nouns affirmed despite verb negation
Note: Tests scope - nouns outside verb negation scope
```

#### 5. Genesis 2:18 (Hebrew)
```yaml
Reference: GEN 2:18
Hebrew: וַיֹּאמֶר יְהוָה אֱלֹהִים לֹא־טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ
English: "The LORD God said, It is not good that the man should be alone"
Constituents: LORD God, man
Expected Polarity: Affirmative (both nouns)
Reason: Nouns affirmed; negation on adjective "good", not nouns
Morphology: לֹא negates "good" (adjective/state), not participant nouns
Context: Tests negative evaluation vs. negative polarity of nouns
```

#### 6. Romans 1:16 (Greek)
```yaml
Reference: ROM 1:16
Greek: οὐ γὰρ ἐπαισχύνομαι τὸ εὐαγγέλιον
English: "For I am not ashamed of the gospel"
Constituents: I (Paul), gospel
Expected Polarity: Affirmative (both)
Reason: Verb negated, but nouns affirmed (Paul exists, gospel exists)
Morphology: οὐ negates verb "ashamed", not the participants
Context: Tests verbal negation not affecting noun polarity
```

#### 7. Exodus 20:2 (Hebrew)
```yaml
Reference: EXO 20:2
Hebrew: אָנֹכִי יְהוָה אֱלֹהֶיךָ אֲשֶׁר הוֹצֵאתִיךָ מֵאֶרֶץ מִצְרַיִם
English: "I am the LORD your God, who brought you out of the land of Egypt"
Constituents: I (God), LORD, God, you (Israel), land, Egypt
Expected Polarity: Affirmative (all)
Reason: Historical statement, all entities affirmed
Morphology: No negative particles
Context: Ten Commandments preamble, establishes positive identity
```

---

### NEGATIVE (7 verses)

**Purpose**: Cover diverse negation patterns and special constructions

#### 8. Genesis 19:31 (Hebrew) - Negative Existential
```yaml
Reference: GEN 19:31
Hebrew: וְאָבִינוּ זָקֵן וְאִישׁ אֵין בָּאָרֶץ לָבוֹא עָלֵינוּ
English: "Our father is old, and there is not a man in the earth to come in to us"
Constituents: father, man, earth
Expected Polarity: father=Affirmative, man=Negative, earth=Affirmative
Reason: Special negative existential אֵין negates "man" existence
Morphology: אֵין (ein) = "there is not" (special Hebrew negative existential)
Context: Lot's daughters, existential negation of available men
Language impact: Russian нет, Turkish yok parallel constructions
```

#### 9. Matthew 5:18 (Greek) - Emphatic Negation
```yaml
Reference: MAT 5:18
Greek: ἰῶτα ἓν ἢ μία κεραία οὐ μὴ παρέλθῃ ἀπὸ τοῦ νόμου
English: "Not one jot or one tittle shall in no wise pass from the law"
Constituents: jot (iota), tittle (keraia), law
Expected Polarity: jot=Negative, tittle=Negative, law=Affirmative
Reason: οὐ μή (emphatic negation) negates "jot" and "tittle" passing; law affirmed
Morphology: οὐ μή = strongest Greek negation (double negative for emphasis)
Context: Jesus on Torah permanence, universal negative quantification
Language impact: Negative concord languages require multiple negatives
```

#### 10. Romans 3:10 (Greek) - Negative Indefinite + NC
```yaml
Reference: ROM 3:10
Greek: οὐκ ἔστιν δίκαιος οὐδὲ εἷς
English: "There is no one righteous, not even one"
Constituents: one (person), righteous (one)
Expected Polarity: Negative (both)
Reason: οὐκ ἔστιν (negative copula) + οὐδὲ (not even) = negative concord
Morphology: οὐκ...οὐδέ = Greek negative concord pattern
Context: Paul's universal indictment, existential negation
Language impact: Spanish "no hay nadie justo" (NC required)
```

#### 11. Psalm 14:1 (Hebrew) - Negative Existential (Theological)
```yaml
Reference: PSA 14:1
Hebrew: אָמַר נָבָל בְּלִבּוֹ אֵין אֱלֹהִים
English: "The fool has said in his heart, There is no God"
Constituents: fool, heart, God
Expected Polarity: fool=Affirmative, heart=Affirmative, God=Negative (in quoted denial)
Reason: אֵין אֱלֹהִים = negative existential ("there is no God")
Morphology: אֵין + noun = standard negative existential construction
Context: Quoted speech - fool's denial, not assertion
Language impact: Tests negative existentials in embedded quotes
```

#### 12. John 1:18 (Greek) - Negative Indefinite
```yaml
Reference: JOH 1:18
Greek: θεὸν οὐδεὶς ἑώρακεν πώποτε
English: "No one has ever seen God"
Constituents: God, one (person)
Expected Polarity: God=Affirmative, one=Negative
Reason: οὐδείς (no one) = negative indefinite pronoun
Morphology: οὐδείς = οὐ + δείς (nobody), πώποτε (ever) reinforces
Context: Christological statement, universal negation
Language impact: English NPI "ever" required in negative context
```

#### 13. Genesis 37:29 (Hebrew) - Negative Existential (Absence)
```yaml
Reference: GEN 37:29
Hebrew: וְהִנֵּה אֵין־יוֹסֵף בַּבּוֹר
English: "And behold, Joseph was not in the pit"
Constituents: Joseph, pit
Expected Polarity: Joseph=Negative (absent), pit=Affirmative
Reason: אֵין־יוֹסֵף = "Joseph is not/there is no Joseph"
Morphology: אֵין + proper name = existential absence
Context: Reuben's discovery, Joseph taken by traders
Language impact: Existential vs. locative negation distinction
```

#### 14. 1 Corinthians 13:1 (Greek) - Negative Conditional
```yaml
Reference: 1CO 13:1
Greek: ἐὰν ταῖς γλώσσαις...λαλῶ ἀγάπην δὲ μὴ ἔχω
English: "If I speak in tongues...but have not love"
Constituents: I (Paul), tongues, love
Expected Polarity: I=Affirmative, tongues=Affirmative, love=Negative (in conditional)
Reason: μὴ ἔχω = "not have" - negates possession of love
Morphology: μή used in conditional/subjunctive contexts
Context: Love chapter, hypothetical negation
Language impact: Tests negation in conditional clauses
```

---

## Value Coverage Summary

| Value | Count | Percentage | Notes |
|-------|-------|------------|-------|
| Affirmative | 7 verses | 50% | Baseline positive assertions, scope testing |
| Negative | 7 verses | 50% | Diverse negation patterns (existential, indefinite, NC, conditional) |

**Coverage analysis**:
- ✅ Hebrew negative existential אֵין: 3 verses (GEN 19:31, PSA 14:1, GEN 37:29)
- ✅ Greek emphatic negation οὐ μή: 1 verse (MAT 5:18)
- ✅ Greek negative concord οὐκ...οὐδέ: 1 verse (ROM 3:10)
- ✅ Greek negative indefinite οὐδείς: 1 verse (JOH 1:18)
- ✅ Conditional negation μή: 1 verse (1CO 13:1)
- ✅ Verbal negation not affecting nouns: 3 verses (PSA 23:1, GEN 2:18, ROM 1:16)
- ✅ Testament balance: 7 OT (Hebrew), 7 NT (Greek)

---

## Negation Type Coverage

| Type | Verses | Notes |
|------|--------|-------|
| **Existential** | GEN 19:31, PSA 14:1, GEN 37:29 | אֵין constructions |
| **Emphatic** | MAT 5:18 | οὐ μή double negative |
| **Negative Concord** | ROM 3:10 | οὐκ...οὐδέ pattern |
| **Negative Indefinite** | JOH 1:18 | οὐδείς (no one) |
| **Conditional** | 1CO 13:1 | μή in hypotheticals |
| **Verbal (scope test)** | PSA 23:1, GEN 2:18, ROM 1:16 | Nouns outside negation scope |

---

## Cross-Linguistic Implications Tested

**Negative Concord** (ROM 3:10):
- Spanish: "no hay nadie justo, ni uno" (NC required)
- Russian: "нет ни одного праведного" (genitive + NC)

**Negative Existentials** (GEN 19:31, GEN 37:29, PSA 14:1):
- Russian: нет constructions (not regular negation)
- Turkish: yok (dedicated negative existential)

**NPIs** (JOH 1:18, MAT 5:18):
- English: "ever" (not "always") in negative context
- Japanese: も-series required

**Genitive of Negation** (ROM 3:10, potential):
- Russian: genitive case required for negated nouns
- Finnish: partitive case under negation

---

## Expected Learning Outcomes

**Phase 3 (Training Analysis) will discover**:
1. When TBTA marks nouns as Negative vs. Affirmative
2. How scope of negation affects noun polarity
3. Whether special constructions (אֵין, οὐδείς) always trigger Negative
4. If verbal negation affects noun polarity (predict: NO based on scope)
5. Negative concord patterns - which constituents get marked

**Algorithm v1.0 goals**:
- High accuracy (90%+) on binary distinction
- Clear scope rules (when nouns are in negation scope)
- Special construction handling (existentials, indefinites)
- Confidence ratings based on negation type

---

## Next Steps

1. **Phase 3**: Access TBTA for all 14 training verses
2. **Analysis**: Document patterns for each negation type
3. **Create**: `PATTERNS-LEARNED.md` with decision rules
4. **Lock**: `ALGORITHM-v1.md` with git commit
5. **Proceed**: Phase 5 (test set design) after algorithm locked

---

**Status**: Training set design complete
**Commit required**: Yes (git add + commit before Phase 3)
**Date**: 2025-11-13
**Phase**: 2 complete, ready for Phase 3
