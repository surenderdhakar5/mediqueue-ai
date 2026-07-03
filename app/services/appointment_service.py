from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.repositories.appointment_repository import (
    create_appointment,
    get_all_appointments,
    get_appointment_by_id,
    get_last_queue_number,
)
from app.repositories.user_repository import get_user_by_id
from app.repositories.doctor_repository import get_doctor_by_id


def book_appointment(db: Session, data):

    patient = get_user_by_id(db, data.patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    doctor = get_doctor_by_id(db, data.doctor_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    last = get_last_queue_number(db)

    if last:
        queue_number = last.queue_number + 1
    else:
        queue_number = 1

    appointment = Appointment(
        patient_id=data.patient_id,
        doctor_id=data.doctor_id,
        appointment_date=data.appointment_date,
        appointment_time=data.appointment_time,
        status="Booked",
        queue_number=queue_number,
    )

    return create_appointment(db, appointment)


def list_appointments(db: Session):
    return get_all_appointments(db)


def get_appointment(db: Session, appointment_id: int):

    appointment = get_appointment_by_id(db, appointment_id)

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment