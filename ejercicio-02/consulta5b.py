from sqlalchemy import create_engine, select, or_
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

stmt = select(Pais).where(
    or_(
        Pais.nombre.like('%uador%'),
        Pais.capital.like('%ito%')
    )
)
resultado = session.execute(stmt)

print("=== Países que contienen 'uador' o capitales que contienen 'ito' ===")
for fila in resultado:
    pais = fila[0]
    print(f"[{pais.nombre}] tiene capital '{pais.capital}'")
