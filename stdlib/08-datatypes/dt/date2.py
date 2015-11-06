#!/usr/local/bin/python


from datetime import datetime
import sys

print len(sys.argv)


try:
  datetime.datetime.strptime(date_text, '%Y-%m-%d')
except ValueError:
  raise ValueError("Incorrect data format, should be YYYY-MM-DD")


bday=datetime.datetime.strptime('09-13-1973', '%m-%d-%Y')
