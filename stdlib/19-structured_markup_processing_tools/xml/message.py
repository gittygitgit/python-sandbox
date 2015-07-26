#!/usr/bin/python

class Message:
  def __init__(self, node):
    messageGroup = node.get('message-group');
    messageId = node.get('message-id');

    self.msgKey = int(messageId) << 16 | int(messageGroup); 
    self.name=node.get('id'); 

  def __repr__(self):
    return 'msgKey: %s, name: %s' % (self.msgKey, self.name)
