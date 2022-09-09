from Controladores import pedido_controlador
from Modelos import pedido
from flask_smorest import Blueprint
from flask import make_response

pedidoBlueprint = Blueprint(
    'Administrar Pedidos', 'pedido', url_prefix='/pedido',
    description='Administrar pedidos'
)

@pedidoBlueprint.route('/create', methods=['POST'])
@pedidoBlueprint.arguments(pedido.pedidoSchemaCreate, location='json')
def create(data):
    id_fruta = data['id_fruta']
    id_peso = data['id_peso']
    cantidad = data['cantidad']
    mensaje_respuesta = pedido_controlador.create(id_fruta, id_peso, cantidad)
    return make_response(mensaje_respuesta, 200)

