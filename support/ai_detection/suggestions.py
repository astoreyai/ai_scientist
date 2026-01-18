"""Generate suggestions for improving detected AI patterns."""

from typing import List
from .models import DetectionResult, Suggestion


class SuggestionGenerator:
    """Generate actionable suggestions for improving text authenticity."""
    
    def generate_suggestions(self, result: DetectionResult) -> List[Suggestion]:
        """Generate suggestions based on detection results."""
        suggestions = []
        
        # Sentence structure suggestions
        if result.sentence_score > 60:
            suggestions.append(Suggestion(
                category="sentence_structure",
                issue="Sentences are too uniform in length",
                suggestion="Vary sentence lengths: mix short (5-10 words), medium (15-20), and long (25-35+) sentences",
                example_before="The results showed significant effects. The analysis demonstrated clear patterns. The findings support our hypothesis.",
                example_after="The results were significant. Our analysis showed clear patterns across all conditions, supporting the hypothesis.",
                priority="high"
            ))
        
        # AI word suggestions
        if result.word_frequency_score > 60:
            ai_words_list = list(result.ai_words_found.keys())[:3]
            suggestions.append(Suggestion(
                category="word_choice",
                issue=f"High frequency of AI-typical words: {', '.join(ai_words_list)}",
                suggestion="Replace AI-typical words with simpler alternatives or field-specific terminology",
                example_before="This study delves into leveraging robust methodologies",
                example_after="We examine how researchers use reliable methods",
                priority="high"
            ))
        
        # Grammar perfection suggestions
        if result.grammar_score > 70:
            suggestions.append(Suggestion(
                category="writing_style",
                issue="Writing is excessively perfect with no natural variations",
                suggestion="Allow natural imperfections: use contractions where appropriate, vary formality slightly, include field-specific casual phrases",
                priority="medium"
            ))
        
        # Paragraph structure suggestions
        if result.paragraph_score > 60:
            suggestions.append(Suggestion(
                category="paragraph_flow",
                issue="Paragraphs follow mechanical structure too consistently",
                suggestion="Vary paragraph lengths (2-8 sentences). Don't force topic-sentence pattern. Use single-sentence paragraphs for emphasis.",
                priority="medium"
            ))
        
        # Transition word suggestions
        if "transition words" in ' '.join(result.patterns_detected).lower():
            suggestions.append(Suggestion(
                category="word_choice",
                issue="Overuse of formal transition words",
                suggestion="Replace formal transitions ('furthermore', 'moreover') with simpler words ('also', 'next') or use dashes/punctuation",
                example_before="Furthermore, the results show... Moreover, the analysis reveals...",
                example_after="The results also show... Looking closer, the analysis reveals...",
                priority="medium"
            ))
        
        return suggestions
    
    def get_word_alternatives(self, ai_word: str) -> List[str]:
        """Get alternative words for AI-typical words."""
        alternatives = {
            "delve": ["examine", "explore", "investigate", "study", "analyze"],
            "leverage": ["use", "apply", "employ", "utilize"],
            "utilize": ["use"],
            "robust": ["strong", "reliable", "thorough", "solid"],
            "comprehensive": ["complete", "thorough", "full", "detailed"],
            "facilitate": ["enable", "help", "allow", "support"],
            "furthermore": ["also", "next", "additionally", "[remove]"],
            "moreover": ["also", "furthermore", "[use dash instead]"],
            "consequently": ["so", "therefore", "as a result"],
            "subsequently": ["then", "later", "next"],
            "demonstrate": ["show", "reveal", "indicate"],
            "implement": ["use", "apply", "create"],
        }
        
        return alternatives.get(ai_word.lower(), [ai_word])
