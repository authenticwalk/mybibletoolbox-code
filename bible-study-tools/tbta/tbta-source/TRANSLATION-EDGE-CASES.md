# Translation Edge Cases

These examples demonstrate why TBTA's linguistic annotations are critical for Bible translation. Each case shows a concrete translation challenge where TBTA provides essential guidance that prevents errors in languages with grammatical features absent from English.

---

## Example 1: Trial Number System - Genesis 1:26

**Verse**: "Then God said, 'Let us create person...'"

**Challenge**: How many persons are speaking? English "us" is ambiguous between 2, 3, or many persons.

**Affected Languages**: 172+ Austronesian and Polynesian languages grammatically distinguish:
- **Dual** (exactly 2 persons)
- **Trial** (exactly 3 persons)
- **Paucal** (a few, small number)
- **Plural** (3+ or many persons)

**TBTA Encoding**:
```yaml
Constituent: "God"
Number: "Trial"           # Exactly 3 persons
Person: "First Inclusive" # "us" including the listener
```

**Translation Impact**:
Maintains Trinity reference in translation. Without TBTA, translators might use dual (2 persons) or generic plural (many persons), losing the theological precision. TBTA explicitly marks this as **trial** (exactly 3), guiding translators in Kilivila (Papua New Guinea), Larike (Maluku), and other trial-number languages to use the correct grammatical form that preserves the Trinitarian reference.

---

## Example 2: Inclusive vs Exclusive First Person - Acts 15:25

**Verse**: "It seemed good to us..."

**Challenge**: Does "us" include the listener or not? English "we/us" is ambiguous.

**Affected Languages**: 400+ languages distinguish:
- **Inclusive "we"** = speaker + listener (e.g., Tagalog "tayo", Malay "kita")
- **Exclusive "we"** = speaker + others, excluding listener (e.g., Tagalog "kami", Malay "kami")

Languages include: Tagalog, Malay, Indonesian, Fijian, Samoan, Tongan, Hawaiian, many Native American languages, and languages across Papua New Guinea.

**TBTA Encoding**:
```yaml
Person: "First Exclusive"  # Apostles speaking, congregation listening
```

**Translation Impact**:
In Acts 15:25, the apostles are speaking to the congregation about their decision. TBTA marks this as **First Exclusive** because "us" = the apostles only, not including the congregation being addressed. A Tagalog translator now knows to use **"kami"** (exclusive), not **"tayo"** (inclusive). Using the wrong form would incorrectly imply the congregation participated in the apostolic decision-making.

---

## Example 3: Participant Tracking - Genesis 4:8

**Verse**: "Cain said to Abel his brother, and he rose up and he killed him"

**Challenge**: Multiple pronouns ("he", "him") in a single verse - which "he" refers to which person? Who performed which action?

**Affected Languages**: 200+ languages with **switch-reference** systems (many Native American, Papua New Guinea, and Australian languages) that require grammatical markers when the subject changes or remains the same across clauses.

**TBTA Encoding**:
```yaml
# Noun List Index:
Cain: "1"
Abel: "2"
brother: "2"  # Same as Abel

# Participant Tracking:
Cain: "Routine"          # Established participant, subject
Abel: "Routine" → "Exiting"  # Dies in this verse
```

**Translation Impact**:
Languages with switch-reference (e.g., Amele, Hua, Usan in Papua New Guinea; Mojave, Choctaw in North America) grammatically mark whether the subject continues or changes:
- Cain speaks (subject = Cain)
- **Same subject marker**: Cain rose up
- **Same subject marker**: Cain killed (subject = Cain, object = Abel)

TBTA's participant tracking and noun list indexing explicitly identify which nouns refer to the same entity and which actions are performed by which participant, preventing translators from misidentifying the subject/object relationships.

---

## Example 4: Demonstrative Proximity - John 1:29

**Verse**: "Behold the Lamb of God"

**Challenge**: How far away is Jesus from the speaker and audience? English has only 2 distance levels (this/that), but many languages have 3, 4, or even 5 distinctions.

**Affected Languages**: 1000+ languages with multi-way demonstrative systems:
- **Japanese**: これ (kore - near me) / それ (sore - near you) / あれ (are - far from both) [3-way]
- **Korean**: 이 (i) / 그 (geu) / 저 (jeo) [3-way]
- **Spanish**: este (near me) / ese (near you) / aquel (far away) [3-way]
- **Some Native American languages**: Near speaker / Near listener / Near both / Remote visible / Remote invisible [5-way]

**TBTA Encoding**:
```yaml
Proximity: "S"  # Near Speaker (John)
# Options: N (near both), S (near speaker), L (near listener),
#          R (remote visible), r (remote invisible),
#          T (temporally near), t (temporally remote)
```

