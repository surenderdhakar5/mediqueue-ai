from fastapi import FastAPI

app = FastAPI(
    title="MediQueue AI",
    version="1.0.0",
    description="Smart Clinic Queue Management System"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to MediQueue AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

from app.api.v1.auth import router as auth_router

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)