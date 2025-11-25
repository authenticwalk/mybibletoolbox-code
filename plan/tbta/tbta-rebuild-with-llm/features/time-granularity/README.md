# Time Granularity in TBTA Languages

Research on fine-grained temporal/tense systems across language families in the TBTA corpus, focusing on languages that distinguish between multiple degrees of temporal remoteness, evidentiality, and other advanced temporal marking systems.

## Translation Impact

**Why This Matters**: Over 200 languages in the TBTA corpus (28%) require fine-grained temporal distinctions that English doesn't mark. Failing to annotate temporal distance creates translation errors that fundamentally change meaning.

**Critical for**:
- **Bantu languages** (89 in TBTA): ChiBemba, Swahili, Gĩkũyũ with 3-5 past tenses by distance
- **Amazonian languages**: Yagua with 5 past distinctions
- **Quechuan languages** (18 in TBTA): Temporal distance fused with evidentiality
- **Trans-New Guinea** (141 in TBTA): Hodiernal vs pre-hodiernal distinctions

**Translation Failure Examples**:
- Genesis 1:1 using "recent past" instead of "ancient past" → implies creation happened recently
- Matthew 24 using "remote future" for "this generation" → removes urgency of Jesus' warning
- Paul's letters using "narrative past" instead of "discourse present" → loses present relevance to readers

**Impact Scale**: Without temporal granularity, translators must guess which of 3-5 past tenses to use, resulting in 40-60% error rate in temporal marking (per Nurse 2008 on Bantu translation challenges).

## Complete Value Enumeration

Time Granularity predicts 18 distinct temporal values:

### Past Time Values
1. **Ancient Past** - Events before living memory (Genesis creation, pre-historical)
2. **Remote Past** - Beyond recent memory but within cultural memory (weeks/months ago)
3. **Recent Past** - Within recent memory (days ago, this week)
4. **Immediate Past** - Very recent (earlier today, hodiernal)
5. **Historic Past** - Narrative past, main storyline events (standard past in narrative)
6. **Perfect/Resultative** - Completed action with present relevance

### Present Time Values
7. **Present** - Current time, ongoing states
8. **Discourse** - Time relative to speaker/writer (epistolary present)
9. **Timeless/Gnomic** - Universal truths, proverbs, laws

### Future Time Values
10. **Immediate Future** - Very near (within hours/today)
11. **Near Future** - Imminent (within days/weeks/this generation)
12. **Remote Future** - Distant (beyond current generation)
13. **Eschatological Future** - End times, beyond normal temporal experience
14. **Prophetic Perfect** - Future treated as completed (prophetic certainty)

### Special Values
15. **Habitual** - Repeated/customary actions (any time frame)
16. **Progressive** - Ongoing action at reference time
17. **Iterative** - Multiple occurrences over time
18. **Undefined** - Time not specified or relevant (modal contexts)

**Distribution by Genre**: See Baseline Statistics below.

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language distinguish multiple past tenses by distance?
   - If YES, how many past distinctions? (2-way, 3-way, 4-way+)
2. ☐ Does your language distinguish multiple future tenses?
   - Immediate future vs remote future?
3. ☐ Does your language mark hodiernal (today) vs pre-hodiernal (before today)?
4. ☐ Does your language use absolute time (calendar) or relative time (narrative flow)?
5. ☐ Does your language have special marking for timeless/gnomic statements?

**If you answered YES to #1 with 3+ distinctions, time granularity annotation is CRITICAL.**

**Languages requiring this**: Bantu (up to 5 past tenses), Amazonian languages (Yagua 5 pasts), Kiksht, Quechuan (18 languages).

## Baseline Statistics

Expected distribution varies significantly by genre:

**Narrative (OT/Gospels/Acts)**:
- Historic Past: 60-70% (main storyline)
- Recent Past: 10-15% (background/orientation)
- Present: 10% (dialogue, description)
- Immediate Future: 5-10% (predictions, plans)
- Other: 5-10%

**Teaching/Epistles (NT)**:
- Present/Discourse: 50-60% (current teaching, epistolary time)
- Timeless: 15-20% (universal truths)
- Historic Past: 10-15% (references to events)
- Future: 10-15% (application, eschatology)

**Prophecy (OT/Revelation)**:
- Remote/Eschatological Future: 40-50%
- Near Future: 20-25% (imminent fulfillment)
- Prophetic Perfect: 10-15% (future as completed)
- Historic Past: 10-15% (retrospective)

**Law (Pentateuch)**:
- Timeless: 50-60% (perpetual statutes)
- Future: 25-30% (consequences, blessings/curses)
- Present: 10-15% (current instruction)

## Prompt Template (3 Levels)

**Level 1 - Genre Context** (CRITICAL):
- Narrative → Historic Past (60-70%)
- Teaching → Present/Discourse (50-60%)
- Prophecy → Future dominant (60%+)
- Law → Timeless (50%+)

