# Topic-Prominent Languages: Detailed Patterns

**Purpose:** Language-specific patterns for translating Topic NP annotations into topic-prominent languages.

**Coverage:** Japanese, Korean, Mandarin Chinese, Tagalog, Indonesian, Thai, Vietnamese, Burmese.

---

## Japanese (日本語)

**Speakers:** ~125 million
**Classification:** Japonic, topic-prominent + subject-marking

### Particle System: wa vs ga

| Particle | Function | When to Use | TBTA Mapping |
|----------|----------|-------------|--------------|
| **は (wa)** | Topic marker | Given info, contrast, general statements | Topic NP = A or P |
| **が (ga)** | Subject marker | New info, exhaustive listing, subject focus | Topic NP = N |
| **∅ wa** | Zero topic | Topic continuity (pro-drop) | Topic NP = A/P + Surface Realization = Zero |

### wa vs ga Decision Tree

```
1. Is NP previously mentioned or contextually given?
   → YES: Use wa (topic)
   → NO: Go to #2

2. Is this a contrastive context (X vs Y)?
   → YES: Use wa (contrastive topic)
   → NO: Go to #3

3. Is this answering "who/what" (exhaustive)?
   → YES: Use ga (subject focus)
   → NO: Use wa (default for generic statements)
```

### Examples from Scripture

**John 8:12** - Topic Continuity
```
TBTA: Topic NP = A (Jesus)
English: "Again Jesus spoke to them"
Japanese: "イエスは再び彼らに語られた"
         Iesu-WA futatabi karera-ni katarareta
```

**Genesis 1:1** - New Information
```
TBTA: Topic NP = N (no topic)
English: "In the beginning, God created"
Japanese: "初めに神が創造された"
         Hajime-ni Kami-GA souzou sareta
         (ga because God is new in discourse)
```

**Matthew 5:3** - Patient Topic
```
TBTA: Topic NP = P (poor in spirit)
English: "Blessed are the poor in spirit"
Japanese: "心の貧しい人々は幸いです"
         Kokoro-no mazushii hitobito-WA shiawai desu
         (wa because topic, even though patient)
```

### Special Cases

**Predicative Constructions:** Usually wa (topic-comment)
- "God IS love" → "神は愛です" (Kami-WA ai desu)

**Existential Constructions:** Usually ga (presentational)
- "There IS a man" → "男がいます" (Otoko-GA imasu)

**Possessive Constructions:** Usually wa for possessor
- "I HAVE a book" → "私は本があります" (Watashi-WA hon-GA arimasu)

---

## Korean (한국어)

**Speakers:** ~82 million
**Classification:** Koreanic, topic-prominent + subject-marking

### Particle System: eun/neun vs i/ga

| Particle | Function | When to Use | TBTA Mapping |
|----------|----------|-------------|--------------|
| **은/는 (eun/neun)** | Topic marker | Given info, contrast, general statements | Topic NP = A or P |
| **이/가 (i/ga)** | Subject marker | New info, exhaustive listing, subject focus | Topic NP = N |

**Allomorphy:**
- 은 (eun) after consonant: "예수는" (Yesu-neun)
- 는 (neun) after vowel: "하나님은" (Hananim-eun)
- 이 (i) after consonant: "사람이" (saram-i)
- 가 (ga) after vowel: "하나님이" (Hananim-i)

### Examples from Scripture

**John 1:1** - Multiple Topics
```
TBTA: Topic NP = A (Word)
English: "In the beginning was the Word"
Korean: "태초에 말씀이 계셨고"
        Taecho-e malsseum-I gyesyeotgo
        (i/ga because new in discourse)

        "And the Word was with God"
        "말씀은 하나님과 함께 계셨다"
        malsseum-EUN hananim-gwa hamkke gyesyeotda
        (eun/neun because now given, continuing topic)
```

**Psalm 23:1** - Generic Statement
```
TBTA: Topic NP = A (LORD)
English: "The LORD is my shepherd"
Korean: "여호와는 나의 목자시니"
        Yeohowa-NEUN na-ui mokja-si-ni
        (neun for generic/timeless statement)
```

