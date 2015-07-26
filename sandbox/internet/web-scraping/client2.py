#!/usr/bin/python
import urllib2
import urllib
data = {}
data['s'] = 'NDAQ'
url_values = urllib.urlencode(data)
print url_values  
url = 'http://finance.yahoo.com/q'
full_url = url + '?' + url_values
# return a file-like object...actually a socket wrapper 
f = urllib2.urlopen(full_url)
data=f.read()

print data

# Compare url requested and url received
print "Original: " + full_url + ", actual: " + f.geturl()

# How do you get response information?
f.info()
print f.info()

