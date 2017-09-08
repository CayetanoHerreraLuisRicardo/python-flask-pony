from app import orm
from app.models.user import User
import base64
import dicttoxml
from flask import Response,request
from flask_api import status
from flask_restful import Resource
import json
from lxml import objectify
from xml.etree import ElementTree as ET
import xmltodict
import os
from app.models.xml_models import XMLMODELS
from app.libs.general_functions import GENERALFUNCTIONS
from flask_jwt import jwt_required

class Auth:
    'Consultar usuario'
    @staticmethod
    def get_user(user):
        try:
            with orm.db_session:
                u = User.get(email=user)
                return u
        except Exception:
            return None

class UserAuth(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    def __str__(self):
        return "User(id='%s')" % self.id

class Users(Resource):
    'Obtener la lista de todos los usuarios'
    @jwt_required()
    def get(self):
        with orm.db_session:
            users = User.select()
            if users:
                result = {"success": True, "data": GENERALFUNCTIONS.parse_array([item.to_dict() for item in users])}
            else:
                result = {"success": False, "message": "sin registros"}

        if request.headers['Content-Type'] == 'application/xml':
            if 'data' in result:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_200_OK)
            else:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            if 'data' in result:
                return result, status.HTTP_200_OK
            else:
                return result, status.HTTP_202_ACCEPTED

    'Crear un usuario nuevo'
    def post(self):
        if request.headers['Content-Type'] == 'application/xml':
#            CON ESTO CHECAMOS SI EL XML ESTA BIEN FORMADO, SI SI LO GUARDAMOS EN FORMATO JSON
            try:
                ET.fromstring(request.data)
                info = json.dumps(xmltodict.parse(request.data))
                info = json.loads(info)
            except Exception:
                return Response(dicttoxml.dicttoxml({"success": False, "message": "XML mal construido"}), mimetype='application/xml', status=status.HTTP_200_OK)
#            CON ESTO CHECAMOS QUE EL XML COINCIDA CON LOS TIPOS DE DATOS DEFINIDO EN LA MODELO DE LA class XMLAPI.py ==> def parse_xml()
            try:
                objectify.fromstring(request.data, XMLMODELS.parse_xml())
            except Exception as e:
                return Response(dicttoxml.dicttoxml({"success": False, "message": str(e)}), mimetype='application/xml', status=status.HTTP_200_OK)

        elif request.headers['Content-Type'] == 'application/json':
            print(request.data)
            try:
                info = json.loads(request.data)
            except Exception:
                return {"success": False, "message": "Json mal construido"}, status.HTTP_202_ACCEPTED

#       AUNQUE SEA XML EL FORMATO ORIGINAL, SE USARÁ EL FORMATO JSON(MAS FACIL DE MANIPULAR Y AHORRAR LINEAS DE CÓDIGO) Y CON 'dicttoxml' LO CONVERTIMOS EN XML
        parse = info['data']
        result = {"success": True, "message": "successful operation"}
        if parse.get('image') is not None:
            try:
                imgdata = base64.b64decode(parse['image'])
            except Exception as e:
                result =  {"success": False, "message": "formato de imagen en base64 incorrecta"}
            file = parse['name'] + ".png"
            saveImg = GENERALFUNCTIONS.save_resize_image(file, imgdata)
            result = saveImg
        else:
            file = "default.png"
        
        if result.get('success') is True:
            try:
                with orm.db_session:
                    User(
                        name=parse['name'],
                        email=parse['email'],
                        position=parse['position'],
                        age=parse['age'],
                        image=file,
                        password=parse['password']
                    )
                result = {"success": True, "message": "successful operation"}
            except Exception as e:
                result = {"success": False, "message": str(e)}

        if request.headers['Content-Type'] == 'application/xml':
            if result.get('success') is True:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_200_OK)
            else:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            if result.get('success') is True:
                return result, status.HTTP_200_OK
            else:
                return result, status.HTTP_202_ACCEPTED

