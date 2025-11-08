# Serial Verb Constructions

**Status:** Documentation complete
**TBTA Relevance:** High - affects Niger-Congo (~40 langs), Trans-New Guinea (129 langs), Austronesian (many langs)
**Greek/Hebrew:** Not present - Greek/Hebrew use coordination or subordination

## Overview

Serial verb constructions (SVCs) are sequences of multiple verbs sharing the same subject and tense-aspect marking without conjunctions, expressing a single complex event. This construction is absent from Greek and Hebrew but obligatory or highly preferred in many target languages.

## Cross-Linguistic Pattern

**Present in:**
- **Niger-Congo**: Kwa, Benue-Congo (~40 languages); less common in Bantu
- **Trans-New Guinea**: Extremely productive across all 129 languages
- **Austronesian**: Some languages

**Pattern:** Multiple verbs in sequence sharing subject and TAM, no conjunctions

## Language Family Examples

### Niger-Congo (Yoruba)
- `Ó mú ìwé wá` (He took book came) = "He brought a book"
- `Mo rí i lọ` (I saw him go) = "I saw him leave"
- Directional: `wá` (come), `lọ` (go) as second verb
- Benefactive: Serial with `fún` (give) = do for someone

### Trans-New Guinea (Common patterns)
- **Directional**: "come + see" = come to see
- **Benefactive**: "do + give" = do for (someone)
- **Causative**: "make + happen" = cause to happen
- **Manner**: "go + run" = go running
- **Purpose**: Compensate for small verb root inventories (some languages <100 roots)

### Austronesian (Various)
- Less productive than Niger-Congo/Trans-New Guinea
- Used for directional and benefactive constructions

## Biblical Translation Examples

### Luke 15:18
**Greek:** ἀναστὰς πορεύσομαι (arise-PART go-FUT)
**English:** "I will arise and go to my father"
**SVC:** arise-go (single serial construction, no conjunction)

### Mark 1:17
**Greek:** Δεῦτε ὀπίσω μου (come-IMP after me)
**English:** "Come, follow me"
**SVC:** come-follow (natural serial verb sequence)

### Acts 8:27
**Greek:** ἀναστὰς ἐπορεύθη (arise-PART went)
**English:** "He rose and went"
**SVC:** rose-went (single serial verb sequence)

### Complex Actions
**Greek:** Coordinated clauses with καί (and)
**English:** "He went up, entering the temple"
**SVC:** go-up-enter (multiple serials, treated as single event)

## Common SVC Patterns

### 1. Directional SVCs
**Function:** Indicate direction of motion
**Pattern:** Motion verb + directional verb
**Biblical use:**
- "Come to see" → come-see
- "Go to speak" → go-speak
- "Ascend to heaven" → go.up-be.in

### 2. Benefactive SVCs
**Function:** Indicate action done for someone's benefit
**Pattern:** Action verb + "give" verb
**Biblical use:**
- "He healed them" → heal-give-them (do-healing for-them)
- "Jesus taught the disciples" → teach-give-disciples

### 3. Causative SVCs
**Function:** Express causation
**Pattern:** Causative verb + result verb
**Biblical use:**
- "Make them understand" → make-understand (cause-to-understand)
- "God made them" → make-exist

### 4. Manner SVCs
**Function:** Describe how an action is performed
**Pattern:** Main verb + manner verb
**Biblical use:**
- "He spoke loudly" → speak-be.loud
- "Run quickly" → run-be.fast

## Cultural Variations

### Action Conceptualization
What counts as a "single event" varies by culture:
- Western: "went shopping" = single event with internal complexity
- SVC languages: "went shopping" = three events (go + look + buy)

### Theological Clarity
**Benefactive SVCs** emphasize actions done "for" someone:
- "God gave us salvation" = do-salvation give-us (serial emphasizes gift nature)
- "Christ died for us" = die give-us (benefactive serial)

