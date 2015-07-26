#!/usr/bin/python
'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
s=raw_input("Enter a string.")

l=len(s)
print len(s)
isPalindrome=True
for i in range(len(s)):
  a=i
  b=len(s)-1-i

  if a < b:
    print str(a) + "|" + str(b) 
    if s[a] != s[b]:
      isPalindrome=False

if isPalindrome:
  print "This string IS a palindrome."
else:
  print "This string IS NOT a palindrome."
  

