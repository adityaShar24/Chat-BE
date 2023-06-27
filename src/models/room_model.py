from database.mongo import Rooms_Collection
from datetime import datetime
import bson
from bson.objectid import ObjectId

class Room:
    def __init__(self , roomname , userID , num_member):
        self.roomname = roomname
        self.userID = ObjectId(userID)
        self.num_member = bson.Int64(num_member)
        
    def find_by_name(roomname):
        existing_room = Rooms_Collection.find_one({"roomname": roomname})
        return existing_room
        
    def create_room(self) :
        room_id = Rooms_Collection.insert_one({'userID':self.userID , 'roomname': self.roomname , 'created_by': self.userID , 'created_at': datetime.utcnow() , "no_members": self.num_member})
        return room_id
        
    