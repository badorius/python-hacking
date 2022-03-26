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

# Understanding how Scapy Words
Create a small ping request example:

In case you would like to import all scapy package library to our python program: 
```python
from scapy.all import scapy
```
To use ICMP layer, we need to import:
```python
from scapy.layers.inet import ICMP

```
To send a pint request, we need to create an IP layer packet, to import IP Layer from scapy:
```python
from scapy.layers.inet import IP
```
To send and recive packets, we can use a function called sr. To import this function:
```python
from scapy.all import sr
```
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
Output:

```shell
sudo python main.py 
[sudo] password for darthv: 
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



