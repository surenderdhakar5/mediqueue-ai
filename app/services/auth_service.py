from fastapi import HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import SECRET_KEY, ALGORITHM
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.models.user import User
from app.repositories.user_repository import (
    get_user_by_email,
    get_user_by_phone,
    create_user as create_user_repo
)


def create_user(db: Session, data):

    # Check if email already exists
    if get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Check if phone already exists
    if get_user_by_phone(db, data.phone):
        raise HTTPException(
            status_code=400,
            detail="Phone already registered"
        )

    # Create new user
    user = User(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        hashed_password=hash_password(data.password),
        role=data.role,
        is_active=True,
        is_verified=False
    )

    return create_user_repo(db, user)


def login_user(db: Session, data):

    user = get_user_by_email(db, data.username)

    if user is None:
        return None

    if not verify_password(
        data.password,
        user.hashed_password
    ):
        return None

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return {
            "email": email,
            "role": payload.get("role")
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )