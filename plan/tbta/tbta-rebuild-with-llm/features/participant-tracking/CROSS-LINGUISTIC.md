# Participant Tracking: Cross-linguistic Patterns

This document provides detailed examples of how different languages encode participant tracking.

## Language Family Comparison Table

| Family | Critical Features | Routine Encoding | First Mention | Frame Inferable | Impact Level |
|--------|-------------------|------------------|---------------|-----------------|--------------|
| **Switch-Reference** | SS/DS morphology | SS marker | DS marker + full NP | DS marker + definite | CRITICAL - grammatically required |
| **Topic-Prominent** | Topic particles (wa/ga) | Topic marker は wa | Subject marker が ga | Definite + が ga | CRITICAL - pragmatic structure |
| **Pro-Drop** | Zero anaphora | Zero Ø | Full NP + indef | Full NP + definite | HIGH - pronoun vs zero choice |
| **Non-Pro-Drop** | Explicit pronouns | Pronoun (he/she) | Full NP + indef | Full NP + definite | MEDIUM - pronoun required |
| **Article Languages** | Definite/indefinite | Pronoun or the+NP | a/an + NP | the + NP (first mention) | MEDIUM - article choice |
| **No-Article** | Context/word order | Position + bare noun | Bare noun + new position | Bare noun + established position | LOW-MEDIUM - word order signals |

## Detailed Language Examples

### 1. English (Non-Pro-Drop, Article Language)

**Text**: "A woman came to the well. She wanted water. The woman spoke to Jesus."

**Analysis**:
1. **"A woman"** → First Mention
   - **Form**: Indefinite article + noun
   - **Reasoning**: Indefiniteness signals discourse-new status

2. **"She"** → Routine
   - **Form**: Pronoun
   - **Reasoning**: Pronoun = high accessibility marker for established referent

3. **"water"** → Generic
   - **Form**: Bare noun (mass noun)
   - **Reasoning**: Non-specific water, not a particular quantity

4. **"The woman"** → Restaging
   - **Form**: Definite article + full NP after topic shift
   - **Reasoning**: Full NP (not pronoun) after gap, reactivating referent

**Key Features**:
- Indefinite/definite article distinction critical
- Pronouns required for routine reference (non-pro-drop)
- Full NP signals reactivation after gap

---

### 2. Japanese (Pro-Drop, Topic-Prominent, No Articles)

**Text**: "女が井戸に来た。Ø 水が欲しかった。女はイエスに話した。"
*Onna ga ido ni kita. Ø Mizu ga hoshikatta. Onna wa Iesu ni hanashita.*

**Analysis**:
1. **"女が" (onna ga)** → First Mention
   - **Form**: Noun + subject marker が (ga)
   - **Reasoning**: が marks new information, subject prominence
   - **Translation**: "A woman came to the well"

2. **"Ø"** → Routine
   - **Form**: Zero anaphora (no pronoun, no noun)
   - **Reasoning**: Topic continuity allows complete ellipsis in Japanese
   - **Translation**: "[She] wanted water"

3. **"水が" (mizu ga)** → Generic
   - **Form**: Bare noun + が (new information marker)
   - **Reasoning**: Non-specific water, が signals new topic
   - **Translation**: "water" (generic)

4. **"女は" (onna wa)** → Restaging
   - **Form**: Noun + topic marker は (wa)
   - **Reasoning**: は marks topic (contrast/reactivation); shift from が (new) to は (established topic)
   - **Translation**: "The woman spoke to Jesus"

**Key Features**:
- **が (ga)** marks NEW information / First Mention / subject focus
- **は (wa)** marks TOPIC / Routine (when established) / Restaging (when reactivated)
- Zero anaphora for clear routine continuations
- No articles; particles carry information structure load

**Particle Strategy**:
```
First Mention:  Noun + が (ga)
Routine:        Ø (zero) or Noun + は (wa) if topic
Restaging:      Noun + は (wa) with contrastive/reactivation force
Frame Inferable: Noun + が (ga) or は (wa) depending on newness vs topicality
```

---

### 3. Biblical Hebrew (Pro-Drop, VSO Word Order, Complex Definiteness)

**Text**: "ותבוא אשה אל הבאר. רצתה מים. האשה דברה אל ישוע."
*Watavo isha el habe'er. Ratzta mayim. Ha'isha dibra el Yeshua.*

**Analysis**:
1. **"אשה" (isha)** → First Mention
   - **Form**: Indefinite noun (no article)
   - **Reasoning**: First introduction, no definite article
   - **Translation**: "A woman came"