### Reciprocal Community
**Niger-Congo example:** "Love one another" can use serial with reciprocal marking
- More natural than single verb + reciprocal object

## Translation Strategy

### When Source Uses Coordination
Greek/Hebrew often use coordinated finite verbs (and):
- Analyze: Are these sequential steps of one event or separate events?
- **Single event** → Use SVC
- **Separate events** → Use coordination (if available) or clause chaining

### When Source Uses Subordination
Greek/Hebrew participles often express manner/purpose:
- "Going, he spoke" → Go-speak (directional SVC)
- "Speaking, he left" → Speak-leave (manner SVC)

### Verb Inventory Considerations
**Trans-New Guinea languages** have small verb inventories:
- May require creative SVC combinations to match Greek/Hebrew semantic richness
- Example: "worship" might be bow-honor-give (three serials)

## Interaction with Other Features

### With Aspect
SVCs typically share aspect marking:
- All verbs in sequence have same aspect value
- TBTA aspect annotation applies to the entire construction

### With Clause Chaining
**Trans-New Guinea:** SVCs differ from clause chains:
- **SVC:** Single event, no switch-reference marking
- **Clause chain:** Sequential events, switch-reference required

### With Participant Tracking
Serial verbs share the same subject:
- Subject tracking simpler within SVCs
- NounListIndex applies to shared subject

## Data Requirements for TBTA

### Per-Verse Annotation
For verses with potential SVCs, annotate:
1. **Greek/Hebrew construction:** Coordination, subordination, or single verb?
2. **Semantic relationship:** Directional, benefactive, causative, manner, other?
3. **Event structure:** Single complex event or multiple events?

### Language-Specific Patterns
Document for each SVC-using language:
- Which semantic relationships use SVCs?
- Are there restrictions on verb combinations?
- How do SVCs interact with TAM marking?
- What coordination alternatives exist?

## Variants by Family

### Niger-Congo
- **Kwa/Benue-Congo:** Extremely productive, many semantic types
- **Bantu:** Less productive, limited to specific constructions
- **Mande:** Different strategies, not typical SVCs

### Trans-New Guinea
- **Universal across family**
- Compensates for small verb inventories
- Very long serial sequences possible (5+ verbs)

### Austronesian
- **Variable productivity**
- Philippine type: moderate use
- Oceanic: variable by language
- Indonesian: limited, more analytic constructions

## Research Gaps

1. Comprehensive catalog of SVC semantic types across languages
2. Interaction with Greek participle constructions
3. Edge cases: When does coordination become SVC?
4. Language-specific restrictions on verb combinations
5. How SVC languages translate Hebrew infinitive absolute constructions

## Sources

### Niger-Congo
- Niger-Congo README.md: Serial Verb Constructions section
- Yoruba examples and patterns
- Bantu limited productivity noted

### Trans-New Guinea
- Trans-New Guinea README.md: Serial Verb Constructions section
- Small verb inventory compensation strategy
- Universal productivity across family

### Austronesian
- Austronesian README.md: Limited SVC documentation
- Variable productivity by sub-family

## Recommendations

### For TBTA Annotation
1. Mark all verses where Greek/Hebrew uses coordination that might map to SVC
2. Identify semantic relationship (directional, benefactive, causative, manner)
3. Note when event structure is ambiguous (single vs multiple events)

### For Tool Development
1. Create SVC semantic type taxonomy
2. Map Greek participle constructions to SVC types
3. Identify common biblical SVC patterns across language families
4. Validate against actual translations in SVC languages

### For Translation Practice
1. Analyze Greek/Hebrew coordination for event unity
2. Consider cultural conceptualization of action boundaries
3. Leverage SVC for natural expression of complex events
4. Avoid over-using coordination when SVC is more natural

---

**Created:** 2025-11-07
**Last Updated:** 2025-11-07
**Languages Affected:** 175+ (Niger-Congo ~40, Trans-New Guinea 129, Austronesian many)
**TBTA Priority:** High - affects narrative structure across major language families
