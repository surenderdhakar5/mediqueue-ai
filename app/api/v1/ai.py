from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.ai.agent import run_agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    doctor_id: int | None = None
    patient_id: int | None = None


@router.post("/chat")
def chat(
    data: ChatRequest,
    db: Session = Depends(get_db)
):
    return run_agent(
        user_input=data.message,
        db=db,
        doctor_id=data.doctor_id,
        patient_id=data.patient_id
    )