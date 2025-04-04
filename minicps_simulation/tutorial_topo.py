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
        pc1 = self.addHost('PC1', ip='10.0.0.20')

        # External Attacker
        pc2 = self.addHost('PC2', ip='192.168.1.100')

        # Add links with explicit interface names
        self.addLink(server, switch, intfName1='server-eth0', intfName2='s1-eth1')
        self.addLink(pc1, switch, intfName1='pc1-eth0', intfName2='s1-eth2')
        self.addLink(pc2, switch, intfName1='PC2-eth0', intfName2='s1-eth3')

topos = { 'tutorial': ( lambda: SimpleAttackTopo() ) }


def run():
    topo = SimpleAttackTopo()
    net = Mininet(topo=topo, controller=Controller)
    net.start()
    net.interact()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()