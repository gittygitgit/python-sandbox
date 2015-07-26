#!/usr/bin/python

print "horse".capitalize() # Horse
print "ABCD".lower() # print abcd
print "hello".upper() # prints "HELLO"
print "   hello   ".strip() # prints "hello"
print "   hello   ".strip('h o') # prints "ell"
print "    hello".lstrip() # prints 'hello'
print "    hello".lstrip("h") # prints '    hello'
print "    hello".lstrip('h ') # prints 'ello'
print "hello   ".rstrip() # prints 'hello'
print "hello   ".rstrip('o') # prints 'hell'
print "testing  ".center(40,'_') # keeps the whitespace
print "3\t2\t".expandtabs(5) # \t is a tab
print " test".ljust(10,"*")
print " testing".ljust(4,"*") # returns original string
print "hello".replace("l","p",1) # returns "heplo"
print "123".zfill(10) # returns "0000000123"
print "test".encode('base64') # returns 'dGVzdA==\n'
print "dGVzdA==\n".decode('base64') # returns "test"

 
print "horse".endswith("se") # prints True
print "horse".startswith("ho") # prints True
print "horse".startswith("ho", 1) # prints False
print "abracadabra".endswith("bracadabra",2) # prints False
print "abracadabra".endswith("bracadabra",1) # prints True
print "a234".isalnum() # True
print "23432".isalnum() # True
print "234234".isalpha() # False
print "asdfasdf".isalpha() # True
print "sdfsdf".isdigit() # False
print "2423442334".isdigit() # True
print "\t   \t ".isspace() # True
print " TSDTSS".isupper() # True

print "abracadabra".find("bra") # prints 1
print "abracadabra".find("bra",4) # prints 8
print "abracadabra".rfind("ab",0) # prints 7
print "abracadabra".rfind("ab",0, 6) # prints 0

print "Cat on a {0} tin {1}".format("hot", "roof")

print "abracadabra".partition("b") # returns 3-tuple ("a","b","racadabra")
print "abracadabra".rpartition("b") # returns 3-tuple ("abracada","b","ra")
print "abracadabra".split("a") # returns ['','br','c','d','br,'']
print "abracadabra".split("a",2) # returns ['','br','cadabra']
print "abracadabra".rsplit("a") # returns ['','br','c','d','br,'']
print "abracadabra".rsplit("a",2) # returns ['abracad','br','']
print "This is a paragraph\nand this is the second line\nfinally the third.".splitlines() # prints a list containing three lines, w/o the line feeds
print "This is a paragraph\nand this is the second line\nfinally the third.".splitlines(True) # prints a list containing three lines, with the line feeds

print "abracadabra".partition("b") # returns 3-tuple ("a","b","racadabra")
print "abracadabra".rpartition("b") # returns 3-tuple ("abracada","b","ra")
print "~".join(["234sdf","2ffff","2222e"]) # prints 234sdf~2ffff~2222e

