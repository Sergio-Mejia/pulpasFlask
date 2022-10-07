from database import db
import marshmallow as ma


class Precio(db.Model):
    __tablename__ = "precio"

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer)

    def __init__(self, valor: int):
        self.valor = valor

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'valor': self.valor
        }

    @property
    def serialize_many2many(self) -> dict:
        """
        Devuelve los datos del objeto en un formato serializable
        Cuando son mas de 1 registros se utiliza el metodo many2many.
        """
        return [item.serialize for item in self.many2many]


class valorSchemaCreate(ma.Schema):
    "Esquema de validacion para la creación de un valor"

    class Meta:
        ordered = True

    valor = ma.fields.Integer(required=True)