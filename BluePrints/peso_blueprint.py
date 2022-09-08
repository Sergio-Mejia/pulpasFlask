from Controladores import peso_controlador
from Modelos import peso
from flask_smorest import Blueprint
from flask import make_response
from control_errores import control_errores


pesoBluePrint = Blueprint(
    'Administrar Peso', 'peso', url_prefix='/peso',
    description='Administrar Peso'
)

@pesoBluePrint.route('/create', methods=['POST'])
@pesoBluePrint.arguments(peso.pesoSchemaCreate, location='json')
@control_errores()
def create(data):
    descripcion = data['descripcion']
    mensaje_respuesta = peso_controlador.create(descripcion)
    return make_response(mensaje_respuesta, 200)

@pesoBluePrint.route('/delete', methods=['DELETE'])
@pesoBluePrint.arguments(peso.pesoSchemaDelete, location='json')
@control_errores()
def delete(data):
    id = data['id']
    mensaje_respuesta = peso_controlador.delete(id)
    return make_response(mensaje_respuesta, 200)

@pesoBluePrint.route('/update', methods=['PATCH'])
@pesoBluePrint.arguments(peso.pesoSchemaUpdate, location='json')
@control_errores()
def update(data):
    id = data['id']
    descripcion = data['descripcion']
    mensaje_respuesta = peso_controlador.update(id, descripcion)
    return make_response(mensaje_respuesta, 200)

@pesoBluePrint.route('/get', methods=['GET'])
@control_errores()
def get():
    mensaje_respuesta = peso_controlador.get()
    return make_response(mensaje_respuesta, 200)