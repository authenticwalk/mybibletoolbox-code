# Participant Tracking: Adversarial Test Set

**Date created**: 2025-11-11
**Algorithm tested**: v1.0 (commit cb388ca)
**Purpose**: Challenge algorithm with edge cases, ambiguous contexts, and rare state search
**Target accuracy**: 60-70% (adversarial challenges)
**Rare state goal**: Find examples of Restaging (R), Integration (i), Exiting (E)

---

## Test Design Strategy

### Core Adversarial Challenges (10 verses)
1. **Definite article ambiguity** (2 verses) - "the X" could be Routine, Frame Inferable, or First Mention
2. **Generic vs. Routine ambiguity** (2 verses) - Abstract nouns, possessives, type vs. instance
3. **Frame inference edge cases** (2 verses) - Novel frames, weak inference
4. **Repeated mention complexity** (2 verses) - Reintroduction, discourse breaks
5. **Interrogative transitions** (2 verses) - Questions with complex referent shifts

### Rare State Search (100+ verses targeted)
6. **Restaging search** (targeting 30+ long narrative verses) - Character returns after absence
7. **Integration search** (targeting 30+ verses with role shifts) - Peripheral → central participant
8. **Exiting search** (targeting 30+ verses with departures) - Explicit exits from narrative
9. **Offstage validation** (10+ verses) - Background modifiers (ethnic, locational)

**Total test size**: 10 adversarial + 100+ rare state search = 110+ verses

---

## Core Adversarial Test (10 Verses)

### Challenge 1: Definite Article Ambiguity (2 verses)

#### Verse 1: Luke 10:34 (Good Samaritan - "the innkeeper")
**Reference**: LUK 10:34-35
**English**: "And went to him, and bound up his wounds, pouring in oil and wine, and set him on his own beast, and brought him to an inn, and took care of him. And on the morrow when he departed, he took out two pence, and gave them to the host..."

**Challenge**: "the host" / "the innkeeper"
- Definite article on first mention
- Could be **Frame Inferable** (inn → innkeeper expected) OR **First Mention** (not explicitly set up)
- Algorithm prediction: Frame Inferable (Rule 3.2 - inn frame inference)
- **Edge case**: Tests strength of frame inference

**Other participants to track**: Samaritan (Routine), wounded man (Routine), inn (First Mention or Frame Inferable)

---

#### Verse 2: Matthew 26:57 (Arrest scene - "the scribes and elders")
**Reference**: MAT 26:57
**English**: "And they that had laid hold on Jesus led him away to Caiaphas the high priest, where the scribes and the elders were assembled."

**Challenge**: "the scribes and the elders"
- Definite article on first mention in this verse
- Could be **Frame Inferable** (trial/arrest frame → officials expected) OR **Routine** (mentioned earlier in Matthew)
- Algorithm prediction: Likely Frame Inferable OR Routine (discourse scope dependent)
- **Edge case**: Tests frame inference + discourse tracking

**Other participants**: "they that had laid hold" (Generic? Frame Inferable?), Jesus (Routine), Caiaphas (First Mention or Routine)

---

### Challenge 2: Generic vs. Routine Ambiguity (2 verses)

#### Verse 3: Psalm 23:1 ("The LORD is my shepherd")
**Reference**: PSA 23:1
**English**: "The LORD is my shepherd; I shall not want."

**Challenge**: "shepherd"
- Metaphorical use (type vs. instance?)
- Could be **Generic** (shepherd as type/concept) OR **Routine** (specific metaphorical reference to God)
- Algorithm prediction: Uncertain - likely Routine (possessive "my shepherd" = specific instance)
- **Edge case**: Metaphor handling

**Other participants**: LORD (Routine - God presupposition), I/me (Routine - psalmist)

---

#### Verse 4: John 10:11 ("I am the good shepherd")
**Reference**: JHN 10:11
**English**: "I am the good shepherd: the good shepherd giveth his life for the sheep."

**Challenge**: "the good shepherd" (both occurrences)
- Self-identification metaphor
- Could be **Generic** (shepherd as type) OR **Routine** (Jesus identifying himself)
- First mention: Might be Generic (type introduction)
- Second mention: Routine (continued reference) or still Generic?
- **Edge case**: Self-identification + metaphor + repetition

**Other participants**: I/me (Jesus - Routine), life (Generic abstract), sheep (Generic class)

---

### Challenge 3: Frame Inference Edge Cases (2 verses)

