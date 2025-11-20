# Hierarchical Prediction Prompt Template

Complete 5-level prompt template for predicting time granularity in Bible translation. Use levels sequentially from top to bottom.

---

## Level 1 - Identify Genre (CRITICAL for time)

**Prompt**: "What genre is this passage?"

### Genre → Time Baseline Rules

**Narrative (OT Historical, Gospels, Acts)**:
- **Expect Historic Past dominance (60-70%)**
- Main storyline events → Historic Past
- Background description → Present or Timeless
- Dialogue → varies (see Level 5)

**Teaching (Epistles, Wisdom, Parables)**:
- **Expect Present/Discourse dominance (50-60%)**
- General truths → Timeless
- Application to audience → Discourse or Present
- Examples from past → Historic Past (10-15%)

**Prophecy (OT Prophets, Revelation)**:
- **Expect Future dominance (60%+)**
- Eschatological → Remote Future (40-50%)
- Near fulfillment → Near Future (20-25%)
- Past events referenced → Historic Past (10-15%)
- Prophetic perfect → Prophetic Perfect (10-15%)

**Law (Pentateuch Legal Material)**:
- **Expect Timeless dominance (50-60%)**
- Perpetual statutes → Timeless
- Consequences → Future (25-30%)
- Current instruction → Present (10-15%)

### Examples

**Genesis 1:1-5** → Narrative → Expect 70%+ Historic Past
**Matthew 5:3-10** → Teaching (direct speech) → Expect Present/Timeless
**Revelation 21:1-4** → Prophecy → Expect Remote Future dominant
**Leviticus 19:1-18** → Law → Expect Timeless dominant

---

## Level 2 - Check Explicit Temporal Markers

**Prompt**: "Are there explicit time words or phrases?"

### Past Time Markers

**Ancient Past Indicators**:
- "in the beginning" (Genesis 1:1)
- "long ago" (Hebrews 1:1)
- "in ancient times"
- "before the foundation of the world"
→ **Predict: Ancient Past or Remote Past**

**Recent Past Indicators**:
- "yesterday" (Genesis 19:34)
- "recently" (Acts 18:2)
- "a few days ago"
- "earlier today"
→ **Predict: Recent Past or Immediate Past**

**Immediate Past (Hodiernal)**:
- "earlier today"
- "this morning"
- "a few hours ago"
→ **Predict: Immediate Past** (critical for hodiernal languages)

### Present Time Markers

**Present Reference**:
- "now" (John 4:18)
- "at this time"
- "currently"
- "today" (in present sense)
→ **Predict: Present or Discourse**

**Timeless/Universal**:
- "always" (Matthew 28:20)
- "forever" (Psalm 100:5)
- "never"
- "every time"
→ **Predict: Timeless**

### Future Time Markers

**Immediate Future**:
- "tomorrow" (Matthew 6:34)
- "soon" (Revelation 1:1)
- "immediately" (Matthew 24:29)
- "about to" (Acts 21:37)
→ **Predict: Immediate Future or Near Future**

**Near Future (This Generation)**:
- "in this generation" (Matthew 24:34)
- "before you die" (Mark 9:1)
- "while I am still alive"
→ **Predict: Near Future**

**Remote Future (Eschatological)**:
- "in the last days" (Acts 2:17)
- "at the end of the age" (Matthew 28:20)
- "when Christ returns"
- "in the age to come"
→ **Predict: Remote Future or Eschatological Future**

### Narrative Frame Markers

**Temporal Deixis**:
- "at that time" (Matthew 11:25) → marks narrative time reference
- "in those days" (Luke 2:1) → sets narrative frame
- "then" (sequential) → continues narrative time
→ **Use for discourse vs narrative distinction**

### Decision Rule

**If explicit marker present**:
- Use stated timeframe (95%+ confidence)
- Override genre baseline
- Example: "long ago" + Teaching genre → Historic Past (not Timeless)

