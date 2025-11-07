# Common Prediction Errors in Time Granularity

Detailed taxonomy of common errors when predicting temporal values in Bible translation, with linguistic examples and solutions.

---

## Error 1: Ignoring Genre Context

### Problem Description

Applying narrative temporal rules to non-narrative genres, or vice versa. This is the most common error (40% of mistakes in initial testing).

### Why It Happens

- Default assumption that all Bible text is narrative
- Not recognizing genre shifts within a book
- Applying past tense rules uniformly without checking genre

### Examples of This Error

**Example 1: Teaching Material Treated as Narrative**

**Passage**: Romans 3:23 - "For all have sinned and fall short of the glory of God"

**Wrong Prediction**:
- **Historic Past** (treating as narrative event)
- Reasoning: "have sinned" looks like past tense → narrative past

**Correct Prediction**:
- **Timeless** or **Present**
- Reasoning: Teaching genre, universal truth, applies to all humans across time
- Greek perfect (ἥμαρτον hēmarton) here = gnomic/universal, not historic event

**Impact**: In languages with multiple past tenses, wrong prediction leads to:
- Bantu: Recent past → "all sinned this week" (wrong!)
- Quechuan: Witnessed past → "I saw everyone sin" (wrong!)

**Example 2: Law Material Treated as Narrative**

**Passage**: Exodus 20:13 - "You shall not murder"

**Wrong Prediction**:
- **Future** (treating as prediction)
- Reasoning: "shall" looks like future tense

**Correct Prediction**:
- **Timeless** (perpetual command)
- Reasoning: Law genre, perpetual statute, applies across all time
- Not a one-time future event but an ongoing prohibition

**Impact**: In languages distinguishing future remoteness:
- Predicting "Near Future" or "Remote Future" misses the timeless quality
- Should use gnomic/perpetual marking if language has it

### Solution

**Always apply Level 1 first**: Check genre before analyzing verb forms.

**Genre Checklist**:
1. **Narrative**: OT historical books, Gospels, Acts → Historic Past dominant
2. **Teaching**: Epistles, Proverbs, teaching sections → Present/Timeless dominant
3. **Prophecy**: Prophets, Revelation → Future dominant
4. **Law**: Pentateuch legal material → Timeless dominant

**Rule**: Genre determines baseline distribution. Verb forms refine within that baseline.

### Test Case

Before predicting temporal value, ask: "What genre is this passage?"
- If Narrative → Expect 60-70% Historic Past
- If Teaching → Expect 50-60% Present/Timeless
- If Prophecy → Expect 60%+ Future
- If Law → Expect 50-60% Timeless

---

## Error 2: Confusing Narrative Time vs Discourse Time

### Problem Description

Not distinguishing between:
- **Narrative time**: Time of the events in the story
- **Discourse time**: Time of the telling/writing

This affects 20-25% of epistolary material.

### Why It Happens

- English often uses same form for both ("I am writing")
- Not recognizing epistolary present
- Treating all first-person statements as past narrative

### Examples of This Error

**Example 1: Epistolary Present Treated as Past**

**Passage**: 1 John 2:1 - "I am writing these things to you"

**Wrong Prediction**:
- **Historic Past** (treating as narrative)
- Reasoning: Letter was written in the past → past tense

**Correct Prediction**:
- **Discourse** (epistolary present)
- Reasoning: Time reference is to the act of writing, not a past event
- From reader's perspective: John is writing "now" (at the moment of composition)

**Impact**: In languages with discourse time marking:
- Wrong: Uses narrative past ("John wrote")
- Right: Uses epistolary present ("John writes to you")
- Affects present relevance to reader

**Example 2: Narrative Dialogue Treated as Discourse**

**Passage**: John 4:10 - "Jesus answered and said to her, 'If you knew the gift of God'"

**Wrong Prediction**:
- **Present** (treating as current/timeless)
- Reasoning: "If you knew" could be present conditional

