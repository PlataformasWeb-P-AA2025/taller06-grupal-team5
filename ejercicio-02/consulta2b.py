from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

stmt = select(Pais).where(Pais.continente == 'AS').order_by(Pais.dial)
resultado = session.execute(stmt)

print("=== Países de Asia ordenados por código de marcación ===")
for fila in resultado:
    pais = fila[0]
    print(f"{pais.nombre} ➜ Dial: {pais.dial}")
