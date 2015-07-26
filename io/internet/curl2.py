#!/usr/bin/python
import urllib2
import re
import sys
from cookielib import CookieJar

url=""
request=""
html=""
# Repository for cookies
cj = CookieJar()
# Custom opener having cookie processor
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))



def onSuccessfulRequest(page):
  print "Successfully retrieved page: {0}".format(page)

def onBadCode(code):
  sys.exit("Unexpected code {0}".format(loginRequest.code))


url="https://www.pnc.com/en/personal-banking.html"
response=opener.open(url)
if response.code != 200:
  onBadCode(response.code)

onSuccessfulRequest("Login")
url="https://www.onlinebanking.pnc.com/alservlet/ValidateUserIdServlet"
response=opener.open(url, "userId=2159903899")
if response.code != 200:
  onBadCode(response.code)

onSuccessfulRequest("Submitted UID")
html=response.read()
start=html.index("<strong>Question:</strong>")
sub=html[start:start+200]
m=re.search("<td>(.*?)</td>", sub)
question=m.group(1)
answer=raw_input(question)

url="https://www.onlinebanking.pnc.com/alservlet/SigninChallengeServlet"
response=opener.open(url, "answer={0}&bindDevice=no&Continue=Continue".format(answer))
if response.code != 200:
  onBadCode(response.code)

onSuccessfulRequest("Submitted challenge")

url="https://www.onlinebanking.pnc.com/alservlet/VerifyPasswordServlet"
response=opener.open(url, "password=6025bdl73")
if response.code != 200:
  onBadCode(response.code)

onSuccessfulRequest("Submitted pw")
html=response.read()
m=re.search("<tr class=\"depAccount", html)
print m.start()

