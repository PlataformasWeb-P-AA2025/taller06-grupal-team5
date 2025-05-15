from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

stmt = select(Pais).where(Pais.continente == 'EU').order_by(Pais.capital)
resultado = session.execute(stmt)

print("=== Países europeos ordenados por su capital ===")
for fila in resultado:
    pais = fila[0]
    print(f"Capital: {pais.capital} → País: {pais.nombre}")
