from flask import request , make_response
from models.users_model import User
import json

def register_middleware():
    if request.endpoint == 'auth_bp.register_wrapper':
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({'message':'username field cannot be empty'} , 400)
        
        if not password:
            return make_response({'message':'password field cannot be empty'} , 400)
        
        registered_user = User.find_by_username(username= username)
        if registered_user:
            return make_response({'message':f"username {username} already exist. Please enter unique username"} , 400)

def login_middleware():
    if request.endpoint == 'auth_bp.login_wrapper':
        body = json.loads(request.data)
        username = body['username']
        password = body['password']
        
        if not username:
            return make_response({'message':'username field cannot be empty'} , 400)
        
        if not password:
            return make_response({'message':'password field cannot be empty'} , 400)
        
        existing_user = User.find_by_username(username= username)
        
        if not existing_user:
            return make_response({'message':f"username {username} does not exists please check and enter again"} , 401)
    