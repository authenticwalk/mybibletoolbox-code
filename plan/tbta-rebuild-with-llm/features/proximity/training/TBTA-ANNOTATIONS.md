# Proximity Feature: TBTA Annotations Analysis

**Feature**: Proximity (TBTA position 8 for nouns)
**Date**: 2025-11-12
**Phase**: 3 - Training Analysis
**Status**: Theoretical patterns documented (awaiting TBTA data access for validation)

## Data Access Status

**CRITICAL NOTE**: Similar to discourse-genre feature, actual TBTA data access for proximity annotations is currently limited. The patterns documented here are based on:

1. **Linguistic analysis** of Greek/Hebrew demonstrative systems
2. **Cross-linguistic typology** research (WALS, language-specific grammars)
3. **Existing proximity research** (LEARNINGS.md, experiment-001.md)
4. **Source text analysis** of training set verses

**Validation Strategy**: Patterns will be validated against TBTA data when accessible, following the same approach as other features.

## Training Set Annotation Predictions

Based on linguistic analysis, here are the expected TBTA annotations for our 20 training verses:

### Value: n (Not Applicable)

**1. Genesis 1:1** - "In the beginning God created..."
```yaml
verse: GEN 1:1
constituents_analyzed:
  - "heavens" (הַשָּׁמַיִם)
  - "earth" (הָאָרֶץ)
predicted_proximity: n
reasoning: Definite article only, no demonstrative marking
confidence: HIGH (95%)
source_evidence: No זֶה or demonstrative present
```

**2. John 1:1** - "In the beginning was the Word"
```yaml
verse: JHN 1:1
constituents_analyzed:
  - "Word" (λόγος)
predicted_proximity: n
reasoning: Definite article only, no demonstrative
confidence: HIGH (95%)
source_evidence: No ὅδε/οὗτος/ἐκεῖνος present
```

### Value: N (Near Speaker and Listener)

**3. Matthew 26:26** - "This is my body"
```yaml
verse: MAT 26:26
constituents_analyzed:
  - "body" (σῶμά)
greek_form: τοῦτό (neuter singular of οὗτος)
predicted_proximity: N
reasoning: Bread physically present with both Jesus (speaker) and disciples (listeners)
confidence: HIGH (85%)
source_evidence: οὗτος + physical object + both present
context: Last Supper scene, bread in shared space
```

**4. Genesis 22:2** - "Take your son"
```yaml
verse: GEN 22:2
constituents_analyzed:
  - "son" (בִּנְךָ)
predicted_proximity: n or N (uncertain)
reasoning: Direct address with son present, but no explicit demonstrative
confidence: MEDIUM (60%)
source_evidence: No זֶה, but context implies presence
context: Abraham and Isaac both present in scene
note: May not receive proximity marking without explicit demonstrative
```

### Value: S (Near Speaker)

**5. John 1:29** - "Behold the Lamb of God"
```yaml
verse: JHN 1:29
constituents_analyzed:
  - "Lamb" (ἀμνός)
predicted_proximity: S (near speaker) or R (remote visible)
reasoning: John (speaker) sees Jesus at distance, pointing him out
confidence: MEDIUM (70%)
source_evidence: ἴδε (imperative "behold") + ὁ ἀμνός (definite article, possible demonstrative function)
context: John standing by Jordan, Jesus approaching but at distance
cross_reference: Spatial deixis with perception verb
```

**6. Exodus 3:3** - "I will turn aside to see this great sight"
```yaml
verse: EXO 3:3
constituents_analyzed:
  - "sight" (הַמַּרְאֶה)
hebrew_form: הַזֶּה (this)
predicted_proximity: S
reasoning: Moses (speaker) approaching the burning bush, from his perspective
confidence: HIGH (85%)
source_evidence: זֶה demonstrative + first person verb ("I will turn")
context: Moses alone, object near to his position
```

### Value: L (Near Listener/Addressee)

**7. Matthew 3:9** - "God is able from these stones"
```yaml
verse: MAT 3:9
constituents_analyzed:
  - "stones" (λίθων)
greek_form: τούτων (genitive plural of οὗτος)
predicted_proximity: L or R
reasoning: John pointing to stones near the crowd (addressees), not near himself
confidence: MEDIUM (65%)
source_evidence: οὗτος + second person context ("Do not presume to say to yourselves")
context: John addressing crowd, stones on ground near them
note: L value is rare in Greek; may default to R
```

