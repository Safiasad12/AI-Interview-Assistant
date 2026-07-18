from app.schemas.interview import InterviewRequest, EvaluateAnswerRequest, InterviewReportRequest
from app.prompts.interview_prompt import build_question_prompt
from app.prompts.feedback_prompt import build_feedback_prompt
from app.prompts.report_prompt import build_report_prompt
from app.config.gemini import client
from app.config.settings import GEMINI_MODEL
import json


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


def evaluate_answer(request: EvaluateAnswerRequest):

    prompt = build_feedback_prompt(
        request.question,
        request.answer
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return json.loads(response.text)


def generate_report(request: InterviewReportRequest):

    prompt = build_report_prompt(request.interview)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return json.loads(response.text)