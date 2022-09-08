from database import db
from flask import jsonify
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

def update(id:int, descripcion:str) -> dict:
    peso_actualizar = Peso.query.get(id)
    peso_actualizar.descripcion = descripcion
    db.session.add(peso_actualizar)
    db.session.commit()
    respuesta = "Peso actualizado"

    return respuesta

def get() -> dict:
    para_listar = Peso.query.all()
    return jsonify(Peso =[i.serialize for i in para_listar])