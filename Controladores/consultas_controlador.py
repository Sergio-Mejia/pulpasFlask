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
                                                ).order_by(desc(Pedido.fecha_registro)).all()
                                        
        
    else:    
        rs = db.session.query(Pedido.id_pedido.label('id_pedido'),
                                Pedido.fecha_registro.label('fecha_venta'),
                                Fruta.descripcion.label('Fruta'),
                                Pedido.cantidad.label('Cantidad'),
                                (Pedido.cantidad * Precio.valor).label('Total')
                                ).select_from(Pedido
                                    ).join(Fruta
                                        ).join(Peso
                                            ).join(Precio
                                                ).filter(Fruta.descripcion == data.get("descripcion")
                                                    ).order_by(desc(Pedido.fecha_registro)).all()
        
    #select fecha, id from pedido inner join 
    #Fruta on Fruta.id == Pedido.id_fruta where fruta.descripcion = 'Mora' order by fecha_registro
    return [row._asdict() for row in rs]


def get_suma_total(data:dict) -> dict:
    if data.get("descripcion") is None:
        rs = db.session.query(func.sum(Pedido.cantidad * Precio.valor).label('Total')
            ).select_from(Pedido
                ).join(Peso
                    ).join(Precio
                        ).all()
    else:
         rs = db.session.query(func.sum(Pedido.cantidad * Precio.valor).label('Total')
                ).select_from(Pedido
                    ).join(Fruta
                        ).join(Peso
                            ).join(Precio
                                ).filter(Fruta.descripcion == data.get("descripcion")
                                    ).all()
    
    return [row._asdict() for row in rs]


