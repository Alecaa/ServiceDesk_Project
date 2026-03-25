from pydantic import BaseModel, EmailStr, Field
from typing import Optional



# Crear empresa
class EmpresaCreate(BaseModel):
    razon_social: str = Field(..., min_length=3, max_length=150)
    identificacion: str = Field(..., min_length=5, max_length=50)
    contacto: str = Field(..., min_length=3, max_length=100)
    correo: EmailStr


# Actualizar empresa
class EmpresaUpdate(BaseModel):
    razon_social: Optional[str] = Field(None, min_length=3, max_length=150)
    identificacion: Optional[str] = Field(None, min_length=5, max_length=50)
    contacto: Optional[str] = Field(None, min_length=3, max_length=100)
    correo: Optional[EmailStr]



# Respuesta empresa
class EmpresaResponse(BaseModel):
    id: int
    codigo_empresa: str
    razon_social: str
    identificacion: str
    contacto: str
    correo: str
    estado: str

    class Config:
        from_attributes = True