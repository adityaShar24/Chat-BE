from controllers.user_contoller import register , login , get_All_Users
from flask import Blueprint
from flask_jwt_extended import jwt_required


auth_bp = Blueprint('auth_bp' , __name__)

@auth_bp.post('/register')
def register_wrapper():
    return register()

@auth_bp.post('/login')
@jwt_required()
def login_wrapper():
    return login()

@auth_bp.get('/all_users')
@jwt_required()
def get_All_Users_wrapper():
    return get_All_Users()