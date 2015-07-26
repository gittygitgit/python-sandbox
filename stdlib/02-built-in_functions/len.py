#!/usr/bin/python
"""
len
"""
print 'There are {0} characters in the word \"hello\"'.format(len("hello"))
print ('There are {0} items in the list ' + [1, 2, 3, 4].__repr__()).format(len([1,2,3,4]))
print 'There are {0} items in the dictionary'.format(len({"one":1,"two":2}))


