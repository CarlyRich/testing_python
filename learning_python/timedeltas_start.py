#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print ("today's date and time is:", str(now))


# print today's date one year from now
print("one year from now will be", str(now + timedelta(days=365)))


# create a timedelta that uses more than one argument
print("in 4 months, 3 weeks and 2 days from now it is CHRISTMAS", str(now + timedelta(weeks=19, days=2)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("one week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
    print ("April Fool's day already happened! %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)
time_to_afd = afd - today
print ("It is", time_to_afd.days, "days til April Fool's Day!")


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

