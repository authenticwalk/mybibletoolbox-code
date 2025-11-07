# TBTA Feature: Proximity

## Translation Impact

Proximity distinctions determine which demonstrative forms translators must choose in the target language. Languages vary from simple two-way systems (English "this/that") to complex person-oriented systems (Japanese ko/so/a distinguishing near-speaker/near-hearer/remote), visibility-based systems (Austronesian visible/invisible), and elevation-based systems (Trans-New Guinea uphill/downhill). Without accurate proximity annotation, translations into these 1009 languages will produce unnatural or incorrect demonstrative choices, particularly problematic for the 37.6% of languages with three-way systems and specialized systems requiring visibility or elevation distinctions.

## Complete Value Enumeration

TBTA encodes proximity using **position 8** of the semantic string for nouns with 10 possible values:

| Code | Category | Meaning | Description |
|------|----------|---------|-------------|
| `n` | N/A | Not Applicable | No proximity distinction needed |
| **Spatial - Physical Location** ||||
| `N` | Physical | Near Speaker and Listener | Referent close to both speaker and hearer |
| `S` | Physical | Near Speaker | Referent close to speaker only |
| `L` | Physical | Near Listener | Referent close to hearer/addressee |
| `R` | Physical | Remote within Sight | Referent far but visible |
| `r` | Physical | Remote out of Sight | Referent far and not visible |
| **Temporal - Time Distance** ||||
| `T` | Temporal | Temporally Near | Recent time reference |
| `t` | Temporal | Temporally Remote | Distant time reference |
| **Discourse - Textual Reference** ||||
| `C` | Discourse | Contextually Near with Focus | Recently mentioned with emphasis |
| `c` | Discourse | Contextually Near | Recently mentioned in discourse |

## Baseline Statistics

Expected distribution in Biblical narrative (estimates based on demonstrative frequency):

| Code | Estimate | Context |
|------|----------|---------|
| `n` (Unmarked) | ~40% | No explicit demonstrative marking |
| `N`, `S` (Near Spatial) | ~30% | "this", "these", nearby referents in scenes |
| `R`, `r` (Far Spatial) | ~20% | "that", "those", distant referents |
| `T`, `t` (Temporal) | ~5% | Time references ("this day", "that day") |
| `C`, `c` (Discourse) | ~5% | Anaphoric/cataphoric references |

**Genre Variation:**
- Narrative (Genesis, Acts): Higher spatial (30-40%)
- Teaching (Epistles): Higher discourse (15-20%)
- Prophecy (Isaiah): Higher temporal (10-15%)

## Quick Translator Test

**Critical questions to determine if your language needs detailed proximity annotation:**

1. **How many distance levels does your language mark?**
   - 2-way (this/that): 54% of languages → Use N/S vs R/r
   - 3-way person-oriented (near me/near you/far): 38% → Use S/L/R
   - 3-way distance (near/middle/far): Use N/R/r
   - 4+ way: Rare but critical → May need compound coding

2. **Does your language distinguish speaker vs. hearer proximity?**
   - Person-oriented (Japanese ko/so/a, Spanish este/ese/aquel)
   - Need `S` (near speaker) vs `L` (near hearer) distinction

3. **Does visibility matter in your language?**
   - Visible vs. invisible demonstratives (Austronesian, Amazonian)
   - TBTA `R` (visible) vs `r` (invisible)

4. **Does elevation or topography matter?**
   - Uphill/downhill demonstratives (Trans-New Guinea, Trans-Himalayan)
   - Map to spatial codes, infer from context + motion verbs

5. **Does your language mark temporal proximity with demonstratives?**
   - "This day" (present) vs "that day" (past/future)
   - TBTA `T` (near time) vs `t` (remote time)

**High-complexity languages requiring detailed annotation:**
- Japanese, Korean (person-oriented 3-way)
- Spanish, Portuguese (este/ese/aquel)
- Austronesian languages (visibility)
- Trans-New Guinea languages (elevation)
- Bantu languages (noun class agreement)

## Examples

**Example 1: John 1:29** - Spatial Proximity
```yaml
Greek: ἴδε ὁ ἀμνὸς τοῦ θεοῦ (ide ho amnos tou theou)
English: "Behold the Lamb of God"
Proximity: R (Remote within Sight)
Reason: Jesus visible but at distance from John the Baptist
```

**Example 2: John 3:16** - Discourse Proximity
```yaml
Greek: οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον (houtōs gar ēgapēsen ho theos ton kosmon)
English: "For God so loved the world"
Proximity: C (Contextually Near with Focus)
Reason: Demonstrative "so/thus" emphasizes the manner just described
```

