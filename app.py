import streamlit as st
from confidence_methods import (
    get_token_confidence,
    get_self_reported_confidence,
    get_ensemble_consistency,
    parse_self_confidence
)
from utils import show_ensemble_bar

st.set_page_config(page_title="XAI Confidence Demo", layout="wide")
st.title("🤖 Explainable AI Prototype – Confidence Explorer")

question = st.text_input("❓ Enter your question:", "Who is the current president of France?")

if st.button("Get Answer with Explanations"):
    with st.spinner("Generating answer and confidence explanations..."):
        answer, prob_conf = get_token_confidence(question)
        self_report = get_self_reported_confidence(question)
        answers, majority, score = get_ensemble_consistency(question, n=5)

    # Extract numeric confidence
    self_conf_value = parse_self_confidence(self_report)
    st.subheader("📌 Final Answer (Token-based)")
    st.write(answer)
    st.metric("Token Confidence", f"{prob_conf:.2f}")

    st.subheader("🧠 Self-Reported Confidence")
    st.text(self_report)

    st.subheader("👥 Ensemble Consistency")
    st.write("All Answers:", answers)
    st.write("Majority Answer:", majority)
    st.metric("Agreement Score", f"{score:.2f}")

    # Chart visualization
    # show_ensemble_bar(answers)

    st.subheader("🔍 Comparison")
    st.markdown(f"""
    - **Token log-prob confidence**: {prob_conf:.2f}  
    - **Self-reported confidence**: {self_conf_value if self_conf_value is not None else 'N/A'}  
    - **Ensemble agreement**: {score:.2f}  
    """)
