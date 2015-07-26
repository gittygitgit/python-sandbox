def isPalindrome(n):
  
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False
  
  
arg0=range(999,99,-1)
arg1=range(999,99,-1)

parm1, parm2=0,0
result=0



for a0 in arg0:
  for a1 in arg1:
    foo=a0*a1
    if (isPalindrome(foo)):
      if foo > result:
        result, parm1,parm2=foo,a0,a1 
        		

print parm1
print parm2
print result