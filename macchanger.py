from logging import exception
import subprocess as sub
import re
import uuid

def change_mac_windwos(new_mac_address):
    print("Sorry bro that's not a working feature yet")

def change_mac_linux(new_mac=None, interface=None):


    if not interface:
        exception("\n\nCould not change MAC address. ERR: No interface supplied")
        return

    print('\n[+] Changing the MAC Address to', new_mac)
    sub.call(['sudo', 'ifconfig', interface, 'down'])
    sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    sub.call(['sudo', 'ifconfig', interface, 'up'])
    print(f"Changed MAC to: {new_mac}")

def check_mac_linux(iface):
    # use the ifconfig command to get the interface details, including the MAC address
    output = sub.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def check_mac_windows():
    print ("Your current mac address is: ", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

