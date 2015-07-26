#!/usr/bin/python
"""
datetime
"""
from datetime import datetime

dt=datetime.today()
print dt.year
print dt.month
print dt.day
print dt.hour
print dt.minute
print dt.second
print dt.microsecond
print dt.tzinfo

d=dt.date() # date obj having year, month and day from dt
t=dt.time() # time obj having hour, min, etc. from dt

dt2=dt.replace(year=1900, month=12)
print dt2.weekday()
print dt2.isoweekday() # monday is 1
print dt2.strftime("%A, %d. %B %Y %I:%M%p")
'''
The datetime module contains several types:
date
time
datetime
timedelta
tzinfo

datetime extends date
'''


'''
Creating dates from strings
'''
bday=datetime.datetime.strptime('09-13-1973', '%m-%d-%Y')


'''
timedelta represents time between datetimes
'''


