from database.mongo import Messages_Collection
from bson.objectid import ObjectId

class Message:
    def __init__(self , roomID , userID  , content):
        self.roomID = ObjectId(roomID)
        self.userID = ObjectId(userID)
        self.content = content
        
    def save_message(self):
        message_id = Messages_Collection.insert_one({'roomID':self.roomID , 'sender': self.userID , 'content': self.content }).inserted_id
        return message_id 
    
    def delete_message(self):
        message = Messages_Collection.find_one_and_delete({'roomID':self.roomID , 'sender': self.sender , 'content': self.content })
        return message
    
    def get_all_messages(roomID):
        messages = Messages_Collection.find({"roomID":ObjectId(roomID)})
        list_msgs = list(messages)
        return list_msgs
    