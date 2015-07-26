#!/usr/bin/python
"""


for a given range of dates
  stage tuples of current / next bus day
 
  if the current date is a business day
    if there's a current bus date already staged
      assign date to next bus date
      print tuple
      remove current date
      make next bus date current date.
    else
      assign date to current date
  else
    skip    

tradeDateMap.put("20141230", "20141231");
"""
import argparse
import sys
from datetime import date
from datetime import timedelta

parser = argparse.ArgumentParser(description="Process a range of dates.")
parser.add_argument("--start_date", help="The date to start from (format YYYYmmdd)")
parser.add_argument("end_date", help="The date to end with (format YYYYmmdd)")

args=parser.parse_args()

def parseDate(dateString):
  if len(dateString) != 8:
    sys.exit()

  try:
    year=dateString[0:4]
    month=dateString[4:6]
    day=dateString[6:8]

    d=date(int(year),int(month),int(day))
    return d

  except ValueError as ve:
    print "invalid date format"


if args.start_date:
  startDate=parseDate(args.start_date)
else:
  startDate=date.today()


endDate=parseDate(args.end_date)


def daterange(start_date, end_date):
  for n in range((end_date - start_date).days):
    yield start_date + timedelta(n)

weekends=set([5,6])
holidays=set([date(2015,1,1), date(2015,1,19), date(2015,2,16), date(2015,4,3), date(2015,5,25), date(2015,7,3), date(2015,9,7), date(2015,11,26), date(2015,12,25)])

def isBusDay(d):
  if d.weekday() not in weekends and d not in holidays:
    return True
  else:
    return False


# currentTd
# nextTd
for d in daterange(startDate, endDate):
  if isBusDay(d):
    if 'currenttd' in globals():
      nexttd = d
      currenttdStr=currenttd.strftime("%Y%m%d")
      nexttdStr=nexttd.strftime("%Y%m%d")
      print "tradeDateMap.put(\"{0}\", \"{1}\");".format(currenttd.strftime("%Y%m%d"), nexttd.strftime("%Y%m%d"))
      currenttd=nexttd 
      del nexttd
    else:
      currenttd = d 
      
