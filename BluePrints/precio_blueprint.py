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

@precioBluePrint.route('/get', methods=['GET'])
@control_errores()
def get():
    mensaje_respuesta = precio_controlador.get()
    return make_response(mensaje_respuesta, 200)

@precioBluePrint.route('/delete', methods=['DELETE'])
@precioBluePrint.arguments(precio.precioSchemaDelete, location='query')
@control_errores()
def delete(data):
    id_precio = data['id']
    mensaje_respuesta = precio_controlador.delete(id_precio)
    return make_response(mensaje_respuesta, 200)

@precioBluePrint.route('/update', methods=['PATCH'])
@precioBluePrint.arguments(precio.precioSchemaUpdate, location='json')
@control_errores()
def update(data):
    id = data['id']
    valor = data['valor']
    mensaje_respuesta = precio_controlador.update(id, valor)
    return make_response(mensaje_respuesta, 200)