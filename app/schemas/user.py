from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    role: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True