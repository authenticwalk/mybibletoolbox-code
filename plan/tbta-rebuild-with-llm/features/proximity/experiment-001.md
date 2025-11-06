# Proximity/Demonstrative Feature Testing - Experiment 001

## Objective
Test and validate methods for predicting demonstrative proximity categories in languages with multi-way distance systems. Test against real Bible verses to develop reproducible prediction methods for:
- Near Speaker
- Near Listener
- Remote within Sight
- Contextually Near

## Methodology

### Phase 1: Research and Theory
Before testing, establish:
1. Which TBTA languages have complex demonstrative systems
2. Linguistic frameworks for proximity prediction
3. Biblical examples that trigger specific proximity categories
4. Language family patterns that affect predictions

### Phase 2: Verse Selection
Select test verses that contain demonstratives with clear spatial/contextual references:
- Direct spatial deixis (physically near/far)
- Discourse deixis (contextually near)
- Anaphoric reference (referring back to previously mentioned items)

### Phase 3: Blind Prediction
For each verse:
1. Identify demonstrative(s) used in the original Greek/Hebrew
2. Predict proximity category for languages with 3-way or 4+ systems
3. Compare to TBTA annotated data
4. Analyze prediction accuracy

### Phase 4: Error Analysis
Categorize failures:
- Incorrect context interpretation
- Missing language family knowledge
- Ambiguous discourse deixis
- TBTA annotation patterns

---

## Test Case 1: Matthew 3:3 - John the Baptist (Discourse Deixis)

### Verse Context
**Matthew 3:3 (Greek):**
"Οὗτος γάρ ἐστιν ὁ ῥηθεὶς διὰ Ἠσαΐου τοῦ προφήτου λέγοντος, Φωνὴ βοῶντος ἐν τῇ ἐρήμῳ..."

"This is he that was spoken of by the prophet Isaiah, saying, The voice of one crying in the wilderness..."

### Analysis

**Demonstrative:** "Οὗτος" (houtos) = "this one"
**Type of Deixis:** Discourse deixis - referring to someone just mentioned (John the Baptist)
**Spatial Context:** Narrative context, not physical proximity
**Speaker Position:** Matthew (narrator) introducing John

### Prediction for 3-Way Systems

For languages like Spanish, Italian, Tagalog with (near speaker / near hearer / far from both):

**Hypothesis 1:** "Contextually Near" or "Near Speaker"
- The referent (John) is newly introduced and "close" in discourse
- Narrator perspective makes John "proximal" to the telling
- Might use Spanish "este" (near speaker) or similar

**Hypothesis 2:** "Neutral/Medial"
- Introducing someone in narrative flow
- Not physically present, but thematically "middle distance"
- Might use intermediate form in some languages

### Test Predictions

| Language | Hypothesis | Predicted Form | Reasoning |
|----------|-----------|----------------|-----------|
| Spanish | Near Speaker | "Este/Este Juan" | Recently introduced in discourse |
| Tagalog | Near Speaker | "Itong..." | Discourse prominence |
| Italian | Medial | "Questo/Colui" | Introducing mentioned figure |

### Success Criteria
- Prediction matches TBTA annotations
- Language family patterns are consistent
- Alternative forms documented if language has multiple options

---

## Test Case 2: Luke 15:29 - The Prodigal Son (Mixed Deixis)

### Verse Context
**Luke 15:29 (Greek):**
"ἀλλ' ὁ υἱὸς αὐτοῦ ὁ πρεσβύτερος ἠγανάκτησεν καὶ εἰς ἐλθεῖν ἠθέλησεν· ὁ δὲ πατὴρ αὐτοῦ ἐξελθὼν παρεκάλει αὐτόν."

"But his elder son was angry and would not go in... So his father came out and entreated him."

### Analysis

