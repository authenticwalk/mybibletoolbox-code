# TBTA Sample Data Files

This directory contains sample TBTA annotation files downloaded from the GitHub repository for analysis and experimentation.

## Downloaded Samples

### Genesis Chapter 1

| File | Verse | Size | Description |
|------|-------|------|-------------|
| genesis_001_001.json | Genesis 1:1 | 9.7K | "In the beginning God created the heavens and the earth" |
| genesis_001_002.json | Genesis 1:2 | 19K | "The earth was formless and empty..." |
| genesis_001_003.json | Genesis 1:3 | 8.2K | "Then God said, 'Let there be light'" |
| genesis_001_026.json | Genesis 1:26 | 38K | "Then God said, 'Let us make man in our image'" |
| genesis_001_027.json | Genesis 1:27 | 28K | "So God created man in his own image" |

### Genesis Chapter 2

| File | Verse | Size | Description |
|------|-------|------|-------------|
| genesis_002_001.json | Genesis 2:1 | 16K | "Thus the heavens and the earth were completed" |

### Genesis Chapter 3

| File | Verse | Size | Description |
|------|-------|------|-------------|
| genesis_003_019.json | Genesis 3:19 | 33K | "By the sweat of your brow you will eat your food" |

## Coverage Summary

- **Total files**: 7 valid samples
- **Book**: Genesis only
- **Chapters**: 1-3
- **Total size**: ~153 KB

## Notable Features in Samples

### Genesis 1:1
- Multiple vocabulary alternates (simple/complex)
- Coordinated noun phrases ("sky and earth")
- Historic Past tense with Inceptive aspect
- Participant tracking (God, sky, earth, beginning)

### Genesis 1:2
- Negative polarity ("earth had no form")
- Predicative adjectives ("formless and empty")
- Attributive adjective phrase ("deep water")
- Backgrounded salience band

### Genesis 1:3
- Embedded clause (quoted speech)
- Quote particles ("-QuoteBegin", "-QuoteEnd")
- Jussive illocutionary force ("Let there be")
- Speaker/Listener tracking (God speaking to God)

### Genesis 1:26
- Trial number (Trinity: "us")
- First person inclusive ("we")
- Complex embedded speech
- Future tense ("Let us make")

### Genesis 1:27
- Parallel structure (repetition of creation)
- Multiple clauses in one verse

### Genesis 2:1
- Completive aspect ("were completed")
- Discourse timeframe reference

### Genesis 3:19
- Complex sentence structure (large file size)
- Multiple embedded clauses

## Failed Downloads

These files returned 404 errors (not available in repository):

- john_003_016.json (John 3:16)
- ruth_003_017.json (Ruth 3:17)

**Note**: The TBTA database export currently covers only the early books of the Bible (Genesis through approximately the historical books). New Testament books like John are not yet available.



## Download More Samples

To download additional verses:

```bash
# Download Genesis 1:4
curl -o genesis_001_004.json https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_004_Genesis.json

# Download Genesis 1:5
curl -o genesis_001_005.json https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_005_Genesis.json

# Download entire Genesis Chapter 1 (verses 1-31)
for i in {1..31}; do
    verse=$(printf "%03d" $i)
    curl -o genesis_001_${verse}.json \
         https://raw.githubusercontent.com/AllTheWord/tbta_db_export/main/json/00_001_${verse}_Genesis.json
done
```

## Repository Information

**Source**: https://github.com/AllTheWord/tbta_db_export

**Format**: JSON (processed from Access database)

**File naming pattern**: `00_{chapter:03d}_{verse:03d}_{BookName}.json`

## References

- See **../README.md** for data structure overview
- See **../SCHEMA.md** for complete field definitions
- See **../examples.md** for annotated examples
