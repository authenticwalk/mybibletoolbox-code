# Translator-Focused Documentation Improvements

**Revised Goal Understanding**: TBTA helps translators solve translation problems that are **specific to their target language** but **not marked in source languages** (Hebrew/Greek), by showing how 900+ other languages solved these problems.

## The Real Problem TBTA Solves

### Example: Clusivity (Inclusive vs Exclusive "we")
- **Greek**: Has one word "ἡμεῖς" (we) - no distinction
- **Your target language** (e.g., Indonesian): Has TWO words - "kita" (inclusive: we+you) vs "kami" (exclusive: we, not you)
- **Translation problem**: Greek doesn't tell you which one!
- **TBTA solution**: Shows you that Japanese uses inclusive here, Korean uses exclusive, Swahili uses inclusive → Pattern emerges (85% inclusive)
- **Translator decision**: Now you can confidently choose "kita" (inclusive) for your Indonesian translation

**This is fundamentally about translator decision support, not annotation accuracy!**

---

## Critical Improvements (Revised for Translator Focus)

### 1. **Language-Specific Feature Relevance Checker** ⭐⭐⭐⭐⭐ HIGHEST PRIORITY

**Problem**: Translators waste time reading about features irrelevant to their language

**Solution**: Quick assessment tool per language family

**Example - Create: `FEATURE-RELEVANCE-BY-LANGUAGE.md`**

```markdown
## Quick Feature Relevance Assessment

### For Austronesian Languages (Filipino, Indonesian, Maori, Hawaiian, etc.)

**CRITICAL Features** (You MUST consider these):
- ✅ Person/Clusivity - Inclusive vs exclusive "we" (kita vs kami in Indonesian)
- ✅ Illocutionary Force - Sentence particles required (Filipino po/ho, Tagalog nga/ba)
- ✅ Speaker Attitude - Honorifics and formality levels
- ✅ Proximity - Distance distinctions in demonstratives

**HIGH PRIORITY Features**:
- ⭐ Topic NP - Topic-prominent structure (ang-focus in Tagalog)
- ⭐ Number Systems - Some have dual/trial (Tok Pisin tupela/tripela)
- ⭐ Surface Realization - Pro-drop patterns

**LOW PRIORITY / Skip**:
- ❌ Degree - Most Austronesian use analytic (mas, paling)
- ❌ Time Granularity - Typically 3-way past/present/future only

### Time Saved: Focus on 7 features instead of 59 (88% reduction)

---

### For Bantu Languages (Swahili, Kinyarwanda, Luganda, Chichewa, etc.)

**CRITICAL Features**:
- ✅ Salience Band - Foreground/background verb forms (-ka- vs -ki- in Swahili)
- ✅ Participant Tracking - Switch-reference and topic continuity
- ✅ Number Systems - Some have classes affecting agreement
- ✅ Surface Realization - Extensive pro-drop

**HIGH PRIORITY Features**:
- ⭐ Mood - Subjunctive used extensively
- ⭐ Aspect - Perfective/imperfective obligatory
- ⭐ Proximity - Distance-from-speaker systems

**LOW PRIORITY / Skip**:
- ❌ Clusivity - Not distinguished in Bantu
- ❌ Topic NP - Subject-prominent, not topic-prominent
- ❌ Degree - Typically analytic

### Time Saved: Focus on 10 features instead of 59 (83% reduction)

---

### For East Asian (Japanese, Korean, Mandarin)

**CRITICAL Features**:
- ✅ Topic NP - Topic-prominent languages (wa/ga, eun/neun, 的话)
- ✅ Speaker Demographics - ALL 6 features (honorifics obligatory)
- ✅ Illocutionary Force - Sentence-final particles required
- ✅ Surface Realization - Extensive zero-anaphora

**HIGH PRIORITY Features**:
- ⭐ Polarity - Negative concord patterns (Japanese)
- ⭐ Number Systems - Often unmarked, context-dependent
- ⭐ Proximity - Complex demonstrative systems

**LOW PRIORITY / Skip**:
- ❌ Clusivity - Not distinguished (except some Korean dialects)
- ❌ Salience Band - Clause chaining but not verb-marked
- ❌ Time Granularity - Typically simple tense systems

### Time Saved: Focus on 12 features instead of 59 (80% reduction)

[Continue for 20+ language families...]
```

**Action Items**:
- [ ] Create language family profiles for all major families
- [ ] Add "Is this relevant to MY language?" section to each feature README
- [ ] Build interactive assessment tool (answer 10 questions → get your priority list)

**Estimated Effort**: 40-60 hours
**Impact**: Translators focus only on relevant features (80-90% time savings)

---

### 2. **Cross-Linguistic Pattern Visualizations** ⭐⭐⭐⭐⭐ HIGHEST PRIORITY

**Problem**: "How did other languages solve this?" is buried in prose

**Solution**: Visual pattern summaries showing translation strategies

**Example - Add to each feature: `TRANSLATION-PATTERNS.md`**

```markdown
## Clusivity: How 900+ Translations Handled "We" in Key Verses

### Genesis 1:26 - "Let US make man in OUR image"

**Greek**: ποιήσωμεν (no clusivity marking)

**Translation Consensus**:
```
█████████████████ 85% EXCLUSIVE (we=Trinity, not including humans)
███ 15% INCLUSIVE or AMBIGUOUS

EXCLUSIVE (we = God alone):
- Indonesian: "Kami" (exclusive)
- Swahili: "tufanye" (exclusive 1pl)
- Japanese: "我々" (watashitachi, exclusive sense)
- Kinyarwanda: "Tureke" (exclusive)
- 150+ other languages

INCLUSIVE (we = God+angels?):
- Some Polynesian: inclusive (God+heavenly court)
- 20-30 languages

AMBIGUOUS:
- English: "we" (unmarked)
- Spanish: "nosotros" (unmarked)
```

**Your Decision Factors**:
1. **Theology**: Is this Trinity speaking (exclusive)? Or God+angels (inclusive)?
2. **Context**: "in our image" → likely exclusive (Trinity's image)
3. **Language family**: Most Austronesian, Bantu, Native American → exclusive
4. **Recommendation**: Use EXCLUSIVE (85% consensus)

---

### Acts 15:28 - "It seemed good to US and to the Holy Spirit"

**Greek**: ἡμῖν (no clusivity marking)

**Translation Consensus**:
```
██████████████████████ 95% EXCLUSIVE (we=apostles, not you readers)
█ 5% INCLUSIVE or UNCLEAR

EXCLUSIVE (apostles, not readers):
- Indonesian: "Kami" (exclusive)
- Japanese: "私たち" (watashitachi, exclusive)
- Swahili: "sisi" (emphatic exclusive)
- Korean: "우리" (uri, but exclusive sense from context)
- 200+ languages

Context clarity: "seemed good to US and to the Holy Spirit" → clear separation
```

**Your Decision**: EXCLUSIVE (95%+ consensus, context very clear)

---

### 1 John 1:3 - "That you may have fellowship with US"

**Greek**: ἡμῶν (no clusivity marking)

**Translation Consensus**:
```
██████████████████ 75% INCLUSIVE (we=believers including you)
██████ 25% EXCLUSIVE (we=apostles, you join us)

INCLUSIVE (we+you will have fellowship together):
- Indonesian: 60% use "kita" (inclusive)
- Japanese: "私たち" (but can be inclusive here)
- Some Bantu: inclusive forms
- Rationale: "fellowship WITH us" implies joining = inclusive

EXCLUSIVE (we=apostles, separate from you readers):
- Indonesian: 40% use "kami" (exclusive)
- Some languages treat apostles as separate category
- Rationale: Apostolic authority → exclusive

This is a JUDGMENT CALL - no clear consensus!
```

**Your Decision Factors**:
1. **Theology**: Is John including readers in "us"? (probably yes)
2. **Discourse**: "that YOU may have fellowship WITH us" (suggests inclusive)
3. **Translation tradition**: Check your language's pattern in similar verses
4. **Recommendation**: Lean INCLUSIVE (70-75%), but EXCLUSIVE defensible

```

