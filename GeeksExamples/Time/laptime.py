# Create a Lap time

# The user needs to press Enter to complete each lap.
# The timer keeps counting till CTRL + C is pressed. 
# For each lap we calculate the lap time by subracting
# the current time from the total time at the end of the previous lap. 
# The time() function of the time module, returns the current epoch time in milliseconds. 

import time

start = time.time()
last = start 
lapnum = 1

print("Press ENTER to count laps.\nPress Ctrl +c to stop. ")
try:
    while True:
        #input for the enter key press
        input()
        laptime = round((time.time() - last), 2 )
        
        # Total time elapsed since the timer started
        totaltime = round((time.time() - start), 2)
        
        # Printing the lap number lap-time and total time
        print("Lap No = "+ str(lapnum))
        print("Total Time: " +str(totaltime))
        print("Lap Time: " + str(laptime))
        print("*"*20)
        
        # updating the previous total time and lap number
        last = time.time()
        lapnum += 1
        
# Stopping when ctrl + C is pressed
except KeyboardInterrupt:
    print("Done")