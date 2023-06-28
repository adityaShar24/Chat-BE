from models.user_model import User
from flask import request , make_response
from flask_jwt_extended import create_access_token
import json
import bson.json_util as json_util
import datetime

def register():
    body = json.loads(request.data)
    username = body["username"]
    password = body["password"]
    
    users = User(username= username , password= password)
    if not (users.password and users.username):
        return make_response({"message":"Username and password cannot be empty"} , 400)
    
    registered_user = User.find_by_username(username)
    
    if registered_user:
        return make_response(f"username {username} already exits please enter unique username" , 401)
    
    saved_user = users.save_user()
    json_Version = json_util.dumps(saved_user)
    return make_response({"message":"User has been registered succesfully" , 'user':json_Version} , 201)

def login():
    body = json.loads(request.data)
    username = body["username"]
    password = body['password']
    
    users = User(username= username , password= password)
    if not (users.password and users.username):
        return make_response({"message":"Username and password cannot be empty"} , 400)
    
    existing_user = User.find_by_username(username)
    if not existing_user:
        return make_response({"message":"Enter username correctly"} , 401)
    
    users_password = User.find_password(password)
    if not users_password:
        return make_response({"message":"Enter password correctly"} , 401)
    
    access_token = create_access_token(identity= username , fresh= datetime.timedelta(minutes= 30))
    return make_response({'access_token': access_token} , 201)

def get_All_Users():
    Users = User.get_all_users()
    return make_response(Users , 201)