# get current time
from datetime import *
x = datetime.now()

#Here you will get your current time in the format
#YYYY-MM-DD HH:MM:SS.ms
print(x)


# If you want only year use %Y
year = x.strftime("%Y")
print("Year = ", year)


#only month use %m
month = x.strftime("%m")
print("Month = ", month)


#only day use %d
day = x.strftime("%d")
print("Day= ", day)