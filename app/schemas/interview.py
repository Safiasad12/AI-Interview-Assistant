from pydantic import BaseModel, Field


class InterviewRequest(BaseModel):
    role: str = Field(..., min_length=2, max_length=100)
    experience: str
    difficulty: str
    number_of_questions: int = Field(..., ge=1, le=20)