import os

from fastapi import UploadFile

from app.utils.pdf_reader import extract_text_from_pdf


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


async def upload_resume(file: UploadFile):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    resume_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "text": resume_text[:500]
    }