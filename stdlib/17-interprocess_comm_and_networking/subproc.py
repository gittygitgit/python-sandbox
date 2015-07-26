#!/usr/bin/python

# What's the diff btw call and check_call?
# check_call throws CalledProcessError if the return-code is non-zero


# What is the purpose of the shell=True arg?
# Specifies that the invocation will be performed through the shell, allowing shell functionality to be utilized.

# What does Popen do?
"""
	
"""

# What is PIPE?
# indicates that a new pipe to the child process should be created.

import subprocess

# Popen(['ping', 'localhost', '-n', 1])
"""
p=subprocess.Popen(['ping', 'localhost'], stdout=subprocess.PIPE)

out, err=p.communicate()
"""

# What does communicate do?
try:
  subprocess.check_call(['ping', 'l1ocalhost', '-n', '1', '-w', '200'], stdout=subprocess.PIPE)
  print "good"
except subprocess.CalledProcessError:
  print "error"