**Example 3: Matthew 24:3** - Temporal Proximity
```yaml
Greek: ταῦτα πάντα ἔσται (tauta panta estai)
English: "When will these things be?"
Proximity: t (Temporally Remote)
Reason: Eschatological future events, distant from present
```

**Example 4: Genesis 19:31** - Spatial/Discourse
```yaml
Hebrew: אֵין אִישׁ בָּאָרֶץ (ein ish ba'aretz)
English: "There is not a man in the earth"
Proximity: r (Remote out of Sight)
Reason: General reference to absent men, not physically present
```

**Example 5: Ezekiel 5:5** - Discourse with Emphasis
```yaml
Hebrew: זֹאת יְרוּשָׁלִָם (zot yerushalaim)
English: "This is Jerusalem"
Proximity: C (Contextually Near with Focus)
Reason: Emphatic subject position, cataphoric introduction
```

## Hierarchical Prompt Template (5-Level)

### Level 1: Check for Demonstrative

```
Does this noun phrase use a demonstrative or deictic marker?

Source: [Greek/Hebrew text]
Translation: [English]

Check for:
- Greek: ὅδε (hode), οὗτος (houtos), ἐκεῖνος (ekeinos)
- Hebrew: זֶה (zeh), זֹאת (zot), אֵלֶּה (elleh), הַלָּז (hallaz)
- Deictic adverbs: here, there, now, then

Answer: YES or NO
```

**Decision:** NO → `n` (Not Applicable), STOP | YES → Continue to Level 2

### Level 2: Identify Source Form

```
What demonstrative form appears in the source text?

Source demonstrative: [Extracted form]

Greek mapping:
- ὅδε → Usually Near Spatial (N/S)
- οὗτος → Near Spatial or Discourse (N/C/c)
- ἐκεῖνος → Far Spatial or Temporal (R/t)

Hebrew mapping:
- זֶה → Context-dependent (analyze further)
- הַלָּז → Always Remote Spatial (R)
- הוּא (demonstrative use) → Usually Discourse (c)
```

**Decision:** Continue to Level 3

### Level 3: Determine Proximity Domain

```
What kind of proximity does this demonstrative indicate?

A. Physical/Spatial: Physical location relative to participants
   - Scene with characters, locations, visible objects

B. Temporal: Time reference (past/present/future)
   - Temporal nouns: day, time, hour, generation

C. Discourse: Reference to textual entities/propositions
   - Abstract concepts, anaphoric/cataphoric reference

Identified domain: [A, B, or C]
```

**Decision:** A → Level 4 | B → Level 5A | C → Level 5B

### Level 4: Spatial Proximity Analysis

```
Analyze physical proximity of the referent.

Questions:
1. Is referent physically present in the scene?
2. How close to speaker? To hearer?
3. Is referent visible to participants?

Proximity codes:
- Near both speaker and listener → N
- Near speaker specifically → S
- Near listener/addressee → L
- Distant but visible → R
- Distant and not visible → r

Final prediction: [Code with justification]
```

### Level 5A: Temporal Proximity Analysis

```
Analyze temporal proximity of the referent.

Questions:
1. What time period is referenced?
2. How close to narrative "now"?
3. Temporal markers: "this day" (near) or "that day" (remote)?

Proximity codes:
- Present, immediate, recent → T
- Past (historical), future (distant/eschatological) → t

Final prediction: [T or t with justification]
```

### Level 5B: Discourse Proximity Analysis

```
Analyze discourse proximity of the referent.

Questions:
1. Is referent abstract (not physical)?
2. Anaphoric (back) or cataphoric (forward)?
3. Is there emphatic focus?

Proximity codes:
- Recently mentioned WITH emphasis → C
- Recently mentioned, routine → c

Final prediction: [C or c with justification]
```

## Gateway Features (Correlations)

High-confidence quick predictions based on context:

| Context | Predict | Confidence | Notes |
|---------|---------|------------|-------|
| No demonstrative word | `n` | 95%+ | Check carefully for implicit deixis |
| Greek ὅδε (hode) | `N` or `S` | 85%+ | Immediate proximal, rarely used |
| Greek οὗτος + spatial scene | `N` | 80%+ | Physical presence implied |
| Greek οὗτος + abstract noun | `C` or `c` | 80%+ | "this teaching", "this word" |
| Greek ἐκεῖνος + past time | `t` | 85%+ | "that day", temporal remote |
| Hebrew הַלָּז (hallaz) | `R` | 95%+ | Always medial spatial |
| Temporal noun + "this" | `T` | 90%+ | "this day", "this hour" |
| Temporal noun + "that" | `t` | 90%+ | "that day", "those times" |
| Cataphoric "this is..." | `C` | 85%+ | Emphatic introduction |

