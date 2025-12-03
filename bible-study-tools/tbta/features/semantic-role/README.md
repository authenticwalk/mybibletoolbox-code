# Semantic Role

**Who does what to whom?** - The fundamental question answered by semantic roles.

---

## Quick Facts

| Aspect | Details |
|--------|---------|
| **Feature Name** | Semantic Role (Thematic Relations, Theta Roles) |
| **TBTA Tier** | **A (Essential)** - affects 1000+ languages, cannot be easily inferred |
| **TBTA Values** | 8 values found in corpus (138,723 annotations): Most Agent-like (53.7%), Most Patient-like (26.5%), Destination (9.1%), State (7.5%), Source (1.3%), Beneficiary (0.7%), Addressee (0.7%), Instrument (0.5%) |
| **Special Forms** | "Most Agent-like", "Most Patient-like" (prototypical cases) |
| **Source Languages** | **Greek**: 5-case system (explicit) \| **Hebrew**: Prepositions (polysemous) |
| **Critical Languages** | Ergative (Mayan, Australian), Applicative (Bantu, Austronesian), Case-rich (Russian, German, Turkish, Japanese) |
| **Theological Stakes** | **HIGH** - Who acts in creation, atonement, prayer? Agent vs Patient in Christology |

---

## What Is It?

Semantic role describes the **relationship between a noun phrase and its verb**:
- **Agent**: Who performs? → God created
- **Patient**: What is affected? → created the heavens
- **Source**: From where? → from Jerusalem
- **Destination**: To where? → to Galilee
- **Instrument**: By what means? → with a sword
- **Beneficiary**: For whom? → for us
- **Addressee**: To whom (communication)? → said to Peter
- **State**: In what condition? → felt happy (experiencer)

---

## Why It Matters

### For 1000+ Languages
- **Mandatory** in 300+ languages: Rich case systems (Russian 6 cases, Turkish 6, Greek 5), ergative languages (Mayan, Australian), applicative languages (Bantu, Austronesian)
- **Optional** in 600+ languages: Prepositional (English, Spanish, Hebrew), particle (Japanese), voice-prominent (Tagalog)
- **Minimal** in 100+ languages: Strict word order (Mandarin, creoles)

### For Theology
**HIGH STAKES** contexts (5-10% of verses):
- ✅ **Trinity**: God/Father/Son/Spirit as **Agents** (creators), not Patients (created) or mere Instruments
- ✅ **Christology**: Christ is **both Agent** (willingly offers self) **and Patient** (genuinely suffers)
- ✅ **Atonement**: Father = Agent (sender), Son = Agent+Patient (offers self, is offered), World = Beneficiary
- ❌ **HERETICAL**: Word as Patient (Arianism - created being)
- ❌ **HERETICAL**: Christ as only Patient (denies deity) or only Agent (docetism - denies real suffering)

---

## Translation Challenges

| Challenge | Example | Solution |
|-----------|---------|----------|
| **Case → No-Case** | Greek dative (Addressee/Beneficiary/Instrument/Location) → English prepositions | Analyze verb semantics + context |
| **Prepositional Polysemy** | Hebrew לְ (to/for/of), בְּ (in/with/by) → multiple roles | Verb-specific frame knowledge |
| **Ergative Inversion** | Mayan: Patient=absolutive (like intransitive subject) | Semantic labels alignment-neutral |
| **Applicative Promotion** | Swahili: Beneficiary promoted to direct object | Recognize B/I as core arguments, not adjuncts |
| **Voice Permutations** | Passive, middle, antipassive change role-to-syntax mapping | Track voice system |

---

## Examples

### ✅ Correct: Genesis 1:1
- **God** = Most Agent-like (volitional creator)
- **heavens and earth** = Most Patient-like (created entities)

### ⚠️ Critical: John 1:3 "Through him all things were made"
- ✅ Orthodox: **Word** = Agent-like (with instrumental function) - preserves deity
- ❌ Heretical: **Word** = Patient-like (created first, then used) - Arianism

### ⚠️ Critical: John 3:16 "God so loved... he gave his Son"
- ✅ **Father** = Agent (initiator), **Son** = Agent (willing) + Patient (given), **World** = Beneficiary
- ❌ **FORBIDDEN**: World = Agent (initiating salvation) - Pelagianism

---

## TBTA Encoding

**Applies to**: Noun Phrases (NP) only
**Policy**: Semantically-driven (not purely morphological)
**Mapping**: `grammar.syntax` in commentary schema
**Coordination**: Each coordinated NP gets independent role
**Mixed annotations**: **NO** - one role per NP

See [research/TBTA.md](research/TBTA.md) for full technical details.

---

## Research Complete

- ✅ 30+ scholarly sources ([SCHOLARLY.md](research/SCHOLARLY.md))
- ✅ 1000+ language typology ([LANGUAGES.md](research/LANGUAGES.md))
- ✅ Theological analysis ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))
- ✅ TBTA documentation ([TBTA.md](research/TBTA.md))

**Next**: Stage 2 Analysis (100+ verses per value, 10 control languages)
