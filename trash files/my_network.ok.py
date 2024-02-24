#!/usr/bin/python3

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
        link_config = dict(bw=10)  # Total Capacity of the link ~ 10Mbps
        host_link_config = dict()

        # Definizione dei prefissi MAC
        vendpor_prefix = "00:00:00:"
        device_type_prefix = "00"

        #switch 00
        group_id = "00:"
        sw0 = self.addSwitch("sw0", mac=vendpor_prefix + group_id+ "00:01")

        group_id = "01:"
        sw1 = self.addSwitch("sw1", mac=vendpor_prefix + group_id+ "00:01")
        sw3 = self.addSwitch("sw3", mac=vendpor_prefix + group_id+ "00:02")
        sw4 = self.addSwitch("sw4", mac=vendpor_prefix + group_id+ "00:03")

        group_id = "02:"
        sw2 = self.addSwitch("sw2", mac=vendpor_prefix + group_id+ "00:01")
        sw5 = self.addSwitch("sw5", mac=vendpor_prefix + group_id+ "00:02")
        sw6 = self.addSwitch("sw6", mac=vendpor_prefix + group_id+ "00:03")

        #host 01
        group_id = "00:"
        h0 = self.addHost("h0", mac=vendpor_prefix + "00:01:01", **host_config)
        
        group_id = "01:"
        h1 = self.addHost("h1", mac=vendpor_prefix + group_id+ "01:01", **host_config)
        h2 = self.addHost("h2", mac=vendpor_prefix + group_id+ "01:02", **host_config)
        h3 = self.addHost("h3", mac=vendpor_prefix + group_id+ "01:03", **host_config)
        
        group_id = "02:"
        h4 = self.addHost("h4", mac=vendpor_prefix + group_id+ "01:01", **host_config)
        h5 = self.addHost("h5", mac=vendpor_prefix + group_id+ "01:02", **host_config)
        h6 = self.addHost("h6", mac=vendpor_prefix + group_id+ "01:03", **host_config)
        
        group_id = "00:"
        s0 = self.addHost("s0", mac=vendpor_prefix + group_id+ "02:01", **host_config)
        
        #server 02
        group_id = "01:"
        s1 = self.addHost("s1", mac=vendpor_prefix + group_id+ "02:01", **host_config)
        s2 = self.addHost("s2", mac=vendpor_prefix + group_id+ "02:01", **host_config)
        
        group_id = "02:"
        s3 = self.addHost("s3", mac=vendpor_prefix + group_id+ "02:02", **host_config)
        s4 = self.addHost("s4", mac=vendpor_prefix + group_id+ "02:03", **host_config)

        # Collegamento dei nodi
        self.addLink(sw0, h0, **link_config)
        self.addLink(sw0, s0, **link_config)

        self.addLink(sw0, sw1, **link_config)
        self.addLink(sw0, sw2, **link_config)

        self.addLink(sw1, sw3, **link_config)
        self.addLink(sw1, sw4, **link_config)

        self.addLink(sw2, sw5, **link_config)
        self.addLink(sw2, sw6, **link_config)

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
        
        # We specify an external controller by passing the Controller object in the Mininet constructor
        # This was added in Mininet 2.2.0 and above.
        # SOS Note: Do not specify port -- Default: 6653
        controller=RemoteController( 'c0', ip='127.0.0.1'), 
        switch=OVSKernelSwitch,
        build=False,
        #autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,
    )
    
    # ------------ Check Constructor for Controller ----------------- #
    #controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    #net.addController(controller)
    
    net.build()
    net.start()
    
    # Here we automate the process of creating the 2 slices by calling as a subprocess the common_scenario.sh
    # Assumption: We begin with a non-emergency scenario.
    subprocess.call("./common_scenario.sh")
    
    CLI(net)
    net.stop()
