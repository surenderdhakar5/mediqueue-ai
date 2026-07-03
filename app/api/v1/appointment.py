from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.appointment import AppointmentCreate

from app.services.appointment_service import (
    book_appointment,
    list_appointments,
    get_appointment,
    change_status,
)

router = APIRouter()


@router.post("/")
def create_new_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    return book_appointment(db, appointment)


@router.get("/")
def get_all_appointments(
    db: Session = Depends(get_db)
):
    return list_appointments(db)


@router.get("/{appointment_id}")
def get_appointment_by_id(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    return get_appointment(db, appointment_id)


@router.patch("/{appointment_id}/start")
def start_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    return change_status(
        db,
        appointment_id,
        "In Progress"
    )


@router.patch("/{appointment_id}/complete")
def complete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    return change_status(
        db,
        appointment_id,
        "Completed"
    )


@router.patch("/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    return change_status(
        db,
        appointment_id,
        "Cancelled"
    )