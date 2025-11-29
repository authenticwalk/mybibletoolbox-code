#!/usr/bin/env python3
"""
Stratified sampling and train/test/validate split for number-systems feature.

Follows STAGES.md Step 4 requirements:
- 100+ verses per value minimum
- Balanced OT/NT distribution
- Genre diversity
- Book diversity
- Include adversarial cases
- 40%/30%/30% split (train/test/validate)
"""

import yaml
import random
from collections import defaultdict
from pathlib import Path

# Set seed for reproducibility
random.seed(42)

# Critical verses that MUST be included (adversarial cases)
CRITICAL_VERSES = {
    "GEN.001.026": "Trial/Plural ambiguity - Trinity reference",
    "GEN.001.027": "Trinity context continuation",
    "GEN.011.007": "Trinity reference - 'let us go down'",
    "LUK.024.013": "Dual - two disciples",
    "MAT.018.020": "Paucal - two or three gather",
    "ACT.015.025": "Plural - apostolic council",
    "ACT.015.028": "Plural - apostolic decision",
    "MRK.006.007": "Dual - sent two by two",
    "ACT.013.002": "Dual - Barnabas and Saul",
}

# Genre classification (simple heuristic based on book)
GENRES = {
    # OT Narrative
    "GEN": "narrative", "EXO": "narrative", "NUM": "narrative", "DEU": "narrative",
    "JOS": "narrative", "JDG": "narrative", "RUT": "narrative",
    "1SA": "narrative", "2SA": "narrative", "1KI": "narrative",
    
    # OT Poetry/Wisdom
    "PSA": "poetry", "PRO": "poetry", "ECC": "poetry", "SNG": "poetry",
    
    # OT Prophecy
    "ISA": "prophecy", "JER": "prophecy", "EZK": "prophecy", "DAN": "prophecy",
    "HOS": "prophecy", "JOL": "prophecy", "AMO": "prophecy", "OBA": "prophecy",
    "JON": "prophecy", "MIC": "prophecy", "NAM": "prophecy", "HAB": "prophecy",
    "ZEP": "prophecy", "HAG": "prophecy", "ZEC": "prophecy", "MAL": "prophecy",
    
    # OT Other
    "NEH": "narrative", "EST": "narrative",
    
    # NT Narrative
    "MAT": "narrative", "MRK": "narrative", "LUK": "narrative", "JHN": "narrative",
    "ACT": "narrative",
    
    # NT Epistle
    "ROM": "epistle", "1CO": "epistle", "2CO": "epistle", "GAL": "epistle",
    "EPH": "epistle", "PHP": "epistle", "COL": "epistle",
    "1TH": "epistle", "2TH": "epistle", "1TI": "epistle", "2TI": "epistle",
    "TIT": "epistle", "PHM": "epistle", "HEB": "epistle",
    "JAS": "epistle", "1PE": "epistle", "2PE": "epistle",
    "1JN": "epistle", "2JN": "epistle", "3JN": "epistle", "JUD": "epistle",
    
    # NT Prophecy
    "REV": "prophecy",
}

OT_BOOKS = {"GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA", "1KI", "2KI",
            "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO", "ECC", "SNG",
            "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON",
            "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"}

def get_book(verse_ref):
    """Extract book code from verse reference."""
    return verse_ref.split('.')[0]

def get_testament(verse_ref):
    """Determine testament from verse reference."""
    book = get_book(verse_ref)
    return "OT" if book in OT_BOOKS else "NT"

def get_genre(verse_ref):
    """Get genre from verse reference."""
    book = get_book(verse_ref)
    return GENRES.get(book, "unknown")

