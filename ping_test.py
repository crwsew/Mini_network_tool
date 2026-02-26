import subprocess
import platform
from logger import log_activity

def ping_test():
    target = input("Enter domain or IP to ping: ")

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", target],
            capture_output=True,
            text=True
        )

        print("\n--- PING RESULT ---\n")
        print(result.stdout)

        log_activity(f"PING -> {target}")

    except Exception as e:
        print("Error:", e)
        log_activity(f"PING ERROR -> {target} | {e}")