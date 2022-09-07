from database import db


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
