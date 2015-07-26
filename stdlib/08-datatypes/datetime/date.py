#!/usr/bin/python
"""

"""
from datetime import date

d=date.today()
d=date(1973, 9, 13)
print d.year
print d.month
print d.day
print d.weekday() # day of the week where Monday is 0
print d.isoweekday() # day of the week where Monday is 1
d.strftime("%d/%m/%y")

