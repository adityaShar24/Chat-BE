from flask import request , make_response
from models.message_model import Message
import bson.json_util as json_util
import json

def send_message():
    body = json.loads(request.data)
    userID = body['userID']
    roomId = body['roomID']
    content = body['content']
    message = Message(userID=userID , roomID= roomId , content= content)
    saved_message = message.save_message()
    json_Version = json_util.dumps(saved_message)
    return make_response({'message':'message has been sent successfully' , 'Message': json_Version} , 201)


def delete_message():
    body = json.loads(request.data)
    userID = body['userID']
    roomId = body['roomID']
    content = body['content']
    message = Message(userID=userID , roomID= roomId , content= content)
    print(message)
    delete_msg = message.delete_message()
    return make_response({'message':'Message has been deleted successfully'} , 201)