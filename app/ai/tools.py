from app.services.dashboard_service import (
    doctor_dashboard,
    patient_dashboard,
)


def execute_tool(
    tool_name: str,
    db=None,
    **kwargs
):

    if tool_name == "GENERAL_CHAT":
        return {
            "message": "Hello! How can I help you today?"
        }

    elif tool_name == "DOCTOR_DASHBOARD":
        return doctor_dashboard(
            db,
            kwargs["doctor_id"]
        )

    elif tool_name == "PATIENT_DASHBOARD":
        return patient_dashboard(
            db,
            kwargs["patient_id"]
        )

    elif tool_name == "BOOK_APPOINTMENT":
        return {
            "message": "Booking tool detected. Next step: integrate with Appointment Service."
        }

    elif tool_name == "CANCEL_APPOINTMENT":
        return {
            "message": "Cancel tool detected. Next step: integrate with Appointment Service."
        }

    elif tool_name == "CHECK_QUEUE":
        return {
            "message": "Queue tool detected. Next step: integrate Queue Service."
        }

    return {
        "message": f"Unknown tool: {tool_name}"
    }