2. **"הבאר" (habe'er)** → Frame Inferable
   - **Form**: Definite article ha- + noun
   - **Reasoning**: Well is part of scene frame, uses definite despite first mention
   - **Translation**: "to the well"

3. **"Ø (verb רצתה)" → Routine**
   - **Form**: Zero subject (pro-drop), person/gender marked on verb
   - **Reasoning**: Subject continuity; verb morphology identifies 3fs (she)
   - **Translation**: "[She] wanted"

4. **"מים" (mayim)** → Generic
   - **Form**: Bare plural
   - **Reasoning**: Non-specific water
   - **Translation**: "water"

5. **"האשה" (ha'isha)** → Restaging
   - **Form**: Definite article + noun
   - **Reasoning**: Full noun (not pro-drop) after topic shift, reactivating participant
   - **Translation**: "The woman"

**Key Features**:
- Pro-drop: routine subjects dropped, marked on verb
- Definite article ha- for frame inferables and restaging
- VSO word order (Verb-Subject-Object typical)
- Subject continuity primary tracking mechanism

**Hebrew Definiteness Patterns**:
```
First Mention:     Bare noun (אשה isha "woman")
Routine:           Ø (dropped, marked on verb)
Frame Inferable:   ha- + noun (הבאר habe'er "the well")
Restaging:         ha- + noun (האשה ha'isha "the woman")
```

---

### 4. Mandarin Chinese (Topic-Prominent, Zero Anaphora, No Articles)

**Text**: "一个女人来到井边。Ø 想要水。那个女人跟耶稣说话。"
*Yīgè nǚrén láidào jǐng biān. Ø xiǎng yào shuǐ. Nàgè nǚrén gēn Yēsū shuōhuà.*

**Analysis**:
1. **"一个女人" (yīgè nǚrén)** → First Mention
   - **Form**: Numeral 一 (yī "one") + classifier 个 (gè) + noun
   - **Reasoning**: Numeral-classifier construction marks indefiniteness
   - **Translation**: "A woman came"

2. **"井边" (jǐng biān)** → Frame Inferable
   - **Form**: Bare noun compound (well-side)
   - **Reasoning**: Part of scene, no explicit marker but definite reading
   - **Translation**: "to the well"

3. **"Ø"** → Routine
   - **Form**: Zero subject
   - **Reasoning**: Topic continuity allows ellipsis; subject understood from context
   - **Translation**: "[She] wanted"

4. **"水" (shuǐ)** → Generic
   - **Form**: Bare noun
   - **Reasoning**: Mass noun, non-specific
   - **Translation**: "water"

5. **"那个女人" (nàgè nǚrén)** → Restaging
   - **Form**: Demonstrative 那 (nà "that") + classifier 个 (gè) + noun
   - **Reasoning**: Demonstrative marks definiteness and reactivation
   - **Translation**: "That woman"

**Key Features**:
- Classifier system: 个 (gè) for general items
- Numeral + classifier for indefiniteness (一个 yīgè "one [classifier]")
- Demonstrative + classifier for definiteness (那个 nàgè "that [classifier]")
- Extensive zero anaphora for routine reference

**Chinese Definiteness Strategy**:
```
First Mention:     一 yī (one) + classifier + noun
Routine:           Ø (zero)
Frame Inferable:   Bare noun or 这/那 zhè/nà (this/that) + classifier + noun
Restaging:         那 nà (that) + classifier + noun
```

---

### 5. Spanish (Pro-Drop with Rich Agreement, Articles)

**Text**: "Una mujer vino al pozo. Ø Quería agua. La mujer habló a Jesús."

**Analysis**:
1. **"Una mujer"** → First Mention
   - **Form**: Indefinite article una + noun
   - **Reasoning**: Indefinite marks new discourse referent
   - **Translation**: "A woman came"

2. **"al pozo"** (a + el = al) → Frame Inferable
   - **Form**: Contracted preposition+definite article + noun
   - **Reasoning**: Definite article despite first mention; part of scene
   - **Translation**: "to the well"

3. **"Ø Quería"** → Routine
   - **Form**: Null subject, 3sg imperfect verb
   - **Reasoning**: Rich verb morphology (quería = 3sg imperfect) identifies subject; pro-drop
   - **Translation**: "[She] wanted"

4. **"agua"** → Generic
   - **Form**: Bare mass noun (Spanish allows bare mass nouns)
   - **Reasoning**: Non-specific water
   - **Translation**: "water"

5. **"La mujer"** → Restaging
   - **Form**: Definite article + noun
   - **Reasoning**: Full NP (not pro-drop) signals reactivation
   - **Translation**: "The woman"

**Key Features**:
- Rich verb morphology allows pro-drop for routine subjects
- Article system similar to English (indefinite una/un, definite el/la)
- Pro-drop for routine, full NP for restaging

**Spanish Pro-drop Pattern**:
```
First Mention:  Una/Un + noun (indefinite article)
Routine:        Ø + verb (null subject, marked on verb)
Restaging:      El/La + noun (definite article + full NP)
```

---

## Switch-Reference Examples

### Iatmul (Papua New Guinea)

**Hypothetical Parallel**:
"Woman come-SS-3sg well-LOC. Ø want-SS-3sg water. Ø speak-DS Jesus-DAT."

**Analysis**:
- **-SS** (Same Subject marker) → Routine participant tracking
- **-DS** (Different Subject marker) → Participant shift
- Zero subjects allowed when SS marker indicates continuity
- Explicit subject when DS marker indicates shift

**Mapping to TBTA**:
- SS continuation → Routine
- DS shift → May indicate First Mention (new participant) or Restaging (returning participant)

---

## Translation Decision Matrix

| TBTA State | English | Japanese | Hebrew | Chinese | Spanish | Switch-Ref |
|------------|---------|----------|--------|---------|---------|------------|
| **First Mention** | a/an + NP | が ga + NP | Bare NP | 一(yī) + CL + NP | un/una + NP | DS + full NP |
| **Routine** | Pronoun | Ø or は wa | Ø (verb) | Ø | Ø (verb) | SS + Ø |
| **Frame Inferable** | the + NP | が/は + NP | ha- + NP | Bare or 这/那 + NP | el/la + NP | DS + def |
| **Restaging** | the + full NP | は wa + NP | ha- + NP | 那 nà + CL + NP | el/la + full NP | DS + full NP |
| **Generic** | Bare PL or a/an | Bare + が | Bare PL | Bare | Bare/PL | (not tracked) |

**Legend**:
- NP = Noun Phrase
- CL = Classifier
- Ø = Zero/null
- PL = Plural

---

## Critical Translation Errors

### Error 1: Pronoun Overuse in Pro-drop Languages

**English (acceptable)**: "He came to the well. He drew water. He drank."

**Spanish (awkward)**: "Él vino al pozo. Él sacó agua. Él bebió."
- Overuse of explicit pronoun "Él" (he)
- Should be: "Ø Vino al pozo. Ø Sacó agua. Ø Bebió."

**Reasoning**: TBTA Routine → Spanish requires zero (Ø), not explicit pronoun

---

### Error 2: Article Misuse in No-Article Languages

**English**: "The woman came. The woman wanted water."

**Japanese (wrong)**: "女は来た。女は水が欲しかった。"
*Onna wa kita. Onna wa mizu ga hoshikatta.*
- Overuse of topic marker は (wa)
- Second sentence should use zero

**Correct**: "女が来た。Ø 水が欲しかった。"
*Onna ga kita. Ø mizu ga hoshikatta.*

**Reasoning**: TBTA First Mention → が (ga), Routine → Ø (zero)

---

### Error 3: Indefinite/Definite Confusion

**Hebrew**: "ותבוא אשה אל הבאר..."
*Watavo isha el habe'er...*
"And came a-woman to the-well"

**English (wrong)**: "And came a woman to a well"
- "a well" treats well as First Mention
- But well is Frame Inferable (expected part of scene)

**Correct**: "And came a woman to **the** well"

**Reasoning**: TBTA Frame Inferable → Definite article even on first mention

---

## Language-Specific Notes

### Japanese Particle Nuances

**が (ga)** - Subject marker, NEW information:
- First Mention
- New topic introduction
- Exhaustive listing

**は (wa)** - Topic marker, GIVEN information:
- Routine (when topic is maintained)
- Restaging (when topic is reactivated)
- Contrast

**Switch pattern**:
"犬**が**来た。犬**は**吠えた。"
*Inu **ga** kita. Inu **wa** hoeta.*
"A dog **came**. The dog **barked**."
→ が marks First Mention, は marks Routine

---

### Biblical Hebrew Verb Forms

**Wayyiqtol** (narrative past):
- Often occurs with zero subject (pro-drop)
- Subject continuity unmarked on verb chain
- TBTA Routine encoded through verb sequence

**Qatal** (perfect):
- Can mark topic shift or participant reintroduction
- More likely to have explicit subject
- May signal TBTA Restaging

---

### Chinese Topic Chains

**Continuous zero**:
"张三来了。Ø 坐下。Ø 喝茶。Ø 说话。"
*Zhang San came. [Ø] sat. [Ø] drank tea. [Ø] spoke.*

All zeros = Routine tracking of Zhang San through topic chain

---

## High-Priority Language Families for TBTA

1. **Switch-Reference Systems** (CRITICAL):
   - 40+ families in Papua New Guinea
   - Amazonian languages (Cavineña, Guanano)
   - Participant tracking grammatically required

2. **Topic-Prominent** (CRITICAL):
   - Japanese, Korean
   - Chinese (Mandarin, Cantonese)
   - Pragmatic structure depends on tracking

3. **Pro-Drop** (HIGH):
   - Romance: Spanish, Italian, Portuguese
   - Greek (Biblical and Modern)
   - Biblical Hebrew
   - Zero vs explicit pronoun choice critical

4. **Article Languages with Pro-drop** (MEDIUM-HIGH):
   - Greek, Arabic
   - Complex interaction of articles and zero anaphora

---

## Summary

Participant tracking manifests differently across language families, but TBTA's 9-state system captures the underlying cognitive distinctions that all languages encode through their specific grammatical means:

- **Switch-reference**: Morphological marking (SS/DS)
- **Topic-prominent**: Particle choice (wa/ga)
- **Pro-drop**: Zero vs explicit encoding
- **Article languages**: Definite/indefinite choice
- **Word order**: Position signals discourse status

Understanding these cross-linguistic patterns ensures that TBTA annotations can be applied to translation into any target language.
