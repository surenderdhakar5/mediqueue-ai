from sqlalchemy import Column, Integer, String, Date, Time, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.db.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("users.id"))

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(Date, nullable=False)

    appointment_time = Column(Time, nullable=False)

    status = Column(String(30), default="Booked")

    queue_number = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )