#!/usr/bin/env python3
"""
Cross-Database Search Translation Engine

Translates search strings between database-specific syntaxes.
Handles field codes, proximity operators, wildcards, and subject headings.

Supported databases:
- PubMed/MEDLINE
- Embase (Ovid)
- Web of Science
- Scopus
- CENTRAL (Cochrane)

Usage:
    from search_translation import SearchTranslator
    
    translator = SearchTranslator()
    embase_query = translator.translate(pubmed_query, from_db="pubmed", to_db="embase")
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class TranslationRule:
    """Translation rule for converting syntax elements."""
    pattern: str
    replacement: str
    description: str


class SearchTranslator:
    """
    Translates search strings between database syntaxes.
    
    Handles:
    - Field codes (ti,ab vs [tiab] vs :ti,ab)
    - Proximity operators (NEAR/3 vs ADJ3 vs W/3)
    - Wildcards (* vs $ vs ?)
    - Truncation (automatic vs manual)
    - Subject headings (MeSH vs Emtree vs descriptors)
    - Boolean operators (case sensitivity)
    """
    
    def __init__(self):
        """Initialize translation rules for each database pair."""
        self._load_translation_rules()
    
    def translate(self, query: str, from_db: str, to_db: str) -> str:
        """
        Translate search query between databases.
        
        Args:
            query: Search string in source database syntax
            from_db: Source database (pubmed, embase, wos, scopus, central)
            to_db: Target database
            
        Returns:
            Translated search string
        """
        from_db = from_db.lower()
        to_db = to_db.lower()
        
        if from_db == to_db:
            return query
        
        # Get translation rules
        key = f"{from_db}_to_{to_db}"
        if key not in self.translation_rules:
            raise ValueError(f"Translation not supported: {from_db} → {to_db}")
        
        rules = self.translation_rules[key]
        
        # Apply translations in order
        translated = query
        
        for rule in rules:
            translated = re.sub(rule.pattern, rule.replacement, translated, flags=re.IGNORECASE)
        
        return translated
    
    def translate_to_all(self, query: str, from_db: str) -> Dict[str, str]:
        """
        Translate query to all supported databases.
        
        Args:
            query: Search string
            from_db: Source database
            
        Returns:
            Dictionary mapping database names to translated queries
        """
        databases = ["pubmed", "embase", "wos", "scopus", "central"]
        databases.remove(from_db.lower())
        
        translations = {from_db: query}
        
        for db in databases:
            try:
                translations[db] = self.translate(query, from_db, db)
            except ValueError:
                translations[db] = f"[Translation not available from {from_db}]"
        
        return translations
    
    def _load_translation_rules(self):
        """Load all translation rules."""
        self.translation_rules = {}
        
        # PubMed → Embase
        self.translation_rules["pubmed_to_embase"] = [
            # Field codes
            TranslationRule(r'\[tiab\]', ':ab,ti', 'Title/abstract field'),
            TranslationRule(r'\[ti\]', ':ti', 'Title field'),
            TranslationRule(r'\[ab\]', ':ab', 'Abstract field'),
            TranslationRule(r'\[au\]', ':au', 'Author field'),
            TranslationRule(r'\[mh\]', '/exp', 'MeSH → Emtree explosion'),
            TranslationRule(r'\[majr\]', '/mj', 'Major topic'),
            TranslationRule(r'\[pt\]', ':it', 'Publication type'),
            
            # Proximity operators (PubMed doesn't have proximity, but if added)
            TranslationRule(r'NEAR/(\d+)', r'NEAR/\1', 'Proximity operator'),
            
            # Wildcards (PubMed uses *, Embase uses $ for single char, * for multiple)
            TranslationRule(r'\*', '$', 'Wildcard conversion'),
            
            # Truncation
            TranslationRule(r':ti,ab', ':ab,ti', 'Field order normalization'),
        ]
        
        # PubMed → Web of Science
        self.translation_rules["pubmed_to_wos"] = [
            # Field codes
            TranslationRule(r'\[tiab\]', '=(TI OR AB)', 'Title/abstract field'),
            TranslationRule(r'\[ti\]', '=TI', 'Title field'),
            TranslationRule(r'\[ab\]', '=AB', 'Abstract field'),
            TranslationRule(r'\[au\]', '=AU', 'Author field'),
            TranslationRule(r'\[mh\]', '=TS', 'MeSH → Topic search'),
            
            # Proximity operators
            TranslationRule(r'NEAR/(\d+)', r'NEAR/\1', 'Proximity operator'),
            
            # Wildcards
            TranslationRule(r'\*', '$', 'Wildcard conversion'),
        ]
        
        # PubMed → Scopus
        self.translation_rules["pubmed_to_scopus"] = [
            # Field codes
            TranslationRule(r'\[tiab\]', '{TITLE-ABS}', 'Title/abstract field'),
            TranslationRule(r'\[ti\]', '{TITLE}', 'Title field'),
            TranslationRule(r'\[ab\]', '{ABS}', 'Abstract field'),
            TranslationRule(r'\[au\]', '{AU}', 'Author field'),
            TranslationRule(r'\[mh\]', '{INDEX}', 'MeSH → Index terms'),
            
            # Proximity operators
            TranslationRule(r'NEAR/(\d+)', r'W/\1', 'Proximity operator (NEAR → W)'),
            
            # Wildcards
            TranslationRule(r'\*', '*', 'Wildcard (no change)'),
        ]
        
        # Embase → PubMed
        self.translation_rules["embase_to_pubmed"] = [
            # Field codes
            TranslationRule(r':ab,ti', '[tiab]', 'Title/abstract field'),
            TranslationRule(r':ti', '[ti]', 'Title field'),
            TranslationRule(r':ab', '[ab]', 'Abstract field'),
            TranslationRule(r':au', '[au]', 'Author field'),
            TranslationRule(r'/exp', '[mh]', 'Emtree → MeSH explosion'),
            TranslationRule(r'/mj', '[majr]', 'Major topic'),
            TranslationRule(r':it', '[pt]', 'Publication type'),
            
            # Wildcards
            TranslationRule(r'\$', '*', 'Wildcard conversion'),
        ]
        
        # Add reverse translations as needed
        # (Other combinations follow similar patterns)
    
    def explain_differences(self, from_db: str, to_db: str) -> List[str]:
        """
        Explain key syntax differences between two databases.
        
        Returns:
            List of difference explanations
        """
        differences = {
            ("pubmed", "embase"): [
                "Field codes: [tiab] → :ab,ti",
                "Subject headings: [mh] → /exp (MeSH vs Emtree)",
                "Wildcards: * → $ (for truncation)",
                "Embase has proximity operators (NEAR/n)",
            ],
            ("pubmed", "wos"): [
                "Field codes: [tiab] → =(TI OR AB)",
                "Subject headings: MeSH not available, use TS (topic)",
                "Wildcards: * → $",
                "Web of Science uses = prefix for field tags",
            ],
            ("pubmed", "scopus"): [
                "Field codes: [tiab] → {TITLE-ABS}",
                "Subject headings: [mh] → {INDEX}",
                "Proximity: NEAR/n → W/n",
                "Scopus uses {} for field tags",
            ],
        }
        
        key = (from_db.lower(), to_db.lower())
        reverse_key = (to_db.lower(), from_db.lower())
        
        if key in differences:
            return differences[key]
        elif reverse_key in differences:
            # Return reverse explanations
            return [f"(Reverse) {diff}" for diff in differences[reverse_key]]
        else:
            return ["Comparison not available for these databases"]


class SearchStringBuilder:
    """
    Interactive builder for developing search strategies.
    
    Helps with:
    - PICOS concept mapping
    - Synonym expansion
    - Boolean logic structuring
    - Subject heading suggestions
    """
    
    def __init__(self):
        self.concepts = {}
    
    def add_concept(self, concept_name: str, terms: List[str]):
        """Add search concept with synonyms."""
        self.concepts[concept_name] = terms
    
    def build_query(self, database: str = "pubmed") -> str:
        """
        Build complete search query from concepts.
        
        Args:
            database: Target database for syntax
            
        Returns:
            Complete search string with Boolean logic
        """
        concept_strings = []
        
        for concept_name, terms in self.concepts.items():
            # Combine terms within concept with OR
            if database == "pubmed":
                term_strings = [f'"{term}"[tiab]' for term in terms]
            elif database == "embase":
                term_strings = [f"'{term}':ab,ti" for term in terms]
            elif database == "wos":
                term_strings = [f'"{term}"=(TI OR AB)' for term in terms]
            elif database == "scopus":
                term_strings = [f'"{term}"{{TITLE-ABS}}' for term in terms]
            else:
                term_strings = [f'"{term}"' for term in terms]
            
            concept_string = " OR ".join(term_strings)
            concept_strings.append(f"({concept_string})")
        
        # Combine concepts with AND
        query = " AND ".join(concept_strings)
        
        return query
    
    def suggest_mesh_terms(self, concept: str) -> List[str]:
        """
        Suggest MeSH terms for a concept.
        
        Note: In production, this would query PubMed MeSH API.
        For now, returns placeholder suggestions.
        """
        # Placeholder - would query: https://www.ncbi.nlm.nih.gov/mesh/
        suggestions = {
            "depression": ["Depression", "Depressive Disorder", "Depressive Disorder, Major"],
            "anxiety": ["Anxiety", "Anxiety Disorders", "Generalized Anxiety Disorder"],
            "cbt": ["Cognitive Behavioral Therapy", "Cognitive Therapy"],
            "mindfulness": ["Mindfulness", "Meditation"],
        }
        
        concept_lower = concept.lower()
        return suggestions.get(concept_lower, [f"Check MeSH database for: {concept}"])


def demo():
    """Demonstrate search translation."""
    print("═══════════════════════════════════════════════════════════════")
    print("           SEARCH TRANSLATION ENGINE DEMO")
    print("═══════════════════════════════════════════════════════════════\n")
    
    # Example PubMed query
    pubmed_query = '''
    ("cognitive therapy"[MeSH] OR "cognitive behavioral therapy"[tiab] OR CBT[tiab])
    AND
    (depression[tiab] OR "depressive disorder"[MeSH])
    AND
    (adult*[tiab])
    '''
    
    print("Original PubMed Query:")
    print(pubmed_query)
    print("\n" + "─" * 65 + "\n")
    
    translator = SearchTranslator()
    
    # Translate to all databases
    translations = translator.translate_to_all(pubmed_query, "pubmed")
    
    for db, query in translations.items():
        if db == "pubmed":
            continue
        print(f"{db.upper()} Translation:")
        print(query)
        print("\n" + "─" * 65 + "\n")
    
    # Show differences
    print("Key Syntax Differences (PubMed → Embase):")
    differences = translator.explain_differences("pubmed", "embase")
    for diff in differences:
        print(f"  • {diff}")
    
    print("\n═══════════════════════════════════════════════════════════════\n")


if __name__ == "__main__":
    demo()
