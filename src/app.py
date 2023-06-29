from flask import Flask 
from flask_jwt_extended import JWTManager
from routes.user_router import auth_bp
from routes.room_router import room_bp
from routes.chat_router import chat_bp
from middlewares.user_middleware import register_middleware , login_middleware
from middlewares.room_middleware import create_room_middleware , join_room_middleware
from middlewares.message_middleware import message_middleware

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)

app.before_request(register_middleware)
app.before_request(login_middleware)
app.before_request(create_room_middleware)
app.before_request(join_room_middleware)
app.before_request(message_middleware)
app.register_blueprint(auth_bp)
app.register_blueprint(room_bp)
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)