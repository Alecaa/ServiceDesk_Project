from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta
from app.utils.security import verify_password
from app.repositories import auth_repo

SECRET_KEY = "secret"
ALGORITHM = "HS256"


def login(db, username, password):
    user = auth_repo.get_user_by_username(db, username)

    # Usuario no existe
    if not user:
        raise HTTPException(401, "Credenciales inválidas")

    # Usuario inactivo
    if user["estado"] != "Activo":
        raise HTTPException(403, "Usuario inactivo")

    #Password incorrecto (por ahora texto plano)
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Payload del token
    payload = {
        "id": user["id"],
        "username": user["username"],
        "id_rol": user["id_rol"],
        "id_empresa": user["id_empresa"],
        "id_area": user["id_area"],
        "exp": datetime.utcnow() + timedelta(hours=8)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }