from fastapi import APIRouter

from app.schemas.interview import InterviewRequest
from app.services.interview_service import generate_question

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post("/generate-question")
def generate_interview_question(request: InterviewRequest):
    return generate_question(request)