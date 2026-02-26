from datetime import datetime

def log_activity(message):
    with open("log.txt", "a") as file:
        file.write(f"[{datetime.now()}] {message}\n")