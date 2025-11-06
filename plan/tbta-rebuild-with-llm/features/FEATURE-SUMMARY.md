# TBTA Features: Quick Reference Summary

## Overview
This table provides a quick reference for all TBTA features. For detailed documentation, see individual feature directories.

## Feature Summary Table

| Category | Feature | Key Values | Critical For | Example Languages |
|----------|---------|------------|--------------|-------------------|
| **NOUN FEATURES** |||||
| Entity Tracking | NounListIndex | 1-9, A-Z, a-z | Pronoun resolution, switch-reference | Navajo, Kiowa, Many PNG languages |
| Number | Number | Singular, Dual, Trial, Paucal, Plural | Grammatical accuracy | Hawaiian, Maori, Samoan, Slovenian |
| Person | Person | 1st/2nd/3rd, Inclusive/Exclusive | "We" disambiguation | Tagalog, Malay, Fijian, Vietnamese |
| Discourse | Participant Tracking | First Mention, Routine, Exiting, Restaging | Information structure | Japanese, Korean, Bantu languages |
| Deixis | Proximity | Near Speaker/Listener, Remote, Temporal | Demonstrative selection | Japanese, Korean, Spanish, Tagalog |
| Negation | Polarity | Affirmative, Negative | Negative concord | Turkish, Finnish, Russian |
| Syntax | Surface Realization | Noun, Pronoun, Zero, Clitic | Pro-drop decisions | Spanish, Japanese, Italian |
| **VERB FEATURES** |||||
| Time | Time | Immediate/Today/Yesterday/Remote/Discourse | Temporal marking | Tagalog, Yagua, Kiksht, ChiBemba |
| Aspect | Aspect | Perfective, Imperfective, Progressive, Habitual | Aspectual accuracy | Russian, Polish, Mandarin, Arabic |
| Modality | Mood | Indicative, Imperative, Subjunctive, Obligation | Modal marking | Turkish, Japanese, Greek |
| Meaning | LexicalSense | A-Z (different senses) | Polysemy resolution | All languages |
| **CLAUSE FEATURES** |||||
| Speech Act | Illocutionary Force | Declarative, Interrogative, Imperative | Sentence particles | Japanese, Chinese, Korean |
| Demographics | Speaker/Listener | Age, Gender, Relationship, Attitude | Honorific selection | Japanese, Korean, Javanese, Thai |
| Genre | Discourse Genre | Narrative, Expository, Poetic, Legal | Register selection | All languages |
| Information | Topic NP | Agent-like, Patient-like | Topic marking | Japanese, Korean, Chinese, Tagalog |
| Prominence | Salience Band | Foreground, Background, Setting | Narrative structure | Bantu languages, many African |
| Questions | Rhetorical Question | Expects Yes/No, Equivalent Statement | Question particles | Various languages |
| Inference | Implicit Information | Situational, Cultural, Optional | Explicitation needs | High-context cultures |
| Syntax | Clause Type | Independent, Relative, Adverbial | Subordination strategy | All languages |
| **ADJECTIVE FEATURES** |||||
| Comparison | Degree | Comparative, Superlative, Excessive | Comparison marking | All languages |
| Position | Usage | Attributive, Predicative, Substantive | Form selection | German, Russian, Japanese |
| **ADPOSITION FEATURES** |||||
| Meaning | LexicalSense | A-Z (different senses) | Preposition selection | All languages |
| Relations | Special Types | Genitive, Kinship, Subgroup | Relationship marking | Languages with possession types |
| **PARTICLE FEATURES** |||||
| Discourse | Type | QuoteBegin/End, Focus, Topic | Discourse marking | Japanese, quotative languages |
| **CONJUNCTION FEATURES** |||||
| Meaning | LexicalSense | A-Z (different senses) | Conjunction selection | All languages |
| Optionality | Implicit | Yes, No | Zero-conjunction | Various languages |
| **PHRASE FEATURES** |||||
| Semantics | Semantic Role | Agent, Patient, Destination, Source | Case assignment | Ergative languages, Filipino |
| Syntax | Relativized | Yes, No | Relative strategy | Languages with resumptives |
| **DISCOURSE FEATURES** |||||
| Complexity | SemanticComplexityLevel | 1-4 (Simple to Complex) | Translation strategy | All languages |

## Most Critical Features by Language Family

### Austronesian/Pacific
1. **Number** (Dual/Trial/Paucal) - ESSENTIAL
2. **Person** (Inclusive/Exclusive) - ESSENTIAL
3. **Semantic Role** (Focus system) - ESSENTIAL
4. **Topic NP** - CRITICAL

### East Asian (Japanese, Korean, Chinese)
1. **Proximity** (3-way demonstratives) - ESSENTIAL
2. **Speaker Demographics** - ESSENTIAL
3. **Topic NP** - ESSENTIAL
4. **Participant Tracking** - CRITICAL
5. **Surface Realization** (Pro-drop) - CRITICAL

### Native American
1. **Person** (Inclusive/Exclusive) - ESSENTIAL
2. **Proximity** (4+ distinctions) - ESSENTIAL
3. **NounListIndex** (Switch-reference) - ESSENTIAL
4. **Participant Tracking** - CRITICAL

### African (Bantu)
1. **Participant Tracking** - ESSENTIAL
2. **Salience Band** - ESSENTIAL
3. **NounListIndex** (Agreement) - CRITICAL
4. **Time** (Degrees of past/future) - CRITICAL

### Slavic
1. **Aspect** - ESSENTIAL
2. **Semantic Role** (Case) - ESSENTIAL
3. **Degree** (Adjective forms) - CRITICAL

### South Asian
1. **Person** (Inclusive/Exclusive) - ESSENTIAL
2. **Speaker Demographics** (Honorifics) - ESSENTIAL
3. **Semantic Role** (Ergative) - CRITICAL

## Feature Frequency in Data

| High Frequency | Medium Frequency | Low Frequency |
|----------------|------------------|---------------|
| NounListIndex | Proximity | Quadrial Number |
| Number (Singular/Plural) | Speaker Demographics | Cessative Aspect |
| Person (1/2/3) | Rhetorical Question | Hortative Mood |
| Participant Tracking | Degree (Comparative) | Exclamative Force |
| Time (Present/Past) | Implicit Information | 4+ SemanticComplexity |
| Semantic Role | Salience Band | Remote Time values |
| LexicalSense | Surface Realization | |
| Illocutionary Force | | |

## Quick Decision Tree

```
Is target language...
├─ Pro-drop? → Check Surface Realization
├─ Has inclusive/exclusive? → Check Person carefully
├─ Has dual/trial? → Check Number carefully
├─ Has honorifics? → Check Speaker Demographics
├─ Topic-prominent? → Check Topic NP
├─ Has demonstrative distinctions? → Check Proximity
├─ Has switch-reference? → Check NounListIndex + Participant Tracking
├─ Ergative? → Check Semantic Role
└─ Has aspect? → Check Aspect carefully
```

## Integration Priority

1. **Always Check**: NounListIndex, Participant Tracking, LexicalSense
2. **Check for Ambiguity**: Person, Number, Semantic Role
3. **Check for Register**: Speaker Demographics, Discourse Genre, Illocutionary Force
4. **Check for Your Language**: Features specific to target language family

## Notes

- Not all features appear in every verse
- Features combine (e.g., Dual + First Inclusive = "we two including you")
- Context determines feature relevance
- Use with Macula for complete linguistic picture