class UserItem(Resource):
    'Optener los datos de un usuario por id'
    @jwt_required()
    def get(self, id):
        with orm.db_session:
            # user = User[id] #ObjectNotFound exception if object with such primary key doesnâ€™t exist.
            user = User.get(id=int(id)) #If no object is found, get() returns None.
            if user:
                result = {"success": True, "data":user.to_dict()}
            else:
                result = {"success": False, "message": "Resource not found"}

        if request.headers['Content-Type'] == 'application/xml':
            if 'data' in result:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_200_OK)
            else:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            if 'data' in result:
                return result, status.HTTP_200_OK
            else:
                return result, status.HTTP_202_ACCEPTED

    'Editar un usuario por id '
    @jwt_required()
    def put(self, id):
        if request.headers['Content-Type'] == 'application/xml':
#            CON ESTO CHECAMOS SI EL XML ESTA BIEN FORMADO, SI SI LO GUARDAMOS EN FORMATO JSON
            try:
                ET.fromstring(request.data)
                info = json.dumps(xmltodict.parse(request.data))
                info = json.loads(info)
            except Exception:
                return Response(dicttoxml.dicttoxml({"success": False, "message": "XML mal construido"}), mimetype='application/xml', status=status.HTTP_200_OK)
#            CON ESTO CHECAMOS QUE EL XML COINCIDA CON LOS TIPOS DE DATOS DEFINIDO EN LA MODELO DE LA class XMLAPI.py ==> def parse_xml()
            try:
                objectify.fromstring(request.data, XMLMODELS.parse_xml())
            except Exception as e:
                return Response(dicttoxml.dicttoxml({"success": False, "message": str(e)}), mimetype='application/xml', status=status.HTTP_200_OK)

        elif request.headers['Content-Type'] == 'application/json':
            try:
                info = json.loads(request.data)
            except Exception:
                return {"success": False, "message": "Json mal construido"}, status.HTTP_202_ACCEPTED

        result = {"success": True}
        with orm.db_session:
            # user = User[id] #ObjectNotFound exception if object with such primary key doesn't exist.
            user = User.get(id=int(id)) #If no object is found, get() returns None.
            if user:
                parse = info['data']
                modImage = False
                if parse.get('image') is not None:
                    try:
                        imgdata = base64.b64decode(parse['image'])
                        print("************ + *****************")
                    except Exception as e:
                        result = {"success": False, "message": "formato de imagen en base64 incorrecta"}

                    if result.get('success') is True:
                        file = parse['name'] + ".png"
                        saveImg = GENERALFUNCTIONS.save_resize_image(file, imgdata)
                        result = saveImg
                        if saveImg.get('success') is True:
                            modImage = True
                        if parse['name'] != user.name and user.image != "default.png":
                            os.remove(os.getcwd() + "\\app\\images\\" + user.name + ".png")
                else:
                    file = "default.png"
                    modImage = True
                    os.remove(os.getcwd() + "\\app\\images\\" + user.name + ".png")

                try:
                    with orm.db_session:
                        user = User[int(id)]
                        if modImage:
                            fileMod = file
                        else:
                            fileMod = user.image

                        user.set(
                                name=parse['name'],
                                email=parse['email'],
                                position=parse['position'],
                                age=parse['age'],
                                image=fileMod
                        )
                        result = {"success": True, "message": "successful operation"}
                except Exception as e:
                    result = {"success": False, "message": str(e)}
            else:
                result = {"status":False, "message":"Resource not found"}
        if request.headers['Content-Type'] == 'application/xml':
            if result.get('success') is True:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_200_OK)
            else:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            if result.get('success') is True:
                return result, status.HTTP_200_OK
            else:
                return result, status.HTTP_202_ACCEPTED

    'Eliminar un usuario por id'
    @jwt_required()
    def delete(self, id):
        try:
            with orm.db_session:
                user = User.get(id=int(id))
                if user:
                    User[int(id)].delete()
                    if user.image != "default.png":
                        os.remove(os.getcwd()+"\\app\\images\\"+user.image)
                else:
                    result = {"status":False, "message":"Resource not found"}
                result = {"success": True, "message": "successful operation"}
        except Exception as e:
            result = {"success": False, "message": str(e)}, status.HTTP_202_ACCEPTED
            
        if request.headers['Content-Type'] == 'application/xml':
            if result.get('success') is True:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_200_OK)
            else:
                return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            if result.get('success') is True:
                return result, status.HTTP_200_OK
            else:
                return result, status.HTTP_202_ACCEPTED