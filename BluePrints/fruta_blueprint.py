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
