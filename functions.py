import scapy.all as scapy
import socket
import re
import time
from colorama import Fore, Style
import requests

from mac_vendor_lookup import MacLookup

# UPDATE MAC VENDOR LIST #
#mac = MacLookup()
#mac.update_vendors()  # <- This can take a few seconds for the download

def find_ip_range():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    octets = re.split('(\W)', local_ip)
    octets[6] = "1/24"
    return "".join(octets)
 
def arp(ip):
    dict = {}
    if ip == "":
        ip = find_ip_range()
        print("Autodetected IP range")
    print(f"{Fore.GREEN}Using IP range:{Fore.YELLOW} {ip} {Style.RESET_ALL}")
    arp_r = scapy.ARP(pdst=ip)
    br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    request = br/arp_r
    answered, unanswered = scapy.srp(request, timeout=1)
    y = 0
    for count, i in enumerate(answered):
        ip, mac = i[1].psrc, i[1].hwsrc
        dict[count] = [ip, mac, lookup_vendor(i[1].hwsrc)]
    return dict

def lookup_vendor(mac):
    try:
        return MacLookup().lookup(mac)
    except:
        return "No Vendor"

def check_conn(attempts, delay=1.5):
    for i in range(attempts):
        try:
            requests.get("https://google.com", timeout=3000)
            time.sleep(delay)
            print(f"\n{Fore.GREEN}Attempt {i} Successful{Style.RESET_ALL}")
            break
        except:
            print(f"{Fore.RED}Failed connection attempt {i}{Style.RESET_ALL}")
            time.sleep(delay)

def wait_for_close():
    time.sleep(20)