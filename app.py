import os
import streamlit as st
from dotenv import load_dotenv
from src.coach import generate_coaching
from src.evaluator import evaluate_response
from src.prompts import PROMPTS

load_dotenv()
st.set_page_config(page_title="AI Coaching Evaluation Lab", page_icon="🧪")
st.title("AI Coaching Evaluation Lab")
st.caption("Compare prompt strategies and evaluate structured LLM coaching outputs.")

strategy = st.selectbox("Prompt strategy", list(PROMPTS))
situation = st.text_area(
    "Situation",
    "I have an exam in five days, three topics left to revise, and I keep "
    "switching between them without finishing anything."
)

if st.button("Generate and evaluate"):
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Add OPENAI_API_KEY to your .env file first.")
    else:
        try:
            result = generate_coaching(situation, strategy)
            score = evaluate_response(result)
            st.subheader(f"Evaluation score: {score.total}/100")
            st.json(result.model_dump())
            st.write({
                "structure": score.structure,
                "actionability": score.actionability,
                "safety": score.safety,
                "concision": score.concision,
            })
        except Exception as exc:
            st.error(str(exc))
