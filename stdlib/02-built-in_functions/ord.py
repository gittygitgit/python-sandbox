#!/usr/bin/python
"""
ord
the inverse of chr

returns the unicode code if the arg is a unicode object, otherwise the byte value when the arg is an 8-bit string
"""
ord('f') # 102
ord('F') # 70

ord(u'\u2020') # 8224
