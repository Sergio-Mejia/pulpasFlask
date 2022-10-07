from database import db
import marshmallow as ma

class Peso(db.Model):
    __tablename__ = "peso"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String)
    id_precio = db.Column(db.Integer, db.ForeignKey('precio.id'))

    def __init__(self, descripcion: str, id_precio: int):
        self.descripcion = descripcion
        self.id_precio = id_precio

    @property
    def serialize(self) -> dict:
        """Devuelve los datos del objeto en un formato serializable"""
        return {
            'id': self.id,
            'descripcion': self.descripcion,
            'id_precio': self.id_precio
        }

    @property
    def serialize_many2many(self) -> dict:
        """
        Devuelve los datos del objeto en un formato serializable
        Cuando son mas de 1 registros se utiliza el metodo many2many.
        """
        return [item.serialize for item in self.many2many]


class pesoSchemaCreate(ma.Schema):
    "Esquema de validacion para la creación de peso"
    class Meta:
        ordered = True

    descripcion = ma.fields.String(required=True)
    id_precio = ma.fields.Integer(required=True)

class pesoSchemaDelete(ma.Schema):
    "Esquema de validación para la elimnación de un peso"
    class Meta:
        ordered = True

    id = ma.fields.Integer(required=True)

class pesoSchemaUpdate(ma.Schema):
    "Esquema de validacion para la actualizacion de un peso"
    class Meta:
        ordered = True

    id = ma.fields.Integer(required=True)
    descripcion = ma.fields.String(required=True)
    id_precio = ma.fields.Integer(required=True)

