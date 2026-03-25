# conexión a la base de datos

from pymysql.cursors import DictCursor
import pymysql
from app.config.settings import settings

def get_connection():
    return pymysql.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        port=settings.DB_PORT,
        cursorclass=DictCursor # Devuelve resultados como diccionarios en lugar de tuplas
    )

def get_db():
    db = get_connection()
    try:
        yield db
    finally:
        db.close()