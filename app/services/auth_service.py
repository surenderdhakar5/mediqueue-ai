from app.utils.security import hash_password

def create_user(data):

    hashed = hash_password(data.password)

    return {
        "full_name": data.full_name,
        "email": data.email,
        "phone": data.phone,
        "password": hashed,
        "role": data.role
    }