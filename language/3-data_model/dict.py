#!/usr/bin/env python3
  
# Dictionaries are different from some other sequence-types because they are indexed by key.
# Dictionary keys must be immutable

tel={'mike':'267-815-1548', 'mike-old':'215-990-3899'}
print("Dictionary {} contains {} entries.".format(tel,len(tel)))

# Entries are accessed via key.
print(tel['mike'])
print(tel['mike-old'])

# dict constructor
# this format only works for keys that are valid identifiers
d=dict(one=1,two=2)

# list of tuples
d=dict([(1,"one"),(2,"two")])

d[1]="ooooooone"
print(d[1])

del d[1]

print(1 in d)# returns False
print(2 in d)# True

print(1 not in d) # returns True

d[3]="three"

for k in d.keys():
  print(k)


# there's also a built-in iter function
i=iter(d)

try:
  while True:
    foo=i.next()
    print("key={:d}, value={:s}".format(foo,d[foo]))
except StopIteration as si:
  print("done")


print(d)
print(d.has_key(2))
print(d.has_key(5))# False

# list of dictionary entries as tuples
for i in d.items():
  print(i)

# clear dictionary
d.clear()