**If no marker**:
- Continue to Level 3

---

## Level 3 - Analyze Verb Form (Greek/Hebrew)

**Prompt**: "What is the source language verb form and mood?"

### Greek Verb Forms

**Aorist Indicative**:
- **Narrative context** → Historic Past (90% confidence)
- **Non-narrative** → Undefined or Timeless
- Example: ἐποίησεν (epoiēsen) "he made" in Genesis 1 → Historic Past

**Imperfect**:
- **Narrative** → Historic Past (ongoing/background)
- **Can indicate**: Remote Past, habitual past
- Example: ἐδίδασκεν (edidasken) "he was teaching" → Historic Past + Progressive

**Perfect**:
- **Recent Past with present relevance**
- Often → Perfect/Resultative
- Example: γέγραπται (gegraptai) "it is written" (perfect) → Present relevance of past writing

**Present**:
- **Narrative** → Historic Present (vivid narrative) OR Present
- **Teaching** → Present or Timeless
- **With "always", "never"** → Timeless
- Example: λέγει (legei) "he says" in narrative → can be Historic Present

**Future**:
- **Context determines remoteness**
- **Check Level 2 markers**
- **Prophecy** → Remote Future or Near Future
- Example: ἔσται (estai) "it will be" → check context for Immediate vs Remote

**Subjunctive/Optative**:
- **Modal contexts** → Often Undefined time
- **Purpose clauses** → Future oriented
- **Conditional** → Hypothetical time

### Hebrew Verb Forms

**Wayyiqtol (וַיִּקְטֹל)**:
- **Narrative mainline** → Historic Past (95% confidence)
- Sequential narrative form
- Example: וַיֹּאמֶר (wayyomer) "and he said" → Historic Past

**Qatal (קָטַל)**:
- **Completed action** → Perfect or Historic Past
- **Context determines** which
- **Prophecy** → can be Prophetic Perfect (future as completed)
- Example: בָּרָא (bara) "created" in Genesis 1:1 → Historic Past

**Yiqtol (יִקְטֹל)**:
- **Future, habitual, or modal**
- **Prophecy** → Future (check remoteness with Level 2)
- **Law** → Timeless or Future
- **Narrative** → can indicate background or habitual
- Example: יִהְיֶה (yihyeh) "it will be" → Future (check context)

**Participle**:
- **Present or progressive**
- **Can be**: Present, Timeless (gnomic), or relative time
- Example: הֹלֵךְ (holek) "going/walking" → Present or Progressive

**Imperative**:
- **Commands** → Future oriented (commanded action)
- **Law genre** → Timeless (perpetual command)

### Decision Rule

**If verb form + context clear**:
- Apply form-specific prediction (80-90% confidence)
- Example: Wayyiqtol in narrative → Historic Past

**If ambiguous**:
- Continue to Level 4 (genre-based rules)

---

## Level 4 - Apply Genre-Based Rules

**Prompt**: "Within this genre, what is the typical temporal pattern?"

### Narrative Specific Rules

**Main Storyline Verbs** (Wayyiqtol, Aorist):
- → **Historic Past** (primary narrative time)
- Example: "Jesus went to Capernaum" → Historic Past

**Background Description** (Circumstantial clauses):
- → **Timeless** or **Present**
- Example: "Capernaum was a city by the sea" → Timeless or Present (setting)

**Direct Speech - Future Reference**:
- **Immediate context** → Immediate Future
- **Distant/eschatological** → Remote Future
- Example: Jesus in narrative says "I will return" → check if immediate promise or eschatological

**Direct Speech - Past Reference**:
- **Check if recent or ancient**
- Example: "Yesterday we saw" → Recent Past
- Example: "Abraham our father" → Ancient Past

**Dialogue - Present Statements**:
- → **Present** (time of speaking within narrative)
- Example: "I am hungry" in narrative dialogue → Present (not Historic Past)

