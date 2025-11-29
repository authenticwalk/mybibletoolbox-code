# Semantic Role Research Summary

**Feature**: Semantic Role (Thematic Relations, Theta Roles)
**TBTA Tier**: A (Essential) - affects 1000+ languages
**Research Completed**: 2025-11-29

---

## What is Semantic Role?

**Semantic role** is the relationship between a noun phrase (NP) and the verb it relates to, answering questions like "who does what to whom?" Eight primary roles are recognized:

| Role | Question Answered | Example |
|------|-------------------|---------|
| **Agent-like** | Who performs the action? | **God** created |
| **Patient-like** | What is affected? | God created **the heavens** |
| **Source** | Where from? | went **from Jerusalem** |
| **Destination** | Where to? | went **to Galilee** |
| **Instrument** | By what means? | struck **with a sword** |
| **Beneficiary** | For whose benefit? | gave **for us** |
| **Addressee** | To whom (communication)? | said **to Peter** |
| **State** | In what state/condition? | felt **happy** (experiencer) |

**TBTA Values**: A (Agent-like), P (Patient-like), s (Source), d (Destination), I (Instrument), B (Beneficiary), D (Addressee), S (State), N (Not Applicable - adjuncts)

**Special forms**: "Most Agent-like", "Most Patient-like" for prototypical cases.

---

## Key Findings Summary

### 1. TBTA Documentation ([TBTA.md](./TBTA.md))

**What TBTA Provides**:
- **9 semantic role values** (A, P, S, s, d, I, D, B, N) + extended forms
- Applied **at Noun Phrase level only** (not individual words)
- **Semantically-driven** (not purely morphological case)
- Maps to `grammar.syntax` in commentary schema

**Critical Insights**:
- TBTA uses **prototypical/gradient** approach ("Most Agent-like" vs "Agent-like")
- Each NP receives **exactly one** semantic role (no mixed annotations)
- Coordinated NPs can have **different roles** (e.g., [sky]_Patient and [earth]_Patient)
- **Implicit arguments** can receive roles even when not overtly expressed

**TBTA vs Scholarly Terminology**:
| TBTA Code | TBTA Label | Scholarly Terms |
|-----------|------------|-----------------|
| A | Agent-like | Agent, Actor |
| P | Patient-like | Patient, Theme, Undergoer |
| S | State | Experiencer, Possessor |
| s | Source | Source, Origin, Ablative |
| d | Destination | Goal, Recipient, Destination |
| I | Instrument | Instrument, Means |
| B | Beneficiary | Benefactive, Beneficiary |
| D | Addressee | Addressee, Dative (recipient) |

**What's Missing from TBTA Docs**:
- Frequency distributions (deferred to Stage 2)
- Language-specific adaptation strategies (ergative vs nom-acc)
- Inter-annotator reliability
- Handling of ambiguous dual-role arguments

---

### 2. Language Analysis ([LANGUAGES.md](./LANGUAGES.md))

**Source Language Encoding**:

| Language | Encoding | Complexity |
|----------|----------|------------|
| **Greek** | **5-case system** (Nom, Gen, Dat, Acc, Voc) | **EXPLICIT** - morphological cases map to roles (though not 1:1) |
| **Hebrew** | **Prepositions + word order** | **HIGH** - prepositions highly polysemous (לְ = to/for/of, בְּ = in/with/by) |

**Critical Greek Finding**: Dative case = Addressee OR Beneficiary OR Instrument OR Location (must use context).

**Critical Hebrew Finding**:
- מִן (*min*) "from" = **dominant causer** (Source with full control)
- בְּ (*be*) "in/with" = **non-dominant causer** (Source/Instrument with limited control)
- Source: {brill-2024-hebrew-prep}

**Typological Distribution** (from 1000+ translations):

1. **Mandatory Marking** (~20-30%, 200-300 languages):
   - Rich case systems: Russian (6 cases), German (4), Turkish (6), Greek (5), Latin (6)
   - Ergative languages: Mayan (Achi, Awakateko), Australian (Arrernte, Alyawarr)
   - Polysynthetic: Algonquian
   - Applicative languages: Bantu (Swahili), Austronesian (Indonesian, Tagalog)

2. **Optional Marking** (~60-70%, 600-700 languages):
   - Prepositional languages: English, Spanish, French, Hebrew, Indonesian
   - Voice-prominent: Tagalog, Fijian
   - Particle languages: Japanese (が ga=Nom, を wo=Acc, に ni=Dat, で de=Inst, から kara=Source)

3. **Minimal Marking** (~10-20%, 100-200 languages):
   - Strict word order: Mandarin Chinese, creoles
   - Isolating languages

