#!/usr/bin/python
"""
hasattr
"""
class Test:
  f="attr1"

t=Test()
if hasattr(t, "f"): print "instance t has attribute f" # will be printed

if hasattr(Test, "f"): print "class Test has attribute f" # will be printed

setattr(t, "f2", 100)

if hasattr(t, "f2"): print "instance t has attribute f2" # this will be printed

if hasattr(Test, "f2"): print "class Test has attribute f2" # won't be printed


