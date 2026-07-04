from fastapi import FastAPI
from app.api.v1.appointment import router as appointment_router
from app.api.v1.auth import router as auth_router
from app.api.v1.doctor import router as doctor_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.ai import router as ai_router
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


# Authentication APIs
app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# Doctor APIs
app.include_router(
    doctor_router,
    prefix="/api/v1/doctors",
    tags=["Doctors"]
)


app.include_router(
    appointment_router,
    prefix="/api/v1/appointments",
    tags=["Appointments"]
)

app.include_router(
    dashboard_router,
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    ai_router,
    prefix="/api/v1/ai",
    tags=["AI Assistant"]
)