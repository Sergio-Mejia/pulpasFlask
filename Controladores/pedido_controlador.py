from database import db
from flask import jsonify
from Modelos.pedido import Pedido


def create(id_fruta: int, id_peso: int, cantidad: int) -> dict:
    pedido_n = Pedido(id_fruta, id_peso, cantidad)
    db.session.add(pedido_n)
    db.session.commit()
    respuesta = 'Pedido creado'

    return respuesta


def delete(id_pedido: int) -> dict:
    para_borrar = Pedido.query.get(id_pedido)
    db.session.delete(para_borrar)
    db.session.commit()
    respuesta = 'Registro borrado'

    return respuesta

def get() -> dict:
    para_listar = Pedido.query.all()
    return jsonify(Pedido = [i.serialize for i in para_listar] )