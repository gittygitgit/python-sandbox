#!/usr/bin/python
'''
files objects can be created manually, and may also be returned from various calls.

files are created manually with the built in open method.
'''

f=open('names.txt')

content=f.read() # read content into memory
content2=f.read(10) # read 10 bytes into memory

''' 
invoking read moves an internal pointer to the current position forward

once read is invoked and EOD hit, read won't return anything more

the file position can be reset using seek.  

To set the position to the beginning of the file, seek(0)

To retrieve the file position, f.tell() 
'''


