from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.repositories.doctor_repository import (
    create_doctor,
    get_all_doctors,
    get_doctor_by_email,
    get_doctor_by_id
)


def register_doctor(db: Session, data):

    if get_doctor_by_email(db, data.email):
        raise HTTPException(
            status_code=400,
            detail="Doctor already exists with this email"
        )

    doctor = Doctor(
        full_name=data.full_name,
        specialization=data.specialization,
        experience=data.experience,
        consultation_fee=data.consultation_fee,
        email=data.email,
        phone=data.phone,
        is_available=True
    )

    return create_doctor(db, doctor)


def list_doctors(db: Session):
    return get_all_doctors(db)


def get_doctor(db: Session, doctor_id: int):

    doctor = get_doctor_by_id(db, doctor_id)

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor