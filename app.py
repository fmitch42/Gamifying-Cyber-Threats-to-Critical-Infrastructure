from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import subprocess
import json

app = Flask(__name__)
socketio = SocketIO(app)

def start_mininet(level):
    subprocess.Popen(
        f'sudo ./scripts/start_{level}.sh',
        shell=True
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tutorial")
def tutorial():
    start_mininet("tutorial")

    return render_template("tutorial.html")

@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/wiki")
def wiki():
    return render_template("wiki.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")

@app.route("/basic")
def basic():
    start_mininet("level1")
    return render_template("basic.html")

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

if __name__ == "__main__":
    socketio.run(app, debug=True)