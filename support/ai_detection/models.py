"""Data models for AI text detection."""

from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime


@dataclass
class TextSegment:
    """A segment of text with AI-detection metadata."""
    
    start_line: int
    end_line: int
    content: str
    confidence: float
    patterns: List[str] = field(default_factory=list)
    ai_words: List[str] = field(default_factory=list)


@dataclass
class DetectionResult:
    """Complete AI-detection analysis result."""
    
    file_path: str
    timestamp: datetime
    overall_confidence: float
    
    # Individual metric scores
    grammar_score: float
    sentence_score: float
    paragraph_score: float
    word_frequency_score: float
    punctuation_score: float
    
    # Detailed findings
    flagged_sections: List[TextSegment] = field(default_factory=list)
    ai_words_found: Dict[str, int] = field(default_factory=dict)
    patterns_detected: List[str] = field(default_factory=list)
    
    # Statistics
    total_words: int = 0
    ai_words_per_1000: float = 0.0
    avg_sentence_length: float = 0.0
    sentence_length_variance: float = 0.0
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "file_path": self.file_path,
            "timestamp": self.timestamp.isoformat(),
            "overall_confidence": self.overall_confidence,
            "scores": {
                "grammar": self.grammar_score,
                "sentence": self.sentence_score,
                "paragraph": self.paragraph_score,
                "word_frequency": self.word_frequency_score,
                "punctuation": self.punctuation_score,
            },
            "flagged_sections": [
                {
                    "lines": f"{seg.start_line}-{seg.end_line}",
                    "confidence": seg.confidence,
                    "patterns": seg.patterns,
                    "ai_words": seg.ai_words,
                }
                for seg in self.flagged_sections
            ],
            "ai_words_found": self.ai_words_found,
            "statistics": {
                "total_words": self.total_words,
                "ai_words_per_1000": self.ai_words_per_1000,
                "avg_sentence_length": self.avg_sentence_length,
                "sentence_variance": self.sentence_length_variance,
            },
        }


@dataclass
class Suggestion:
    """A suggestion for improving detected AI patterns."""
    
    category: str  # "word_choice", "sentence_structure", "paragraph_flow"
    issue: str
    suggestion: str
    example_before: str = ""
    example_after: str = ""
    priority: str = "medium"  # "low", "medium", "high"
