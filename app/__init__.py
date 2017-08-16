from flask import Flask
from flask_restful import Api
from pony import orm
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)
db = orm.Database()
db.bind('mysql', host='localhost', user='root', passwd='', db='test')
from app.models.user import User
orm.sql_debug(True)
db.generate_mapping(create_tables=True)


from app.routes import app
