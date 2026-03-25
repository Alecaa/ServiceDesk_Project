
def get_user_by_username(db, username):
    cursor = db.cursor()

    query = """
    SELECT 
        id,
        username,
        password,
        id_rol,
        id_empresa,
        id_area,
        estado
    FROM users
    WHERE username = %s
    """

    cursor.execute(query, (username,))
    return cursor.fetchone()