# wlan_monitor/main.py
from src.domain.repository import load_known_devices
from src.domain.repository import get_all_devices
from src.services.notifier import send_notification

def main():
    # Load known devices from CSV file
    known_devices = load_known_devices()
    print("Loaded known devices:")
    for mac, device in known_devices.items():
        print(f"{mac} : {device.hint}")

    # Scan the network
    try:
        scanned_devices = get_all_devices()
    except Exception as e:
        print(e)
        return

    print("Scanned MAC addresses:")
    for device in scanned_devices:
        print("Found:", device.raw)

    # Determine unknown devices
    new_devices = [device for device in scanned_devices if device.mac not in known_devices]
    for device in new_devices:
        print("-> Unknown device detected:", device.raw)

    # Notify if unknown devices found
    if new_devices:
        message_lines = [device.raw for device in new_devices]
        message = "Unknown devices detected:\n" + "\n".join(message_lines)
        send_notification(message)
    else:
        print("No unknown devices detected.")

if __name__ == "__main__":
    main()