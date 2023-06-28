from controllers.rooms_controller import create_room , get_All_rooms , join_room
from flask import Blueprint
from flask_jwt_extended import jwt_required

room_bp = Blueprint('room_bp' , __name__)

@room_bp.post('/create_room')
def create_room_wrapper():
    return create_room()

@room_bp.post('/join_room')
def join_room_wrapper():
    return join_room()
    
@room_bp.get('/all_rooms')
def get_All_rooms_wrapper():
    return get_All_rooms()