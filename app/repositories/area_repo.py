def crear_area(db, data):
    cursor = db.cursor()
    query = """
        INSERT INTO area (nombre, descripcion, estado) 
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (data.nombre, data.descripcion, "Activo"))
    return cursor.lastrowid

def listar_areas(db):
    cursor = db.cursor()
    query = "SELECT id, nombre, descripcion, estado FROM area"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    areas = []
    for row in rows:
        areas.append({
            "id": row["id"],
            "nombre": row["nombre"],
            "descripcion": row["descripcion"],
            "estado": row["estado"]
        })
    return areas

def get_area(db, id_area):
    cursor = db.cursor()
    query = "SELECT id, nombre, descripcion, estado FROM area WHERE id = %s"
    cursor.execute(query, (id_area,))
    row = cursor.fetchone()
    
    if row:
        return {
            "id": row["id"],
            "nombre": row["nombre"],
            "descripcion": row["descripcion"],
            "estado": row["estado"]
        }
    return None

def actualizar_area(db, id_area, data):
    cursor = db.cursor()
    update_data = data.dict(exclude_unset=True)
    updates = []
    values = []
    
    for key, value in update_data.items():
        updates.append(f"{key} = %s")
        values.append(value)
        
    if not updates:
        return
        
    values.append(id_area)
    query = f"UPDATE area SET {', '.join(updates)} WHERE id = %s"
    cursor.execute(query, tuple(values))

def cambiar_estado(db, id_area, estado):
    cursor = db.cursor()
    query = "UPDATE area SET estado = %s WHERE id = %s"
    cursor.execute(query, (estado, id_area))