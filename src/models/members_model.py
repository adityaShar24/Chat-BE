from database.mongo import Rooms_Collection , Members_collection
from datetime import datetime
from bson.objectid import ObjectId

class Members:
    def __init__(self , userID , roomID):
        self.userID = ObjectId(userID)
        self.roomID = ObjectId(roomID)

    def add_member(self):
        rooms = Rooms_Collection.find_one({'_id':self.roomID})
        members_id = Members_collection.insert_one({'roomname':self.roomID , 'username':self.userID , 'added_at': datetime.utcnow()})
        Rooms_Collection.find_one_and_update({"_id":self.roomID} , {'$inc':{'no_members': 1}})
        return members_id
