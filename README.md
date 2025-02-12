# WLAN Watchdog
Get notified when having unwanted devices in your network.

# Setup
Create a file name `known_devices.csv` in the root folder for adding known devices' MAC addresses. The file should have the following format:
```csv
00:11:22:33:44:55,My Phone
00:11:22:33:44:56,My Laptop
00:11:22:33:44:57,My Smart TV
00:11:22:33:44:58,My Smart Speaker
00:11:22:33:44:59,My Smart Watch
00:11:22:33:44:60,My Tablet
00:11:22:33:44:61,My Desktop
00:11:22:33:44:62,My Printer
00:11:22:33:44:63,My Game Console
00:11:22:33:44:64,My Camera
00:11:22:33:44:65,My Smart Fridge
etc.
```

Create a virtual environment (Python 3) and activate it.
```bash
python -m venv venv
source venv/bin/activate
```

Then run the following command to install the required packages:
```bash
pip install -r requirements.txt
```
Run the script with the following command:
```bash
python -m src.main
```


## Push Notifications
To receive notifications, you need a Pushover account. Create an application and get the API token and user key. Create a `.env` file in the root of the project and add these keys to it. The file should have the following format:
```
PUSHOVER_TOKEN=application_token
PUSHOVER_USER=user_key
```