# Participant Tracking: Random Test Predictions (LOCKED)

**Date**: 2025-11-11
**Algorithm**: v1.0 (commit cb388ca) - 97% training accuracy
**Method**: Blind predictions - NO TBTA ACCESS during prediction phase
**Verses**: 12 random test verses
**Lock status**: PREDICTIONS TO BE LOCKED via git commit before validation

---

## ⚠️ PREDICTION INTEGRITY PROTOCOL ⚠️

**CRITICAL**: These predictions are made WITHOUT accessing TBTA annotations.
- ✅ Algorithm v1.0 rules ONLY
- ❌ NO reading TBTA YAML files
- ❌ NO peeking at actual annotations
- ✅ Lock predictions via git commit BEFORE Phase 7 validation

**Validation**: Phase 7 will access TBTA and calculate accuracy

---

## Prediction Methodology

For each verse, I will:
1. Read verse text only (English, NOT TBTA data)
2. Identify all participants (noun phrases)
3. Apply Algorithm v1.0 hierarchical rules:
   - Rule 1: Interrogative (question context)
   - Rule 2: Generic (universal quantifiers, abstracts, negatives, vocatives)
   - Rule 3: Frame Inferable (relational, frame-expected, definite on first mention)
   - Rule 4: First Mention vs. Routine (indefinite vs. established)
4. Record prediction with confidence level

---

## Predictions

### Verse 1: 1 Samuel 9:21

**English text** (from memory/Bible, NOT TBTA):
"And Saul answered and said, Am not I a Benjamite, of the smallest of the tribes of Israel? and my family the least of all the families of the tribe of Benjamin? wherefore then speakest thou so to me?"

**Participants identified**:
1. **Saul** - "Saul answered"
2. **I** - "Am not I" (Saul speaking, first person)
3. **Benjamite** - "a Benjamite"
4. **tribes** - "the smallest of the tribes"
5. **Israel** - "tribes of Israel"
6. **family** - "my family"
7. **families** - "all the families"
8. **tribe** - "the tribe of Benjamin"
9. **Benjamin** - "tribe of Benjamin"
10. **thou** - "speakest thou" (addressee, Samuel presumably)
11. **me** - "to me" (Saul, object)

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| Saul | **Routine (D)** | High | Protagonist, main narrative participant established in prior verses (1 SAM 9:1-20) |
| I (first) | **Routine (D)** | High | Pronoun referring to Saul (established participant) |
| Benjamite | **Generic (G)** | Medium | "a Benjamite" - tribal identity, could be Generic (type) OR First Mention (specific identity). Rule 2: likely Generic tribal designation |
| tribes | **Routine (D)** | High | Definite "the tribes" - established concept in Israelite context |
| Israel | **Routine (D)** | High | God presupposition analogy - Israel as nation is presupposed/established |
| family | **Routine (D)** | High | "my family" - possessive, specific instance (Rule 2 contrast: not abstract Generic) |
| families | **Generic (G)** | Medium | "all the families" - universal quantifier "all" → Generic (Rule 2.1) |
| tribe | **Routine (D)** | High | "the tribe of Benjamin" - definite, specific tribe |
| Benjamin | **Routine (D)** | High | Proper name, established tribal patriarch |
| thou | **Routine (D)** | High | Pronoun referring to Samuel (established in prior context) |
| me | **Routine (D)** | High | Pronoun referring to Saul |

---

### Verse 2: 1 Samuel 13:6

**English text**:
"When the men of Israel saw that they were in a strait, (for the people were distressed,) then the people did hide themselves in caves, and in thickets, and in rocks, and in high places, and in pits."

**Participants identified**:
1. **men** - "the men of Israel"
2. **Israel** - "men of Israel"
3. **they** - "they were in a strait"
4. **people** (first) - "for the people were distressed"
5. **people** (second) - "then the people did hide"
6. **themselves** - "hide themselves"
7. **caves** - "in caves"
8. **thickets** - "in thickets"
9. **rocks** - "in rocks"
10. **places** - "high places"
11. **pits** - "in pits"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| men | **Routine (D)** | High | "the men of Israel" - definite, established group in narrative context |
| Israel | **Routine (D)** | High | Nation name, presupposed (like God) |
| they | **Routine (D)** | High | Pronoun referring to "men of Israel" |
| people (first) | **Routine (D)** | High | "the people" - definite, same referent as "men of Israel" |
| people (second) | **Routine (D)** | High | Repeated mention, continued reference |
| themselves | **Routine (D)** | High | Reflexive pronoun referring to "the people" |
| caves | **First Mention (I)** | Medium | "in caves" - indefinite (no article), new locations introduced. Could be Generic (caves as type) but likely First Mention as specific hiding places |
| thickets | **First Mention (I)** | Medium | "in thickets" - parallel to caves, new hiding places |
| rocks | **First Mention (I)** | Medium | "in rocks" - new hiding place |
| places | **First Mention (I)** | Low | "high places" - could be Frame Inferable (hiding frame → high places expected?) or First Mention. Leaning First Mention |
| pits | **First Mention (I)** | Medium | "in pits" - final hiding place in list |

---

### Verse 3: 2 John 1:3

**English text**:
"Grace be with you, mercy, and peace, from God the Father, and from the Lord Jesus Christ, the Son of the Father, in truth and love."

**Participants identified**:
1. **Grace** - "Grace be with you"
2. **you** - "with you"
3. **mercy** - "mercy"
4. **peace** - "and peace"
5. **God** - "from God"
6. **Father** (first) - "God the Father"
7. **Lord** - "the Lord"
8. **Jesus Christ** - "Lord Jesus Christ"
9. **Son** - "the Son of the Father"
10. **Father** (second) - "the Son of the Father"
11. **truth** - "in truth"
12. **love** - "and love"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| Grace | **Generic (G)** | High | Abstract concept as type (Rule 2.3), not specific instance |
| you | **Routine (D)** | High | Pronoun referring to recipients (established in greeting context) |
| mercy | **Generic (G)** | High | Abstract concept, parallel to "grace" |
| peace | **Generic (G)** | High | Abstract concept, third in blessing triad |
| God | **Routine (D)** | High | God presupposition (Special Case) |
| Father (first) | **Routine (D)** | High | "God the Father" - God is Routine, Father as title/attribute |
| Lord | **Routine (D)** | Medium | "the Lord" - could be Generic (title) OR Routine (refers to Jesus). Likely Routine as referential |
| Jesus Christ | **Routine (D)** | High | Proper name, central figure in epistolary context |
| Son | **Frame Inferable (F)** | High | Relational noun "Son" inferable from "Father" (Rule 3.1 relational inference) |
| Father (second) | **Routine (D)** | High | Repeated mention of Father |
| truth | **Generic (G)** | High | Abstract concept |
| love | **Generic (G)** | High | Abstract concept |

---

### Verse 4: Acts 2:1

**English text**:
"And when the day of Pentecost was fully come, they were all with one accord in one place."

**Participants identified**:
1. **day** - "the day of Pentecost"
2. **Pentecost** - "day of Pentecost"
3. **they** - "they were all"
4. **accord** - "with one accord"
5. **place** - "in one place"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| day | **Routine (D)** | Medium | "the day of Pentecost" - could be Frame Inferable (temporal frame) OR First Mention. Definite suggests Routine or Frame Inferable. Leaning Routine (Pentecost is known festival) |
| Pentecost | **Routine (D)** | Medium | Jewish festival, culturally established |
| they | **Routine (D)** | High | Pronoun referring to disciples/apostles (established in Acts 1) |
| accord | **Generic (G)** | Medium | "one accord" - abstract concept/state, not specific instance |
| place | **First Mention (I)** | Medium | "one place" - indefinite-like ("one" = a), new location. Likely First Mention |

---

### Verse 5: Acts 3:8

**English text**:
"And he leaping up stood, and walked, and entered with them into the temple walking, and leaping, and praising God."

