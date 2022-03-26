#CREATE AND IP_LAYER PACKET AND PRINT IT OUT

#IMPORT ICMP LAYER
from scapy.layers.inet import ICMP
#IMPORT IP LAYER
from scapy.layers.inet import IP
#Import sr to send pkg #https://thepacketgeek.com/scapy/building-network-tools/part-06/
from scapy.sendrecv import sr1

if __name__ == "__main__":
    src_ip = "192.168.1.31"
    dest_ip = "www.google.com"
    #Create IP Layer
    ip_layer = IP(src = src_ip, dst = dest_ip)
    #Create ICMP Layer
    icmp_req = ICMP(id=100)
    #Create packet combined 2 layers
    #Note the / operator. This operator is used to combine different layers in Scapy
    packet = ip_layer / icmp_req
    #Send paquet with sr1
    response = sr1(packet, iface="eno1")
    #Show response
    if response:
        print(response.show())

