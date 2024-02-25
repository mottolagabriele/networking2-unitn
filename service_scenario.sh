#!/bin/bash


# Definisci un array associativo per specificare il numero di porte per ciascuno switch
declare -A switch_ports=(
    [sw0]=4
    [sw1]=3
    [sw2]=3
    [sw3]=4
    [sw4]=3
    [sw5]=4
    [sw6]=3
)

# Valori max-rate predefiniti per le tre code
max_rate1=$1
max_rate2=$2
max_rate3=$3

# Cancella tutte le code esistenti per i dispositivi
# Cancella tutte le code esistenti per ciascuna porta di ciascun dispositivo
for switch in "${!switch_ports[@]}"
do
    num_ports=${switch_ports[$switch]}
    for ((i=1; i<=$num_ports; i++))
    do
        port="eth$i"
        sudo ovs-vsctl -- clear Port ${switch}-${port} qos
    done
done


#for device in "${!switch_ports[@]}"
#do
#    sudo ovs-vsctl -- clear Port $device qos
#done

# Cancella tutte le code esistenti
sudo ovs-vsctl -- --all destroy QoS -- --all destroy Queue

echo "sl1 ${max_rate1} - sl2 ${max_rate2} - sl3 ${max_rate3}"

for switch in "${!switch_ports[@]}"
do
    num_ports=${switch_ports[$switch]}
    for ((i=1; i<=$num_ports; i++))
    do
       #!/bin/bash

    # Definizione dei nomi dei servizi
    TORRENT="torrent"
    STREAMING="streaming"
    VOIP="voip"
    
    # Impostazione delle regole di QoS per gestire il traffico all'interno delle slice
    sudo ovs-vsctl set port ${switch}-${port} qos=@newqos \
    -- --id=@newqos create QoS type=linux-htb \
    other-config:max-rate=1000000000 \
    queues:1=@torrent-queue \
    queues:2=@streaming-queue \
    queues:3=@voip-queue \
    -- --id=@torrent-queue create queue other-config:min-rate=1000000 other-config:max-rate=5000000 \
    -- --id=@streaming-queue create queue other-config:min-rate=1000000 other-config:max-rate=15000000 \
    -- --id=@voip-queue create queue other-config:min-rate=20000000 other-config:max-rate=30000000

    done
done


devices=("sw0" "sw1" "sw2" "sw3" "sw4" "sw5" "sw6")


# Regole per la prima slice (h1,h2,h3,h4,h5,h6 <-> s1,s3)
for device in "${devices[@]}"
do
    #nw_proto -> 6 TPC e 17 UDP
   # Regola per il traffico torrent
    sudo ovs-ofctl add-flow $device \
    "priority=65500,ip,nw_proto=6,tp_dst=6881,actions=set_queue:1,normal"

    # Regola per il traffico streaming uso 1935 dello streaming RTMP
    sudo ovs-ofctl add-flow $device \
        "priority=65500,ip,nw_proto=17,tp_dst=1935,actions=set_queue:2,normal"

    # Regola per il traffico VoIP simulo con SIP 5060
    sudo ovs-ofctl add-flow $device \
        "priority=65500,ip,nw_proto=17,tp_dst=5060,actions=set_queue:3,normal"

        # Assicurati che altri flussi non specificati siano lasciati cadere
    sudo ovs-ofctl add-flow $device priority=1,actions=normal
done

echo '[SERVICE STATE] - Create service slices.'
