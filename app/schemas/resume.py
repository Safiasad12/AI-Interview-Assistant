from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    summary: str
    skills: list[str]
    experience: str
    strengths: list[str]
    recommended_role: str