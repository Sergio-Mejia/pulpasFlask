from Controladores import precio_controlador
from Modelos import precio
from flask_smorest import Blueprint
from flask import make_response
from control_errores import control_errores

precioBluePrint = Blueprint(
    'Administrar Precios', 'precio', url_prefix='/precio',
    description='Administrar Precios'
)


@precioBluePrint.route('/create', methods=['POST'])
@precioBluePrint.arguments(precio.valorSchemaCreate, location='json')
@control_errores()
def create(data):
    valor = data['valor']
    mensaje_respuesta = precio_controlador.create(valor)
    return make_response(mensaje_respuesta, 200)