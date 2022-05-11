from functions import arp
from macchanger import change_mac_windwos, change_mac_linux, check_mac_linux, check_mac_windows

check_mac_windows()

change_mac_windwos("c8:b2:9b:45:2c:c0")

check_mac_windows()