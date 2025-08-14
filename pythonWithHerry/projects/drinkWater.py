import time
from plyer import notification

#Settings → System → Notifications & actions
# Keep running the code inside this loop forever, until I manually stop it or break out of it.”

try:
 while True:
    print("Please Drink Some Water")
    notification.notify(
        title="Please Drink some Water",
        message="You need to drink some Water"
    )
    time.sleep(10)
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
