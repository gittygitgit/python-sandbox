#!/usr/bin/python
from myparser import MyParse
import httplib

site = "www.yahoo.com"
file_loc = "/index.html"
conn = httplib.HTTPConnection(site, 80, False)
conn.request("GET", file_loc)
r1 = conn.getresponse()
#copy response to variable because reading clears it
data = r1.read()
t = MyParse()
t.feed(data) 
