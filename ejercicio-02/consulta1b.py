from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

stmt = select(Pais).where(Pais.continente.in_(['NA', 'SA']))
resultado = session.execute(stmt)

print("=== Países del continente americano ===")
for fila in resultado:
    pais = fila[0]
    print(f"País: {pais.nombre} | Continente: {pais.continente}")
