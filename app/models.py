from sqlalchemy import Column, Integer, String
from .database import Base

# Modelo de ejemplo para una tabla 'Moldes'
class Empleado(Base):
    __tablename__ = "empleado"

    idempleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellidos = Column(String, index=True)
    puesto = Column(String, index=True)
    estado = Column(String, index=True)
