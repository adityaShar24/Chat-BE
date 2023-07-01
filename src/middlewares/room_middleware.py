from flask import request , make_response
from models.room_model import Room
import json


def create_room_middleware():
    if request.endpoint == 'room_bp.create_room_wrapper':
        body = json.loads(request.data)
        roomname = body['roomname']
        userID = body['userID']
        if not roomname:
            return make_response({'message':'roomname field cannot be empty'} , 400)
        if not userID:
            return make_response({'message':'userID field cannot be empty'} , 400)
        existing_room = Room.find_by_name(roomname= roomname)
        if existing_room:
            return make_response({'message':f"roomname {roomname} already exists please enter a unique roomname"} , 400)
    
    
    
def add_member_middleware():
    if request.endpoint == 'add_member_wrapper':
        body = json.loads(request.data)
        roomID = body['roomname']
        userID = body['userID']
        if not roomID:
            return make_response({'message':'roomID field cannot be empty'} , 400)
        
        if not userID:
            return make_response({'message':'userID field cannot be empty'} , 400)
        
        existing_room = Room.find_by_id(roomID)
        if not existing_room:
            return make_response({'message': f"Room with ID {roomID} does not exist please check and enter again"} , 404)
    

    