# taller06

### Problemática

* Crear un proceso de importación de datos. Desde la siguiente dirección web a una base de datos local. Usar sqlite como gestor de base de datos y además usar la librería SqlAlchemy para la creación de la entidad, guardar registros y consulta de información.

Considerandos:
* Analizar lo que se realiza en la carpeta ejmplo01
* Trabajar en la carpeta ejercicio-02
* La data está en la siguiente dirección: https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json

* Crear una entidad con los siguientes atributos:
	* Nombre de pais
	* Capital
	* Continente
	* Dial
	* Geoname ID
	* ITU
	* Lenguajes
	* Si es independiente

* Leer los datos en su entorno local
	* Usar la libreria requests: import requests; primero instalar la librería: pip install requests
	* Usar el método get: requests.get(dirección del archivo json en str)
	* Obtener los datos en json a través de .json():  

* Guardar los registros en la base de datos local.
* Realizar la siguientes consultas, usar archivos separados para cada consulta.:
	* Presentar todos los países del continente americano
	* Presentar los países de Asía, ordenados por el atributo Dial.
	* Presentar los lenguajes de cada país.
	* Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
	* Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

* Presentar capturas de pantalla de la base de datos en sqlite
* Agregar comentarios explicativos de las parte más importantes realizadas

### Importante
* Se sugiere realizar un script por cada tarea: crear entidad; guardar información y consultar información
