import os

from fastapi import UploadFile

from app.utils.pdf_reader import extract_text_from_pdf
from app.data import resume_store
from app.config.gemini import client
from app.config.settings import GEMINI_MODEL
from app.prompts.resume_prompt import build_resume_analysis_prompt
import json


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


async def upload_resume(file: UploadFile):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text_from_pdf(file_path)

    resume_store.resume_text = text

    return {
        "filename": file.filename,
        "text": text[:500]
    }

def analyze_resume():

    if not resume_store.resume_text:
        return {
            "error": "No resume uploaded"
        }

    prompt = build_resume_analysis_prompt(
        resume_store.resume_text
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    analysis = json.loads(response.text)

    return analysis