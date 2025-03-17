from minicps.devices import Device, PLC, SCADA
from minicps.topology import Topology

# Create your network topology
topology = Topology()

plc = PLC('PLC1')
scada = SCADA('SCADA1')

# Add devices to topology
topology.add_device(plc)
topology.add_device(scada)

# Setup connections between devices
plc.connect_to(scada)

# Define behavior of devices (e.g., attack simulation, status reporting)
def simulate_attack():
    plc.attack()  # Simulating an attack on the PLC

topology.run()
