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
class Users(Resource):
    'Obtener la lista de todos los usuarios'
    def get(self):
        # time.sleep(5)
        with orm.db_session:
            users = User.select()
            if users:
                result = {"success": True, "data":[item.to_dict() for item in users]}
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

#       AUNQUE SEA XML EL FORMATO ORIGINAL, SE USARÁ EL FORMATO JSON(MAS FACIL DE MANIPULAR Y AHORRAR LINEAS DE CÓDIGO)
        parse = info['data']
        if parse.get('image') is not None:
            if 'image' in parse:
                try:
                    imgdata = base64.b64decode(parse['image'])
                except Exception as e:
                    return {"success": False, "message": "formato de imagen en base64 incorrecta"}, status.HTTP_202_ACCEPTED
                file = parse['name'] + ".png"
                saveImg = GENERALFUNCTIONS.save_resize_image(file, imgdata)
                if saveImg.get('success') is False:
                    return saveImg, status.HTTP_202_ACCEPTED
        else:
            file = "default.png"
        try:
            with orm.db_session:
                User(
                    name=parse['name'],
                    email=parse['email'],
                    position=parse['position'],
                    age=parse['age'],
                    image=file
                )
            result = {"success": True, "message": "successful operation"}
        except Exception as e:
            result = {"success": False, "message": str(e)}

        if request.headers['Content-Type'] == 'application/xml':
            return Response(dicttoxml.dicttoxml(result), mimetype='application/xml', status=status.HTTP_202_ACCEPTED)
        elif request.headers['Content-Type'] == 'application/json':
            return result, status.HTTP_200_OK

class UserItem(Resource):
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
                objectify.fromstring(request.data, XMLAPI.parse_xml())
            except Exception as e:
                return Response(dicttoxml.dicttoxml({"success": False, "message": str(e)}), mimetype='application/xml', status=status.HTTP_200_OK)

        elif request.headers['Content-Type'] == 'application/json':
            try:
                info = json.loads(request.data)
            except Exception:
                return {"success": False, "message": "Json mal construido"}, status.HTTP_202_ACCEPTED
        try:
            print(info)
            with orm.db_session:
                # user = User[id] #ObjectNotFound exception if object with such primary key doesn't exist.
                user = User.get(id=int(id)) #If no object is found, get() returns None.
                if user:
                    parse = info['data']
                    modImage = False

                    if 'image' in parse:
                        try:
                            imgdata = base64.b64decode(parse['image'])
                        except Exception as e:
                            return {"success": False, "message": "formato de imagen en base64 incorrecta"}, status.HTTP_202_ACCEPTED
                        file = parse['name'] +".png"
                        saveImg = GENERALFUNCTIONS.save_resize_image(file,imgdata)
                        if saveImg.get('success') is False:
                            return saveImg, status.HTTP_202_ACCEPTED
                        else:
                            modImage = True
                        if parse['name'] != user.name and user.name != "default.png":
                            os.remove(os.getcwd()+"\\app\\images\\"+user.name+".png")
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
                            return {"success": True, "message": "successful operation"}, status.HTTP_200_OK
                    except Exception as e:
                        return {"success": False, "message": str(e)}, status.HTTP_202_ACCEPTED
                else:
                    return {"status":False, "message":"Resource not found"}, status.HTTP_202_ACCEPTED

        except Exception as e:
            return {"success": False, "message": str(e)}, status.HTTP_202_ACCEPTED

    'Eliminar un usuario por id'
    def delete(self, id):
        try:
            with orm.db_session:
                user = User.get(id=int(id))
                if user:
                    User[int(id)].delete()
                    if user.name != "default":
                        os.remove(os.getcwd()+"\\app\\images\\"+user.name+".png")
                else:
                    return {"status":False, "message":"Resource not found"}
                return {"success": True, "message": "successful operation"}, status.HTTP_200_OK
        except Exception as e:
            return {"success": False, "message": str(e)}, status.HTTP_202_ACCEPTED