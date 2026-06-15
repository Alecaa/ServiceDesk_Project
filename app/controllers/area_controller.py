from fastapi import APIRouter, Depends
from app.schemas import area_schema
from app.services import area_service
from app.config.db import get_db

router = APIRouter(
    prefix="/areas",
    tags=["Áreas"]
)

@router.post("/")
def crear_area(data: area_schema.AreaCreate, db = Depends(get_db)):
    return area_service.crear_area(db, data)

@router.get("/")
def listar_areas(db = Depends(get_db)):
    return area_service.listar_areas(db)

@router.get("/{id_area}")
def get_area(id_area: int, db = Depends(get_db)):
    return area_service.get_area(db, id_area)

@router.put("/{id_area}")
def actualizar_area(id_area: int, data: area_schema.AreaUpdate, db = Depends(get_db)):
    return area_service.actualizar_area(db, id_area, data)

@router.patch("/{id_area}/estado")
def cambiar_estado(id_area: int, payload: area_schema.AreaEstado, db = Depends(get_db)):
    return area_service.cambiar_estado(db, id_area, payload.estado)