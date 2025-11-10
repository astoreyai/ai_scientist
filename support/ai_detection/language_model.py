"""
Statistical Language Modeling for AI Text Detection

Detects AI-generated text using n-gram analysis and statistical anomaly detection.
Compares text against corpus of human academic writing.
"""

from typing import Dict, List, Tuple, Counter as CounterType
from collections import Counter, defaultdict
from dataclasses import dataclass
import math
import re


@dataclass
class LanguageModelResult:
    """Results from language model analysis."""
    bigram_score: float  # 0-1, higher = more likely AI
    trigram_score: float  # 0-1, higher = more likely AI
    transition_anomaly_score: float  # 0-1, higher = more unusual transitions
    repetition_score: float  # 0-1, higher = more repetitive patterns
    overall_score: float  # Weighted combination
    unusual_bigrams: List[Tuple[str, str, float]]  # (word1, word2, probability)
    unusual_trigrams: List[Tuple[str, str, str, float]]  # (w1, w2, w3, probability)
    repetitive_phrases: List[Tuple[str, int]]  # (phrase, count)


class LanguageModel:
    """
    N-gram language model for detecting AI-generated text.
    
    Uses statistical properties of word sequences to identify
    patterns typical of AI language generation.
    """
    
    def __init__(self):
        """Initialize with baseline statistics from human academic writing."""
        # These statistics are approximations based on academic corpus analysis
        # In production, these would be loaded from pre-computed corpus files
        
        # Common bigram transition probabilities in academic writing
        # Format: (word1, word2) -> probability
        self.bigram_baseline = self._load_bigram_baseline()
        
        # Common trigram probabilities
        # Format: (word1, word2, word3) -> probability
        self.trigram_baseline = self._load_trigram_baseline()
        
        # Thresholds
        self.unusual_bigram_threshold = 0.001  # P(w2|w1) < 0.001 is unusual
        self.unusual_trigram_threshold = 0.0001  # P(w3|w1,w2) < 0.0001 is unusual
        self.repetition_threshold = 3  # Same phrase appearing 3+ times is unusual
        
    def _load_bigram_baseline(self) -> Dict[Tuple[str, str], float]:
        """
        Load baseline bigram probabilities.
        
        In production, this loads from corpus/bigrams.json.
        For now, returns common academic transitions.
        """
        # Common academic bigrams with approximate probabilities
        # These are illustrative - real implementation uses full corpus
        common_bigrams = {
            ("the", "study"): 0.05,
            ("the", "results"): 0.04,
            ("this", "study"): 0.03,
            ("these", "results"): 0.02,
            ("we", "found"): 0.03,
            ("we", "observed"): 0.02,
            ("our", "results"): 0.03,
            ("our", "findings"): 0.02,
            ("in", "this"): 0.04,
            ("in", "the"): 0.06,
            ("of", "the"): 0.08,
            ("to", "the"): 0.05,
            ("and", "the"): 0.04,
            ("as", "shown"): 0.02,
            ("as", "described"): 0.01,
            # AI-typical transitions (less common in human writing)
            ("delve", "into"): 0.0005,  # Very AI-typical
            ("leverage", "the"): 0.0003,
            ("utilize", "the"): 0.0008,
            ("robust", "methodology"): 0.0002,
            ("comprehensive", "analysis"): 0.0004,
        }
        return common_bigrams
    
    def _load_trigram_baseline(self) -> Dict[Tuple[str, str, str], float]:
        """
        Load baseline trigram probabilities.
        
        In production, this loads from corpus/trigrams.json.
        """
        common_trigrams = {
            ("in", "this", "study"): 0.02,
            ("the", "results", "show"): 0.015,
            ("as", "shown", "in"): 0.01,
            ("we", "found", "that"): 0.02,
            ("these", "findings", "suggest"): 0.01,
            ("our", "results", "demonstrate"): 0.008,
            # AI-typical transitions
            ("furthermore", "it", "is"): 0.0001,
            ("moreover", "the", "results"): 0.0001,
            ("additionally", "it", "should"): 0.00008,
        }
        return common_trigrams
    
    def analyze(self, text: str) -> LanguageModelResult:
        """
        Analyze text using n-gram language modeling.
        
        Args:
            text: Text to analyze
            
        Returns:
            LanguageModelResult with scores and detected anomalies
        """
        # Tokenize
        words = self._tokenize(text)
        
        if len(words) < 3:
            return LanguageModelResult(
                bigram_score=0.0,
                trigram_score=0.0,
                transition_anomaly_score=0.0,
                repetition_score=0.0,
                overall_score=0.0,
                unusual_bigrams=[],
                unusual_trigrams=[],
                repetitive_phrases=[]
            )
        
        # Calculate bigram statistics
        bigram_score, unusual_bigrams = self._analyze_bigrams(words)
        
        # Calculate trigram statistics
        trigram_score, unusual_trigrams = self._analyze_trigrams(words)
        
        # Detect repetitive patterns
        repetition_score, repetitive_phrases = self._detect_repetition(words)
        
        # Calculate transition anomaly score
        transition_anomaly_score = self._calculate_transition_anomalies(words)
        
        # Overall score (weighted combination)
        overall_score = (
            0.30 * bigram_score +
            0.30 * trigram_score +
            0.25 * transition_anomaly_score +
            0.15 * repetition_score
        )
        
        return LanguageModelResult(
            bigram_score=bigram_score,
            trigram_score=trigram_score,
            transition_anomaly_score=transition_anomaly_score,
            repetition_score=repetition_score,
            overall_score=overall_score,
            unusual_bigrams=unusual_bigrams[:10],  # Top 10
            unusual_trigrams=unusual_trigrams[:10],  # Top 10
            repetitive_phrases=repetitive_phrases[:10]  # Top 10
        )
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into words.
        
        Lowercases and removes punctuation (except sentence boundaries).
        """
        # Remove special characters but keep sentence boundaries
        text = re.sub(r'[^\w\s\.\!\?]', ' ', text.lower())
        
        # Split on whitespace
        words = text.split()
        
        # Remove empty strings
        words = [w for w in words if w and w not in {'.', '!', '?'}]
        
        return words
    
    def _analyze_bigrams(self, words: List[str]) -> Tuple[float, List[Tuple[str, str, float]]]:
        """
        Analyze bigram patterns.
        
        Returns:
            (score, unusual_bigrams) where score is 0-1
        """
        bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
        
        if not bigrams:
            return 0.0, []
        
        unusual_bigrams = []
        total_unusual = 0
        
        for bigram in bigrams:
            # Get expected probability
            expected_prob = self.bigram_baseline.get(bigram, 0.01)  # Default: 1%
            
            # Count this bigram in text
            bigram_count = bigrams.count(bigram)
            observed_prob = bigram_count / len(bigrams)
            
            # Check if unusual (much more or much less frequent than expected)
            if expected_prob < self.unusual_bigram_threshold:
                # This is an unusual bigram even in human writing
                unusual_bigrams.append((bigram[0], bigram[1], expected_prob))
                total_unusual += 1
            elif observed_prob > expected_prob * 3:
                # This bigram appears way more than expected
                unusual_bigrams.append((bigram[0], bigram[1], observed_prob))
                total_unusual += 1
        
        # Remove duplicates
        unusual_bigrams = list(set(unusual_bigrams))
        
        # Score: proportion of unusual bigrams
        score = min(1.0, total_unusual / max(1, len(bigrams)) * 10)  # Scale up
        
        # Sort by probability (most unusual first)
        unusual_bigrams.sort(key=lambda x: x[2])
        
        return score, unusual_bigrams
    
    def _analyze_trigrams(self, words: List[str]) -> Tuple[float, List[Tuple[str, str, str, float]]]:
        """
        Analyze trigram patterns.
        
        Returns:
            (score, unusual_trigrams) where score is 0-1
        """
        trigrams = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]
        
        if not trigrams:
            return 0.0, []
        
        unusual_trigrams = []
        total_unusual = 0
        
        for trigram in trigrams:
            # Get expected probability
            expected_prob = self.trigram_baseline.get(trigram, 0.001)  # Default: 0.1%
            
            # Count this trigram in text
            trigram_count = trigrams.count(trigram)
            observed_prob = trigram_count / len(trigrams)
            
            # Check if unusual
            if expected_prob < self.unusual_trigram_threshold:
                unusual_trigrams.append((trigram[0], trigram[1], trigram[2], expected_prob))
                total_unusual += 1
            elif observed_prob > expected_prob * 3:
                unusual_trigrams.append((trigram[0], trigram[1], trigram[2], observed_prob))
                total_unusual += 1
        
        # Remove duplicates
        unusual_trigrams = list(set(unusual_trigrams))
        
        # Score: proportion of unusual trigrams
        score = min(1.0, total_unusual / max(1, len(trigrams)) * 10)
        
        # Sort by probability
        unusual_trigrams.sort(key=lambda x: x[3])
        
        return score, unusual_trigrams
    
    def _detect_repetition(self, words: List[str]) -> Tuple[float, List[Tuple[str, int]]]:
        """
        Detect repetitive phrase patterns.
        
        AI models tend to repeat certain phrases more than humans.
        
        Returns:
            (score, repetitive_phrases) where score is 0-1
        """
        # Check for repeated n-grams of length 3-5
        phrase_counts = Counter()
        
        # 3-grams
        for i in range(len(words) - 2):
            phrase = " ".join(words[i:i+3])
            phrase_counts[phrase] += 1
        
        # 4-grams
        for i in range(len(words) - 3):
            phrase = " ".join(words[i:i+4])
            phrase_counts[phrase] += 1
        
        # 5-grams
        for i in range(len(words) - 4):
            phrase = " ".join(words[i:i+5])
            phrase_counts[phrase] += 1
        
        # Find phrases repeated more than threshold
        repetitive = [(phrase, count) for phrase, count in phrase_counts.items() 
                     if count >= self.repetition_threshold]
        
        # Sort by count (most repetitive first)
        repetitive.sort(key=lambda x: x[1], reverse=True)
        
        # Score: proportion of words in repetitive phrases
        total_repetitive_words = sum(len(phrase.split()) * count for phrase, count in repetitive)
        score = min(1.0, total_repetitive_words / max(1, len(words)))
        
        return score, repetitive
    
    def _calculate_transition_anomalies(self, words: List[str]) -> float:
        """
        Calculate overall transition probability anomaly score.
        
        Uses perplexity-like measure: do word transitions seem natural?
        
        Returns:
            Score 0-1, where higher means more anomalous
        """
        bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
        
        if not bigrams:
            return 0.0
        
        # Calculate average negative log probability
        total_neg_log_prob = 0.0
        
        for bigram in bigrams:
            prob = self.bigram_baseline.get(bigram, 0.01)  # Smoothing
            total_neg_log_prob += -math.log(prob)
        
        # Average perplexity
        avg_perplexity = math.exp(total_neg_log_prob / len(bigrams))
        
        # Normalize to 0-1 scale
        # Human writing: perplexity ~50-200
        # AI writing: perplexity often <30 (too predictable) or >300 (unusual transitions)
        
        if avg_perplexity < 50:
            # Too predictable (AI-like)
            score = (50 - avg_perplexity) / 50
        elif avg_perplexity > 200:
            # Too unusual (possibly AI with unusual vocabulary)
            score = min(1.0, (avg_perplexity - 200) / 200)
        else:
            # Normal range
            score = 0.0
        
        return score


# Convenience function
def analyze_language_model(text: str) -> LanguageModelResult:
    """
    Analyze text using language modeling.
    
    Args:
        text: Text to analyze
        
    Returns:
        LanguageModelResult with detailed scores
    """
    model = LanguageModel()
    return model.analyze(text)
