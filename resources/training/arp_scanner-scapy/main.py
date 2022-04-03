from scapy.layers.inet import Ether
#from scapy.all import Ether, ARP, srp
from scapy.all import srp
from scapy.layers.l2 import ARP

if __name__ == "__main__":
    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)
    ip_range = "192.168.1.0/24"
    arp_layer = ARP(pdst = ip_range)
    packet = ether_layer / arp_layer
    ans, unans = srp(packet, iface = "wlan0", timeout=2)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)