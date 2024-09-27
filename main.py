# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, get_db  # Asegúrate de que esta ruta sea correcta

# Crear la instancia de FastAPI
app = FastAPI()

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Ruta para obtener todos los empleados
@app.get("/empleados/", response_model=list[schemas.Empleado])  # Agrega el modelo de respuesta
def leer_empleados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    empleados = db.query(models.Empleado).order_by(models.Empleado.idempleado).offset(skip).limit(limit).all()
    return empleados

# Ruta para obtener un empleado por su ID
@app.get("/empleados/{idempleado}", response_model=schemas.Empleado)  # Modelo de respuesta
def leer_empleado(idempleado: int, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.idempleado == idempleado).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

# Ruta para crear un nuevo empleado
@app.post("/empleados/", response_model=schemas.Empleado)  # Modelo de respuesta
def crear_empleado(empleado: schemas.EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleado = models.Empleado(nombre=empleado.nombre, apellidos=empleado.apellidos, puesto=empleado.puesto)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

# Ruta para eliminar un empleado
@app.delete("/empleados/{idempleado}")
def eliminar_empleado(idempleado: int, db: Session = Depends(get_db)):
    empleado = db.query(models.Empleado).filter(models.Empleado.idempleado == idempleado).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    db.delete(empleado)
    db.commit()
    return {"mensaje": "Empleado eliminado correctamente"}

# Ruta para actualizar un empleado
@app.put("/empleados/{idempleado}", response_model=schemas.Empleado)  # Modelo de respuesta
def actualizar_empleado(idempleado: int, empleado: schemas.EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleado = db.query(models.Empleado).filter(models.Empleado.idempleado == idempleado).first()
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    db_empleado.nombre = empleado.nombre
    db_empleado.apellidos = empleado.apellidos
    db_empleado.puesto = empleado.puesto
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

