from fastapi import APIRouter, Depends, Path, Query
from app.schemas.ticket_schema import TicketCreate, TicketUpdate
from app.services import ticket_service
from app.config.db import get_db
from app.dependencies.auth import get_current_user, require_admin_or_super
from app.schemas.ticket_schema import TicketEscalar
from fastapi import UploadFile, File, Depends
from app.services import ticket_evidencia_service
from app.schemas.ticket_schema import TicketSolucion

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# Crear ticket (cliente o admin)
@router.post("/")
def crear_ticket(
    data: TicketCreate,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.crear_ticket(db, data, user)


# Listar tickets
@router.get("/")
def listar_tickets(
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.listar_tickets(db, user)


# Obtener ticket
@router.get("/{ticket_id}")
def obtener_ticket(
    ticket_id: int = Path(...),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.get_ticket(db, ticket_id, user)

# Obtener ticket oor numero de ticket
@router.get("/number/{num_ticket}")
def obtener_ticket_number(
    num_ticket: str = Path(...),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    print(f"Obteniendo ticket por número: {num_ticket} para usuario {user['id']}")
    return ticket_service.get_ticket_by_number(db, num_ticket, user)


# Actualizar ticket
@router.put("/{ticket_id}")
def actualizar_ticket(
    ticket_id: int,
    data: TicketUpdate,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.actualizar_ticket(db, ticket_id, data, user)


# Asignar técnico
@router.post("/{ticket_id}/asignar")
def asignar_ticket(
    ticket_id: int,
    id_tec: int = Query(...),
    id_area: int = Query(...),
    db=Depends(get_db),
    user=Depends(require_admin_or_super)
):
    return ticket_service.asignar_ticket(db, ticket_id, id_tec, id_area, user)


# Cambiar estado
@router.patch("/{ticket_id}/estado")
def cambiar_estado(
    ticket_id: int,
    estado: str = Query(...), #define parámetros de consulta. Estado se obtiene de la URL 
    #como query param. Query le dice a FastAPI que espere un parámetro de consulta llamado "estado" en la URL.
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.cambiar_estado(db, ticket_id, estado, user)


#escalar ticket
@router.post("/{ticket_id}/escalar")
def escalar_ticket(
    ticket_id: int,
    data: TicketEscalar,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.escalar_ticket(db, ticket_id, data, user)


@router.post("/{ticket_id}/evidencias")
def subir_evidencia(
    ticket_id: int,
    file: UploadFile = File(...),
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_evidencia_service.subir_evidencia(db, ticket_id, file, user)



# Agregar solución
@router.post("/{ticket_id}/solucion")
def agregar_solucion(
    ticket_id: int,
    data: TicketSolucion,
    db=Depends(get_db),
    user=Depends(get_current_user)
):
    return ticket_service.agregar_solucion(db, ticket_id, data, user)