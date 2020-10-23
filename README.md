EJEMPLO DE API REST EN PYTHON
=================
ESTE ES UN PEQUEÑO EJEMPLO DE UNA API REST EN PYTHON, PUEDE SERVIR DE BASE PARA LOS QUE APENAS SE VAN ABRIENDO AL MUNDO DE PYTHON.

PARA ESTE PROYECTO SE UTILIZÓ *`FLASK`* COMO FRAMEWORK PARA DISEÑO DE LA API. 

CABE SEÑALAR QUE PARA HACER ESTA API SE TOMÓ COMO BASE ESTE REPOSITORIO https://github.com/andriisoroka/user-flask-restapi-pony-orm DEL AMIGO @andriisoroka 

ESTA API REST SE TRABAJO CON 
Content-Type: 	
- application/json
- application/xml

TAMBIEN SE IMPLEMENTÓ LA AUTENTICACIÓN CON *`JWT`*, LA QUE NOS OFRECE *`FLASK`* ES EL PAQUETE *`Flask-JWT`*


ESTO TANTO EN EL *`RESQUEST`* COMO EN EL *`RESPONSE`*.
##### INSTALAR
- PYTHON 3.x (VERSION USADO 3.6.0) 
[![](https://www.python.org/static/favicon.ico)](https://www.python.org/downloads/)
- MYSQL
[![N|Solid](https://labs.mysql.com/common/themes/sakila/favicon.ico)](https://www.mysql.com/downloads/)

##### CLONAR REPOSITORIO

```sh
    $ git clone https://github.com/CayetanoHerreraLuisRicardo/python-flask-pony.git
```

##### INSTALAR PAQUETES DE PYTHON
- ENTRAR AL SHELL DE TU S.O.
- UBICARSE EN LA RAIZ DEL REPOSITORIO, AHÍ ESTÁ UN  ARCHIVO *`requirements.txt`*  ESTE TIENE UNA LISTA DE PAQUETES QUE SE INSTALARON EN EL PROYECTO. UTILIZAREMOS *`pip`* (INSTALADOR DE PAQUETES).
- EJECUTAR:
```sh
    $ pip install -r requirements.txt 
```
##### BASE DE DATOS
- ENTRAR AL SHELL DE TU S.O.
- UBICARSE EN LA RAIZ DEL REPOSITORIO HAY UN  ARCHIVO *`db.sql`* (backup de las base de datos)
- EJECUTAR:
```sh
    $ mysql -u <user> -p <mydatabase> < db.sql
```

##### CORRER PROYECTO
PARA ESTE PUNTO YA CONTAMOS CON LO NECESARIO PARA ECHAR A ANDAR LA APP
```sh
    $ python run.py
```

##### DOCUMENTACIÓN DE LA API
SERVICIOS:

| MÉTODO | URI | DESCRIPCIÓN |
| ------ | ------ | ------ |
| **`POST`** | http://127.0.0.1:5000/auth | *ATENTICACIÓN CON LA API*|
| **`GET`** | http://127.0.0.1:5000/api/users | *TODOS LOS USUARIOS* |
| **`GET`** | http://127.0.0.1:5000/api/users/`{id}` | *UN USUARIO POR ID* |
| **`POST`** | http://127.0.0.1:5000/api/users | *CREAR UN USUARIO* |
| **`PUT`** | http://127.0.0.1:5000/api/users/`{id}` | *MODIFICAR USUARIO POR ID* |
| **`DELETE`** | http://127.0.0.1:5000/api/users/`{id}` | *ELIMINAR USUARIO POR ID* |

##### **`POST`** http://127.0.0.1:5000/auth
**REQUEST:**
```
HEADERS:
	Content-Type: 	application/json
BODY:
	IN JSON:
		{	
			"username":"4444@4444.com",
			"password":"123456"
		}
```
**RESPONSE:**
```
IN JSON:
	{
		"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDQ3MjQ3ODAsImlhdCI6MTUwNDcyMjEwMSwibmJmIjoxNTA0NzIyMTAxLCJpZGVudGl0eSI6NH0.bi2ILzwnllCFFZaInn2pDTpWgCc0lDT_25pIBDDaxl4"
	}
```
##### **`GET`** http://127.0.0.1:5000/api/users
**REQUEST:**
```
HEADERS:
    Content-Type: 	application/xml
	                application/json
    Authorization:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDQ3MjQwOTAsImlhdCI6MTUwNDcyMTQxMiwibmJmIjoxNTA0NzIxNDEyLCJpZGVudGl0eSI6NH0.5fX-AUkPVX9hlq0MxYJe8BwfzC4nMLiHHwJbPug2RD8
```

**RESPONSE:**
```
		IN XML:
			<?xml version="1.0" encoding="UTF-8" ?>
			<root>
				<success type="bool">True</success>
				<data type="list">
					<item type="dict">
						<id type="int">4</id>
						<name type="str">44444</name>
						<email type="str">4444@4444.com</email>
						<position type="str">4444</position>
						<age type="int">43</age>
						<image type="str">44444.png</image>
					 </item>
					<item type="dict">
						<id type="int">7</id>
						<name type="str">5555</name>
						<email type="str">555@555.com</email>
						<position type="str">4455544</position>
						<age type="int">23</age>
						<image type="str">5555.png</image>
					 </item>
					<item type="dict">
						<id type="int">8</id>
						<name type="str">asssss</name>
						<email type="str">assss@fdfds.com</email>
						<position type="str">asss</position>
						<age type="int">43</age>
						<image type="str">default.png</image>
					 </item>
					<item type="dict">
						<id type="int">9</id>
						<name type="str">xml1</name>
						<email type="str">xml1@xml1.COM</email>
						<position type="str">xml1</position>
						<age type="int">20</age>
						<image type="str">default.png</image>
					 </item>
					<item type="dict">
						<id type="int">10</id>
						<name type="str">xml3</name>
						<email type="str">xml3@xml3.COM</email>
						<position type="str">xml3</position>
						<age type="int">22</age>
						<image type="str">default.png</image>
					 </item>
					<item type="dict">
						<id type="int">11</id>
						<name type="str">xml3</name>
						<email type="str">xml3@xml3.COM</email>
						<position type="str">xml3</position>
						<age type="int">22</age>
						<image type="str">xml3.png</image>
					 </item>
				 </data>
			 </root>

		IN JSON:
			{
				"data": [
					{
						"age": 43,
						"email": "4444@4444.com",
						"id": 4,
						"image": "44444.png",
						"name": "44444",
						"position": "4444"
					},
					{
						"age": 23,
						"email": "555@555.com",
						"id": 7,
						"image": "5555.png",
						"name": "5555",
						"position": "4455544"
					},
					{
						"age": 43,
						"email": "assss@fdfds.com",
						"id": 8,
						"image": "default.png",
						"name": "asssss",
						"position": "asss"
					},
					{
						"age": 20,
						"email": "xml1@xml1.COM",
						"id": 9,
						"image": "default.png",
						"name": "xml1",
						"position": "xml1"
					},
					{
						"age": 22,
						"email": "xml3@xml3.COM",
						"id": 10,
						"image": "default.png",
						"name": "xml3",
						"position": "xml3"
					},
					{
						"age": 22,
						"email": "xml3@xml3.COM",
						"id": 11,
						"image": "xml3.png",
						"name": "xml3",
						"position": "xml3"
					}
				],
				"success": true
			}
```
##### **`GET`** http://127.0.0.1:5000/api/users/`{id}`
**REQUEST:**
```
HEADERS:
    Content-Type: 	application/xml
	                application/json
    Authorization:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDQ3MjQwOTAsImlhdCI6MTUwNDcyMTQxMiwibmJmIjoxNTA0NzIxNDEyLCJpZGVudGl0eSI6NH0.5fX-AUkPVX9hlq0MxYJe8BwfzC4nMLiHHwJbPug2RD8
```
**RESPONSE:**
```
		IN XML
			<?xml version="1.0" encoding="UTF-8" ?>
			<root>
				<success type="bool">True</success>
				<data type="dict">
					<id type="int">4</id>
					<name type="str">44444</name>
					<email type="str">4444@4444.com</email>
					<position type="str">4444</position>
					<age type="int">43</age>
					<image type="str">44444.png</image>
				</data>
			</root>

		IN JSON
			{
				"success": true,
				"data": {
					"id": 41,
					"name": "2-22-22",
					"email": "2-22-2@PRUEBA4346563.COM",
					"position": "DEL",
					"age": 27,
					"image": "default.png",
					"password": "123456Aa"
				}
			}
```

##### **`POST`** http://127.0.0.1:5000/api/users
**REQUEST:**
*(PARA ESTE CASO NO SE REQUIERE ENVIAR EL TOKEN PARA `Authorization` PUES ES PARA CREAR UN USUARIO)*
```
		HEADERS:
			Content-Type: 	application/xml
							application/json
		BODY:
			IN XML:
				WITH IMAGEN BASE 64:
					<data>
						<name>PRUEBA4346563</name>
						<email>PRUEBA4346563@PRUEBA4346563.COM</email>
						<position>PRUEBA4346563</position>
						<age>27</age>
						<image>iVBORw0KGgoAAAANSUhEUgA ... AAASUVORK5CYII=</image>
						<password>123456Aa</password>
					</data>
				WITHOUT IMAGEN BASE 64:
					<data>
						<name>PRUEBA4346563</name>
						<email>PRUEBA4346563@PRUEBA4346563.COM</email>
						<position>PRUEBA4346563</position>
						<age>27</age>
						<image></image>
		              	<password>123456Aa</password>
					</data>
			IN JSON:
				WITH IMAGEN BASE 64
					{
						"data":{
							"name":"EEEEE43434",
							"email": "EEEEE43434@EEEEE43434.com",
							"position":"EEEEE43434",
							"age": 43,
							"image": "iVBORw0KGgoAAAANSUhEUgA ... AAASUVORK5CYII=",
							"password":"123456As"
						}
					}
				WITHOUT IMAGEN BASE 64
					{
						"data":{
							"name":"EEEEE43434",
							"email": "EEEEE43434@EEEEE43434.com",
							"position":"EEEEE43434",
							"age": 43,
							"image": null,
							"password":"123456As"
						}
					}
```
**RESPONSE:**
```
		IN XML:
			<?xml version="1.0" encoding="UTF-8" ?>
			<root>
			<success type="bool">True</success>
			<message type="str">successful operation</message>
			 </root>
		IN JSON:
			{
				"message": "successful operation",
				"success": true
			}
```

##### **`PUT`** http://127.0.0.1:5000/api/users/`{id}`
**REQUEST:**
```
		HEADERS:
			Content-Type: 	application/xml
							application/json
			Authorization:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDQ3MjQwOTAsImlhdCI6MTUwNDcyMTQxMiwibmJmIjoxNTA0NzIxNDEyLCJpZGVudGl0eSI6NH0.5fX-AUkPVX9hlq0MxYJe8BwfzC4nMLiHHwJbPug2RD8
		BODY:
			IN XML:
				WITH IMAGEN BASE 64:
					<data>
						<name>PRUEBA4346563</name>
						<email>PRUEBA4346563@PRUEBA4346563.COM</email>
						<position>PRUEBA4346563</position>
						<age>27</age>
						<image>iVBORw0KGgoAAAANSUhEUgA ... AAASUVORK5CYII=</image>
						<password>123456Aa</password>
					</data>
				WITHOUT IMAGEN BASE 64:
					<data>
						<name>PRUEBA4346563</name>
						<email>PRUEBA4346563@PRUEBA4346563.COM</email>
						<position>PRUEBA4346563</position>
						<age>27</age>
						<image></image>
		              	<password>123456Aa</password>
					</data>
			IN JSON:
				WITH IMAGEN BASE 64
					{
						"data":{
							"name":"EEEEE43434",
							"email": "EEEEE43434@EEEEE43434.com",
							"position":"EEEEE43434",
							"age": 43,
							"image": "iVBORw0KGgoAAAANSUhEUgA ... AAASUVORK5CYII=",
							"password":"123456As"
						}
					}
				WITHOUT IMAGEN BASE 64
					{
						"data":{
							"name":"EEEEE43434",
							"email": "EEEEE43434@EEEEE43434.com",
							"position":"EEEEE43434",
							"age": 43,
							"image": null,
							"password":"123456As"
						}
					}
```
**RESPONSE:**
```
		IN XML:
			<?xml version="1.0" encoding="UTF-8" ?>
			<root>
			<success type="bool">True</success>
			<message type="str">successful operation</message>
			 </root>
		IN JSON:
			{
				"message": "successful operation",
				"success": true
			}
```
##### **`DELETE`** http://127.0.0.1:5000/api/users/`{id}`
**REQUEST:**
```
		HEADERS:
			Content-Type: 	application/xml
							application/json
			Authorization:	JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDQ3MjQwOTAsImlhdCI6MTUwNDcyMTQxMiwibmJmIjoxNTA0NzIxNDEyLCJpZGVudGl0eSI6NH0.5fX-AUkPVX9hlq0MxYJe8BwfzC4nMLiHHwJbPug2RD8
```
**RESPONSE:**
```
		IN XML:
			<?xml version="1.0" encoding="UTF-8" ?>
			<root>
			<success type="bool">True</success>
			<message type="str">successful operation</message>
			 </root>
		IN JSON:
			{
				"message": "successful operation",
				"success": true
			}
```
