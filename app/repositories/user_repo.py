#Crear usuario
def crear_usuario(db, data, hashed_password):
    cursor = db.cursor()

    query = """
    INSERT INTO users (
        username,
        nombre,
        password,
        correo,
        contacto,
        id_rol,
        id_empresa,
        id_area,
        fecha_creacion,
        estado
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW(),'Activo')
    """

    cursor.execute(query, (
        data.username,
        data.nombre,
        hashed_password,
        data.correo,
        data.contacto,
        data.id_rol,
        data.id_empresa,
        data.id_area
    ))

    return cursor.lastrowid

#Usuario por id
def get_user_by_id(db, user_id):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return cursor.fetchone()


#Usuario por username
def get_user_by_username(db, username):
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    return cursor.fetchone()

#Listar usuarios
def listar_usuarios(db):
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, username, nombre, correo, contacto, id_rol, id_empresa, id_area, estado
        FROM users
        ORDER BY id DESC
    """)
    return cursor.fetchall()

#actualizar usuario
def actualizar_usuario(db, user_id, data):
    cursor = db.cursor()

    data_dict = data.dict(exclude_unset=True)

    if not data_dict:
        return

    fields = []
    values = []

    for key, value in data_dict.items():
        fields.append(f"{key}=%s")
        values.append(value)

    values.append(user_id)

    query = f"UPDATE users SET {', '.join(fields)} WHERE id=%s"

    cursor.execute(query, tuple(values))

#Cambiar estado
def cambiar_estado(db, user_id, estado):
    cursor = db.cursor()

    cursor.execute(
        "UPDATE users SET estado=%s WHERE id=%s",
        (estado, user_id)
    )

# Listar por empresa
def listar_por_empresa(db, id_empresa):
    cursor = db.cursor()

    query = """
    SELECT id, username, nombre, correo, id_empresa
    FROM users
    WHERE id_empresa = %s
    """

    cursor.execute(query, (id_empresa,))
    return cursor.fetchall()

def listar_todos(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()