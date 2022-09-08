from database import db
from Modelos.peso import Peso

def create(descripcion: str) -> dict:
    peso_n = Peso(descripcion)
    db.session.add(peso_n)
    db.session.commit()
    respuesta = "Nuevo peso creado"

    return respuesta
