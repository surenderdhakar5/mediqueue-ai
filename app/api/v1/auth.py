from fastapi import APIRouter

from app.schemas.auth import RegisterRequest
from app.services.auth_service import create_user

router = APIRouter()

@router.post("/register")
def register(user: RegisterRequest):

    new_user = create_user(user)

    return {
        "message": "User Registered Successfully",
        "user": new_user
    }