
import pyautogui
import time
import sys
import random

# --- Configuration ---
# Interval range (in seconds) to wait before pressing the key.
# Using a range makes the timing less predictable.
MIN_INTERVAL_SECONDS = 200  # 3 minutes 20 seconds
MAX_INTERVAL_SECONDS = 280  # 4 minutes 40 seconds
# Default Teams idle timeout is 5 minutes (300 seconds)

# Key to press. 'shift', 'ctrl', 'alt', 'cmd' (on Mac) are modifier keys.
# 'f15' or 'f16' are often good choices on Mac if available, as they rarely interfere.
# Avoid keys that type characters or trigger major actions.
KEY_TO_PRESS = 'shift'

# --- Main Loop ---
print("--- Teams Activity Keeper ---")
print(f"[*] Pressing the '{KEY_TO_PRESS}' key every {MIN_INTERVAL_SECONDS}-{MAX_INTERVAL_SECONDS} seconds.")
print("[*] This script runs in the foreground of the terminal.")
print("[*] To stop, press Ctrl+C in this terminal window.")
print("---------------------------")

# Disable pyautogui's fail-safe mechanism (moving mouse to corner to stop)
# Only disable if you are sure, otherwise it's a safety feature.
# pyautogui.FAILSAFE = False

try:
    while True:
        # 1. Choose a random wait time within the defined interval
        wait_time = random.uniform(MIN_INTERVAL_SECONDS, MAX_INTERVAL_SECONDS)
        
        # 2. Wait for the calculated time
        # Print sleep time if you want verbose output
        # print(f"[*] Waiting for {wait_time:.2f} seconds...")
        time.sleep(wait_time)

        # 3. Press the specified key
        pyautogui.press(KEY_TO_PRESS)
        # Print confirmation if you want verbose output
        # print(f"[*] '{KEY_TO_PRESS}' key pressed at {time.strftime('%H:%M:%S')}")

except KeyboardInterrupt:
    print("\n[*] Script stopped by user (Ctrl+C). Exiting.")
    sys.exit(0)
except Exception as e:
    print(f"\n[!] An error occurred: {e}")
    print("[!] Please ensure necessary permissions are granted (e.g., Accessibility on macOS).")
    sys.exit(1)