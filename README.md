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
>resources/training/[eth0hwch.py](https://github.com/badorius/python-hacking/blob/main/resources/training/eth0hwch/main.py)

# Introduction to Scapy
Scapy library is designed to send, sniff, dissect, and edit network packets. Scapy is a very powerful network packet manipulation tool. More about scapy:
>[scapy site](https://scapy.readthedocs.io/en/latest/introduction.html)

# Installing Scpay
In order to scapy works with fine privileges, we need to install it on system:
```shell pacman -S scapy```
or 
```shell sudo pip3 install scapy```
