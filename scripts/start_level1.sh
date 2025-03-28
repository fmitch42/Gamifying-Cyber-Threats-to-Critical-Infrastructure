#!/bin/bash
echo "Starting Level 1"
sudo python3 ./minicps_simulation/level1_topology.py &

PID=$!
echo $PID | sudo tee mininet.pid