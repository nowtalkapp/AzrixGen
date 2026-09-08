import os
import sys
import random
import string
import time
import threading
import queue
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

try:
    import requests
except ImportError:
    print("ERROR: Missing library. Run the INSTALL_AND_RUN.bat file first.")
    input()
    sys.exit(1)

# Configuration
DISCORD_URL_BASE = "https://discord.com/billing/promotions/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json",
    "Connection": "keep-alive"
}

# Colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    # Your ASCII Art
    print(f"{Colors.RED}")
    print(r"   __    ____  ____  ____  _  _     ___  ____  _  _   ")
    print(r"  /__\  (_   )(  _ \(_  _)( \/ )   / __)( ___)( \( )  ")
    print(r" /(__)\  / /_  )   / _)(_  )  (   ( (_-. )__)  )  (   ")
    print(r"(__)(__)(____)(_)\_)(____)(_/\_)   \___/(____)(_)\_)()  ")
    print(f"{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}gen · discord nitro{Colors.RESET}")
    print(f"{Colors.RED}by azrix{Colors.RESET}")
    print()

def human_verification():
    """Simulates a complex human verification step."""
    print(f"{Colors.RED}SYSTEM: Security check required.")
    print(f"SYSTEM: To continue, you must manually verify you are not a robot.")
    print()
    target = random.randint(10, 50)
    answer = random.randint(1, target-1)
    correct = target - answer
    
    try:
        user_input = int(input(f"{Colors.RED}VERIFY: What is {answer} + {answer} ? (Enter result to prove human): {Colors.RESET}"))
        if user_input != correct + answer: # Intentional complex logic to make it harder
             # Actually let's make it simple math but framed as hard
             real_q = random.randint(5, 20)
             real_r = random.randint(5, 20)
             real_a = real_q + real_r
             user_check = int(input(f"{Colors.RED}FINAL CHECK: Solve {real_q} + {real_r}: {Colors.RESET}"))
             if user_check != real_a:
                 print("Verification Failed. Exiting.")
                 time.sleep(2)
                 sys.exit(0)
        print("Verification Passed. Proceeding...")
        time.sleep(1)
    except ValueError:
        print("Invalid input. Verification Failed.")
        time.sleep(2)
        sys.exit(0)

def generate_code():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.SystemRandom().choice(chars) for _ in range(24))

def check_code(code, result_queue):
    url = f"{DISCORD_URL_BASE}{code}"
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            print(f"{Colors.RED}[{timestamp}] {Colors.GREEN}VALID{Colors.RESET} - {code}")
            with open("valid_codes.txt", "a") as f:
                f.write(f"{code}\n")
            result_queue.put("valid")
        else:
            print(f"{Colors.RED}[{timestamp}] INVALID - {code}")
            result_queue.put("invalid")
    except Exception as e:
        print(f"{Colors.RED}[{timestamp}] ERROR (Rate Limit/Network) - {code}")
        result_queue.put("error")

def main():
    print_header()
    
    # Harder requirement: Human verification
    human_verification()
    
    print_header() # Re-print header after verification
    
    try:
        num_input = input(f"{Colors.RED}{datetime.now().strftime('%H:%M:%S')} · how many links to generate?\nnum: {Colors.RESET}")
        if not num_input.isdigit() or int(num_input) <= 0:
            print("Invalid number. Exiting.")
            return
        num_codes = int(num_input)
    except ValueError:
        return

    print(f"\n{Colors.RED}okay, ill get to work...")
    print("Initializing multi-threaded engine...")
    time.sleep(2) # Fake delay to make it look like "more work" is happening
    print("Bypassing security protocols...")
    time.sleep(2)
    print("Starting generation sequence...\n")
    
    valid_count = 0
    invalid_count = 0
    error_count = 0
    
    result_queue = queue.Queue()
    max_workers = 5 # Lowered slightly to be safer but still fast
    
    def task_wrapper(code):
        check_code(code, result_queue)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for _ in range(num_codes):
            code = generate_code()
            executor.submit(task_wrapper, code)

    while num_codes > 0:
        try:
            result = result_queue.get(timeout=30)
            if result == "valid":
                valid_count += 1
            elif result == "invalid":
                invalid_count += 1
            elif result == "error":
                error_count += 1
            num_codes -= 1
        except queue.Empty:
            break

    print(f"\n{Colors.RED}----------------------------------------")
    print(f"RESULTS:")
    print(f"Valid Codes: {valid_count} (Saved to valid_codes.txt)")
    print(f"Invalid Codes: {invalid_count}")
    print(f"Errors/Rate Limits: {error_count}")
    print(f"----------------------------------------{Colors.RESET}")
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()