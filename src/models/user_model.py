from database.mongo import Users_collection

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password

    def save_user(self):
        user_id = Users_collection.insert_one({ 'username':self.username , 'password':self.password }).inserted_id
        return user_id