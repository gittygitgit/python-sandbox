#!/usr/bin/python

import xlwt
import collections
"""
Generates an excel spreadsheet containing user info for users in the current FBMS bcp.USERS table.
"""
class User:
  def __init__(self, raw):
    t=raw.split('|')

    self.username=t[0]
    self.badge=t[2]
    self.firmcode=t[3]
    self.fullname=t[9]
    self.firmname=t[10]

  def __repr__(self):
    return "username=" + self.username + ", badge=" + self.badge + ", firmcode=" + self.firmcode + ", fullname=" + self.fullname + ", firmname=" + self.firmname

wb=xlwt.Workbook()
ws=wb.add_sheet('New AD accounts')



f=open('sybase/02202013/bcp.USERS', 'r')
accounts={}
for l in f:
  t=l.split('|')
  if t[0][0]=='B':
    uname=t[0]
    accounts[uname]=User(l)



#					accounts.sort()
#					for a in accounts:
#					  fOut.write(a + "\n")
print accounts.values()

od=collections.OrderedDict(sorted(accounts.items()))
print od

row=0
col=0
for k, v in od.iteritems():
  print k, v
  ws.write(row, col, v.username)
  col+=1
  ws.write(row, col, v.badge)
  col+=1
  ws.write(row, col, v.firmcode)
  col+=1
  ws.write(row, col, v.firmname)
  col+=1
  ws.write(row, col, v.fullname)
  col=0
  row+=1


wb.save('new_fbms_ad_accounts.xls')
