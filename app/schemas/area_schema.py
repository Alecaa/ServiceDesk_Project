from pydantic import BaseModel
from typing import Optional

class AreaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class AreaCreate(AreaBase):
    pass

class AreaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class AreaEstado(BaseModel):
    estado: str  # "Activo" o "Inactivo"

class AreaResponse(AreaBase):
    id: int
    estado: str

    class Config:
        from_attributes = True