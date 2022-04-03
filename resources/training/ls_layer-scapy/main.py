#CREATE AND IP_LAYER PACKET AND LS
from scapy.layers.inet import IP
from scapy.all import ls

#To get information about ip_layer, we can print ls like this:
dest_ip = "www.google.com"
ip_layer = IP(dst = dest_ip)
print(ls(ip_layer))

#PRINTING ONE VALUE FROM LS
print("Destination  = ", ip_layer.dst)

#PRINTING SUMMARY
print("Summary  = ",ip_layer.summary())