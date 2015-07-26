#!/usr/bin/python
import re
'''
Replacements
  re.sub

Finding matches
  re.search and match return an object

  findall return all matching occurrences of a pattern in string as a list of strings 

'''

'''
 why r in beginning of re pattern?
 for example: re.search(r"foo", text)
 tells python to treat the string as a raw 

 match object
 string - the string being searched
 group
   matched string within string.

 subgroup
   group broken down by parenthesised portion of pattern

 start
   the index within string where the matched group starts.

 end
   the index within string where the matched group ends
 TODO

 
'''


with open("html.txt", 'rw') as f1:
  content=f1.read()

# search for seomthing we know isn't in here
m=re.search("abcdefg", content)

# if search result evaluates False, no match was found.
if m:
  print "Found pattern"

# now we'll search for something we know is in the file
m=re.search("body", content)

