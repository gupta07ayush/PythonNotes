# The most common way we use to store dates and times into a Database
# is in the form of a timestamp. When we receive a 
# date and time in form of a string before storing it into 
# a database, we convert that date and time string into a timestamp. 
# Python provides various ways of converting the data to timestamp.
# Few of them are:
# 1. Using timetuple()
# 2. Using timestamp()

# Method 1 :
# timetuple() takes two arguments:
    # string format of the date and time
    # format of the input string
# we convert date and time string into a date object
# then we use timetuple() to convert date object into tuple
# At the end we use mktime(tuple) to convert the Date tuple into a timestamp.

import time 
import datetime

string = "20/01/2020"
string2 = "24/05/2023"

print(time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple()))
print(time.mktime(datetime.datetime.strptime(string2, "%d/%m/%Y").timetuple()))

# example 2
mystring = "20/01/2020"
element = datetime.datetime.strptime(string, "%d/%m/%Y")

x = element.timetuple()
timestamp = time.mktime(x)
print(timestamp)



# Method 2 using timestamp()
#  strptime method. This method takes two arguments
# First arguments s the string format of the date and time
# Second argument is the format of the input string
# Then it returns date and time value in timestamp format and we stored this in timestamp variable.

element = datetime.datetime.strptime(mystring, "%d/%m/%Y")
timestamp = datetime.datetime.timestamp(element)
print(timestamp)