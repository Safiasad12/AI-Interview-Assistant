from pydantic import BaseModel


class ResumeInterviewQuestionResponse(BaseModel):
    question: str


class ResumeInterviewEvaluateRequest(BaseModel):
    question: str
    answer: str


class ResumeInterviewEvaluateResponse(BaseModel):
    score: int
    feedback: str
    ideal_answer: str