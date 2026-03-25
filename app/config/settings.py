# Variables de entorno, config general.

from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

class Settings:
    # Base de datos
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = int(os.getenv("DB_PORT", 3306))

    # Seguridad
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS = 8

# instancia global
settings = Settings()