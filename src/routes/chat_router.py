from flask import Blueprint
from middlewares.message_middleware import message_middleware
from controllers.chat_controller import send_message , delete_message

chat_bp = Blueprint('chat_bp' , __name__)


@chat_bp.post('/send_message')
def send_message_wrapper():
    return send_message()

@chat_bp.post('/delete_message')
def delete_message_wrapper():
    return delete_message()