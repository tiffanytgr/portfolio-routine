import os
import requests
import sys

def send_message(text):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Missing Telegram Environment Credentials.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Telegram max message length is 4096 chars; split if needed
    chunks = [text[i:i+4096] for i in range(0, len(text), 4096)]
    for chunk in chunks:
        payload = {"chat_id": chat_id, "text": chunk, "parse_mode": "Markdown"}
        response = requests.post(url, json=payload)
        if not response.ok:
            # Retry without parse_mode in case of markdown errors
            payload.pop("parse_mode")
            response = requests.post(url, json=payload)
        if not response.ok:
            print(f"Failed: {response.status_code} {response.text}")
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        send_message(message)
