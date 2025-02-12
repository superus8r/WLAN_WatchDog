from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Loads variables from .env into the environment

pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")

def send_notification(message):
    """
    Sends a notification using Pushover.
    """
    payload = {
        "token": pushover_token,
        "user": pushover_user,
        "message": message
    }
    response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Notification failed:", response.text)