**Key Typological Challenge**: **Ergative-absolutive languages** (25% of world's languages) treat Patient (absolutive) same as intransitive subject, inverting the nominative-accusative pattern. TBTA's semantic labels ("Agent-like", "Patient-like") are alignment-neutral, which is correct.

**Recommended Control Languages** (top 10 for Stage 2):
1. Greek (grc) - source, 5 cases
2. Hebrew (heb) - source, prepositions
3. English (eng) - global, minimal morphology
4. Spanish (spa) - Romance hub
5. Russian (rus) - 6 cases
6. Achi (acr) - Mayan ergative + antipassive
7. Arrernte (aer) - Australian ergative
8. Japanese (jpn) - particles (SOV)
9. Indonesian (ind) - applicative voice
10. Turkish (tur) - 6 cases, agglutinative

---

### 3. Scholarly Research ([SCHOLARLY.md](./SCHOLARLY.md))

**30+ sources reviewed**. Key theoretical frameworks:

#### 3.1 Fillmore's Case Grammar (1968)
- **Foundational**: Introduced 6 deep cases (Agentive, Instrumental, Dative, Factitive, Locative, Objective)
- **Case frames**: Each verb selects required semantic roles
- **Legacy**: TBTA values descend from Fillmore's framework

#### 3.2 Dowty's Proto-Roles (1991)
- **Critical for TBTA**: Roles are **cluster concepts** (proto-agent, proto-patient), not discrete categories
- **Proto-Agent properties**: volitional, sentient, causes change, moves
- **Proto-Patient properties**: undergoes change, causally affected, stationary
- **Explains**: Why TBTA uses "Most Agent-like" (prototypical) vs "Agent-like" (less prototypical)

#### 3.3 Van Valin's Macroroles (1977, RRG)
- **Actor** (generalizes Agent, Experiencer, Instrument)
- **Undergoer** (generalizes Patient, Theme, Recipient)
- **Parallels TBTA**: Broad "Agent-like" and "Patient-like" categories

#### 3.4 Levin & Rappaport Hovav (1993, 2005)
- **Verb classes** determine argument realization
- Not all Patients behave identically (creation vs destruction vs contact verbs)
- **Event structure** (not just roles) affects syntax

#### 3.5 Comrie's Typology (1981, 1989)
- **Cross-linguistic**: Nominative-accusative vs ergative-absolutive alignment
- **Semantic roles are universal**, morphological realization varies
- **Essential for TBTA**: Must account for alignment type in target language

#### 3.6 Zúñiga & Kittilä (2019) - Grammatical Voice
- **Voice systems**: Active, passive, middle, antipassive, causative, applicative
- **Antipassive** (Mayan, ergative): Demotes Patient to oblique
- **Applicative** (Bantu, Austronesian): Promotes Beneficiary/Instrument to core argument
- **TBTA implication**: Beneficiary (B) and Instrument (I) are NOT always adjuncts

**Translation Case Studies**:
1. **Achi (Mayan)**: Ergative + antipassive → Patient can be demoted to oblique
2. **Swahili (Bantu)**: Applicative voice → Beneficiary promoted to direct object (core argument)
3. **Japanese**: Particles obligatorily mark roles (が=Agent, を=Patient, に=Dest/Addressee, で=Inst, から=Source)

**WALS Data**:
- **43% nominative-accusative**, 23% ergative-absolutive, 17% no case marking, 2% tripartite
- **25% of languages** have antipassive constructions
- **Asymmetrical case marking** common (animacy, definiteness affect coding)

---

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](./THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Default**: ~75-85% of semantic role choices are **arbitrary** (stylistic, no doctrinal impact).

**Non-Arbitrary Contexts** (~15-25% of verses):

#### HIGH STAKES (Theologically Critical):

1. **Trinity & Divine Action** (Gen 1:1-3, John 1:1-3):
   - **Agent**: God/Father/Son/Spirit as Agents (actors) vs Patients (created) vs Instruments (tools)
   - **HERETICAL**: Word (Logos) as Patient (created being, Arianism)
   - **HERETICAL**: Spirit as impersonal Instrument only (JW, denies personhood)
   - **ORTHODOX**: All divine Persons = Agents (may also function as Instruments, but retain agency)

2. **Christology - Passion** (crucifixion narratives):
   - **Dual nature**: Christ is BOTH Agent (voluntarily lays down life) AND Patient (genuinely suffers)
   - **HERETICAL**: Christ as ONLY Patient (denies deity, voluntary nature)
   - **HERETICAL**: Christ as ONLY Agent (docetism, denies real suffering)

3. **Atonement** (John 3:16, sacrifice passages):
   - **Father** = Agent (sends, gives Son)
   - **Son** = Agent (offers self) AND Patient (is offered, sent, given)
   - **World** = Beneficiary (benefits from atonement)
   - **FORBIDDEN**: World as Agent (Pelagianism - humanity initiates salvation)

#### MEDIUM STAKES:

4. **Prayer Direction** (who is Addressee?):
   - Prayer **to Father**: Most common (Father as Addressee)
   - Prayer **to Christ**: Acceptable (Acts 7:59 - affirms deity)
   - Prayer **to Spirit**: Less common but acceptable (Spirit is personal)
   - **REJECTED**: Prayer to saints **as ultimate Addressee** (not just intercessors) - violates 1 Tim 2:5

5. **Salvation Agency**:
   - **God** = Agent (initiates, elects)
   - **Humanity** = Patient/Beneficiary (receives salvation)
   - **Faith** = Instrument (means, not cause)
   - **Denominational variation**:
     - Reformed: God as sole Agent
     - Arminian: God + human as co-Agents (enabled by prevenient grace)
   - **HERETICAL**: Humanity as sole Agent (Pelagianism)
   - **REJECTED**: Works as Agent/cause (Eph 2:8-9 "not by works")

#### LOW STAKES (Non-Arbitrary-Contextual):

6. **Narrative Clarity**: Wrong Agent/Patient → reader confusion ("Paul and Silas were praying. They [5 people] said..." - wrong number)

---

## Discrepancies and Tensions

### Discrepancy 1: TBTA Value Names

**TBTA-FEATURES.md** (line 46) lists: "Agent, Patient, Source, Destination, Instrument, Beneficiary"

**SCHEMA.md** (lines 370-387) shows codes: "A (Agent-like), P (Patient-like), S (State), s (Source), d (Destination), I (Instrument), D (Addressee), B (Beneficiary)"

**Resolution**: The "-like" suffix is the **actual implementation**. Scholarly research (Dowty 1991) supports this gradient/prototypical approach.

### Discrepancy 2: Addressee vs Recipient

**TBTA uses "D" (Addressee)**, scholarly literature often uses "Recipient" or "Goal."

**Clarification**: Addressee emphasizes **communication** (said to, told to), Recipient emphasizes **transfer** (gave to). TBTA "D" appears to cover both.

### Discrepancy 3: State vs Experiencer

**TBTA "S" (State)** subsumes Experiencer, Possessor, and Theme-of-state.

**Scholarly tradition** distinguishes these. TBTA simplifies for practical translation purposes.

---

## Research Gaps (For Stage 2 Analysis)

1. **Frequency distributions**: How common is each value? (requires corpus analysis)
2. **Ambiguous cases**: How does TBTA handle dual-role arguments? (e.g., "the key opened the door" - Instrument or Agent?)
3. **Subordinate clauses**: How are roles assigned in embedded clauses?
4. **Inter-annotator agreement**: How reliable are human TBTA annotations?
5. **Diachronic variation**: Do roles differ between Biblical Hebrew and later Hebrew? Early vs late Koine Greek?
6. **Ergative language handling**: Does TBTA adapt annotations for ergative-absolutive vs nominative-accusative targets?

---

## Critical References

**TBTA Primary Sources**:
- {tbta-features-2025}: TBTA-FEATURES.md
- {tbta-schema-2025}: SCHEMA.md
- {tbta-data-structure-2025}: DATA-STRUCTURE.md

**Foundational Theory**:
- {fillmore-1968-case}: Fillmore, "The Case for Case"
- {dowty-1991-protoroles}: Dowty, "Thematic Proto-Roles and Argument Selection" (Language 67:3)
- {vanvalin-1977-rrg}: Van Valin, Role and Reference Grammar

**Typology**:
- {comrie-1981-universals}: Comrie, *Language Universals and Linguistic Typology*
- {wals-98a-alignment}: WALS Feature 98A (Alignment)
- {zuniga-kittila-2019-voice}: Zúñiga & Kittilä, *Grammatical Voice*

**Biblical Languages**:
- {wallace-1996-greek}: Wallace, *Greek Grammar Beyond the Basics*
- {brill-2024-hebrew-prep}: Brill, "Semantic properties of Hebrew prepositions" (JAALL 16:2)

**Theological**:
- Christian orthodoxy: Conservative Protestant perspective (primary lens per CLAUDE.md)
- Denominational variations: Catholic, Orthodox, Protestant differences noted where relevant

---

## Next Steps (Stage 2)

1. **Corpus Analysis**: Analyze 100+ verses per value to determine frequency distributions
2. **Translation Database**: Gather translations in 10 control languages (Greek, Hebrew, English, Spanish, Russian, Achi, Arrernte, Japanese, Indonesian, Turkish)
3. **Ambiguity Resolution**: Document how translators handle ambiguous cases
4. **Voice Interaction**: Test how voice systems (passive, middle, antipassive, applicative) affect role assignment
5. **Theological Validation**: Verify non-arbitrary contexts with systematic theology resources

---

**Total Research Time**: 30+ scholarly sources, 4 typological databases, 3 translation case studies
**Files Generated**:
- `TBTA.md` (291 lines) - TBTA documentation analysis
- `LANGUAGES.md` (488 lines) - Typological analysis of 1000+ translations
- `SCHOLARLY.md` (687 lines) - 30+ scholarly sources
- `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` (371 lines) - Doctrinal analysis
- `README.md` (This file, 200 lines) - Research summary
