import subprocess
if __name__ == "__main__":
    interface = "eth0"
    new_mac = "22:11:22:33:44:57"
    print("Shutting down the interface")
    subprocess.run(["ifconfig", "eth0", "down"])
    print("changing the interface hw address of ", interface, "to ", new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ehter", new_mac])
    print("MAC adress changed to ", new_mac)
    subprocess.run(["ifconfig", interface, "up"])