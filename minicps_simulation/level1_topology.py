import json
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class SimpleAttackTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        # Internal Network
        server = self.addHost('server', ip='10.0.0.10')
        workstation = self.addHost('workstation', ip='10.0.0.20')

        # External Attacker
        attacker = self.addHost('attacker', ip='192.168.1.100')

        # Add links with explicit interface names
        self.addLink(server, switch, intfName1='server-eth0', intfName2='s1-eth1')
        self.addLink(workstation, switch, intfName1='station-eth0', intfName2='s1-eth2')
        self.addLink(attacker, switch, intfName1='attacker-eth0', intfName2='s1-eth3')

def generate_topology_json():
    """Generate JSON representation of the Mininet topology."""
    topo = SimpleAttackTopo()
    nodes = []
    links = []

    for node in topo.nodes():
        nodes.append({"id": node, "label": node})

    for link in topo.links():
        links.append({"source": link[0], "target": link[1]})

    network_data = {"nodes": nodes, "links": links}

    with open("static/topology.json", "w") as f:
        json.dump(network_data, f, indent=4)

    print("Topology JSON saved to static/topology.json")


def run():
    topo = SimpleAttackTopo()
    net = Mininet(topo=topo, controller=Controller)
    net.start()
    generate_topology_json() # Export network data for visualisation
    net.interact()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()