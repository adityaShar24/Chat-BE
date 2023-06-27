from flask import request , make_response
import json
from models.room_model import Room
import bson.json_util as json_util


def create_room():
    body = json.loads(request.data)
    roomname = body['roomname']
    userID = body['userID']
    rooms = Room(roomname= roomname , userID= userID)
    
    if not roomname and userID:
        return make_response({'message':'roomname and created_by cannot be empty'} , 400)
    
    existing_room = Room.find_by_name(roomname)
    
    if existing_room:
        return make_response({f"roomname {roomname} already exists please enter a unique roomname"} , 401)
    
    create_room_id = rooms.create_room()
    
    json_Version = json_util.dumps(create_room_id)
    
    return make_response({'message':"Room has been created successfully" , "Room":json_Version} , 201)

def get_All_rooms():
    rooms = Room.get_rooms()
    json_Version = json_util.dumps(rooms)
    return make_response({'message':"Here's the list of all rooms" , 'Rooms': json_Version} , 201)