**8. Ruth 4:1** - "The redeemer came by"
```yaml
verse: RUT 4:1
constituents_analyzed:
  - "redeemer" (הַגֹּאֵל)
predicted_proximity: L or R
reasoning: Boaz calling to approaching person
confidence: LOW (50%)
source_evidence: הִנֵּה (behold) + approaching context
context: Boaz at gate, calling to person passing by
note: May be R (remote visible) rather than L (near listener)
```

### Value: R (Remote within Sight)

**9. Matthew 3:17** - "This is my beloved Son"
```yaml
verse: MAT 3:17
constituents_analyzed:
  - "Son" (υἱός)
greek_form: οὗτός
predicted_proximity: R
reasoning: Voice from heaven (remote) referring to Jesus (visible to crowd)
confidence: HIGH (80%)
source_evidence: οὗτος + spatial separation (heaven → earth)
context: God speaking from above, Jesus below at baptism
theological: Divine speech with visible earthly referent
```

**10. Genesis 13:14-15** - "All the land that you see"
```yaml
verse: GEN 13:14-15
constituents_analyzed:
  - "land" (הָאָרֶץ)
predicted_proximity: R
reasoning: Viewing distant landscape, visible but far away
confidence: HIGH (85%)
source_evidence: רֹאֶה (seeing) + panoramic view context
context: Abraham on hill viewing land, vast distance
```

### Value: r (Remote out of Sight)

**11. Genesis 19:31** - "There is not a man in the earth"
```yaml
verse: GEN 19:31
constituents_analyzed:
  - "man" (אִישׁ)
predicted_proximity: r
reasoning: General reference to absent men, not physically present
confidence: HIGH (85%)
source_evidence: אֵין (there is not) + general reference
context: Lot's daughters in cave, speaking of absent men
```

**12. John 4:21** - "Neither on this mountain nor in Jerusalem"
```yaml
verse: JHN 4:21
constituents_analyzed:
  - "mountain" (ὄρει)
  - "Jerusalem" (Ἱεροσολύμοις)
greek_form: τούτῳ (this mountain)
predicted_proximity:
  - mountain: S or N (present location)
  - Jerusalem: r (remote out of sight)
reasoning: Currently on mountain (proximal), Jerusalem distant and not visible
confidence: MEDIUM (70%)
source_evidence: οὗτος for mountain (present), plain reference for Jerusalem (absent)
context: Samaritan woman and Jesus at Jacob's well on Mt. Gerizim
```

### Value: T (Temporally Near)

**13. Matthew 26:29** - "I will not drink from this fruit of the vine"
```yaml
verse: MAT 26:29
constituents_analyzed:
  - "fruit" (γενήματος)
greek_form: τούτου (genitive of οὗτος)
predicted_proximity: T or N (ambiguous: temporal vs spatial)
reasoning: "From now" (ἀπ' ἄρτι) indicates present/near temporal reference
confidence: MEDIUM (65%)
source_evidence: οὗτος + temporal marker ἀπ' ἄρτι + physical cup present
context: Last Supper, transitional moment
note: Could be N (spatial with cup) or T (temporal "this moment")
```

**14. Exodus 12:14** - "This day shall be to you for a memorial"
```yaml
verse: EXO 12:14
constituents_analyzed:
  - "day" (הַיּוֹם)
hebrew_form: הַזֶּה (this)
predicted_proximity: T
reasoning: "This day" - present/immediate temporal reference (Passover)
confidence: HIGH (90%)
source_evidence: הַיּוֹם הַזֶּה construction (classic "this day" formula)
context: Establishment of Passover memorial on that very day
```

### Value: t (Temporally Remote)

**15. Matthew 24:3** - "When will these things be?"
```yaml
verse: MAT 24:3
constituents_analyzed:
  - "things" (implied referent: events)
greek_form: ταῦτα (neuter plural of οὗτος)
predicted_proximity: t
reasoning: Eschatological future events, distant from present moment
confidence: HIGH (85%)
source_evidence: οὗτος + future tense ἔσται + eschatological discourse
context: Disciples asking about end times, prophetic future
```

**16. Isaiah 2:11** - "The LORD alone will be exalted in that day"
```yaml
verse: ISA 2:11
constituents_analyzed:
  - "day" (יוֹם)
hebrew_form: הַהוּא (that)
predicted_proximity: t
reasoning: Prophetic future "that day" - remote time reference
confidence: HIGH (90%)
source_evidence: בַּיּוֹם הַהוּא construction (classic "that day" formula)
context: Prophetic oracle about future judgment
```

