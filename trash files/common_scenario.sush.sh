#!/bin/bash

# Creating slices on sw0
echo 'Creating slices on sw0...'
sudo ovs-vsctl set port sw0 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw1
echo 'Creating slices on sw1...'
sudo ovs-vsctl set port sw1 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw2
echo 'Creating slices on sw2...'
sudo ovs-vsctl set port sw2 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw3
echo 'Creating slices on sw3...'
sudo ovs-vsctl set port sw3 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw4
echo 'Creating slices on sw4...'
sudo ovs-vsctl set port sw4 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw5
echo 'Creating slices on sw5...'
sudo ovs-vsctl set port sw5 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

# Creating slices on sw6
echo 'Creating slices on sw6...'
sudo ovs-vsctl set port sw6 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=1000000 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=1000000 other-config:max-rate=5000000

echo 'End of slice creation.'
vendor_id="00:00:00"
# Map traffic to slices

# Mapping the sw0 queues to hosts and switches connected to it
# Add your mappings for sw0 here
# Mapping the sw0 queues to hosts and switches connected to it
# Regole per la slice 1: h1, h2, h3, h4, h5, h6, s1, s3
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal #h1
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal #h2
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal #h3
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal #h4
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal #h5
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal #h6
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:00:00:01,actions=set_queue:123,normal #w0

sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal #s1
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:02:02:01,actions=set_queue:234,normal #s3
 
# Regole per la slice 2: s2, s4, h0, s0
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal #h0
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal #s1
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:01:02:02,actions=set_queue:234,normal #s2
sudo ovs-ofctl add-flow sw0 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal #s4




# Mapping the sw1 queues to hosts and switches connected to it
# Add your mappings for sw1 here
# Mapping the sw1 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw1 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal

# Mapping the sw2 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw2 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal


# Mapping the sw3 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw3 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal


# Mapping the sw4 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw4 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal


# Mapping the sw5 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw5 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal


# Mapping the sw6 queues to hosts and switches connected to it
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:00:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:01:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:01:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:01:01:03,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:02:01:01,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:02:01:02,actions=set_queue:123,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:02:01:03,actions=set_queue:123,normal

sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:00:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:01:02:01,actions=set_queue:234,normal
sudo ovs-ofctl add-flow sw6 ip,priority=65500,dl_dst=${vendor_id}:02:02:02,actions=set_queue:234,normal
