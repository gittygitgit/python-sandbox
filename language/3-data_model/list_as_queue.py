#!/usr/bin/python

from collections import deque

# double endede queue
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft()

print queue.popleft()
print queue


