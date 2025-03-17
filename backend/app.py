from flask import Flask
from flask_socketio import SocketIO
from routes import api_blueprint
from sockets import socketio

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Register API routes
app.register_blueprint(api_blueprint)

# Initialize WebSocket support
socketio.init_app(app, cors_allowed_origins="*")

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
