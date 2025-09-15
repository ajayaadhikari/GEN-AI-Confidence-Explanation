import streamlit as st
import matplotlib.pyplot as plt

def show_ensemble_bar(answers):
    """Visualize distribution of ensemble answers."""
    from collections import Counter
    counts = Counter(answers)

    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values())
    ax.set_ylabel("Frequency")
    ax.set_title("Ensemble Answer Distribution")
    st.pyplot(fig)
