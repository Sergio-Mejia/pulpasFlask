from flask import jsonify
from database import db
from Modelos.fruta import Fruta


def create(descripcion: str) -> dict:
    fruta_n = Fruta(descripcion)
    db.session.add(fruta_n)
    db.session.commit()
    respuesta = {"Respuesta":f"Se creó la fruta {fruta_n.descripcion}"}
    return respuesta


def delete(id: int) -> dict:
    para_borrar = Fruta.query.get(id)
    db.session.delete(para_borrar)
    db.session.commit()
    respuesta = {"Respuesta": f"Se eliminó la fruta correctamente"}
    return respuesta


def update(id: int, descripcion:str) -> dict:
    to_update = Fruta.query.get(id)
    to_update.descripcion = descripcion
    db.session.add(to_update)
    db.session.commit()
    respuesta = {"Respuesta": f"Se actualizó la fruta a {descripcion}"}
    return respuesta


def get() -> dict:
    listar = Fruta.query.all()
    return jsonify(frutas=[i.serialize for i in listar])
