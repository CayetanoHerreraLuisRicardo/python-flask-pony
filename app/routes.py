from app import api
from app import app
from app.views.v1.users import UserItem,Users
from flask import jsonify
from flask_api import status

@app.route("/")
def index():
    return "EJEMPLO DE UNA API REST FULL CON PYTHON+FLASK+PONY (table 'user' methods==> get, post, patch, delete)"

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"success": False, "message": "Resource not found"}), status.HTTP_404_NOT_FOUND

api.add_resource(Users, '/api/users')
api.add_resource(UserItem,'/api/users/<int:id>')