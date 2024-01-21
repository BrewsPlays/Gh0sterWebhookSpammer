import requests
from art import *

def send_webhook(webhook_url, message, repeat):
    for _ in range(repeat):
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code != 204:
            raise ValueError(f"Request to '{webhook_url}' returned an error {response.status_code}, the response is:\n{response.text}")

def main():
    print(text2art("Gh0ster Webhook"))
    print(text2art("Spammer"))
    webhook_url = input("Enter Webhook URL: ")
    message = input("Enter Message: ")
    repeat = int(input("Repeat: "))
    send_webhook(webhook_url, message, repeat)

if __name__ == "__main__":
    main()
