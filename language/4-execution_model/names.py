#!/usr/bin/python

# What is a name?
# Something defined in a particular namespace
# An object 

# Why names?
# Provide a handle by which to access objects

# How is a name used?
# It is found in program text.

# What is the meaning of a name?
# The binding between an object and the innermost block containing it's definition

# What is a block?
# A piece of code that is executed as a unit (atomically)
# A block is executed in an execution frame

# What kinds of blocks are there?
# modules, function bodies, class definitions, script files, strings passed to eval and exec functions.

# What is an execution frame?
# A context within which a block executes containing information about how and where execution continues after a block is finished executing

# What is the scope of a name?
# The block and all blocks 

# What is meant by a name being resolved?
# The object to which the name refers is identified and invoked

# What is a namespace?
# A scope within which names are defined

# Why namespaces?
# To provide a container within which certain names are valid

# How are namespaces manifest?
# Certain namespaces are always available (global namespace)
# Others are available at other times

# What determines how a name is resolved?
# The nearest enclosing block within which the name is bound

# What is a scope?
# Defines the visibility of a name within a block

# What is the scope of a name?
# For names defined in a function block, the scope includes the block and any blocks contained within the defining one
# Names bound at a module level are considered global

# What is a global variable?
# TODO

# What if a name is redefined in a subblock?
# Then the scope of the original name binding is limited to blocks above

# How are names bound?
# Parameters to functions
# Import statements
# Class and function defs

# Why are certain names named starting with __?
# http://www.python.org/dev/peps/pep-0008/

# print names available in main module
print dir()


