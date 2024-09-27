from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la cadena de conexión usando los parámetros que proporcionaste
SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://dipole:d1p0l3@ANTENAS\\SQLEXPRESS/prueba?"
    "driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"
)

# Crear el motor de conexión a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos en las peticiones
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
