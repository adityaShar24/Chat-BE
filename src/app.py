from flask import Flask 
from flask_jwt_extended import JWTManager
from routes.user_router import auth_bp
from routes.room_router import room_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(room_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)