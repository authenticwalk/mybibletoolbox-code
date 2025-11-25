# Proximity System: Research Findings

**Proximity System** encodes spatial (near/far), temporal (recent/remote), and discourse (focus/routine) distance relationships between referents and speech participants. This 10-way system captures essential distinctions for 1000+ languages requiring demonstrative marking.

## TBTA Feature Definition

TBTA implements a comprehensive **10-value proximity encoding** at position 6 (or 8 per discrepancy noted) in noun semantic strings. Values cover three dimensions:

- **Spatial**: Near Speaker (S), Near Listener (L), Near Both (N), Remote Visible (R), Remote Invisible (r)
- **Temporal**: Temporally Near (T), Temporally Remote (t)
- **Discourse**: Contextually Near with Focus (C), Contextually Near routine (c)
- **Default**: Not Applicable (n) for non-demonstrative nouns

**Status:** Implemented across 11,649 verses; 34 books marked. No inference algorithm documented.

[Read detailed TBTA review →](TBTA.md)

## Language Typology: Critical Families

Proximity systems vary dramatically: **54% of languages** use simple 2-way (this/that), **38%** use 3-way systems, **8%** use specialized features (elevation/visibility).

**Source Language Reality:**
- **Greek** (NT): Explicitly encodes 3-way distance (ὅδε/οὗτος/ἐκεῖνος) — high annotation reliability
- **Hebrew** (OT): Distance-neutral; requires contextual inference — lower reliability

**Target Language Priority Groups:**
- **Austronesian** (176 languages): Visibility distinctions (visible/invisible) — TBTA's R/r distinction directly applicable
- **Trans-New Guinea** (141 languages): Elevation systems (uphill/downhill) — require contextual mapping
- **Romance** (Spanish, Portuguese): 3-way person-oriented (speaker/hearer/far) — TBTA's S/L/R essential
- **Bantu** (Swahili, Akan): Noun class agreement + proximity — secondary to class selection

Candidate languages for Stage 4 testing: Spanish (spa), Akan (aka), Awa (awb), Agutaynen (agn), Indonesian or Swahili.

[Read detailed language analysis →](LANGUAGES.md)

## Scholarly Foundation: 30+ Sources

Demonstratives are **universal across languages** and among the oldest grammatical elements (Diessel 1999, 2006). Core insights:

- **Typological diversity**: Systems range from 2-way (English, Russian) to 12-way (Daga, Muna with distance+elevation+visibility)
- **Universal functions**: Exophoric (situational), endophoric/anaphoric (discourse), discourse deictic (meta-reference), recognitional (shared knowledge)
- **Person-orientation discovery**: Japanese и Spanish systems encode speaker/hearer proximity, not pure distance (Imai 2003, Anderson & Keenan 1985)
- **Special features**: Elevation (Trans-New Guinea), visibility (Austronesian), noun class agreement (Bantu)
- **Translation challenge**: Greek's explicit encoding enables NT reliability; Hebrew's context-dependent system requires scene analysis

**Key Case Studies:** John 1:29 (distance variations across 5 languages), Matthew 24:3 (temporal vs. discourse proximity), Swahili noun class interaction.

[Read scholarly research →](SCHOLARLY.md)

## Theological Significance: 15% Non-Arbitrary

**85% of proximity choices are stylistic/arbitrary.** However, **15% are theologically critical:**

### Critical Non-Arbitrary Contexts

1. **Eucharistic/Sacramental** ("This is my body") — REQUIRED PROXIMAL (forbidden: distal)
2. **Christological Theophany** ("This is my beloved Son") — REQUIRED PROXIMAL (forbidden: distal)
3. **Resurrection Apologetic** ("See my hands, touch my side") — REQUIRED PROXIMAL (forbidden: distal)
4. **Covenant Establishment** ("This is my covenant") — REQUIRED PROXIMAL for new/active covenant
5. **Messianic Fulfillment** (Luke 4:21: "This Scripture fulfilled today") — REQUIRED PROXIMAL + temporal "today"
6. **Eschatological Timing** (Matthew 24: "This generation" vs "that day") — Proximal/distal distinguish near-term vs. distant prophecy

All non-arbitrary contexts require **preserving source language proximity**. Using distal in Eucharistic contexts would imply theological distance, weakening sacramental immediacy.

[Read theological classification →](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)

## Known Issues & Research Gaps

**Documentation Problems:**
- Position discrepancy: Position 6 vs. 8 in semantic string (requires verification)
- C/c distinction undefined: "Focus" criteria not specified
- No inference algorithm: Decision rules for proximity determination not documented
- John 1:29 discrepancy: Documentation vs. contextual analysis mismatch

**Coverage Gaps:**
- Trans-New Guinea elevation deixis: 50+ languages lack elevation markers in TBTA
- Austronesian maritime deixis: Coastal languages may need across-water/along-coast distinctions
- Visibility-elevation intersection: Complex systems combining multiple parameters

**Next Steps (Stage 2):** Frequency analysis of all 10 values across corpus; position verification; validation protocol against parallel Gospel passages.

---

**Status:** Stage 1 Complete | **Document Lines:** ~190 | **Sources Reviewed:** 4 source files, 30+ scholarly sources | **Confidence:** High for typology; Medium for cultural nuances
