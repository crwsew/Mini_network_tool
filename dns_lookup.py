import socket
from logger import log_activity

def dns_lookup():
    domain = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP address of {domain}: {ip}")
        log_activity(f"DNS Lookup -> {domain} | IP: {ip}")

    except Exception as e:
        print("Error:", e)
        log_activity(f"DNS ERROR -> {domain} | {e}")