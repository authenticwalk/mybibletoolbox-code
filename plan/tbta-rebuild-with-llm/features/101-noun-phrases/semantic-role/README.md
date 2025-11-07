# Semantic Role (TBTA Noun Phrase Feature)

**Target Audience:** Bible translators working with ergative languages, linguists analyzing case systems, pastors studying original language texts

**Primary Use Case:** When translating into ergative languages (Basque, Georgian, Mayan, Polynesian, etc.), translators must distinguish agents from patients to apply correct case marking, word order, and verb agreement. Accusative-based translations can mislead since grammatical subject ≠ semantic agent in ergative systems.

---

## Translation Impact

**Critical for ergative languages** where case marking, word order, and verb agreement depend on semantic role rather than grammatical function. Affects ~25% of world's languages (including major language families: Mayan, Kartvelian, Polynesian, Australian, Tibeto-Burman, some Caucasian). Without semantic role identification, translators may incorrectly map Greek/Hebrew subjects to ergative absolutive case or misalign verb agreement patterns.

---

## Complete Value Enumeration

| **Semantic Role** | **Definition** | **Example** | **Typical Markers** |
|-------------------|----------------|-------------|---------------------|
| **Agent** | Doer of volitional action | "**Jesus** healed the man" | Ergative case, nominative case |
| **Patient** | Entity affected by action | "Jesus healed **the man**" | Absolutive case, accusative case |
| **Theme** | Entity undergoing change/movement | "**The letter** went to Rome" | Absolutive case, nominative case |
| **Experiencer** | Entity in psychological state | "**Peter** saw the vision" | Dative case, nominative case |
| **Instrument** | Means by which action done | "He struck with **a rod**" | Instrumental case, oblique prep |
| **Beneficiary** | For whom action done | "He prayed for **them**" | Dative case, benefactive prep |
| **Location** | Spatial location of action | "He taught in **the temple**" | Locative case, locative prep |
| **Goal** | Destination/recipient | "They went to **Jerusalem**" | Allative case, directional prep |
| **Source** | Origin/starting point | "He came from **Galilee**" | Ablative case, source prep |
| **Stimulus** | Trigger of perception/emotion | "They heard **the sound**" | Accusative case, genitive case |

---

## Baseline Statistics

**Estimated Distribution (NT Greek):**
- Agent: ~40% (volitional subjects of transitive verbs)
- Patient: ~25% (direct objects of transitive verbs)
- Theme: ~15% (subjects of intransitive verbs, objects of motion)
- Experiencer: ~8% (perception/cognition subjects)
- Instrument: ~3%
- Beneficiary: ~3%
- Location/Goal/Source: ~4%
- Stimulus/Other: ~2%

**Genre Variation:**
- Narrative (Gospels/Acts): Higher Agent/Patient (action-heavy)
- Epistles: Higher Experiencer (cognitive verbs: know, believe, think)
- Apocalyptic: Higher Theme (passive subjects, cosmic movements)

---

## Quick Translator Test

1. **Is your language ergative/split-ergative?** (Basque, Georgian, K'iche', Tongan) → CRITICAL
2. **Does word order determine semantic role?** (English, Chinese, isolating) → Affects order
3. **Does case marking distinguish agent vs. patient?** (Latin, Russian, Georgian) → Needed
4. **Do verbs agree with agent/patient not subject?** (Mayan, Polynesian) → Determines morphology
5. **Passive-like constructions based on role?** (Antipassive) → Needed

**Scoring:** YES to #1 = CRITICAL; YES to #2-5 = HIGH priority

---

## Concrete Verse Examples

### Example 1: Agent vs. Patient (Transitive)

**John 3:16** - "God loved the world"
- **God** = Agent (Basque: ergative Jainkoak) | Greek: nominative
- **world** = Patient (Basque: absolutive mundua) | Greek: accusative

### Example 2: Theme (Intransitive Motion)

**Luke 10:30** - "A man was going down from Jerusalem to Jericho"
- **man** = Theme (Basque: absolutive, NOT ergative - non-volitional movement)
- **from Jerusalem** = Source | **to Jericho** = Goal

### Example 3: Experiencer vs. Stimulus

**Matthew 2:10** - "They saw the star"
- **they** = Experiencer (perception verb, not volitional Agent)
- **star** = Stimulus (trigger of perception)
- Some ergative languages treat Experiencer like Agent (ergative case); others use dative

### Example 4: Instrument

