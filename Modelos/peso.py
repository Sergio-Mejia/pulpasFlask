from database import db
import marshmallow as ma

class Peso(db.Model):
    __tablename__ = "peso"

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


class pesoSchemaCreate(ma.Schema):
    class Meta:
        ordered = True

    descripcion = ma.fields.String(required=True)