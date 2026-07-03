from app.db.database import engine
from app.models.user import User
from app.models.doctor import Doctor
from app.db.database import Base
from app.models.appointment import Appointment

Base.metadata.create_all(bind=engine)

print("Database Connected Successfully ✅")