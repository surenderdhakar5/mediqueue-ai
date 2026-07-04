from datetime import datetime

from app.services.dashboard_service import (
    doctor_dashboard,
    patient_dashboard,
)
from app.services.appointment_service import book_appointment
from app.schemas.ai import AIBookAppointment


def general_chat(**kwargs):
    return {
        "message": "Hello! How can I help you today?"
    }


def book(db=None, **kwargs):

    data = AIBookAppointment(
        patient_id=kwargs["patient_id"],
        doctor_id=kwargs["doctor_id"],
        appointment_date=datetime.strptime(
            kwargs["appointment_date"],
            "%Y-%m-%d"
        ).date(),
        appointment_time=datetime.strptime(
            kwargs["appointment_time"],
            "%H:%M:%S"
        ).time()
    )

    return book_appointment(db, data)


def doctor(db=None, **kwargs):
    return doctor_dashboard(
        db,
        kwargs["doctor_id"]
    )


def patient(db=None, **kwargs):
    return patient_dashboard(
        db,
        kwargs["patient_id"]
    )


def cancel(**kwargs):
    return {
        "message": "Cancel Appointment - Coming Soon"
    }


def queue(**kwargs):
    return {
        "message": "Queue API - Coming Soon"
    }


TOOL_FUNCTIONS = {
    "GENERAL_CHAT": general_chat,
    "BOOK_APPOINTMENT": book,
    "DOCTOR_DASHBOARD": doctor,
    "PATIENT_DASHBOARD": patient,
    "CANCEL_APPOINTMENT": cancel,
    "CHECK_QUEUE": queue,
}


def execute_tool(tool_name: str, db=None, **kwargs):

    func = TOOL_FUNCTIONS.get(tool_name)

    if func is None:
        return {
            "message": f"Unknown Tool : {tool_name}"
        }

    return func(db=db, **kwargs)