#### Verse 5: Luke 10:30 (Good Samaritan opening - "thieves")
**Reference**: LUK 10:30
**English**: "A certain man went down from Jerusalem to Jericho, and fell among thieves, which stripped him of his raiment, and wounded him, and departed, leaving him half dead."

**Challenge**: "thieves"
- Are thieves **Frame Inferable** from "travel/road" frame? (dangerous roads → thieves expected)
- OR **First Mention** (not clearly inferable, introduces antagonists)
- Algorithm prediction: Likely First Mention (thieves not clearly frame-inferable from travel alone)
- **Edge case**: Weak frame inference (is "travel → thieves" strong enough?)

**Other participants**: "a certain man" (First Mention), him (Routine continuation)

---

#### Verse 6: Mark 1:29 (Household scene - "Simon's wife's mother")
**Reference**: MRK 1:29
**English**: "And forthwith, when they were come out of the synagogue, they entered into the house of Simon and Andrew, with James and John. But Simon's wife's mother lay sick of a fever..."

**Challenge**: "Simon's wife's mother"
- **Frame Inferable** (household frame → family members expected) OR **First Mention** (specific person not previously mentioned)
- Algorithm prediction: Frame Inferable (Rule 3.1 relational + 3.2 household frame)
- **Edge case**: Complex relational NP (wife's mother = mother-in-law)

**Other participants**: they (Routine - disciples), house (First Mention or Routine), Simon (Routine), Andrew/James/John (Routine)

---

### Challenge 4: Repeated Mention Complexity (2 verses)

#### Verse 7: Genesis 6:9 ("Noah" genealogical introduction)
**Reference**: GEN 6:9
**English**: "These are the generations of Noah: Noah was a just man and perfect in his generations, and Noah walked with God."

**Challenge**: "Noah" (three mentions in one verse)
- First mention: **First Mention** (genealogical introduction formula)
- Second mention: **Routine** (repeated in same verse)
- Third mention: **Routine** (continued)
- **Edge case**: Multiple mentions in single verse, transition point unclear

**Other participants**: generations (Generic? Abstract?), man (Generic or Routine specific instance), God (Routine presupposition)

---

#### Verse 8: John 4:7-8 (Woman at well - discourse break)
**Reference**: JHN 4:7-8
**English**: "There cometh a woman of Samaria to draw water: Jesus saith unto her, Give me to drink. (For his disciples were gone away unto the city to buy meat.)"

**Challenge**: "woman" + discourse break with parenthetical
- v7: "a woman" - **First Mention** (indefinite, new participant)
- v8: "her" (referring to woman) - **Routine** (continued reference) OR affected by parenthetical discourse break?
- **Edge case**: Parenthetical interruption, pronoun after discourse break

**Other participants**: Jesus (Routine), disciples (Routine), water (Generic? Routine?), city (First Mention or Routine)

---

### Challenge 5: Interrogative Transitions (2 verses)

#### Verse 9: Luke 10:29 ("Who is my neighbor?")
**Reference**: LUK 10:29
**English**: "But he, willing to justify himself, said unto Jesus, And who is my neighbour?"

**Challenge**: "who" and "neighbour"
- "who" - **Interrogative** (question word)
- "neighbour" - **Interrogative** (questioned referent) OR **Routine** (concept already established in Law)?
- **Edge case**: Definitional question (asking about concept, not specific person)

**Other participants**: he (Routine - lawyer), Jesus (Routine)

---

#### Verse 10: Matthew 16:13 ("Who do men say that I am?")
**Reference**: MAT 16:13
**English**: "When Jesus came into the coasts of Caesarea Philippi, he asked his disciples, saying, Whom do men say that I the Son of man am?"

**Challenge**: "Whom", "men", "I", "Son of man"
- "Whom" - **Interrogative** (question word)
- "men" - **Generic** (people in general) OR **Interrogative** (part of question)?
- "I" (Jesus) - **Interrogative** (questioned identity) OR **Routine** (established participant)?
- "Son of man" - **Routine** (Jesus's self-designation) OR **Interrogative** (questioned identity)?
- **Edge case**: Complex identity question with multiple participants in interrogative context

**Other participants**: Jesus (Routine), he (Routine), disciples (Routine)

---

## Rare State Search (100+ Verses)

### Restaging (R) - Returning After Absence (Target: 30+ verses)

**Strategy**: Search long narratives where characters leave and return

#### Search Corpus 1: Genesis (Joseph narrative)
**Verses**: GEN 37:1-50:26 (Joseph sold into Egypt, later reunited)
**Target participants**:
- Joseph: GEN 37 (present) → 38 (absent, focus shifts to Judah) → 39+ (returns as protagonist)
- Brothers: GEN 37 (present) → long absence → GEN 42+ (return to buy grain)
- **Expected**: Restaging when Joseph/brothers reappear after extended absence

**Sample verses**: GEN 37:2, 38:1 (Judah focus shift), 39:1 (Joseph restaging?), 42:1 (brothers restaging?)

---

#### Search Corpus 2: 1-2 Samuel (David narrative)
**Verses**: 1 SAM 16 - 2 SAM 24 (David introduced, flees from Saul, returns as king)
**Target participants**:
- David: Introduced 1 SAM 16, leaves court (1 SAM 19-30), returns as king (2 SAM 1+)
- Saul: Present early, absent during David's flight, mentioned again later
- **Expected**: Restaging when David returns to prominence after exile period

**Sample verses**: 1 SAM 16:13 (David introduced), 25:1 (Saul absent?), 2 SAM 1:1 (David restaging?), 2:1 (David returns to Judah)

---

#### Search Corpus 3: Acts (Paul's journeys)
**Verses**: ACT 13-28 (Paul's missionary journeys, returns to Jerusalem)
**Target participants**:
- Paul: Journey 1 (ACT 13-14), Journey 2 (15-18), Journey 3 (18-21), returns to Jerusalem repeatedly
- Barnabas: Present ACT 13-15, absent after split (15:39), mentioned again later?
- **Expected**: Restaging when Paul returns to cities/Jerusalem after journeys

**Sample verses**: ACT 13:1 (Paul/Barnabas start), 15:36 (return to cities), 18:21 (return to Jerusalem), 21:17 (arrival restaging?)

---

### Integration (i) - Peripheral to Central (Target: 30+ verses)

**Strategy**: Search for minor characters who suddenly become focal

#### Search Corpus 1: Judas betrayal narrative
**Verses**: MAT 26:14-16 (Judas emerges from background), 26:47-50 (Judas acts), JHN 13:21-30 (Judas identified)
**Target participant**: Judas
- MAT 10:4 (listed among twelve, peripheral)
- MAT 26:14 (Judas steps forward to betray - Integration?)
- **Expected**: Integration when Judas moves from background disciple to central betrayer

**Sample verses**: MAT 10:4 (Judas in list), 26:14 (Judas acts independently), 26:47 (Judas leads crowd)

---

#### Search Corpus 2: Centurion at crucifixion
**Verses**: MAT 27:54, MRK 15:39 (centurion confesses), LUK 23:47
**Target participant**: Centurion
- Background figure (soldiers present at crucifixion)
- Suddenly speaks central confession ("Truly this was the Son of God")
- **Expected**: Integration when centurion moves from background → confessing protagonist

**Sample verses**: MAT 27:35 (soldiers present, background), 27:54 (centurion confesses - Integration?)

---

#### Search Corpus 3: Zacchaeus (Luke 19)
**Verses**: LUK 19:1-10 (Zacchaeus emerges from crowd)
**Target participant**: Zacchaeus
- Not mentioned before LUK 19:2
- Introduced as peripheral (tax collector in crowd)
- Becomes central (Jesus goes to his house, focal conversation)
- **Expected**: Integration when Zacchaeus moves from peripheral crowd member → central host

**Sample verses**: LUK 19:2 (Zacchaeus introduced), 19:5 (becomes central as Jesus's host)

---

### Exiting (E) - Departing Narrative (Target: 30+ verses)

**Strategy**: Search for explicit departure statements

#### Search Corpus 1: Judas departure (John 13)
**Verses**: JHN 13:30 ("he went out immediately")
**Target participant**: Judas
- Present at Last Supper (JHN 13:1-29)
- **Explicit exit**: "he went out immediately; and it was night" (13:30)
- Does not return to narrative (exits to betray)
- **Expected**: Exiting at JHN 13:30

**Sample verses**: JHN 13:30 (explicit departure)

---

#### Search Corpus 2: Jesus departures
**Verses**: Multiple Gospel instances where Jesus "departed", "went away", "withdrew"
**Target participant**: Jesus
- MAT 4:12 "withdrew into Galilee"
- MAT 12:15 "withdrew himself from thence"
- MAT 14:13 "departed thence by ship"
- JHN 6:15 "departed again into a mountain"
- **Expected**: Some marked as Exiting (departure from scene), others Routine (narrative continues)

**Sample verses**: MAT 12:15, 14:13, JHN 6:15 (explicit withdrawals)

---

#### Search Corpus 3: Disciples sent out
**Verses**: MAT 10:5 ("These twelve Jesus sent forth"), LUK 10:1 ("sent them two and two")
**Target participants**: Disciples
- Present with Jesus
- Sent out on mission (explicit departure)
- Return later (MAT 10:1 vs. 11:1 transition?)
- **Expected**: Exiting when sent out, Restaging when return?

**Sample verses**: MAT 10:5 (disciples sent - Exiting?), LUK 10:17 (disciples return - Restaging?)

---

### Offstage (O) - Background Modifiers (Target: 10+ verses)

**Strategy**: Search for ethnic/locational attributes as background

#### Search Corpus 1: Ethnic modifiers
**Verses**: Various instances of "the Canaanite", "the Roman", "of Nazareth", etc.
**Target phrases**:
- "Simon the Canaanite" (MAT 10:4)
- "Jesus of Nazareth" (MAT 2:23, 26:71)
- "Mary Magdalene" (= Mary of Magdala)
- "Judas Iscariot" (= Judas of Kerioth?)
- **Expected**: Offstage for ethnic/locational modifiers (not active participants, just attributes)

**Sample verses**: MAT 10:4 (Simon the Canaanite), MAT 26:71 (Jesus of Nazareth as title/attribute)

---

#### Search Corpus 2: Locational attributes
**Verses**: "the centurion of Capernaum" (MAT 8:5), "the woman of Canaan" (MAT 15:22)
**Target phrases**: Locational modifiers
- Not active participants, just descriptive attributes
- **Expected**: Offstage (background modification only)

**Sample verses**: MAT 8:5, 15:22 (locational descriptors)

---

## Test Set Summary

### Core Adversarial Test
**Total**: 10 verses
**Challenges**:
1-2. Definite article ambiguity (Frame Inferable vs. First Mention vs. Routine)
3-4. Generic vs. Routine (metaphors, abstracts, possessives)
5-6. Frame inference edge cases (weak frames, novel frames)
7-8. Repeated mention complexity (discourse breaks, same-verse transitions)
9-10. Interrogative transitions (definitional questions, identity questions)

**Target accuracy**: 60-70% (challenging edge cases)

---

### Rare State Search
**Total**: 100+ verses targeted
**Goals**:
- **Restaging**: Find 1-4 examples in 30+ verses (Joseph, David, Paul narratives)
- **Integration**: Find 1-4 examples in 30+ verses (Judas, centurion, Zacchaeus)
- **Exiting**: Find 1-4 examples in 30+ verses (Judas exit, Jesus withdrawals, disciples sent)
- **Offstage**: Validate <0.001% frequency in 10+ verses (ethnic/locational modifiers)

**Success criterion**: Find at least ONE example each of Restaging, Integration, Exiting (proving rare states exist)

---

## Methodology

### Phase 5 (Current): Test Set Design
- Document adversarial verses (10 verses above)
- Document rare state search strategy (100+ verses above)
- Commit and lock test set design

### Phase 6: Make Predictions
- Apply Algorithm v1.0 to 10 adversarial verses (**NO TBTA ACCESS**)
- Predict rare state locations in 100+ verse search
- Lock predictions via git commit

### Phase 7: Validation
- Access TBTA for adversarial verses
- Verify rare state predictions in search corpus
- Calculate accuracy
- Document findings

---

## Expected Outcomes

### Adversarial Test
- **60-70% accuracy** (challenging cases, algorithm will struggle with ambiguity)
- Errors expected on: definite article disambiguation, weak frames, complex interrogatives

### Rare State Search
- **Find 1-4 examples** of Restaging (character returns)
- **Find 1-4 examples** of Integration (peripheral → central)
- **Find 1-4 examples** of Exiting (explicit departures)
- **Validate Offstage** <0.001% (extremely rare, background only)

**Degree feature lesson applied**: Even 0% in small samples doesn't mean non-existent. Adversarial search at scale (100+ verses) WILL find rare states at 1-4 per 100 rates.

---

**Created**: 2025-11-11
**Status**: Test set designed, ready for Phase 6 (blind predictions)
**Algorithm**: v1.0 (locked commit cb388ca)
**Next**: Make blind predictions on 10 adversarial + search 100+ for rare states
