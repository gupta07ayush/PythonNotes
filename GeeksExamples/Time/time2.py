# Current Time
from datetime import datetime

now = datetime.now()
print(now)


# strftime() method is used to create a string representing the current time.
only_time = now.strftime("%H:%M:%S")
print(only_time)



# Method 2

from datetime import datetime
 
# Time object containing
# the current time.
time = datetime.now().time()
print("Current Time =", time)





# Method 3 using time module
import time
x = time.localtime()
print(x)

currentTime = time.strftime("%H:%M:%S")
print(currentTime)