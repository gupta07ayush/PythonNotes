# Current Time
from datetime import datetime

now = datetime.now()
print(now)


# strftime() method is used to create a string representing the current time.
only_time = now.strftime("%H:%M:%S")
print(only_time)