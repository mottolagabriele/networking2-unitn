#!/bin/bash


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

# Definizione degli indirizzi IP per gli host
ip_h0="10.0.0.1"
ip_h1="10.0.0.2"
ip_h2="10.0.0.3"
ip_h3="10.0.0.4"
ip_h4="10.0.0.5"
ip_h5="10.0.0.6"
ip_h6="10.0.0.7"

# Definizione degli indirizzi IP per i server
ip_s0="10.0.0.8"
ip_s1="10.0.0.9"
ip_s2="10.0.0.10"
ip_s3="10.0.0.11"
ip_s4="10.0.0.12"


vendor_id="00:00:00"


devices=("sw0" "sw1" "sw2" "sw3" "sw4" "sw5" "sw6")

for device in "${devices[@]}"
do
    sudo ovs-vsctl -- clear Port $device qos
    sudo ovs-vsctl -- clear Port $device qos
done

sudo ovs-vsctl -- --all destroy QoS -- --all destroy Queue


for device in "${devices[@]}"
do
    sudo ovs-vsctl set port $device qos=@newqos -- \
    --id=@newqos create QoS type=linux-htb \
    other-config:max-rate=10000000 \
    queues:1=@1q \
    queues:2=@2q -- \
    --id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
    --id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000
    #for eth in eth1 eth2 eth3 eth4
    #do
    #    echo "Creating slices on ${device}-${eth}..."
    #    sudo ovs-vsctl set port ${device}-${eth} qos=@${device}-${eth}-qos -- \
    #    --id=@${device}-${eth}-qos create QoS type=linux-htb \
    #    other-config:max-rate=10000000 \
    #    queues:1=@${device}-${eth}-q1 \
    #    queues:2=@${device}-${eth}-q2 -- \
    #    --id=@${device}-${eth}-q1 create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
    #    --id=@${device}-${eth}-q2 create queue other-config:min-rate=1000000 other-config:max-rate=5000000
    #done
done


echo 'End of slice creation [3].'


mask=24
# Regole per la prima slice (h1,h2,h3,h4,h5,h6 <-> s1,s3)
for device in "${devices[@]}"
do

    # Mapping degli IP agli host e ai server sulle slice
    # Prima slice (s1, s3) possono essere contattati da (h1, h2, h3, h4, h5, h6)
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h1,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h2,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h3,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h4,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h5,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h6,nw_dst=$ip_s1,idle_timeout=0,actions=set_queue:1,normal

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h5,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s1,nw_dst=$ip_h6,idle_timeout=0,actions=set_queue:1,normal


    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h5,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s3,nw_dst=$ip_h6,idle_timeout=0,actions=set_queue:1,normal

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h1,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h2,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h4,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h3,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h6,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h5,nw_dst=$ip_s3,idle_timeout=0,actions=set_queue:1,normal

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h5,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h6,idle_timeout=0,actions=set_queue:1,normal

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h1,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h2,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h4,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h3,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h6,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h5,nw_dst=$ip_s2,idle_timeout=0,actions=set_queue:1,normal


    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h1,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h2,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h3,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h5,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h6,idle_timeout=0,actions=set_queue:1,normal

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h1,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h2,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h4,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h3,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h6,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h5,nw_dst=$ip_s4,idle_timeout=0,actions=set_queue:1,normal




    # Seconda slice (s0, s2, s4) possono comunicare tra loro

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h0,nw_dst=$ip_s0,idle_timeout=0,actions=set_queue:2,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h0,nw_dst=$ip_s2,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_h0,nw_dst=$ip_s4,idle_timeout=0,actions=drop

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s0,nw_dst=$ip_h0,idle_timeout=0,actions=set_queue:2,normal
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s0,nw_dst=$ip_s2,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s0,nw_dst=$ip_s4,idle_timeout=0,actions=drop

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_h0,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_s0,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s2,nw_dst=$ip_s4,idle_timeout=0,actions=drop

    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_h0,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_s0,idle_timeout=0,actions=drop
    sudo ovs-ofctl add-flow $device ip,priority=65500,nw_src=$ip_s4,nw_dst=$ip_s2,idle_timeout=0,actions=drop


    # Assicurati che altri flussi non specificati siano lasciati cadere
    sudo ovs-ofctl add-flow $device priority=1,actions=drop
done
   