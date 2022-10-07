from Controladores import pedido_controlador
from Modelos import pedido
from flask_smorest import Blueprint
from flask import make_response

from control_errores import control_errores

pedidoBlueprint = Blueprint(
    'Administrar Pedidos', 'pedido', url_prefix='/pedido',
    description='Administrar pedidos'
)

@pedidoBlueprint.route('/create', methods=['POST'])
@pedidoBlueprint.arguments(pedido.pedidoSchemaCreate, location='query')
@control_errores()
def create(data):
    id_fruta = data['id_fruta']
    id_peso = data['id_peso']
    cantidad = data['cantidad']
    mensaje_respuesta = pedido_controlador.create(id_fruta, id_peso, cantidad)
    return make_response(mensaje_respuesta, 200)

@pedidoBlueprint.route('/delete', methods=['DELETE'])
@pedidoBlueprint.arguments(pedido.pedidoSchemaDelete, location='query')
@control_errores()
def delete(data):
    id_pedido = data['id_pedido']
    mensaje_respuesta = pedido_controlador.delete(id_pedido)
    return make_response(mensaje_respuesta, 200)

@pedidoBlueprint.route('/get', methods=['GET'])
@control_errores()
def get():
    mensaje_respuesta = pedido_controlador.get()
    return make_response(mensaje_respuesta, 200)


@pedidoBlueprint.route('/update', methods=['PATCH'])
@pedidoBlueprint.arguments(pedido.pedidoSchemaUpdate, location='query')
@control_errores()
def update(data):
    id_pedido = data['id_pedido']
    id_fruta = data['id_fruta']
    id_peso = data['id_peso']
    cantidad = data['cantidad']
    mensaje_respuesta = pedido_controlador.update(id_pedido, id_fruta, id_peso, cantidad)
    return make_response(mensaje_respuesta, 200)