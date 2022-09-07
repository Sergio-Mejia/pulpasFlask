from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from database import db
from Controladores import fruta_controlador
from flask import jsonify


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


def loaddbSettings():
    with open('dbSettings.json') as f:
        data = json.load(f)
    data = f"""postgresql://{data["user"]}:{data["password"]}@localhost/{data["database"]}"""
    return data


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurar Base de Datos
    dbSettings = loaddbSettings()
    app.config['SQLALCHEMY_DATABASE_URI'] = dbSettings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/fruta", methods=['GET'])
    def getFruta():
        json = fruta_controlador.get()
        return json

    return app

def set_up_db(app):
    """Crear Tablas"""
    with app.app_context():
        db.create_all()





if __name__ == '__main__':
    dataConfig = loadFileConfig()
    app = create_app()
    app.app_context().push()
    set_up_db(app)
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
