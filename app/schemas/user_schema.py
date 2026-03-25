from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    nombre: str
    password: str = Field(..., min_length=6)
    correo: EmailStr
    contacto: str

    id_rol: int
    id_empresa: Optional[int] = None
    id_area: Optional[int] = None



class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    contacto: Optional[str] = None
    id_area: Optional[int] = None


class UserResponse(BaseModel):
    id: int
    username: str
    nombre: str
    correo: str
    contacto: str
    id_rol: int
    id_empresa: Optional[int]
    id_area: Optional[int]
    estado: str