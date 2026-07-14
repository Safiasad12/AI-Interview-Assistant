from fastapi import APIRouter
from app.schemas.interview import InterviewRequest

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post("/generate-question")
def generate_question(request: InterviewRequest):
    return {
        "message": "Request received successfully.",
        "data": request
    }