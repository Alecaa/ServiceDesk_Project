from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

# ============================================
# CONFIG
# ============================================

SECRET_KEY = "secret"
ALGORITHM = "HS256"

security = HTTPBearer()

## ROLES

ROLE_SUPER_ADMIN = 1
ROLE_ADMIN = 2
ROLE_TECNICO = 3
ROLE_CLIENTE = 4  

# DECODIFICAR TOKEN

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Validación básica del payload
        required_fields = ["id", "id_rol"]
        for field in required_fields:
            if field not in payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token inválido (payload incompleto)"
                )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expirado"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

# ============================================
## Validador de roles

def require_roles(*roles_permitidos):
    def role_validator(user=Depends(get_current_user)):
        if user["id_rol"] not in roles_permitidos:
            raise HTTPException(
                status_code=403,
                detail="No autorizado"
            )
        return user
    return role_validator

# ============================================
## Accesos por rol

def require_super_admin(user=Depends(get_current_user)):
    if user["id_rol"] != ROLE_SUPER_ADMIN:
        raise HTTPException(403, "Solo super administrador")
    return user


def require_admin(user=Depends(get_current_user)):
    if user["id_rol"] != ROLE_ADMIN:
        raise HTTPException(403, "Solo administrador de empresa")
    return user


def require_tecnico(user=Depends(get_current_user)):
    if user["id_rol"] != ROLE_TECNICO:
        raise HTTPException(403, "Solo técnico")
    return user


def require_cliente(user=Depends(get_current_user)):
    if user["id_rol"] != ROLE_CLIENTE:
        raise HTTPException(403, "Solo cliente")
    return user


def require_admin_or_super(user=Depends(get_current_user)):
    if user["id_rol"] not in [ROLE_ADMIN, ROLE_SUPER_ADMIN]:
        raise HTTPException(403, "Solo admin o super admin")
    return user


def require_tecnico_or_admin(user=Depends(get_current_user)):
    if user["id_rol"] not in [ROLE_TECNICO, ROLE_ADMIN]:
        raise HTTPException(403, "Solo técnico o admin")
    return user