**Format for every important verse**:
- Show percentage breakdown
- List specific language examples
- Highlight decision factors
- Give clear recommendation with confidence level
- Note when it's ambiguous (translator judgment needed)

**Action Items**:
- [ ] Create translation pattern summaries for 100-200 key verses per feature
- [ ] Focus on verses where source language is ambiguous
- [ ] Show visual consensus bars
- [ ] Document minority interpretations
- [ ] Add "Why they differ" explanations

**Estimated Effort**: 8-12 hours per feature × 22 = 176-264 hours
**Impact**: Translators see patterns at a glance, make confident decisions

---

### 3. **"Languages Like Yours" Recommendations** ⭐⭐⭐⭐⭐

**Problem**: 900 translations overwhelming - which ones matter for MY language?

**Solution**: Show how genetically/typologically similar languages solved it

**Example - Add to each verse annotation:**

```markdown
## Romans 1:1 - Paul's Self-Introduction

### Your Language: Javanese

**Languages typologically similar to yours:**

**Same family (Austronesian)**:
- Indonesian: "hamba" (low honorific, appropriate for addressing God)
- Tagalog: "alipin" (servant/slave)
- Malay: "hamba" (low status)
- Maori: "pononga" (servant)
→ **Pattern**: Austronesian uses low-status self-reference

**Similar honorific systems**:
- Japanese: "僕" (boku, humble first-person when addressing superior)
- Korean: "종" (jong, slave/servant with humble verb ending)
- Thai: "ข้าพเจ้า" (kha phom, highly formal humble pronoun)
→ **Pattern**: Honorific languages use humble self-designations

**Your decision**:
- Use Javanese KRAMA INGGIL register (highest respect)
- Self-reference: "kawula" (very humble "I")
- Paul is addressing God → requires highest respect level
- **Recommended**: "Kawula Paulus, abdi dalem Kristus Yesus" (humble servant of Christ Jesus)

**Why this matters**:
- Javanese has 10+ speech levels
- Wrong level = incomprehensible or offensive
- Other Austronesian + honorific languages all go HIGH respect here
- 95% of similar languages agree
```

**Also show**:
- Genetic relationship (language family tree)
- Typological similarity (honorific systems, topic-prominent, etc.)
- Geographic proximity (regional translation traditions)
- Which languages to prioritize for your specific case

**Action Items**:
- [ ] Map all 900 languages by family and typology
- [ ] Create "similar languages" lookup table
- [ ] Add "Your language: X → Check these 10-20 translations" to each feature
- [ ] Weight by relevance (genetic > typological > geographic)

**Estimated Effort**: 60-80 hours (one-time investment)
**Impact**: Translators see most relevant examples (90% noise reduction)

---

### 4. **Translation Problem Statements** ⭐⭐⭐⭐⭐

**Problem**: Documentation explains linguistics, not practical translation issues

**Solution**: Lead with the translation problem, not the linguistic theory

**Example - Reframe each feature README:**

**CURRENT** (Salience Band):
```markdown
# Salience Band

Salience Band indicates the discourse prominence level of clauses in narrative...

[500 words of linguistic theory]
```

**IMPROVED** (Translation-Problem-First):
```markdown
# Salience Band: Foreground vs Background

## The Translation Problem

**You're translating to Swahili (or other Bantu language)**:

Your language has **different verb forms for main storyline vs background information**:
- **-ka-** tense: Main storyline (foreground) - "And then he said..."
- **-ki-** tense: Background information (setting, simultaneous action) - "While he was..."
- **-li-** tense: Scene-setting (time anchor) - "In those days..."

**Greek and Hebrew don't mark this!**
- Greek uses aorist for both foreground and some background
- Hebrew wayyiqtol is mostly foreground, but not always

**If you get this wrong:**
- Story becomes confusing (what's main plot vs side information?)
- Sounds unnatural to native speakers
- Misses discourse structure

**TBTA helps you by:**
- Showing which clauses are foreground (Primary/Pivotal) → use -ka-
- Showing which are background (Background/Setting) → use -ki- or -li-
- Comparing with other Bantu translations for patterns

---

## Quick Translation Guide

### Step 1: Identify YOUR language's system

**Does your language have different verb forms for:**
- ☐ Main storyline vs background? (Bantu, some Native American)
- ☐ Main clause vs subordinate clause? (Most languages)
- ☐ Just word order changes? (English, Chinese)

**If NO to all**: You can probably skip this feature (use default translation)

**If YES to #1**: This feature is CRITICAL - read full documentation

**If YES to #2-3**: This feature is helpful for better discourse flow

### Step 2: Check what TBTA says

For each clause, TBTA gives salience level:
- **Pivotal** (5%) → STRONGEST foreground (climax, turning point)
- **Primary** (25%) → Main storyline
- **Secondary** (40%) → Supporting information
- **Background** (25%) → Setting, circumstances
- **Setting** (5%) → Scene-setting

### Step 3: Map to YOUR language

**For Swahili**:
- Pivotal → -ka- (with emphasis)
- Primary → -ka- (sequential chain)
- Secondary → -ka- or -ki- (depending on whether advancing plot)
- Background → -ki- (circumstantial)
- Setting → -li- (scene anchor)

**For English** (word order, not verb form):
- Pivotal → Main clause, emphatic position
- Primary → Main clause
- Secondary → Main or subordinate clause
- Background → Subordinate clause ("while...", "when...")
- Setting → Temporal phrase at start

### Step 4: Check similar languages

**Other Bantu languages** (Kinyarwanda, Luganda, Chichewa):
- Genesis 1:3 "God said" → ALL use foreground form (Primary)
- Genesis 1:2 "earth was formless" → ALL use background (Setting)
- John 9:6 "While saying this, he spat" → Split: main clause foreground, participle background

**Your pattern**: When Bantu languages agree 90%+, follow the pattern

---

## Examples: How to Use TBTA for Translation

[Complete worked examples showing the TRANSLATION DECISION PROCESS, not just linguistic annotation]

```

**This format**:
1. Starts with the practical problem
2. Explains why it matters (consequences of errors)
3. Gives step-by-step translation process
4. Shows how to use TBTA data
5. Provides similar-language comparison

**Action Items**:
- [ ] Rewrite all 22 feature READMEs starting with translation problem
- [ ] Add "Quick Translation Guide" (5 steps max)
- [ ] Show translation decision process, not just annotation
- [ ] Include "Does your language need this?" early
- [ ] Add "Consequences of getting it wrong" section

**Estimated Effort**: 3-4 hours per feature × 22 = 66-88 hours
**Impact**: Translators immediately understand relevance and usage

---

### 5. **Common Translation Mistakes** ⭐⭐⭐⭐

**Problem**: "Common Errors" sections focus on annotation errors, not translation errors

**Solution**: Document actual translation mistakes with before/after

**Example - Add to each feature: `TRANSLATION-MISTAKES.md`**

```markdown
## Common Translation Mistakes: Clusivity

### Mistake #1: Prayer - Assuming All Prayer Uses Exclusive

**Wrong Translation** (Indonesian):
```
Matthew 6:9 - "Bapa kami yang di surga" (Our Father, EXCLUSIVE)
```
**Why it's wrong**: This implies "Our Father (not including you who I'm talking to)" - but Jesus is teaching the disciples to pray together (inclusive)

**Correct Translation**:
```
Matthew 6:9 - "Bapa kita yang di surga" (Our Father, INCLUSIVE)
```
**Why**: Jesus says "When YOU pray, say OUR..." - the "our" includes the listeners (inclusive)

**How to avoid**: Check if prayer is:
- Intercessory (praying FOR others) → Often exclusive
- Corporate (praying WITH others) → Often inclusive
- Taught prayer (teaching others to pray) → Usually inclusive

---

### Mistake #2: Divine Speech - Defaulting to Inclusive

**Wrong Translation** (Swahili):
```
Genesis 1:26 - "Tufanye mtu kwa mfano WETU" (Let us make man, INCLUSIVE)
```
**Why it's wrong**: This suggests God is including humans/angels in "our" - but humans don't exist yet!

**Correct Translation**:
```
Genesis 1:26 - "Na Mungu akasema, 'Tufanye binadamu...' " (EXCLUSIVE - Trinity)
```
**Why**: The Trinity is speaking (Father, Son, Spirit) - not including anyone else

**How to avoid**: When God says "we/us":
- Check context: Who could be included?
- If before creation → Must be exclusive (Trinity only)
- If heavenly council mentioned → Could be inclusive (God+angels)
- Theological tradition in your translation

---

### Mistake #3: Apostolic Authority - Mixing Up Apostle vs Believer

**Tricky Case** (Indonesian):
```
1 John 1:3 - "Yang kami lihat dan dengar, kami wartakan kepada kamu"
             (What WE saw and heard, WE proclaim to you)
