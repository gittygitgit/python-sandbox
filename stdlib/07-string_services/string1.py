#!/usr/bin/python
import string
v="Hello|Goodbye"

print "The first character is '" + v[0] + "'"

print "The fifth through thirteenth chars are " + v[5:13]
print "The first through tenth chars are " + v[:10]

for i in v[5:10]: print i

if 'o' in v: print "got o"

i="""sadfsaf sadfas asdfsa asdf
asdfas asdf sdfa sdafsa asdfsa
asdfasdf sadf """
print i

# Always try to use the string module if possible...it's faster and more portable than other modules

s="happy birthday"
print string.find(s,"birth")
print string.count(s, "p")
print string.replace(s, "birth", "Sun")

# built-in constants
print string.uppercase

# convert between strings and tuples
L=string.split(s)
print L

print len(s)