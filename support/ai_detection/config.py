"""Configuration for AI text detection."""

import yaml
from pathlib import Path
from typing import Dict, List


# Default AI-typical words
AI_WORDS = {
    "high_risk": [
        "delve", "delving", "delved",
        "leverage", "leveraging", "leveraged",
        "utilize", "utilizes", "utilizing", "utilized", "utilization",
    ],
    "medium_risk": [
        "robust", "robustly", "robustness",
        "comprehensive", "comprehensively",
        "facilitate", "facilitates", "facilitating", "facilitated",
        "substantial", "substantially",
        "considerable", "considerably",
        "innovative", "innovatively",
        "cutting-edge",
        "state-of-the-art",
        "demonstrate", "demonstrates", "demonstrating", "demonstrated",
        "implement", "implements", "implementing", "implemented",
        "enhance", "enhances", "enhancing", "enhanced",
    ],
    "transitions": [
        "furthermore",
        "moreover",
        "additionally",
        "consequently",
        "subsequently",
        "nevertheless",
        "nonetheless",
        "therefore",
        "thus",
        "hence",
    ],
}

# Detection weights (must sum to 1.0)
DEFAULT_WEIGHTS = {
    "grammar_perfection": 0.20,
    "sentence_uniformity": 0.25,
    "paragraph_structure": 0.20,
    "ai_word_frequency": 0.25,
    "punctuation_patterns": 0.10,
}

# Thresholds
DEFAULT_THRESHOLDS = {
    "ai_words_per_1000": 3.0,
    "human_baseline_per_1000": 1.5,
    "block_threshold": 0.70,
    "warn_threshold": 0.30,
}


class AICheckConfig:
    """Configuration manager for AI-check."""
    
    def __init__(self, config_path: str = None):
        """Load configuration from file or use defaults."""
        self.weights = DEFAULT_WEIGHTS.copy()
        self.thresholds = DEFAULT_THRESHOLDS.copy()
        self.ai_words = AI_WORDS.copy()
        
        if config_path and Path(config_path).exists():
            self.load_from_file(config_path)
    
    def load_from_file(self, config_path: str):
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        # Update detection parameters
        if "detection" in config:
            if "weights" in config["detection"]:
                self.weights.update(config["detection"]["weights"])
            if "ai_words" in config["detection"]:
                # Merge with defaults
                for category, words in config["detection"]["ai_words"].items():
                    if category in self.ai_words:
                        self.ai_words[category].extend(words)
                    else:
                        self.ai_words[category] = words
            if "ai_words_per_1000_threshold" in config["detection"]:
                self.thresholds["ai_words_per_1000"] = config["detection"]["ai_words_per_1000_threshold"]
            if "human_baseline_per_1000" in config["detection"]:
                self.thresholds["human_baseline_per_1000"] = config["detection"]["human_baseline_per_1000"]
        
        # Update pre-commit thresholds
        if "pre_commit" in config:
            if "block_threshold" in config["pre_commit"]:
                self.thresholds["block_threshold"] = config["pre_commit"]["block_threshold"]
            if "warn_threshold" in config["pre_commit"]:
                self.thresholds["warn_threshold"] = config["pre_commit"]["warn_threshold"]
    
    def get_all_ai_words(self) -> List[str]:
        """Get flat list of all AI-typical words."""
        all_words = []
        for category_words in self.ai_words.values():
            all_words.extend(category_words)
        return list(set(all_words))
    
    def get_word_weight(self, word: str) -> float:
        """Get weight for a specific AI word."""
        word_lower = word.lower()
        if word_lower in self.ai_words.get("high_risk", []):
            return 3.0
        elif word_lower in self.ai_words.get("medium_risk", []):
            return 2.0
        elif word_lower in self.ai_words.get("transitions", []):
            return 1.5
        return 1.0


# Global default config instance
default_config = AICheckConfig()
