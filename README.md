# PYTHON HACKING NOTES
Create virtual environment:
```shell
python3 -m venv my-virtualenv
source my-virtualenv/bin/activate
```
---
Python has a standard library that it uses to run system commands called subprocess. This library allows you to interact with the underlying OS.
To import this library:
```python
import subprocess
```
Subprocess example changeing HW adress from eth0 interface:
>resources/training/eth0hwch/[main.py](https://github.com/badorius/python-hacking/blob/main/resources/training/eth0hwch/main.py)

# Introduction to Scapy
Scapy library is designed to send, sniff, dissect, and edit network packets. Scapy is a very powerful network packet manipulation tool. More about scapy:
>[scapy site](https://scapy.readthedocs.io/en/latest/introduction.html)

# Installing Scpay
In order to scapy works with fine privileges, we need to install it on system:
```shell 
pacman -S scapy
```
or 
```shell 
sudo pip3 install scapy
```

# Understanding how Scapy Works
Create a small ping request example:

In case you would like to import all scapy package library to our python program: 
```python
from scapy.all import scapy
```
To use ICMP layer, we need to import:
```python
from scapy.layers.inet import ICMP

```
To send a ping request, we need to create an IP layer packet, to import IP Layer from scapy:
```python
from scapy.layers.inet import IP
```
To send and recive packets, we can use a function called sr. To import this function:
```python
from scapy.sendrecv import sr1
```
For more detail about sr function see
>[https://thepacketgeek.com/scapy/building-network-tools/part-06/](https://thepacketgeek.com/scapy/building-network-tools/part-06/)

Notes from example:
```python
    #Create IP Layer
    ip_layer = IP(src = src_ip, dst = dest_ip)
    #Create ICMP Layer
    icmp_req = ICMP(id=100)
    #Create packet combined 2 layers
    #Note the / operator. This operator is used to combine different layers in Scapy
    packet = ip_layer / icmp_req
    #Send paquet with sr1
    response = sr1(packet, iface="eno1")
```
>NOTE: The / operator. This operator is used to combine different layers in Scapy

Output:

```shell
sudo python main.py 
[sudo] password for user: 
Begin emission:
Finished sending 1 packets.
...*
Received 4 packets, got 1 answers, remaining 0 packets
###[ IP ]### 
  version   = 4
  ihl       = 5
  tos       = 0x0
  len       = 28
  id        = 0
  flags     = 
  frag      = 0
  ttl       = 119
  proto     = icmp
  chksum    = 0x407b
  src       = 142.250.178.164
  dst       = 192.168.1.31
  \options   \
###[ ICMP ]### 
     type      = echo-reply
     code      = 0
     chksum    = 0xff9b
     id        = 0x64
     seq       = 0x0
     unused    = ''
###[ Padding ]### 
        load      = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

None
```
Example:
>resources/training/introduction-scapy/[main.py](https://github.com/badorius/python-hacking/blob/main/resources/training/introduction-scapy/main.py)

If you want to see more details about a certain layer in Scapy and what options are available in the layer to modify, you can use the ls function in Scapy. To import this function, you can use this command:
```python
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
```
>resources/training/ls_layer-scapy/[main.py](https://github.com/badorius/python-hacking/blob/main/resources/training/ls_layer-scapy/main.py)

The output should be:
```shell
version    : BitField  (4 bits)                  = 4               ('4')
ihl        : BitField  (4 bits)                  = None            ('None')
tos        : XByteField                          = 0               ('0')
len        : ShortField                          = None            ('None')
id         : ShortField                          = 1               ('1')
flags      : FlagsField                          = <Flag 0 ()>     ('<Flag 0 ()>')
frag       : BitField  (13 bits)                 = 0               ('0')
ttl        : ByteField                           = 64              ('64')
proto      : ByteEnumField                       = 0               ('0')
chksum     : XShortField                         = None            ('None')
src        : SourceIPField                       = '192.168.1.23'  ('None')
dst        : DestIPField                         = Net("www.google.com/32") ('None')
options    : PacketListField                     = []              ('[]')
None
Destination  =  142.250.178.164
Summary  =  192.168.1.23 > Net("www.google.com/32") hopopt
Process finished with exit code 0
```
>NOTE: We can access any value from ls using . Example: print("Destination  = ", ip_layer.dst) This function call will print dst value. The same with summary print.
---
# Network scanner using Scapy
We start creating an ARP scanner with python 

```python
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
```
>resources/training/arp_scanner-scapy/[main.py](https://github.com/badorius/python-hacking/blob/main/resources/training/arp_scanner-scapy/main.py)



