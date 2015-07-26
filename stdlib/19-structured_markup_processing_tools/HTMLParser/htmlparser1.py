#!/usr/bin/python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print "Encountered the beginning of a %s tag" % tag

  def handle_endtag(self, tag):
    print "Encountered the end of a %s tag" % tag

hp=MyHTMLParser()

html='<li class="right" ><a href="../modindex.html" title="Global Module Index" accesskey="M">modules</a></li>'
hp.feed(html)

