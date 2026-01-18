"""
Workflow Context Management

Maintains state and context throughout the research workflow.
Provides data passing between phases and agents.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Any
import json
import uuid


class Mode(str, Enum):
    """Research workflow operation mode"""
    ASSISTANT = "assistant"  # Human-guided
    AUTONOMOUS = "autonomous"  # Automated


class ResearchPhase(str, Enum):
    """11 phases of research workflow"""
    PROBLEM_FORMULATION = "problem_formulation"
    LITERATURE_REVIEW = "literature_review"
    GAP_ANALYSIS = "gap_analysis"
    HYPOTHESIS_FORMATION = "hypothesis_formation"
    EXPERIMENTAL_DESIGN = "experimental_design"
    IRB_APPROVAL = "irb_approval"
    DATA_COLLECTION = "data_collection"
    ANALYSIS = "analysis"
    INTERPRETATION = "interpretation"
    WRITING = "writing"
    PUBLICATION = "publication"


@dataclass
class PhaseRecord:
    """Record of a completed phase"""
    phase: ResearchPhase
    entered_at: str
    exited_at: Optional[str] = None
    validation_score: Optional[float] = None
    outputs: List[str] = field(default_factory=list)
    agent_used: Optional[str] = None
    notes: str = ""


@dataclass
class ValidationResult:
    """Result of validation gate"""
    passed: bool
    score: float  # 0.0 - 1.0
    missing_items: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    blocking_issues: List[str] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return asdict(self)


@dataclass
class WorkflowContext:
    """Complete workflow state and context"""

    # Identity
    workflow_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    # Current state
    mode: Mode = Mode.ASSISTANT
    current_phase: ResearchPhase = ResearchPhase.PROBLEM_FORMULATION
    phase_history: List[PhaseRecord] = field(default_factory=list)

    # Research context
    research_question: str = ""
    domain: str = ""
    resources: Dict[str, Any] = field(default_factory=dict)

    # Validation tracking
    validation_results: Dict[str, ValidationResult] = field(default_factory=dict)

    # Audit trail
    audit_trail: List[Dict[str, Any]] = field(default_factory=list)

    # File paths
    project_root: Path = field(default_factory=lambda: Path.cwd())

    def update_timestamp(self):
        """Update the last modified timestamp"""
        self.updated_at = datetime.now().isoformat()

    def add_audit_entry(self, action: str, details: Dict[str, Any]):
        """Add entry to audit trail"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "phase": self.current_phase.value,
            "details": details
        }
        self.audit_trail.append(entry)
        self.update_timestamp()

    def start_phase(self, phase: ResearchPhase, agent: Optional[str] = None):
        """Record phase start"""
        record = PhaseRecord(
            phase=phase,
            entered_at=datetime.now().isoformat(),
            agent_used=agent
        )
        self.phase_history.append(record)
        self.current_phase = phase
        self.add_audit_entry(
            "phase_started",
            {"phase": phase.value, "agent": agent}
        )

    def complete_phase(
        self,
        validation_result: ValidationResult,
        outputs: List[str]
    ):
        """Record phase completion"""
        if self.phase_history:
            current_record = self.phase_history[-1]
            current_record.exited_at = datetime.now().isoformat()
            current_record.validation_score = validation_result.score
            current_record.outputs = outputs

        # Store validation result
        self.validation_results[self.current_phase.value] = validation_result

        self.add_audit_entry(
            "phase_completed",
            {
                "phase": self.current_phase.value,
                "validation_score": validation_result.score,
                "passed": validation_result.passed,
                "outputs": outputs
            }
        )

    def get_phase_outputs(self, phase: ResearchPhase) -> List[str]:
        """Get outputs from a specific phase"""
        for record in self.phase_history:
            if record.phase == phase and record.exited_at:
                return record.outputs
        return []

    def has_completed_phase(self, phase: ResearchPhase) -> bool:
        """Check if a phase has been completed"""
        for record in self.phase_history:
            if record.phase == phase and record.exited_at:
                return True
        return False

    def get_current_phase_index(self) -> int:
        """Get index of current phase in workflow"""
        phases = list(ResearchPhase)
        return phases.index(self.current_phase)

    def to_dict(self) -> dict:
        """Convert context to dictionary for serialization"""
        data = {
            "workflow_id": self.workflow_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "mode": self.mode.value,
            "current_phase": self.current_phase.value,
            "phase_history": [
                {
                    "phase": record.phase.value,
                    "entered_at": record.entered_at,
                    "exited_at": record.exited_at,
                    "validation_score": record.validation_score,
                    "outputs": record.outputs,
                    "agent_used": record.agent_used,
                    "notes": record.notes
                }
                for record in self.phase_history
            ],
            "research_question": self.research_question,
            "domain": self.domain,
            "resources": self.resources,
            "validation_results": {
                k: v.to_dict() for k, v in self.validation_results.items()
            },
            "audit_trail": self.audit_trail,
            "project_root": str(self.project_root)
        }
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "WorkflowContext":
        """Load context from dictionary"""
        # Convert string enums back to enum types
        data["mode"] = Mode(data["mode"])
        data["current_phase"] = ResearchPhase(data["current_phase"])

        # Convert phase history
        phase_history = []
        for record_data in data.get("phase_history", []):
            record_data["phase"] = ResearchPhase(record_data["phase"])
            phase_history.append(PhaseRecord(**record_data))
        data["phase_history"] = phase_history

        # Convert validation results
        validation_results = {}
        for phase, result_data in data.get("validation_results", {}).items():
            validation_results[phase] = ValidationResult(**result_data)
        data["validation_results"] = validation_results

        # Convert project root to Path
        data["project_root"] = Path(data.get("project_root", Path.cwd()))

        return cls(**data)

    def save(self, filepath: Optional[Path] = None):
        """Save context to JSON file"""
        if filepath is None:
            filepath = self.project_root / ".research_workflow" / "state.json"

        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, filepath: Path) -> "WorkflowContext":
        """Load context from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)


def create_backup(context: WorkflowContext, backup_dir: Optional[Path] = None):
    """Create timestamped backup of workflow state"""
    if backup_dir is None:
        backup_dir = context.project_root / ".research_workflow" / "backups"

    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"state_{timestamp}.json"

    context.save(backup_file)
    return backup_file
