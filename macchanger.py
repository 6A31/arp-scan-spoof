from logging import exception
import subprocess as sub
import re
import uuid
from colorama import Fore, Style
def change_mac_windwos(new_mac_address):
    print(f"{Fore.RED}Sorry bro that's not a working feature yet{Style.RESET_ALL}")

def change_mac_linux(new_mac=None, interface=None):


    if not interface:
        exception(f"\n\n{Fore.RED}Could not change MAC address. ERR: No interface supplied{Style.RESET_ALL}")
        return

    print('\n[+] Changing the MAC Address to', new_mac)
    sub.call(['sudo', 'ifconfig', interface, 'down'])
    sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
    sub.call(['sudo', 'ifconfig', interface, 'up'])
    print(f"Changed MAC to: {new_mac}")

def check_mac_linux(iface):
    output = sub.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def check_mac_windows():
    print (f"Your current mac address is: {Fore.GREEN}", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

