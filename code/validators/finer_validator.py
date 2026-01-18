"""
FINER Criteria Validator

Validates problem formulation using FINER criteria:
- Feasible
- Interesting
- Novel
- Ethical
- Relevant
"""

from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_context import WorkflowContext, ValidationResult
from validators.base import BaseValidator


class FINERValidator(BaseValidator):
    """
    Validator for Problem Formulation phase using FINER criteria.

    Checks that research question satisfies FINER framework.
    """

    def __init__(self, context: WorkflowContext):
        super().__init__(context)
        self.problem_statement_path = "docs/problem_statement.md"

    def can_enter(self) -> ValidationResult:
        """
        Problem formulation is always the first phase - no entry requirements.
        """
        return ValidationResult(
            passed=True,
            score=1.0,
            details={"message": "Problem formulation is the starting phase"}
        )

    def can_exit(self) -> ValidationResult:
        """
        Check if problem formulation is complete and meets FINER criteria.

        Requirements:
        - Problem statement file exists
        - Research question present
        - FINER criteria addressed (≥4/5)
        """
        missing_items = []
        warnings = []
        blocking_issues = []
        scores = {}

        # Check if problem statement exists
        if not self._file_exists(self.problem_statement_path):
            blocking_issues.append(
                f"Problem statement file not found: {self.problem_statement_path}"
            )
            return ValidationResult(
                passed=False,
                score=0.0,
                missing_items=[self.problem_statement_path],
                blocking_issues=blocking_issues
            )

        # Read problem statement
        content = self._read_problem_statement()

        # Check for research question
        has_question = self._check_research_question(content)
        if not has_question:
            blocking_issues.append("No clear research question found")
            scores["research_question"] = 0.0
        else:
            scores["research_question"] = 1.0

        # Check FINER criteria
        finer_scores = self._evaluate_finer_criteria(content)
        scores.update(finer_scores)

        # Calculate overall score
        total_score = sum(scores.values()) / len(scores) if scores else 0.0

        # Determine pass/fail
        # Need research question + at least 4/5 FINER criteria
        finer_count = sum(1 for k, v in finer_scores.items() if v >= 0.5)
        passed = has_question and finer_count >= 4

        if not passed:
            if finer_count < 4:
                missing_items.append(
                    f"FINER criteria: Only {finer_count}/5 addressed (need ≥4)"
                )

        # Generate warnings for weak criteria
        for criterion, score in finer_scores.items():
            if score < 0.5:
                warnings.append(f"{criterion.upper()} criterion not clearly addressed")

        return ValidationResult(
            passed=passed,
            score=total_score,
            missing_items=missing_items,
            warnings=warnings,
            blocking_issues=blocking_issues,
            details={
                "finer_scores": finer_scores,
                "finer_count": finer_count,
                "all_scores": scores
            }
        )

    def _read_problem_statement(self) -> str:
        """Read problem statement file"""
        path = self.project_root / self.problem_statement_path
        with open(path, 'r') as f:
            return f.read()

    def _check_research_question(self, content: str) -> bool:
        """Check if a clear research question is present"""
        # Look for question marks or "research question" heading
        has_question_mark = '?' in content
        has_rq_heading = bool(re.search(
            r'(research question|RQ|question)', content, re.IGNORECASE
        ))

        return has_question_mark or has_rq_heading

    def _evaluate_finer_criteria(self, content: str) -> dict:
        """
        Evaluate FINER criteria presence in problem statement.

        Returns:
            Dictionary with scores for each criterion (0.0-1.0)
        """
        content_lower = content.lower()

        scores = {}

        # Feasible: mentions of resources, time, sample, data availability
        feasible_keywords = [
            'feasible', 'resource', 'budget', 'time', 'timeline',
            'sample', 'access', 'data available', 'practical'
        ]
        scores['feasible'] = self._score_keyword_presence(
            content_lower, feasible_keywords, threshold=1
        )

        # Interesting: mentions of significance, impact, importance
        interesting_keywords = [
            'interesting', 'significant', 'important', 'impact',
            'contribution', 'advance', 'understanding'
        ]
        scores['interesting'] = self._score_keyword_presence(
            content_lower, interesting_keywords, threshold=1
        )

        # Novel: mentions of gap, new, unexplored, first
        novel_keywords = [
            'novel', 'new', 'gap', 'unexplored', 'first', 'original',
            'innovative', 'missing', 'lack of'
        ]
        scores['novel'] = self._score_keyword_presence(
            content_lower, novel_keywords, threshold=1
        )

        # Ethical: mentions of ethics, IRB, consent, human subjects
        ethical_keywords = [
            'ethic', 'irb', 'consent', 'human subjects', 'animal',
            'welfare', 'harm', 'benefit', 'risk'
        ]
        # If no keywords, assume ethical (no red flags)
        ethical_score = self._score_keyword_presence(
            content_lower, ethical_keywords, threshold=0
        )
        scores['ethical'] = max(ethical_score, 0.5)  # Default to pass if not mentioned

        # Relevant: mentions of application, clinical, practical, field
        relevant_keywords = [
            'relevant', 'application', 'clinical', 'practical',
            'field', 'domain', 'problem', 'address', 'solve'
        ]
        scores['relevant'] = self._score_keyword_presence(
            content_lower, relevant_keywords, threshold=1
        )

        return scores

    def _score_keyword_presence(
        self, text: str, keywords: list, threshold: int = 1
    ) -> float:
        """
        Score presence of keywords in text.

        Args:
            text: Text to search
            keywords: List of keywords to find
            threshold: Minimum keyword count for full score

        Returns:
            Score from 0.0 to 1.0
        """
        count = sum(1 for keyword in keywords if keyword in text)

        if threshold == 0:
            return 1.0  # Always pass if no threshold

        if count >= threshold:
            return 1.0
        elif count > 0:
            return count / threshold
        else:
            return 0.0
