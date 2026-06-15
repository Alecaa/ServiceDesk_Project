from fastapi import HTTPException
from app.repositories import area_repo

def crear_area(db, data):
    try:
        id_area = area_repo.crear_area(db, data)
        db.commit()
        return {
            "mensaje": "Área creada correctamente",
            "id": id_area
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear área: {str(e)}")

def listar_areas(db):
    areas = area_repo.listar_areas(db)
    return {
        "total": len(areas),
        "data": areas
    }

def get_area(db, id_area):
    area = area_repo.get_area(db, id_area)
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada")
    return area

def actualizar_area(db, id_area, data):
    try:
        area = area_repo.get_area(db, id_area)
        if not area:
            raise HTTPException(status_code=404, detail="Área no encontrada")
            
        area_repo.actualizar_area(db, id_area, data)
        db.commit()
        return {"mensaje": "Área actualizada correctamente", "id_area": id_area}
    except HTTPException as he:
        raise he
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar: {str(e)}")

def cambiar_estado(db, id_area, estado):
    try:
        estado = estado.capitalize()
        if estado not in ["Activo", "Inactivo"]:
            raise HTTPException(status_code=400, detail="Estado inválido")
            
        area = area_repo.get_area(db, id_area)
        if not area:
            raise HTTPException(status_code=404, detail="Área no encontrada")
            
        if area["estado"] == estado:
            return {"mensaje": f"El área ya se encuentra {estado}"}
            
        area_repo.cambiar_estado(db, id_area, estado)
        db.commit()
        return {"mensaje": f"Área actualizada a {estado}", "id_area": id_area}
    except HTTPException as he:
        raise he
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al cambiar estado: {str(e)}")