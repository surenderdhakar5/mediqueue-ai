from app.db.database import engine
from app.models.user import User
from app.db.database import Base

Base.metadata.create_all(bind=engine)

print("Database Connected Successfully ✅")