**Participants identified**:
1. **he** - "he leaping up" (healed lame man)
2. **them** - "with them" (Peter and John)
3. **temple** - "into the temple"
4. **God** - "praising God"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| he | **Routine (D)** | High | Pronoun referring to lame man (introduced in Acts 3:1-7) |
| them | **Routine (D)** | High | Pronoun referring to Peter and John (established) |
| temple | **Routine (D)** | High | "the temple" - definite, established location (mentioned in Acts 3:1 "gate of the temple") |
| God | **Routine (D)** | High | God presupposition (Special Case) |

---

### Verse 6: Acts 3:10

**English text**:
"And they knew that it was he which sat for alms at the Beautiful gate of the temple: and they were filled with wonder and amazement at that which had happened unto him."

**Participants identified**:
1. **they** (first) - "they knew"
2. **it** - "it was he"
3. **he** - "it was he which sat"
4. **alms** - "sat for alms"
5. **gate** - "the Beautiful gate"
6. **Beautiful** - "the Beautiful gate" (attribute/name?)
7. **temple** - "gate of the temple"
8. **they** (second) - "they were filled"
9. **wonder** - "with wonder"
10. **amazement** - "and amazement"
11. **that** - "that which had happened"
12. **him** - "happened unto him"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| they (first) | **Routine (D)** | High | Pronoun referring to people at temple (established in scene) |
| it | **Routine (D)** | High | Expletive or pronoun referring to situation |
| he | **Routine (D)** | High | Pronoun referring to healed lame man (continued from Acts 3:8) |
| alms | **Generic (G)** | Medium | Abstract concept (charity), or could be Routine (specific alms he received). Leaning Generic (alms as practice) |
| gate | **Routine (D)** | Medium | "the Beautiful gate" - definite, specific location. Could be First Mention if first time mentioned, but "Beautiful gate" suggests established landmark. Leaning Routine |
| Beautiful | **Routine (D)** | Medium | Proper name/attribute of gate |
| temple | **Routine (D)** | High | Repeated mention from Acts 3:8 |
| they (second) | **Routine (D)** | High | Same referent as "they" first mention |
| wonder | **Generic (G)** | High | Abstract emotional state |
| amazement | **Generic (G)** | High | Abstract emotional state |
| that | **Routine (D)** | Medium | Refers to healing event (established action) |
| him | **Routine (D)** | High | Pronoun referring to healed man |

---

### Verse 7: Daniel 1:20

**English text**:
"And in all matters of wisdom and understanding, that the king enquired of them, he found them ten times better than all the magicians and astrologers that were in all his realm."

**Participants identified**:
1. **matters** - "all matters"
2. **wisdom** - "matters of wisdom"
3. **understanding** - "and understanding"
4. **king** - "the king enquired"
5. **them** (first) - "enquired of them" (Daniel and friends)
6. **he** - "he found" (the king)
7. **them** (second) - "found them"
8. **times** - "ten times"
9. **magicians** - "all the magicians"
10. **astrologers** - "and astrologers"
11. **realm** - "his realm"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| matters | **Generic (G)** | High | "all matters" - universal quantifier "all" → Generic (Rule 2.1) |
| wisdom | **Generic (G)** | High | Abstract concept |
| understanding | **Generic (G)** | High | Abstract concept |
| king | **Routine (D)** | High | "the king" - definite, main authority figure established in Daniel 1 (Nebuchadnezzar) |
| them (first) | **Routine (D)** | High | Pronoun referring to Daniel and friends (established in Dan 1:3-19) |
| he | **Routine (D)** | High | Pronoun referring to king |
| them (second) | **Routine (D)** | High | Continued reference to Daniel and friends |
| times | **Generic (G)** | Low | "ten times" - measurement/degree. Could be Generic (abstract quantity) or Routine. Leaning Generic |
| magicians | **Generic (G)** | Medium | "all the magicians" - universal "all" → Generic (class of magicians, not specific individuals). Rule 2.1 |
| astrologers | **Generic (G)** | High | Parallel to magicians, universal class |
| realm | **Routine (D)** | High | "his realm" - possessive, specific kingdom (Babylon) |

