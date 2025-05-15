from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais

import json

import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

datos_json = archivo.json()

# No es necesario ingresar a docs, porque ya es una lista
# puedo iterar tranquilamente sobre sus elementos
for d in datos_json:
    try:
        # Creo un objeto pais con sus atributos
        p = Pais(
        	# En caso de no existir la clave o de no tener valor
        	# se agrega el valor Desconocido
            nombre_pais=d.get("CLDR display name"),
            capital=d.get("Capital"),
            continente=d.get("Continent"),
            dial=d.get("Dial"),
            # En caso de haber valor lo convierte a int, y si no lo hay envia un None
            geoname_id=int(d.get("Geoname ID", 0)) if d.get("Geoname ID") else None,
            itu=d.get("ITU"),
            lenguajes=d.get("Languages"),
            independiente=d.get("is_independent")
        )

        session.add(p)
    except Exception as e:
        print(f"Error al procesar: {d}")
        print(e)

# Guardar los cambios
session.commit()