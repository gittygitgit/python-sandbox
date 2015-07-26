#!/usr/bin/python
'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
http://www.nytimes.com
'''
import requests
from BeautifulSoup import BeautifulSoup

r=requests.get("http://www.nytimes.com")

bs=BeautifulSoup(r.text)
stories=bs.findAll("h2", {"class":"story-heading"})

for i in stories:
  if i.a:
    print i.a.text.replace("\n", " ").strip()
  else:
    print i.contents[0]



