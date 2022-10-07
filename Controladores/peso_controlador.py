from database import db
from flask import jsonify
from Modelos.peso import Peso

def create(descripcion: str, id_precio:int) -> dict:
    peso_n = Peso(descripcion, id_precio)
    db.session.add(peso_n)
    db.session.commit()
    respuesta = {"Respuesta": f"Nuevo peso creado de {peso_n.descripcion}"}

    return respuesta

def delete(id: int) -> dict:
    peso_borrar = Peso.query.get(id)
    db.session.delete(peso_borrar)
    db.session.commit()
    respuesta = {"Respuesta": f"Peso eliminado correctamente"}

    return respuesta

def update(id:int, descripcion:str, id_precio: int) -> dict:
    peso_actualizar = Peso.query.get(id)
    peso_actualizar.descripcion = descripcion
    peso_actualizar.id_precio = id_precio
    db.session.add(peso_actualizar)
    db.session.commit()
    respuesta = {"Respuesta": f"Se actualizó el peso {id} a {descripcion}"}

    return respuesta

def get() -> dict:
    para_listar = Peso.query.all()
    return jsonify(Peso =[i.serialize for i in para_listar])