### Value: C (Contextually Near with Focus)

**17. John 3:16** - "For God so loved the world"
```yaml
verse: JHN 3:16
constituents_analyzed:
  - "manner/thus" (implied demonstrative)
greek_form: οὕτως (thus, so)
predicted_proximity: C
reasoning: Emphatic demonstrative adverb emphasizing manner, high discourse focus
confidence: HIGH (85%)
source_evidence: οὕτως (demonstrative adverb) + γὰρ (emphatic "for")
context: Climactic statement in Nicodemus discourse
note: οὕτως is adverbial, but modifies how God loved (demonstrative manner)
```

**18. Ezekiel 5:5** - "This is Jerusalem"
```yaml
verse: EZK 5:5
constituents_analyzed:
  - "Jerusalem" (יְרוּשָׁלִָם)
hebrew_form: זֹאת (this - feminine)
predicted_proximity: C
reasoning: Emphatic subject position, cataphoric introduction with focus
confidence: HIGH (85%)
source_evidence: זֹאת in subject position + predicate nominative
context: Prophetic declaration introducing focused judgment
```

### Value: c (Contextually Near - Routine Discourse)

**19. John 7:16** - "My teaching is not mine"
```yaml
verse: JHN 7:16
constituents_analyzed:
  - "teaching" (διδαχὴ)
predicted_proximity: c
reasoning: Anaphoric reference to teaching just mentioned, routine discourse reference
confidence: HIGH (80%)
source_evidence: ἡ ἐμὴ διδαχὴ (the my teaching) with definite article + possessive
context: Jesus responding to questions about his teaching (v. 15)
note: May not have explicit demonstrative, relying on definite article for discourse reference
```

**20. 1 Corinthians 11:25** - "This cup is the new covenant"
```yaml
verse: 1CO 11:25
constituents_analyzed:
  - "cup" (ποτήριον)
greek_form: τοῦτο (neuter of οὗτος)
predicted_proximity: c or N (ambiguous)
reasoning: Physical cup present (N) but also discourse/ritual reference (c)
confidence: MEDIUM (60%)
source_evidence: οὗτος + physical object + ritual context
context: Lord's Supper institution, repeated ritual formula
note: Borderline between spatial (cup present) and discourse (ritual formula)
```

## Pattern Summary from Training Set

### Source Language Demonstratives

**Greek Patterns:**
- **οὗτος** (houtos) - Most common, used for:
  - Spatial proximity (N, S, occasionally L)
  - Discourse proximity (c, C)
  - Temporal proximity (T)
  - Context determines which domain

- **ἐκεῖνος** (ekeinos) - Distal, used for:
  - Remote spatial (R, r)
  - Temporal remote (t)

- **ὅδε** (hode) - Immediate proximal (not in training set, but documented as → N/S)

**Hebrew Patterns:**
- **זֶה/זֹאת/אֵלֶּה** (zeh/zot/elleh) - Unmarked, requires context:
  - Can map to any proximity value
  - Context analysis critical
  - Defaults to discourse (c) if ambiguous

- **הַלָּז** (hallaz) - Always medial spatial (R) - (not in training set, but documented)

### Domain Classification Hierarchy

**Priority Decision Tree (from training set):**

1. **Temporal Nouns** + Demonstrative → T or t
   - "This day" → T (90% confidence)
   - "That day" → t (90% confidence)
   - Clearest pattern, highest accuracy expected

2. **Physical Scene** + Concrete Noun + Demonstrative → Spatial (N/S/L/R/r)
   - Speaker/listener positioning determines N vs S vs L
   - Visibility determines R vs r
   - Medium confidence (65-85%) - requires scene analysis

3. **Abstract Noun** or **No Physical Scene** → Discourse (C/c)
   - Emphasis markers (subject position, fronting) → C
   - Routine anaphoric → c
   - Medium confidence (70-85%) - requires syntactic analysis

4. **No Demonstrative** → n (Not Applicable)
   - High confidence (95%)

### Confidence Levels by Category

