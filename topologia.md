
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

Collegamenti:

    sw0 è collegato a:
        h0
        s0
        sw1
        sw2
    sw1 è collegato a:
        sw3
        sw4
    sw2 è collegato a:
        sw5
        sw6
    sw3 è collegato a:
        h1
        h2
        h3
    sw4 è collegato a:
        s1
        s2
    sw5 è collegato a:
        h4
        h5
        h6
    sw6 è collegato a:
        s3
        s4
