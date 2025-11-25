# Surface Realization: Cross-Feature Interactions

> **Parent Context:** How Surface Realization interacts with other TBTA features (Participant Tracking, Person, Number, Honorifics, Switch-Reference, Proximity).

## Gateway Feature: Participant Tracking (PRIMARY - 95% correlation)

**Relationship**: Near-perfect correlation. Surface realization is the OUTPUT of participant tracking state.

| Tracking State | Surface Realization | Confidence | Notes |
|---------------|---------------------|------------|-------|
| First Mention | **Noun** | 95%+ | Introducing new referent |
| Routine | **Pronoun** / **Zero** | 90%+ | Depends on pro-drop status |
| Restaging | **Noun** | 85%+ | Reintroducing after absence |
| Frame Inferable | **Noun** (definite) | 90%+ | "The priest" (role-based) |
| Generic | **Noun** (often bare) | 85%+ | "Water is essential" |
| Offstage | **Noun** (modifier) | 95%+ | "Peter's house" |

**Usage guideline**: ALWAYS check Participant Tracking state FIRST before predicting surface realization. Tracking state is the primary predictor.

**Validation rule**: If Tracking = First Mention but Surface = Zero → **FLAG ERROR** (except in rare contexts like diary style or highly elliptical discourse)

**Exception handling**: In rare cases of zero at first mention, verify:
- Diary register (highly elliptical)
- Chain clause structure (some Trans-New Guinea languages)
- Topic-prominent discourse (Japanese, Korean allowing topic-marked zero introduction)

---

## Predicting from Source Language

### Greek/Hebrew Explicit Pronoun → Emphasis Signal

**Pattern**: When Greek/Hebrew has explicit pronoun in pro-drop context

**Interpretation**:
- Unusual → Signals emphasis, contrast, or disambiguation
- αὐτός (autos) = "HE himself" (emphatic)
- Contrast: "Not you, but HE"
- Disambiguation when multiple referents present

**Translation strategy**:
- Preserve emphasis in target language
- Use explicit pronoun even in pro-drop target
- Or use focal cleft structure ("It is HE who...")

**Warning**: Do NOT infer emphasis from absence of pronoun in source. Zero is the norm.

---

### Greek/Hebrew Zero → Normal Routine Reference

**Pattern**: No explicit pronoun in Greek/Hebrew

**Interpretation**:
- Normal, unmarked routine reference
- Cannot infer emphasis from absence
- Default state in pro-drop languages

**Translation strategy**:
- **Pro-drop target**: Use zero (natural)
- **Non-pro-drop target**: Must use pronoun (grammatical requirement)
- Zero in source does NOT mean zero in target

---

### English Always Explicit → Cannot Infer Emphasis

**Pattern**: English "he" appears

