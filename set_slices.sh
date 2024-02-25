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


for switch in "${!switch_ports[@]}"
do
    num_ports=${switch_ports[$switch]}
    for ((i=1; i<=$num_ports; i++))
    do
        eth="eth$i"
        echo "Creating slices on ${switch}-${eth}..."
        qos_command="sudo ovs-vsctl set port ${switch}-${eth} qos=@${switch}-${eth}-qos -- \
        -- --id=@${switch}-${eth}-qos create QoS type=linux-htb \
        other-config:max-rate=10000000 \
        queues:1=@${switch}-${eth}-q1 \
        queues:2=@${switch}-${eth}-q2 \
        queues:3=@${switch}-${eth}-q3 -- \
        -- --id=@${switch}-${eth}-q1 create queue other-config:min-rate=1000000 other-config:max-rate=${max_rate1} -- \
        --id=@${switch}-${eth}-q2 create queue other-config:min-rate=1000000 other-config:max-rate=${max_rate2} -- \
        --id=@${switch}-${eth}-q3 create queue other-config:min-rate=1000000 other-config:max-rate=${max_rate3}"

        eval $qos_command
    done
done
