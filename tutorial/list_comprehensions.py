'''
Used to create lists.

Lists can be created using comprehensions...
- By applying a function to a separate list.
- By filtering a separate list to create a sublist.


'''

# all the following are equivilent...
l1=[x**2 for x in range(10)]
l2=map(lambda x: x**2, range(10))

l3=[]
for i in range(10):
  l3.append(i**2)


'''
Filtering a list

Apply identify function to each el in unfiltered, then perform a test
'''

unfiltered=[1,2,3,4,5,6,7]
filtered=[x for x in unfiltered if x % 2 == 0]


