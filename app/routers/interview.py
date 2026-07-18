from fastapi import APIRouter

from app.schemas.interview import InterviewRequest, EvaluateAnswerRequest, InterviewReportRequest
from app.services.interview_service import generate_question, evaluate_answer, generate_report

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post("/generate-question")
def generate_interview_question(request: InterviewRequest):
    return generate_question(request)

@router.post("/evaluate")
def evaluate(request: EvaluateAnswerRequest):
    return evaluate_answer(request)

@router.post("/report")
def report(request: InterviewReportRequest):
    return generate_report(request)