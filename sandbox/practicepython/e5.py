#!/usr/bin/python
'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (dont worry if you cant figure this out at this point - well get to it soon)
'''
l1=raw_input("Enter a comma separated list of numbers.")
l2=raw_input("Enter another comma separated list of numbers.")

lr=[]

for i in l1.split(","):
  if i in l2:
    lr.append(i)

for i in l2.split(","):
  if i in l1:
    lr.append(i)

print set(lr)  
