"""Track AI-check results over time."""

import json
import sqlite3
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from .models import DetectionResult


class AICheckTracker:
    """Track AI-check results in local database."""
    
    def __init__(self, db_path: str = ".research_workflow/ai_check_history.db"):
        """Initialize tracker with database path."""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_database()
    
    def _init_database(self):
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS ai_check_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT NOT NULL,
                    git_commit TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    overall_confidence REAL,
                    grammar_score REAL,
                    sentence_score REAL,
                    paragraph_score REAL,
                    word_frequency_score REAL,
                    punctuation_score REAL,
                    ai_words_found TEXT,  -- JSON
                    patterns_detected TEXT,  -- JSON
                    total_words INTEGER,
                    ai_words_per_1000 REAL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_file_path 
                ON ai_check_history(file_path)
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON ai_check_history(timestamp)
            """)
    
    def log_detection(self, result: DetectionResult, git_commit: Optional[str] = None):
        """Log a detection result to the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO ai_check_history (
                    file_path, git_commit, timestamp,
                    overall_confidence, grammar_score, sentence_score,
                    paragraph_score, word_frequency_score, punctuation_score,
                    ai_words_found, patterns_detected, total_words, ai_words_per_1000
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                result.file_path,
                git_commit,
                result.timestamp.isoformat(),
                result.overall_confidence,
                result.grammar_score,
                result.sentence_score,
                result.paragraph_score,
                result.word_frequency_score,
                result.punctuation_score,
                json.dumps(result.ai_words_found),
                json.dumps(result.patterns_detected),
                result.total_words,
                result.ai_words_per_1000,
            ))
    
    def get_history(self, file_path: str, limit: int = 10) -> List[dict]:
        """Get detection history for a file."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT * FROM ai_check_history
                WHERE file_path = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (file_path, limit))
            
            results = []
            for row in cursor:
                results.append({
                    "timestamp": row["timestamp"],
                    "git_commit": row["git_commit"],
                    "overall_confidence": row["overall_confidence"],
                    "ai_words_per_1000": row["ai_words_per_1000"],
                    "patterns": json.loads(row["patterns_detected"]) if row["patterns_detected"] else [],
                })
            
            return results
    
    def generate_trend_report(self, file_path: str) -> dict:
        """Generate trend analysis for a file."""
        history = self.get_history(file_path, limit=100)
        
        if not history:
            return {"error": "No history found"}
        
        # Calculate trend
        confidences = [h["overall_confidence"] for h in history]
        
        trend = "improving" if len(confidences) > 1 and confidences[0] < confidences[-1] else "stable"
        if len(confidences) > 2:
            recent_avg = sum(confidences[:3]) / 3
            older_avg = sum(confidences[3:6]) / min(3, len(confidences) - 3) if len(confidences) > 3 else recent_avg
            
            if recent_avg < older_avg * 0.8:
                trend = "improving"
            elif recent_avg > older_avg * 1.2:
                trend = "worsening"
        
        return {
            "file_path": file_path,
            "check_count": len(history),
            "current_confidence": confidences[0] if confidences else 0,
            "trend": trend,
            "history": history[:5],  # Last 5 checks
        }
