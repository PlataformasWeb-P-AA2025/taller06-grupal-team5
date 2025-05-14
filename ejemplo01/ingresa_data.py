from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Persona

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepersonas.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = open("data/data-personas-001.json", "r")
# archivo = request.get("------------------.json")

datos_json =  json.load(archivo) # paso los datos del archivo a json
# archivo.json()
documentos = datos_json["docs"]

for d in documentos:
    print(d)
    print(len(d.keys()))
    p = Persona(nombre=d['nombre'], apellido=d['apellido'], pais=d['pais'], \
            email=d['email'])
    session.add(p)

# confirmar transacciones

session.commit()
