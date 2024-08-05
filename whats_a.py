import pywhatkit as pyw
from datetime import datetime
import time

# Get the current time
now = datetime.now()
hour = now.hour
minute = now.minute

# Print the scheduled time for verification
print(f"Scheduling message for {hour}:{minute}...")

try:
    # Send a WhatsApp message
    # Note: pywhatkit schedules messages a few seconds in advance
    pyw.sendwhatmsg('+918082520347', 'Welcome to wscubetech', hour, minute + 1)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

# Optional: Add a small sleep to ensure the script completes
time.sleep(10)
