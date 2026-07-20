from pydantic import BaseModel


class ResumeInterviewQuestionResponse(BaseModel):
    question: str