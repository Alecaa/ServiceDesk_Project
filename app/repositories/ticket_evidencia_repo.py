def guardar_evidencia(db, ticket_id, nombre, ruta, tipo):
    cursor = db.cursor()

    query = """
    INSERT INTO tickets_evidencias (
        id_tkt,
        nombre_archivo,
        ruta,
        tipo,
        fecha
    )
    VALUES (%s,%s,%s,%s,NOW())
    """

    cursor.execute(query, (ticket_id, nombre, ruta, tipo))


def listar_evidencias(db, ticket_id):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, nombre_archivo, ruta, tipo, fecha
        FROM tickets_evidencias
        WHERE id_tkt = %s
        ORDER BY fecha DESC
    """, (ticket_id,))

    return cursor.fetchall()