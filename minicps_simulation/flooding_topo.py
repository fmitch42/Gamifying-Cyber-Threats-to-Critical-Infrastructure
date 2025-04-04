from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
import time

class FloodingAttackTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')

        # Adding hosts
        server = self.addHost('server', ip='10.0.0.10')
        legitimate_user = self.addHost('user', ip='10.0.0.20')
        attacker = self.addHost('attacker', ip='10.0.0.30')

        # Connecting hosts to the switch
        self.addLink(server, switch, intfName1='server-eth0', intfName2='s1-eth1')
        self.addLink(legitimate_user, switch, intfName1='user-eth0', intfName2='s1-eth2')
        self.addLink(attacker, switch, intfName1='attacker-eth0', intfName2='s1-eth3')


topos = { 'flooding': ( lambda: FloodingAttackTopo() ) }


def start_flooding(net):
    """Function to simulate a flooding attack using hping3."""
    attacker = net.get('attacker')
    server_ip = "10.0.0.10"

    print("[*] Attacker is starting the flooding attack...")
    attacker.cmd(f"hping3 --flood --rand-source {server_ip} &")

def run():
    topo = FloodingAttackTopo()
    net = Mininet(topo=topo, controller=Controller)
    net.start()

    print("Network started. Type 'exit' to close Mininet CLI.")
    
    # Start flooding attack after a delay
    time.sleep(2)
    start_flooding(net)
    net.interact()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
