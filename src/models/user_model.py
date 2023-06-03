from database.mongo import Users_collection

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
    
    def save_user(self):
        user_id = Users_collection.insert_one({"username":self.username , 'password':self.password}).inserted_id
        return user_id
    
    @classmethod
    def find_by_username(cls, username):
        existing_user = Users_collection.find_one({'username': username})
        return existing_user
    
    def get_all_users(self):
        users = Users_collection.find()
        users_list = list(users)
        return users_list
    
    def delete_user(self):
        deleted_user = Users_collection.delete_one({"username":self.username , 'password':self.password})
        return deleted_user
        