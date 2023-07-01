from flask import Blueprint
from controllers.message_controller import send_message , delete_message , get_all_messages
from flask_jwt_extended import jwt_required

message_bp = Blueprint('message_bp' , __name__)


@message_bp.post('/send_message')
def send_message_wrapper():
    return send_message()

@message_bp.post('/delete_message')
def delete_message_wrapper():
    return delete_message()

@message_bp.get('/all_messages')
@jwt_required()
def get_all_messages_wrapper():
    return get_all_messages()
    