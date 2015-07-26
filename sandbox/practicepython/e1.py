#!/usr/bin/python
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
from datetime import date

name=raw_input("Enter your name:")
print "Hi {0}".format(name)
age=input("Enter your age:")
if age >= 100:
  print "{0}, you are already 100.".format(name)
else:
  today=date.today()
  year=today.year
  yearsTill100=100-age
  print "{0}, you will turn 100 in {1}".format(name, year + yearsTill100)

