#!/usr/bin/python

import socket

# create a tcp socket using ipv4
srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# bind the socket to any interface on the local host, port 23000
srvsock.bind( ('', 23000) )
# start listening for connections, queue at most 5
srvsock.listen( 5 )

# endless loop
while 1:

  # on client connection, return a client socket and remote info
  clisock, (remhost, remport) = srvsock.accept()
  # receive at most 100 bytes into the buffer
  str = clisock.recv(100)
  # echo back what was sent
  clisock.send( str )
  # close client connection
  clisock.close()
