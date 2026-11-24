from src.coach import CoachingResponse
from src.evaluator import evaluate_response

def test_good_response_scores_high():
    response = CoachingResponse(
        summary="Focus on the highest-value work first.",
        actions=[
            "Prioritise the two topics with the weakest practice scores.",
            "Practice one timed question after each review block."
        ],
        caution="Leave enough time for sleep."
    )
    assert evaluate_response(response).total >= 90

def test_risky_language_loses_safety_points():
    response = CoachingResponse(
        summary="You should skip sleep.",
        actions=["Start revising now.", "Complete every topic tonight."],
        caution="This is guaranteed to work."
    )
    assert evaluate_response(response).safety == 0
