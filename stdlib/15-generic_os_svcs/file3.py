import os

fname='./file3.txt'

# delete file
print "Performing preprocessing..."
if os.path.exists(fname):
  print "Deleting " + fname
  os.remove(fname)
  
# create file in write mode
f=open(fname, 'w')

# write content
f.write("hello there\n")
f.write("my name is mike\n")

f.close()

# open file and read contents
with open(fname, 'r') as f1:
  print f1
  for l in f1:
    print l
  
with open(fname, 'r') as f1:
  f1.read(1)