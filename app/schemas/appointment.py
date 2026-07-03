from pydantic import BaseModel
from datetime import date, time, datetime


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time


class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    status: str
    queue_number: int
    created_at: datetime

    class Config:
        from_attributes = True