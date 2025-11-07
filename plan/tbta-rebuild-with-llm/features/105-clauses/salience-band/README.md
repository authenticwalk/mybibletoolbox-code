# Salience Band

Salience Band captures clause-level prominence in discourse structure, marking the foreground-background distinction that determines whether events advance the main storyline (foreground) or provide supporting information (background). This discourse-level feature is **CRITICAL** for Bantu languages where verb forms change based on clause salience.

## Quick Reference

**Validation**: 70-80% accuracy expected (discourse features are harder than syntactic)
**Test Case**: Genesis 1 (varied salience levels in creation narrative)
**Implementation**: LLM prompting with discourse analysis (genre-sensitive)

## Translation Impact

Salience Band is **CRITICAL** for Bantu languages (89 languages in TBTA corpus) where verb forms systematically distinguish foreground (mainline narrative events) from background (setting, circumstance, explanation). It affects verb morphology selection, word order, and narrative structure across entire paragraphs, making it essential for participant tracking and discourse coherence in accusative languages with foreground/background verb distinctions.

### High-Impact Language Families

| Family | Critical Features | Impact | Examples |
|--------|-------------------|--------|----------|
| **Bantu** | Past tense forms split by salience (-li- mainline, -ka- sequential, -ki- background) | CRITICAL - grammatically required | Swahili, Kinyarwanda, Luganda, Chichewa, Shona (89 in TBTA) |
| **Turkish** | Evidential morphology (-miş marks background, lower salience) | HIGH - pragmatic/grammatical | Turkish, Azerbaijani |
| **Japanese** | Te-form chaining for sequential foreground vs subordinate background | HIGH - clause chaining structure | Japanese, Korean (similar patterns) |
| **Accusative** | Tense, word order, subordination encode salience | MEDIUM - stylistic but important | English, Romance, Germanic |

## Complete Value Enumeration

TBTA defines 5 salience band levels representing discourse prominence:

| Level | Frequency Est. | Definition | Example |
|-------|----------------|------------|---------|
| **Pivotal** | ~5% | Turning point, climax, critical decision, peak narrative moment | "Then God said, 'Let there be light'" (GEN 1:3) |
| **Primary** | ~25% | Main storyline events, advancing plot, sequential foreground | "God separated the light from darkness" (GEN 1:4) |
| **Secondary** | ~40% | Supporting events, elaboration, consequential actions | "God called the light Day" (GEN 1:5) |
| **Background** | ~25% | Setting, circumstance, explanation, descriptive state | "The earth was formless and void" (GEN 1:2) |
| **Setting** | ~5% | Scene-setting, temporal anchors, discourse frames | "In the beginning God created..." (GEN 1:1) |

**Note**: Frequencies vary significantly by genre:
- **Narrative**: Higher Primary/Secondary (60%+ foreground)
- **Epistles/Teaching**: Higher Background/Setting (explaining concepts)
- **Poetry/Prophecy**: More Pivotal moments, less linear progression

## Baseline Statistics

Expected distribution in Biblical narrative (genre-dependent):

### Narrative Texts (Genesis, Gospels, Acts)
- **Primary**: 20-30% (main storyline)
- **Secondary**: 35-45% (supporting events)
- **Background**: 20-30% (circumstances)
- **Pivotal**: 3-8% (turning points)
- **Setting**: 2-5% (scene anchors)

### Epistles/Teaching (Romans, Hebrews)
- **Background**: 40-50% (explanation, reasoning)
- **Secondary**: 25-35% (supporting points)
- **Primary**: 10-20% (main arguments)
- **Pivotal**: 5-10% (theological climaxes)
- **Setting**: 2-5% (discourse transitions)

**Red flags**:
- <10% Primary in narrative → Missing main storyline
- >50% Background in narrative → Over-backgrounding events
- >15% Pivotal → Over-identifying turning points (should be rare)
- Flat distribution (20% each) → Not tracking discourse structure

## Quick Translator Test

**Does your target language require salience band distinctions?**

