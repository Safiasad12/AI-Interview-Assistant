from app.schemas.interview import InterviewRequest
from app.prompts.interview_prompt import build_question_prompt
from app.config.gemini import client
from app.config.settings import GEMINI_MODEL


def generate_question(request: InterviewRequest):

    prompt = build_question_prompt(
        request.role,
        request.experience,
        request.difficulty
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return {
        "question": response.text
    }