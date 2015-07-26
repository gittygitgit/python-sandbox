#!/usr/bin/python

from lxml import etree
import sys
import codecs
import traceback
#with open('foo.html', 'r', encoding='latin-1') as f:
#with codecs.open('foo.html', 'r', encoding='latin-1') as f:
with codecs.open('foo.html', 'r', encoding='utf-8') as f:
  html=f.read()

  print(html[5300:5400]) 
  print(html[5328:5332]) 
  print(html[5348:5352]) 
print("---------")
'''
s=html[5300:5400]
print s
decoded=s.decode('latin-1')
print "decoded"
print decoded

htmlEncoded=html.encode('utf-8')
print htmlEncoded
'''
parser=etree.XMLParser(encoding='latin-1')
print parser
try:
   
  tree = etree.parse(html, parser=parser)
except IOError as ioe:
  print "Heard IOError"
  print ioe
  exc_type, exc_value, exc_traceback = sys.exc_info()
  print("1")
  traceback.print_tb(exc_traceback)
  print("2")
  traceback.print_exception(exc_type, exc_value, exc_traceback)
#print etree.tostring(tree)
