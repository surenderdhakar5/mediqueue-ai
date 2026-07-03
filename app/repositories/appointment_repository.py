from sqlalchemy.orm import Session

from app.models.appointment import Appointment


def create_appointment(db: Session, appointment: Appointment):
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


def get_all_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(
        Appointment.id == appointment_id
    ).first()


def get_last_queue_number(db: Session):

    appointment = (
        db.query(Appointment)
        .order_by(Appointment.queue_number.desc())
        .first()
    )

    return appointment