from flask import request , make_response
import json


def message_middleware():
    if request.endpoint == 'chat_bp.send_message_wrapper':
        body = json.loads(request.data)
        userID = body['userID']
        roomId = body['roomID']
        content = body['content']
        
        if not userID:
            return make_response({'message':'userID field cannot be empty'} , 400)
        
        if not roomId:
            return make_response({'message':'roomID field cannot be empty'} , 400)
        
        if not content:
            return make_response({'message':"content field cnaoot be empty"} , 400)
    
