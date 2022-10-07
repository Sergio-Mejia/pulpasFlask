from database import db
from flask import jsonify
from Modelos.pedido import Pedido

def create(id_fruta: int, id_peso: int, cantidad: int) -> dict:
    pedido_n = Pedido(id_fruta, id_peso, cantidad)
    db.session.add(pedido_n)
    db.session.commit()
    respuesta = {'Respuesta': f'Se creó pedido con fruta: {id_fruta} de {id_peso} '
                              f'de peso con una cantidad de {cantidad} pulpas'}

    return respuesta


def delete(id_pedido: int) -> dict:
    para_borrar = Pedido.query.get(id_pedido)
    db.session.delete(para_borrar)
    db.session.commit()
    respuesta = {'Respuesta': f'Se eliminó el pedido {id_pedido} correctamente'}

    return respuesta

def get() -> dict:
    para_listar = Pedido.query.all()
    return jsonify(Pedido = [i.serialize for i in para_listar] )

def update(id_pedido: int, id_fruta: int, id_peso: int, cantidad: int) -> dict:
    para_actualizar = Pedido.query.get(id_pedido)
    para_actualizar.id_fruta = id_fruta
    para_actualizar.id_peso = id_peso
    para_actualizar.cantidad = cantidad
    db.session.add(para_actualizar)
    db.session.commit()
    respuesta = {"Respuesta":f"Se actualizó el pedido {id_pedido} con la fruta {id_fruta}"
                             f", el peso {id_peso} y cantidad de {cantidad} pulpas"}

    return respuesta
