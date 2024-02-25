from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
import subprocess


class NetworkSlicingTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Create template host, switch, and link
        host_config = dict(inNamespace=True)
        link_config = dict(bw=100)  # Total Capacity of the link ~ 10Mbps
        host_link_config = dict()

        # Definizione dei prefissi MAC
        vendpor_prefix = "00:00:00:"

                # Definizione dei mac per gli switch
        mac_sw0="00:00:00:00:00:01"
        mac_sw1="00:00:00:01:00:01"
        mac_sw2="00:00:00:02:00:01"
        mac_sw3="00:00:00:01:00:02"
        mac_sw4="00:00:00:01:00:03"
        mac_sw5="00:00:00:02:00:02"
        mac_sw6="00:00:00:02:00:03"
        
        # Definizione dei mac per gli host
        mac_h0="00:00:00:00:01:01"
        mac_h1="00:00:00:01:01:01"
        mac_h2="00:00:00:01:01:02"
        mac_h3="00:00:00:01:01:03"
        mac_h4="00:00:00:02:01:01"
        mac_h5="00:00:00:02:01:02"
        mac_h6="00:00:00:02:01:03"
        
        # Definizione dei prefissi per i server
        mac_s0="00:00:00:00:02:01"
        mac_s1="00:00:00:01:02:01"
        mac_s2="00:00:00:01:02:02"
        mac_s3="00:00:00:02:02:01"
        mac_s4="00:00:00:02:02:02"

        #switch 00
        group_id = "00:"
        sw0 = self.addSwitch("sw0", mac=mac_sw0)

        group_id = "01:"
        sw1 = self.addSwitch("sw1", mac=mac_sw1)
        sw3 = self.addSwitch("sw3", mac=mac_sw3)
        sw4 = self.addSwitch("sw4", mac=mac_sw4)

        group_id = "02:"
        sw2 = self.addSwitch("sw2", mac=mac_sw2)
        sw5 = self.addSwitch("sw5", mac=mac_sw5)
        sw6 = self.addSwitch("sw6", mac=mac_sw6)

        #host 01
        group_id = "00:"
        h0 = self.addHost("h0", mac=mac_h0, ip="10.0.0.1/24", **host_config)
        
        group_id = "01:"
        h1 = self.addHost("h1", mac=mac_h1, ip="10.0.0.2/24", **host_config)
        h2 = self.addHost("h2", mac=mac_h2, ip="10.0.0.3/24", **host_config)
        h3 = self.addHost("h3", mac=mac_h3, ip="10.0.0.4/24", **host_config)
        
        group_id = "02:"
        h4 = self.addHost("h4", mac=mac_h4, ip="10.0.0.5/24", **host_config)
        h5 = self.addHost("h5", mac=mac_h4, ip="10.0.0.6/24", **host_config)
        h6 = self.addHost("h6", mac=mac_h6, ip="10.0.0.7/24", **host_config)
        
        group_id = "00:"
        s0 = self.addHost("s0", mac=mac_s0, ip="10.0.0.8/24", **host_config)
        
        #server 02
        group_id = "01:"
        s1 = self.addHost("s1", mac=mac_s1, ip="10.0.0.9/24", **host_config)
        s2 = self.addHost("s2", mac=mac_s2, ip="10.0.0.10/24", **host_config)
        
        group_id = "02:"
        s3 = self.addHost("s3", mac=mac_s3, ip="10.0.0.11/24", **host_config)
        s4 = self.addHost("s4", mac=mac_s4, ip="10.0.0.12/24", **host_config)

        # Collegamento dei nodi
        self.addLink(h0, sw0, **link_config)
        self.addLink(s0, sw0, **link_config)

        self.addLink(sw1,sw0,  **link_config)
        self.addLink(sw2,sw0,  **link_config)

        self.addLink(sw3,sw1,  **link_config)
        self.addLink(sw4,sw1,  **link_config)

        self.addLink(sw5,sw2,  **link_config)
        self.addLink(sw6,sw2,  **link_config)

        # Collegamento dei nodi host agli switch
        self.addLink(h1, sw3, **host_link_config)
        self.addLink(h2, sw3, **host_link_config)
        self.addLink(h3, sw3, **host_link_config)

        self.addLink(s1, sw4, **host_link_config)
        self.addLink(s2, sw4, **host_link_config)

        self.addLink(h4, sw5, **host_link_config)
        self.addLink(h5, sw5, **host_link_config)
        self.addLink(h6, sw5, **host_link_config)

        self.addLink(s3, sw6, **host_link_config)
        self.addLink(s4, sw6, **host_link_config)


topos = {"networkslicingtopo": (lambda: NetworkSlicingTopo())}



if __name__ == "__main__":
    topo = NetworkSlicingTopo()
    net = Mininet(
        topo=topo,
        controller=RemoteController( 'c0', ip='127.0.0.1'), 
        switch=OVSKernelSwitch,
        build=False,
        autoStaticArp=True,
        link=TCLink,
    )
    
    net.build()
    net.start()
    
    CLI(net)
    net.stop()
