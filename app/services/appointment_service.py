from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.services.ai_service import estimate_wait_time

from app.repositories.appointment_repository import (
    create_appointment,
    get_all_appointments,
    get_appointment_by_id,
    get_last_queue_number,
    get_current_queue,
    update_appointment_status,
)

from app.repositories.user_repository import get_user_by_id
from app.repositories.doctor_repository import get_doctor_by_id


def book_appointment(db: Session, data):

    # Check Patient
    patient = get_user_by_id(db, data.patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # Check Doctor
    doctor = get_doctor_by_id(db, data.doctor_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    # Queue Number
    last = get_last_queue_number(
        db,
        data.doctor_id,
        data.appointment_date
    )

    if last:
        queue_number = last.queue_number + 1
    else:
        queue_number = 1

    # Create Appointment
    appointment = Appointment(
        patient_id=data.patient_id,
        doctor_id=data.doctor_id,
        appointment_date=data.appointment_date,
        appointment_time=data.appointment_time,
        status="Booked",
        queue_number=queue_number,
    )

    saved_appointment = create_appointment(db, appointment)

    # Current Queue
    current = get_current_queue(
        db,
        data.doctor_id,
        data.appointment_date
    )

    current_queue = 0

    if current:
        current_queue = current.queue_number

    # AI Wait Time
    estimated = estimate_wait_time(
        queue_number,
        current_queue
    )

    return {
        "appointment": saved_appointment,
        "estimated_wait_time_minutes": estimated,
        "current_queue": current_queue
    }


def list_appointments(db: Session):
    return get_all_appointments(db)


def get_appointment(db: Session, appointment_id: int):

    appointment = get_appointment_by_id(
        db,
        appointment_id
    )

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


def change_status(
    db: Session,
    appointment_id: int,
    status: str
):
    """
    Change appointment status.
    """

    appointment = update_appointment_status(
        db,
        appointment_id,
        status
    )

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return {
        "message": f"Appointment marked as {status}",
        "appointment": appointment
    }