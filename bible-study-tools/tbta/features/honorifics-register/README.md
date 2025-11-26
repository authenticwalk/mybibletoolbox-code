# Honorifics/Register (Speaker Demographics)

**Encodes grammatically required social relationships, status, age, formality, and respect marking through pronouns, verbs, vocabulary, and particles.**

## Quick Facts

| Aspect | Value |
|--------|-------|
| **Status** | ✅ Complete in TBTA |
| **Affects** | ~25% world languages (500+) |
| **Feature Type** | Clause-level, multi-dimensional |
| **Theological Stakes** | HIGH (divine address, Jesus relationships) |
| **Complexity Range** | Simple: None → Binary T/V → Multi-level (7+ forms) |

## Critical Languages by System Type

| Type | Languages | Mechanism | Encoding |
|------|-----------|-----------|----------|
| **Mandatory Multi-level** | Japanese, Korean, Thai, Javanese | Pronouns, verbs, vocabulary | 4-7 obligatory levels |
| **Mandatory Binary** | Hindi, Bengali | Pronouns + verb agreement | तू/तुम/आप (3 levels) |
| **Optional T/V** | Spanish, French, German, Russian | Binary pronouns | tú/usted distinction |
| **Lexical/Particle** | Vietnamese, Indonesian, Tagalog | Kinship terms, particles | Context-dependent |
| **Absent** | English, Swahili | No grammatical marking | Tone/vocabulary only |

## Sub-Features & Values

| Sub-Feature | Values | Status | Notes |
|-------------|--------|--------|-------|
| Speaker/Listener | Free text (identity) | ✅ | E.g., "God", "daughter", "Abraham" |
| Speaker_Age | Child, Young Adult, Adult, Elder | ✅ | TBTA complete; Bantu: age-specific kinship required |
| Speaker_Listener_Age | Older, Same, Younger | ✅ | Critical in honor-shame cultures (East/South Asia) |
| Speaker_Attitude | Neutral, Familiar, Polite, Honorable | ✅ | Japan: keigo system (teineigo/sonkeigo/kenjōgo) |
| Speech_Style | Informal, Formal | ✅ | Binary for most languages |
| **Gender** | ? | ❌ | **NOT DOCUMENTED** (Japanese: wa/ne vs. zo/na) |
| **Relationship** | ? | ❌ | **NOT DOCUMENTED** (TBTA mentions, no values) |

## Key Translation Challenges

### Challenge 1: Divine Address (Matthew 6:9 - Lord's Prayer)
- **Hebrew/Greek**: No formal/informal distinction
- **Japanese Translation**: Must choose—teineigo (polite) balances reverence + intimacy
- **Korean Translation**: Highest jondaemal (formal respect) emphasized
- **French Translation**: Modern: _tu_ (intimate); Traditional: _vous_ (reverent) ✅
- **⚠️ Doctrinal Stakes**: MEDIUM-HIGH—affects theology of prayer

### Challenge 2: Social Hierarchies (Luke 15:11-32 - Prodigal Son)
- **Father → Sons**: Paternal, respectful (teineigo in Japanese)
- **Sons → Father**: Filial, formal/humble (sonkeigo in Japanese)
- **Elder Son → Servants**: Commanding, familiar forms (kudaketa)
- **⚠️ Critical**: Master/servant register is ESSENTIAL to parable meaning

### Challenge 3: Bantu Age-Specific Kinship (Matthew 4:18 - Peter & Andrew)
- **Greek**: ἀδελφός (_adelphos_, age-neutral "brother")
- **Swahili/Bantu MUST choose**: _kaka mkubwa_ (older brother) OR _kaka mdogo_ (younger)
- **Problem**: Biblical source text ambiguous on age relationship
- **⚠️ Translator Decision Required**: Research or infer from context

## TBTA Encoding Structure

**Location**: `/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md` Section 5 "Speaker Demographics"

**Format**: Clause-level annotation in JSON/YAML
```
Speaker: "God"
Listener: "disciples"
Speaker_Age: "Elder"
Speaker_Listener_Age: "Older"
Speaker_Attitude: "Honorable"
Speech_Style: "Formal"
```

**Constraints**: Valid only for direct speech/dialogue clauses with identifiable participants.

---

**[→ Deep Research: see `research/README.md`]**
**[→ Language Analysis: see `research/LANGUAGES.md`]**
**[→ Scholarly Sources: see `research/SCHOLARLY.md` (37+ sources)]**
**[→ Theological Guidelines: see `research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`]**