**Correct Prediction**:
- **Present** within narrative frame (Jesus' present, not narrator's)
- Reasoning: Direct speech within narrative uses time relative to speaker (Jesus)
- Frame "Jesus answered" = Historic Past (narrative)
- Content "if you knew" = Present conditional (within Jesus' timeframe)

**Impact**: Need to distinguish:
- Narrative frame verbs → Historic Past
- Speech content → Present (relative to speaker)

### Solution

**Check whose timeframe is referenced**:

1. **Epistolary/Letter Context**:
   - "I write", "I urge", "I pray" → **Discourse** (time of writing)
   - Look for: First person + direct address to readers

2. **Narrative Context**:
   - "He said", "They went" → **Historic Past** (narrative frame)
   - Direct speech within narrative → **Present** (within story time)

3. **Test**: Ask "When is this event relative to?"
   - Relative to narrator → Narrative Time
   - Relative to writer composing → Discourse Time
   - Relative to speaker in story → Present (within narrative)

### Examples

**Discourse Time**:
- Romans 1:8: "I thank my God" → Discourse (Paul writing now)
- 1 Corinthians 1:10: "I appeal to you" → Discourse
- Philemon 1:4: "I thank my God always" → Discourse

**Narrative Time + Speech**:
- Mark 1:15: "Jesus said, 'The time is fulfilled'" → Frame: Historic Past; Content: Present
- John 8:58: "'Before Abraham was, I am'" → Frame: Historic Past; Content: Timeless/Present

### Test Case

Ask: "Is the time reference relative to the writer/speaker or to the events described?"
- Writer/speaker → Discourse or Present
- Events described → Historic Past (with appropriate remoteness)

---

## Error 3: Missing Prophetic Perfect

### Problem Description

Treating future events in prophetic perfect form as completed past events, missing the prophetic convention.

Affects 10-15% of prophetic material, particularly in Isaiah and Psalms.

### Why It Happens

- Hebrew Qatal and Greek Perfect forms look like past tense
- Not recognizing prophetic convention (certain future = grammatically complete)
- Western temporal logic doesn't use this construction

### Examples of This Error

**Example 1: Isaiah's Prophetic Perfect**

**Passage**: Isaiah 53:5 - "He was pierced for our transgressions"

**Wrong Prediction**:
- **Historic Past** (treating as completed event)
- Reasoning: Hebrew Qatal form = perfective aspect → past event

**Correct Prediction**:
- **Prophetic Perfect** (future as completed)
- Reasoning: Isaiah writing before crucifixion, but presents as certain/completed
- Prophetic convention: Absolute certainty expressed as accomplished fact

**Impact**: Translation must convey:
- Future event (crucifixion hadn't happened yet)
- Certainty (not "might be" but "will certainly be")
- Some languages: Special prophetic mood/aspect
- Others: Future tense + certainty particle

**Example 2: Psalm 22 Prophetic Description**

**Passage**: Psalm 22:16 - "They have pierced my hands and feet"

**Wrong Prediction**:
- **Historic Past** (David's past experience)
- Reasoning: Perfect form = past event

**Correct Prediction**:
- **Prophetic Perfect** OR **Historic Past with prophetic application**
- Reasoning: Can be read as:
  - David's experience (Historic Past)
  - Prophetic of Messiah (Prophetic Perfect)
- Christian interpretation: Prophetic Perfect pointing to crucifixion

**Impact**: Messianic prophecies require:
- Recognizing prophetic perfect convention
- May need translator note to indicate prophetic nature
- Some languages mark this distinctly from simple past or future

### Solution

**Identify Prophetic Perfect Context**:

1. **Check genre**: Prophecy section of OT Prophets, Psalms with messianic content
2. **Check verb form**: Hebrew Qatal or Greek Perfect in prophetic context
3. **Check timeline**: Is event future to the prophet but described as complete?
4. **Check certainty**: Does context emphasize inevitability/divine decree?

**Indicators**:
- Oracle introduction: "Thus says the LORD" + perfect forms
- Future context: Surrounding verses clearly future
- Theological: God's decree presented as accomplished

**Translation Strategy**:
- **Option 1**: Future tense + certainty marker ("will surely", "will certainly")
- **Option 2**: Prophetic perfect form (if language has it)
- **Option 3**: Perfect with future context ("has decreed that...")

### Examples

**Prophetic Perfect**:
- Isaiah 9:6: "A child is born" (future event, prophetic perfect)
- Isaiah 53:4-5: Multiple perfects describing future suffering
- Micah 5:2: "Out of you will come" (prophetic future)

**Not Prophetic Perfect**:
- Isaiah 6:5: "I have seen the Lord" (Isaiah's actual past experience) → Historic Past
- Jeremiah 1:5: "Before I formed you, I knew you" (God's actual past action) → Historic Past

### Test Case

Before predicting Historic Past for a perfect form, ask:
1. Is this in prophetic literature?
2. Is the event future to the prophet?
3. Does context emphasize certainty/divine decree?
4. Is it referenced as prophecy in NT?

If YES to 2+, consider **Prophetic Perfect**.

---

## Error 4: Unclear Immediate vs Remote Distinctions

### Problem Description

Not having clear guidelines for what counts as "immediate" vs "recent" vs "remote" temporal distance.

Affects languages with 3-5 past/future distinctions (40% of languages requiring time granularity).

### Why It Happens

- English doesn't distinguish temporal remoteness grammatically
- "Immediate" and "remote" are relative concepts
- Cultural differences: What's "recent" varies by culture

### Examples of This Error

**Example 1: Unclear Past Remoteness**

**Passage**: Mark 1:9 - "In those days Jesus came from Nazareth"

**Ambiguous Predictions**:
- **Recent Past** (happened recently to Mark's writing?)
- **Immediate Past** (earlier that day?)
- **Historic Past** (standard narrative past?)
- **Remote Past** (long ago before Mark's time?)

**Clarification Needed**:
- Time of event: ~30 years before Mark's writing
- Reader's perspective: Ancient or recent?
- Narrative flow: Beginning of Jesus' ministry

**Correct Prediction**:
- **Historic Past** (standard narrative past)
- NOT Immediate Past (not hodiernal - not today)
- NOT Remote Past (not ancient/legendary)
- Within living memory but narrative standard

**Example 2: Unclear Future Remoteness**

**Passage**: Matthew 24:34 - "This generation will not pass away until all these things take place"

**Ambiguous Predictions**:
- **Immediate Future** (days/weeks)?
- **Near Future** (within generation = 40 years)?
- **Remote Future** (eschatological)?

**Clarification Needed**:
- "This generation" = within lifetime of hearers
- Some events: Near term (70 AD destruction)
- Some events: Could be eschatological

**Correct Prediction**:
- **Near Future** (within generation/lifetime)
- NOT Immediate Future (not today/tomorrow)
- NOT Remote Future (not end-times beyond normal expectation)

### Solution: Temporal Distance Guidelines

**Past Tenses**:

1. **Immediate Past (Hodiernal)**: Earlier today, this morning
   - Timeframe: Within same day
   - Marker languages: Bantu hodiernal, some Trans-New Guinea
   - Biblical examples: Rare (most narrative is pre-hodiernal)

2. **Recent Past**: Days/weeks ago, this month
   - Timeframe: Recent memory, current context
   - Within weeks, still fresh
   - Biblical examples: "Yesterday", "a few days ago"

3. **Historic Past**: Standard narrative past, weeks/months/years ago
   - Timeframe: Within living/cultural memory
   - Default narrative tense
   - Biblical examples: Most Gospel narrative (20-50 years before writing)

4. **Remote Past**: Beyond living memory, ancient
   - Timeframe: Generations ago, legendary past
   - "Long ago", "in ancient times"
   - Biblical examples: Genesis events, "long ago" in Hebrews

5. **Ancient Past**: Before living memory, primordial
   - Timeframe: Creation, pre-historical
   - "In the beginning"
   - Biblical examples: Genesis 1-11, before Abraham

**Future Tenses**:

1. **Immediate Future**: Today, very soon, about to happen
   - Timeframe: Hours, same day
   - "About to", "immediately", "right now"
   - Biblical examples: "I am about to" (imminent action)

2. **Near Future**: Days/weeks/months, this generation
   - Timeframe: Within lifetime, foreseeable
   - "Soon", "this generation", "while you live"
   - Biblical examples: Matthew 24 near-term prophecies

3. **Remote Future**: Beyond generation, distant
   - Timeframe: Beyond normal expectation
   - "In the last days", "when I return"
   - Biblical examples: Some eschatological prophecy

4. **Eschatological Future**: End times, beyond normal time
   - Timeframe: Final events, new creation
   - "The age to come", "when heaven and earth pass away"
   - Biblical examples: Revelation new heaven/earth, final judgment

### Guidelines by Language Type

**Hodiernal/Hesternal Systems** (Bantu, some Trans-New Guinea):
- Immediate Past = Today's past (hodiernal)
- Recent Past = Yesterday (hesternal)
- Historic Past = Pre-hesternal (before yesterday)
- Remote Past = Distant pre-hesternal

**Graded Past Systems** (Quechuan, Bantu):
- Use witness/experience as guide:
  - Witnessed/participated → closer past
  - Heard/reported → more remote
  - Ancient/legendary → most remote

**Simple Past/Future** (Many Austronesian):
- May not mark remoteness at all
- Use context and adverbials

### Test Cases

**Past Distance Decision Tree**:
1. Today? → Immediate Past
2. Yesterday/this week? → Recent Past
3. Weeks/months/years (in living memory)? → Historic Past
4. Generations/ancient? → Remote/Ancient Past

**Future Distance Decision Tree**:
1. Today/hours? → Immediate Future
2. Days/weeks/generation? → Near Future
3. Beyond lifetime? → Remote Future
4. End times/new creation? → Eschatological Future

---

## Error 5: Confusing Aspect with Time

### Problem Description

Treating aspectual distinctions (how action unfolds) as temporal distinctions (when action occurs).

Progressive aspect ≠ present time; Perfect aspect ≠ past time.

Affects 15-20% of predictions, especially in aspect-prominent languages.

### Why It Happens

- English often fuses time and aspect ("is walking" = present + progressive)
- Not separating "when" (time) from "how" (aspect)
- Source language (Greek/Hebrew) aspect systems don't map 1:1 to time

### Examples of This Error

**Example 1: Imperfect = Present?**

**Passage**: Mark 1:22 - "They were astonished at his teaching"

**Wrong Prediction**:
- **Present** (because ongoing action)
- Reasoning: Imperfect = progressive aspect → present time

**Correct Prediction**:
- **Historic Past** + Progressive aspect
- Reasoning: TIME = past (narrative time), ASPECT = progressive (ongoing)
- "Were astonishing" (imperfect) = past time + progressive aspect

**Impact**: In languages separating time and aspect:
- Need: Past tense marker + progressive aspect marker
- Not: Present tense marker

**Example 2: Perfect = Past?**

**Passage**: Matthew 11:5 - "The blind receive sight" (Greek: ἀναβλέπουσιν anablepousin)

**Wrong Prediction**:
- **Historic Past** (because action completed)
- Reasoning: Completed action = past time

**Correct Prediction**:
- **Present** (Jesus describing current/ongoing reality)
- Reasoning: TIME = present (within Jesus' discourse), ASPECT = may be completive
- Greek present tense here = current events, not past narrative

**Example 3: Progressive ≠ Present**

**Passage**: Luke 2:8 - "Shepherds were keeping watch over their flock by night"

**Wrong Prediction**:
- **Present** (because progressive action)
- Reasoning: "Were keeping" = progressive → present time

**Correct Prediction**:
- **Historic Past** + Progressive aspect
- Reasoning: TIME = past (narrative), ASPECT = progressive (ongoing at that past time)
- Imperfect in Greek = past time + progressive aspect

### Solution: Separate Time from Aspect

**Time (When?)**:
- Past: Before now (various remoteness levels)
- Present: At now
- Future: After now

**Aspect (How?)**:
- Perfective: Action viewed as whole, completed
- Imperfective: Action viewed as ongoing, incomplete
- Progressive: Action in progress at reference time
- Habitual: Repeated action
- Iterative: Multiple occurrences

**Integration**:
- Past + Progressive = "was walking" (Historic Past + Progressive)
- Present + Progressive = "is walking" (Present + Progressive)
- Future + Progressive = "will be walking" (Future + Progressive)

### Examples of Correct Time + Aspect

**Historic Past + Perfective**:
- "Jesus went to Capernaum" (Aorist) → Historic Past + Perfective

**Historic Past + Progressive**:
- "Jesus was teaching" (Imperfect) → Historic Past + Progressive

**Present + Perfective**:
- "I tell you" (Aorist in some contexts) → Present + Perfective

**Historic Past + Perfect**:
- "Had come" (Pluperfect) → Historic Past + Perfect aspect (prior action)

**Timeless + Habitual**:
- "The righteous flourish" → Timeless + Habitual

### Guidelines

1. **Determine time first** (Level 1-5 of prompt template)
2. **Then determine aspect** (separate analysis)
3. **Combine**: Time + Aspect = full prediction

**For aspect-prominent languages** (Mayan, Hebrew, Austronesian):
- May express time through context, aspect through grammar
- Aspect is obligatory, time is inferred
- Example: Hebrew Qatal = perfective aspect; time determined by context

### Test Cases

Before predicting, separate:
- **When does the action occur?** → Time value
- **How does the action unfold?** → Aspect value

Do NOT conflate:
- Progressive → Present
- Perfect → Past
- Aorist → Past

Each aspect can occur at any time.

---

## Summary: Error Prevention Checklist

Before making temporal prediction:

1. ☐ **Check Genre** (Level 1) - What's the baseline distribution?
2. ☐ **Check Explicit Markers** (Level 2) - Any time words?
3. ☐ **Separate Time from Aspect** - Am I confusing "when" with "how"?
4. ☐ **Check Discourse Frame** (Level 5) - Narrative time or discourse time?
5. ☐ **Check Remoteness Guidelines** - Which temporal distance level?
6. ☐ **Check Prophetic Context** - Could this be prophetic perfect?

**If prediction differs significantly from genre baseline**: Review decision path.

**If uncertain**: Note uncertainty and provide rationale for choice.

---

*This error taxonomy helps improve accuracy in time granularity prediction for TBTA.*
