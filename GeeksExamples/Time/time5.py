# Python program to find yesterday's, today's and tomorrow's date
# datetime module helps to find the present day by using the now() or today() method
# timedelta class from datetime module helps to find the previous day date and next day date

from datetime import datetime, timedelta

# today's date
present = datetime.now()

# yesterday date
yesterday = present - timedelta(1)

# tomorrow date
tomorrow = present + timedelta(1)

print('Today', present.strftime('%d-%m-%Y'))
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Tomorrow", tomorrow.strftime('%d-%m-%Y'))