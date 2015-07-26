#!/usr/bin/python

import re

f=open("foo.out","r")
data=f.read()

mo=re.search("\<span class=\"time.*?>(<span.*?>)([0-9]*\.[0-9]*)?</span>",data)

print mo.group(2) # prints 28.36


