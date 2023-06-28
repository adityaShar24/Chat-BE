from controllers.users_controller import Register , Login , getAllUsers
from flask import Blueprint
from flask_jwt_extended import jwt_required
from middlewares.user_middleware import register_middleware , login_middleware

auth_bp = Blueprint('auth_bp' , __name__)


@auth_bp.before_request
def register_middleware_wrapper():
    return register_middleware()

@auth_bp.before_request
def login_middleware_wrapper():
    return login_middleware()

@auth_bp.post('/register')
def register_wrapper():
    return Register()

@auth_bp.post('/login')
def login_wrapper():
    return Login()

@auth_bp.get('/all_users')
@jwt_required()
def get_All_Users_wrapper():
    return getAllUsers()

