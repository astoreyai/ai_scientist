"""
Quality Assurance System

Comprehensive QA for research integrity, reproducibility, and rigor.
"""

from .base import ValidationResult, QAReport, BaseValidator
from .reproducibility_validator import ReproducibilityValidator
from .citation_verifier import CitationVerifier
from .statistical_validator import StatisticalValidator
from .qa_manager import QAManager

__all__ = [
    "ValidationResult",
    "QAReport",
    "BaseValidator",
    "ReproducibilityValidator",
    "CitationVerifier",
    "StatisticalValidator",
    "QAManager",
]