---

### Verse 8: Ephesians 1:6

**English text**:
"To the praise of the glory of his grace, wherein he hath made us accepted in the beloved."

**Participants identified**:
1. **praise** - "the praise"
2. **glory** - "the glory of his grace"
3. **grace** - "his grace"
4. **he** - "he hath made" (God)
5. **us** - "made us accepted"
6. **beloved** - "in the beloved" (Christ)

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| praise | **Generic (G)** | High | Abstract concept (not specific instance of praise) |
| glory | **Generic (G)** | High | Abstract concept |
| grace | **Generic (G)** | Medium | "his grace" - possessive suggests specific instance, BUT in theological context likely Generic (grace as divine attribute/concept). Uncertain - could be Routine |
| he | **Routine (D)** | High | Pronoun referring to God (established in Ephesians 1:1-5) |
| us | **Routine (D)** | High | Pronoun referring to believers/recipients (established in epistle context) |
| beloved | **Routine (D)** | Medium | "the beloved" - definite, refers to Christ (established). Could be Generic (title) but likely Routine (specific reference) |

---

### Verse 9: Ephesians 1:7

**English text**:
"In whom we have redemption through his blood, the forgiveness of sins, according to the riches of his grace."

**Participants identified**:
1. **whom** - "in whom" (Christ)
2. **we** - "we have redemption"
3. **redemption** - "have redemption"
4. **blood** - "his blood"
5. **forgiveness** - "the forgiveness"
6. **sins** - "forgiveness of sins"
7. **riches** - "the riches of his grace"
8. **grace** - "his grace"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| whom | **Routine (D)** | High | Pronoun referring to "beloved" / Christ (continued from Eph 1:6) |
| we | **Routine (D)** | High | Pronoun referring to believers |
| redemption | **Generic (G)** | High | Abstract theological concept |
| blood | **Routine (D)** | Medium | "his blood" - possessive (Christ's blood), could be Generic (blood as concept) OR Routine (specific instance of Christ's sacrifice). Leaning Routine (specific blood) |
| forgiveness | **Generic (G)** | High | Abstract concept |
| sins | **Generic (G)** | High | Abstract/class concept (sins in general, not specific sins) |
| riches | **Generic (G)** | Medium | Could be Generic (riches as abundance concept) OR Routine (specific riches). Metaphorical use suggests Generic |
| grace | **Generic (G)** | Medium | Same as Eph 1:6 - theological attribute, likely Generic |

---

### Verse 10: Ephesians 1:8

**English text**:
"Wherein he hath abounded toward us in all wisdom and prudence."

**Participants identified**:
1. **he** - "he hath abounded" (God)
2. **us** - "toward us"
3. **wisdom** - "all wisdom"
4. **prudence** - "and prudence"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| he | **Routine (D)** | High | Pronoun referring to God (continued from Eph 1:7) |
| us | **Routine (D)** | High | Pronoun referring to believers |
| wisdom | **Generic (G)** | High | "all wisdom" - universal quantifier "all" + abstract concept → Generic |
| prudence | **Generic (G)** | High | Abstract concept parallel to wisdom |

---

### Verse 11: Ephesians 3:20

**English text**:
"Now unto him that is able to do exceeding abundantly above all that we ask or think, according to the power that worketh in us."

**Participants identified**:
1. **him** - "unto him that is able"
2. **all** - "above all that we ask" (could be quantifier, not participant)
3. **we** - "that we ask"
4. **power** - "the power"
5. **us** - "worketh in us"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| him | **Routine (D)** | High | Pronoun referring to God (established throughout Ephesians) |
| we | **Routine (D)** | High | Pronoun referring to believers |
| power | **Generic (G)** | Medium | "the power" - could be Generic (power as concept/attribute) OR Routine (specific divine power). Abstract theological attribute suggests Generic |
| us | **Routine (D)** | High | Pronoun referring to believers |

