"""
Sentence Complexity Analysis for AI Text Detection

Analyzes readability metrics and complexity variance to detect AI-generated text.
AI tends to maintain uniform complexity, while human writing varies naturally.
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass
import re
import math
from collections import Counter


@dataclass
class ComplexityResult:
    """Results from complexity analysis."""
    flesch_kincaid_grade: float  # Reading grade level
    gunning_fog_index: float  # Fog index
    avg_sentence_length: float  # Words per sentence
    avg_word_length: float  # Characters per word
    complexity_variance: float  # Variance in sentence complexity
    uniformity_score: float  # 0-1, higher = more uniform (AI-like)
    readability_score: float  # 0-100, lower = harder to read
    overall_ai_score: float  # 0-1, higher = more likely AI
    sentence_complexities: List[float]  # Complexity score for each sentence


class ComplexityAnalyzer:
    """
    Analyzes text complexity and readability metrics.
    
    Detects AI-generated text by identifying excessive uniformity
    in sentence complexity - a hallmark of AI writing.
    """
    
    def __init__(self):
        """Initialize analyzer with thresholds."""
        # Human writing typically shows variance in sentence complexity
        # AI writing tends to cluster around narrow complexity ranges
        self.low_variance_threshold = 2.0  # Variance < 2.0 is suspiciously uniform
        self.ideal_variance_range = (3.0, 8.0)  # Typical human variance
        
    def analyze(self, text: str) -> ComplexityResult:
        """
        Analyze text complexity and uniformity.
        
        Args:
            text: Text to analyze
            
        Returns:
            ComplexityResult with detailed metrics
        """
        # Split into sentences
        sentences = self._split_sentences(text)
        
        if not sentences:
            return self._empty_result()
        
        # Calculate metrics for each sentence
        sentence_complexities = [self._sentence_complexity(s) for s in sentences]
        
        # Calculate readability metrics
        flesch_kincaid = self._flesch_kincaid_grade(text, sentences)
        gunning_fog = self._gunning_fog_index(text, sentences)
        readability = self._flesch_reading_ease(text, sentences)
        
        # Calculate average lengths
        words = text.split()
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
        
        # Calculate complexity variance
        complexity_variance = self._calculate_variance(sentence_complexities)
        
        # Calculate uniformity score (low variance = high uniformity = AI-like)
        uniformity_score = self._calculate_uniformity_score(complexity_variance)
        
        # Overall AI score combines multiple signals
        overall_ai_score = self._calculate_overall_score(
            flesch_kincaid, gunning_fog, complexity_variance, uniformity_score
        )
        
        return ComplexityResult(
            flesch_kincaid_grade=flesch_kincaid,
            gunning_fog_index=gunning_fog,
            avg_sentence_length=avg_sentence_length,
            avg_word_length=avg_word_length,
            complexity_variance=complexity_variance,
            uniformity_score=uniformity_score,
            readability_score=readability,
            overall_ai_score=overall_ai_score,
            sentence_complexities=sentence_complexities
        )
    
    def _split_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.
        
        Handles common abbreviations and edge cases.
        """
        # Simple sentence splitting (improved version would use NLTK)
        # This handles basic cases: periods, exclamation marks, question marks
        sentences = re.split(r'[.!?]+\s+', text)
        
        # Remove empty sentences
        sentences = [s.strip() for s in sentences if s.strip()]
        
        return sentences
    
    def _sentence_complexity(self, sentence: str) -> float:
        """
        Calculate complexity score for a single sentence.
        
        Combines multiple factors:
        - Sentence length
        - Average word length
        - Syllable count
        - Clause count (approximated by comma count)
        
        Returns:
            Complexity score (0-100+)
        """
        words = sentence.split()
        
        if not words:
            return 0.0
        
        # Sentence length factor
        length_factor = len(words)
        
        # Average word length factor
        avg_word_len = sum(len(w) for w in words) / len(words)
        
        # Syllable count (approximation)
        syllables = sum(self._count_syllables(w) for w in words)
        
        # Clause count (approximation using commas and conjunctions)
        clauses = sentence.count(',') + sentence.count(';') + 1
        
        # Combine factors
        complexity = (
            0.4 * length_factor +
            0.3 * (avg_word_len * 2) +
            0.2 * (syllables / len(words) * 10) +
            0.1 * (clauses * 5)
        )
        
        return complexity
    
    def _count_syllables(self, word: str) -> int:
        """
        Approximate syllable count for a word.
        
        Uses simple vowel-counting heuristic.
        """
        word = word.lower()
        count = 0
        vowels = 'aeiouy'
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                count += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent e
        if word.endswith('e'):
            count -= 1
        
        # Every word has at least one syllable
        if count == 0:
            count = 1
        
        return count
    
    def _flesch_kincaid_grade(self, text: str, sentences: List[str]) -> float:
        """
        Calculate Flesch-Kincaid Grade Level.
        
        Formula: 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
        
        Returns:
            Grade level (e.g., 12.0 = 12th grade reading level)
        """
        words = text.split()
        
        if not words or not sentences:
            return 0.0
        
        total_sentences = len(sentences)
        total_words = len(words)
        total_syllables = sum(self._count_syllables(w) for w in words)
        
        if total_sentences == 0 or total_words == 0:
            return 0.0
        
        grade = (
            0.39 * (total_words / total_sentences) +
            11.8 * (total_syllables / total_words) -
            15.59
        )
        
        return max(0.0, grade)  # Can't be negative
    
    def _gunning_fog_index(self, text: str, sentences: List[str]) -> float:
        """
        Calculate Gunning Fog Index.
        
        Formula: 0.4 * ((words/sentences) + 100 * (complex_words/words))
        Complex words = 3+ syllables
        
        Returns:
            Fog index (e.g., 12.0 = 12th grade reading level)
        """
        words = text.split()
        
        if not words or not sentences:
            return 0.0
        
        total_sentences = len(sentences)
        total_words = len(words)
        complex_words = sum(1 for w in words if self._count_syllables(w) >= 3)
        
        if total_sentences == 0 or total_words == 0:
            return 0.0
        
        fog = 0.4 * (
            (total_words / total_sentences) +
            100 * (complex_words / total_words)
        )
        
        return fog
    
    def _flesch_reading_ease(self, text: str, sentences: List[str]) -> float:
        """
        Calculate Flesch Reading Ease score.
        
        Formula: 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
        
        Returns:
            Score 0-100 (higher = easier to read)
        """
        words = text.split()
        
        if not words or not sentences:
            return 0.0
        
        total_sentences = len(sentences)
        total_words = len(words)
        total_syllables = sum(self._count_syllables(w) for w in words)
        
        if total_sentences == 0 or total_words == 0:
            return 0.0
        
        ease = (
            206.835 -
            1.015 * (total_words / total_sentences) -
            84.6 * (total_syllables / total_words)
        )
        
        # Clamp to 0-100
        return max(0.0, min(100.0, ease))
    
    def _calculate_variance(self, values: List[float]) -> float:
        """
        Calculate variance of a list of values.
        
        Returns:
            Variance (0 = all values identical)
        """
        if not values:
            return 0.0
        
        mean = sum(values) / len(values)
        squared_diffs = [(x - mean) ** 2 for x in values]
        variance = sum(squared_diffs) / len(values)
        
        return variance
    
    def _calculate_uniformity_score(self, variance: float) -> float:
        """
        Convert complexity variance to uniformity score.
        
        Low variance = high uniformity = AI-like
        
        Args:
            variance: Complexity variance
            
        Returns:
            Uniformity score 0-1 (higher = more uniform = more AI-like)
        """
        if variance < self.low_variance_threshold:
            # Very uniform (very AI-like)
            return 1.0
        elif variance < self.ideal_variance_range[0]:
            # Somewhat uniform (possibly AI)
            return 0.7
        elif variance <= self.ideal_variance_range[1]:
            # Normal variance (human-like)
            return 0.0
        else:
            # High variance (could be poor writing or mixed sources)
            return 0.3
    
    def _calculate_overall_score(
        self,
        flesch_kincaid: float,
        gunning_fog: float,
        variance: float,
        uniformity: float
    ) -> float:
        """
        Calculate overall AI likelihood score.
        
        Combines multiple complexity signals.
        
        Returns:
            Score 0-1 (higher = more likely AI)
        """
        # AI text often has:
        # 1. Very uniform complexity (high uniformity score)
        # 2. Moderate readability (FK grade 10-14, not too simple or complex)
        # 3. Similar Flesch-Kincaid and Gunning-Fog scores
        
        # Uniformity is the strongest signal
        score = 0.6 * uniformity
        
        # Moderate complexity is typical of AI (grades 10-14)
        if 10 <= flesch_kincaid <= 14:
            score += 0.2
        
        # Very similar FK and GF scores suggest AI
        if abs(flesch_kincaid - gunning_fog) < 2.0:
            score += 0.2
        
        return min(1.0, score)
    
    def _empty_result(self) -> ComplexityResult:
        """Return empty result for empty text."""
        return ComplexityResult(
            flesch_kincaid_grade=0.0,
            gunning_fog_index=0.0,
            avg_sentence_length=0.0,
            avg_word_length=0.0,
            complexity_variance=0.0,
            uniformity_score=0.0,
            readability_score=0.0,
            overall_ai_score=0.0,
            sentence_complexities=[]
        )


# Convenience function
def analyze_complexity(text: str) -> ComplexityResult:
    """
    Analyze text complexity.
    
    Args:
        text: Text to analyze
        
    Returns:
        ComplexityResult with detailed metrics
    """
    analyzer = ComplexityAnalyzer()
    return analyzer.analyze(text)