**Matthew 26:51** - "Struck the servant with his sword"
- **sword** = Instrument (Greek: ἐν μαχαίρῃ instrumental dative)

### Example 5: Beneficiary

**1 Corinthians 15:3** - "Christ died for our sins"
- **Christ** = Theme (undergoes death, not volitional)
- **our sins** = Beneficiary ("on behalf of")

---

## Gateway Features

1. **Voice:** Passive → Patient subject; Middle → Agent+Patient (reflexive); Active → Agent/Theme
2. **Verb Semantics:** Action → Agent+Patient; Perception → Experiencer+Stimulus; Motion → Theme+Goal/Source
3. **Case Marking:** Greek dative → Beneficiary/Experiencer; Accusative object → Patient/Stimulus
4. **Animacy:** Animate+transitive → Agent; Inanimate → Patient/Instrument

---

## Common Errors

1. **Confusing subject with Agent:** Passive subjects are Patient, not Agent ("stone was thrown" → stone=Patient)
2. **Ignoring ergative patterns:** Mapping all subjects to nominative without checking volitionality
3. **Misidentifying Experiencer as Agent:** Perception verbs have Experiencer, not volitional Agent
4. **Overlooking oblique roles:** Missing Instrument, Beneficiary, Location in prepositional phrases
5. **Confusing Theme with Patient:** Patient=affected by action; Theme=undergoes change/motion

---

## Validation Approach

**50-Verse Test Set:** 20 transitive (Agent+Patient), 10 intransitive motion (Theme), 10 perception (Experiencer), 5 instrument/beneficiary, 5 passive

**Expected Accuracy:** 80-85% overall (85-90% Agent/Patient, 70-80% Experiencer/Agent distinction)

**Validation:** Compare with ergative Bibles (Basque, Georgian, K'iche') to verify case marking alignment

**Manual Review Focus:** Perception verbs, passive constructions, middle voice, metaphorical usage

---

## Related Features

- **Voice** (TBTA verb feature): Passive → Patient as subject
- **Case** (Greek/Hebrew morphology): Correlates with semantic role
- **Word Order**: Some languages use role to determine order
- **Verb Agreement**: Ergative languages agree with Patient/Theme, not Agent
- **Animacy**: High animacy + transitive → likely Agent

---

## Prediction Methodology

*See [PREDICTION-METHODOLOGY.md](./PREDICTION-METHODOLOGY.md) for detailed 5-level hierarchical prompt template.*

**Quick Summary:**
1. Level 1: Grammatical role (subject → usually Agent/Theme)
2. Level 2: Verb semantics (action/perception/motion)
3. Level 3: Voice (active/passive/middle)
4. Level 4: Animacy and word order
5. Level 5: Context and discourse

---

## Ergative Language Examples

*See [ERGATIVE-LANGUAGES.md](./ERGATIVE-LANGUAGES.md) for comprehensive language-specific patterns.*

**Quick Examples:**
- **Basque**: ERG-ABS system, verb agrees with ABS (patient/theme)
- **Georgian**: Split ergativity (past tense), complex verb agreement
- **K'iche' Maya**: ERG-ABS, agent markers on verb, absolutive zero-marked
- **Dyirbal**: ERG-ABS with syntactic ergativity
- **Tongan**: ERG-ABS with ergative preposition 'e

---

## Summary

**Semantic Role is critical for accurate Bible translation because:**

1. **Ergative Languages**: ~25% of world's languages require Agent/Patient distinction for case marking
2. **Verb Agreement**: Some languages agree with Patient/Theme (not subject)
3. **Word Order**: Role affects translation order in isolating languages
4. **Case Selection**: Determines which case to use in highly inflected languages
5. **Cross-linguistic Accuracy**: Prevents grammatical subject from misleading ergative translators

**Key Takeaways:**
- **Agent** (~40%): Volitional doer of transitive action
- **Patient** (~25%): Affected entity (direct object)
- **Theme** (~15%): Undergoes change/motion (often intransitive subject)
- **Experiencer** (~8%): Psychological state (perception/cognition)
- **Other roles** (~12%): Instrument, Beneficiary, Location, Goal, Source

**For tool developers:** Implement 5-level hierarchical prediction (grammatical role → verb semantics → voice → animacy → context)

**For translators:** Essential for ergative languages; helpful for understanding Greek/Hebrew case patterns in all languages

---

**Document Status:** Production-ready documentation (experiments not yet run)
**Lines:** 190
**Last Updated:** 2025-11-07
**Next Steps:** Run validation experiments on 50-verse test set
