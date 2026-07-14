from fastapi import FastAPI

app = FastAPI(
    title="AI Interview Assistant API",
    description="Backend APIs for AI Interview Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Assistant API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }