from flask_smorest import Blueprint
from flask import make_response
from Controladores import fruta_controlador
from Modelos import fruta


frutaBlueprint = Blueprint(
    'Administrar Fruta', 'fruta', url_prefix='/fruta',
    description='Administrar Frutas'
)


@frutaBlueprint.route('/create', methods=['POST'])
@frutaBlueprint.arguments(fruta.FrutaEsquemasCreate, location='json')
def create(data):
    descripcion = data['descripcion']
    mensaje_respuesta = fruta_controlador.create(descripcion)
    return make_response(mensaje_respuesta, 200)

@frutaBlueprint.route('/delete', methods=['DELETE'])
@frutaBlueprint.arguments(fruta.FrutaEsquemaDelete, location='json')
def delete(data):
    id = data['id']
    mensaje_respuesta = fruta_controlador.delete(id)
    return make_response(mensaje_respuesta, 200)


@frutaBlueprint.route('/update', methods=['PATCH'])
@frutaBlueprint.arguments(fruta.FrutaEsquemaUpdate, location='json')
def update(data):
    id = data['id']
    descripcion = data['descripcion']
    mensaje_respuesta = fruta_controlador.update(id, descripcion)
    return make_response(mensaje_respuesta, 200)

@frutaBlueprint.route('/get', methods=['GET'])
def get():
    mensaje_respuesta = fruta_controlador.get()
    return make_response(mensaje_respuesta, 200)