**Problem**: Could be routine OR emphatic (English doesn't distinguish)

**Solution**: Check Greek/Hebrew source for emphasis signals
- If Greek/Hebrew has explicit pronoun → Likely emphatic
- If Greek/Hebrew has zero (verb agreement) → Routine (English requirement, not emphasis)

**Translation strategy**: Rely on source language, not English intermediate

---

## Correlation with Person/Clusivity (70% correlation)

**Relationship**: Clusivity applies even when subject is zero

**Example**:
- Spanish: "[∅] Vamos" = "We (inclusive/exclusive?) go"
- Surface = **Zero**, but person = 1PL, clusivity = TBD

**Important points**:
1. Zero surface form does NOT mean person is unspecified
2. Person/number encoded in verb morphology
3. Clusivity distinction still matters for translation
4. Must analyze verb agreement, not just surface form

**Application for pro-drop languages**:
- Zero subjects still have person/number features
- 1st plural zero → Check clusivity (inclusive/exclusive)
- Verb morphology carries full person/number/clusivity information

**Validation**: In pro-drop languages with clusivity distinction:
- If verb is 1PL → Mark clusivity (even if surface=zero)
- Spanish "vamos" → Ambiguous (no morphological distinction)
- Indonesian "pergi" → Check context for "kita" (inclusive) vs "kami" (exclusive)

---

## Correlation with Number (65% correlation)

**Relationship**: Number affects pronoun selection and pro-drop patterns

### Dual/Trial/Paucal Languages

**Pattern**: Special pronoun forms for exact quantities

**Example**:
- "The two disciples" → If pronoun used, must be dual form
- Hebrew/Greek encode number in verb morphology
- Affects pro-drop: Number visible in verb even when subject is zero

**Application**:
- Greek: "ἦλθον" (elthon) = "came-3PL" (zero subject, plural)
- Target with dual: Must check if exactly 2 or more than 2
- Dual form required if exactly 2

### Languages Without Number Distinction in Pronouns

**Pattern**: Some languages don't mark number on pronouns (or limited marking)

**Example**: Chinese, Japanese, Thai
- Pronouns may not distinguish singular/plural
- Context or classifiers provide number information
- Surface realization less tied to number

---

## Correlation with Honorifics/Register (60% correlation)

**Relationship**: Formality affects pronoun choice and noun usage

### T-V Distinction Languages

**Pattern**: Formal vs informal pronoun choice (French tu/vous, Spanish tú/usted)

**Application**:
- Pronoun selection depends on social distance
- Formal contexts may use title + name instead of pronoun
- Example: "The teacher said" (formal) vs "He said" (informal)

**Bible translation considerations**:
- Prayers to God → High formality (many languages)
- May prefer nouns over pronouns even for routine reference
- Example: "The Lord" repeated instead of "He"

### Japanese/Korean Honorific Systems

**Pattern**: Extensive honorific systems affecting all pronouns

**Application**:
- Pronoun choice dramatically affected by formality
- High-formality contexts may avoid pronouns entirely
- Use title/role noun instead: "The teacher" (not "he")
- Verb endings carry honorific information

**Zero subjects in honorific contexts**:
- Japanese allows zero with honorific verb forms
- Surface = Zero, but honorific level = High
- Honorifics encoded in verb morphology, not surface form

---

## Correlation with Switch-Reference (80% correlation)

**Relationship**: Switch-reference systems interact strongly with surface realization

### Languages with Switch-Reference

**Pattern**: Marking on verb indicates if subject is same or different from previous clause

**Examples**: Many Papuan languages, some Mayan languages

**Application**:
- **Same-subject (SS) marker** → Often allows zero
  - Amele: "John came-SS [∅] ate" → Same subject, zero OK
- **Different-subject (DS) marker** → May require noun or pronoun
  - Amele: "John came-DS Mary ate" → Different subject, must be explicit

**Validation rule**: If language has switch-reference, check consistency:
- SS marking + Zero → ✓ Consistent
- SS marking + Different noun → ✗ Inconsistent (flag error)
- DS marking + Same referent noun → ✓ Can be consistent (disambiguation)
- DS marking + Zero → ✗ Likely inconsistent

### Chain Clauses with Medial Verbs

**Pattern**: Trans-New Guinea languages use chains of medial verbs

**Application**:
- Long chains with single final verb
- Medial verbs carry switch-reference
- Zero subjects throughout chain (except at switches)
- Surface realization highly constrained by clause type

---

## Correlation with Proximity (Demonstratives) (50% correlation)

**Relationship**: Demonstrative determiners affect noun phrase form

### When Noun Appears with Demonstrative

**Pattern**: Demonstrative + noun = full NP (cannot reduce)

**Examples**:
- "This man" → Surface = **Noun**, Proximity = Near
- "That man" → Surface = **Noun**, Proximity = Far

**Constraint**: Cannot use zero/pronoun with demonstrative
- Must be full noun phrase
- Demonstrative + noun = single constituent

### Demonstrative Pronouns

**Pattern**: "This one", "That one" in languages with demonstrative pronouns

**Analysis options**:
- Some analyses: Pronoun with demonstrative modifier
- TBTA analysis: Treat as **Pronoun** (the head is pronominal)

**Cross-linguistic variation**:
- English: Can reduce to "this" or "that" (pronoun)
- Spanish: "este" can be pronoun or determiner
- Japanese: "kore" (this) is pronoun (no noun needed)

---

## Discourse Factors Affecting Surface Realization

### 1. Givenness/Information Status (Ariel's Accessibility Hierarchy)

**Accessibility Scale** (most to least accessible):
1. Zero / Unstressed pronoun (highest accessibility)
2. Stressed pronoun
3. Demonstrative pronoun
4. Definite description
5. Indefinite description (lowest accessibility)

**Application**:
- New/Unknown → Noun (indefinite): "A rabbi came"
- Given/Known → Pronoun/Zero: "He taught" or "[∅] Taught"
- Accessible/Inferrable → Definite noun: "The rabbi"

---

### 2. Distance from Antecedent

**Pattern**: Accessibility decreases with distance

- **Adjacent (0-1 clauses)**: Zero most common (pro-drop languages)
- **Nearby (2-3 clauses)**: Pronoun common
- **Distant (4+ clauses)**: Noun preferred for clarity

**Language variation**:
- Japanese: Allows zero even at distance if salient
- English: Requires noun if 3+ clauses away
- Spanish: Intermediate (zero for salient topics at moderate distance)

---

### 3. Semantic Role and Saliency

**Pattern**: Agents and salient participants allow more reduction

- **Agents**: Pro-drop more likely
- **Patients**: May require more explicit marking
- **Inanimate**: More likely to require explicit marking
- **Salient characters** (Jesus, God): Pro-drop more likely even at distance

---

### 4. Register and Style

**Pattern**: Formality increases explicitness

- **Formal written**: More nouns, more explicit
- **Informal spoken**: More pro-drop, more pronouns
- **Narrative**: Often high use of zero (pro-drop languages)
- **Direct speech**: More pronouns for clarity

---

## Cross-Feature Validation Checks

**Validation rules** (flag for review if violated):

1. **Tracking + Surface mismatch**: First Mention with Zero (except rare cases)
2. **Pro-drop + Distribution**: Pro-drop language with 0% zero (except formal register)
3. **Person + Zero**: Zero subject without person encoding in verb morphology
4. **Switch-reference + Surface**: SS marking with different referent noun
5. **Demonstrative + Zero**: Demonstrative determiner with zero realization
6. **Number + Pronoun**: Dual number with plural pronoun form

---

**See Also**:
- [Prediction methodology](prediction-methodology.md)
- [Participant Tracking feature](../participant-tracking/README.md)
- [Key findings](LEARNINGS.md)
