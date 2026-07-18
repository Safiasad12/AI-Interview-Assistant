from fastapi import APIRouter, UploadFile, File
from app.services.resume_service import upload_resume, analyze_resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    return await upload_resume(file)


@router.post("/analyze")
def analyze():
    return analyze_resume()