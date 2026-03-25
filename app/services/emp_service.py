from fastapi import HTTPException, status
from app.repositories import emp_repo


# Crear empresa
def crear_empresa(db, data):
    try:
        cursor = db.cursor()

        # 1. Crear empresa
        id_empresa = emp_repo.crear_empresa(db, data)

        # 2. Generar código basado en ID
        codigo = f"EMP{id_empresa:04d}"  # EMP0001, EMP0002...

        # 3. Actualizar código (MISMA TRANSACCIÓN)
        emp_repo.actualizar_codigo(db, id_empresa, codigo)

        db.commit()

        return {
            "mensaje": "Empresa creada correctamente",
            "empresa": {
                "id": id_empresa,
                "codigo_empresa": codigo
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear empresa: {str(e)}"
        )



# Listar empresas
def listar_empresas(db):
    empresas = emp_repo.listar_empresas(db)

    return {
        "total": len(empresas),
        "data": empresas
    }



# Obtener empresa
def get_empresa(db, id_empresa):
    empresa = emp_repo.get_empresa(db, id_empresa)

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa no encontrada"
        )

    return empresa


# Actualizar empresa
def actualizar_empresa(db, id_empresa, data):
    empresa = emp_repo.get_empresa(db, id_empresa)

    if not empresa:
        raise HTTPException(404, "Empresa no encontrada")

    # Validar que haya datos para actualizar
    if not data.dict(exclude_unset=True):
        raise HTTPException(400, "No hay datos para actualizar")

    emp_repo.actualizar_empresa(db, id_empresa, data)

    db.commit()

    return {
        "mensaje": "Empresa actualizada correctamente",
        "id_empresa": id_empresa
    }



# Cambiar estado
def cambiar_estado(db, id_empresa, estado):
    estado = estado.capitalize()  # Normaliza → Activo/Inactivo

    if estado not in ["Activo", "Inactivo"]:
        raise HTTPException(400, "Estado inválido")

    empresa = emp_repo.get_empresa(db, id_empresa)

    if not empresa:
        raise HTTPException(404, "Empresa no encontrada")

    # Evitar updates innecesarios
    if empresa["estado"] == estado:
        return {
            "mensaje": f"La empresa ya está en estado {estado}"
        }

    emp_repo.cambiar_estado(db, id_empresa, estado)

    db.commit()

    return {
        "mensaje": f"Empresa actualizada a {estado}",
        "id_empresa": id_empresa,
        "estado": estado
    }