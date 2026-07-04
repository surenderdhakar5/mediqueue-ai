from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.dashboard_service import (
    doctor_dashboard,
    patient_dashboard,
)

router = APIRouter()


@router.get("/doctor/{doctor_id}")
def get_doctor_dashboard(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return doctor_dashboard(db, doctor_id)


@router.get("/patient/{patient_id}")
def get_patient_dashboard(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return patient_dashboard(db, patient_id)