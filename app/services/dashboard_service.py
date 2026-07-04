from datetime import date

from sqlalchemy.orm import Session

from app.models.appointment import Appointment


# ==========================
# Doctor Dashboard
# ==========================

def doctor_dashboard(db: Session, doctor_id: int):

    # Development ke liye fixed date
    # Deployment se pehle isko date.today() kar dena
    today = date.today()

    total = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == today
        )
        .count()
    )

    completed = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == today,
            Appointment.status == "Completed"
        )
        .count()
    )

    waiting = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == today,
            Appointment.status == "Booked"
        )
        .count()
    )

    in_progress = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == today,
            Appointment.status == "In Progress"
        )
        .count()
    )

    cancelled = (
        db.query(Appointment)
        .filter(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == today,
            Appointment.status == "Cancelled"
        )
        .count()
    )

    return {
        "today_appointments": total,
        "completed": completed,
        "waiting": waiting,
        "in_progress": in_progress,
        "cancelled": cancelled
    }


# ==========================
# Patient Dashboard
# ==========================

def patient_dashboard(db: Session, patient_id: int):

    # Development ke liye fixed date
    today = date.today()

    total = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id
        )
        .count()
    )

    upcoming = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.appointment_date >= today,
            Appointment.status == "Booked"
        )
        .count()
    )

    completed = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.status == "Completed"
        )
        .count()
    )

    cancelled = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.status == "Cancelled"
        )
        .count()
    )

    next_appointment = (
        db.query(Appointment)
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.appointment_date >= today,
            Appointment.status == "Booked"
        )
        .order_by(
            Appointment.appointment_date,
            Appointment.appointment_time
        )
        .first()
    )

    if next_appointment:
        next_data = {
            "doctor_id": next_appointment.doctor_id,
            "date": next_appointment.appointment_date,
            "time": next_appointment.appointment_time,
            "queue_number": next_appointment.queue_number
        }
    else:
        next_data = None

    return {
        "total_appointments": total,
        "upcoming": upcoming,
        "completed": completed,
        "cancelled": cancelled,
        "next_appointment": next_data
    }