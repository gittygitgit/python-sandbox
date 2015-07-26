#!/usr/bin/python
import sys
import subprocess
import telnetlib


def main():
  fname='foo.txt'
  hostname='localhost'
  ports_good=[]
  ports_bad=[]
  portString=''
  if len(sys.argv) > 2:
    portString=sys.argv[2]
  if len(sys.argv) > 1: 
    hostname=sys.argv[1]
  con_rqst=ConnectivityRequest(hostname,portString)
  print 'Executing with args [host: {0}, port(s): {1}]'.format(con_rqst.hostname, con_rqst.ports)
  con_rqst.execute() 



def ping(addr):
  try:
    if 0==subprocess.check_call(["ping", addr, "-n", "1"], stdout=subprocess.PIPE):
      return True
  except subprocess.CalledProcessError:
    return False

def telnet(hostname, p):
  tn=None 
  try:
    timeout=2
    tn = telnetlib.Telnet(hostname, p, timeout)
    tn.open(hostname, p)
    return True
  except:
      return False
  finally:
    if tn != None:
      tn.close()


class ConnectivityRequest:
  ports=None

  def __init__ (self, hostname, portString):
    self.hostname=hostname
    self.ports=self.add(portString)
    print self.ports

  def add(self, portString):
    rangeIndex=-1
    rangeStart, rangeStop=-1,-1
    tokens=portString.split(',')
    portList=[] 
    for token in tokens:
      print token
      ranges=token.split('-')

      if len(ranges) > 1:
        rangeStart=int(ranges[0])
        rangeEnd=int(ranges[1])
        r=range(rangeStart,rangeEnd+1)
        for i in r:
          portList.append(i)
      else:
        portList.append(int(token))
    print portList  
    portSet=set(portList)     
    print portSet
    l=list(portSet)
    l.sort()
    return l

  def execute(self):
    print "executing connectivity test"
    print "{:15}{:10}{:5}  {:20}".format('hostname','test','port','result')
    print "{:15}{:10}{:5}  {:20}".format(self.hostname,'ping','','PASS' if ping(self.hostname) else 'FAIL')
    
    for p in self.ports:
      print "{:15}{:10}{:>5}  {:20}".format(self.hostname,'connect',p,'PASS' if telnet(self.hostname, p) else 'FAIL')
"""
def printResults():
  print 'Good: {0}'.format(len(ports_good))
  print 'Bad: {0}'.format(len(ports_bad))

def printResults2():
  print 'Good: {0}'.format(len(ports_good))
  print 'Bad: {0}'.format(len(ports_bad))
"""
"""
hosts=[]
with open(fname, 'r') as fh:
  for line in fh:
    hosts.append(line.strip())
"""
#  hosts = fh.readlines()


if __name__ == "__main__":
  main()
