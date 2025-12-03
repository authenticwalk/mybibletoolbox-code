import csv
import re
import os

# Configuration
CSV_DIR = "temp_tbta_repo/csv/Bible"
BOOKS = [
    "Genesis.csv", "Joshua.csv", "Ruth.csv", 
    "1_Samuel.csv", "2_Samuel.csv", 
    "Nehemiah.csv", "Esther.csv", "Daniel.csv", 
    "Jonah.csv", "Nahum.csv", 
    "Matthew.csv", "Mark.csv", "Acts.csv", 
    "Titus.csv", "Philemon.csv", "2_John.csv"
]

# Rules and Regex
PATTERNS = {
    "Rule1_Coreference_Contradiction": re.compile(r'\b(he|she|they)\b', re.IGNORECASE),
    "Rule3_Relativization_Support": re.compile(r'\[who (was|is|were|are|had)\b'),
    "Rule3_Relativization_Contradiction": re.compile(r',[ ]?the [a-z]+'), # Simplistic appositive check
    "Rule4_Deixis_Support": re.compile(r'\b(I|you|we|my|your|our|us|me)\((Speaker|Addressee|Possessor|Group|S|A|P|G)'),
    "Rule4_Deixis_Contradiction": re.compile(r'\b(I|you|we)\b(?![\(\[])'), # Pronoun without paren
    "Rule6_Subordinate_Support": re.compile(r'\['),
    "Rule7_Quote_Support": re.compile(r'said, \["'),
    "Rule7_Quote_Contradiction": re.compile(r'said, "'),
    "Rule8_Imperative_Support": re.compile(r'\(imp\)'),
    "Rule9_Hyphenated_Support": re.compile(r'\b[a-z]+-[a-z]+\b'),
    "Rule11_Demonym_Support": re.compile(r'\[who (was|were) from [A-Z]'),
    "Rule11_Demonym_Contradiction": re.compile(r'\b[A-Z][a-z]+(ite|ites|ian|ians)\b'),
    "Rule12_Gap_Support": re.compile(r'\((implicit-|footnote)'),
}

# Store results
results = {key: [] for key in PATTERNS.keys()}

def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ref = row.get('Reference', 'Unknown')
            verse = row.get('Verse', '')
            
            if not verse:
                continue

            for key, pattern in PATTERNS.items():
                if len(results[key]) >= 10: # Limit examples
                    continue
                
                # Check for match
                match = pattern.search(verse)
                if match:
                    # For contradictions, we want to be sure it's not a false positive
                    # e.g. "he" in "the" (boundary handled by \b)
                    # e.g. "I" in "I(Speaker)" (handled by negative lookahead for Rule 4)
                    
                    # Context snippet
                    start = max(0, match.start() - 20)
                    end = min(len(verse), match.end() + 20)
                    snippet = verse[start:end].replace('\n', ' ')
                    
                    results[key].append({
                        'ref': ref,
                        'match': match.group(0),
                        'snippet': snippet,
                        'full_verse': verse[:100] + "..." if len(verse) > 100 else verse
                    })

def main():
    for book in BOOKS:
        path = os.path.join(CSV_DIR, book)
        print(f"Analyzing {book}...")
        analyze_file(path)
    
    # Output results
    print("\n=== ANALYSIS RESULTS ===\n")
    for key, items in results.items():
        print(f"\n--- {key} ({len(items)}) ---")
        for item in items:
            print(f"{item['ref']}: {item['snippet']}")

if __name__ == "__main__":
    main()

