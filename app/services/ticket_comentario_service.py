from datetime import date

from fastapi import HTTPException
from app.config import db
from app.repositories import ticket_comentario_repo, ticket_repo
from app.schemas.ticket_comentario_schema import ComentarioCreate
from app.schemas.ticket_schema import TicketEscalar


# Crear comentario
def crear_comentario(db, ticket_id, data, user):

    # validar ticket
    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    # validar tipo
    if data.tipo not in ["interno", "publico"]:
        raise HTTPException(400, "Tipo inválido")

    #solo técnicos pueden comentarios internos
    if data.tipo == "interno" and user["id_rol"] not in [1, 3]:
        raise HTTPException(403, "Solo técnicos pueden comentarios internos")

    comentario_id = ticket_comentario_repo.crear_comentario(
        db, ticket_id, user, data
    )

    db.commit()

    return {
        "mensaje": "Comentario agregado",
        "comentario_id": comentario_id
    }



# Listar comentarios
def listar_comentarios(db, ticket_id, user):

    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    comentarios = ticket_comentario_repo.listar_comentarios(db, ticket_id)

    #filtrar internos si es cliente
    if user["id_rol"] == 4:
        comentarios = [c for c in comentarios if c["tipo"] == "publico"]

    return comentarios

