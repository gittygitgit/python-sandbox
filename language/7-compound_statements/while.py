#!/usr/bin/python

l=[1,2,3,4,5]

"""
[1,2,3,4,5]

doInsert([1,2,3,4,5], 3, 1)

 
"""
def doInsert(l, srcIdx, tgtIdx):
  val=l[srcIdx]

  limit=srcIdx
  i=limit
  # shift
  while i > tgtIdx:
    l[i] = l[i-1]
    i -= 1

  l[tgtIdx]=val

doInsert(l, 3, 1)
print l
