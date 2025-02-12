import os

INTERFACE = "eth0"
ARP_SCAN_CMD = ["sudo", "arp-scan", "--localnet", "--interface", INTERFACE]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWN_DEVICES_FILE = os.path.join(BASE_DIR, "known_devices.csv")