#!/usr/bin/python
'''

'''
import re

s="once upon a time\nthere was a princess named Fiona.\n\n"

# remove all newlines
s_no_newlines=re.sub("\n", '', s)
s_no_newlines=re.sub("[\t\n]", '', s)

