"""
AI-Generated Text Detection Library

Provides tools for detecting LLM-generated text patterns in academic writing.
"""

from .detector import AITextDetector
from .models import DetectionResult, TextSegment, Suggestion
from .suggestions import SuggestionGenerator
from .tracker import AICheckTracker

__version__ = "1.0.0"

__all__ = [
    "AITextDetector",
    "DetectionResult",
    "TextSegment",
    "Suggestion",
    "SuggestionGenerator",
    "AICheckTracker",
]
