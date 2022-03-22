#CREATE AND IP_LAYER PACKET AND PRINT IT OUT
from scapy.layers.inet import ICMP
from scapy.layers.inet import IP
from scapy.all import sr

if __name__ == "__main__":
    src_ip = "192.168.1.23"
    print(src_ip)
    dest_ip = "www.google.com"
    ip_layer = IP(
        src = src_ip,
        dst = dest_ip
    )

    print(ip_layer.show())
