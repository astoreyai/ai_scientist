"""
Enhanced AI Text Detector - Version 1.1.0

Integrates multiple detection methods:
1. Original detection (grammar, sentence, paragraph, word frequency, punctuation)
2. N-gram language modeling  
3. Sentence complexity analysis
4. Citation pattern analysis
5. Adaptive thresholding based on user history
"""

import re
from typing import List, Dict, Tuple, Optional
from datetime import datetime
from collections import Counter
import statistics
import json
from pathlib import Path

from .models import DetectionResult, TextSegment
from .config import AICheckConfig, default_config
from .detector import AITextDetector
from .language_model import LanguageModel, LanguageModelResult
from .complexity import ComplexityAnalyzer, ComplexityResult
from .citation_analysis import CitationAnalyzer, CitationResult


class EnhancedAITextDetector:
    """
    Enhanced AI text detector with multiple detection methods.
    
    Combines:
    - Original 5-method detection
    - N-gram language modeling
    - Complexity analysis
    - Citation pattern analysis
    - Adaptive thresholding
    """
    
    def __init__(self, config: AICheckConfig = None, user_profile_path: Optional[str] = None):
        """
        Initialize enhanced detector.
        
        Args:
            config: AI-check configuration
            user_profile_path: Path to user's writing history profile (for adaptive thresholding)
        """
        self.config = config or default_config
        self.user_profile_path = user_profile_path
        
        # Initialize component detectors
        self.base_detector = AITextDetector(config)
        self.language_model = LanguageModel()
        self.complexity_analyzer = ComplexityAnalyzer()
        self.citation_analyzer = CitationAnalyzer()
        
        # Load user profile if available
        self.user_profile = self._load_user_profile() if user_profile_path else None
    
    def analyze(self, text: str, file_path: str = "") -> Dict:
        """
        Perform comprehensive AI-detection analysis.
        
        Args:
            text: Text to analyze
            file_path: Optional file path for context
            
        Returns:
            Dictionary with all detection results and overall assessment
        """
        # Run all detection methods
        base_result = self.base_detector.analyze(text, file_path)
        language_result = self.language_model.analyze(text)
        complexity_result = self.complexity_analyzer.analyze(text)
        citation_result = self.citation_analyzer.analyze(text)
        
        # Calculate enhanced overall confidence
        enhanced_confidence = self._calculate_enhanced_confidence(
            base_result,
            language_result,
            complexity_result,
            citation_result
        )
        
        # Apply adaptive thresholding if user profile exists
        if self.user_profile:
            adjusted_confidence = self._apply_adaptive_threshold(
                enhanced_confidence,
                language_result,
                complexity_result
            )
        else:
            adjusted_confidence = enhanced_confidence
        
        # Generate comprehensive assessment
        assessment = self._generate_assessment(
            adjusted_confidence,
            base_result,
            language_result,
            complexity_result,
            citation_result
        )
        
        # Update user profile
        if self.user_profile_path:
            self._update_user_profile(text, language_result, complexity_result)
        
        return {
            "file_path": file_path,
            "timestamp": datetime.now().isoformat(),
            "overall_confidence": adjusted_confidence,
            "base_confidence": base_result.overall_confidence,
            "enhanced_confidence": enhanced_confidence,
            "assessment": assessment,
            
            # Component results
            "base_detection": {
                "grammar_score": base_result.grammar_score,
                "sentence_score": base_result.sentence_score,
                "paragraph_score": base_result.paragraph_score,
                "word_frequency_score": base_result.word_frequency_score,
                "punctuation_score": base_result.punctuation_score,
                "ai_words_found": dict(base_result.ai_words_found),
                "ai_words_per_1000": (sum(base_result.ai_words_found.values()) / 
                                     max(1, len(text.split())) * 1000)
            },
            
            "language_model": {
                "bigram_score": language_result.bigram_score,
                "trigram_score": language_result.trigram_score,
                "transition_anomaly_score": language_result.transition_anomaly_score,
                "repetition_score": language_result.repetition_score,
                "unusual_bigrams": language_result.unusual_bigrams[:5],
                "unusual_trigrams": language_result.unusual_trigrams[:5],
                "repetitive_phrases": language_result.repetitive_phrases[:5]
            },
            
            "complexity": {
                "flesch_kincaid_grade": complexity_result.flesch_kincaid_grade,
                "gunning_fog_index": complexity_result.gunning_fog_index,
                "complexity_variance": complexity_result.complexity_variance,
                "uniformity_score": complexity_result.uniformity_score,
                "readability_score": complexity_result.readability_score,
                "avg_sentence_length": complexity_result.avg_sentence_length
            },
            
            "citations": {
                "total_citations": citation_result.total_citations,
                "unique_citations": citation_result.unique_citations,
                "citation_density": citation_result.citation_density,
                "front_loading_score": citation_result.front_loading_score,
                "generic_frame_score": citation_result.generic_frame_score,
                "cluster_score": citation_result.cluster_score,
                "citation_diversity": citation_result.citation_diversity,
                "generic_frames_found": citation_result.generic_frames_found
            },
            
            # Metadata
            "detection_version": "1.1.0",
            "user_profile_used": self.user_profile is not None
        }
    
    def _calculate_enhanced_confidence(
        self,
        base_result: DetectionResult,
        language_result: LanguageModelResult,
        complexity_result: ComplexityResult,
        citation_result: CitationResult
    ) -> float:
        """
        Calculate enhanced overall confidence combining all methods.
        
        Weights:
        - Base detection (original 5 methods): 40%
        - Language modeling: 25%
        - Complexity analysis: 20%
        - Citation patterns: 15%
        
        Returns:
            Overall confidence 0-1
        """
        confidence = (
            0.40 * base_result.overall_confidence +
            0.25 * language_result.overall_score +
            0.20 * complexity_result.overall_ai_score +
            0.15 * citation_result.overall_ai_score
        )
        
        return min(1.0, confidence)
    
    def _apply_adaptive_threshold(
        self,
        confidence: float,
        language_result: LanguageModelResult,
        complexity_result: ComplexityResult
    ) -> float:
        """
        Apply adaptive thresholding based on user's writing history.
        
        Personalizes detection to individual writing style.
        
        Returns:
            Adjusted confidence score
        """
        if not self.user_profile:
            return confidence
        
        # Compare current text to user's baseline
        baseline_complexity = self.user_profile.get("avg_complexity_variance", 5.0)
        baseline_perplexity = self.user_profile.get("avg_perplexity", 100.0)
        
        current_complexity = complexity_result.complexity_variance
        
        # Calculate deviation from user's normal style
        complexity_deviation = abs(current_complexity - baseline_complexity) / max(1, baseline_complexity)
        
        # Adjust confidence based on deviation
        # If text matches user's usual style, decrease AI confidence
        # If text deviates significantly, increase AI confidence
        
        if complexity_deviation < 0.2:
            # Very similar to user's usual style - likely authentic
            adjustment = -0.15
        elif complexity_deviation < 0.4:
            # Somewhat similar - slight decrease
            adjustment = -0.05
        elif complexity_deviation > 0.8:
            # Very different from usual - increase suspicion
            adjustment = 0.15
        else:
            # Moderately different
            adjustment = 0.0
        
        adjusted = confidence + adjustment
        return max(0.0, min(1.0, adjusted))
    
    def _generate_assessment(
        self,
        confidence: float,
        base_result: DetectionResult,
        language_result: LanguageModelResult,
        complexity_result: ComplexityResult,
        citation_result: CitationResult
    ) -> str:
        """
        Generate human-readable assessment of detection results.
        
        Returns:
            Assessment string
        """
        if confidence < 0.30:
            level = "LOW"
            verdict = "Likely human-written"
        elif confidence < 0.70:
            level = "MEDIUM"
            verdict = "Possible AI assistance"
        else:
            level = "HIGH"
            verdict = "Likely AI-generated"
        
        # Build detailed findings
        findings = []
        
        # Base detection findings
        if base_result.word_frequency_score > 0.6:
            ai_word_count = sum(base_result.ai_words_found.values())
            findings.append(f"Contains {ai_word_count} AI-typical words")
        
        if base_result.sentence_score > 0.7:
            findings.append("Excessive sentence uniformity detected")
        
        # Language model findings
        if language_result.repetition_score > 0.5:
            findings.append(f"Repetitive phrases detected ({len(language_result.repetitive_phrases)} instances)")
        
        if language_result.transition_anomaly_score > 0.6:
            findings.append("Unusual word transition patterns")
        
        # Complexity findings
        if complexity_result.uniformity_score > 0.7:
            findings.append(f"Very uniform complexity (variance: {complexity_result.complexity_variance:.2f})")
        
        # Citation findings
        if citation_result.generic_frame_score > 0.5:
            findings.append(f"Generic citation frames detected ({len(citation_result.generic_frames_found)} types)")
        
        if citation_result.front_loading_score > 0.6:
            findings.append("Citations front-loaded in text")
        
        # Combine into assessment
        assessment = f"{level} confidence ({confidence:.1%}): {verdict}\n"
        
        if findings:
            assessment += "\nKey findings:\n"
            for finding in findings:
                assessment += f"  • {finding}\n"
        
        return assessment.strip()
    
    def _load_user_profile(self) -> Optional[Dict]:
        """
        Load user's writing history profile.
        
        Returns:
            User profile dictionary or None
        """
        try:
            path = Path(self.user_profile_path)
            if path.exists():
                with open(path, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        
        return None
    
    def _update_user_profile(
        self,
        text: str,
        language_result: LanguageModelResult,
        complexity_result: ComplexityResult
    ):
        """
        Update user's writing profile with current text.
        
        Builds personalized baseline over time.
        """
        # Load existing profile or create new
        profile = self.user_profile or {
            "samples": 0,
            "total_complexity_variance": 0.0,
            "total_perplexity": 0.0,
            "avg_complexity_variance": 0.0,
            "avg_perplexity": 0.0
        }
        
        # Update with current sample
        profile["samples"] += 1
        profile["total_complexity_variance"] += complexity_result.complexity_variance
        
        # Recalculate averages
        profile["avg_complexity_variance"] = profile["total_complexity_variance"] / profile["samples"]
        
        # Save updated profile
        try:
            path = Path(self.user_profile_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w') as f:
                json.dump(profile, f, indent=2)
        except Exception:
            pass  # Fail silently if can't save


# Convenience function
def analyze_enhanced(text: str, file_path: str = "", user_profile_path: Optional[str] = None) -> Dict:
    """
    Analyze text using enhanced AI detection.
    
    Args:
        text: Text to analyze
        file_path: Optional file path
        user_profile_path: Optional path to user writing profile
        
    Returns:
        Comprehensive detection results
    """
    detector = EnhancedAITextDetector(user_profile_path=user_profile_path)
    return detector.analyze(text, file_path)
