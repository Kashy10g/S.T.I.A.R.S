import os
import time
import requests
import urllib3
from dotenv import load_dotenv

# 1. INITIALIZE: Load your hidden secrets from the .env file
load_dotenv() 

# 2. SETUP: Silence SSL warnings for local network testing
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 3. CONFIGURATION: Securely pull your keys into the script
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("MY_CHAT_ID")

# --- PROMPT FOR THE TARGET ---
TARGET_URL = input("Enter the website to guard (include http/https): ")
# ------------------------------------------

def send_telegram_msg(message):
    """Function to push alerts to your phone"""
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(api_url, data=payload, timeout=10)
    except Exception as e:
        print(f"❌ Failed to send Telegram alert: {e}")

print(f"🚀 Shield Active. Guarding {TARGET_URL}...")
send_telegram_msg(f"✅ **Monitor Started**\nNow guarding: {TARGET_URL}")

while True:
    current_time = time.strftime('%H:%M:%S')
    try:
        # THE KNOCK
        response = requests.get(TARGET_URL, verify=False, timeout=5)

        if response.status_code == 200:
            print(f"[{current_time}] Site is healthy.")
            # We don't message for 'UP' to avoid spamming your phone
        else:
            alert = f"⚠️ **SECURITY ALERT**\nSite: {TARGET_URL}\nStatus: {response.status_code}\nTime: {current_time}"
            print(alert)
            send_telegram_msg(alert)

    except Exception:
        alert = f"🚨 **CRITICAL FAILURE**\nTarget {TARGET_URL} is DOWN!\nTime: {current_time}"
        print(alert)
        send_telegram_msg(alert)

    # Log to file as well (The Black Box)
    with open("security_log.txt", "a") as f:
        f.write(f"[{current_time}] Checked {TARGET_URL}\n")

    time.sleep(60) # Wait 1 minute