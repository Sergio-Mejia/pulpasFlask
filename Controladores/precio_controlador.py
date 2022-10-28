from flask import jsonify
from database import db
from Modelos.precio import Precio

def create(valor:int) -> dict:
    precio_n = Precio(valor)
    db.session.add(precio_n)
    db.session.commit()
    respuesta = {"Respuesta": f"Valor creado con {precio_n.valor}"}

    return respuesta

def get() -> dict:
    listar = Precio.query.all()
    return jsonify(Precio = [i.serialize for i in listar])

def delete(id:int) -> dict:
    para_eliminar = Precio.query.get(id)
    db.session.delete(para_eliminar)
    db.session.commit()
    respuesta = {"Respuesta": f"El precio {para_eliminar.valor} fue eliminado"}

    return respuesta

def update(id:int, valor:int) -> dict:
    para_actualizar = Precio.query.get(id)
    para_actualizar.valor = valor
    db.session.add(para_actualizar)
    db.session.commit()
    respuesta = {"Respuesta": f"El precio {valor} fue actualizado"}

    return respuesta