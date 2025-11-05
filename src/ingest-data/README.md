# Data Ingestion Scripts

This directory contains scripts for fetching and ingesting data from various Bible resources.

## Directory Structure

Each data source has its own subdirectory:

- `ebible/` - eBible corpus (1000+ translations)
- `strongs/` - Strong's Hebrew and Greek dictionaries
- `macula/` - Macula Hebrew and Greek source language datasets (fetch + process)
- `tbta/` - The Bible Translator's Assistant data

## Usage

### eBible Corpus

Fetch translations from the eBible corpus (https://github.com/BibleNLP/ebible):

```bash
python3 -m src.ingest-data.ebible.ebible_fetcher
```

### Strong's Dictionaries

Fetch Strong's Hebrew and Greek dictionary data:

```bash
python3 src/ingest-data/strongs/strongs_fetcher.py
```

### Macula Datasets

**Step 1: Download raw data (one-time setup):**
```bash
python3 src/ingest-data/macula/macula_fetcher.py
```

**Step 2: Process verses into YAML files:**
```bash
# Single verse
python3 src/ingest-data/macula/macula_processor.py --verse "JHN 3:16"

# Entire book
python3 src/ingest-data/macula/macula_processor.py --book MAT

# All verses
python3 src/ingest-data/macula/macula_processor.py --all
```

### TBTA (The Bible Translator's Assistant)

Process TBTA JSON export files:

```bash
# Single verse
python3 src/ingest-data/tbta/tbta_processor.py --verse "GEN 1:1"

# Entire book
python3 src/ingest-data/tbta/tbta_processor.py --book GEN
```