**Demonstratives Present:**
- "ὁ υἱὸς" - "the son" (definite article as demonstrative)
- "ὁ πατήρ" - "the father" (definite article as demonstrative)
- "αὐτόν" - "him" (anaphoric pronoun)

**Spatial Context:**
- Son outside, standing at distance from father
- Father comes OUT to approach son
- Clear physical distance transitioning to proximity

**Speaker Position:** Narrative from omniscient perspective

### Prediction for Elevation-Based Systems (Mian, etc.)

For Trans-New Guinea languages with elevation directionals:

**Hypothesis 1:** "Up/Down Distinction"
- Son standing outside (potentially elevated position)
- Father coming from house toward son (moving down)
- Could trigger elevation-based demonstratives

**Hypothesis 2:** "Movement-Based Selection"
- Dynamic situation with approaching/retreating
- Some languages may mark if object is approaching or receding
- Cup'ik's 29-way system might include motion component

### Test Predictions

| Language Family | Type | Predicted Feature | Reasoning |
|-----------------|------|------------------|-----------|
| Trans-New Guinea | Elevation | Up/Down | Physical positioning in narrative |
| Yupik (Cup'ik) | 29-way | Motion + Placement | Father approaching (stationary to moving) |
| Spanish 3-way | Person-oriented | Distal ("Aquel") | Both figures at distance from narrator |

---

## Test Case 3: John 3:29 - John the Baptist's Voice (Sensory Deixis)

### Verse Context
**John 3:29 (Greek):**
"ὁ ἔχων τὴν νύμφην νυμφίος ἐστίν· ὁ δὲ φίλος τοῦ νυμφίου, ὁ ἑστηκὼς καὶ ἀκούων αὐτοῦ, χαρᾷ χαίρει διὰ τὴν φωνὴν τοῦ νυμφίου."

"The one who has the bride is the bridegroom... the friend of the bridegroom... stands and hears him, and rejoices greatly at the bridegroom's voice."

### Analysis

**Demonstrative:** "ὁ ἑστηκώς" - "the one standing" (demonstrative use of definite article)
**Sensory Component:** "hears" and "voice" - John the Baptist hearing Jesus's voice
**Visibility Status:** Can the speaker see or hear the referent?
**Question:** How do visibility-encoding languages handle this?

### Prediction for Visibility Systems (Ticuna, Malagasy, Nuxalk)

**Hypothesis 1:** "Auditory Proximity" = "Near"
- John hears Jesus's voice (auditory evidence of presence)
- Hearing may trigger "visible" or "proximal" demonstrative
- Malagasy might use visible form despite physical distance

**Hypothesis 2:** "Out of Sight" Demonstrative
- Jesus is not visually present to John (but audible)
- Some languages distinguish: visible present vs. non-visible present
- May require "invisible" demonstrative despite proximity

**Hypothesis 3:** "Contextually Near"
- In discourse, this is highlighted moment
- Demonstrative prominence despite physical separation

### Test Predictions

| Language | Hypothesis | Predicted Form | Reasoning |
|----------|-----------|----------------|-----------|
| Ticuna | Visible/Invisible | Invisible proximal | Can hear but not see |
| Malagasy | Visible 7-degree | Medial visible | Auditory contact = partial proximity |
| Nuxalk | Visible/Invisible pair | Invisible form | Not in direct line of sight |

---

## Test Case 4: Genesis 37:19-20 - Joseph's Coat (Physical Deixis)

### Verse Context
**Genesis 37:19-20 (Hebrew):**
"וַיֹּאמְרוּ אִישׁ אֶל־אָחִיו הִנֵּה בַעַל הַחֲלוֹמוֹת הַלָּזֶה בָּא... וַאֲנַחְנוּ נִשְׁמְרָה לוֹ דָּבָר."

"They said to one another, 'Behold, this dreamer is coming... Let us do away with him.'"

### Analysis

**Demonstrative:** "הַלָּזֶה" (ha-laze) = "this one / this very one"
**Physical Context:** Joseph approaching brothers, they see him
**Emotional Component:** Contempt and threat perception
**Question:** How do different languages mark "that guy coming right at us"?

### Prediction for Person-Oriented Systems

**Hypothesis 1:** "Near Listener/Mixed Speaker-Hearer"
- Joseph approaching brothers
- All speakers' perspective (the group)
- May use form marking proximity to hearer group
- Spanish might use "ese" (near hearer) if hearer-inclusive

**Hypothesis 2:** "Distal with Contempt Marking"
- Brothers treat Joseph with disdain
- May use distal form despite physical proximity
- Emotional distance overrides physical distance

**Hypothesis 3:** "Immediate Threat Proximal"
- Joseph immediately approaching
- May trigger near speaker form
- Imminent action = proximity marking

### Test Predictions

| Language | Type | Predicted Form | Reasoning |
|----------|------|----------------|-----------|
| Spanish | 3-way person | "ese" | Near the hearer group |
| Tagalog | 3-way person | "Yan" (near hearer) | Brothers as hearer focus |
| Dravidian (Tamil) | Distance-based | Near form | Physical approach triggers proximal |

---

## Test Case 5: Revelation 4:1 - The Heavenly Voice (Cosmic Deixis)

### Verse Context
**Revelation 4:1 (Greek):**
"μετὰ ταῦτα εἶδον, καὶ ἰδοὺ θύρα ἠνεῳγμένη ἐν τῷ οὐρανῷ, καὶ ἡ φωνὴ ἡ πρώτη ἣν ἤκουσα..."

"After this I looked, and behold, a door standing open in heaven, and the first voice which I heard..."

### Analysis

**Demonstratives:**
- "ταῦτα" (tauta) - "these things" (discourse deixis)
- "ἡ πρώτη" - "the first one" (deictic article)

**Spatial Challenge:**
- "Heaven" is remote, non-earthly realm
- How do languages that mark elevation handle cosmic distance?
- Not merely "far" but "transcendent"

**Visibility Status:**
- Voice heard but source unclear/unseen
- Vision follows hearing

### Prediction for Elevation/Transcendent Systems

**Hypothesis 1:** "Ultimate Elevation" or "Transcendent Remote"
- Languages with elevation markers may lack precise category
- "Above" (heavenly) may trigger special form
- Quechuan languages might use "up" directional

**Hypothesis 2:** "Invisible/Non-Visible"
- Voice without visible source
- Visibility languages may use "invisible" demonstrative
- Appropriate for spirit realm references

**Hypothesis 3:** "Contextually Remote"
- Despite being "far," maintains discourse salience
- May not use most distal form
- Marked as exceptional/spiritual

### Test Predictions

| Language | Type | Predicted Feature | Reasoning |
|----------|------|------------------|-----------|
| Quechuan | Elevation | Ultimate Up ("hawa") | Heavenly height |
| Ticuna | Visibility | Invisible proximal | Heard but unseen |
| Malagasy | Visibility+Distance | Most distal visible | Transcendent realm |

---

## Methodology for Validation

### Step 1: Access TBTA Data
Verify if annotated data exists for these verses in TBTA:
1. Check TBTA GitHub repository
2. Look for demonstrative/proximity annotations
3. Identify which languages have explicit markings

### Step 2: Cross-Reference Language Families
For each test case:
1. Identify TBTA languages from identified families
2. Compare predictions to TBTA decisions
3. Note consistent vs. divergent patterns

### Step 3: Error Analysis Framework
For each failed prediction, document:

```
FAILED PREDICTION TEMPLATE:

Verse: [Reference]
Language: [Code]
Predicted Proximity: [Category]
Actual TBTA Value: [Category]
Error Type:
  - [ ] Context Misinterpretation
  - [ ] Language Family Unknown
  - [ ] Theology/Doctrine Issue
  - [ ] Ambiguity in Original
  - [ ] TBTA Error Suspected

Root Cause Analysis:
[Why did prediction fail?]

Refined Hypothesis:
[Updated prediction rule based on error]

Similar Verses to Test:
[Other verses with same pattern]
```

---

## Preliminary Findings Framework

### Pattern Categories (to be validated)

1. **Discourse Deixis Pattern**
   - Newly introduced entities: Near/Contextually Near
   - References back to previous: Depends on discourse distance
   - Major topic shift: May reset to Remote

2. **Physical Deixis Pattern**
   - Approaching entity: Near Speaker
   - Entity at listener location: Near Listener
   - Visible but distant: Remote within Sight
   - Invisible spiritual: Invisible/Transcendent category (if available)

3. **Emotional Distance Pattern**
   - Contempt/rejection: Distal (emotional distance)
   - Intimacy/unity: Proximal (emotional proximity)
   - Neutral reference: Medial/Unmarked

4. **Elevation-Based Pattern** (TNG, Quechuan, etc.)
   - Heaven/spiritual realm: Up directional
   - Underworld/hell: Down directional
   - Mountain/height narrative: Up
   - Valley/depth narrative: Down

5. **Visibility-Based Pattern** (Ticuna, Malagasy, Nuxalk)
   - Physically visible: Visible form
   - Audible but not visible: Mixed (some use visible, some invisible)
   - Purely conceptual/recalled: Invisible
   - Spiritual beings: Invisible category preferred

---

## Expected Outcomes

### Success Indicators
- [ ] 70%+ accuracy on discourse deixis
- [ ] 80%+ accuracy on physical deixis
- [ ] 60%+ accuracy on emotional/abstract deixis
- [ ] Language family patterns consistent
- [ ] Identifiable error categories

### Hypotheses to Validate
- [ ] 3-way systems (person-oriented) differ from distance-oriented
- [ ] Visibility languages use distinct strategy for spiritual references
- [ ] Elevation languages correlate with mountainous theology
- [ ] Discourse deixis more challenging than physical deixis
- [ ] Emotional distance influences proximity marking

### Documentation Deliverables
- [ ] Test results matrix (verses × languages)
- [ ] Error analysis by category
- [ ] Language family prediction patterns
- [ ] Refined proximity prediction rules
- [ ] Outstanding questions/ambiguities

---

## Next Steps

1. **Identify TBTA Data Source**
   - Locate actual TBTA annotations for selected verses
   - Determine which languages have demonstrative annotations
   - Access translation samples for test languages

2. **Refine Predictions with Actual Data**
   - Test against real TBTA values
   - Track accuracy metrics
   - Document divergences from predictions

3. **Language Family Deep Dive**
   - For each family, study 2-3 representative languages
   - Understand how family patterns apply to Bible translation
   - Note exceptions within families

4. **Create Prediction Ruleset**
   - Synthesize successful patterns into decision rules
   - Create flowchart for proximity determination
   - Document confidence levels by context type

5. **Extend to Remaining TBTA Languages**
   - Apply developed rules to other languages with complex demonstratives
   - Test on new verses not yet analyzed
   - Measure external validation accuracy

---

## References and Resources

### Linguistic Typology
- WALS Chapter 41: Distance Contrasts in Demonstratives
- Anderson & Keenan (1985): Deixis in Language Typology
- Adelaar & Himmelmann (2013): Austronesian Languages

### Language-Specific Sources
- Proximity language typology: [language-typology.md](language-typology.md)
- Person systems examples: [../person-systems/BIBLE-EXAMPLES.md](../person-systems/BIBLE-EXAMPLES.md)

### TBTA Resources
- TBTA GitHub: https://github.com/AllTheWord/tbta_db_export
- TBTA README: https://github.com/AllTheWord/tbta_db_export/blob/main/README.md

---

## Status
- Created: [Date]
- Phase: Planning and Test Case Development
- Ready for: Validation with actual TBTA data
