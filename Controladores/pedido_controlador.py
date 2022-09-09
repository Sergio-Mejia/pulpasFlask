from database import db
from Modelos.pedido import Pedido

def create(id_fruta:int, id_peso:int, cantidad:int) -> dict:
    pedido_n = Pedido(id_fruta, id_peso, cantidad)
    db.session.add(pedido_n)
    db.session.commit()
    respuesta = 'Pedido creado'

    return respuesta
