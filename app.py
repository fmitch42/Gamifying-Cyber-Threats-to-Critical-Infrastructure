from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import random  # Simulating Minicps network state
import subprocess
import json



mn_process = None

app = Flask(__name__)
socketio = SocketIO(app)

# Simulated network state
network_data = {
    "nodes": [
        {"id": "PLC1", "type": "PLC"},
        {"id": "SCADA", "type": "SCADA"},
        {"id": "HMI", "type": "HMI"}
    ],
    "edges": [
        {"source": "PLC1", "target": "SCADA"},
        {"source": "SCADA", "target": "HMI"}
    ]
}

def start_mininet(level):
    subprocess.Popen(
        f'sudo ./scripts/start_{level}.sh',
        shell=True
    )


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/topology')
def get_topology():
    
    try:
        with open("static/topology.json", "r") as f:
            topology_data = json.load(f)
        return jsonify(topology_data)

    except FileNotFoundError:
            return jsonify({"error": "Topology data not found"}), 404

@app.route("/level1")
def level1():
    start_mininet("level1")

    return render_template("level1.html")

@app.route("/dashboard")
def dashboard():
    
    return render_template("dashboard.html")

@app.route("/level2")
def level2():
    return render_template("level2.html")

@app.route("/level3")
def level3():
    return render_template("level3.html")

@app.route('/stop_mininet', methods=['POST'])
def stop_mininet():

    #Check if a tmux session exists
    result = subprocess.run(
        ["tmux", "has-session", "-t", "mininet_session"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if result.returncode == 0: # check if a session is running
        subprocess.run("tmux kill-session -t mininet_session", shell=True) # close session manually
        print("Mininet session closed") 

    else: # do nothing if user has closed session
        print("Mininet session closed by user")

    return "Mininet closed"

@app.route("/api/network")
def get_network():
    """Returns the current network state."""
    return jsonify(network_data)

@socketio.on("update_network")
def update_network(data):
    """Handle user actions and update the network."""
    global network_data
    network_data["nodes"].append({"id": f"Device{random.randint(2, 100)}", "type": "New Device"})
    socketio.emit("network_updated", network_data)  # Send update to frontend

if __name__ == "__main__":
    socketio.run(app, debug=True)