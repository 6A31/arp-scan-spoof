# arp-scan-spoof
**Search devices on your local network via ARP protocol and easily spoof them.**

**Bypass guest logins in free WiFi by spoofing a MAC address of an already registered device.**

Requires Python 3!

-------------

# Script

This script features auto IP range detection, MAC address vendor check (works offline) and inbuilt spoofing.

Using mc-vendor-lookup it is easy to determine what devices are phones, computers and routers. By using the compact console output layout, it is easy to select and spoof a desired device.

The script was tested on **Windows 10 and Linux (Ubuntu)**.

**Dependencies: `python3`, `scapy`, `colorama`, `requests`, `mac-vendor-lookup`, `winreg`, `re`**


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

**Talk to me on [Discord](https://discord.6A31.com)**

## FAQ

Why does my Antivirus flag X file?
> Your antivirus may flag the .exe file malicious as it containes code that modifies & snifs on network interfaces

I'm getting X Y and Z Error.
> Open a github issue or talk to me on [Discord](https://discord.6A31.com)

## Example use case

Picture this, you're sitting in a Café and you see, lucky you, a free guest WiFi.
You connect to it expecting to have a simple web access only to find yourself prompted with a "sign up page".

Because you're not a fan of spam emails, you don't feel like entering your email, or even worse, your phone number.

**but fear no more,** someone came to save the day. You can simply bypass the registration by following those steps.

1. Clone the repository
2. Connect to the guest WiFi
3. Run `main.py`
4. Don't supply an IP range to use the auto detection
5. Pick a device that seems like it's a computer or a phone. (take the Vendor as help)
6. Spoof their MAC address
7. Wait for your device to reconnect to the guest WiFi (allow up to a minute)
8. **Enjoy your free guest WiFi**
