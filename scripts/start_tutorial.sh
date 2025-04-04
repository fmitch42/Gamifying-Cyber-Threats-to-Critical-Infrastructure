#!/bin/bash
echo "Starting Tutorial"
cd minicps_simulation
#tmux new -d -s mininet_session "sudo python2 MiniNAM.py --custom level1_topology.py --topo level1"
sudo python2 MiniNAM.py --custom tutorial_topo.py --topo tutorial