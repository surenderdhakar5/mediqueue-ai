from datetime import date

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
    return (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )


def get_last_queue_number(
    db: Session,
    doctor_id: int,
    appointment_date
):
    """
    Returns the last queue number
    for a specific doctor on a specific date.
    """

    return (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == appointment_date
        )
        .order_by(Appointment.queue_number.desc())
        .first()
    )


def get_current_queue(
    db: Session,
    doctor_id: int,
    appointment_date
):
    """
    Returns the appointment that is currently
    in progress for a doctor on a specific date.
    """

    return (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == appointment_date,
            Appointment.status == "In Progress"
        )
        .first()
    )


def update_appointment_status(
    db: Session,
    appointment_id: int,
    status: str
):
    """
    Update appointment status.
    """

    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if appointment:
        appointment.status = status
        db.commit()
        db.refresh(appointment)

    return appointment


# ==========================
# Patient Dashboard Functions
# ==========================

def get_patient_total_appointments(
    db: Session,
    patient_id: int
):
    return (
        db.query(Appointment)
        .filter(Appointment.patient_id == patient_id)
        .count()
    )


def get_patient_completed_appointments(
    db: Session,
    patient_id: int
):
    return (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.status == "Completed"
        )
        .count()
    )


def get_patient_cancelled_appointments(
    db: Session,
    patient_id: int
):
    return (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.status == "Cancelled"
        )
        .count()
    )


def get_patient_upcoming_appointments(
    db: Session,
    patient_id: int
):
    return (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.appointment_date >= date.today(),
            Appointment.status == "Booked"
        )
        .count()
    )


def get_next_appointment(
    db: Session,
    patient_id: int
):
    return (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.appointment_date >= date.today(),
            Appointment.status == "Booked"
        )
        .order_by(
            Appointment.appointment_date,
            Appointment.appointment_time
        )
        .first()
    )