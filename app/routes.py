from app import api
from app import app
from app.views.v2.users import UserItem,Users,Auth,UserAuth
from flask import jsonify
from flask_api import status
from flask_jwt import JWT
from app.models.user import User

def authenticate(username, password):
    if not (username and password):
        return False

    u = Auth.get_user(username)
    if u:
        if username == u.email and password == u.password:
            return UserAuth(id=u.id,username=u.email,password=u.password)

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

jwt = JWT(app, authenticate, identity)

@app.route("/")
def index():
    return "EJEMPLO DE UNA API REST FULL CON PYTHON+FLASK+PONY (table 'user' methods==> get, post, patch, delete)"

@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "message": "The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again."}), status.HTTP_404_NOT_FOUND

@app.errorhandler(405)
def not_allowed(error):
    return jsonify({"success": False, "message": "The method is not allowed for the requested URL."}), status.HTTP_405_METHOD_NOT_ALLOWED

api.add_resource(Users, '/api/users')
api.add_resource(UserItem,'/api/users/<int:id>')