from fastapi import FastAPI

from app.routers import health, interview, resume

app = FastAPI(
    title="AI Interview Assistant API",
    description="Backend APIs for AI Interview Assistant",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(interview.router)
app.include_router(resume.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Assistant API"
    }