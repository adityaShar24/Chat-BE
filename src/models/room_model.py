from database.mongo import Rooms_Collection
from bson.objectid import ObjectId

class Room:
    def __init__(self , roomname , userID):
        self.roomname = roomname
        self.userID = ObjectId(userID)
        self.members = []

        
    def find_by_name(roomname):
        existing_room = Rooms_Collection.find_one({"roomname": roomname})
        return existing_room
        
    def create_room(self) :
        room_id = Rooms_Collection.insert_one({'roomname': self.roomname , 'userID': self.userID}).inserted_id
        return room_id
        
    def delete_room(roomname):
        room_id = Rooms_Collection.find_one_and_delete({'roomname': roomname })
        return room_id
    
    def get_rooms():
        rooms = Rooms_Collection.find()
        rooms_list = list(rooms)
        return rooms_list
    
    def add_members(self , userID):
        member_id = self.members.append(userID)
        return member_id