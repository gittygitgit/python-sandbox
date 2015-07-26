#!/usr/bin/python
"""
What is yield?
A mechanism that enables creating generator functions

What is a generator function?
A function which returns an iterator

Why generator functions?
Allows you to create a function which behaves like an iterator and can be used in loops
Generator-provided values are only loaded into memory on demand
Provides a shortcut to implementing the iterator api

"""
# Build and return a list
def firstn(n):
  num, nums = 0, []
  while num < n:
    nums.append(num)
    num += 1
  return nums

l=firstn(1000000)
print len(l)
sum_of_first_n = sum(l)
print sum_of_first_n

class firstn(object):
  def __init__(self, n):
    self.n = n
    self.num, self.nums = 0, []
 
  def __iter__(self):
    return self
 
  def next(self):
    if self.num < self.n:
      cur, self.num = self.num, self.num+1
      return cur
    else:
      raise StopIteration()

sum_of_first_n = sum(firstn(1000000))
print sum_of_first_n

# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print sum_of_first_n


