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


class InterviewItem(BaseModel):
    question: str
    answer: str

class InterviewReportRequest(BaseModel):
    interview: list[InterviewItem]

class InterviewReportResponse(BaseModel):
    overall_score: int
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    hire_recommendation: str