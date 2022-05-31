import subprocess
import re
import uuid
from colorama import Fore, Style



def change_mac_linux(new_mac=None, interface=None):


    if not interface:
        print(f"\n{Fore.RED}Could not change MAC address. ERR: No interface supplied{Style.RESET_ALL}\n")
        return

    print('\n[+] Changing the MAC Address to', new_mac)
    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    print(f"Changed MAC to: {new_mac}")

def check_mac_linux(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    print(re.search("ether (.+) ", output).group().split()[1].strip())

def check_mac_windows():
    print (f"\nYour current MAC address is: {Fore.GREEN}", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))
    print(Style.RESET_ALL) # Don't know how to add this to the other line...


    