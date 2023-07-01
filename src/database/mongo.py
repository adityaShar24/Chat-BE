from pymongo import MongoClient
MONGO_CONNECTION_STRING = "mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(MONGO_CONNECTION_STRING)

Database = mongo_client['CHAT-BE']
Users_Collection = Database['Users']
Rooms_Collection = Database['Rooms']
Messages_Collection = Database['Message']

try:
    mongo_client.server_info()
    print("Connection to MongoDb Successful!")
except Exception as e:
    print("Failed to Connect" , e)
