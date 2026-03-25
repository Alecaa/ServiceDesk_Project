
def crear_ticket(db, data, user, num_ticket):
    cursor = db.cursor()

    #obtener codigo_empresa desde DB
    cursor.execute(
        "SELECT codigo_empresa FROM empresa WHERE id = %s",
        (user["id_empresa"],)
    )
    empresa = cursor.fetchone()

    if not empresa:
        raise Exception("Empresa no encontrada")

    codigo_empresa = empresa["codigo_empresa"]

    query = """
    INSERT INTO tickets (
        num_ticket,
        codigo_empresa,
        id_usr,
        modulo,
        tipo_caso,
        descripcion,
        estado,
        prioridad,
        fecha_creacion
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())
    """

    cursor.execute(query, (
        num_ticket,
        codigo_empresa, 
        user["id"],
        data.modulo,
        data.tipo_caso,
        data.descripcion,
        "Abierto",
        data.prioridad
    ))

    return cursor.lastrowid



# Listar tickets
def listar_tickets(db, user):
    cursor = db.cursor()

    # super admin
    if user["id_rol"] == 1:
        cursor.execute("SELECT * FROM tickets ORDER BY id DESC")
        return cursor.fetchall()

    # empresa
    query = """
    SELECT t.*
    FROM tickets t
    JOIN empresa e ON t.codigo_empresa = e.codigo_empresa
    WHERE e.id = %s
    ORDER BY t.id DESC
    """

    cursor.execute(query, (user["id_empresa"],))
    return cursor.fetchall()



# Obtener ticket
def get_ticket(db, ticket_id, user):
    cursor = db.cursor()

    query = """
    SELECT * FROM tickets
    WHERE id = %s
    """

    cursor.execute(query, (ticket_id,))
    ticket = cursor.fetchone()

    if not ticket:
        return None

    # Solo super admin o empresa dueña del ticket pueden verlo
    if user["id_rol"] != 1 and ticket["codigo_empresa"] != user["id_empresa"]:
        return None

    return ticket

# Obtener ticket por número de ticket
def get_ticket_by_number(db, num_ticket, user):
    cursor = db.cursor()
    print("Buscando ticket con número:", num_ticket)  # Debug: Verificar el número de ticket recibido
    query = """
    SELECT * FROM tickets
    WHERE num_ticket = %s
    """

    cursor.execute(query, (num_ticket,))
    ticket = cursor.fetchone()

    if not ticket:
        return None

    # Solo super admin o empresa dueña del ticket pueden verlo
    if user["id_rol"] != 1 and ticket["codigo_empresa"] != user["id_empresa"]:
        return None

    return ticket

# Actualizar ticket
def actualizar_ticket(db, ticket_id, data):
    cursor = db.cursor()

    data_dict = data.dict(exclude_unset=True)

    fields = []
    values = []

    for k, v in data_dict.items():
        fields.append(f"{k}=%s")
        values.append(v)

    values.append(ticket_id)

    query = f"""
    UPDATE tickets
    SET {", ".join(fields)}
    WHERE id = %s
    """

    cursor.execute(query, tuple(values))



# Asignar técnico
def asignar_ticket(db, ticket_id, id_tec, id_area):
    cursor = db.cursor()

    query = """
    UPDATE tickets
    SET id_tec=%s, id_area=%s, estado='En proceso'
    WHERE id=%s
    """

    cursor.execute(query, (id_tec, id_area, ticket_id))


# Cambiar estado
def cambiar_estado(db, ticket_id, estado):
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tickets SET estado=%s WHERE id=%s",
        (estado, ticket_id)
    )



# Escalar ticket
def escalar_ticket(db, ticket_id, data):
    cursor = db.cursor()

    query = """
    UPDATE tickets
    SET 
        escalado = 1,
        area_escalado_id = %s,
        tec_escalado_id = %s,
        estado = 'Escalado'
    WHERE id = %s
    """

    cursor.execute(query, (
        data.id_area,
        data.id_tec,
        ticket_id
    ))

#actualizar número de ticket después de crear el ticket para que sea tipo TKT-000001
def actualizar_numero_ticket(db, ticket_id, num_ticket):
    cursor = db.cursor()

    cursor.execute(
        "UPDATE tickets SET num_ticket = %s WHERE id = %s",
        (num_ticket, ticket_id)
    )


def agregar_solucion(db, ticket_id, solucion):
    cursor = db.cursor()

    query = """
    UPDATE tickets
    SET solucion = %s,
        estado = 'Resuelto'
    WHERE id = %s
    """

    cursor.execute(query, (solucion, ticket_id))