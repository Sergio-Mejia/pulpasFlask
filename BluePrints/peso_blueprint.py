from Controladores import peso_controlador
from Modelos import peso
from flask_smorest import Blueprint
from flask import make_response


pesoBluePrint = Blueprint(
    'Administrar Peso', 'peso', url_prefix='/peso',
    description='Administrar Peso'
)

@pesoBluePrint.route('/create', methods=['POST'])
@pesoBluePrint.arguments(peso.pesoSchemaCreate, location='json')
def create(data):
    descripcion = data['descripcion']
    mensaje_respuesta = peso_controlador.create(descripcion)
    return make_response(mensaje_respuesta, 200)

@pesoBluePrint.route('/delete', methods=['DELETE'])
@pesoBluePrint.arguments(peso.pesoSchemaDelete, location='json')
def delete(data):
    id = data['id']
    mensaje_respuesta = peso_controlador.delete(id)
    return make_response(mensaje_respuesta, 200)