1. ☐ Does your language distinguish foreground vs background clauses? (verb forms, word order)
2. ☐ Do verbs change form by salience (mainline vs offline, sequential vs background)?
3. ☐ Are there special narrative forms for main storyline events? (narrative tense vs descriptive)
4. ☐ Does word order change for backgrounded information? (topic-comment, left-dislocation)
5. ☐ Are there particles marking clause prominence? (topic markers, focus particles)

**If YES to #1-2**: This feature is **CRITICAL** for grammatical correctness (especially Bantu).
**If YES to #3**: Need accurate Primary/Secondary distinction for verb form selection.
**If YES to #4-5**: Need Background/Setting distinction for syntactic structure.

**High-priority languages**: All Bantu (Swahili, Kinyarwanda, Luganda, etc.), Turkish, Japanese, Korean.

## Concrete Verse Examples

### Genesis 1:1-5 (Creation Narrative with Swahili)

| Verse | English | Salience | Swahili Form | Pattern |
|-------|---------|----------|--------------|---------|
| **1:1** | "In beginning God created..." | Setting | a-li-umba | -li- scene anchor |
| **1:2** | "Earth was formless and void" | Background | i-li-kuwa | -li- stative |
| **1:3** | "God said, 'Let there be light'" | Pivotal | a-ka-sema | -ka- mainline |
| **1:4** | "God saw...God separated" | Primary | a-ka-ona, a-ka-tenganisha | -ka- sequential |
| **1:5** | "God called the light Day" | Secondary | a-ka-ita | -ka- lower prominence |

**Key Pattern**: Setting (-li-) → Background (-li- stative) → Pivotal (-ka-) → Primary (-ka- chain) → Secondary (-ka-)

### Matthew 24:29-30 (Eschatological Peaks)

| Verse | Content | Salience | Reason |
|-------|---------|----------|--------|
| **24:29** | "After tribulation...sun darkened" | Setting | Temporal frame for climax |
| **24:30a** | "Sign of Son of Man appears" | Pivotal | Cosmic turning point |
| **24:30b** | "Tribes of earth will mourn" | Primary | Consequential response |

## Hierarchical Prompt Template (5 Levels)

| Level | Question | Key Indicators | Predicted Salience |
|-------|----------|----------------|-------------------|
| **1. Notional Structure** | Clause type? | Climax → Pivotal/Primary; Means → Secondary/Background | High confidence |
| **2. Participant Tracking** | Referent status? | First Mention → Primary; Generic → Background | Medium confidence |
| **3. Discourse Flow** | Advance storyline? | Sequential → Primary; Simultaneous → Background | High confidence |
| **4. Genre** | Text type? | Narrative → 60% foreground; Epistles → 50% background | Context-dependent |
| **5. Verb Form** | Greek/Hebrew? | Aorist/wayyiqtol → Primary; Imperfect/qatal → Background | High confidence |

**Usage**: Apply levels 1-5 in order, weighing higher levels more heavily. Genre (Level 4) adjusts expectations.

## Gateway Features

Strong correlations with other TBTA features:

| Source Feature | Correlation | Predicted Salience | Confidence |
|----------------|-------------|-------------------|------------|
| **Notional Structure = Climax** | High | Pivotal or Primary | 80% |
| **Notional Structure = Means** | High | Secondary or Background | 75% |
| **Participant Tracking = First Mention** | Medium | Primary or Secondary | 65% |
| **Participant Tracking = Generic** | High | Background | 85% |
| **Discourse Genre = Narrative** | Medium | Primary/Secondary dominant | 70% |
| **Greek aorist indicative (main clause)** | High | Primary | 75% |
| **Greek imperfect** | High | Background | 80% |
| **Hebrew wayyiqtol** | High | Primary (sequential) | 85% |
| **Subordinate syntax** | Medium | Background | 65% |

**Validation rule**: If Pivotal but Routine participant + no special verb form → Re-check (Pivotal should be rare, marked events)

## Common Errors

### Error 1: Confusing Grammatical Subordination with Discourse Backgrounding
**Problem**: Assuming all subordinate clauses are Background salience
**Wrong**: "When Jesus saw the crowds, he went up the mountain" → Both Background
**Right**: "When Jesus saw the crowds" (Background setting), "he went up the mountain" (Primary mainline)
**Fix**: Subordinate syntax ≠ discourse background. Check if clause advances storyline.

