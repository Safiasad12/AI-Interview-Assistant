def build_feedback_prompt(question: str, answer: str):
    return f"""
You are an experienced technical interviewer.

Evaluate the candidate's answer based on the following criteria:

1. Technical correctness
2. Completeness
3. Clarity of explanation
4. Use of examples (if applicable)

Scoring Rules:
- Score must be between 0 and 10.
- 0-2 = Poor
- 3-4 = Below Average
- 5-6 = Average
- 7-8 = Good
- 9-10 = Excellent

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON in the following format:

{{
    "score": 0,
    "feedback": "",
    "strengths": [],
    "improvements": [],
    "ideal_answer": "",
    "follow_up_question": ""
}}

Rules:
- Do not include markdown.
- Do not wrap the JSON inside ```json.
- Do not add any explanation before or after the JSON.
"""