### Special Cases

**Contrastive Topic:** Always eun/neun
- "You believe, but I don't" → "너는 믿지만, 나는 안 믿어"

**Weather/Time:** Usually ga (no topic)
- "Rain is falling" → "비가 온다" (bi-GA onda)

---

## Mandarin Chinese (普通话)

**Speakers:** ~1.2 billion (native + L2)
**Classification:** Sino-Tibetan, topic-prominent (no subject marking)

### Topic-Comment Structure

**Unlike Japanese/Korean, Mandarin has no topic particle.** Topic is marked by:
1. **Sentence-initial position** (unmarked topic position)
2. **的話 (de huà)** - "as for, speaking of" (marked topic)
3. **Zero anaphora** for topic continuity

### Topic Patterns

| Pattern | Structure | TBTA Mapping | Example |
|---------|-----------|--------------|---------|
| **SVO (canonical)** | Subject-Verb-Object | Topic NP = A (if subject=topic) | 神創造天地 (God created heaven-earth) |
| **Topic-Comment** | Topic, [Comment about it] | Topic NP = A or P | 那塊石頭，建造的人丟棄了 (That stone, builders rejected) |
| **Pro-drop** | ∅ Verb Object | Topic NP = A + Zero | (他)說... (∅ said...) |

### Examples from Scripture

**Matthew 5:3** - Topic Fronting
```
TBTA: Topic NP = P (poor in spirit)
English: "Blessed are the poor in spirit"
Mandarin: "虛心的人有福了"
         Xūxīn de rén yǒu fú le
         humble-heart DE people have blessing LE
         (Topic-comment: "humble people, have blessing")
```

**John 8:12** - Topic Continuity (Pro-drop)
```
TBTA: Topic NP = A (Jesus) + Surface Realization = Zero
English: "Again Jesus spoke to them"
Mandarin: "(耶穌)又對他們說"
         (Yēsū) yòu duì tāmen shuō
         (Jesus) again to them said
         (Jesus often dropped after first mention)
```

### Special Constructions

**把 (bǎ) Construction:** Patient → pre-verbal topic
```
"I read the book" → "我把書讀了" (Wǒ bǎ shū dú le)
TBTA: Topic NP = P (book moved to topic position)
```

**被 (bèi) Passive:** Patient becomes topic
```
"The book was read" → "書被讀了" (Shū bèi dú le)
TBTA: Topic NP = P (book as passive topic)
```

---

## Tagalog (Filipino)

**Speakers:** ~90 million (native + L2)
**Classification:** Austronesian, topic-prominent with focus system

### ang-Focus System

**Tagalog marks TOPIC (called "focus") with ang, not subject!**

| Marker | Function | TBTA Mapping |
|--------|----------|--------------|
| **ang** | Topic (definite) | Topic NP = A or P (depending on voice) |
| **ng** | Non-topic argument (genitive) | Not topic |
| **sa** | Oblique (location, beneficiary) | Not topic |

**Voice system aligns with topic:**
- Agent voice (-um-, mag-) → Agent is topic (ang)
- Patient voice (-in) → Patient is topic (ang)
- Location voice (-an) → Location is topic (ang)
- Beneficiary voice (i-) → Beneficiary is topic (ang)

### Examples from Scripture

**John 3:16** - Agent Topic
```
TBTA: Topic NP = A (God)
English: "For God so loved the world"
Tagalog: "Sapagkat gayon na lamang ang pag-ibig ng Diyos sa mundo"
         ANG Diyos (topic=God) + ng mundo (non-topic=world)
```

**Genesis 1:1** - Patient Topic (Common in Tagalog)
```
TBTA: Topic NP = P (heaven and earth)
English: "God created the heavens and the earth"
Tagalog: "Nilalang ng Diyos ang langit at lupa"
         ni-lalang (patient voice) ng Diyos (agent, non-topic) ANG langit at lupa (patient, topic)
```

