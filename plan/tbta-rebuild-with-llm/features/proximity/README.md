# TBTA Proximity Annotation System: Comprehensive Research

**Document Purpose**: Deep research into TBTA's proximity annotation system for demonstratives and spatial deixis
**Date**: 2025-11-05
**Status**: Research Complete

## Executive Summary

TBTA encodes proximity distinctions using a 10-value system (position 8 in noun semantic strings) that captures spatial, temporal, and discourse-based proximity. This system is designed to help Bible translators working in the 1009 languages with diverse demonstrative systems ranging from two-way (proximal/distal) to complex multi-dimensional systems involving speaker/hearer location, visibility, elevation, and discourse reference.

## 1. TBTA Proximity Values

### 1.1 Complete Value Set

TBTA uses **position 8** of the semantic string for nouns (Syntactic Category 1) to encode proximity:

| Code | Meaning | Category | Description |
|------|---------|----------|-------------|
| `n` | Not Applicable | N/A | No proximity distinction needed |
| **Spatial - Physical Location** ||||
| `N` | Near Speaker and Listener | Physical | Referent close to both speaker and hearer |
| `S` | Near Speaker | Physical | Referent close to speaker only |
| `L` | Near Listener | Physical | Referent close to hearer/addressee |
| `R` | Remote within Sight | Physical | Referent far but visible |
| `r` | Remote out of Sight | Physical | Referent far and not visible |
| **Temporal - Time Distance** ||||
| `T` | Temporally Near | Temporal | Recent time reference |
| `t` | Temporally Remote | Temporal | Distant time reference |
| **Discourse - Textual Reference** ||||
| `C` | Contextually Near with Focus | Discourse | Recently mentioned with emphasis |
| `c` | Contextually Near | Discourse | Recently mentioned in discourse |

### 1.2 Category Analysis

#### Spatial Proximity (5 values)
The spatial category distinguishes:
1. **Three person-oriented positions**: N (both), S (speaker), L (listener)
2. **Two distance-oriented positions**: R (visible), r (invisible)

This hybrid system allows encoding both:
- **Person-oriented** distinctions (Japanese ko/so/a, Spanish este/ese/aquel)
- **Visibility-based** distinctions (Salish, Amazonian languages)

#### Temporal Proximity (2 values)
Mirrors spatial proximal/distal distinction applied to time:
- **T (near)**: "this day," "this time," immediate temporal reference
- **t (remote)**: "that day," "those times," distant temporal reference

#### Discourse Proximity (2 values)
Captures discourse deixis and anaphoric reference:
- **C (focused)**: "this matter we just discussed" (emphatic reference)
- **c (unfocused)**: "that earlier point" (routine reference)

### 1.3 Design Rationale

TBTA's 10-value system is designed to cover the major cross-linguistic demonstrative distinctions:

**Coverage Analysis:**
- **2-way systems** (54.3% of world's languages): Uses N/S vs R/r
- **3-way systems** (37.6% of languages): Uses N/S/L or N/R/r
- **4-way systems** (Japanese-type): Uses N/S/L/R
- **Visibility systems** (Amazonian): Uses R vs r
- **Elevation systems** (Trans-New Guinea): Maps to physical proximity categories
- **Temporal systems** (many languages): Uses T vs t
- **Discourse systems** (all languages): Uses C vs c

## 2. Cross-Linguistic Demonstrative Typology

### 2.1 WALS Typology (Chapter 41)

According to the World Atlas of Language Structures (Diessel 2013), demonstrative systems worldwide show the following distribution:

#### Distance Contrast Categories

**1. Two-Way Contrast (54.3% of languages)**
- **Proximal**: Near speaker/deictic center ("this")
- **Distal**: Far from speaker/deictic center ("that")
- **Examples**: English, Mandarin Chinese, many Indo-European languages

**2. Three-Way Contrast (37.6% of languages)**

Two subtypes:

**a) Distance-Oriented (Linear Distance Scale)**
- **Proximal**: Near speaker
- **Medial**: Middle distance
- **Distal**: Far from speaker
- **Example**: Hunzib (Nakh-Daghestanian)

**b) Person-Oriented (Speaker/Hearer Reference)**
- **Proximal**: Near speaker
- **Medial**: Near hearer/addressee
- **Distal**: Away from both
- **Examples**: Japanese, Korean, Spanish, many languages

**3. Four/Five-Way Contrast (4% of languages)**
- Nearly always person-oriented with additional distance distinctions
- **Example**: Hausa (Niger-Congo)
  - Near speaker
  - Near hearer
  - Away from both
  - Far away from both

**4. Distance-Neutral Systems (3% of languages)**
- No inherent distance marking in demonstratives
- **Example**: German (uses adverbs "hier"/"da" when contrast needed)

#### Geographic Distribution Patterns

| Region | Mean Distance Contrasts |
|--------|------------------------|
| Europe | 2.12 |
| Africa | 2.36 |
| Asia | 2.41 |
| Oceania | 2.44 |
| South America | 2.53 |
| North America | 2.75 (highest) |

**Key Finding**: Two and three-way systems dominate globally, with North America showing the most complex systems on average.

### 2.2 Additional Demonstrative Features

Beyond simple distance, demonstratives can encode:

#### 2.2.1 Visibility Distinctions

**Definition**: Marking whether referent is visible or invisible to speaker/hearer

**Examples:**

**Salish Language Nuxalk (British Columbia)**
- Three visible demonstratives: proximal/medial/distal (all require visibility)
- Three invisible demonstratives: proximal/medial/distal (all referent not visible)
- **Total**: 6-way system based on distance + visibility

**Ticuna (Amazonian Isolate, Brazil/Colombia/Peru)**
- Four demonstratives with visibility preferences
- Speaker-medial and speaker-distal primarily index visible referents
- Speaker-proximal and addressee-proximal can index visible or invisible
- **Research Finding**: Visibility may be less fundamental than distance in actual usage