```

**Question**: Is this:
- **Exclusive** "kami" (we apostles, not you readers)?
- **Inclusive** "kita" (we believers together)?

**Most translations**: EXCLUSIVE "kami" (70%)
- Why: Apostles saw Jesus personally (you readers didn't)
- "What WE saw... WE proclaim to YOU" = clear distinction

**But**: Next clause says "so you may have fellowship with us" (kita? kami?)
- Some use **inclusive** here (you join us in fellowship = we together)
- Some use **exclusive** (you have fellowship with us, we remain distinct)

**How to decide**:
1. Check your language's translation tradition
2. Check related verses (1 John 1:1-4 as unit)
3. Ask: Does your theology emphasize apostolic authority (exclusive) or believer unity (inclusive)?
4. Be consistent throughout 1 John

---

### Mistake #4: Copy English Without Thinking

**Wrong Assumption**: "English doesn't mark it, so it doesn't matter"

**Harmful Result**:
```
English: "We will go" (ambiguous)
[Translator copies without deciding]
Target language: Uses random form (inconsistent)
```

**Why it's harmful**:
- Inconsistent clusivity confuses readers
- "We" in verse 1 = exclusive, verse 2 = inclusive (same English word!) → readers confused
- Missing the discourse pattern

**Correct Approach**:
1. English is ambiguous - don't copy blindly
2. Check TBTA: What do similar languages do?
3. Look for patterns in nearby verses
4. Make deliberate choice for your language
5. Be consistent

---

## Translation Checklist: Before Finalizing

For each "we/us/our" in your translation:

- [ ] Have you deliberately chosen inclusive vs exclusive?
- [ ] Is it consistent with nearby verses?
- [ ] Does it match what similar languages did?
- [ ] Have you checked TBTA consensus (is it 85%+)?
- [ ] Have you considered theological implications?
- [ ] If ambiguous, have you added a footnote explaining?

**Never**: Just copy English/source without thinking about YOUR language's requirements
```

**Action Items**:
- [ ] Document 10-20 common translation mistakes per feature
- [ ] Show wrong/right examples from actual translations
- [ ] Explain WHY it's wrong (consequences)
- [ ] Give decision-making process
- [ ] Add translation checklist

**Estimated Effort**: 6-10 hours per feature × 22 = 132-220 hours
**Impact**: Prevents common errors, improves translation quality

---

### 6. **Verse-Level Translation Commentary** ⭐⭐⭐⭐

**Problem**: TBTA data is just labels (A, P, D, etc.) - not translation guidance

**Solution**: Generate translation commentary for every verse

**Example - For each annotated verse, create:**

