from fastapi import APIRouter, Depends, UploadFile, File

from app.services import ticket_evidencia_service
from app.config.db import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/tickets", tags=["Evidencias"])


@router.post("/{ticket_id}/evidencias")
def subir_evidencia(
    ticket_id: int,
    file: UploadFile = File(...),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_evidencia_service.subir_evidencia(
        db, ticket_id, file, user
    )


@router.get("/{ticket_id}/evidencias")
def listar_evidencias(
    ticket_id: int,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_evidencia_service.listar_evidencias(
        db, ticket_id, user
    )