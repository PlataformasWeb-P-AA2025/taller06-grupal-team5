from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepaises.db')
Session = sessionmaker(bind=engine)
session = Session()

stmt = select(Pais)
resultado = session.execute(stmt)

print("=== Lenguajes oficiales por país ===")
for fila in resultado:
    pais = fila[0]
    print(f"{pais.nombre}: lenguas = {pais.lenguajes}")
