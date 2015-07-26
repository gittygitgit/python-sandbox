#!/usr/bin/python

import urllib2
import urllib

# get resource @ http://finance.yahoo.com/q?s=JAOSX
data = {} # an empty dictionary
data['s'] = 'JAOSX' # add a dictionary entry

url_values = urllib.urlencode(data) # encode url parameters using urllib module
print url_values  
url = 'http://finance.yahoo.com/q'
full_url = url + '?' + url_values
# return a file-like object...actually a socket wrapper 
f = urllib2.urlopen(full_url)
data=f.read()

print data

# dump the resource to a file
f=open("foo.out","w") # create a file in write mode
f.writelines(data)
f.close()

# Compare url requested and url received
print "Original: " + full_url + ", actual: " + f.geturl()

# How do you get response information?
f.info()
print f.info()

