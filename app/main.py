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