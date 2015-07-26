#!/usr/bin/python

import collections
import string
"""
Generates SQL insert statements for migrating existing FBMS users into new FBMS persistent store.
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
#print accounts.values()

od=collections.OrderedDict(sorted(accounts.items()))
print od

template_sql="insert into tUser(Username, DisplayName, Badge, IsBoothUser, Firm, IsQccTrader, IsCash, Company) values (\'$username\', \'$displayname\', \'$badge\', 0, \'$firm\', 0, 0, \'$company\');\n"

def genInsert(user):
  print user
  insert=string.Template(template_sql)
  return insert.substitute(username=user.username, displayname=user.fullname, badge=user.badge, firm=user.firmcode, company=user.firmname)

inserts=map(genInsert, od.values())
print inserts 



fileInserts=open('insert_tUsers.sql', 'w')
fileInserts.writelines(inserts)

