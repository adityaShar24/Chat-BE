# Chat Application

A chat application built using Flask and Flask-SocketIO. This application allows users to register, login, create rooms, join existing rooms, send messages, and delete messages.

## Table of Contents

- Technologies Used
- Features
- Getting Started
- Usage
- API Endpoints
- Socket Events
- Contributing
- License

## Technologies Used

- **Flask**: A micro web framework for building web applications.
- **Flask-SocketIO**: A Flask extension that adds WebSocket support to Flask applications.
- **MongoDB**: A NoSQL document database used for storing user, room, and message data.
- **Flask-JWT-Extended**: A Flask extension that adds support for JSON Web Tokens (JWT) for user authentication.
- **SocketIO**: A library that enables real-time, bidirectional communication between web clients and servers.

# Features

- **User Registration**: Users can register an account by providing a username and password.
- **User Login**: Registered users can log in using their credentials and receive an access token.
- **Create Room**: Users can create a new chat room by providing a room name.
- **Join Room**: Users can join an existing chat room by providing the room ID.
- **Send Message**: Users can send messages in a chat room.
- **Delete Message**: Users can delete their own messages in a chat room.
- **Get All Messages**: Users can retrieve all messages in a specific chat room.
- **Get All Rooms**: Users can retrieve a list of all available chat rooms.

## Getting Started

1. Clone the repository:
bash
Copy code
git clone (https://github.com/adityaShar24/Chat-BE.git)
Install the dependencies:

2. bash
Copy code
pip install -r requirements.txt
Set up the MongoDB connection:

Modify the MONGO_CONNECTION_STRING variable in database/mongo.py with your MongoDB connection string.
Run the application:

3. bash
Copy code
python app.py
The application will be accessible at http://localhost:5000.

4. -**Usage**
Register a new user by making a POST request to /register with the following JSON payload:

json
Copy code
{
  "username": "your-username",
  "password": "your-password"
}
- Log in with your registered user credentials by making a POST request to /login with the following JSON payload:

json
Copy code
{
  "username": "your-username",
  "password": "your-password"
}
- Use the obtained access token in the response for subsequent API requests by including it in the Authorization header:

5. bash
Copy code
Authorization: Bearer <access-token>
- Create a new room by making a POST request to /create_room with the following JSON payload:

json
Copy code
{
  "roomname": "your-room-name",
  "userID": "your-user-ID"
}
- Note: You need to be authenticated as a user to create a room.

-**Join an existing room by making a POST request to /join_room with the following JSON payload:**

json
Copy code
{
  "roomID": "room-ID",
  "userID": "your-user-ID"
}
Note: You need to be authenticated as a user to join a room.

Send a message in a room by making a POST request to /send_message with the following JSON payload:

json
Copy code
{
  "roomID": "room-ID",
  "userID": "your-user-ID",
  "message": "your-message"
}
- Note: You need to be authenticated as a user and a member of the room to send a message.

- Delete a message by making a POST request to /delete_message with the following JSON payload:

json
Copy code
{
  "roomID": "room-ID",
  "messageID": "message-ID",
  "userID": "your-user-ID"
}
- Note: You can only delete your own messages.

- Retrieve all messages in a room by making a GET request to /get_messages/<room-ID>.

- Retrieve a list of all rooms by making a GET request to /get_rooms.

### API Endpoints

- POST /register: Register a new user.
- POST /login: Log in with user credentials.
- POST /create_room: Create a new chat room.
- POST /join_room: Join an existing chat room.
- POST /send_message: Send a message in a chat room.
- POST /delete_message: Delete a message in a chat room.
- GET /get_messages/<room-ID>: Get all messages in a chat room.
- GET /get_rooms: Get a list of all chat rooms.

## Socket Events
- **join**: Join a room.
- **leave**: Leave a room.
- **message**: Send a message in a room.
- **delete_message**: Delete a message in a room.
- **connect**: Connect to the server.
- **disconnect**: Disconnect from the server.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

Please note that the code blocks in the Markdown file are indented by four spaces for proper formatting..
