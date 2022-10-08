from flask_smorest import Blueprint
from flask import make_response
from Controladores import consultas_controlador
from Modelos import fruta
from Modelos import pedido
from control_errores import control_errores


consultaBlueprint = Blueprint(
    'Consultas', 'consultas', url_prefix='/consulta',
    description='Consultas estadisticas'
)


@consultaBlueprint.route('/get_pedido_fruta', methods=['GET'])
@consultaBlueprint.arguments(fruta.ResultadosEsquemaFruta, location='query')
@control_errores()
def get_pedido_fruta(data):
    mensaje_respuesta = consultas_controlador.get_pedido_por_Fruta(data)
    return make_response(mensaje_respuesta, 200)
