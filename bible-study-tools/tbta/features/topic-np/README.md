<<<<<<< HEAD
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
=======
# Topic NP

## Overview

This feature is under development as part of the TBTA (Translation-Based Text Analysis) project.

## Purpose

Topic NP (Noun Phrase) analyzes topic-prominent vs subject-prominent language features, including topic marking, focus structures, information structure, and how languages encode what is being talked about (topic) vs who/what performs the action (subject).

## Development Status

🚧 **Stage 0**: Not yet started

See [STAGES.md](../STAGES.md) for the complete 6-stage development methodology.

## Development Checklist

### Stage 1: Research TBTA Documentation
- [ ] Review official TBTA docs for this feature
- [ ] Review existing feature analysis (check `../features-archive/topic-np/`)
- [ ] Generate README.md with feature definition + stage checklist

### Stage 2: Language Study
- [ ] Identify which language families need this feature
- [ ] Determine where feature is grammatically obligatory vs optional
- [ ] Update README.md with language analysis + target scenarios

### Stage 3: Scholarly and Internet Research
- [ ] Find scholarly articles on this subject
- [ ] Research general web information
- [ ] Update README.md with latest findings

### Stage 4: Generate Test Set with Translation Data
- [ ] Philosophy: Discover answers from what real translators did
- [ ] Sample size: 100+ verses per value minimum
- [ ] Create translation database (5-10 representative translations)
- [ ] Generate dual outputs: answer sheets (TBTA) + question sheets (translations)
- [ ] Split: train (40%), test (30%), validate (30%)

### Stage 5: Analyze Translations & Develop Algorithm
- [ ] Translation discovery analysis (primary source)
- [ ] Create ANALYSIS.md (up to 12 approaches)
- [ ] Develop PROMPT1.md with locked predictions
- [ ] Systematic error analysis (6-step process)
- [ ] Iterative refinement (PROMPT2.md, PROMPT3.md, etc.)

### Stage 6: Test Against Validate Set & Peer Review
- [ ] Blind subagent validation
- [ ] 4 critical peer reviews (theological, linguistic, methodological, translation practitioner)
- [ ] Translation practitioner testing with 2-3 languages
- [ ] Production readiness verification

## Resources

- **Authoritative Methodology**: [STAGES.md](../STAGES.md)
- **Feature Template**: [TEMPLATE.md](../TEMPLATE.md)
- **Previous Work**: [features-archive/topic-np/](../features-archive/topic-np/)
>>>>>>> origin/feat/self-learning-tbta
