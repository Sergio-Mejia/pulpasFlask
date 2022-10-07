from database import db
from Modelos.precio import Precio

def create(valor:int) -> dict:
    precio_n = Precio(valor)
    db.session.add(precio_n)
    db.session.commit()
    respuesta = {"Respuesta": f"Valor creado con {precio_n.valor}"}

    return respuesta