from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from database import db
from flask_smorest import Api
from Controladores import fruta_controlador
from BluePrints import fruta_blueprint
from BluePrints import peso_blueprint
from BluePrints import pedido_blueprint
from BluePrints import precio_blueprint
from BluePrints import consultas_blueprint
from flask import jsonify


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


def loaddbSettings():
    with open('dbSettings.json') as f:
        data = json.load(f)
    data = f"""postgresql://{data["user"]}:{data["password"]}@{data["host"]}/{data["database"]}"""
    return data


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurar Base de Datos
    dbSettings = loaddbSettings()
    app.config['SQLALCHEMY_DATABASE_URI'] = dbSettings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    #swagger
    app.config["API_TITLE"] = "Backend Pulpas fruta"
    app.config["API_VERSION"] = "0.1.0"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_JSON_PATH"] = "api-spec.json"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # noqa: 501

    #Registrar Blueprints
    api = Api(app)
    api.register_blueprint(fruta_blueprint.frutaBlueprint)
    api.register_blueprint(peso_blueprint.pesoBluePrint)
    api.register_blueprint(pedido_blueprint.pedidoBlueprint)
    api.register_blueprint(precio_blueprint.precioBluePrint)
    api.register_blueprint(consultas_blueprint.consultaBlueprint)

    return app


def set_up_db(app):
    """Crear todas las Tablas"""
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    app = create_app()
    app.app_context().push()
    set_up_db(app)
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
