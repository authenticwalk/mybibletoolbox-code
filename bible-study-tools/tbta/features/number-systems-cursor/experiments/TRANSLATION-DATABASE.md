# Translation Database for Number-Systems Feature

## Selected Languages

### Trial-Marking Languages (Genesis 1:26 validation)

1. **Fijian (fij)**
   - **Family**: Austronesian, Oceanic, Central Pacific
   - **Number System**: Singular, Dual, Trial, Paucal, Plural
   - **Source**: Direct from English
   - **Availability**: eBible.org, Bible.com
   - **Priority**: HIGH (has all number distinctions we need)

2. **Hawaiian (haw)**
   - **Family**: Austronesian, Polynesian
   - **Number System**: Singular, Dual, Trial, Plural
   - **Source**: Direct from source texts
   - **Availability**: eBible.org
   - **Priority**: HIGH (natural trial usage)

3. **Tok Pisin (tpi)**
   - **Family**: Austronesian creole
   - **Number System**: Singular, Dual, Trial, Plural (pronouns only)
   - **Examples**: mitripela (we-three-exclusive), yumitripela (we-three-inclusive)
   - **Source**: Creole derived from English
   - **Availability**: eBible.org, Bible.com
   - **Priority**: MEDIUM (trial in pronouns, useful for Genesis 1:26)

### Dual-Marking Languages (Luke 24:13, Mark 6:7 validation)

4. **Samoan (smo)**
   - **Family**: Austronesian, Polynesian
   - **Number System**: Singular, Dual, Plural
   - **Examples**: lāua (they-two), tāua (we-two-inclusive), māua (we-two-exclusive)
   - **Source**: Direct from source texts
   - **Availability**: eBible.org, Bible.com
   - **Priority**: HIGH (clear dual marking)

5. **Slovenian (slv)**
   - **Family**: Indo-European, Slavic, South Slavic
   - **Number System**: Singular, Dual, Plural (OBLIGATORY)
   - **Examples**: hiša (one house), hiši (two houses), hiše (three+ houses)
   - **Source**: Dalmatinova Biblija (1583), modern translations
   - **Availability**: Bible.com
   - **Priority**: HIGH (only living IE language with obligatory dual)
   - **Note**: Dual is most distinctive feature of Slovenian

### Paucal-Marking Languages (Matthew 18:20 validation)

**Note**: Paucal-marking languages (Warlpiri, Australian languages) have limited Bible translation availability. If accessible, would be valuable for distinguishing paucal (2-5) from plural (many) contexts.

**Fallback**: Use contextual analysis in trial/dual languages to distinguish small group (paucal) from large assembly (plural).

## Translation Validation Strategy

### High-Confidence Verses (80%+ agreement expected)
- **Luke 24:13** "two of them" - Expect 100% dual marking (explicit count)
- **Genesis 19:1** "two angels" - Expect 100% dual marking (explicit count)
- **Mark 6:7** "two by two" - Expect 100% dual marking (explicit emphasis)

### Ambiguous/Theological Verses (mixed agreement expected)
- **Genesis 1:26** "Let us make" - Expect variation:
  - Trial languages may use trial (Trinity interpretation)
  - May use plural (divine council interpretation)
  - Document consensus and minority views

### Corporate Solidarity Verses (context-dependent)
- **Israel/Church references** - May be singular (collective) or plural (individuals)
- Expect variation based on translation philosophy
- Document patterns across translations

## Data Access

**eBible.org**: 
- API: https://ebible.org/Scriptures/
- Format: USFM files available for download
- Coverage: Excellent for Austronesian and Pacific languages

**Bible.com**:
- No public API (web scraping needed)
- Coverage: Broad, includes Slovenian

**Fallback**: If API access blocked, manually lookup key verses (Genesis 1:26, Luke 24:13, Matthew 18:20) in each translation using web interfaces.

## Next Steps

1. Check `.data/commentary/` directory for cached eBible translations
2. If not available, fetch from eBible.org API
3. For each verse in train/test/validate:
   - Lookup translation in each of 5 languages
   - Extract relevant text
   - Populate `*_questions.yaml` files
4. Analyze translation consensus patterns
5. Use as primary evidence for algorithm development (Stage 5)

---

**Last Updated**: 2025-11-17
**Status**: Translation selection complete, data fetching pending
