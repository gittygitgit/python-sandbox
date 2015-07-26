#!/usr/bin/python

# multiline
f="hello " \
"there " \
"Mike."

print f

# lines containing expressions in parentheses, square-brackets or curly
# braces can be split over multiple lines w/o using explicit line-joining
# with (\)
months=['Jan', 'Feb', 'March'
, 'April'
, 'May']

print months


