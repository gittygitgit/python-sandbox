#!/usr/bin/python
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
from datetime import datetime
from datetime import timedelta

def ageFromBday(dateStr):
  bd=datetime.strptime(dateStr, '%m-%d-%Y')
  today=datetime.today()

  age=(today-bd).days/365
  return age
name=raw_input("What is your name?")
print "Hi {0}!".format(name)
bdayStr=raw_input("What is your birthday [mm-dd-YYYY]?")
print ageFromBday(bdayStr)

