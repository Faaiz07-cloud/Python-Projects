# ---------- Digital Clock ----------

# Modules
import time
from datetime import datetime
from zoneinfo import ZoneInfo

# Menu
try:
    print("\n------------- Digital Clock -------------\n")
    while True:
        Date = datetime.today().strftime('%A - %#d/%b/%Y')
        Time = datetime.now(ZoneInfo('Asia/Karachi')).strftime('%I:%M:%S %p - %Z')
        print(f"\r{Date} | {Time}", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nStopped!")