#!/usr/bin/python

import sys
import socket

TIMEOUT=1
# Defining a target
if len(sys.argv) == 4:

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    fport = int(sys.argv[2])
    eport = int(sys.argv[3]) + 1
else:
    print("Invalid amount of Argument")
    exit()


try:

    # will scan ports between 1 to 65,535
    for port in range(fport, eport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(TIMEOUT)

        # returns an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("{} : Port {} is open".format(target, port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