**Malagasy (Austronesian, Madagascar)**
- Demonstratives distinguish visible vs. invisible spatial locations
- Part of broader Austronesian tendency toward visibility marking

**TBTA Mapping**: R (visible) vs r (invisible) captures this distinction

#### 2.2.2 Elevation-Based Systems

**Definition**: Demonstratives encode vertical/topographic relationships (uphill/downhill, up/down)

**Geographic Distribution**: Concentrated in mountainous regions:
- **Trans-New Guinea languages** (Papua New Guinea highlands)
- **Trans-Himalayan/Sino-Tibetan** (Himalayan regions)
- Occasional in other mountainous areas

**Examples:**

**Yupno (Trans-New Guinea, Finisterre-Huon)**
- Motion verbs inflected for uphill/downhill/level movement
- Demonstratives optionally inflected for elevation
- **Temporal Extension**: Uphill = future, Downhill = past
- Reflects mountainous environment with strong vertical orientation

**Kewapi (Enga-Kewa-Huli, Southern Highlands PNG)**
- 13 demonstratives total
- 9 co-express elevational meanings + distance
- Among richest demonstrative systems documented

**Tauya (Madang, PNG)**
- Topographical deixis in demonstratives
- Uphill/downhill distinctions grammaticalized

**Trans-Himalayan Languages**
- Widespread topographical deixis
- Upriver/downriver, uphill/downhill distinctions
- Common across multiple subgroups

**TBTA Mapping**: Elevation systems would map to spatial proximity categories (S/L/R), with elevation distinction captured in other features or lexical choice

#### 2.2.3 Direction and Movement

**Definition**: Demonstratives or spatial deictics encode direction toward/away from deictic center

**Examples:**

**Yupno and related languages**
- Motion verbs encode direction of movement
- Uphill/downhill inherently directional

**Various languages**
- Upriver/downriver (riverine communities)
- Seaward/landward (coastal communities)
- Toward/away from deictic center

**TBTA Mapping**: Direction may be implicit in choice between proximal (approaching) and distal (receding), or captured in verb semantics rather than demonstrative proximity

### 2.3 Language Family Patterns

#### 2.3.1 Indo-European

**Dominant Pattern**: Two-way systems (proximal/distal)

**Examples:**
- **English**: this/that (2-way)
- **German**: dieser/jener (distance-neutral in modern usage)
- **Spanish**: este/ese/aquel (3-way: near me/near you/far)
- **Portuguese**: este/esse/aquele (3-way)
- **Italian**: questo/codesto/quello (3-way, codesto archaic)
- **Greek (Ancient)**: ὅδε/οὗτος/ἐκεῖνος (3-way, see Section 3)
- **Latin**: hic/iste/ille (3-way)
- **Slavic languages**: Often 2-way (Russian этот/тот)

**Trend**: Germanic languages simplified to 2-way; Romance retains 3-way in many branches

#### 2.3.2 Austronesian

**Dominant Pattern**: Two-way and three-way systems with additional features

**Examples:**
- **Hawaiian**: 3-way distance system
- **Hawu (Eastern Indonesia)**:
  - Nominal system: 10 terms distinguishing distance, specificity, individuation, knowledge
  - Verbal system: 5 terms distinguishing distance, number, presentative function
  - One of the most complex documented systems
- **Tagalog**: Complex system with case-marking interaction
- **Malagasy**: Visibility distinctions (visible/invisible)

**Features:**
- Visibility distinctions common
- Interaction with noun class/definiteness systems
- Sometimes distinguish referent individuation

**Reconstructed Proto-Austronesian**: Had demonstrative system, details debated

#### 2.3.3 Niger-Congo (esp. Bantu)

**Dominant Pattern**: Demonstratives interact with noun class systems

**Examples:**
- **Swahili (Bantu)**:
  - Proximal: ha- + class marker (e.g., hawa "these persons")
  - Distal: class marker + -le (e.g., wale "those persons")
  - Agreement with 15+ noun classes
- **Hausa (Chadic, but in Africa)**:
  - 4-way system: near speaker / near hearer / away from both / far away
  - One of few documented 4-way systems

**Features:**
- Noun class agreement obligatory
- Each demonstrative has multiple forms for different noun classes
- Typically 2-3 distance distinctions × 10-20 noun classes = large paradigm

**Proto-Bantu**: Reconstructed demonstrative system with proximal/distal distinction

#### 2.3.4 Trans-New Guinea

**Dominant Pattern**: 2-3 way systems with frequent elevation marking

**Examples:**
- **Yupno**: Elevation-based + distance (see 2.2.2)
- **Kewapi**: 13 demonstratives with elevation (see 2.2.2)
- **Many TNG languages**: 2-3 distance distinctions
- **Elevational marking**: Concentrated in highland languages

**Features:**
- SOV word order affects demonstrative placement
- Elevation-based systems common in highlands
- Demonstratives may show noun class/gender agreement (in some families)
- Interaction with clause-chaining and switch-reference systems

