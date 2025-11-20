# Topic NP (TBTA Category 105, Position 4)

**TIER A - HIGH PRIORITY**
**Last Updated:** 2025-11-07
**Location:** `Category 105 (Clauses), Position 4`
**Values:** `A` (Agent-like topic), `P` (Patient-like topic), `N` (No topic)

Topic NP identifies which noun phrase serves as the discourse topic (what the clause is "about"), distinct from grammatical subject. Critical for ~25% of world's languages that are topic-prominent.

**Target Audience:** Translators working with Japanese, Korean, Mandarin, Tagalog, and other topic-prominent languages.

---

## TIER 1: Translation Impact

Topic NP marking is **CRITICAL** for topic-prominent languages including Japanese (~125M speakers), Korean (~82M), Mandarin Chinese (~1.2B), and many Austronesian languages (Tagalog, Indonesian). In these languages:

- **Topic particles** are obligatory (Japanese wa/ga, Korean eun/neun, Mandarin 話說)
- **Word order** differs from subject-prominent languages (topic-fronting is unmarked/natural)
- **Information structure** explicitly marks given vs new information through topic-comment distinction

Without Topic NP annotation, translators must guess whether an entity is topic or subject, leading to unnatural or grammatically incorrect translations. The wa/ga distinction in Japanese alone can change meaning fundamentally.

---

## Complete Value Enumeration

| Value | Meaning | Frequency | Example |
|-------|---------|-----------|---------|
| **A** | Agent-like Topic | ~15-20% | "Jesus (TOPIC) said to them..." (John 8:12) |
| **P** | Patient-like Topic | ~10-15% | "That stone (TOPIC), the builders rejected" (Ps 118:22) |
| **N** | No explicit topic | ~70% | "God created the heavens" (Gen 1:1 - subject-predicate) |

**Note:** Topic ≠ Subject. A topic can be any fronted element about which the clause makes a statement. See TOPIC-VS-SUBJECT.md for detailed explanation.

**In TBTA data:** Values borrowed from semantic role system (A/P) to indicate whether topic is agent-like or patient-like. ~30% of clauses have explicit topic marking, higher in narrative genres.

---

## Baseline Statistics

**Corpus analysis (estimated from TBTA patterns):**

| Genre | Topic Marking Rate | Primary Pattern |
|-------|-------------------|-----------------|
| Narrative (Gospels, Acts) | ~35% | Topic continuity across clauses |
| Epistles (Teaching) | ~25% | Subject-predicate dominant |
| Prophetic/Poetry | ~40% | Contrastive topic-fronting |
| Legal (Leviticus) | ~15% | Generic/impersonal subjects |

**Topic continuity:** When same participant is topic across 3+ consecutive clauses, pro-drop languages typically use zero anaphora (Japanese ∅ wa, Korean ∅ eun).

**Cross-linguistic:** Topic-prominent languages: 25-30% of world's languages. Subject-prominent: 60-65%. Mixed systems: 10-15%.

---

## Quick Translator Test

**Determine if your language needs Topic NP annotations:**

1. **Does your language have topic particles?** (Japanese wa, Korean eun/neun, Mandarin 的話/huà)
2. **Is topic-comment structure different from subject-predicate?** (Can non-subjects be topics?)
3. **Can topics be fronted from any position?** (object → topic: "Fish, I ate")
4. **Are topics typically definite or generic?** (rather than indefinite)
5. **Do topics require special verb agreement?** (or lack agreement that subjects have)

**If YES to 2+ questions:** Topic NP is ESSENTIAL for your language.

---

## Concrete Verse Examples

### Example 1: Agent-like Topic (John 8:12)
```
Greek: Πάλιν οὖν αὐτοῖς ἐλάλησεν ὁ Ἰησοῦς
English (subject-prominent): "Again Jesus spoke to them"
Japanese (topic-prominent): "イエスは再び彼らに語られた"
                            Iesu-WA futatabi karera-ni katarareta
                            Jesus-TOPIC again them-to spoke
TBTA: Topic NP = A (Ἰησοῦς/Jesus)
```

**Why A:** Jesus is continuing topic from previous discourse. Restaging + Agent role.

---

### Example 2: Patient-like Topic (Psalm 118:22)
```
Hebrew: אֶבֶן מָאֲסוּ הַבּוֹנִים
English: "The stone that the builders rejected"
Japanese: "建てる者たちが捨てた石は"
         Tateru mono-tachi-ga suteta ishi-WA
         Build people-PL-SUBJ rejected stone-TOPIC
TBTA: Topic NP = P (אֶבֶן/stone)
```

**Why P:** Stone is fronted as topic (what the clause is "about"), but is Patient of "reject."

---

### Example 3: Topic ≠ Subject (Matthew 5:3)
```
Greek: Μακάριοι οἱ πτωχοὶ τῷ πνεύματι
English: "Blessed are the poor in spirit"
Japanese: "心の貧しい人々は幸いです"
         Kokoro-no mazushii hitobito-WA shiawai desu
         Heart-GEN poor people-TOPIC blessed are
TBTA: Topic NP = P (οἱ πτωχοί/poor)
```

