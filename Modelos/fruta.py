from database import db
import marshmallow as ma


class Fruta(db.Model):
    __tablename__ = "fruta"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String)

    def __init__(self, descripcion: str):
        self.descripcion = descripcion

    @property
    def serialize(self) -> dict:
        """Devuelve los datos del objeto en un formato serializable"""
        return {
            'id': self.id,
            'descripcion': self.descripcion
        }

    @property
    def serialize_many2many(self) -> dict:
        """
        Devuelve los datos del objeto en un formato serializable
        Cuando son mas de 1 registros se utiliza el metodo many2many.
        """
        return [item.serialize for item in self.many2many]


class FrutaEsquemasCreate(ma.Schema):
    "Esquema de validacion para la creacion de una fruta -> Create"
    class Meta:
        ordered = True

    descripcion = ma.fields.String(required=True)

class FrutaEsquemaDelete(ma.Schema):
    "Esquema de validacion para la eliminacion de una fruta"
    class Meta:
        ordered = True

    id = ma.fields.Integer(required=True)

class FrutaEsquemaUpdate(ma.Schema):
    "Esquema de validacion para la actualizacion de una fruta"
    class Meta:
        ordered = True

    id = ma.fields.Integer(required=True)
    descripcion = ma.fields.String(required=True)

class ResultadosEsquemaFruta(ma.Schema):
    """Esquema de validacion para endpoint de Fruta: Get"""
    class Meta:
        ordered = True

    descripcion = ma.fields.String(required=False)