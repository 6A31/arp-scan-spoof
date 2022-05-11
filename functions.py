import scapy.all as scapy
import requests
import socket
import re
from colorama import Fore, Style

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
    print("Checking vendors....")
    for count, i in enumerate(answered):
        ip, mac = i[1].psrc, i[1].hwsrc
        dict[count] = [ip, mac, requests.get("https://macvendors.co/api/vendorname/{i[1.hwsrc]}").text]
    return dict
