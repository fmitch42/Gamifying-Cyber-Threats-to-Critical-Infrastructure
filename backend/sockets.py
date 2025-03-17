from flask_socketio import SocketIO, emit
import subprocess

socketio = SocketIO()

@socketio.on('attack_trigger')
def handle_attack_trigger(message):
    subprocess.call(["python3", "minicps_simulation/attack_simulation.py", "start"])
    emit('status_update', {'status': 'Attack started'}, broadcast=True)
