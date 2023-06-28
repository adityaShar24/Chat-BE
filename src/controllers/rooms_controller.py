from flask import request , make_response
import json
from models.room_model import Room
import bson.json_util as json_util


def create_room():
    body = json.loads(request.data)
    roomname = body['roomname']
    userID = body['userID']
    rooms = Room(roomname= roomname , userID= userID)
    create_room_id = rooms.create_room()
    
    json_Version = json_util.dumps(create_room_id)
    
    return make_response({'message':"Room has been created successfully" , "Room":json_Version} , 201)

def join_room():
    body = json.loads(request.data)
    roomID = body['roomID']
    userID = body['userID']
    member_id = Room.add_members(roomID , userID)
    json_Version = json_util.dumps(member_id)
    
    return make_response({'message': f"Member has been added to room {roomID} successfully" , "Member": json_Version} , 201)
    

def get_All_rooms():
    rooms = Room.get_rooms()
    json_Version = json_util.dumps(rooms)
    return make_response({'message':"Here's the list of all rooms" , 'Rooms': json_Version} , 201)