from fastapi import APIRouter

from app.services.resume_interview_service import generate_resume_question, evaluate_resume_answer

from app.schemas.resume_interview import ResumeInterviewEvaluateRequest



router = APIRouter(
    prefix="/resume/mock-interview",
    tags=["Resume Mock Interview"]
)


@router.post("/generate-question")
def generate_question():
    return generate_resume_question()

@router.post("/evaluate")
def evaluate(
        request: ResumeInterviewEvaluateRequest
):
    return evaluate_resume_answer(request)