**Translation Implications**:
- Vertical spatial language in Scripture (ascension, descension) maps naturally
- Hebrew עָלָה ('alah "go up") and יָרַד (yarad "go down") find direct equivalents

#### 2.3.5 Sino-Tibetan

**Dominant Pattern**: 2-3 way systems, some with elevation

**Examples:**
- **Mandarin Chinese**: 这 (zhè "this") / 那 (nà "that") - 2-way
- **Cantonese**: 呢 (ni1 "this") / 嗰 (go2 "that") - 2-way
- **Trans-Himalayan languages**: Topographical deixis common
- **Tibetic languages**: Often 2-3 way with elevation features

**Features:**
- Demonstratives often function as determiners
- Elevation marking in mountainous regions
- Interaction with classifier systems

#### 2.3.6 Native American Languages

**Dominant Pattern**: High diversity, including most complex systems

**Examples:**
- **Koasati (Muskogean)**: 4-term system
- **Maricopa (Yuman)**: 4-term system
- **Navajo (Athabaskan)**: 4-term system
- **Tlingit (Na-Dene)**: 4-term system
- **Quileute (Chimakuan)**: 4-term system

**Features:**
- North America has highest mean distance contrasts (2.75)
- Many 4-5 term systems
- Often person-oriented (near me/near you/near third person/remote)
- Some with evidential or epistemic extensions

**Geographic Clustering**: Complex systems cluster in Pacific Northwest and Southeast

## 3. Biblical Source Language Systems

### 3.1 Ancient Greek Demonstratives

#### 3.1.1 Three-Way System

Ancient Greek has three demonstrative pronouns:

| Demonstrative | Proximal Value | Typical Translation | Phonetic |
|--------------|----------------|---------------------|----------|
| **ὅδε** | Immediate proximal | "this here" (very close) | hóde |
| **οὗτος** | Proximal | "this" (near/present) | hoûtos |
| **ἐκεῖνος** | Distal | "that" (remote) | ekeînos |

#### 3.1.2 Semantic Distinctions

**ὅδε (hóde)** - Immediate/Deictic
- **Spatial**: "this right here" (immediately present)
- **Discourse**: Often used to introduce what follows (cataphoric)
- **Emphasis**: Highlights immediacy or presence
- **Usage**: Less common in Koine Greek, more common in Classical

**οὗτος (hoûtos)** - Proximal/Anaphoric
- **Spatial**: "this" (present, near, or immediate in thought)
- **Discourse**: Typically refers back to what was just mentioned (anaphoric)
- **Thematic**: Often marks thematically central or "near" entities
- **Pragmatic**: Can create near/far distinction to differentiate thematic importance
- **Usage**: Most common demonstrative in New Testament

**ἐκεῖνος (ekeînos)** - Distal/Remote
- **Spatial**: "that" (farther away in space, time, or thought)
- **Discourse**: Refers to something less immediate or beyond present situation
- **Thematic**: Marks thematically peripheral or "far" entities
- **Temporal**: Often used for past events or future remote events
- **Usage**: Common in narrative for shifting reference

#### 3.1.3 Usage Patterns in New Testament

**Spatial Deixis** (Physical Location):
- οὗτος: Objects/persons present or near speaker
- ἐκεῖνος: Objects/persons absent or far from speaker

**Temporal Deixis** (Time Reference):
- οὗτος: "this present time," "this generation," "this day"
- ἐκεῖνος: "that day" (often eschatological), "at that time"

**Discourse Deixis** (Textual Reference):
- οὗτος: Recently mentioned entity (anaphoric)
- ἐκεῖνος: Earlier mentioned entity or shift to different participant
- Creates contrast: "this one" (near in discourse) vs "that one" (far in discourse)

**Example**: John 1:29
- "Behold the Lamb of God" - Is Jesus near John? Near audience? Visible but distant?
- Greek uses demonstrative to position Jesus spatially for narrative purposes

#### 3.1.4 TBTA Mapping for Greek

**Recommended TBTA Encoding:**
- ὅδε → `N` (Near Speaker and Listener) or `S` (Near Speaker)
- οὗτος → `N` (Near Speaker and Listener), `C` (Contextually Near with Focus), or `c` (Contextually Near)
- ἐκεῖνος → `R` (Remote within Sight) or `t` (Temporally Remote) depending on context

### 3.2 Biblical Hebrew Demonstratives

#### 3.2.1 System Overview

Biblical Hebrew demonstrative system is more complex than simple spatial deixis:

**Primary Demonstrative: זֶה Paradigm**
| Form | Gloss | Gender/Number |
|------|-------|---------------|
| זֶה | zeh | Masculine Singular |
| זֹאת | zo't | Feminine Singular |
| אֵלֶּה | 'elleh | Common Plural |

**Key Finding**: זֶה paradigm is **unmarked for distance** - used for both near and far referents

**Secondary Forms: הוּא Paradigm**
| Form | Gloss | Gender/Number |
|------|-------|---------------|
| הוּא | hu' | Masculine Singular |
| הִיא | hi' | Feminine Singular |
| הֵם / הֵמָּה | hem/hemmah | Masculine Plural |
| הֵן / הֵנָּה | hen/hennah | Feminine Plural |

**Key Finding**: הוּא paradigm is **NOT primarily spatial** - functions as anaphoric pronoun and for recognitional reference, not true demonstrative

**Medial Deixis Forms: הַלָּז Paradigm** (rare)
| Form | Gloss | Usage |
|------|-------|-------|
| הַלָּז | hallaz | "that (at a distance)" |
| הַלָּזֶה | hallazeh | "that one" |
| הַלָּזוּ | hallazu | "those" |

**Function**: Indicates observable referents at some distance (medial deixis)

#### 3.2.2 Functional Analysis

**זֶה (zeh) - Neutral Demonstrative**
- **Distance**: Unmarked (both proximal and distal uses)
- **Spatial**: Can refer to near or far entities
- **Discourse Functions**:
  - Recognitional demonstrative ("this you know")
  - Cataphoric (pointing forward): "this is what..."
  - Anaphoric (pointing back): "this thing mentioned"
  - Emphatic in discourse

**הוּא (hu') - Anaphoric Pronoun**
- **NOT a spatial demonstrative** (common misconception)
- **Primary Functions**:
  - Third-person pronoun ("he," "she," "it")
  - Anaphoric reference (referring back)
  - Recognitional function
  - Copular use ("X is Y")
- **Distance**: No inherent spatial deixis

**הַלָּז (hallaz) - Medial Demonstrative** (rare)
- **Distance**: Medial (observable but at distance)
- **Spatial**: Requires some distance from speaker
- **Usage**: Sporadic in Biblical Hebrew
- **Function**: True spatial demonstrative for distant observable referents

#### 3.2.3 Discourse Deixis in Hebrew

Hebrew demonstratives function heavily in **discourse organization**:

**Emphatic/Focus Function** (Ezekiel 5:5):
- זֹאת as subject marks emphasis and deixis
- Creates discourse prominence for Jerusalem

**Cataphoric Function** (Introducing New Information):
- זֹאת introducing direct speech or new content
- "This is what..." constructions

**Anaphoric Function** (Referring Back):
- Both זֶה and הוּא for backward reference
- זֶה often for recently mentioned entities

**Recognitional Function**:
- "This X" where X is assumed known to hearer
- Presupposes shared knowledge

#### 3.2.4 TBTA Mapping for Hebrew

**Recommended TBTA Encoding:**

Since Hebrew זֶה is unmarked for distance, encoding must rely on **context**:

**Spatial Context:**
- Near referent: `N` (Near Speaker and Listener) or `S` (Near Speaker)
- Far referent: `R` (Remote within Sight)
- Invisible referent: `r` (Remote out of Sight)

**Temporal Context:**
- "This day" (present): `T` (Temporally Near)
- "That day" (past/future): `t` (Temporally Remote)

**Discourse Context:**
- Cataphoric/anaphoric with focus: `C` (Contextually Near with Focus)
- Routine discourse reference: `c` (Contextually Near)

**הוּא (hu') encoding:**
- Anaphoric use: `c` (Contextually Near) or `n` (Not Applicable)
- NOT spatial proximity unless context clearly spatial

**הַלָּז (hallaz) encoding:**
- Always: `R` (Remote within Sight) - true medial spatial demonstrative

#### 3.2.5 Hebrew vs Greek Comparison

| Feature | Hebrew | Greek |
|---------|--------|-------|
| **Basic System** | Unmarked for distance | 3-way distance distinction |
| **Primary Demonstrative** | זֶה (neutral) | οὗτος (proximal), ἐκεῖνος (distal) |
| **Spatial Encoding** | Context-dependent | Inherent in forms |
| **Discourse Function** | Very prominent | Prominent (especially οὗτος) |
| **Rare Forms** | הַלָּז (medial) | ὅδε (immediate) |
| **Anaphora** | זֶה and הוּא both used | οὗτος primary, ἐκεῖνος for remote |

**Translation Implication**: Greek spatial distinctions may need to be inferred for Hebrew, since Hebrew doesn't encode them lexically in the same way.

## 4. Methodology for Reproducing TBTA Proximity Decisions

### 4.1 Analysis Framework

To reproduce TBTA's proximity annotations, follow this decision tree:

#### Step 1: Identify Demonstrative Context

**Question**: Does the noun have demonstrative/deictic features in source text?

**Check for:**
- Greek demonstratives (ὅδε, οὗτος, ἐκεῖνος)
- Hebrew demonstratives (זֶה, זֹאת, אֵלֶּה, הַלָּז)
- Demonstrative modifiers or determiners
- Deictic adverbs (here, there, now, then)
- Contextual spatial/temporal reference

**If NO**: Code as `n` (Not Applicable)
**If YES**: Proceed to Step 2

#### Step 2: Determine Proximity Type

**Question**: What type of proximity is being marked?

**A. Spatial (Physical Location)**
- Are participants physically present in narrative?
- Is location relative to speaker/hearer specified?
- Is visibility mentioned or implied?
→ Proceed to 4.2 (Spatial Proximity)

**B. Temporal (Time Reference)**
- Does demonstrative refer to time ("this day," "that time")?
- Is temporal distance from narrative "now" relevant?
→ Proceed to 4.3 (Temporal Proximity)

**C. Discourse (Textual Reference)**
- Is demonstrative pointing to discourse entities?
- Is reference anaphoric (back) or cataphoric (forward)?
- Is emphasis/focus involved?
→ Proceed to 4.4 (Discourse Proximity)

### 4.2 Spatial Proximity Decision Tree

```
Is referent physically present in the narrative scene?
│
├─ YES → Is it near both speaker and listener?
│        │
│        ├─ YES → Code: N (Near Speaker and Listener)
│        │
│        └─ NO → Is it near speaker specifically?
│                 │
│                 ├─ YES → Code: S (Near Speaker)
│                 │
│                 └─ NO → Is it near listener specifically?
│                          │
│                          ├─ YES → Code: L (Near Listener)
│                          │
│                          └─ NO → Is it visible to participants?
│                                   │
│                                   ├─ YES → Code: R (Remote within Sight)
│                                   │
│                                   └─ NO → Code: r (Remote out of Sight)
│
└─ NO → Is referent being discussed but not present?
         │
         └─ YES → Code: r (Remote out of Sight) OR use discourse proximity
```

**Greek Source Text Mapping:**
- ὅδε → `N` or `S` (immediate presence)
- οὗτος → `N` (present scene) or discourse codes
- ἐκεῖνος → `R` (visible but distant) or `r` (absent/invisible)

**Hebrew Source Text Mapping:**
- זֶה → Context-dependent: `N`, `S`, `R`, or discourse
- הַלָּז → `R` (observable at distance)

### 4.3 Temporal Proximity Decision Tree

```
Does demonstrative refer to a time period?
│
└─ YES → Is time period close to narrative "now" or deictic center?
          │
          ├─ YES → Recent, immediate, "this day/time"
          │        → Code: T (Temporally Near)
          │
          └─ NO → Past/future, "that day/time," remote
                   → Code: t (Temporally Remote)
```

**Examples:**
- "This generation" (present time) → `T`
- "In that day" (eschatological future) → `t`
- "This very hour" (immediate) → `T`
- "In those days" (remote past) → `t`

**Greek Indicators:**
- οὗτος ὁ αἰών ("this age") → `T`
- ἐκείνῃ τῇ ἡμέρᾳ ("that day") → `t`

**Hebrew Indicators:**
- הַיּוֹם הַזֶּה ("this day") → `T`
- בַּיּוֹם הַהוּא ("in that day") → `t`

### 4.4 Discourse Proximity Decision Tree

```
Is demonstrative referring to entities/propositions in the discourse?
│
└─ YES → Is there emphatic focus or highlighting?
          │
          ├─ YES → Recently mentioned with emphasis
          │        → Code: C (Contextually Near with Focus)
          │
          └─ NO → Routine discourse reference
                   │
                   ├─ Anaphoric (refers back to recent mention)
                   │  → Code: c (Contextually Near)
                   │
                   └─ Remote reference (earlier in discourse)
                      → Code: c (Contextually Near)
```

**Greek Indicators:**
- οὗτος ὁ λόγος ("this word/message" - recently stated) → `C` or `c`
- Anaphoric οὗτος referring to previous participant → `c`
- ἐκεῖνος shifting to remote discourse participant → May still be `c` or coded spatially

**Hebrew Indicators:**
- זֹאת as emphatic subject (Ezek 5:5) → `C`
- זֶה in "this is what..." constructions → `C`
- Anaphoric זֶה or הוּא → `c`

### 4.5 Edge Cases and Special Situations

#### Case 1: Ambiguous Demonstratives

**Situation**: Greek οὗτος or Hebrew זֶה could be spatial or discourse

**Solution**: Prioritize discourse function if:
- No physical scene described
- Entity is abstract or propositional
- Clear anaphoric/cataphoric function

**Otherwise**: Use spatial proximity based on context

#### Case 2: Multiple Simultaneous Functions

**Situation**: Demonstrative serves both spatial and discourse functions

**Example**: "This man" - referring to Jesus present in scene but also prominent in discourse

**Solution**: Prioritize **physical presence** if narrative describes scene:
- Use `N`, `S`, `L`, `R`, or `r` for physical proximity
- Discourse function is secondary

**Exception**: If physical location is indeterminate but discourse function clear:
- Use `C` or `c`

#### Case 3: Abstract Referents

**Situation**: "This righteousness," "that hope," "these things"

**Solution**:
- **Abstract concepts** with demonstrative → Use discourse proximity (`C` or `c`)
- **Abstract concepts** with temporal frame → May use temporal proximity (`T` or `t`)
- Not spatial

#### Case 4: Quoted Speech

**Situation**: Demonstrative in quoted speech must reflect speaker's perspective

**Solution**:
- Encode proximity from **speaker's point of view**
- If speaker says "this man" while pointing → `N` or `S`
- If speaker refers to absent person → `r` or discourse

#### Case 5: Hebrew זֶה Ambiguity

**Situation**: Hebrew זֶה unmarked for distance

**Solution**: Analyze **context clues**:
- Physical scene description → Infer spatial proximity
- Temporal frame → Use temporal codes
- Discourse prominence → Use discourse codes
- Uncertain → Default to `c` (Contextually Near) for anaphoric use

### 4.6 Validation Against Source Languages

To ensure accurate TBTA proximity encoding:

**For Greek Texts:**
1. Identify demonstrative form (ὅδε/οὗτος/ἐκεῖνος)
2. Check for spatial indicators in context (here, there, present, absent)
3. Check for temporal frame (this time, that day)
4. Default anaphoric οὗτος → `c` or `C` (discourse)
5. Default distal ἐκεῖνος → `R` or `t` (spatial/temporal)

**For Hebrew Texts:**
1. Identify demonstrative (זֶה/הַלָּז) or הוּא in demonstrative function
2. Analyze narrative scene for spatial clues
3. Check for temporal markers (הַיּוֹם, בַּיּוֹם)
4. Check for discourse emphasis (subject position, cataphoric)
5. Default זֶה → `c` if ambiguous
6. הַלָּז → Always `R` (true spatial medial)

## 5. Cross-Linguistic Examples from Our 1009 Languages

### 5.1 Two-Way Systems (54.3% of languages)

**Pattern**: Proximal vs. Distal

**TBTA Encoding**: Uses `N`/`S` (proximal) vs `R`/`r` (distal)

**Example Languages in Dataset:**
- **English** (eng): this/that
- **Mandarin Chinese** (cmn): 这 zhè / 那 nà
- **Russian** (rus): этот etot / тот tot
- **Arabic** (arb): هذا hāḏā / ذلك ḏālika
- **Swahili** (swh): -a hapa / -a pale (with noun class agreement)

**Translation Strategy:**
- Biblical "this" → Target language proximal
- Biblical "that" → Target language distal
- TBTA codes N/S map to proximal
- TBTA codes R/r map to distal

### 5.2 Three-Way Person-Oriented Systems

**Pattern**: Near Speaker / Near Hearer / Away from Both

**TBTA Encoding**: Uses `S` (speaker), `L` (listener), `R` (remote)

**Example Languages in Dataset:**
- **Japanese** (jpn): これ kore / それ sore / あれ are
- **Korean** (kor): 이 i / 그 geu / 저 jeo
- **Spanish** (spa): este / ese / aquel
- **Tagalog** (tgl): ito / iyan / iyon

**Translation Strategy:**
- If Jesus near John speaking → `S` → Japanese これ kore
- If Jesus near audience → `L` → Japanese それ sore
- If Jesus far from all → `R` → Japanese あれ are

### 5.3 Three-Way Distance-Oriented Systems

**Pattern**: Near / Middle / Far (linear distance scale)

**TBTA Encoding**: Maps to `N`, `L`/`R`, `r`

**Example Languages:**
- Various languages in dataset may have this system

**Translation Strategy:**
- TBTA `N` → Proximal
- TBTA `L` or `R` → Medial
- TBTA `r` → Distal

### 5.4 Visibility-Based Systems

**Pattern**: Visible vs. Invisible (with or without distance distinctions)

**TBTA Encoding**: `R` (visible) vs `r` (invisible)

**Example Languages:**
- Potential Austronesian languages in dataset
- Some Trans-New Guinea languages

**Translation Strategy:**
- TBTA `N`, `S`, `L`, `R` → Visible demonstrative
- TBTA `r` → Invisible demonstrative
- Critical distinction for narratives with unseen participants

### 5.5 Elevation-Based Systems (Trans-New Guinea)

**Pattern**: Uphill / Downhill / Level (with distance distinctions)

**TBTA Encoding**: Maps to spatial proximity, elevation inferred from context

**Example Languages in Dataset:**
- **Yupno** (yut) - Finisterre-Huon
- **Kewapi/Kewapi** (kew, kjs) - Enga-Kewa-Huli
- **Tauya** (not in dataset) - Madang
- Many other TNG languages (129 total in dataset)

**Translation Strategy:**
- Biblical "go up to Jerusalem" → Uphill demonstrative/motion
- TBTA spatial codes + Hebrew עָלָה ('alah) → Uphill form
- Biblical "come down from mountain" → Downhill demonstrative/motion
- TBTA spatial codes + Hebrew יָרַד (yarad) → Downhill form

**Unique Feature**: Yupno uses uphill for FUTURE time, downhill for PAST time
- TBTA `T` (temporally near/future) → May map to uphill in Yupno
- TBTA `t` (temporally remote/past) → May map to downhill in Yupno

### 5.6 Noun Class Agreement Systems (Niger-Congo)

**Pattern**: Demonstratives agree with noun class (10-20 classes)

**TBTA Encoding**: Proximity separate from noun class; class marked elsewhere

**Example Languages in Dataset:**
- **Swahili** (swh): Proximal ha- + class / Distal class + -le
  - Class 1 (person sg): huyu / yule
  - Class 2 (person pl): hawa / wale
  - Class 5 (object): hili / lile
  - Class 7 (object): hiki / kile
- Many Bantu languages (86 in dataset)

**Translation Strategy:**
- TBTA proximity code → Choose proximal or distal form
- Noun class → Choose appropriate class agreement form
- Both operate independently

## 6. Patterns Identified in Our 1009 Languages

### 6.1 Dataset Language Family Distribution

From `languages.tsv`, our dataset includes:

**Major Families with Demonstrative Diversity:**
- **Niger-Congo**: 86 languages (esp. Bantu with noun class systems)
- **Trans-New Guinea**: 129 languages (elevation systems, 2-3 way distance)
- **Austronesian**: 182 languages (visibility distinctions, complex systems)
- **Indo-European**: ~100 languages (2-3 way systems)
- **Sino-Tibetan**: ~50 languages (2-way, some elevation)
- **Afro-Asiatic**: ~50 languages (2-3 way, Semitic and others)
- **Oto-Manguean**: ~30 languages (Mesoamerican diversity)
- **Many others**: Including Native American families, Australian, etc.

### 6.2 Expected Distance Distinction Patterns

Based on WALS typology applied to our dataset:

**Predicted Distribution:**
- **2-way systems**: ~540 languages (54%)
- **3-way systems**: ~376 languages (37%)
- **4+ way systems**: ~40 languages (4%)
- **Distance-neutral**: ~30 languages (3%)
- **Uncertain**: ~23 languages (insufficient data)

### 6.3 Special Features Expected

**Elevation Systems:**
- **Trans-New Guinea**: 129 languages
  - Concentrated in highlands: Enga, Chimbu, Ok, Finisterre-Huon families
  - Estimate: 50-80 languages with some elevation marking

**Visibility Distinctions:**
- **Austronesian**: 182 languages
  - Scattered across families, especially eastern Indonesia and Pacific
  - Estimate: 20-40 languages with visibility marking

**Noun Class Agreement:**
- **Niger-Congo (Bantu)**: 86 languages
  - Nearly all have noun class demonstrative agreement
  - Demonstrative paradigms: 2-3 distance × 10-20 classes = 20-60 forms per language

**Person-Oriented (vs. Distance-Oriented):**
- **East Asian**: Japanese, Korean, and languages influenced by them
- **Romance**: Spanish, Portuguese (some varieties)
- **Estimate**: 100-150 languages with person-oriented systems

### 6.4 Translation Challenges by Feature

**Highest Challenge Languages:**

**1. Complex Multi-Dimensional Systems**
- **Hawu** (Austronesian): 10 nominal demonstrative terms
- **Kewapi** (Trans-New Guinea): 13 demonstratives with elevation
- **Challenge**: TBTA 10 values may need compound coding

**2. Noun Class Agreement Systems**
- **Swahili and Bantu languages**: 86 languages in dataset
- **Challenge**: Single TBTA code expands to 10-20 surface forms

**3. Elevation-Based Systems**
- **Trans-New Guinea highlands**: ~50-80 languages estimated
- **Challenge**: Vertical dimension not explicitly in TBTA (inferred from context)

**4. Four-Way Systems**
- **Potentially in dataset**: Various Native American languages
- **Challenge**: TBTA spatial codes limited to 5 values (n, N, S, L, R, r)

### 6.5 Coverage Analysis: TBTA System Adequacy

**TBTA's 10-Value System Coverage:**

✅ **Well-Covered:**
- 2-way systems (54% of languages) - `N/S` vs `R/r`
- 3-way person-oriented (large portion of 37%) - `S`, `L`, `R`
- Temporal distinctions (universal need) - `T` vs `t`
- Discourse deixis (universal) - `C`, `c`
- Visibility (Austronesian, Amazonian) - `R` vs `r`

⚠️ **Partially Covered:**
- 3-way distance-oriented - Maps to `N`, `R`, `r` (but middle distance ambiguous)
- Elevation systems - Must infer from spatial codes + context
- Noun class agreement - Proximity separate from class (class marked elsewhere)

❌ **Gaps:**
- Four+ way systems - Only 5 spatial values (N, S, L, R, r)
- Complex multi-dimensional systems (Hawu 10 terms, Kewapi 13 terms) - Cannot fully encode
- Direction (toward/away) - Not explicitly marked

**Recommendation**: TBTA's system covers ~90% of cross-linguistic needs. Edge cases (4+ way, multi-dimensional) require:
- Compound encoding (multiple TBTA features)
- Language-specific extensions
- Contextual inference during translation

## 7. Sources Consulted

### 7.1 Typological and Cross-Linguistic Studies

**Diessel, Holst. 2013.** "Distance Contrasts in Demonstratives." In Matthew S. Dryer & Martin Haspelmath (eds.), *The World Atlas of Language Structures Online*. Leipzig: Max Planck Institute for Evolutionary Anthropology. https://wals.info/chapter/41
- **Key contribution**: Global typology of demonstrative distance systems
- 234 languages surveyed
- Geographic and genetic distribution patterns

**Levinson, Stephen C. 2018.** "Demonstratives: patterns in diversity." In Stephen C. Levinson, Sarah Cutfield, Michael Dunn, N. J. Enfield & Sergio Meira (eds.), *Demonstratives in cross-linguistic perspective*, 1-42. Cambridge: Cambridge University Press.
- **Key contribution**: Comprehensive cross-linguistic overview
- Patterns in diversity across families

**Imai, Shingo. 2003.** "Spatial deixis." PhD dissertation, SUNY Buffalo.
- **Key contribution**: Detailed analysis of spatial deictic systems

### 7.2 Discourse and Textual Deixis

**Acton, Eric K. & Christopher Potts. 2014.** "That straight talk: Sarah Palin and the sociolinguistics of demonstratives." *Journal of Sociolinguistics* 18(1): 3-31.
- **Key contribution**: Discourse functions of demonstratives

**Çakır, Hülya. 2014.** "Deixis: This and That in Written Narrative Discourse." *Discourse Processes* 51(3): 201-229.
- **Key contribution**: Research on "this" vs "that" in narrative sequences
- Text deixis and anaphora interaction
- Findings on adjacent vs. distant discourse reference

**Cornish, Francis. 2011.** "English demonstratives: Discourse deixis and anaphora. A discourse-pragmatic account." In Kerstin Fischer (ed.), *Approaches to Discourse Particles*, 147-166. Amsterdam: Elsevier.
- **Key contribution**: Demonstrative functions in discourse

### 7.3 Greek Demonstratives

**Anderson, Stephen R. & Edward L. Keenan. 1985.** "Deixis." In Timothy Shopen (ed.), *Language Typology and Syntactic Description, Vol. 3: Grammatical Categories and the Lexicon*, 259-308. Cambridge: Cambridge University Press.
- **Key contribution**: Greek three-term system classification

**Hasegawa, Yoko. 2012.** *The Routledge Course in Japanese Translation*. London: Routledge.
- **Key contribution**: Challenges Anderson & Keenan's distance-based interpretation of Japanese (and by extension Greek)

**Smyth, Herbert Weir. 1920.** *A Greek Grammar for Colleges*. New York: American Book Company.
- **Key contribution**: Classical description of ὅδε, οὗτος, ἐκεῖνος distinctions
- Available: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0007

**NT Discourse (website).** "Intro to near/far distinctions." 2008.
- https://www.ntdiscourse.org/2008/11/near_far_distinctions/
- **Key contribution**: Pragmatic analysis of Greek demonstratives in New Testament

### 7.4 Hebrew Demonstratives

**Van Hecke, Pierre. 2011.** "Biblical Hebrew הלוא זה\זאת\אלה and Medial Deixis Demonstratives." In Steven E. Fassberg & Avi Hurvitz (eds.), *Biblical Hebrew in Its Northwest Semitic Setting: Typological and Historical Perspectives*, 261-276. Winona Lake: Eisenbrauns.
- **Key contribution**: Analysis of medial deixis in Hebrew
- הַלָּז paradigm documentation

**Ehrenpreis, Roxanne. 2020.** "The Demonstrative זֹאת as Subject: Deixis and Emphasis in Ezekiel 5:5." Biblical Hebrew studies.
- https://biblicalhebrew.org/demonstrative-zot-as-subject-deixis-and-emphasis-in-ezekiel5-5.aspx
- **Key contribution**: Discourse-emphatic function of זֹאת

**Gesenius, Wilhelm & Emil Kautzsch. 1910.** *Gesenius' Hebrew Grammar*. Edited and translated by A. E. Cowley. Oxford: Clarendon Press.
- Section 34: "The Demonstrative Pronoun"
- https://en.wikisource.org/wiki/Gesenius'_Hebrew_Grammar/34._The_Demonstrative_Pronoun

### 7.5 Language-Specific and Regional Studies

**Cooperrider, Kensy, James Slotta & Rafael Núñez. 2017.** "Uphill and Downhill in a Flat World: The Conceptual Topography of the Yupno House." *Cognitive Science* 41: 768-799.
- **Key contribution**: Yupno elevation-based spatial system
- Temporal metaphors (uphill=future, downhill=past)

**Diana Forker. 2020.** "Elevation as a Grammatical and Semantic Category of Demonstratives." *Frontiers in Psychology* 11: 1712.
- **Key contribution**: Comprehensive survey of elevational demonstratives
- Trans-New Guinea and Trans-Himalayan examples
- https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01712/full

**Bowden, John & Sonja Riesberg. 2022.** "Cross-linguistic differences in demonstrative systems: Comparing spatial and non-spatial influences on demonstrative use in Ticuna and Dutch." *Journal of Pragmatics* 192: 144-161.
- **Key contribution**: Visibility distinctions in Amazonian Ticuna
- Experimental testing of spatial vs. non-spatial factors

**Post, Mark W. 2011.** "Topographical deixis in Trans-Himalayan (Sino-Tibetan) Languages." In Jan Wohlgemuth & Michael Cysouw (eds.), *Rethinking Universals: How rarities affect linguistic theory*, 205-246. Berlin: De Gruyter.
- **Key contribution**: Topographical deixis typology
- Trans-Himalayan patterns

### 7.6 TBTA Documentation

**AllTheWord.** TBTA Database Export. https://github.com/AllTheWord/tbta_db_export
- **Key contribution**: Primary data source for TBTA proximity encoding
- Semantic string position 8 for nouns
- 10-value proximity system documentation

**TBTA Export README.md**
- https://github.com/AllTheWord/tbta_db_export/blob/main/README.md
- **Key contribution**: Detailed field definitions including proximity

### 7.7 Additional References

**Wikipedia.** "Demonstrative." https://en.wikipedia.org/wiki/Demonstrative
- Overview of demonstrative systems

**Wikipedia.** "Deixis." https://en.wikipedia.org/wiki/Deixis
- General introduction to deictic categories

**Tofugu (Japanese learning website).** "Japanese Demonstratives: こそあど (Ko-So-A-Do)."
- https://www.tofugu.com/japanese-grammar/kosoado/
- Accessible explanation of Japanese system

**Ultimate Guide to Demonstratives in Biblical Languages.** Number Analytics blog.
- https://www.numberanalytics.com/blog/ultimate-guide-to-demonstratives-in-biblical-languages
- Popular-level overview

## 8. Conclusion and Summary

### 8.1 Key Findings

**TBTA's Proximity System**:
- **10-value encoding**: Captures spatial (5), temporal (2), and discourse (2) proximity plus N/A
- **Hybrid approach**: Combines person-oriented (S/L) and distance-oriented (R/r) distinctions
- **Visibility encoding**: Distinguishes visible (R) from invisible (r)
- **Coverage**: Adequate for ~90% of world's demonstrative systems

**Cross-Linguistic Typology**:
- **54.3%** of languages have 2-way systems → TBTA uses proximal vs. distal codes
- **37.6%** have 3-way systems → TBTA uses S/L/R or N/R/r combinations
- **4%** have 4+ way systems → TBTA may require compound encoding
- **Special features** (elevation, visibility, noun class) are accommodated or inferred

**Biblical Source Languages**:
- **Greek**: 3-way system (ὅδε/οὗτος/ἐκεῖνος) maps clearly to TBTA
- **Hebrew**: Unmarked system (זֶה) requires context-based TBTA encoding
- **Both**: Heavy discourse deixis function well-captured by TBTA C/c codes

**Language Family Patterns**:
- **Trans-New Guinea** (129 languages): Elevation systems, 2-3 way distance
- **Austronesian** (182 languages): Visibility distinctions, complex paradigms
- **Niger-Congo** (86 languages): Noun class agreement, 2-way distance core
- **Indo-European** (~100 languages): 2-3 way systems predominate

### 8.2 Reproduction Methodology Summary

To reproduce TBTA proximity annotations:

1. **Identify demonstrative context** in source text (Greek/Hebrew demonstratives, modifiers)
2. **Determine proximity type**: Spatial, temporal, or discourse
3. **Apply decision tree**:
   - Spatial → N/S/L/R/r based on speaker/hearer location and visibility
   - Temporal → T (near) vs t (remote)
   - Discourse → C (focus) vs c (routine)
4. **Map source language forms**:
   - Greek: ὅδε→N/S, οὗτος→N/C/c, ἐκεῖνος→R/t
   - Hebrew: זֶה→context-dependent, הַלָּז→R
5. **Validate** against narrative context and target language requirements

### 8.3 Translation Applications

**For Translators**:
- TBTA proximity codes guide choice among target language demonstrative forms
- 2-way systems: Use proximal for N/S/T/C, distal for R/r/t
- 3-way person-oriented: Map S/L/R directly to near-speaker/near-hearer/remote
- Visibility systems: Use R for visible, r for invisible forms
- Elevation systems: Infer from spatial codes + motion verbs

**For AI Systems**:
- TBTA codes provide explicit proximity values for ambiguous source texts
- Essential for generating natural demonstrative choices in target languages
- Prevents errors in complex systems (Japanese, Swahili, TNG languages)
- Grounds translation in analyzed spatial/temporal/discourse context

### 8.4 Future Research Directions

**Recommended Extensions**:
1. **Elevation coding**: Add explicit up/down/level distinction for TNG languages
2. **Direction coding**: Toward/away from deictic center
3. **Multi-value encoding**: Allow compound codes for 4+ way systems
4. **Noun class integration**: Link proximity to noun class for Niger-Congo
5. **Evidential interaction**: Study how demonstratives interact with evidentiality

**Dataset Analysis**:
- Survey all 1009 languages for demonstrative system types
- Create language-specific demonstrative profiles
- Build demonstrative choice decision trees per language family
- Test TBTA adequacy across full dataset

---

**Document Prepared**: 2025-11-05
**Research Scope**: TBTA proximity system, cross-linguistic demonstrative typology, Biblical Hebrew/Greek systems
**Languages Covered**: Typological patterns across 1009 languages in dataset
**Primary Sources**: WALS Chapter 41, TBTA export documentation, linguistic literature on demonstratives and spatial deixis
