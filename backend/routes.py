from flask import Blueprint, jsonify
import subprocess

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/network/status', methods=['GET'])
def get_network_status():
    status = subprocess.check_output(["python3", "minicps_simulation/topology.py", "get_status"])
    return jsonify({'status': status.decode('utf-8')})