### Teaching Specific Rules

**General Truths**:
- → **Timeless**
- Example: "God is love" → Timeless
- Example: "The righteous will flourish" → Timeless

**Application to Audience**:
- → **Present** or **Immediate Future**
- → **Discourse** if epistolary context
- Example: "Therefore, brothers, I urge you" → Discourse/Present

**Historical Examples**:
- → **Historic Past**
- Example: "Abraham believed God" (cited in teaching) → Historic Past
- Proportion: 10-15% of teaching content

**Future Application**:
- → **Immediate Future** or **Near Future**
- Example: "You will face trials" → Near Future (reader's lifetime)

### Prophecy Specific Rules

**Near Fulfillment** (within generation):
- → **Near Future**
- Example: "This generation will not pass away" (Matthew 24:34) → Near Future
- Timeframe: Within reader's/hearer's lifetime

**Eschatological Fulfillment**:
- → **Remote Future** or **Eschatological Future**
- Example: "New heaven and new earth" (Revelation 21) → Eschatological Future
- Timeframe: End times, beyond normal experience

**Prophetic Perfect** (Hebrew Qatal, Greek Perfect):
- → **Prophetic Perfect**
- Future event treated as already completed (certainty)
- Example: Isaiah 53 "he was pierced" (prophetic) → Prophetic Perfect
- Translation note: Some languages mark this differently than simple future

**Historical Retrospective**:
- → **Historic Past**
- Example: Prophet recounts past events as basis for prophecy
- Proportion: 10-15% of prophetic content

### Law Specific Rules

**Perpetual Statutes**:
- → **Timeless**
- Example: "You shall not murder" → Timeless (perpetual command)
- Proportion: 50-60% of legal material

**Consequences/Blessings/Curses**:
- → **Future** (conditional or certain)
- Example: "If you obey, you will be blessed" → Future
- Proportion: 25-30% of legal material

**Current Instruction** (narrative frame of law-giving):
- → **Present**
- Example: "The LORD said to Moses" (frame) → Historic Past
- Example: "Today I set before you" → Present (rhetoric)

---

## Level 5 - Check Discourse Frame

**Prompt**: "Is time relative to discourse moment or narrative moment?"

### Discourse Time (Epistolary Present)

**Definition**: Time relative to the moment of speaking/writing, not narrative time.

**Indicators**:
- First-person statements in letters
- Direct address to readers ("you")
- Performative verbs ("I write", "I urge", "I command")

**Examples**:
- "I am writing to you" (1 John 2:1) → **Discourse** (time of writing, not past)
- "I urge you, brothers" (Romans 12:1) → **Discourse/Present**
- "I thank God" (Philippians 1:3) → **Discourse** (now, as I write)

**Translation**: Languages with epistolary present must mark this differently from narrative past or general present.

### Narrative Time

**Definition**: Time relative to the events in the story, not the telling.

**Indicators**:
- Third-person narrative
- Sequential events
- Narrative frame ("he said", "they went")

**Examples**:
- "Jesus was teaching in the synagogue" → **Historic Past** (narrative time)
- "The disciples said to him" → **Historic Past**
- "They went to Capernaum" → **Historic Past**

**Translation**: Standard narrative past tense (or appropriate remoteness level).

### Mixed Discourse/Narrative

**Direct Speech within Narrative**:
- **Frame** → Narrative Time (Historic Past)
- **Content of speech** → Present time (relative to speaker within story)

**Example**:
- Frame: "Jesus said" → **Historic Past** (narrative frame)
- Content: "'I am the bread of life'" → **Present** (Jesus' present, not narrator's past)
- Content: "'Before Abraham was, I am'" → **Timeless** (eternal present)

**Embedded Teaching in Narrative**:
- Narrative introduces: Historic Past
- Teaching content: Timeless or Present
- Example: Sermon on Mount (Matthew 5-7)
  - "Jesus taught them saying" → Historic Past (frame)
  - "Blessed are the poor in spirit" → Timeless (universal truth)

### Decision Rule

**Epistolary/Letter Genre**:
- First-person statements → **Discourse** (unless clearly past narrative)
- Commands to readers → **Immediate Future** or **Timeless**
- Example: Romans, 1 Corinthians → Heavy Discourse time

**Narrative Genre**:
- Third-person → **Historic Past** (appropriate remoteness level)
- Direct speech → **Present** (within narrative frame)

**Prophetic Oracle**:
- Oracle frame ("The word of the LORD came") → Historic Past
- Oracle content ("Thus says the LORD") → varies by content (Future, Timeless, etc.)

---

## Integration Example: Mark 1:21-28

Demonstrating all 5 levels on one passage.

### Verse 1:21: "They went into Capernaum"

**Level 1**: Genre = Narrative → Expect Historic Past
**Level 2**: No explicit temporal marker → Continue
**Level 3**: Greek verb = Aorist (eisporeuontai historical present or eisēlthon aorist) → Historic Past
**Level 4**: Main storyline verb in narrative → Historic Past
**Level 5**: Narrative time (not discourse) → Historic Past

**Prediction**: **Historic Past**
**Confidence**: 95%

### Verse 1:22: "They were astonished at his teaching"

**Level 1**: Narrative → Historic Past expected
**Level 2**: No marker → Continue
**Level 3**: Imperfect (exeplēssonto) → Historic Past + Progressive
**Level 4**: Background reaction in narrative → Historic Past
**Level 5**: Narrative time → Historic Past

**Prediction**: **Historic Past** (with progressive aspect if language marks it)
**Confidence**: 90%

### Verse 1:24: "What have you to do with us, Jesus of Nazareth?"

**Level 1**: Narrative genre, but direct speech → Check speech content
**Level 2**: No temporal marker → Continue
**Level 3**: Present tense in Greek → Present (within narrative)
**Level 4**: Direct speech in narrative → Present (speaker's present)
**Level 5**: Speech content = Present (not discourse, not narrative frame)

**Prediction**: **Present** (within the narrative frame, demon speaking)
**Confidence**: 85%

### Verse 1:27: "He has authority over unclean spirits"

**Level 1**: Narrative, but reaction/commentary → Check content
**Level 2**: No explicit marker → Continue
**Level 3**: Present tense → Present or Timeless
**Level 4**: Commentary/conclusion → Present or Timeless
**Level 5**: Crowd's realization at that moment → Present (within narrative)

**Prediction**: **Present** (within narrative context, could be **Timeless** if seen as universal truth)
**Confidence**: 80% Present, 20% Timeless

### Verse 1:28: "Immediately his fame spread"

**Level 1**: Narrative → Historic Past
**Level 2**: "Immediately" (euthys) → Immediate Past or Historic Past (immediate within story)
**Level 3**: Aorist (exēlthen) → Historic Past
**Level 4**: Main storyline consequence → Historic Past
**Level 5**: Narrative time, immediate consequence → Historic Past

**Prediction**: **Historic Past** (immediate within narrative flow)
**Note**: "Immediately" here means immediate within the story sequence, not hodiernal
**Confidence**: 95%

---

## Prompt Template Summary

Use this decision tree sequentially:

```
1. Genre? → Set baseline distribution
   ↓
2. Explicit time marker? → If YES, use it (95% confidence)
   ↓ (if NO)
3. Verb form + mood? → Apply Greek/Hebrew rules
   ↓ (if ambiguous)
4. Genre-specific rules? → Apply narrative/teaching/prophecy patterns
   ↓ (if still unclear)
5. Discourse vs narrative? → Check time reference point
```

**Final Check**: Does prediction match genre baseline distribution? If significantly different, review decision path.

---

*This template provides systematic prompts for LLM-based time granularity prediction in TBTA translations.*
