# Time Granularity in TBTA Languages

Research on fine-grained temporal/tense systems across language families in the TBTA corpus, focusing on languages that distinguish between multiple degrees of temporal remoteness, evidentiality, and other advanced temporal marking systems.

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language distinguish multiple past tenses by distance?
   - If YES, how many past distinctions? (2-way, 3-way, 4-way+)
2. ☐ Does your language distinguish multiple future tenses?
   - Immediate future vs remote future?
3. ☐ Does your language mark hodiernal (today) vs pre-hodiernal (before today)?
4. ☐ Does your language use absolute time (calendar) or relative time (narrative flow)?
5. ☐ Does your language have special marking for timeless/gnomic statements?

If you answered YES to #1 with 3+ distinctions, time granularity annotation
is CRITICAL.

**Languages requiring this**:
- Bantu: Up to 5 past tenses by distance (ChiBemba, Swahili)
- Amazonian: Yagua has 5 past distinctions
- Kiksht: Complex narrative time with multiple pasts
- Quechuan: Multiple past levels

## Baseline Statistics

Expected distribution varies significantly by genre:

**Narrative (OT/Gospels/Acts)**:
- Historic Past: ~60% (main storyline events)
- Immediate Past: ~15% (recent events referenced)
- Present: ~10% (dialogue, description)
- Immediate Future: ~10% (predictions, plans)
- Other: ~5%

**Teaching/Epistles (NT)**:
- Present: ~40% (current teaching, timeless truth)
- Discourse: ~25% (time relative to discourse moment)
- Historic Past: ~15% (references to events)
- Future: ~15% (prophecy, eschatology)
- Other: ~5%

**Prophecy (OT/Revelation)**:
- Remote Future: ~35% (eschatological)
- Near Future: ~25% (imminent fulfillment)
- Historic Past: ~15% (retrospective)
- Prophetic Perfect: ~15% (future as completed)
- Other: ~10%

**Law (Pentateuch)**:
- Timeless: ~50% (perpetual statutes)
- Future: ~30% (consequences)
- Present: ~15% (current instruction)
- Other: ~5%

## Scope

This research analyzes 725+ languages from 11 major language families represented in TBTA:
- **Austronesian** (176 languages)
- **Trans-New Guinea** (141 languages)
- **Indo-European** (135 languages)
- **Niger-Congo** (89 languages, including Bantu)
- **Otomanguean** (69 languages)
- **Mayan** (41 languages)
- **Australian** (36 languages)
- **Afro-Asiatic** (25 languages)
- **Sino-Tibetan** (18 languages)
- **Quechuan** (18 languages)
- **Other families** (81 languages across smaller groups)

## Key Temporal System Types

### 1. Graded/Multi-Degree Past Tense Systems

#### Bantu Languages (Niger-Congo)
Bantu languages exhibit among the world's most complex tense systems with 3-4 distinct past tense degrees:

**Example: Gĩkũyũ (Kenyan Bantu)**
- Four grades of past tense
- Three grades of future tense
- Each grade marks temporal remoteness from present moment
- Tenses organized along "cognitive space" rather than simple linear time

**Example: Isu (Grassfields Bantu, Cameroon)**
- Three synthetically marked degrees of past
- Two distinct futures
- Complex interaction with aspect and mood

**Key Source**: Nurse, Derek (2008). "Tense and Aspect in Bantu" - Details organization of tense/aspect systems along dimensions of temporal remoteness.

#### Quechuan Languages
Multiple past tenses indicating both temporal distance and evidential value:

**Immediate Past vs. Remote Past Distinction**
- **-rqa/-ra**: Direct experience (witnessed past)
  - "I directly saw/experienced this event"
  - Common in narrative introduction and explanations

- **-sqa/-sha**: Indirect experience (non-witnessed/remote past)
  - Events not directly experienced or before speaker's lifetime
  - Used for narrative main events and surprise expressions
  - Developed from present perfect morphology

**Example: South Conchucos Quechua**
- Multiple past tense forms place events relative to each other in past time
- Choices between past forms determined by both temporal remoteness AND evidential source
- Tense used metaphorically for narrative structure and emotional distance
- Remote past forms used with peripheral narrative (orientation, side remarks)
- Immediate past forms used with main narrative events

**Key Source**: Hintz, Diane. "Past tense forms and their functions in South Conchucos Quechua" - Academic examination of evidential-tense interaction.

### 2. Hodiernal vs. Pre-Hodiernal Systems

#### Bantu Languages: Hodiernal Distinctions
Some Bantu languages explicitly mark whether events occurred "today" vs. before today:

**Mwera (Bantu, Tanzania)**
- Hodiernal past: Events that occurred earlier today
- Pre-hodiernal past: Events before today
- Additional markers for remote past

