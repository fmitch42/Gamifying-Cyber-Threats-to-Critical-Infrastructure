from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Serve a simple HTML page

# Define a route to handle player actions
@app.route('/action', methods=['POST'])
def action():
    data = request.json  # Get JSON data from the request
    action_type = data.get('action')
    # Handle the action here (e.g., add firewall, monitor logs, etc.)
    return jsonify({"message": f"Action '{action_type}' received!"})

# Run the app
if __name__ == '__main__':
    socketio.run(app, debug=True)
