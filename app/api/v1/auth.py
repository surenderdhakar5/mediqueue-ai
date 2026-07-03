from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest
from app.services.auth_service import (
    create_user,
    login_user,
    get_current_user,
)

from app.db.database import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):

    new_user = create_user(db, user)

    return {
        "message": "User Registered Successfully",
        "user": new_user
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    result = login_user(db, form_data)

    if result is None:
        return {
            "message": "Invalid Email or Password"
        }

    return result


@router.get("/me")
def current_user(
    token: str = Depends(oauth2_scheme)
):

    return get_current_user(token)