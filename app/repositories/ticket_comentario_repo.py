
# Crear comentario
def crear_comentario(db, ticket_id, user, data):
    cursor = db.cursor()

    query = """
    INSERT INTO tickets_comentarios (
        id_tkt,
        id_tec,
        comentario,
        tipo,
        fecha
    )
    VALUES (%s,%s,%s,%s,NOW())
    """

    cursor.execute(query, (
        ticket_id,
        user["id"],
        data.comentario,
        data.tipo
    ))

    return cursor.lastrowid


# Listar comentarios
def listar_comentarios(db, ticket_id):
    cursor = db.cursor()

    query = """
    SELECT 
        c.id,
        c.comentario,
        c.tipo,
        c.fecha,
        u.nombre as tecnico
    FROM tickets_comentarios c
    LEFT JOIN users u ON u.id = c.id_tec
    WHERE c.id_tkt = %s
    ORDER BY c.fecha ASC
    """

    cursor.execute(query, (ticket_id,))
    return cursor.fetchall()

