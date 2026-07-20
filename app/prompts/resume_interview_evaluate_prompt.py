def build_resume_evaluate_prompt(
        resume_text: str,
        question: str,
        answer: str
):

    return f"""
You are a Senior Technical Interviewer.

Candidate Resume:

--------------------------------

{resume_text}

--------------------------------

Interview Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer based on:

1. Technical accuracy
2. Relevance to the question
3. Communication
4. Completeness
5. Confidence

Give constructive feedback.

Also provide an ideal answer.

Return ONLY valid JSON.

{{
    "score": 0,
    "feedback": "",
    "ideal_answer": ""
}}
"""