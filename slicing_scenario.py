import subprocess
import threading
import time
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types


class TrafficSlicing(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(TrafficSlicing, self).__init__(*args, **kwargs)
        
               
        
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
                                                         
                                                        
                                          
        # Destination Mapping [router --> MAC Destination --> Eth Port Output]
        self.mac_to_port = {
            'sw0': {
                mac_sw1: 1,  # Port connected to sw1
                mac_sw2: 2,  # Port connected to sw2
                mac_h0: 3,   # Port connected to h0
                mac_s0: 4    # Port connected to s0
            },
            'sw1': {
                mac_sw0: 1,  # Port connected to sw0
                mac_sw3: 2,  # Port connected to sw3
                mac_sw4: 3   # Port connected to sw4
            },
            'sw2': {
                mac_sw0: 1,  # Port connected to sw0
                mac_sw5: 2,  # Port connected to sw5
                mac_sw6: 3   # Port connected to sw6
            },
            'sw3': {
                mac_sw1: 1,  # Port connected to sw1
                mac_h1: 2,   # Port connected to h1
                mac_h2: 3,   # Port connected to h2
                mac_h3: 4    # Port connected to h3
            },
            'sw4': {
                mac_sw1: 1,  # Port connected to sw1
                mac_s1: 2,   # Port connected to s1
                mac_s2: 3    # Port connected to s2
            },
            'sw5': {
                mac_sw2: 1,  # Port connected to sw2
                mac_h4: 2,   # Port connected to h4
                mac_h5: 3,   # Port connected to h5
                mac_h6: 4    # Port connected to h6
            },
            'sw6': {
                mac_sw2: 1,  # Port connected to sw2
                mac_s3: 2,   # Port connected to s3
                mac_s4: 3    # Port connected to s4
            }
        }



        self.thread = threading.Thread(target=self.init, args=())
        self.thread.start()

        # Source Mapping
        self.port_to_port = {
            "sw0": {
                1: 2,  # Porta 1 di sw0 si collega a sw1
                2: 3,  # Porta 2 di sw0 si collega a sw2
                3: 1,  # Porta 3 di sw0 si collega a h0
                4: 1   # Porta 4 di sw0 si collega a s0
            },
            "sw1": {
                1: 4,  # Porta 1 di sw1 si collega a sw3
                2: 1,  # Porta 2 di sw1 si collega a h1
                3: 2,  # Porta 3 di sw1 si collega a h2
                4: 3   # Porta 4 di sw1 si collega a h3
            },
            "sw2": {
                1: 4,  # Porta 1 di sw2 si collega a sw4
                2: 1,  # Porta 2 di sw2 si collega a h4
                3: 2,  # Porta 3 di sw2 si collega a h5
                4: 3   # Porta 4 di sw2 si collega a h6
            },
            "sw3": {
                1: 1,  # Porta 1 di sw3 si collega a s1
                2: 2   # Porta 2 di sw3 si collega a s2
            },
            "sw4": {
                1: 1,  # Porta 1 di sw4 si collega a s3
                2: 2   # Porta 2 di sw4 si collega a s4
            },
            "sw5": {
                1: 1,  # Porta 1 di sw5 si collega a h4
                2: 2,  # Porta 2 di sw5 si collega a h5
                3: 3   # Porta 3 di sw5 si collega a h6
            },
            "sw6": {
                1: 1,  # Porta 1 di sw6 si collega a s3
                2: 2   # Porta 2 di sw6 si collega a s4
            }
        }


    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install the table-miss flow entry.
        match = parser.OFPMatch()
        actions = [
            parser.OFPActionOutput(
                ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)
        ]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # construct flow_mod message and send it.
        inst = [parser.OFPInstructionActions(
            ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = parser.OFPFlowMod(
            datapath=datapath, priority=priority, match=match, instructions=inst
        )
        datapath.send_msg(mod)

    def _send_package(self, msg, datapath, in_port, actions):
        data = None
        ofproto = datapath.ofproto
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = datapath.ofproto_parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=data,
        )
        datapath.send_msg(out)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        in_port = msg.match["in_port"]

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            # ignore lldp packet
            return

        dst = eth.dst
        src = eth.src

        dpid = datapath.id

        if dpid in self.mac_to_port:
            if dst in self.mac_to_port[dpid]:
                out_port = self.mac_to_port[dpid][dst]
                actions = [datapath.ofproto_parser.OFPActionOutput(out_port)]
                match = datapath.ofproto_parser.OFPMatch(eth_dst=dst)
                self.add_flow(datapath, 1, match, actions)
                self._send_package(msg, datapath, in_port, actions)

    def init(self):
        time.sleep(1)

        subprocess.run(["sudo", "python3", "my_network.py"])