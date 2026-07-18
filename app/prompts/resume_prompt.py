def build_resume_analysis_prompt(resume_text: str):
    return f"""
Analyze the resume.

Return ONLY valid JSON.

{{
    "summary": "",
    "skills": [],
    "experience": "",
    "strengths": [],
    "recommended_role": ""
}}

Resume:

{resume_text}
"""