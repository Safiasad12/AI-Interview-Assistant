from fastapi import APIRouter

from app.services.resume_interview_service import generate_resume_question


router = APIRouter(
    prefix="/resume/mock-interview",
    tags=["Resume Mock Interview"]
)


@router.post("/generate-question")
def generate_question():
    return generate_resume_question()