**Multi-feature gateway (high confidence):**
- Greek οὗτος + Abstract Noun + Anaphoric → `c` (90%+)
- Greek ἐκεῖνος + Temporal + Eschatological → `t` (95%+)
- Hebrew זֶה + Physical Scene + Speaker Present → `N` or `S` (80%+)

## Common Prediction Errors

### Error 1: Confusing Spatial and Discourse Proximity (~20-30% of errors)

**Problem:** Treating abstract concepts as physically near

**Example:**
- Verse: "This teaching is true" (John 7:16)
- Wrong: `N` (Near Speaker) — treating "teaching" as physical
- Right: `C` or `c` (Discourse) — teaching is abstract

**Solution:** Ask "Can you physically touch this?" If no → Discourse

### Error 2: Missing Greek/Hebrew Nuances (~15-20% of errors)

**Problem:** Over-relying on English gloss, missing source distinctions

**Example:**
- Greek: ἐκεῖνος used (distal)
- English: "this" (translator choice)
- Wrong: `N` (based on English "this")
- Right: `R` or `t` (based on Greek ἐκεῖνος)

**Solution:** Always check source language form first

### Error 3: Not Accounting for Language-Specific Systems (~30-40% in complex languages)

**Problem:** Assuming 2-way system when target has 3-way or special features

**Example:**
- Scene: Jesus near John (speaker), crowd nearby
- 2-way: `N` (Near) — generic
- Japanese needs: `S` (near speaker John) vs `L` (near crowd) vs `R` (far)

**Solution:** Check target language typology before prediction

### Error 4: Temporal vs. Eschatological Confusion (~10-15% in prophetic texts)

**Problem:** Treating eschatological future as temporally near

**Example:**
- "In that day, the Lord will..." (Isaiah prophecy)
- Wrong: `T` (seeing "day" + demonstrative)
- Right: `t` (eschatological future is remote)

**Solution:** Check prophetic/narrative context

### Error 5: Ignoring Quoted Speech Perspective (~10-20% in narrative)

**Problem:** Using narrator perspective instead of speaker's

**Example:**
- Jesus said, "Take this bread"
- Wrong: Code from narrator perspective
- Right: Code from Jesus' perspective (bread near Jesus = `S` or `N`)

**Solution:** Identify who is speaking in quoted speech

## Validation Approach

**How to test proximity predictions:**

1. **Source Language Validation**
   - Check Greek demonstrative form (ὅδε/οὗτος/ἐκεῖνος)
   - Check Hebrew demonstrative (זֶה/הַלָּז) or context
   - Verify spatial/temporal/discourse indicators

2. **Cross-Feature Validation**
   - First Mention + Demonstrative = Unlikely (check for recognitional use)
   - Interrogative + Spatial = Verify (questions usually discourse)
   - Abstract Noun + Spatial = Likely Error (should be discourse)
   - Temporal Noun + Non-Temporal = Verify context

3. **Sample Testing**
   - Annotate 50-100 verses across genres
   - Compare predictions to TBTA gold standard
   - Calculate error rate by category
   - Target: <10% error rate with methodology

4. **Target Language Validation**
   - Test demonstrative choices with native speakers
   - Verify person-oriented distinctions (S vs L)
   - Confirm visibility requirements (R vs r)
   - Check elevation context if applicable

**Error Rate Expectations:**
- Without methodology: 40-50% error rate
- With source checking + context: <10% error rate

## Detailed Documentation

For comprehensive linguistic analysis, see:
- **[typology.md](typology.md)** - Cross-linguistic demonstrative systems, WALS data, language family patterns
- **[source-languages.md](source-languages.md)** - Greek and Hebrew demonstrative systems in detail
- **[methodology.md](methodology.md)** - Complete decision trees, edge cases, validation procedures

## Summary

Proximity is critical for accurate demonstrative translation across 1009 languages. The 10-value TBTA system covers ~90% of cross-linguistic needs through spatial (5 values), temporal (2 values), and discourse (2 values) distinctions. Key challenges include person-oriented 3-way systems (Japanese, Spanish), visibility-based systems (Austronesian), and elevation systems (Trans-New Guinea). Accurate annotation requires checking source language forms, determining proximity domain (spatial/temporal/discourse), and validating against target language requirements.
