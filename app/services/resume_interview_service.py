import json

from app.config.gemini import client
from app.config.settings import GEMINI_MODEL

from app.data import resume_store

from app.prompts.resume_interview_prompt import (
    build_resume_interview_prompt
)


def generate_resume_question():

    if not resume_store.resume_text:

        return {
            "error": "No resume uploaded"
        }

    prompt = build_resume_interview_prompt(
        resume_store.resume_text
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return json.loads(response.text)