from flask import request , make_response
from models.room_model import Room
import json
from routes.room_router import room_bp

@room_bp.before_request
def create_room_middleware():
    if request.endpoint == 'create_room_wrapper':
        body = json.loads()
        roomname = body['roomname']
        userID = body['userID']
        if not roomname:
            return make_response({'message':'roomname field cannot be empty'} , 400)
        if not userID:
            return make_response({'message':'userID field cannot be empty'} , 400)
        existing_room = Room.find_by_name(roomname= roomname)
        if existing_room:
            return make_response({'message':f"roomname {roomname} already exists please enter a unique roomname"} , 400)
    
    
    
@room_bp.before_request    
def join_room_middleware():
    if request.endpoint == 'join_room_wrapper':
        body = json.loads(request.data)
        roomname = body['roomname']
        userID = body['userID']
        
        if not roomname:
            return make_response({'message':'roomname field cannot be empty'} , 400)
        
        if not userID:
            return make_response({'message':'userID field cannot be empty'} , 400)
        
        existing_room = Room.find_by_name(roomname= roomname)
        if not existing_room:
            return make_response({'message':f"roomname {roomname} does not exists please check and enter again"} , 400)
    

    