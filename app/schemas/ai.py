from pydantic import BaseModel
from datetime import date
from datetime import time


class AIBookAppointment(BaseModel):

    patient_id: int

    doctor_id: int

    appointment_date: date

    appointment_time: time