import json
from pathlib import Path
from .coach import generate_coaching
from .evaluator import evaluate_response

def run_suite(strategy: str, dataset_path: str = "data/scenarios.json"):
    scenarios = json.loads(Path(dataset_path).read_text(encoding="utf-8"))
    results = []
    for case in scenarios:
        response = generate_coaching(case["situation"], strategy=strategy)
        score = evaluate_response(response)
        results.append({
            "id": case["id"],
            "category": case["category"],
            "score": score.total,
            "response": response.model_dump(),
        })
    return results
