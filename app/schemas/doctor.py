from pydantic import BaseModel, EmailStr
from datetime import datetime


class DoctorCreate(BaseModel):
    full_name: str
    specialization: str
    experience: int
    consultation_fee: int
    email: EmailStr
    phone: str


class DoctorResponse(BaseModel):
    id: int
    full_name: str
    specialization: str
    experience: int
    consultation_fee: int
    email: EmailStr
    phone: str
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True