from pydantic import BaseModel


class ComentarioCreate(BaseModel):
    comentario: str
    tipo: str  # "interno" o "publico"