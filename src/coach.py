import json
import os
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError
from .prompts import PROMPTS

class CoachingResponse(BaseModel):
    summary: str
    actions: list[str] = Field(min_length=2, max_length=4)
    caution: str

def generate_coaching(situation: str, strategy: str = "structured",
                      model: str | None = None) -> CoachingResponse:
    if strategy not in PROMPTS:
        raise ValueError(f"Unknown strategy: {strategy}")
    if not situation.strip():
        raise ValueError("Situation cannot be empty.")

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    chosen_model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    response = client.chat.completions.create(
        model=chosen_model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": PROMPTS[strategy]},
            {"role": "user", "content": situation.strip()},
        ],
        response_format={"type": "json_object"},
    )

    raw = response.choices[0].message.content
    try:
        return CoachingResponse.model_validate(json.loads(raw))
    except (json.JSONDecodeError, ValidationError) as exc:
        raise ValueError(f"Model returned an invalid structured response: {exc}") from exc