```markdown
## John 3:16 - Translation Commentary

### Source Text
**Greek**: οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον...
**English (ESV)**: For God so loved the world that he gave his only Son...

### Critical Translation Decisions

#### 1. **Clusivity** (if your language has it)
**Not applicable** - No "we/us" in this verse
- Skip to next verse

#### 2. **Honorifics** (Japanese, Korean, Javanese, Thai, etc.)
**CRITICAL DECISION NEEDED**:

**Speaker**: Narrator (John) - describing God's action
**Listener**: Generic reader (teaching context)
**Attitude**: **Honorable** (speaking about God with highest respect)

**Your translation**:
- **Japanese**: Use most respectful forms for God
  - God: 神様 (kami-sama, honorific suffix)
  - Gave: お与えになった (o-atae-ni-natta, honorific verb form)
  - Son: 御子 (miko, honorific prefix)

- **Korean**: Use 존댓말 (jondaemal, respectful form)
  - God: 하나님 (Hananim, respectful title)
  - Loved: 사랑하셨다 (sarang-hasyeoss-da, honorific past)
  - Gave: 주셨다 (ju-syeoss-da, honorific)

- **Javanese**: Use **Krama Inggil** (highest register)
  - For God's actions, highest respect required
  - Narrator speaking formally about divine action

**How other similar languages handled it**:
- 95% of honorific languages use HIGHEST respect level
- This is theological statement about God's love
- Wrong register = inappropriate / offensive

#### 3. **Topic NP** (Japanese, Korean, Mandarin, etc.)
**DECISION NEEDED**:

**Question**: Is "God" the topic or just subject?

**Japanese translators**:
- 65% use: "神は" (Kami-WA, TOPIC particle)
  - Why: "God" is given information, topic of discourse
  - Natural Japanese prefers topic-comment structure

- 35% use: "神が" (Kami-GA, SUBJECT particle)
  - Why: Emphasis on God (not anyone else) as actor
  - Contrastive focus

**Recommendation**: Use **WA** (topic) - 65% consensus
- This is explaining God's character (topic), not contrasting
- Unless you want emphasis ("It was GOD who loved...")

#### 4. **Semantic Role** (Ergative languages)
**DECISION NEEDED**:

**Roles identified**:
- "θεός" (God) = **Agent** (doer of loving/giving)
- "κόσμον" (world) = **Patient** (object of love)
- "υἱόν" (Son) = **Theme** (what was given)

**If your language is ergative** (Basque, Georgian, K'iche', Dyirbal, etc.):
- "God" → Use **ergative case** (doer of transitive verb)
- "world" → Use **absolutive case** (object)
- "Son" → Use **absolutive case** (given object)

**Examples**:
- **Basque**: "Jainkoak mundua hainbeste maite izan zuen..."
  - Jainko-ak (God-ERGATIVE)
  - mundua (world-ABSOLUTIVE)

- **Georgian**: (split ergative, past tense uses ergative)
  - Past tense "loved" → ergative on God
  - "world" → dative case (Georgian is unusual)

**How to check**: Look at other Basque/Georgian Bible verses for pattern

#### 5. **Time Granularity** (Languages with multiple past tenses)
**DECISION NEEDED**:

**Greek**: ἠγάπησεν (aorist - simple past, no distance marking)

**If your language marks temporal distance**:
- **Yagua** (Peru): Has 5 past tenses (immediate → ancient)
- **ChiBemba** (Zambia): Has 4 past tenses
- **Others**: Check if your language needs this

**Question**: How far in the past is God's love?

**Translation consensus** (languages with distance marking):
- 70% use **TIMELESS/GNOMIC** (eternal, no specific time)
  - Why: God's love is eternal, ongoing
  - Not a one-time past event

- 20% use **ANCIENT PAST** (mythic time, primordial)
  - Why: Before creation, eternal plan

- 10% use **HISTORIC PAST** (narrative past)
  - Why: Aorist = past in Greek

**Recommendation**: **TIMELESS** (70% consensus)
- This is theological truth, not historical narrative
- God's love is eternal, not time-bound
- Most languages with distance-marking treat this as timeless principle

---

### Translation Checklist for This Verse

**Required decisions for your language**:
- [ ] Honorifics: Use highest respect for God's actions
- [ ] Topic marking: "God" as topic (WA in Japanese) vs subject
- [ ] Ergative case: Mark God as ergative agent (if applicable)
- [ ] Time distance: Use timeless/gnomic (if applicable)
- [ ] Foreground/background: This is Primary teaching (mainline)

**Common mistakes to avoid**:
- ❌ Using low/medium honorific for God (inappropriate)
- ❌ Using time-specific past when language allows timeless
- ❌ Copying English structure without considering target language needs

**Similar verses to check for consistency**:
- John 3:17 (God sent Son - same pattern)
- 1 John 4:9-10 (God's love shown - similar structure)
- Romans 5:8 (God loved us while sinners - compare tense usage)
```

