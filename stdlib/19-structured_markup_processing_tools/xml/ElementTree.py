#!/usr/bin/python
 
import xml.etree.ElementTree as ET
import message as Message

#######################################
# Generate parser file
#######################################
fname='parser.js';
f=open(fname, 'w');

f.write('var sprintf = require(\'sprintf-js\').sprintf\n');
f.write('var winston = require(\'winston\')\n');
f.write('function parse(b, l) {\n');
f.write('  var messageGroup = b.readInt16LE(0);\n');
f.write('  var messageId= b.readInt16LE(2);\n');
f.write('  var msgKey=(messageId << 16) | messageGroup;\n');

f.write('  switch(msgKey) {\n');


tree=ET.parse('directdrop_messages.xml')
root = tree.getroot()

msgs=root.findall('./messages/*');
# parse all messages 

for m in msgs:
  msg=Message.Message(m)
  print msg
  f.write('    case ' + str(msg.msgKey) + ':\n')
  f.write('      winston.debug(\'' + msg.name + '\');\n')
  f.write('      l.on' + msg.name + '(b);\n')
  f.write('      break;\n')
  

f.write('    default:\n')
f.write('      winston.debug(sprintf("unknown message type [messageId=%1$s, messageGroup=%2$s, msgkey=%3$s", messageId, messageGroup, msgKey));\n')
f.write('  }\n')
f.write('}\n')

f.write('module.exports={\n')
f.write('  parse:parse\n')
f.write('}\n')
f.close()

 
#######################################
# Generate listener file
#######################################
fname='listener.js'
f=open(fname, 'w');

f.write('var Messages = require(\'./messages.js\')\n')

f.write('function Listener() {\n')
for m in msgs:
  msg=Message.Message(m)
  f.write('  this.on' + msg.name + ' = function(buf) {\n')
  f.write('    var x = new Messages.' + msg.name[:1].lower() + msg.name[1:] + '(buf);\n')
  f.write('    x.print();\n')
  f.write('  }\n')
f.write('}\n')

f.write('module.exports={\n')
f.write('  Listener: Listener\n')
f.write('}\n')
f.close()

#######################################
# Generate messages file
#######################################
fname='messages.js'
f=open(fname, 'w');

f.write('var util = require(\'util\');\n')
f.write('var BigNumber = require(\'bignumber.js\');\n')
f.write('var fn = require(\'./functions.js\');\n')
f.write('var sprintf = require(\'sprintf-js\').sprintf;\n')
f.write('var indent=\'    \';\n')

f.write('function getRecordFmt(n) {\n')
f.write('  var pad=\'\';\n')
f.write('  for (var i = 0; i < n; i++) {\n')
f.write('    pad += indent;\n')
f.write('  };\n')

f.write('  return pad + \'%1$-50s = %2$s\';\n')
f.write('}\n')

f.write('var fmt=getRecordFmt(1);\n')
f.write('var fmt2=getRecordFmt(2);\n')
f.write('var fmt3=getRecordFmt(3);\n')

refTypes={}

records=root.findall('./records/*');
for r in records:
  id = r.get('id')
  fields={}
  fieldNodes = r.findall('./fields/field')
    for n in fieldNodes:
      fields[n.get('name')] = n.get('type')
  refTypes[id] = fields;

 
def handleRef():
  print 'handleRef'

def handleField(f, name, type):
  f.write('  this.' + name + "=")
  if type == 'long':
    f.write('fn.readUInt64(buf, p);\n')
    f.write('p+=8;\n')
  elif type == 'integer':
    
  elif type == 'string':

  elif type == 'short':
 
  elif type == 'boolean':

  elif type == 'byte':

  elif type == 'char':


f.write('Messages={};\n')
for m in msgs:
  msg = Message.Message(m)
  f.write('Messages.' + msg.name[:1].lower() + msg.name[1:] + '=function(buf) {\n')
  f.write('  var p = 0;\n')
  f.write('  this.messageGroup = buf.readInt16LE(p);\n')
  f.write('  p+=2;\n')
  f.write('  this.messageId= buf.readInt16LE(p);\n')
  f.write('  p+=2;\n')

  flds = m.findall('./fields/field')
  for f in flds:
    name=f.get('name')
    type=f.get('type')
    isRef=type == None

    if !isRef:
      # this is a field
    else:
      # this is a ref field
    
    handleField(f, name, type)