def stratified_sample(verses, target_size, ot_ratio):
    """
    Sample verses with OT/NT stratification.
    
    Args:
        verses: List of verse references
        target_size: Target number of verses to sample
        ot_ratio: Desired ratio of OT verses (0.0 to 1.0)
    
    Returns:
        List of sampled verse references
    """
    # Separate OT and NT
    ot_verses = [v for v in verses if get_testament(v) == "OT"]
    nt_verses = [v for v in verses if get_testament(v) == "NT"]
    
    # Calculate target counts
    target_ot = int(target_size * ot_ratio)
    target_nt = target_size - target_ot
    
    # Sample (or use all if not enough)
    sampled_ot = random.sample(ot_verses, min(target_ot, len(ot_verses)))
    sampled_nt = random.sample(nt_verses, min(target_nt, len(nt_verses)))
    
    return sampled_ot + sampled_nt

def main():
    # Load raw data
    raw_data_path = Path("raw_tbta_data.yaml")
    with open(raw_data_path, 'r') as f:
        raw_data = yaml.safe_load(f)
    
    print("=" * 80)
    print("NUMBER-SYSTEMS FEATURE: STRATIFIED SAMPLING & SPLITTING")
    print("=" * 80)
    
    # Process each value
    all_samples = {}
    
    for value_data in raw_data['value']:
        value = value_data['specific_value']
        verses = value_data['verses']
        total = value_data['total_verses']
        ot_count = value_data['distribution']['OT']
        nt_count = value_data['distribution']['NT']
        
        print(f"\n{value}:")
        print(f"  Total available: {total}")
        print(f"  OT: {ot_count}, NT: {nt_count}")
        print(f"  OT ratio: {ot_count/total:.2%}")
        
        # Determine target sample size
        if value == "Singular":
            target = 300  # Sample from 113K
        elif value == "Plural":
            target = 300  # Sample from 55K
        elif value == "Dual":
            target = min(300, len(verses))  # Sample or use all of 1,744
        elif value == "Trial":
            target = len(verses)  # Use all 496
        elif value == "Quadrial":
            target = len(verses)  # Use all 185
        elif value == "Paucal":
            target = len(verses)  # Use all 52
        else:
            target = min(300, len(verses))
        
        # Calculate OT ratio from original distribution
        ot_ratio = ot_count / total if total > 0 else 0.5
        
        # Sample with stratification
        sampled = stratified_sample(verses, target, ot_ratio)
        
        # Add critical verses if they match this value
        for critical_verse in CRITICAL_VERSES:
            if critical_verse in verses and critical_verse not in sampled:
                # Remove a random verse and add critical verse
                if len(sampled) >= target:
                    sampled.pop(random.randint(0, len(sampled) - 1))
                sampled.append(critical_verse)
        
        print(f"  Sampled: {len(sampled)}")
        print(f"  Critical verses included: {sum(1 for v in sampled if v in CRITICAL_VERSES)}")
        
        all_samples[value] = sampled
    
    # Split each value into train/test/validate (40%/30%/30%)
    print("\n" + "=" * 80)
    print("SPLITTING INTO TRAIN/TEST/VALIDATE (40%/30%/30%)")
    print("=" * 80)
    
    splits = {
        'train': {},
        'test': {},
        'validate': {}
    }
    
    for value, verses in all_samples.items():
        random.shuffle(verses)  # Shuffle for random split
        
        n = len(verses)
        train_size = int(n * 0.40)
        test_size = int(n * 0.30)
        
        train_verses = verses[:train_size]
        test_verses = verses[train_size:train_size+test_size]
        validate_verses = verses[train_size+test_size:]
        
        splits['train'][value] = train_verses
        splits['test'][value] = test_verses
        splits['validate'][value] = validate_verses
        
        print(f"\n{value}:")
        print(f"  Train: {len(train_verses)} ({len(train_verses)/n:.1%})")
        print(f"  Test: {len(test_verses)} ({len(test_verses)/n:.1%})")
        print(f"  Validate: {len(validate_verses)} ({len(validate_verses)/n:.1%})")
        
        # Check critical verses distribution
        train_critical = sum(1 for v in train_verses if v in CRITICAL_VERSES)
        test_critical = sum(1 for v in test_verses if v in CRITICAL_VERSES)
        validate_critical = sum(1 for v in validate_verses if v in CRITICAL_VERSES)
        
        if train_critical + test_critical + validate_critical > 0:
            print(f"  Critical verses: train={train_critical}, test={test_critical}, validate={validate_critical}")
    
    # Generate output YAML files
    print("\n" + "=" * 80)
    print("GENERATING OUTPUT FILES")
    print("=" * 80)
    
    for split_name, split_data in splits.items():
        output = {
            'feature': 'number-systems',
            'translation_database': {
                'languages': ['fij', 'haw', 'smo', 'slv', 'tpi'],
                'families': ['Austronesian', 'Indo-European'],
                'rationale': 'Selected for dual/trial marking: Fijian (dual+trial), Hawaiian (dual+trial), Samoan (dual), Slovenian (obligatory dual), Tok Pisin (trial)'
            },
            'value': []
        }
        
        for value, verses in split_data.items():
            # Calculate distributions
            ot_verses = [v for v in verses if get_testament(v) == "OT"]
            nt_verses = [v for v in verses if get_testament(v) == "NT"]
            
            book_dist = defaultdict(int)
            for v in verses:
                book_dist[get_book(v)] += 1
            
            genre_dist = defaultdict(int)
            for v in verses:
                genre_dist[get_genre(v)] += 1
            
            # Build verse list with metadata
            verse_list = []
            for v in verses:
                verse_entry = {
                    'reference': v,
                    'tbta_value': value,
                    'genre': get_genre(v),
                    'difficulty': 'adversarial' if v in CRITICAL_VERSES else 'typical'
                }
                if v in CRITICAL_VERSES:
                    verse_entry['notes'] = CRITICAL_VERSES[v]
                verse_list.append(verse_entry)
            
            value_entry = {
                'specific_value': value,
                'total_verses': len(verses),
                'distribution': {
                    'OT': len(ot_verses),
                    'NT': len(nt_verses),
                    'Books': dict(book_dist)
                },
                'genres': dict(genre_dist),
                'verses': verse_list
            }
            
            output['value'].append(value_entry)
        
        # Write answer sheet (with TBTA values)
        output_path = Path(f"{split_name}.yaml")
        with open(output_path, 'w') as f:
            yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"✓ Generated {output_path}")
        
        # Generate question sheet (translations only - placeholder)
        question_output = {
            'feature': 'number-systems',
            'translations_included': ['fij', 'haw', 'smo', 'slv', 'tpi'],
            'note': 'Translation texts need to be fetched from eBible.org or Bible.com APIs',
            'verses': []
        }
        
        for value_entry in output['value']:
            for verse_meta in value_entry['verses']:
                verse_ref = verse_meta['reference']
                question_output['verses'].append({
                    'reference': verse_ref,
                    'translations': {},
                    'note': f'Fetch from .data/commentary/{verse_ref.replace(".", "/")}-ebible.yaml'
                })
        
        question_path = Path(f"{split_name}_questions.yaml")
        with open(question_path, 'w') as f:
            yaml.dump(question_output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"✓ Generated {question_path} (placeholder - translations need fetching)")
    
    # Generate TRANSLATION-DATABASE.md
    translation_db_content = """# Translation Database for Number-Systems Feature

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
"""
    
    with open("TRANSLATION-DATABASE.md", 'w') as f:
        f.write(translation_db_content)
    
    print(f"✓ Generated TRANSLATION-DATABASE.md")
    
    print("\n" + "=" * 80)
    print("SAMPLING COMPLETE!")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Fetch translations for verses in *_questions.yaml")
    print("2. Proceed to Stage 5: Algorithm development using train.yaml and train_questions.yaml")
    print("3. Lock predictions before checking test.yaml")
    print("4. Never look at validate.yaml until final blind validation")

if __name__ == "__main__":
    main()