**Translation Impact**:
In John 1:29, Jesus is near John the Baptist (the speaker) but remote from the original listeners. A Japanese translator would use **それ** (sore - near you) rather than これ (kore - near me) or あれ (are - far from both). Without TBTA's proximity encoding, translators must guess the spatial relationship, potentially choosing a demonstrative that misrepresents the physical distance.

---

## Example 5: Time Granularity - Genesis Narratives

**Verse**: Genesis creation and patriarchal narratives (general example)

**Challenge**: When exactly did this happen? Some languages **require** specific time distinctions that English handles with context alone.

**Affected Languages**: 150+ languages with grammatically required time specificity:
- **Tagalog**: Different verb forms for "just now", "earlier today", "yesterday", "long ago"
- **Yimas (Papua New Guinea)**: 5 past tense distinctions (immediate, recent, mid-distance, distant, remote)
- **Nuer (South Sudan)**: Past tense distinguishes time-of-day
- **Many Bantu languages**: Near past vs. remote past grammatically required

**TBTA Encoding**:
```yaml
Time: "h"  # Historic Past (20+ time granularity options)
# Options include:
# D (immediate past), A (earlier today), a (yesterday),
# b (2 days ago), c (3 days ago), d (week ago), e (month ago),
# h (historic past), etc.
```

**Translation Impact**:
Genesis narratives describe events thousands of years ago. TBTA marks these as **"Historic Past"**, guiding Tagalog translators to use the remote past verb form rather than recent past. Similarly, in discourse sections where Jesus teaches timeless principles, TBTA can mark time as "Discourse/Timeless", prompting use of generic present forms. Without this encoding, translators might inconsistently apply tense markers, creating confusion about temporal distance.

---

## Example 6: Speaker Demographics - Genesis 19:31

**Verse**: Older daughter speaking to younger daughter: "Our father is old..."

**Challenge**: What is the social relationship, age difference, and appropriate register/formality level? Languages with grammatically required honorifics need this information.

**Affected Languages**: 500+ languages with grammatically required honorific/register systems:
- **Japanese/Korean**: Verb endings change based on age, social status, formality (5+ levels)
- **Javanese/Balinese**: 3-5 politeness levels (ngoko/low, madya/middle, krama/high) required for all speech
- **Thai/Khmer**: Royal register vs. common register
- **Nepali/Hindi**: Formal vs. informal "you" with corresponding verb agreement

**TBTA Encoding**:
```yaml
Speaker: "daughter"
Listener: "daughter"
Speaker_Age: "Young Adult (18-24)"
Speaker_Listener_Age: "Essentially the Same Age"
Speaker_Attitude: "Neutral"
Speech_Style: "Informal"
```

**Translation Impact**:
Sisters of approximately the same age speaking informally:
- **Japanese**: Use casual form (よ / yo), not respectful form (です / desu)
- **Korean**: Use informal ending (아/어), not honorific (습니다)
- **Javanese**: Use ngoko (intimate), not krama (respectful)

Without TBTA's demographic data, translators must guess the social relationship from context. In Genesis 19:31, using a respectful register would sound strange (sisters don't speak formally to each other), while in Genesis 18:3 (Abraham speaking to divine visitors), formal register is required. TBTA provides this social-pragmatic information explicitly.

---

## Summary: Why This Matters

### The Translation Problem

English-trained AI systems and commentaries assume English grammatical categories:
- 2 numbers (singular/plural)
- 2 demonstratives (this/that)
- Ambiguous "we" (no inclusive/exclusive distinction)
- Context-based time references
- No grammatical honorifics

But **1000+ languages** have mandatory grammatical features absent from English.

### The TBTA Solution

TBTA provides explicit annotations for cross-linguistic edge cases:
- ✅ Number systems: dual, trial, quadrial, paucal
- ✅ Person systems: inclusive/exclusive first person
- ✅ Participant tracking: noun indexing and discourse flow
- ✅ Proximity: multi-way demonstrative distinctions
- ✅ Time granularity: 20+ temporal distance levels
- ✅ Social register: age, relationship, formality, attitude

### Real-World Impact

**Scenario**: AI assists translator working in:
- Kilivila (Papua New Guinea) - has trial number
- Ilokano (Philippines) - has inclusive/exclusive distinction
- Japanese - needs demonstrative proximity + age-based register

**Without TBTA**: AI defaults to English categories → translation errors

**With TBTA**: AI provides language-specific guidance → accurate, culturally appropriate translation

### Macula + TBTA = Comprehensive Coverage

- **Macula**: "What does the Greek/Hebrew say grammatically?" (morphology, syntax, semantics)
- **TBTA**: "How should this be rendered in languages with different categories?" (cross-linguistic pragmatics)

Together, they provide AI systems with the complete linguistic context needed for grounded, accurate Bible translation across all 7,000+ world languages.
