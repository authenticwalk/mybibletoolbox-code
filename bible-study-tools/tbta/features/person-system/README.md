# Person System

## Overview

This feature is under development as part of the TBTA (Translation-Based Text Analysis) project.

## Purpose

Person system identifies grammatical person distinctions (first person, second person, third person) and related features like inclusive vs exclusive first person plural, clusivity, and person agreement patterns.

## Development Status

🚧 **Stage 0**: Not yet started

See [STAGES.md](../STAGES.md) for the complete 6-stage development methodology.

## Development Checklist

### Stage 1: Research TBTA Documentation
- [ ] Review official TBTA docs for this feature
- [ ] Review existing feature analysis (check `../features-archive/person-system/`)
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
- **Previous Work**: [features-archive/person-system/](../features-archive/person-system/)