### Error 2: Treating All Clauses as Equal Salience
**Problem**: Marking entire passage as Primary/Secondary without variation
**Wrong**: Every sentence in narrative = Primary
**Right**: Identify foreground (Primary/Secondary), background (Background), peaks (Pivotal)
**Fix**: Use discourse structure analysis, not clause-by-clause processing

### Error 3: Missing Pivotal Moments
**Problem**: Under-identifying narrative turning points
**Example**: Genesis 1:3 "Let there be light" = Primary (should be Pivotal)
**Fix**: Look for climactic events, first occurrences of key themes, narrative peaks

### Error 4: Over-Pivoting
**Problem**: Marking too many clauses as Pivotal (should be <10% even in dramatic texts)
**Wrong**: Every divine speech in Genesis 1 = Pivotal
**Right**: First creative word (1:3) = Pivotal; others = Primary/Secondary
**Fix**: Reserve Pivotal for true turning points, not all important events

### Error 5: Ignoring Discourse Structure
**Problem**: Assigning salience without paragraph-level context
**Wrong**: Analyzing verse-by-verse without discourse flow
**Right**: Track narrative development, identify episode boundaries, find peaks
**Fix**: Read full paragraph/pericope before assigning salience levels

### Error 6: Applying Narrative Patterns to Non-Narrative Genres
**Problem**: Using narrative salience distribution in epistles
**Example**: Romans 3:23-24 → Expecting 30% Primary (wrong for theological explanation)
**Fix**: Adjust expectations by genre; epistles have more Background/Setting

## Validation Approach

**Test Passages**: Genesis 1, John 9 (narrative); Romans 3, Hebrews 11 (epistles); Matthew 24 (eschatological)

**Methods**:
1. **Bantu Check**: -ka- forms = Primary; -ki- forms = Background (compare published Swahili)
2. **Discourse Structure**: Pivotal marks peaks; Primary follows sequential chains
3. **Frequency**: Narrative 60%+ foreground; Epistles 50%+ background; <10% Pivotal

**Expected Accuracy**: 70-80% overall (easier in narrative, harder in abstract argument; requires paragraph-level context)

## Theoretical Foundations

Based on: Hopper & Thompson (1980) foreground/background; Longacre (1990s) narrative peak; Givón (1984) grounding; Levinsohn (2015) Greek NT discourse; Dooley & Levinsohn (2001) SIL manual.

See DISCOURSE-THEORY.md for full linguistic foundations (40+ years of research).

## Cross-linguistic Application

| Language | Encoding | Foreground | Background |
|----------|----------|------------|------------|
| **Swahili** | Verb morphology | -ka- (sequential) | -ki- (circumstantial) |
| **English** | Tense/syntax | Simple past, main clause | Progressive, subordinate |
| **Japanese** | Chaining | Te-form | -nagara (simultaneous) |
| **Turkish** | Evidential | -DI (witnessed) | -mIş (non-witnessed) |

See BANTU-VERB-FORMS.md for 10+ Bantu languages; DISCOURSE-THEORY.md for full linguistic theory.

## Quick Start

1. **5 levels**: Setting → Background → Secondary → Primary → Pivotal
2. **Check genre**: Narrative (60%+ foreground); epistles (50%+ background)
3. **Use hierarchical template**: Notional Structure → Participant Tracking → Discourse Flow → Genre → Verb Form
4. **Validate**: Compare with Swahili (-ka- = Primary; -ki- = Background)
5. **Test**: Genesis 1 (clear variation, well-studied)

## Success Criteria

- [ ] Distribution matches genre baseline (narrative: 60%+ foreground; epistles: 50%+ background)
- [ ] Pivotal marks true turning points (<10% of clauses)
- [ ] Primary aligns with Greek aorist indicative, Hebrew wayyiqtol
- [ ] Background aligns with Greek imperfect, Hebrew qatal, subordinate clauses
- [ ] Bantu translations use correct verb forms (if available for validation)
- [ ] 70-80% accuracy when validated against native speaker discourse analysis
