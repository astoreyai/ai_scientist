"""Core AI text detection logic."""

import re
from typing import List, Dict, Tuple
from datetime import datetime
from collections import Counter
import statistics

from .models import DetectionResult, TextSegment
from .config import AICheckConfig, default_config


class AITextDetector:
    """Detect AI-generated text patterns."""
    
    def __init__(self, config: AICheckConfig = None):
        """Initialize detector with configuration."""
        self.config = config or default_config
    
    def analyze(self, text: str, file_path: str = "") -> DetectionResult:
        """Perform complete AI-detection analysis on text."""
        
        # Calculate individual metrics
        grammar_score = self.check_grammar_patterns(text)
        sentence_score = self.check_sentence_uniformity(text)
        paragraph_score = self.check_paragraph_structure(text)
        word_freq_score, ai_words_found = self.check_word_frequency(text)
        punct_score = self.check_punctuation_patterns(text)
        
        # Calculate overall confidence
        overall_confidence = self._calculate_overall_confidence(
            grammar_score, sentence_score, paragraph_score,
            word_freq_score, punct_score
        )
        
        # Get text statistics
        total_words = len(re.findall(r'\b\w+\b', text))
        sentences = self._split_sentences(text)
        avg_sentence_length = statistics.mean([len(re.findall(r'\b\w+\b', s)) for s in sentences]) if sentences else 0
        sentence_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
        sentence_variance = statistics.variance(sentence_lengths) if len(sentence_lengths) > 1 else 0
        
        # Calculate AI words per 1000
        total_ai_words = sum(ai_words_found.values())
        ai_words_per_1000 = (total_ai_words / total_words * 1000) if total_words > 0 else 0
        
        # Identify flagged sections
        flagged_sections = self._identify_flagged_sections(text, overall_confidence)
        
        # Detect patterns
        patterns = self._detect_patterns(text, grammar_score, sentence_score, 
                                        paragraph_score, word_freq_score, punct_score)
        
        return DetectionResult(
            file_path=file_path,
            timestamp=datetime.now(),
            overall_confidence=overall_confidence,
            grammar_score=grammar_score,
            sentence_score=sentence_score,
            paragraph_score=paragraph_score,
            word_frequency_score=word_freq_score,
            punctuation_score=punct_score,
            flagged_sections=flagged_sections,
            ai_words_found=ai_words_found,
            patterns_detected=patterns,
            total_words=total_words,
            ai_words_per_1000=ai_words_per_1000,
            avg_sentence_length=avg_sentence_length,
            sentence_length_variance=sentence_variance,
        )
    
    def check_grammar_patterns(self, text: str) -> float:
        """
        Check for suspicious grammar perfection.
        Returns score 0-100 (higher = more AI-like).
        """
        score = 0.0
        
        # Count potential grammar issues (absence indicates perfection)
        # Real human writing has these occasionally
        
        # Check for any typos or common mistakes
        common_mistakes = [
            r'\bits\s',  # "its" vs "it's" errors
            r'\btheir\s', r'\bthere\s', r'\bthey\'re\s',  # their/there/they're
            r'\byour\s', r'\byou\'re\s',  # your/you're
            r',\s*which\s',  # comma before which (often correct, but varies)
        ]
        
        mistake_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in common_mistakes)
        
        # If text is long (>1000 words) with zero variation, suspicious
        word_count = len(re.findall(r'\b\w+\b', text))
        if word_count > 1000:
            if mistake_count == 0:
                score += 40.0  # Very suspicious for long text
            elif mistake_count < word_count * 0.001:  # Less than 1 per 1000 words
                score += 25.0
        
        # Check for perfect comma usage (very complex to detect, simplified)
        # Count commas vs. independent clauses (rough heuristic)
        comma_count = text.count(',')
        sentence_count = len(self._split_sentences(text))
        
        if sentence_count > 0:
            commas_per_sentence = comma_count / sentence_count
            # AI tends to use 1-2 commas per sentence very consistently
            if 0.8 <= commas_per_sentence <= 2.2:
                score += 15.0
        
        # Check for consistent formal register
        informal_markers = [
            r'\b(OK|ok|okay)\b',
            r'\b(yeah|yep|nope)\b',
            r'\b(gonna|wanna|gotta)\b',
            r'\b(kinda|sorta)\b',
            r'!!+',  # Multiple exclamation marks
            r'\?+',  # Multiple question marks
        ]
        
        informal_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) 
                           for pattern in informal_markers)
        
        if word_count > 500 and informal_count == 0:
            score += 20.0  # No informal elements in long text is suspicious
        
        return min(score, 100.0)
    
    def check_sentence_uniformity(self, text: str) -> float:
        """
        Check for suspicious sentence length uniformity.
        Returns score 0-100 (higher = more AI-like).
        """
        sentences = self._split_sentences(text)
        
        if len(sentences) < 5:
            return 0.0  # Too few sentences to judge
        
        # Count words in each sentence
        sentence_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
        
        if not sentence_lengths:
            return 0.0
        
        score = 0.0
        
        # Check for AI sweet spot (15-25 words)
        sweet_spot_count = sum(1 for length in sentence_lengths if 15 <= length <= 25)
        sweet_spot_ratio = sweet_spot_count / len(sentence_lengths)
        
        if sweet_spot_ratio > 0.6:
            score += 40.0  # Very suspicious
        elif sweet_spot_ratio > 0.4:
            score += 25.0
        
        # Check variance (low variance = suspicious uniformity)
        if len(sentence_lengths) > 1:
            variance = statistics.variance(sentence_lengths)
            mean_length = statistics.mean(sentence_lengths)
            
            # Coefficient of variation
            cv = (variance ** 0.5) / mean_length if mean_length > 0 else 0
            
            # Human writing typically has CV > 0.4
            # AI writing often has CV < 0.3
            if cv < 0.2:
                score += 35.0
            elif cv < 0.3:
                score += 20.0
        
        # Check for repetitive sentence starters
        starters = []
        for sentence in sentences:
            words = sentence.strip().split()
            if words:
                starter = words[0].lower()
                if len(words) > 1:
                    starter = f"{words[0].lower()} {words[1].lower()}"
                starters.append(starter)
        
        if starters:
            starter_counts = Counter(starters)
            most_common = starter_counts.most_common(1)[0][1]
            repetition_ratio = most_common / len(starters)
            
            if repetition_ratio > 0.3:
                score += 25.0  # High repetition of sentence starters
        
        return min(score, 100.0)
    
    def check_paragraph_structure(self, text: str) -> float:
        """
        Check for artificial paragraph uniformity.
        Returns score 0-100 (higher = more AI-like).
        """
        # Split by double newlines
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        if len(paragraphs) < 3:
            return 0.0  # Too few paragraphs
        
        score = 0.0
        
        # Count sentences per paragraph
        para_sentence_counts = []
        for para in paragraphs:
            sentences = self._split_sentences(para)
            para_sentence_counts.append(len(sentences))
        
        if not para_sentence_counts:
            return 0.0
        
        # Check for uniform paragraph lengths (4-6 sentences)
        uniform_count = sum(1 for count in para_sentence_counts if 4 <= count <= 6)
        uniform_ratio = uniform_count / len(para_sentence_counts)
        
        if uniform_ratio > 0.7:
            score += 40.0
        elif uniform_ratio > 0.5:
            score += 25.0
        
        # Check variance in paragraph lengths
        if len(para_sentence_counts) > 1:
            variance = statistics.variance(para_sentence_counts)
            mean_count = statistics.mean(para_sentence_counts)
            
            cv = (variance ** 0.5) / mean_count if mean_count > 0 else 0
            
            if cv < 0.3:
                score += 30.0  # Very uniform
            elif cv < 0.5:
                score += 15.0
        
        # Check for mechanical topic sentence pattern
        # (simplified: check if first sentence is consistently longer)
        first_sentences = []
        for para in paragraphs:
            sentences = self._split_sentences(para)
            if sentences:
                first_sentences.append(len(re.findall(r'\b\w+\b', sentences[0])))
        
        if len(first_sentences) > 2:
            avg_first = statistics.mean(first_sentences)
            avg_all = statistics.mean([len(re.findall(r'\b\w+\b', s)) 
                                      for para in paragraphs 
                                      for s in self._split_sentences(para)])
            
            # AI often makes first sentences consistently longer
            if avg_first > avg_all * 1.2:
                score += 20.0
        
        return min(score, 100.0)
    
    def check_word_frequency(self, text: str) -> Tuple[float, Dict[str, int]]:
        """
        Check for AI-typical word usage.
        Returns (score 0-100, dict of found words with counts).
        """
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        word_count = len(words)
        
        if word_count == 0:
            return 0.0, {}
        
        # Count AI-typical words
        ai_words_found = {}
        all_ai_words = self.config.get_all_ai_words()
        
        for ai_word in all_ai_words:
            # Use word boundary matching
            pattern = r'\b' + re.escape(ai_word.lower()) + r'\b'
            count = len(re.findall(pattern, text_lower))
            if count > 0:
                ai_words_found[ai_word] = count
        
        # Calculate weighted score
        total_ai_words = sum(ai_words_found.values())
        ai_words_per_1000 = (total_ai_words / word_count * 1000) if word_count > 0 else 0
        
        # Score based on frequency vs. human baseline
        baseline = self.config.thresholds["human_baseline_per_1000"]
        threshold = self.config.thresholds["ai_words_per_1000"]
        
        if ai_words_per_1000 >= threshold * 2:  # 2x threshold
            score = 100.0
        elif ai_words_per_1000 >= threshold:
            score = 70.0
        elif ai_words_per_1000 >= baseline * 2:
            score = 50.0
        elif ai_words_per_1000 >= baseline:
            score = 30.0
        else:
            score = 10.0
        
        # Bonus for high-risk words
        high_risk_words = self.config.ai_words.get("high_risk", [])
        high_risk_found = sum(count for word, count in ai_words_found.items() 
                             if word in high_risk_words)
        
        if high_risk_found > 0:
            score = min(score + (high_risk_found * 10), 100.0)
        
        return score, ai_words_found
    
    def check_punctuation_patterns(self, text: str) -> float:
        """
        Check for AI-typical punctuation patterns.
        Returns score 0-100 (higher = more AI-like).
        """
        score = 0.0
        
        # Count various punctuation
        semicolon_count = text.count(';')
        colon_count = text.count(':')
        em_dash_count = text.count('—')
        en_dash_count = text.count('–')
        ellipsis_count = text.count('...')
        exclamation_count = text.count('!')
        
        sentence_count = len(self._split_sentences(text))
        
        if sentence_count == 0:
            return 0.0
        
        # Excessive semicolon use
        semicolons_per_sentence = semicolon_count / sentence_count
        if semicolons_per_sentence > 0.3:
            score += 25.0
        elif semicolons_per_sentence > 0.15:
            score += 15.0
        
        # Perfect colon usage (hard to detect, simplified)
        if colon_count > 0 and colon_count < sentence_count * 0.1:
            # Some colons but not too many = potentially AI
            score += 10.0
        
        # Consistent em-dash usage
        if em_dash_count > 3:
            score += 15.0
        
        # Lack of informal punctuation in long text
        word_count = len(re.findall(r'\b\w+\b', text))
        if word_count > 500:
            if ellipsis_count == 0 and exclamation_count == 0:
                score += 20.0
        
        # Check for perfect punctuation (no spaces before punctuation errors)
        # This is a simplified check
        punctuation_errors = [
            r'\s+[,.:;!?]',  # Space before punctuation
            r'[,.:;!?]\w',   # No space after punctuation
        ]
        
        error_count = sum(len(re.findall(pattern, text)) for pattern in punctuation_errors)
        
        if word_count > 1000 and error_count == 0:
            score += 20.0  # Very suspicious for long text
        
        return min(score, 100.0)
    
    def _calculate_overall_confidence(self, grammar: float, sentence: float, 
                                     paragraph: float, word_freq: float, 
                                     punct: float) -> float:
        """Calculate weighted overall confidence score."""
        weights = self.config.weights
        
        overall = (
            grammar * weights["grammar_perfection"] +
            sentence * weights["sentence_uniformity"] +
            paragraph * weights["paragraph_structure"] +
            word_freq * weights["ai_word_frequency"] +
            punct * weights["punctuation_patterns"]
        )
        
        return overall / 100.0  # Convert to 0-1 scale
    
    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences."""
        # Simple sentence splitter (could be improved)
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _identify_flagged_sections(self, text: str, overall_confidence: float) -> List[TextSegment]:
        """Identify specific text sections with high AI confidence."""
        # Split text into paragraphs
        lines = text.split('\n')
        paragraphs = []
        current_para = []
        current_start = 0
        
        for i, line in enumerate(lines):
            if line.strip():
                current_para.append(line)
            else:
                if current_para:
                    paragraphs.append((current_start, i, '\n'.join(current_para)))
                    current_para = []
                current_start = i + 1
        
        if current_para:
            paragraphs.append((current_start, len(lines), '\n'.join(current_para)))
        
        # Analyze each paragraph
        flagged = []
        for start_line, end_line, para_text in paragraphs:
            if len(para_text.strip()) < 50:  # Skip very short paragraphs
                continue
            
            # Quick analysis of paragraph
            para_result = self.analyze(para_text)
            
            if para_result.overall_confidence > 0.6:  # High confidence threshold
                # Identify specific issues
                patterns = []
                ai_words = []
                
                if para_result.sentence_score > 60:
                    patterns.append("Uniform sentence structure")
                if para_result.word_frequency_score > 60:
                    patterns.append("AI-typical words")
                    ai_words = list(para_result.ai_words_found.keys())
                if para_result.grammar_score > 60:
                    patterns.append("Excessive perfection")
                
                segment = TextSegment(
                    start_line=start_line + 1,
                    end_line=end_line,
                    content=para_text[:200] + "..." if len(para_text) > 200 else para_text,
                    confidence=para_result.overall_confidence,
                    patterns=patterns,
                    ai_words=ai_words[:5],  # Limit to top 5
                )
                
                flagged.append(segment)
        
        return flagged
    
    def _detect_patterns(self, text: str, grammar: float, sentence: float,
                        paragraph: float, word_freq: float, punct: float) -> List[str]:
        """Detect specific AI patterns present in text."""
        patterns = []
        
        if grammar > 70:
            patterns.append("Excessive grammatical perfection")
        if sentence > 70:
            patterns.append("Uniform sentence lengths (AI sweet spot)")
        if paragraph > 70:
            patterns.append("Mechanical paragraph structure")
        if word_freq > 70:
            patterns.append("High frequency of AI-typical words")
        if punct > 70:
            patterns.append("Artificial punctuation patterns")
        
        # Check for transition word overuse
        sentences = self._split_sentences(text)
        transition_starters = 0
        transitions = self.config.ai_words.get("transitions", [])
        
        for sentence in sentences:
            first_word = sentence.strip().split()[0].lower() if sentence.strip() else ""
            if first_word in transitions:
                transition_starters += 1
        
        if len(sentences) > 0:
            transition_ratio = transition_starters / len(sentences)
            if transition_ratio > 0.5:
                patterns.append("Excessive transition words at sentence starts")
        
        return patterns
