from fastapi import APIRouter, Depends, Path

from app.schemas.ticket_comentario_schema import ComentarioCreate
from app.services import ticket_comentario_service
from app.config.db import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/tickets", tags=["Comentarios"])


# Crear comentario
@router.post("/{ticket_id}/comentarios")
def crear_comentario(
    ticket_id: int = Path(...),
    data: ComentarioCreate = None,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_comentario_service.crear_comentario(
        db, ticket_id, data, user
    )


# Listar comentarios
@router.get("/{ticket_id}/comentarios")
def listar_comentarios(
    ticket_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_comentario_service.listar_comentarios(
        db, ticket_id, user
    )