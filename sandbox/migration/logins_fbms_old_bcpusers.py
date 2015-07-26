#!/usr/bin/python

f=open('sybase/02202013/bcp.USERS', 'r')
outpath="foo.txt"
fOut=open(outpath, 'w')
accounts=[]
for l in f:
  t=l.split('|')
  if t[0][0]=='B' and not(t[9].startswith('TEST')):
    print t[0]
    print t[9]
    #fOut.write(t[0]+'\n')
    accounts.append(t[0])

accounts.sort()
for a in accounts:
  fOut.write(a + "\n")
