#!/usr/bin/python

import xml.etree.ElementTree as ET
import urllib2
import argparse
import re

parser = argparse.ArgumentParser(description="Get a realtime quote.")
parser.add_argument("quote")
args=parser.parse_args()

print args.quote
url = "http://finance.yahoo.com/q?s={0}".format(args.quote)
response = urllib2.urlopen(url)

html = response.read()
m=re.search("(<span class=\"time_rtq_ticker\">)<span.*?>(.*?)(</span>)", html)
print m.group(2)

