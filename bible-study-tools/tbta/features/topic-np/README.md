# Topic NP: Discourse Topic Marking

**What**: Identifies which noun phrase is the discourse topic (what clause is "about"), distinct from grammatical subject.

---

## Quick Facts

| Feature | Value |
|---------|-------|
| **TBTA Tier** | A (Essential) |
| **Category** | 105 (Clause-level) | Position 4 |
| **Values** | A (Agent-like), P (Patient-like), N (No topic) |
| **Theological Stakes** | MINIMAL (95% arbitrary; 5% contextual emphasis) |
| **Critical Languages** | Japanese, Korean, Mandarin, Thai, Tagalog, Vietnamese |
| **Typology** | Li & Thompson (1976): Topic-prominent (25-30% of languages) |

---

## Language Target Audience

**Topic-Prominent Languages** (MANDATORY feature):
- **Japonic**: Japanese (wa/ga particles) ⭐
- **Sino-Tibetan**: Mandarin Chinese (positional topic-prominence)
- **Koreanic**: Korean (eun/neun particles) — *Not in database*
- **Austronesian**: Tagalog, Cebuano, Indonesian (voice alternation)
- **Other**: Thai, Vietnamese, Burmese

**Subject-Prominent Languages** (optional/emphatic only):
- English, Spanish, French, German — Use topic-fronting sparingly

See `/research/LANGUAGES.md` for detailed typology & candidate selection.

---

## Examples

| Context | Subject-Prominent | Topic-Prominent (Japanese) | Analysis |
|---------|------------------|---------------------------|----------|
| **Continuing Topic** | Jesus spoke... he said | イエスは語った(Iesu-wa katarata) | Jesus as topic → wa |
| **NEW Information** | God created heavens... | 神が天を創造した(Kami-**GA** ten-wo souzou) | God as NEW → **ga** |

---

## Theological Stance

**Mostly Arbitrary** (95%): Topic-marking affects discourse STYLE, not doctrine. "Jesus healed" = "Jesus (topic), he healed" → Same truth claim, different packaging.

**Non-Arbitrary Only**: Contrastive polemic, predicate constructions, narrative clarity (discourse only, not doctrine).

**Critical**: Topic-marking CANNOT cause heresy. Arianism, Modalism, Works-Righteousness are SEMANTIC errors, NOT topic-marking errors.

See `/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for Christian orthodox guidance.

---

## TBTA Encoding

**Schema**: Category 105, Position 4 (Clause-level)
**Values**: "Most Agent-like" | "Most Patient-like" | (absent for no topic)
**Gateway**: Part = "Clause" with overt noun phrase

See `/research/TBTA.md` for policy, constraints, edge cases.

---

**Stage 1 Research Complete**: See `/research/README.md` for synthesis of all findings. Ready for Stage 2 (Translation Database).