| Proximity Type | Training Examples | Expected Accuracy | Key Factors |
|----------------|-------------------|-------------------|-------------|
| **n** (Not Applicable) | 2 verses | 95%+ | Easy: absence of demonstrative |
| **T/t** (Temporal) | 4 verses | 85-90% | Easy: temporal nouns are clear |
| **C** (Discourse Focus) | 2 verses | 80-85% | Medium: emphasis detection |
| **c** (Discourse Routine) | 2 verses | 75-80% | Medium: anaphoric tracking |
| **R** (Remote Visible) | 2 verses | 75-80% | Medium: visibility inference |
| **r** (Remote Invisible) | 2 verses | 80-85% | Medium: absence marking |
| **N** (Near Both) | 2 verses | 70-75% | Hard: both present determination |
| **S** (Near Speaker) | 2 verses | 65-70% | Hard: speaker perspective |
| **L** (Near Listener) | 2 verses | 50-60% | Very Hard: rare in source languages |

### Key Uncertainties

**High Uncertainty Cases (3 verses):**
1. **MAT 26:29**: Temporal (T) vs. Spatial (N) - physical cup vs. temporal moment
2. **1CO 11:25**: Spatial (N) vs. Discourse (c) - physical vs. ritual formula
3. **RUT 4:1**: Listener-oriented (L) vs. Remote (R) - rare L value

**Medium Uncertainty Cases (5 verses):**
1. **GEN 22:2**: No explicit demonstrative, may be n rather than N
2. **JHN 1:29**: Speaker (S) vs. Remote (R) - John's perspective vs. distance
3. **MAT 3:9**: Listener (L) vs. Remote (R) - Greek L is rare
4. **JHN 4:21**: Two values in one verse (S/N for mountain, r for Jerusalem)
5. **JHN 7:16**: May lack explicit demonstrative coding (definite article only)

## Cross-Linguistic Validation Notes

### Expected Target Language Patterns

**2-Way Systems** (English, Germanic - 54% of languages):
- N/S/L → "this"
- R/r → "that"
- T → "this" (time)
- t → "that" (time)
- C/c → "this" (discourse)

**3-Way Person-Oriented** (Spanish, Japanese - 38% of languages):
- N → "este/これ" (near speaker, or near both)
- S → "este/これ" (near speaker)
- L → "ese/それ" (near hearer)
- R/r → "aquel/あれ" (far from both)

**3-Way Distance** (Some Bantu, Polynesian):
- N/S → Proximal
- R → Medial
- r → Distal

**Visibility Systems** (Austronesian, Amazonian):
- R (visible) vs. r (invisible) distinction critical
- May not distinguish speaker/listener (N vs S vs L)

### Special Cases Requiring Target Language Knowledge

1. **Elevation Systems** (Trans-New Guinea): May need vertical axis (up/down)
   - Not testable from training set without explicit vertical context

2. **Multimodal Deixis** (Some Amazonian): May encode gestural deixis
   - Source text doesn't preserve gesture, must infer

3. **Honorific Demonstratives** (Japanese, Korean): May encode social distance
   - Not marked in TBTA proximity, separate feature

## Validation Strategy

### When TBTA Data Becomes Available:

1. **Check each training verse** against actual TBTA proximity annotations
2. **Calculate accuracy** overall and per-value
3. **Identify systematic errors**:
   - Are temporal (T/t) predictions accurate? (expected: 85-90%)
   - Is Greek ἐκεῖνος reliably → R/r? (expected: 80%+)
   - Is Hebrew זֶה truly ambiguous? (expected: 60-70% accuracy)
   - Is L (near listener) as rare as predicted? (expected: 0-1 instances)

4. **Error Analysis Categories**:
   - **Spatial vs. Discourse confusion**: Did TBTA choose spatial when we predicted discourse?
   - **Emphasis detection failures**: C vs. c mismatches
   - **Visibility inference errors**: R vs. r when narrative doesn't state visibility
   - **Hebrew contextual failures**: Wrong spatial code for unmarked זֶה

5. **Update PATTERNS-LEARNED.md** based on actual results

## Next Steps

**Phase 4**: Use these predicted patterns to develop Algorithm v1.0
- Codify decision tree (temporal → spatial → discourse → n)
- Implement Greek/Hebrew form mappings
- Add context analysis rules
- Target 75-80% accuracy on training set predictions

**Future Validation**: Once TBTA access confirmed, rerun analysis and update patterns

---

**Status**: Theoretical analysis complete, awaiting TBTA validation
**Confidence**: Medium-High (patterns based on solid linguistic research)
**Accuracy Estimate**: 70-80% overall when validated against TBTA
