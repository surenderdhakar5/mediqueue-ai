from fastapi import HTTPException
from jose import jwt, JWTError

from app.core.config import SECRET_KEY, ALGORITHM

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def create_user(data):
    hashed = hash_password(data.password)

    return {
        "full_name": data.full_name,
        "email": data.email,
        "phone": data.phone,
        "password": hashed,
        "role": data.role
    }


def login_user(data):
    # OAuth2PasswordRequestForm uses 'username'
    if data.username != "surendra@gmail.com":
        return None

    # Demo Password
    hashed_password = hash_password("123456")

    if not verify_password(data.password, hashed_password):
        return None

    token = create_access_token(
        {
            "sub": data.username
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
            "email": email
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )