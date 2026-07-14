from fastapi import APIRouter

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post("/generate-question")
def generate_question():
    return {
        "question": "Explain Dependency Injection in FastAPI."
    }