from flask_socketio import SocketIO , join_room 
from flask import request
socketio = SocketIO()

@socketio.on("connect")
def handle_connect():
    session_id = request.sid
    print(f"Client connected with session ID: {session_id}")
    
@socketio.on("user_join")
def handle_userjoin(payload):
    print(f"User {payload['username']} joined!")
    join_room({payload['roomID']})
    
    
@socketio.on("create_room")
def handle_room(data):
    join_room(data['roomID'])
    print(f"User {data['username']} created a room : {data['roomID']}")
