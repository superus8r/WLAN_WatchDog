import subprocess
import re
import csv
from .models import KnownDevice, Device
from src.config import KNOWN_DEVICES_FILE, INTERFACE

def load_known_devices() -> dict:
    """
    Loads known devices from a CSV file.
    Returns a dictionary mapping lower-case MAC addresses to KnownDevice objects.
    """
    known = {}
    with open(KNOWN_DEVICES_FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and len(row) >= 1:
                mac = row[0].strip().lower()
                hint = row[1].strip() if len(row) > 1 else ""
                device = KnownDevice(mac=mac, hint=hint)
                known[device.mac] = device
    return known


def get_all_devices() -> list:
    """
    Scans the network using arp-scan and returns a list of Device objects.
    """
    cmd = ["sudo", "arp-scan", "--localnet", "--interface", INTERFACE]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error running arp-scan: {e}")

    devices = []
    # Pattern to capture IP, MAC, and vendor info:
    # Example arp-scan output line:
    # "192.168.1.2   AA:BB:CC:DD:EE:FF   Some Vendor Inc"
    pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)\s+([0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5})\s+(.+)$')
    for line in output.splitlines():
        match = pattern.match(line)
        if match:
            ip = match.group(1)
            mac = match.group(2).lower()
            vendor = match.group(3).strip()
            devices.append(Device(ip=ip, mac=mac, vendor=vendor, raw=line.strip()))
    return devices