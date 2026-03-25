from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from app.schemas.emp_schema import EmpresaCreate, EmpresaUpdate
from app.services import emp_service
from app.config.db import get_db
from app.dependencies.auth import require_super_admin

router = APIRouter(prefix="/empresa", tags=["Empresa"])


# Crear empresa
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_empresa(
    data: EmpresaCreate,
    db=Depends(get_db),
    user=Depends(require_super_admin)
):
    return emp_service.crear_empresa(db, data)



# Listar empresas
@router.get("/")
def listar_empresas(
    db=Depends(get_db),
    user=Depends(require_super_admin)
):
    return emp_service.listar_empresas(db)



# Obtener empresa por ID
@router.get("/{emp_id}")
def obtener_empresa(
    emp_id: int = Path(..., gt=0),
    db=Depends(get_db),
    user=Depends(require_super_admin)
):
    empresa = emp_service.get_empresa(db, emp_id)

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return empresa



# Actualizar empresa
@router.put("/{emp_id}")
def actualizar_empresa(
    emp_id: int = Path(..., gt=0),
    data: EmpresaUpdate = None,
    db=Depends(get_db),
    user=Depends(require_super_admin)
):
    empresa = emp_service.actualizar_empresa(db, emp_id, data)

    if not empresa:
        raise HTTPException(404, "Empresa no encontrada")

    return empresa



# Cambiar estado (Activo/Inactivo)
@router.patch("/{emp_id}/estado")
def cambiar_estado_empresa(
    emp_id: int = Path(..., gt=0),
    estado: str = Query(..., pattern="^(Activo|Inactivo)$"),
    db=Depends(get_db),
    user=Depends(require_super_admin)
):
    empresa = emp_service.cambiar_estado(db, emp_id, estado)

    if not empresa:
        raise HTTPException(404, "Empresa no encontrada")

    return {
        "mensaje": "Estado actualizado correctamente",
        "empresa": empresa
    }