from app.schemas.interview import InterviewRequest


def generate_question(request: InterviewRequest):
    return {
        "message": "Request received successfully.",
        "data": request.model_dump()
    }