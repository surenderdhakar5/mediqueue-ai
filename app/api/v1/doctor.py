from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.doctor import DoctorCreate
from app.services.doctor_service import (
    register_doctor,
    list_doctors,
    get_doctor
)

router = APIRouter()


@router.post("/")
def create_new_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    return register_doctor(db, doctor)


@router.get("/")
def get_all_doctors(
    db: Session = Depends(get_db)
):
    return list_doctors(db)


@router.get("/{doctor_id}")
def get_doctor_by_id(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return get_doctor(db, doctor_id)