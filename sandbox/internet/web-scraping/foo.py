#!/usr/bin/python

import urllib2
import urllib

req = urllib2.Request('http://finance.yahoo.com/q')
data = {} # empty dictionary
data['s']='NDAQ'

url_values = urllib.urlencode(data)

print url_values

url = 'http://finance.yahoo.com/q'
full_url = url + '?' + url_values

print full_url
data = urllib2.urlopen(full_url)
the_page = data.read()
print the_page
