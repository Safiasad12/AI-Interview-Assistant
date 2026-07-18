from pydantic import BaseModel, Field


class InterviewRequest(BaseModel):
    role: str = Field(..., min_length=2, max_length=100)
    experience: str
    difficulty: str


class EvaluateAnswerRequest(BaseModel):
    question: str
    answer: str

class EvaluateAnswerResponse(BaseModel):
    score: int
    feedback: str
    strengths: list[str]
    improvements: list[str]
    ideal_answer: str
    follow_up_question: str