**Why P:** "Poor" are topic but are Patient/Experiencer of "blessed," not Agent. Predicate adjective construction.

---

### Example 4: No Topic Marking (Genesis 1:1)
```
Hebrew: בְּרֵאשִׁית בָּרָא אֱלֹהִים
English: "In the beginning, God created"
Japanese: "初めに神が創造された"
         Hajime-ni Kami-GA souzou sareta
         Beginning-at God-SUBJ created
TBTA: Topic NP = N (no topic)
```

**Why N:** "God" is subject (ga, not wa), new information in discourse. Not topic-comment structure.

---

### Example 5: Contrastive Topic (John 3:11)
```
Greek: ἡμεῖς λαλοῦμεν... καὶ τὴν μαρτυρίαν ἡμῶν οὐ λαμβάνετε
English: "We speak... but you do not receive our testimony"
Japanese: "私たちは語るが、あなたがたは私たちの証しを受け入れない"
         Watashitachi-WA kataru ga, anatagata-WA watashitachi-no akashi-WO ukeirenai
         We-TOPIC speak but, you-TOPIC we-GEN testimony-OBJ receive-not
TBTA: Topic NP = A for both "we" (Agent) and "you" (Agent of receive)
```

**Why A:** Both pronouns are contrastive topics (we vs you), both agents of their verbs. Marked with wa in Japanese, not ga.

---

## Gateway Features

**Strong Correlations with other TBTA features:**

| If Feature X = Value | Then Topic NP | Confidence |
|---------------------|---------------|------------|
| Participant Tracking = Restaging | = A or P | 70% |
| Semantic Role = A + Sentence-initial | = A | 80% |
| Surface Realization = Zero (pro-drop) + Previous Topic | = (continued) | 75% |
| Salience Band = Foreground | More likely topic | 60% |

**Inverse correlations:**
- If indefinite NP ("a man") → UNLIKELY topic (5%)
- If new participant (First Mention) → LESS likely topic immediately (15%)

---

## Quick Reference

### When to Mark Topic NP = A/P

**Mark as A (agent-like topic):**
- Restaging participant who is agent/subject
- Contrastive topic in agent role
- Generic statements about agent ("Lions hunt")

**Mark as P (patient-like topic):**
- Fronted patient/object ("Stone, builders rejected")
- Predicate constructions ("Blessed are the poor")
- Experiencers as topic

**Mark as N (no topic):**
- New information (presentational)
- No clear topic-comment structure
- Subject-predicate dominant

---

## Validation Approach

### Test Set: 100 clauses
- 50 from narrative (Gospels)
- 25 from teaching (Epistles)
- 25 from poetry (Psalms)

### Validation Method
Compare TBTA Topic NP values with Japanese/Korean/Mandarin translations:
- **Japanese:** wa (topic) vs ga (subject) particle usage
- **Korean:** eun/neun (topic) vs i/ga (subject) particle usage
- **Mandarin:** Topic-comment structure vs subject-predicate

### Expected Accuracy
- **75-85%** (discourse features are challenging)
- Higher in narrative (topic continuity)
- Lower in poetry (complex structures)

**Validation Rules:**
- ✅ If TBTA = A/P → Japanese should have wa (or zero wa in pro-drop)
- ✅ If TBTA = N → Japanese may have ga (subject) or no particle
- ❌ If Japanese wa appears → TBTA should not be N (mismatch)

---

## Related Features

**Integration with TBTA features:**

1. **Participant Tracking** (Nouns, Pos 6): Restaging → often Topic
2. **Surface Realization** (Nouns, Pos 3): Topic continuity → zero allowed
3. **Semantic Role** (NP, Pos 3): Topic inherits A/P from semantic role
4. **Salience Band** (Cat 105, Pos X): Foreground → more topic marking

---

## Documentation Structure

**This directory contains:**

1. **README.md** (this file) - Overview with TIER 1 elements, quick reference
2. **DETAILED-METHODOLOGY.md** - TIER 2 hierarchical prompt, gateway features, common errors
3. **TOPIC-PROMINENT-LANGUAGES.md** - Language-specific patterns (Japanese, Korean, Mandarin, Tagalog, etc.)
4. **TOPIC-VS-SUBJECT.md** - Theoretical distinction, Li & Thompson typology, Lambrecht information structure

**Start here:** Use Quick Translator Test to determine if Topic NP is relevant for your language. If YES, read TOPIC-PROMINENT-LANGUAGES.md for language-specific rules.

---

## Summary

**What is Topic NP?** The noun phrase that serves as discourse topic (what the clause is "about"), marked in TBTA Category 105, Position 4 as A (agent-like) or P (patient-like).

**Why critical?** ~25% of world's languages (1.5B+ speakers) are topic-prominent and require topic marking for grammatical, natural translation.

**Key insight:** Topic ≠ Subject. Patients and objects can be topics. Discourse context determines topic, not just syntax.

**Accuracy:** 75-85% predictable from Participant Tracking, syntactic position, and information structure.

**Languages:** ESSENTIAL for Japanese, Korean, Mandarin, Tagalog, Indonesian. HELPFUL for all languages (topic-fronting for emphasis).
