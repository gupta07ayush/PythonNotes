# Python program to convert time from 12 hour to 24 hour format
from datetime import datetime

def convert(time):
    # parse the time string into a datetime object
    t = datetime.strptime(time, '%I:%M:%S %p')
    return t.strftime('%H:%M:%S')
print(convert('11:21:30 PM'))  # Output: '23:21:30'
print(convert('12:12:20 AM'))  # Output: '00:12:20'

