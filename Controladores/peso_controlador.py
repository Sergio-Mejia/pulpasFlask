from database import db
from Modelos.peso import Peso

def create(descripcion: str) -> dict:
    peso_n = Peso(descripcion)
    db.session.add(peso_n)
    db.session.commit()
    respuesta = "Nuevo peso creado"

    return respuesta

def delete(id: int) -> dict:
    peso_borrar = Peso.query.get(id)
    db.session.delete(peso_borrar)
    db.session.commit()
    respuesta = "Peso eliminado"

    return respuesta