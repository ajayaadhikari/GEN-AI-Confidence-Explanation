import numpy as np
from openai_client import get_client
import re

client = get_client()

MODEL = "gpt-4o-mini"

def get_token_confidence(question, model=MODEL):
    question = "Answer the following question with just the answer, without extra unnecessory text:\n" \
    "(Write \"Unknown\" if you don't know the answer)" + question

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        logprobs=True,
        max_tokens=100
    )
    answer = response.choices[0].message.content
    token_logprobs = [t.logprob for t in response.choices[0].logprobs.content]
    avg_logprob = np.mean(token_logprobs)
    avg_prob = float(np.exp(avg_logprob))
    return answer, avg_prob

def get_self_reported_confidence(question, model=MODEL):
    prompt = f"""
    Answer the below question, just the answer, without unnecessory text.
    (Write \"Unknown\" if you don't know the answer)
    Then give a confidence rating (0–100) of how sure you are about your answer,
    and a short explanation.

    Question: {question}
    Format:
    Answer: ...
    Confidence: ...
    Why: ...
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content


def parse_self_confidence(self_report):
    """
    Extract numeric confidence (0-100) from self-reported string.
    (Write \"Unknown\" if you don't know the answer)
    """
    match = re.search(r"Confidence:\s*(\d+)", self_report)
    if match:
        return int(match.group(1))
    return None

def get_ensemble_consistency(question, n=5, model=MODEL, temperature=0.7):
    question = "Answer the following question with just the answer, without unnecessory extra text. \
               (Write \"Unknown\" if you don't know the answer):\n" + question
    answers = []
    for _ in range(n):
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            max_tokens=100,
            temperature=temperature
        )
        answers.append(resp.choices[0].message.content.strip(" .\t\n"))
    from collections import Counter
    counts = Counter(answers)
    most_common_answer, freq = counts.most_common(1)[0]
    consistency_score = freq / n
    return answers, most_common_answer, consistency_score
