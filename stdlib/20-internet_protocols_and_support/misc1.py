#!/usr/bin/python

import urllib2 as urlmodule
from pprint import pprint as pp
url = "http://www.yahoo.com"
u = urlmodule.urlopen(url)
meta = u.info()
pp(meta.headers)
