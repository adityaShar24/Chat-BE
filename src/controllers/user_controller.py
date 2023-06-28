from flask import request , make_response
from models.users_model import User
import json
import bson.json_util as json_util
from flask_jwt_extended import create_access_token

def Register():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username = username , password = password)
    saved_user = users.save_users()
    json_version = json_util.dumps(saved_user)
    
    return make_response({"message": "User has been registered successfully", "user": json_version}, 201)

def Login():
    body = json.loads(request.data)
    username = body['username']
    password = body['password']
    users = User(username=username, password=password)
    access_token = create_access_token(identity= username)
    return make_response({"access_token": access_token} , 201)
        
def getAllUsers():
    users = User.get_Users()
    json_Version = json_util.dumps(users)
    return make_response(json_Version , 201)