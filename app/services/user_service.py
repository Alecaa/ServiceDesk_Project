from fastapi import HTTPException
from app.repositories import user_repo
from app.utils.security import hash_password 

''' Crear usuario '''
def crear_usuario(db, data):
    ''' Validar username único '''
    if user_repo.get_user_by_username(db, data.username):
        raise HTTPException(400, "El username ya existe")

    hashed_password = hash_password(data.password)  

    user_id = user_repo.crear_usuario(db, data, hashed_password)

    db.commit()

    return {
        "mensaje": "Usuario creado",
        "user_id": user_id
    }



''' Listar usuarios '''
def listar_usuarios(db, user):

    ''' Super admin ve todo '''
    if user["id_rol"] == 1:
        return user_repo.listar_todos(db)

    ''' Admin solo su empresa '''
    return user_repo.listar_por_empresa(db, user["id_empresa"])




''' Obtener usuario por ID '''
def get_usuario(db, user_id):
    user = user_repo.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(404, "Usuario no encontrado")

    return user



''' Actualizar usuario'''
def actualizar_usuario(db, user_id, data):
    if not user_repo.get_user_by_id(db, user_id):
        raise HTTPException(404, "Usuario no encontrado")

    user_repo.actualizar_usuario(db, user_id, data)

    db.commit()

    return {"mensaje": "Usuario actualizado"}




'''CAMBIAR ESTADO DE USUARIO: Activo/Inactivo'''
def cambiar_estado(db, user_id, estado):
    estado = estado.capitalize()

    if estado not in ["Activo", "Inactivo"]:
        raise HTTPException(400, "Estado inválido")

    if not user_repo.get_user_by_id(db, user_id):
        raise HTTPException(404, "Usuario no encontrado")

    user_repo.cambiar_estado(db, user_id, estado)

    db.commit()

    return {"mensaje": f"Usuario {estado}"}