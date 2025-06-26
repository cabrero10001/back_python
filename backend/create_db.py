from app import create_app
from app.models import db
from sqlalchemy import create_engine, text
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL completa
DATABASE_URL = os.getenv("DATABASE_URL")

# Parsear la URL
parsed_url = urlparse(DATABASE_URL)
DB_USER = parsed_url.username
DB_PASSWORD = parsed_url.password
DB_HOST = parsed_url.hostname
DB_NAME = parsed_url.path.lstrip("/")  # elimina el primer "/"

# Crear conexión sin base de datos
engine = create_engine(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}")
with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};"))

# Crear las tablas
app = create_app()
with app.app_context():
    db.create_all()
    print("✅ Tablas creadas")
