from database.mongo import Messages_Collection
from bson.objectid import ObjectId
from datetime import datetime

class Message:
    def __init__(self , roomID , userID  , content):
        self.roomId = ObjectId(roomID)
        self.sender = ObjectId(userID)
        self.receiver = ObjectId(userID)
        self.content = content
        self.datetime = datetime.utcnow()
        
    def save_message(self):
        message_id = Messages_Collection.insert_one({'roomID':self.roomId , 'sender': self.sender , 'receiver': self.receiver , 'content': self.content , 'datetime': self.datetime }).inserted_id
        return message_id 
    
    