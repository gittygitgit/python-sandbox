#!/usr/bin/python
from constants import *
import abc
import logging
import re

logging.basicConfig(level=logging.DEBUG)

# Associated with a preference type
class BasePreference(object):
  __metaclass__=abc.ABCMeta
  
  def __init__(self, row):
    self.type=row.type

  '''
  Add preference info corresponding to a row in legacy PROFILE table
  '''
  @abc.abstractmethod
  def add(self, row):
    '''
    adds a new row to this preference
    a row is a single record from the profiles dump
    '''
    return

  '''
  returns string to be inserted in tUserPreference.UserPreferenceValue
  '''
  @abc.abstractmethod
  def formatForInsert(self):
    return

'''
B030|CMTA|161 = 0
B030|CMTA|005 = 1
Has a list of preferred values
'''
class SimplePreference(BasePreference):
  def __init__(self, row):
    super(SimplePreference, self).__init__(row)
    self.values=[]
    self.add(row)

  def add(self, row):
    '''
    row value format:
      B030|CMTA|161 = 0
    '''
    print "Adding simple preference [type=" + row.type + ", value=" + row.value + "]"
    print "Before [" + str(self.values) + "]"
    self.values.append(row.value[0:row.value.find(' = ')])
    print "After [" + str(self.values) + "]"

  def formatForInsert(self):
    # 161,540,999
    s=''
    isFirst=True
    for v in self.values:
      if not isFirst:
        s=s + ','
      s=s + v
      isFirst=False
    return s
'''
There are many grouped types
B558|Contra_ARUN|B558 = 0
B558|Contra_ARUN|180 = 1
Associeated with a map of groupnames to preferred value
'''
class GroupedPreference(BasePreference):
  def __init__(self, row):
    super(GroupedPreference, self).__init__(row)
    self.values={}
    self.add(row)
    self.groupSepOpen="["
    self.groupSepClose="]"

  def encodeRowValue(self,val):
    return val[0:val.find(' = ')];

  def add(self,row):
    '''
    row value forma:
      B524|Contra_TFX|B524 = 0     
    '''
    logging.debug("Adding row to grouped pref [row={0}]".format(row))
    if row.group not in self.values:
      self.values[row.group]=[]

    grouplist=self.values[row.group]
    print "Adding grouped preference [type=" + row.type + ", group=" + row.group + ", value=" + row.value + "]"
    print "Before [" + str(grouplist) + "]"
    grouplist.append(self.encodeRowValue(row.value))
    print "After [" + str(grouplist) + "]"
 
  def formatGroup(self,label, pref):
    # todo: For NL prefs, change inner braces to brackets {'DELL':['B004','234'],'AAPL':['123']}
    s="\"{label}\"".format(label=label)+ ":" + self.groupSepOpen
    isFirst=True
    for p in pref:
      if not isFirst:
        s = s + ','
      else:
        isFirst=False
      s=s + p

    s=s+self.groupSepClose
    return s

  def formatForInsert(self):
    #{"TFX":{"B524",540},...}
    s=''
    isFirst=True
    for group,pref in self.values.iteritems():
      if isFirst:
        s=s + "{"
        isFirst=False 
      else:
        s=s + ', '      
      s=s + self.formatGroup(group, pref)
    s=s + "}"
    return s

class Template:
  TOKENS_MINIMUM=36
  EMPTY='`'
  def __init__(self, val):
    logging.debug("Decoding template")
    value_tokens=val.split('|')
    numTokens=len(value_tokens)
    if numTokens < Template.TOKENS_MINIMUM:
      raise ValueError
    if value_tokens[15] in map_type:
      self.accountType=map_type[value_tokens[15]]
    self.marketMakerNumber=value_tokens[16]
    if self.marketMakerNumber:
      self.marketMakerNumber=self.marketMakerNumber.lstrip('0')
    if value_tokens[12] in map_tif:
      self.timeInForce=map_tif[value_tokens[12]]
    self.suffix=value_tokens[17]
    self.multiAccount=value_tokens[18]
    self.market=value_tokens[19]
    self.instructions=value_tokens[26]
    self.isAllOrNone=value_tokens[34]
    if self.isAllOrNone is not None:
      self.isAllOrNone=self.isAllOrNone.lower()
    self.firmMnemonic=value_tokens[0]
    self.branchCode=value_tokens[1]
    self.houseAccountNum=value_tokens[20]
    if (self.houseAccountNum):
        self.houseAccountNum=self.houseAccountNum.lstrip('0')
        self.houseAccountNum=re.sub('[A-Z]','',self.houseAccountNum)
    self.cmta=value_tokens[21]
    self.floorBrokerNum=value_tokens[23]
    self.supplementaryInfo=value_tokens[25]
    if numTokens > Template.TOKENS_MINIMUM:
      try:
        self.cust=value_tokens[36]
        self.routing=value_tokens[37]
        self.billingIndicator=value_tokens[38]
      except IndexError:
        logging.debug("Row only has {0} tokens".format(numTokens))
 
  def __repr__(self):
    return "type={1}, mm={2}, sfx={3}, mult={4}, mkt={5}, inst={6}, aon={7}, tif={8}, firm={9}, branch={10}, house={11}, cmta={12}, fbnum={13}, suppid={14}, cust={15}, bi={16}, routing={17}".format(self.accountType, self.marketMakerNumber, self.suffix, self.multiAccount, self.market, self.instructions, self.isAllOrNone, self.timeInForce, self.firmMnemonic, self.branchCode, self.houseAccountNum, self.cmta, self.floorBrokerNum, self.suppid, self.cust, self.billingIndicator, self.routing)
    
  def format(self):
    s=''
    first=True
    '''only set first to False after we've written a field'''
    for f, val in self.__dict__.iteritems():
      print first
      if not first:
        print "not first"
        s=s + ','
      s=self.formatField(s, f, val)
      if s in [',', '']: 
        first = True
        s=''
      else:
        first = False
        if s.endswith(','):
          s=s[:-1]
      print s
    return s
    

  '''If field is non-empty, append it'''
  def formatField(self, s, f, val):
    if val is not None and val != '':
      if f in ['marketMakerNumber', 'isAllOrNone', 'houseAccountNum']:  
        return s + '\"' + f + '\":' + str(val) + ''
      else:
        return s + '\"' + f + '\":\"' + str(val) + '\"'
    else:
      return s

'''
There are four template types.
A badge may have multiple instances of each type labeled with a group
'''
class TemplatePreference(GroupedPreference):
  def __init__(self, row):
    print "_init_"
    super(TemplatePreference, self).__init__(row)
    self.groupSepOpen='{'
    self.groupSepClose='}'
  
  def encodeRowValue(self,val):
    return Template(val).format();

