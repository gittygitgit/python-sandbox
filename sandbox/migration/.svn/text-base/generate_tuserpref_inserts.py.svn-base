#!/usr/bin/python
"""
Import legacy FBMS user preferences into new data model

"""
import string
from preference_codecs import *
from constants import *
import inspect
import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("Starting...")
f=open('../out/badge_to_uid.txt', 'r')

# build badge:tUser UserId mapping
badgeUidMap={}
for l in f:
  t=l.split(',')
  badge=t[0]
  uid=t[1].rstrip()
  badgeUidMap[badge]=uid

f.close()
# build legacy pref:pref_uid mapping
prefMap={'TemplHnd':2,'TemplAcc':3,'TemplAgy':6,'TemplCtr':7,'Contra':4,'CustAcct':8,'Instruction':9,'CMTA':10,'HouseNum':11,'FBNum':12,'MultAcct':13,'SuppID':14,'Firm':15,'Branch':16,'Symbol':0,'Quantity':17,'MMBadge':18,'DefaultAccTemplate':19,'DefaultHandTemplate':20,'DefaultAgencyTemplate':21,'DefaultContraTemplate':22}
#prefMap={'TemplHnd':2,'TemplAcc':3,'TemplAgy':6,'TemplCtr':7}

f=open('../sybase/02202013/bcp.PROFILES', 'r')

# Unique number of preference records without an associated user
badgesWithoutUid=set()
# Unique number of badges referenced in the profile file
totalBadges=set()
# 
userPrefMap={}

def isBadgeActive(badge):
  return badgeUidMap.has_key(badge)

def isForPrefType(prefTypeStr, prefType):
  return prefTypeStr.startswith(prefType)

def isToBeSkipped(row):
  return row.type not in prefMap 


class Row:
  
  TOKEN='|'
  EMPTY_VALUE='`'
  def __init__(self, row):
    toks=row.split(Row.TOKEN, 2)
    self.badge=toks[0]
    self.type=toks[1]
    self.isGroupPref='_' in self.type
    self.group=None
    if self.isGroupPref:
      preftype=self.type[0:self.type.find('_')]
      group=self.type[self.type.find('_')+1:]
      self.type=preftype
      self.group=group
    self.value=toks[2].replace(Row.EMPTY_VALUE, '')

  def isTemplateType(self):
    return self.type.startswith('Templ')

  def __str__(self):
    return "Row [badge={0}, type={1}, group={2}, value={3}]".format(self.badge, self.type, self.group, self.value)

  def __repr__(self):
    return "Row [badge={0}, type={1}, group={2}, value={3}]".format(self.badge, self.type, self.group, self.value)

def generateSql():
  print "Generating SQL"
  sql="insert into tUserPreference(UserId, UserPreferenceValue, UserPreferenceTypeId) values (\'{userid}\', \'{value}\', \'{typeid}\');\n"
  f=open('preferences.sql', 'w')
  
  for badge, prefs in userPrefMap.iteritems():
    print "SQL for badge " + badge + "..." 
    for type, pref in prefs.iteritems():
      print sql.format(userid=str(badgeUidMap[badge]),value=pref.formatForInsert(), typeid=prefMap[type]) 
      f.write(sql.format(userid=str(badgeUidMap[badge]),value=pref.formatForInsert(), typeid=prefMap[type])) 
  f.close()
'''
print "There are {0} total badges having preferences, {1} of which lack user accounts".format(len(totalBadges),len(badgesWithoutUid))
print "Orphan badges: {0}".format(badgesWithoutUid)
print userPrefMap
fPrefOrphan.close()
'''

def getBadgeEntry(row):
  if row.badge not in userPrefMap:
    print "Adding badge entry [badge=" + row.badge + "]"
    userPrefMap[row.badge]={}

  return userPrefMap[row.badge]

'''
{badge:{preftype:Preference}}


'''
def processRow(row):
  if isToBeSkipped(row):
    #print "Skipping row [row=" + str(row) + "]"
    return 

  print "processing row [row=" + str(row) + "]"
  try:
    badgeEntry=getBadgeEntry(row)
    if row.type not in badgeEntry:
      print "Adding preference type entry [type=" + row.type + "]"
      if row.isTemplateType():
        
        t=TemplatePreference(row)
        print("hello")
        badgeEntry[row.type]=t
        return
      elif row.isGroupPref:
        badgeEntry[row.type]=GroupedPreference(row)
	return
      else:
        badgeEntry[row.type]=SimplePreference(row)
	return
    else:
	prefTypeEntry=badgeEntry[row.type]
        prefTypeEntry.add(row)
  except KeyError as ke:
    print "keyerror"
    badgesWithoutUid.add(badge)
  except ValueError as ve:
    print "Bad record"
  finally:
    pass

fPrefOrphan=open('../out/prefOrphan.txt', 'w')

# process each row in source file
for r in f:
  row=Row(r)
  totalBadges.add(row.badge)
  #if row.badge == 'B030' and isBadgeActive(row.badge): 
  #if row.badge in ['B001','B002','B068','B066', 'B067', 'B065','B504','B505', 'B503', 'B507','B508','B509','B539'] and isBadgeActive(row.badge):

  if isBadgeActive(row.badge): 
    processRow(row)
  else:
    #fPrefOrphan.write(row)
    #print "No user...skipping row"
    pass

generateSql()

f.close()
