# schemas.py
from pydantic import BaseModel

class EmpleadoBase(BaseModel):
    nombre: str
    apellidos: str
    puesto: str

class EmpleadoCreate(EmpleadoBase):  
    pass

class Empleado(EmpleadoBase):  
    idempleado: int

    class Config:
        from_attributes = True  # Cambia orm_mode a from_attributes
