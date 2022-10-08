from sqlalchemy import func
from Modelos.pedido import Pedido
import marshmallow as ma
from Modelos.fruta import Fruta
from Modelos.precio import Precio
from Modelos.peso import Peso
from database import db
from sqlalchemy.sql import func, label, cast, desc

def get_pedido_por_Fruta(data: dict) -> dict:
    if data.get("descripcion") is None:
        rs = db.session.query(Pedido.id_pedido.label('id_pedido'),
                                Pedido.fecha_registro.label('fecha_venta'),
                                Fruta.descripcion.label('Fruta'),
                                Pedido.cantidad.label('Cantidad'),
                                (Pedido.cantidad * Precio.valor).label('Total')
                                ).select_from(Pedido
                                    ).join(Fruta
                                        ).join(Peso
                                            ).join(Precio
                                                ).all()
                                        
        
    else:    
        rs = db.session.query(Pedido.id_pedido.label('id_pedido'),
                                Pedido.fecha_registro.label('fecha_venta'),
                                Fruta.descripcion.label('Fruta'),
                                Pedido.cantidad.label('Cantidad')
                                ).select_from(Pedido
                                    ).join(Fruta
                                        ).filter(Fruta.descripcion == data.get("descripcion")).all()
        

    #select fecha, id from pedido inner join 
    #Fruta on Fruta.id == Pedido.id_fruta where fruta.descripcion = 'Mora'
    return [row._asdict() for row in rs]




    