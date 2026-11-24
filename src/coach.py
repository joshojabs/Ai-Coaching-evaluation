import os

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from .prompts import PROMPTS


class CoachingResponse(BaseModel):
    summary: str
    actions: list[str] = Field(min_length=2, max_length=4)
    caution: str


def generate_coaching(
    situation: str,
    strategy: str = "structured",
    model: str | None = None,
) -> CoachingResponse:

    if strategy not in PROMPTS:
        raise ValueError(f"Unknown strategy: {strategy}")

    if not situation.strip():
        raise ValueError("Situation cannot be empty.")

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing.")

    client = genai.Client(api_key=api_key)

    chosen_model = model or os.environ.get(
        "GEMINI_MODEL",
        "gemini-3.8-flash",
    )

    prompt = f"""
{PROMPTS[strategy]}

USER SITUATION:
{situation.strip()}
"""

    response = client.models.generate_content(
        model=chosen_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            response_mime_type="application/json",
            response_json_schema=CoachingResponse.model_json_schema(),
        ),
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    try:
        return CoachingResponse.model_validate_json(response.text)
    except Exception as exc:
        raise ValueError(
            f"Model returned an invalid structured response: {exc}"
        ) from exc