from pydantic import BaseModel
from typing import Optional


class TicketCreate(BaseModel):
    modulo: str
    tipo_caso: str
    descripcion: str
    prioridad: str


class TicketUpdate(BaseModel):
    descripcion: Optional[str]
    prioridad: Optional[str]
    estado: Optional[str]


class TicketResponse(BaseModel):
    id: int
    num_ticket: str
    codigo_empresa: str
    id_usr: int
    id_tec: Optional[int]
    id_area: Optional[int]
    estado: str
    prioridad: str


class TicketEscalar(BaseModel):
    id_area: int
    id_tec: int | None = None
    motivo: str


class TicketSolucion(BaseModel):
    solucion: str