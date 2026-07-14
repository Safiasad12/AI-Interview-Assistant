def build_question_prompt(role, experience, difficulty):
    return f"""
You are an experienced technical interviewer.

Generate ONE interview question.

Role: {role}
Experience: {experience}
Difficulty: {difficulty}

Return only the question.
"""