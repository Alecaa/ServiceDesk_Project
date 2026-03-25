from fastapi import HTTPException
from app.repositories import ticket_repo, ticket_comentario_repo
from app.schemas.ticket_comentario_schema import ComentarioCreate


def crear_ticket(db, data, user):

    # 1. crear
    ticket_id = ticket_repo.crear_ticket(db, data, user, None)

    # 2. generar número seguro
    num_ticket = f"TKT-{ticket_id:06d}"

    # 3. actualizar
    ticket_repo.actualizar_numero_ticket(db, ticket_id, num_ticket)

    db.commit()

    return {
        "mensaje": "Ticket creado",
        "ticket_id": ticket_id,
        "num_ticket": num_ticket
    }


# Listar
def listar_tickets(db, user):
    return ticket_repo.listar_tickets(db, user)



# Obtener
def get_ticket(db, ticket_id, user):
    ticket = ticket_repo.get_ticket(db, ticket_id, user)

    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    return ticket

# Obtener por número de ticket
def get_ticket_by_number(db, num_ticket, user):  
    ticket = ticket_repo.get_ticket_by_number(db, num_ticket, user)

    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    return ticket

# Actualizar
def actualizar_ticket(db, ticket_id, data, user):
    if not ticket_repo.get_ticket(db, ticket_id, user):
        raise HTTPException(404, "Ticket no encontrado")

    ticket_repo.actualizar_ticket(db, ticket_id, data)

    db.commit()

    return {"mensaje": "Ticket actualizado"}


# Asignar ticket
def asignar_ticket(db, ticket_id, id_tec, id_area, user):
    if user["id_rol"] not in [1, 2]:
        raise HTTPException(403, "No autorizado")

    ticket_repo.asignar_ticket(db, ticket_id, id_tec, id_area)

    db.commit()

    return {"mensaje": "Ticket asignado"}



# Cambiar estado
def cambiar_estado(db, ticket_id, estado, user):
    ticket_repo.cambiar_estado(db, ticket_id, estado)

    db.commit()

    return {"mensaje": f"Estado cambiado a {estado}"}


#escalar ticket
def escalar_ticket(db, ticket_id, data, user):

    # validar ticket
    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    # solo técnicos o admin
    if user["id_rol"] not in [1, 2, 3]:
        raise HTTPException(403, "No autorizado")

    # evitar escalar a misma área
    if ticket["id_area"] == data.id_area:
        raise HTTPException(400, "Ya pertenece a esa área")

    ticket_repo.escalar_ticket(db, ticket_id, data)

    db.commit()

    return {
        "mensaje": "Ticket escalado",
        "nuevo_area": data.id_area,
        "nuevo_tecnico": data.id_tec
    }


# Agregar solución
def agregar_solucion(db, ticket_id, data, user):

    #validar ticket (multi-tenant incluido)
    ticket = ticket_repo.get_ticket(db, ticket_id, user)
    if not ticket:
        raise HTTPException(404, "Ticket no encontrado")

    #solo técnico o admin
    if user["id_rol"] not in [1, 2, 3]:
        raise HTTPException(403, "No autorizado")

    #agregar solución
    ticket_repo.agregar_solucion(db, ticket_id, data.solucion)

    #guardar historial en comentarios
    comentario = ComentarioCreate(
        comentario=f"Solución aplicada: {data.solucion}",
        tipo="interno"
    )

    ticket_comentario_repo.crear_comentario(
        db,
        ticket_id,
        user,
        comentario
    )

    db.commit()

    return {
        "mensaje": "Ticket resuelto correctamente",
        "ticket_id": ticket_id,
        "estado": "Resuelto"
    }