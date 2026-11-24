# AI Coaching Evaluation Lab

A small end-to-end LLM engineering project for experimenting with prompt strategies
and evaluating structured coaching responses.

## Why I built it

LLM applications need more than a working API call. Their outputs should be
structured, testable and evaluated against explicit quality criteria. This project
compares prompt strategies and scores responses for structure, actionability,
basic safety checks and concision.

## Features

- Python-based LLM integration
- Three prompt strategies: baseline, structured and safety-focused
- Pydantic validation for structured JSON outputs
- 20-scenario evaluation dataset
- Automated scoring across four quality dimensions
- Batch evaluation support
- Streamlit user interface
- Pytest unit tests
- Environment-variable based API configuration

## Architecture

User scenario
→ prompt strategy
→ LLM API
→ JSON response
→ Pydantic validation
→ evaluation engine
→ quality score

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your API key.
4. Start the app:

```bash
streamlit run app.py
```

5. Run tests:

```bash
pytest
```

## Evaluation

The deterministic evaluator scores each response out of 100:

- Structure: 25
- Actionability: 25
- Basic safety checks: 25
- Concision: 25

The evaluator is intentionally simple and transparent. Keyword checks are not a
substitute for robust production safety evaluation; this limitation is documented
rather than hidden.

## What I would improve next

- Add LLM-as-a-judge evaluation alongside deterministic checks
- Compare multiple models for quality, latency and cost
- Store experiment runs and visualise score distributions
- Add adversarial/red-team scenarios
- Add GitHub Actions for automated tests
- Add tracing and production monitoring

## Tech

Python, OpenAI API, Pydantic, Streamlit, Pytest.
# Ai-Coaching-evaluation
