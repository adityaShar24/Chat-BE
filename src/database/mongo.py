from pymongo import MongoClient
CONNECTION_STRING = "mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(CONNECTION_STRING)

database = mongo_client['Chat']
Users_collection = database['users']
chat_collection = database['chat']

try:
    mongo_client.server_info() 
    print("Connection to MongoDB successful!")
except Exception as e:
    print("Connection to MongoDB failed:", e)