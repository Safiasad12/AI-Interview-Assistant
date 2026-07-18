from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, interview, resume

app = FastAPI(
    title="AI Interview Assistant API",
    description="Backend APIs for AI Interview Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(interview.router)
app.include_router(resume.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Assistant API"
    }