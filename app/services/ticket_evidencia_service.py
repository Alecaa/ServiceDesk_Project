import os
from fastapi import UploadFile, HTTPException

from app.repositories import ticket_evidencia_repo, ticket_repo


UPLOAD_DIR = "uploads/"


def subir_evidencia(db, ticket_id, file: UploadFile, user):

    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    # guardar archivo en disco
    filename = file.filename
    ruta = os.path.join(UPLOAD_DIR, filename)

    with open(ruta, "wb") as buffer:
        buffer.write(file.file.read())

    tipo = file.content_type

    ticket_evidencia_repo.guardar_evidencia(
        db,
        ticket_id,
        filename,
        ruta,
        tipo
    )

    db.commit()

    return {
        "mensaje": "Evidencia subida",
        "archivo": filename
    }


def listar_evidencias(db, ticket_id, user):

    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    return ticket_evidencia_repo.listar_evidencias(db, ticket_id)