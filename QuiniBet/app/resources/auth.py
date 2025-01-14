from flask import jsonify, request
from flask import Blueprint
from flask_jwt_extended import create_access_token
from app.services import UserService
from app.mapping import UserSchema
from app.validators import validate_with
from app.models import User
from app.services import auth_service

auth = Blueprint('auth', __name__)
user_schema = UserSchema()


@auth.route('/login', methods=["POST"])
@validate_with(User)
def login():

    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user_service = UserService()

    if auth_service.check_auth(email, password):
        user = user_service.find_by_username(email)
        list_roles = [role.name for role in user.roles] #lista por comprensión
        
        acces_token = create_access_token(user_schema.dmp(user), additional_claims={'roles': list_roles})
        return jsonify({'token':acces_token, 'id':user.id})

    return jsonify({'token':acces_token}), 401