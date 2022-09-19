from database import db
import marshmallow as ma
from sqlalchemy.sql import func



def dump_datetime(value):
    """Deserializa objetos datetime en un string para ser facilmente
        en un JSON."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


class Pedido(db.Model):

    __tablename__ = 'pedido'

    id_pedido = db.Column(db.Integer, primary_key=True)
    id_fruta = db.Column(db.Integer, db.ForeignKey('fruta.id'))
    id_peso = db.Column(db.Integer, db.ForeignKey('peso.id'))
    fecha_registro = db.Column(db.DateTime(timezone=True), server_default=func.now())
    cantidad = db.Column(db.Integer())


    def __init__(self, id_fruta:int, id_peso:int, cantidad:int):
        self.id_fruta = id_fruta
        self.id_peso = id_peso
        self.cantidad = cantidad


    @property
    def serialize(self) -> dict:
        return {
            'id_pedido': self.id_pedido,
            'id_fruta': self.id_fruta,
            'id_peso': self.id_peso,
            'fecha_registro': dump_datetime(self.fecha_registro),
            'cantidad': self.cantidad
        }

    @property
    def serialize_many2many(self) -> dict:
        return [item.serialize for item in self.serialize_many2many]


class pedidoSchemaCreate(ma.Schema):
    class Meta:
        ordered = True

    id_fruta = ma.fields.Integer(required=True)
    id_peso = ma.fields.Integer(required=True)
    cantidad = ma.fields.Integer(required=True)


class pedidoSchemaDelete(ma.Schema):
    class Meta:
        ordered = True

    id_pedido = ma.fields.Integer(required=True)

