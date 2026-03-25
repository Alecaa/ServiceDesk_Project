from fastapi import APIRouter, Depends, Query, Path

from app.schemas.user_schema import UserCreate, UserUpdate
from app.services import user_service
from app.config.db import get_db
from app.dependencies.auth import require_admin_or_super

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# Crear usuario
@router.post("/")
def crear_usuario(
    data: UserCreate,
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return user_service.crear_usuario(db, data)


# Listar usuarios
@router.get("/")
def listar_usuarios(
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return user_service.listar_usuarios(db, user)


# Obtener usuario
@router.get("/{user_id}")
def obtener_usuario(
    user_id: int = Path(..., gt=0),
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return user_service.get_usuario(db, user_id)


# Actualizar usuario
@router.put("/{user_id}")
def actualizar_usuario(
    user_id: int,
    data: UserUpdate,
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return user_service.actualizar_usuario(db, user_id, data)


# Cambiar estado
@router.patch("/{user_id}/estado")
def cambiar_estado(
    user_id: int,
    estado: str = Query(...),
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return user_service.cambiar_estado(db, user_id, estado)