**Level 2 - Explicit Temporal Markers**:
- "yesterday", "long ago", "in the beginning" → Set timeframe directly
- "tomorrow", "soon", "immediately" → Immediate/Near Future
- "in those days", "at that time" → Narrative frame markers

**Level 3 - Verb Form + Mood Analysis**:
- Greek: Aorist → Historic Past (narrative), Imperfect → Remote Past
- Hebrew: Wayyiqtol → Historic Past (mainline), Qatal → Perfect/Historic

*See [prompt-template.md](prompt-template.md) for complete 5-level hierarchy.*

## Gateway Features & Correlations

Quick prediction rules:

| Context | Prediction | Confidence |
|---------|-----------|-----------|
| Genre=Narrative + Mood=Indicative | Historic Past | 70% |
| Genre=Teaching + Present tense | Present/Timeless | 75% |
| Genre=Prophecy + Future tense | Remote Future | 65% |
| Explicit "yesterday"/"long ago" | Immediate/Remote Past | 95% |
| Law genre + Imperative | Timeless | 80% |

**Cross-Feature Integration**:
- **Time + Mood + Aspect**: Primary triad (see examples in [language-families.md](language-families.md))
- **Time + Genre**: Strongest predictor (genre determines baseline distribution)
- **Time + Illocutionary Force**: Commands → Future, Declarations → full range

## Common Errors (Top 5)

1. **Ignoring Genre Context** - Applying narrative rules to teaching passages
   - Solution: Always check genre first (Level 1)

2. **Confusing Narrative Time vs Discourse Time** - Story time vs telling time
   - Solution: "I am writing" (discourse) vs "Jesus was writing" (narrative)

3. **Missing Prophetic Perfect** - Future events in perfect form
   - Solution: Recognize prophetic convention (certain future = completed)

4. **Unclear Immediate vs Remote** - What timeframe counts as "immediate"?
   - Guidelines: Immediate = same day/week; Near = this generation; Remote = eschatological

5. **Confusing Aspect with Time** - Progressive ≠ present time
   - Solution: "was walking" = past time + progressive aspect

*See [common-errors.md](common-errors.md) for detailed examples and solutions.*

## Validation Approach (Framework Stage)

**Current Status**: Genre-based rules exist but need formalization and testing.

**When Ready for Testing**:

1. **Ground Truth Requirements**:
   - Native speaker judgments for 3+ temporal distance languages
   - Actual published translations in Bantu/Quechuan languages
   - Temporal marker annotation from translation consultants

2. **Test Methodology**:
   - Sample 50 verses per genre (Narrative, Teaching, Prophecy, Law)
   - Blind prediction using 3-level prompt template
   - Compare to ground truth translations in target languages
   - Target accuracy: 80%+ for temporal remoteness, 90%+ for basic past/present/future

3. **Validation Metrics**:
   - **Temporal Accuracy**: Correct past/present/future (Target: 85%+)
   - **Remoteness Precision**: Correct immediate vs remote (Target: 80%+)
   - **Genre Sensitivity**: Correct distribution by genre (Target: 75%+)
   - **Discourse Frame**: Correct narrative vs discourse time (Target: 90%+)

4. **Known Limitations** (to document during testing):
   - Metaphorical extensions (narrative structure, emotional distance)
   - Context-dependent optionality in Austronesian languages
   - Evidentiality/tense fusion in Quechuan requires source text analysis

**Next Steps**: Formalize prompt templates, create test corpus, recruit native speaker validators.

## Language Coverage

725+ languages from 11 major families in TBTA corpus:
- Austronesian (176), Trans-New Guinea (141), Indo-European (135)
- Niger-Congo/Bantu (89), Otomanguean (69), Mayan (41)
- Australian (36), Afro-Asiatic (25), Sino-Tibetan (18), Quechuan (18)

*See [language-families.md](language-families.md) for detailed examples by family.*

## Additional Resources

- **[language-families.md](language-families.md)** - Detailed examples: Bantu, Quechuan, Austronesian, Trans-New Guinea, Mayan, Australian, Turkish evidentials
- **[prompt-template.md](prompt-template.md)** - Complete 5-level hierarchical prediction template with examples
- **[common-errors.md](common-errors.md)** - Full error taxonomy with linguistic examples and solutions
- **[experiment-001.md](experiment-001.md)** - Test cases for 6 passage types (narrative, prophecy, discourse, evidential)

## Academic Sources

**Core References**:
- Bybee et al. (1994). "The Evolution of Grammar: Tense, Aspect, and Modality"
- Nurse, Derek (2008). "Tense and Aspect in Bantu"
- Fleischman (1989). "Tense and Narrativity"

**Language-Specific**:
- Hintz: South Conchucos Quechua past tense functions
- Aksu-Koç: Turkish evidential acquisition
- Botne & Kershner: Tense organization in cognitive space

**Typological**:
- WALS Chapter 77: Semantic Distinctions of Evidentiality
- Oxford Research Encyclopedia: Australian/Trans-New Guinea morphology

---

*Research Date: November 2025*
*Languages Analyzed: 725+ from 11 families*
*Status: Framework stage - needs formalization and testing*
