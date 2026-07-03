from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    specialization = Column(String(100), nullable=False)

    experience = Column(Integer, nullable=False)

    consultation_fee = Column(Integer, nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(15), unique=True, nullable=False)

    is_available = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )