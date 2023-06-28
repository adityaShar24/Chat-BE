from controllers.users_controller import Register , Login , getAllUsers
from flask import Blueprint
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth_bp' , __name__)



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

