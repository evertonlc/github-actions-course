import requests
import time
import os

def ping_url(url: str, max_trials: int, delay_seconds: int) -> bool:

    for _ in range(max_trials):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(delay_seconds)
    return False

def run():

    url = os.getenv("INPUT_URL")
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))
    delay_seconds = int(os.getenv("INPUT_DELAY_SECONDS"))

    if not url:
        print("URL environment variable is not set.")
        return

    if ping_url(url, max_trials, delay_seconds):
        print(f"Successfully pinged {url}")
    else:
        exit(f"Failed to ping {url} after {max_trials} attempts.")

if __name__ == "__main__":
    run()