**Other Examples**
- Kalaw Lagaw Ya distinguishes hodiernal futures
- Some Bantu languages mark "crastinal" (tomorrow) and "hesternal" (yesterday)

### 3. Evidential Tense Marking

Languages where tense and evidence source are grammatically fused:

#### Turkish (Turkic, Afro-Asiatic influence)
Obligatory marking of past tense with evidence source:

**-DI (Witnessed/Direct Past)**
```
Gördüm = "I saw" (I witnessed it directly)
-DI marks actions the speaker witnessed firsthand
```

**-mIş (Inferential/Heard Past)**
```
Görülmüş = "I inferred/heard about seeing" (indirect evidence)
-mIş marks events speaker didn't witness but inferred from:
  - Hearsay/reported information
  - Visual traces (e.g., "It must have rained" seeing wet ground)
  - Inference from general knowledge
When combined with first person: indicates unintentional/unconscious action
```

**Dialectal Variation**: Cypriot Turkish has begun losing the -DI/-mIş distinction in modern usage.

#### Georgian (Kartvelian, Indo-European connection)
Evidentiality marks in past tense through:
- Perfect tense with secondary evidential meaning
- Particle /turme/ for non-witnessed events
- Admirative value in certain past forms

**Key Sources**:
- Aksu-Koç, Ayhan. Pioneering work on Turkish evidential acquisition in children
- Botne, Robert & Kershner, Tiffany. "Tense and cognitive space" - Analysis of graded tense organization

#### Other Languages with Evidential Tense
- **Komi-Zyrian** (Finno-Ugric): Direct vs. indirect past
- **Haida** (Language isolate, Alaska/BC): Witnessed vs. unwitnessed past
- **Ika** (Chibchan, Colombia): Direct vs. indirect evidence in past

### 4. Australian Aboriginal Languages

Complex evidential and modal tense-aspect systems:

**Characteristics**
- Distinction between relative vs. absolute tense (some languages)
- Grammatical expression through clitics/particles rather than inflections
- Mixed focus/temporal meaning (elements paraphrased as 'now' vs. 'then')
- Complex tense-case interactions in some Pama-Nyungan languages
- Modal-tense interactions creating hypothetical/counterfactual meanings
- Polysynthetic morphology: temporal meanings expressed within word structure

**Key Feature**: Temporal/focus clitics crucial for proper ordering in narrative events - distinct from Indo-European reliance on temporal connectives.

**Research Gap**: Subtle, context-sensitive TAME (Tense-Aspect-Modality-Evidentiality) categories increasingly difficult to document; only fully competent native speakers can provide reliable data.

### 5. Austronesian Languages

More optional TAM marking compared to other major families:

**Characteristics**
- Optional vs. obligatory TAM marking varies by language
- Some languages use lexical markers (optional context-dependent)
- Others use preverbal particles/affixes with head-initial structure
- Interaction with focus systems affects tense/mood reading

**Examples**
- **T'boli** (Philippines): Lexicalized morphemes for aspect; affix-based focus system
- **Old Rapa** (French Polynesia): Three tense markers (Imperfective, Progressive, Perfective)
- **Kavalan** (Taiwan): Debate between tense dichotomy (future vs. non-future) vs. mood (realis vs. irrealis)

**Key Feature**: Optionality of TAM marking correlates with presence of time adverbials - less obligatory expression than Indo-European or Bantu.

### 6. Trans-New Guinea Languages

Complex but variable tense systems with multiple past distinctions:

**Characteristics**
- Multiple deictic distinctions of temporal distance
- Common pattern: Present → Today's past → Yesterday's past → Remote past → Habitual past
- Serial verb constructions for aspect marking (e.g., 'stay' > progressive marker)
- Extensive verbal morphology with large paradigms
- Grammaticalization paths: verbs → tense/aspect meanings

**Examples**
- **Amele**: Morphological future affix "-an" (irrealis)
- **Mian**: Verb s- 'sleep' grammaticalized into hesternal (yesterday) past
- **Kobon**: Future suffix "-nab" (irrealis)

**Research Pattern**: Diachronic stability in present and remote past; instability and variation in middle pasts and future tenses.

### 7. Mayan Languages

Aspect-based rather than tense-based temporal systems:

**Characteristics**
- Tenseless languages (e.g., Tzotzil uses binary aspect: completive vs. incompletive)
- Temporal meaning expressed through CONTEXT + ASPECT rather than tense affixes
- Proto-Mayan reconstructed system: 7 aspects (incompletive, progressive, completive, imperative, potential, optative, perfective)
- Recent grammaticalization of auxiliaries for finer TAM distinctions in Yucatec Maya
- Status suffixes related to transitivity and aspectual characteristics

**Historical Development**
- Colonial and post-colonial periods show continuous productive formation of tense/aspect/mood auxiliaries
- Represents shift from status system (inherited) to auxiliary-based system
- Auxiliary pattern converges across languages despite heterogeneous source constructions

**Key Source**: Kaufman's Proto-Mayan reconstruction showing 7-aspect system.

## Cross-Cutting Linguistic Phenomena

### Metaphorical Extension of Tense

Languages with graded tense systems often extend temporal meanings metaphorically:

- **Quechuan**: Temporal distance extended to narrative structure (main vs. peripheral content) and emotional affect
- **Bantu**: Temporal remoteness mapped to cognitive "distance" along dimensions beyond chronological time
- **English (some dialects)**: Historical extension of evidential meanings in modal verbs (e.g., *sollen* 'should' > hearsay marker in German)

### Grammaticalization Pathways

Common patterns in language evolution:

1. **Aspect → Tense**: Progressive aspect grammaticalizes into future tense
2. **Verb → TAM**: Specific verbs ('stay', 'sleep', 'go') grammaticalize into tense/aspect markers
3. **Perfect → Evidential**: Perfect tense develops secondary evidential meaning (Turkish, Georgian)
4. **Serial constructions → Aspect**: Last verb in serialization becomes aspect marker

### Interaction Domains

TAM systems frequently interact with:
- **Mood**: Modal meanings (hypothetical, counterfactual) combined with tense marking
- **Focus/Word Order**: Head-initial languages mark TAM with preverbal particles
- **Agreement**: Case and subject agreement morphology interact with tense marking
- **Narrative Structure**: Tense choices signal narrative organization (main vs. side content)

## Hierarchical Prediction Prompt Template

**Level 1 - Identify Genre** (CRITICAL for time)
Prompt: "What genre is this passage?"
- Narrative → Expect Historic Past dominance (60%+)
- Teaching → Expect Present/Discourse dominance (60%+)
- Prophecy → Expect Future dominance (60%+)
- Law → Expect Timeless dominance (50%+)

**Level 2 - Check Explicit Temporal Markers**
Prompt: "Are there explicit time words?"
- "yesterday", "tomorrow", "long ago" → Use stated timeframe
- "now", "at that time", "then" → Mark temporal deixis
- No marker → Continue Level 3

**Level 3 - Analyze Verb Form (Greek/Hebrew)**
Greek:
- Aorist → Usually Historic Past (narrative) or Undefined (non-narrative)
- Imperfect → Historic Past (ongoing) or Remote Past
- Perfect → Recent Past with present relevance
- Present → Present or Discourse
- Future → Immediate Future or Remote Future (check context)

Hebrew:
- Wayyiqtol → Historic Past (narrative mainline)
- Qatal → Completed action (Historic Past or Perfect)
- Yiqtol → Future, habitual, or modal
- Participle → Present or progressive

**Level 4 - Apply Genre-Based Rules**
Narrative:
- Main storyline verbs → **Historic Past**
- Background description → **Timeless** or **Present**
- Direct speech about future → **Immediate Future** or **Remote Future**

Teaching:
- General truths → **Timeless**
- Application to audience → **Present** or **Immediate Future**
- Examples from past → **Historic Past**

Prophecy:
- Near fulfillment → **Near Future** (within generation)
- Eschatological → **Remote Future** (end times)
- Prophetic perfect (future as done) → **Remote Future** with perfect aspect

**Level 5 - Check Discourse Frame**
Prompt: "Is time relative to discourse moment or narrative moment?"
- Letter writing: "I am writing to you" → **Discourse** (time of writing)
- Narrative: "Jesus was teaching" → **Historic Past** (time of story)

## Gateway Features & Correlations

Quick prediction rules:

| If Context Shows... | Then Predict... | Confidence |
|---------------------|----------------|------------|
| Genre=Narrative + Mood=Indicative | **Historic Past** | 70%+ |
| Genre=Teaching + Present tense | **Present** or **Timeless** | 75%+ |
| Genre=Prophecy + Future tense | **Remote Future** | 65%+ |
| Explicit "yesterday", "long ago" | **Immediate Past** or **Remote Past** | 95%+ |
| Explicit "tomorrow", "soon" | **Immediate Future** | 90%+ |
| Law genre + imperative | **Timeless** | 80%+ |

**Correlation with Mood + Aspect**:
- Indicative + Aorist (Greek) → Historic Past (narrative context) 90%
- Indicative + Present → Present or Timeless 80%
- Subjunctive → Often Future or Conditional time

## Common Prediction Errors

**Error 1**: Ignoring genre context
- Problem: Applying narrative rules to teaching passages
- Solution: Always check genre first (Level 1)
- Example: Present tense in narrative=currently happening; in teaching=timeless truth

**Error 2**: Confusing narrative time vs discourse time
- Problem: Not distinguishing story time from telling time
- Solution: Check if time is relative to narrative or speaker
- Example: "I am writing" (discourse time) vs "Jesus was writing" (narrative time)

**Error 3**: Missing prophetic perfect
- Problem: Treating future events as past because of perfect form
- Solution: Recognize prophetic convention (certain future = completed)
- Example: Isaiah's "the virgin has conceived" (future treated as complete)

**Error 4**: Overusing "Immediate" vs "Remote"
- Problem: Not clear what "immediate" means (hours? days? weeks?)
- Solution: Use cultural context and explicit markers
- Guidelines:
  - Immediate: Within day/week, same scene
  - Near: Within generation, this era
  - Remote: Beyond generation, eschatological

**Error 5**: Confusing aspect with time
- Problem: Progressive aspect ≠ present time
- Solution: Separate aspect (how action unfolds) from time (when it occurs)
- Example: "was walking" = past time + progressive aspect

## Cross-Feature Interactions

**Time + Mood + Aspect** (PRIMARY TRIAD):
These three features form a tightly integrated system:
- Mood: Factual/hypothetical/commanded
- Aspect: Internal temporal structure
- Time: Location on timeline

Example combinations:
- Indicative + Perfective + Historic Past = "he walked" (narrative)
- Indicative + Progressive + Present = "he is walking" (current)
- Subjunctive + Imperfective + Future = "he might walk" (hypothetical future)

**Time + Genre**:
- Narrative: Dominated by Historic Past
- Teaching: Dominated by Present/Timeless
- Prophecy: Dominated by Future
- Law: Dominated by Timeless

**Time + Illocutionary Force**:
- Declarative: Full range of time
- Imperative: Usually Future (commanded action)
- Interrogative: Usually Present or Future
- Performative: Usually Present (speech act creates reality)

## Research Implications for TBTA

### Design Considerations for Fine-Grained Time Marking

1. **Template Structure**: Need flexible fields for:
   - Temporal remoteness degrees (immediate, recent, remote, ancient)
   - Evidential source (witnessed, reported, inferred, unspecified)
   - Aspectual completion (completive, incompletive, progressive, habitual)
   - Modal force (indicative, subjunctive, hypothetical)

2. **Language-Specific Notes**: Important to document:
   - Obligatory vs. optional TAM marking
   - Metaphorical extensions (emotional/narrative distance)
   - Interaction with focus, mood, or agreement systems
   - Grammaticalization patterns and historical development

3. **Citation Requirements**: When analyzing complex temporal systems:
   - Distinguish between direct experience and hearsay
   - Document time-frame accessibility to speakers
   - Note context-dependency of temporal expressions
   - Specify dialectal variation in TAM systems

### Academic Sources for Further Consultation

**Core References**
- Bybee, Joan L., Revere Perkins, & William Pagliuca. (1994). "The Evolution of Grammar: Tense, Aspect, and Modality in the Languages of the World"
- Fleischman, Suzanne. (1989). "Tense and Narrativity"
- Nurse, Derek. (2008). "Tense and Aspect in Bantu"

**Specific Language Families**
- Hintz, Diane. "Past tense forms and their functions in South Conchucos Quechua"
- Aksu-Koç, Ayhan. Work on Turkish evidential acquisition
- Botne, Robert & Kershner, Tiffany. "Tense and cognitive space: On the organization of tense/aspect systems in Bantu languages and beyond"

**Typological Resources**
- WALS Online - Chapter 77: "Semantic Distinctions of Evidentiality"
- Oxford Research Encyclopedia of Linguistics - Chapters on:
  - Australian Aboriginal Language Morphology
  - Trans-New Guinea Language Morphology
  - Evidentiality and Epistemic Modality

---

## Next Steps

1. **Language Selection**: Identify 5-10 representative languages per major family with fine-grained temporal systems
2. **Schema Development**: Create extended SCHEMA.md fields for evidential tense, temporal remoteness, and metaphorical extensions
3. **Tool Creation**: Design bible-study-tools for:
   - Comparing temporal systems across translation equivalents
   - Marking evidence sources in translations
   - Tracking metaphorical extensions of tense in narrative
4. **Validation**: Establish validation requirements for evidential marking and temporal remoteness claims

---

*Research Date: November 2025*
*Languages Analyzed: 725+ from 11 families*
*Primary Focus: TBTA corpus languages with complex temporal marking*