**Action Items**:
- [ ] Generate translation commentary for top 500 verses (most translated)
- [ ] Focus on verses with translation challenges
- [ ] Prioritize: Gospels, Romans, Genesis, Psalms
- [ ] Include language-specific guidance
- [ ] Show similar-language examples

**Estimated Effort**: 15-20 minutes per verse × 500 = 125-167 hours
**Impact**: Translators have verse-specific guidance (not just abstract features)

---

### 7. **Book-Level Translation Guides** ⭐⭐⭐

**Problem**: Features documented generically, not by Biblical book

**Solution**: Create translation guides for major books

**Example - Create: `TRANSLATION-GUIDES/MARK.md`**

```markdown
# Translation Guide: Gospel of Mark

## Overview for Translators

**Genre**: Narrative (fast-paced action)
**Special challenges**:
- Repetitive "immediately" (εὐθύς) 42 times
- Present tense for vividness (historic present)
- Short, simple sentences
- Minimal dialogue markers

### Key Features for Your Language

**If your language has...**

**Salience marking (Bantu, etc.)**:
- Mark is FAST-PACED - lots of foreground (-ka- in Swahili)
- "Immediately" sequences are all Primary salience
- Less background than Matthew/Luke
- Keep the urgency in your verb forms

**Honorifics (Japanese, Korean, etc.)**:
- Jesus speaking: Use respectful forms (teacher authority)
- Disciples to Jesus: Use highest respect (master-disciple)
- Narrator: Neutral-formal register
- Mark is LEAST formal of Gospels - don't over-formalize

**Topic marking (Japanese, Korean, etc.)**:
- Jesus is topic throughout (use WA/eun consistently)
- Rapid topic shifts (Mark's style)
- Less topic continuity than John

### Chapter-by-Chapter Notes

**Mark 1**: Rapid-fire introduction
- Verse 1: Ancient book title style (formal)
- Verses 2-8: Background (John the Baptist) - use background forms
- Verse 9: PIVOT - Jesus appears (Primary salience, scene shift)
- Verses 10-13: Three rapid events (baptism, temptation, arrest) - keep foreground
- Verse 14-15: PIVOT - Jesus' ministry begins
- Verses 16-20: First disciples - all Primary foreground

**Common mistake**: Using background forms for the rapid action sequence (9-13)
- These are all main storyline, even though fast
- Keep foreground/Primary salience throughout

**Mark 4**: Parables
- Shift to Teaching genre (verses 2-34)
- Still Narrative frame (verses 1, 35-41)
- Don't use pure narrative forms for teaching sections
- Parables: Some languages use special "story-within-story" marking

**Mark 16**: Resurrection
- Verse 6: Angel's speech - use Imperative forms clearly
- Verse 8: Abrupt ending - preserve the terseness
- Verses 9-20: Different style (likely later addition) - smoother, more formal

### Consistent Patterns in Mark

**"Immediately" (εὐθύς)**:
- Appears 42 times (more than all other Gospels combined)
- If your language can't repeat same word 42 times naturally:
  - Alternate: "at once", "right away", "without delay"
  - Or: Use foreground verb forms that imply immediacy
  - Or: Reduce frequency slightly (30-35 times) but keep PACE

**Historic Present** (Greek present tense in past narrative):
- Mark uses 151 times (vividness technique)
- Most languages: Translate as past (don't copy Greek present)
- Exception: If your language uses historic present for drama (some do)

**Parataxis** ("and...and...and..."):
- Mark uses καὶ (and) constantly (1,331 times in 16 chapters!)
- Greek style: acceptable
- Many languages: Needs variation
  - Use subordinate clauses where appropriate
  - Use temporal markers ("then", "after", "while")
  - Don't chain 10 "ands" if unnatural in your language

### Translation Examples (Mark 1:21-28)

[Complete worked example showing how all features apply to one passage]

### Language-Specific Notes

**For Bantu translators**:
- Use -ka- extensively (foreground action)
- Reserve -ki- for rare background clauses
- Mark's pace matches natural Swahili narrative style

**For honorific-language translators**:
- Jesus: Medium-high register (teacher, not deity emphasized)
- Miracles: Show respect but not over-the-top
- Mark is earthiest Gospel - matches everyday respect level

**For topic-prominent translators**:
- Maintain Jesus as continuous topic (don't shift unnecessarily)
- Rapid scene changes - allow topic shifts with location changes
- Less complex discourse structure than John

```

