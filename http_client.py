import requests
from logger import log_activity

def http_get():
    url = input("Enter URL (with https://): ")

    try:
        response = requests.get(url)

        print("\n--- RESPONSE INFO ---")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("\nBody (first 300 chars):\n")
        print(response.text[:300])

        log_activity(f"HTTP GET -> {url} | Status: {response.status_code}")

    except Exception as e:
        print("Error:", e)
        log_activity(f"HTTP ERROR -> {url} | {e}")