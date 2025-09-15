# 🧠 From Guesswork to Certainty: Explainable AI Chatbots with Confidence Estimates

LLMs are smart, but not always honest. They often sound confident even when they’re completely wrong — a phenomenon known as hallucination. This creates a big challenge: how much can we actually trust their answers?

In this repo, we implement a simple but powerful idea to make LLMs more transparent: pair every answer with a confidence score. Instead of just taking the model’s output at face value, we’ll dig into how sure it really is, using different strategies to estimate confidence. You’ll learn how to implement this in Python and run it effortlessly with Streamlit.
A blog about this project with in-depth explanation can be found here: [WordPress Article](https://adhikariajaya.wordpress.com/2025/09/15/from-guesswork-to-certainty-explainable-ai-chatbots-with-confidence-estimates/)

Here is how the end application will look like:  

<img width="834" height="380" alt="President of nepal example 1" src="https://github.com/user-attachments/assets/f875fba7-c698-4ed3-8786-20245abfe549" />
<img width="835" height="371" alt="President of nepal example 2" src="https://github.com/user-attachments/assets/60955968-414b-4084-8bf1-874c0de1b343" />

---

## 🌟 Why This Project?

This project demonstrates how to make LLMs more transparent and reliable by combining their answers with **confidence metrics** and reasoning. It shows how to:

- Extract **self-reported confidence** from LLMs
- Compute **token-level confidence** from log probabilities
- Measure **ensemble agreement** across multiple runs
- Optionally extend with **retrieval-based fact-checking**
- Build a **user-friendly Streamlit interface** for real-time interaction

Such a system is useful for applications where trust, interpretability, and reliability of AI answers are important — e.g., research assistants, knowledge bots, and educational tools.

---

## 📄 Project structure
XAI-confidence-chatbot/
│
├── app.py                  # Main Streamlit app with UI and confidence metrics
├── confidence_methods.py   # Functions for self-reported, token-level, and ensemble confidence
├── openai_client.py        # OpenAI API client setup
├── requirements.txt        # List of Python dependencies
└── .streamlit/
    └── secrets.toml        # API keys for OpenAI (local development)

## 🛠️ Setup Instructions

1. **Clone the Repository**
```bash
git clone [https://github.com/ajayaadhikari/XAI-confidence-chatbot.git](https://github.com/ajayaadhikari/GEN-AI-Confidence-Explanation/)
cd GEN-AI-Confidence-Explanation
```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

3. **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Up Secrets**
Create a .streamlit/secrets.toml file in the project root:
```bash
OPENAI_API_KEY = "your_openai_api_key_here"
```

5. **Run the App**
```bash
streamlit run app.py
```
Open http://localhost:8501 in your browser to interact with your XAI chatbot.



