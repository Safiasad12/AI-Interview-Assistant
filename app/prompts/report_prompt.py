def build_report_prompt(interview):

    return f"""
You are an experienced technical interviewer.

Below is the complete interview.

{interview}

Analyze the overall interview performance.

Return ONLY valid JSON.

{{
    "overall_score": 0,
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "recommendations": [],
    "hire_recommendation": ""
}}

Rules:

- overall_score must be between 0 and 10.
- Consider technical knowledge, communication and accuracy.
- Do not return markdown.
- Return JSON only.
"""