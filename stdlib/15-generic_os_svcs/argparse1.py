#!/usr/bin/python
import argparse
from datetime import date 
import sys

parser = argparse.ArgumentParser(description="Process a range of dates.")
parser.add_argument("--start_date", help="The date to start from (format YYYYmmdd)")
parser.add_argument("end_date", help="The date to end with (format YYYYmmdd)")

args=parser.parse_args()

def parseDate(dateString):
  print dateString
  if len(args.start_date) != 8:
    print "bad"
    sys.exit()
  
  try:
    year=args.start_date[0:4]
    month=args.start_date[4:6]
    day=args.start_date[6:8]

    startDate=date(int(year),int(month),int(day))
    return startDate
 
  except ValueError as ve:
    print "invalid date format"



if args.start_date:
  print "start_date"  
  startDate=parseDate(args.start_date)
else:
  start_date=date.today()


endDate=parseDate(args.end_date)
print args.end_date