**Action Items**:
- [ ] Create translation guides for 20 major books
  - Gospels (4) - Different styles
  - Pauline Epistles (7 major ones)
  - Genesis, Exodus
  - Psalms
  - Revelation
  - Other high-priority books
- [ ] Focus on book-specific challenges
- [ ] Include language-family-specific notes
- [ ] Show how features manifest in that book

**Estimated Effort**: 10-15 hours per book × 20 = 200-300 hours
**Impact**: Translators understand book-level patterns, not just verse-level

---

## Implementation Roadmap (Translator-Focused)

### Phase 1: Quick Wins (Weeks 1-2)
**Goal**: Help translators identify what matters for THEIR language

1. ✅ Language-Specific Feature Relevance Checker (40-60 hours)
2. ✅ Translation Problem Statements (reframe all 22 READMEs) (66-88 hours)

**Deliverable**: Translators quickly identify relevant features (80% time savings)

### Phase 2: Decision Support (Weeks 3-6)
**Goal**: Help translators see how other languages solved problems

3. ✅ Cross-Linguistic Pattern Visualizations (176-264 hours)
4. ✅ "Languages Like Yours" Recommendations (60-80 hours)

**Deliverable**: Translators see patterns and examples from similar languages

### Phase 3: Error Prevention (Weeks 7-10)
**Goal**: Help translators avoid common mistakes

5. ✅ Common Translation Mistakes (132-220 hours)
6. ✅ Verse-Level Translation Commentary (125-167 hours)

**Deliverable**: Practical guidance preventing translation errors

### Phase 4: Scale Up (Weeks 11-16)
**Goal**: Comprehensive coverage of major books

7. ✅ Book-Level Translation Guides (200-300 hours)

**Deliverable**: Complete translation support for 20 major books

---

## Total Estimated Effort

**Phase 1**: 106-148 hours
**Phase 2**: 236-344 hours
**Phase 3**: 257-387 hours
**Phase 4**: 200-300 hours

**Total**: 799-1,179 hours (20-30 weeks with parallel work)

---

## Success Metrics (Translator-Focused)

### Usability
- Time to identify relevant features: <5 minutes (vs. 2+ hours reading all 59)
- Time to make decision on ambiguous verse: <10 minutes (vs. days of research)
- Confidence in translation decision: 85%+ (with cross-linguistic evidence)

### Adoption
- % of translators who find it helpful: 90%+
- % who check TBTA before finalizing: 70%+
- % who recommend to other translators: 85%+

### Quality
- Reduction in clusivity errors: 80%+
- Reduction in honorific errors: 75%+
- Reduction in foreground/background errors: 70%+
- Overall translation consistency improvement: 60%+

### Coverage
- 500+ key verses with translation commentary
- 20+ major books with translation guides
- 30+ language families with tailored guidance
- 100+ common translation mistakes documented

---

## Key Insight

**The documentation should answer**:
1. ❓ "Does MY language need this feature?" (5 minutes to answer)
2. ❓ "How did languages LIKE MINE handle this verse?" (Pattern at a glance)
3. ❓ "What are common MISTAKES to avoid?" (Error prevention)
4. ❓ "What's the RIGHT DECISION for this specific verse?" (Practical guidance)

**NOT**:
- ❌ "Here's a linguistic theory explanation" (translators don't care)
- ❌ "Here's how to annotate this feature" (not their job)
- ❌ "Here's all 900 translations" (overwhelming)
- ❌ "Figure it out yourself" (defeats the purpose)

**Ultimate Goal**: Enable translators to produce **accurate, natural, culturally appropriate** translations by learning from how 900+ other languages solved the same problems.
