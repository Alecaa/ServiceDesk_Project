from datetime import datetime



# Insertar empresa
def crear_empresa(db, data):
    cursor = db.cursor()

    query = """
    INSERT INTO empresa (
        razon_social,
        identificacion,
        contacto,
        correo,
        fecha_creacion,
        estado
    ) VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data.razon_social,
        data.identificacion,
        data.contacto,
        data.correo,
        datetime.now(),
        "Activo"
    ))

    return cursor.lastrowid


# Actualizar código empresa
def actualizar_codigo(db, id_empresa, codigo):
    cursor = db.cursor()

    cursor.execute(
        "UPDATE empresa SET codigo_empresa = %s WHERE id = %s",
        (codigo, id_empresa)
    )



# Listar empresas
def listar_empresas(db):
    cursor = db.cursor()

    query = """
    SELECT 
        id,
        codigo_empresa,
        razon_social,
        identificacion,
        contacto,
        correo,
        estado,
        fecha_creacion
    FROM empresa
    ORDER BY id DESC
    """

    cursor.execute(query)
    return cursor.fetchall()



# Obtener empresa por ID
def get_empresa(db, id_empresa):
    cursor = db.cursor()

    query = """
    SELECT 
        id,
        codigo_empresa,
        razon_social,
        identificacion,
        contacto,
        correo,
        estado,
        fecha_creacion
    FROM empresa
    WHERE id = %s
    """

    cursor.execute(query, (id_empresa,))
    return cursor.fetchone()



# Actualizar empresa (DINÁMICO)
def actualizar_empresa(db, id_empresa, data):
    cursor = db.cursor()

    data_dict = data.dict(exclude_unset=True)

    if not data_dict:
        return

    fields = []
    values = []

    for key, value in data_dict.items():
        fields.append(f"{key} = %s")
        values.append(value)

    values.append(id_empresa)

    query = f"""
    UPDATE empresa
    SET {", ".join(fields)}
    WHERE id = %s
    """

    cursor.execute(query, tuple(values))


# Cambiar estado
def cambiar_estado(db, id_empresa, estado):
    cursor = db.cursor()

    query = """
    UPDATE empresa
    SET estado = %s
    WHERE id = %s
    """

    cursor.execute(query, (estado, id_empresa))