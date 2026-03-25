from pydantic import BaseModel
from typing import Optional


class EvidenciaResponse(BaseModel):
    id: int
    nombre_archivo: str
    ruta: str
    tipo: str