**Critical:** Tagalog heavily prefers patient-topic constructions, even when English has agent-subject. Check TBTA Topic NP to determine voice selection.

---

## Indonesian/Malay

**Speakers:** ~280 million (native + L2)
**Classification:** Austronesian, topic-prominent (weaker than Tagalog)

### Topic Patterns

**No explicit topic marker**, but topic indicated by:
1. **Sentence-initial position** (default topic position)
2. **meN- voice** (agent topic) vs **di- voice** (patient topic)
3. **Zero anaphora** for topic continuity

### Voice and Topic

| Voice | Topic | Non-topic | TBTA Mapping |
|-------|-------|-----------|--------------|
| **meN- (active)** | Agent (initial) | Patient (post-verbal) | Topic NP = A |
| **di- (passive)** | Patient (initial) | Agent (optional oleh) | Topic NP = P |

### Examples from Scripture

**John 1:1** - Topic Continuity
```
TBTA: Topic NP = A (Word)
English: "In the beginning was the Word"
Indonesian: "Pada mulanya adalah Firman"
           (Firman in topic position, predicative)

"The Word was with God"
"Firman itu bersama-sama dengan Allah"
(Firman continues as topic)
```

---

## Thai (ภาษาไทย)

**Speakers:** ~69 million
**Classification:** Kra-Dai, topic-prominent

### Topic Patterns

**No grammatical topic marker**, but:
1. **Sentence-initial = topic** (unmarked)
2. **Pro-drop for topic continuity** (very common)
3. **เรื่อง (rêuang)** = "about, concerning" (marked topic)

### Examples

**John 8:12** - Pro-drop
```
TBTA: Topic NP = A (Jesus) + Surface Realization = Zero
English: "Again Jesus spoke"
Thai: "(พระเยซู)ตรัสอีกว่า"
      (Prá Yaysoo) dtrùat èek wâa
      (Jesus) spoke again that
      (Jesus dropped after first mention in discourse)
```

**Topic continuity in Thai is extreme:** Subjects/topics routinely dropped when discourse-given.

---

## Vietnamese (Tiếng Việt)

**Speakers:** ~95 million
**Classification:** Austroasiatic, topic-prominent

### Topic Patterns

1. **Sentence-initial position** (unmarked topic)
2. **Còn... thì...** = "as for X..." (marked topic)
3. **Pro-drop** (moderate, less than Thai)

### Examples

**Contrastive Topic**
```
"We preach, but you reject"
Vietnamese: "Còn chúng tôi thì rao giảng, nhưng anh em lại từ chối"
           Còn chúng-tôi THÌ (as for us), nhưng anh-em (but you)
TBTA: Topic NP = A (both pronouns)
```

---

## Summary Table

| Language | Topic Marker | Subject Marker | Pro-drop | Voice System |
|----------|-------------|----------------|----------|--------------|
| Japanese | は (wa) | が (ga) | High | Active/passive |
| Korean | 은/는 (eun/neun) | 이/가 (i/ga) | High | Active/passive |
| Mandarin | (position, 的話) | None | High | Active/passive/把/被 |
| Tagalog | ang | None (ng = non-topic) | Moderate | 4-way focus system |
| Indonesian | (position) | None | Moderate | meN-/di- voice |
| Thai | (position) | None | Very high | Active/passive |
| Vietnamese | (position, còn...thì) | None | Moderate | Active/passive |

---

## Translation Workflow

**For each verse with Topic NP annotation:**

1. **Check TBTA Topic NP value** (A/P/N)
2. **Determine target language topic marking:**
   - Japanese/Korean: wa/ga particle selection
   - Mandarin: position, pro-drop, or 的話
   - Tagalog: voice selection (agent vs patient)
   - Indonesian: meN-/di- voice selection
   - Thai/Vietnamese: pro-drop decision
3. **Verify topic continuity** across adjacent clauses (pro-drop context)
4. **Apply language-specific rules** (see above sections)

**Common pattern:** Participant Tracking = Restaging → Topic NP = A/P → Use topic marker in target language.
