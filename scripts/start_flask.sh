#!/bin/bash
echo "Starting Flask Server..."
export FLASK_APP=backend/app.py
flask run --host=0.0.0.0 --port=5000
