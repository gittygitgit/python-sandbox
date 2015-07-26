#!/usr/bin/python

import subprocess

# subprocess
# A subprocess is a process spawned by a parent process

# Popen
# Underlies the subprocess convenience functions
# Can be used directly when subprocess convenience fct's don't suffice
# executes a new child program in a new process

# Popen parameters
# args
# Can be a single string or a sequence
#   Must be executed through a shell if a single string 

#   On Unix...
#     the string is the command to execute through the shell
subprocess.Popen("ls") 
try:
  subprocess.Popen("ls -l") # fails since there's no command ls -l
except OSError as e:
  print e

subprocess.Popen("ls -l", shell=True)
subprocess.Popen(["ls"])
subprocess.Popen(["ls", "-l"]) #No need for shell=true since Popen knows how to handle properly when sequence is set
subprocess.Popen(["ls", "-l"], shell=False) # works fine 



# Shell
# ? Execute a command through the shell
# Avoid executing user-entered commands through the shell
# Defaults to False
# On unix...
#   the shell defaults to /bin/sh
# While shell is useful for taking advantage of shell features, note that
#   python has many implementations of shell-like features.
 
# call
# Returns return code
# Avoid setting stdout or stderr to PIPE, since the pipes aren't ever used in the spawning process
subprocess.call(["ls", "-l"])


# check_call
# similar to call, except only returns with zero return code, otherwise raises CalledProcessError
# see call for avoiding PIPE
subprocess.check_call("exit 1", shell=True)



# file handles

#   stdin, stdout and stderr
#     valid values
#       PIPE
#       positive integer (existing file descriptor)
#         0 - input, 1 - output, 2 - error
#       existing file object
#         /dev/pty0 - input, /dev/pty1 - output, /dev/pty2 - error

#       None (default setting)
#         handles inherited from parent
#       STDOUT - for stderr only, uses same handle for stdout and stderr


