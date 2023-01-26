import argparse
import socket  # for connecting
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

# number of threads, feel free to tune this parameter as you wish
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()


def port_scan(host, port):
    print(f"{GRAY}{host:15}:{port:5} is closed  {RESET}", end='\r')
    print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")

    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        print(f"{GRAY}{host:15}:{port:5} is closed  {RESET}", end='\r')
    else:
        print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
    finally:
        s.close()


def main():
    host = "192.168.1.254"
    port = "22"
    port_scan(host, port)


if __name__ == '__main__':
    main()
