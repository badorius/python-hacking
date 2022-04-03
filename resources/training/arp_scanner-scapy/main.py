from scapy.layers.inet import Ether
#from scapy.all import Ether, ARP, srp
from scapy.all import srp
from scapy.layers.l2 import ARP

if __name__ == "__main__":
    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)
    ip_range = "192.168.1.1/24"
    arp_layer = ARP(pdst = ip_range)
    packet = ether_layer / arp_layer
    #srp returns both answered and unanswered packets. We are interested in answered packets from online devices only.
    ans, unans = srp(packet, iface = "wlan0", timeout=2)

    # Now, We iterate over the answer to see the IP and corresponding MAC addresses:
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)