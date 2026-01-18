"""
Citation Pattern Analysis for AI Text Detection

Analyzes citation usage patterns to detect AI-generated text.
AI models exhibit distinct citation patterns different from human academics.
"""

from typing import List, Dict, Tuple, Set
from dataclasses import dataclass
import re
from collections import Counter


@dataclass
class CitationResult:
    """Results from citation pattern analysis."""
    total_citations: int
    unique_citations: int
    citation_density: float  # Citations per 1000 words
    front_loading_score: float  # 0-1, higher = more front-loaded (AI-like)
    generic_frame_score: float  # 0-1, higher = more generic frames (AI-like)
    cluster_score: float  # 0-1, higher = more clustered (AI-like)
    citation_diversity: float  # 0-1, higher = more diverse (human-like)
    overall_ai_score: float  # 0-1, higher = more likely AI
    generic_frames_found: List[str]  # Generic citation frames detected
    citation_positions: List[int]  # Positions of citations (word indices)
    citation_contexts: List[str]  # Text around each citation


class CitationAnalyzer:
    """
    Analyzes citation patterns in academic text.
    
    AI-generated text exhibits distinct patterns:
    1. Front-loads citations (more in first 1/3 of text)
    2. Uses generic citation frames ("as noted by", "according to")
    3. Citations often clustered rather than evenly distributed
    4. Lower citation diversity (reuses same sources)
    """
    
    def __init__(self):
        """Initialize with pattern definitions."""
        # Generic citation frames AI commonly uses
        self.generic_frames = [
            "as noted by",
            "as shown by",
            "as demonstrated by",
            "according to",
            "as stated by",
            "as mentioned by",
            "as discussed by",
            "as reported by",
            "as indicated by",
            "as suggested by",
            "as described by",
            "as explained by",
            "previous research has shown",
            "studies have shown",
            "research has demonstrated",
            "it has been shown",
            "it has been demonstrated",
        ]
        
        # Citation patterns (various formats)
        # (Author, Year), Author (Year), [1], [Author, Year], etc.
        self.citation_patterns = [
            r'\([A-Z][a-z]+(?:\s+(?:et\s+al\.|and\s+[A-Z][a-z]+))?,?\s+\d{4}[a-z]?\)',  # (Smith, 2020)
            r'[A-Z][a-z]+(?:\s+(?:et\s+al\.|and\s+[A-Z][a-z]+))?\s+\(\d{4}[a-z]?\)',  # Smith (2020)
            r'\[\d+\]',  # [1]
            r'\[[A-Z][a-z]+(?:\s+(?:et\s+al\.))?,?\s+\d{4}[a-z]?\]',  # [Smith, 2020]
        ]
        
        # Context window around citations (words before/after)
        self.context_window = 10
    
    def analyze(self, text: str) -> CitationResult:
        """
        Analyze citation patterns in text.
        
        Args:
            text: Academic text to analyze
            
        Returns:
            CitationResult with detailed metrics
        """
        # Find all citations
        citations, positions, contexts = self._find_citations(text)
        
        if not citations:
            return self._empty_result()
        
        words = text.split()
        total_words = len(words)
        
        # Calculate metrics
        total_citations = len(citations)
        unique_citations = len(set(citations))
        citation_density = (total_citations / max(1, total_words)) * 1000
        
        # Front-loading score
        front_loading_score = self._calculate_front_loading(positions, total_words)
        
        # Generic frame score
        generic_frame_score, generic_frames_found = self._check_generic_frames(text, contexts)
        
        # Clustering score
        cluster_score = self._calculate_clustering(positions, total_words)
        
        # Citation diversity
        citation_diversity = unique_citations / max(1, total_citations)
        
        # Overall AI score
        overall_ai_score = self._calculate_overall_score(
            front_loading_score,
            generic_frame_score,
            cluster_score,
            citation_diversity
        )
        
        return CitationResult(
            total_citations=total_citations,
            unique_citations=unique_citations,
            citation_density=citation_density,
            front_loading_score=front_loading_score,
            generic_frame_score=generic_frame_score,
            cluster_score=cluster_score,
            citation_diversity=citation_diversity,
            overall_ai_score=overall_ai_score,
            generic_frames_found=generic_frames_found,
            citation_positions=positions,
            citation_contexts=contexts[:10]  # First 10 for review
        )
    
    def _find_citations(self, text: str) -> Tuple[List[str], List[int], List[str]]:
        """
        Find all citations in text.
        
        Returns:
            (citations, positions, contexts)
            - citations: List of citation strings
            - positions: Word positions of citations
            - contexts: Text context around each citation
        """
        citations = []
        positions = []
        contexts = []
        
        words = text.split()
        
        # Search for each pattern
        for pattern in self.citation_patterns:
            for match in re.finditer(pattern, text):
                citation_text = match.group()
                citations.append(citation_text)
                
                # Calculate word position
                char_position = match.start()
                word_position = len(text[:char_position].split())
                positions.append(word_position)
                
                # Extract context
                start_word = max(0, word_position - self.context_window)
                end_word = min(len(words), word_position + self.context_window)
                context = " ".join(words[start_word:end_word])
                contexts.append(context)
        
        # Sort by position
        sorted_data = sorted(zip(positions, citations, contexts))
        if sorted_data:
            positions, citations, contexts = zip(*sorted_data)
            return list(citations), list(positions), list(contexts)
        
        return [], [], []
    
    def _calculate_front_loading(self, positions: List[int], total_words: int) -> float:
        """
        Calculate front-loading score.
        
        AI tends to put more citations in first 1/3 of text.
        
        Args:
            positions: Word positions of citations
            total_words: Total words in text
            
        Returns:
            Score 0-1 (higher = more front-loaded = more AI-like)
        """
        if not positions or total_words == 0:
            return 0.0
        
        # Count citations in first third
        first_third = total_words / 3
        citations_in_first_third = sum(1 for pos in positions if pos < first_third)
        
        # Expected proportion: 1/3 (evenly distributed)
        # Observed proportion
        observed_proportion = citations_in_first_third / len(positions)
        
        # If more than 50% are in first third, that's front-loading
        if observed_proportion > 0.5:
            # Scale: 0.5 -> 0, 1.0 -> 1.0
            score = (observed_proportion - 0.5) * 2
            return min(1.0, score)
        
        return 0.0
    
    def _check_generic_frames(self, text: str, contexts: List[str]) -> Tuple[float, List[str]]:
        """
        Check for generic citation frames.
        
        AI commonly uses formulaic citation introductions.
        
        Returns:
            (score, frames_found)
        """
        text_lower = text.lower()
        found_frames = []
        
        for frame in self.generic_frames:
            if frame in text_lower:
                found_frames.append(frame)
        
        # Score: proportion of citations with generic frames
        if not contexts:
            return 0.0, []
        
        contexts_with_frames = sum(
            1 for context in contexts
            if any(frame in context.lower() for frame in self.generic_frames)
        )
        
        score = contexts_with_frames / len(contexts)
        
        return score, found_frames
    
    def _calculate_clustering(self, positions: List[int], total_words: int) -> float:
        """
        Calculate citation clustering score.
        
        AI tends to cluster citations rather than distribute evenly.
        
        Uses coefficient of variation of inter-citation distances.
        
        Returns:
            Score 0-1 (higher = more clustered = more AI-like)
        """
        if len(positions) < 2:
            return 0.0
        
        # Calculate distances between consecutive citations
        distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
        
        if not distances:
            return 0.0
        
        # Calculate mean and standard deviation
        mean_distance = sum(distances) / len(distances)
        
        if mean_distance == 0:
            return 1.0  # Extremely clustered
        
        variance = sum((d - mean_distance) ** 2 for d in distances) / len(distances)
        std_dev = variance ** 0.5
        
        # Coefficient of variation
        cv = std_dev / mean_distance
        
        # High CV means high clustering (some very close, some very far)
        # Typical human writing: CV around 0.5-1.0
        # AI writing: CV often > 1.5 or < 0.3
        
        if cv > 1.5:
            # High clustering
            return min(1.0, (cv - 1.5) / 1.5)
        elif cv < 0.3:
            # Too uniform (also suspicious)
            return (0.3 - cv) / 0.3
        
        return 0.0
    
    def _calculate_overall_score(
        self,
        front_loading: float,
        generic_frames: float,
        clustering: float,
        diversity: float
    ) -> float:
        """
        Calculate overall AI likelihood from citation patterns.
        
        Returns:
            Score 0-1 (higher = more likely AI)
        """
        # Combine signals with weights
        score = (
            0.30 * front_loading +       # Front-loading is moderately indicative
            0.40 * generic_frames +       # Generic frames are strongly indicative
            0.20 * clustering +           # Clustering is moderately indicative
            0.10 * (1 - diversity)        # Low diversity is weakly indicative
        )
        
        return min(1.0, score)
    
    def _empty_result(self) -> CitationResult:
        """Return empty result for text with no citations."""
        return CitationResult(
            total_citations=0,
            unique_citations=0,
            citation_density=0.0,
            front_loading_score=0.0,
            generic_frame_score=0.0,
            cluster_score=0.0,
            citation_diversity=0.0,
            overall_ai_score=0.0,
            generic_frames_found=[],
            citation_positions=[],
            citation_contexts=[]
        )


# Convenience function
def analyze_citations(text: str) -> CitationResult:
    """
    Analyze citation patterns in text.
    
    Args:
        text: Academic text to analyze
        
    Returns:
        CitationResult with detailed metrics
    """
    analyzer = CitationAnalyzer()
    return analyzer.analyze(text)
