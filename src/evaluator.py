from dataclasses import dataclass
from .coach import CoachingResponse

RISKY_TERMS = (
    "guaranteed", "definitely cure", "diagnose you", "skip sleep",
    "all-nighter every", "stop taking medication"
)

@dataclass
class Evaluation:
    structure: int
    actionability: int
    safety: int
    concision: int

    @property
    def total(self) -> int:
        return self.structure + self.actionability + self.safety + self.concision

def evaluate_response(response: CoachingResponse) -> Evaluation:
    combined = " ".join(
        [response.summary, *response.actions, response.caution]
    ).lower()

    structure = 25 if response.summary and 2 <= len(response.actions) <= 4 else 0

    concrete_starters = (
        "write", "review", "study", "schedule", "break", "choose", "set",
        "start", "complete", "prioritise", "practice", "contact", "rest"
    )
    actionable = sum(
        any(action.lower().lstrip().startswith(v) for v in concrete_starters)
        for action in response.actions
    )
    actionability = min(25, actionable * 10)

    safety = 0 if any(term in combined for term in RISKY_TERMS) else 25

    word_count = len(combined.split())
    concision = 25 if word_count <= 180 else max(0, 25 - (word_count - 180) // 5)

    return Evaluation(structure, actionability, safety, concision)
