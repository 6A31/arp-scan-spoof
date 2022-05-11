# arp-scan-spoof
**Search devices on your local network via ARP protocol and easily spoof them.**

**Bypass guest logins in free WiFi by spoofing a MAC address of an already registered device.**

-------------

# Script

This script features auto IP range detection, MAC address vendor check (works offline) and inbuilt spoofing.

Using mc-vendor-lookup it is easy to determine what devices are phones, computers and routers. By using the compact console output layout, it is easy to select and spoof a desired device.

The script was tested on **Windows 10 and Linux (Ubuntu)**.

**Dependencies: `scapy`, `colorama`, `requests`, `mac-vendor-lookup`, `winreg`, `re`**


> If you get an `Module Error` try installing the module with `pip install modulenamhere`

# Download
Download the **COMING SOON** [.EXE](https://placeholder.com) from the release page or clone the repository and run **`main.py`**


## Windows
Make sure to run the script as administrator on Windows. Changing a MAC address requires admin privileges.


## Linux
Make sure to run the script as administrator as the script will execute 3 "sudo" commands (interface down, up, MAC change).

# Files

The script is spread across 3 files, **[main.py](https://github.com/ScobraScope/arp-scan-spoof/blob/main/main.py) | [functions.py](https://github.com/ScobraScope/arp-scan-spoof/blob/main/functions.py) | [macchanger.py](https://github.com/ScobraScope/arp-scan-spoof/blob/main/macchanger.py)**

Make sure to have all files in the same folder when running `main.py`.

## Support

Talk to me on [Discord](https://discord.6A31.com)

## FAQ

Why does my Antivirus flag X file?
> Your antivirus may flag the .exe file malicious as it containes code that modifies & snifs on network interfaces

I'm getting X Y and Z Error.
> Open a github issue or talk to me on [Discord](https://discord.6A31.com)

## Example use case

**COMING SOON**