---

### Verse 12: Esther 1:5

**English text**:
"And when these days were expired, the king made a feast unto all the people that were present in Shushan the palace, both unto great and small, seven days, in the court of the garden of the king's palace."

**Participants identified**:
1. **days** - "these days"
2. **king** - "the king made"
3. **feast** - "made a feast"
4. **people** - "all the people"
5. **Shushan** - "in Shushan"
6. **palace** (first) - "Shushan the palace"
7. **great** - "unto great and small" (people of high status)
8. **small** - "and small" (common people)
9. **days** (second) - "seven days"
10. **court** - "the court of the garden"
11. **garden** - "the garden of the king's palace"
12. **palace** (second) - "the king's palace"

**Predictions**:

| Participant | Predicted State | Confidence | Reasoning |
|-------------|----------------|------------|-----------|
| days (first) | **Routine (D)** | High | "these days" - demonstrative refers to prior 180-day feast (Esther 1:4), Routine |
| king | **Routine (D)** | High | "the king" - Ahasuerus, established in Esther 1:1-4 |
| feast | **First Mention (I)** | Medium | "a feast" - indefinite, NEW feast (different from 180-day feast). First Mention |
| people | **Generic (G)** | High | "all the people" - universal quantifier "all" → Generic (class of all people, not specific individuals). Rule 2.1 |
| Shushan | **Routine (D)** | High | Capital city, established in Esther 1:2 |
| palace (first) | **Routine (D)** | High | "Shushan the palace" - established location |
| great | **Generic (G)** | High | "great and small" - classes of people (high status vs. common), not specific individuals. Generic |
| small | **Generic (G)** | High | Parallel to "great", Generic class |
| days (second) | **Generic (G)** | Low | "seven days" - measurement/duration. Could be Generic (time period as type) OR First Mention (specific 7-day period). Leaning Generic (duration measurement) |
| court | **First Mention (I)** | Medium | "the court of the garden" - definite, could be Frame Inferable (palace frame → court expected) OR First Mention. Leaning First Mention (specific new location for this feast) |
| garden | **Frame Inferable (F)** | Medium | "the garden of the king's palace" - inferable from palace frame (royal palace → garden expected). Rule 3.2 |
| palace (second) | **Routine (D)** | High | "the king's palace" - established location |

---

## Prediction Summary

**Total participants predicted**: ~85-90 across 12 verses

**Predicted distribution**:
- **Routine (D)**: ~60-65 participants (~70%)
- **Generic (G)**: ~20-25 participants (~25%)
- **Frame Inferable (F)**: ~2-3 participants (~3%)
- **First Mention (I)**: ~5-7 participants (~7%)
- **Interrogative (Q)**: 0 participants (0%) - no question contexts in selected verses

**Confidence**:
- High confidence: ~70% of predictions (clear algorithmic rules apply)
- Medium confidence: ~25% (ambiguous cases, edge decisions)
- Low confidence: ~5% (genuinely uncertain between states)

**Key ambiguities**:
1. Abstract nouns with possessives ("his grace", "his blood") - Generic or Routine?
2. Definite on first mention ("the court") - Frame Inferable or First Mention?
3. Measurements/quantities ("ten times", "seven days") - Generic or other?
4. Tribal/ethnic designations ("a Benjamite") - Generic or First Mention?

---

## Lock Commitment

**Status**: ✅ READY TO LOCK

These predictions are made using ONLY Algorithm v1.0 without accessing TBTA annotations.

**Next step**: Git commit to lock predictions, then proceed to Phase 7 validation.

**Locked commit SHA**: c485d295e59aa67948f38ab8210f7db7d6a2d3b4

---

**Created**: 2025-11-11
**Predictor**: Algorithm v1.0 (locked commit cb388ca)
**Verses**: 12 random test verses (1SAM×2, 2JN, ACT×3, DAN, EPH×4, EST)
**Method**: Blind prediction (NO TBTA ACCESS)
**Status**: READY FOR GIT LOCK
