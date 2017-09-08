from flask import Flask
from flask_restful import Api
from pony import orm
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
#valor aleatorio complejo cuando desee utilizar flask_jwt
app.config['SECRET_KEY'] = "b'_,\xa3\xce\xd2.\xa9\xfbVn\x0e\xbcl\xf8>\x01\xb1E\xa5\xaf|A#\xb7"
#La URL para la autenticación. El valor predeterminado es /auth
app.config['JWT_AUTH_URL_RULE'] = '/auth'
#que indica cuánto son válidos los tokens.
app.config['JWT_EXPIRATION_DELTA'] = timedelta(milliseconds=1440 * 31 * 60)
# Expone todos los recursos que coincidan con /api/* al CORS
# y permite cabeceras Content-Type, que es necesario para peticiones POST
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)
db = orm.Database()
#Conexión con la BD MySQL
db.bind('mysql', host='localhost', user='root', passwd='', db='test')
from app.models.user import User
orm.sql_debug(True)
db.generate_mapping(create_tables=True)
from app.routes import app