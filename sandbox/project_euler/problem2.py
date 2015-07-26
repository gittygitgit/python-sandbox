i=0
sequence=[]
limit=4000000
result=0

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-2) + fib(n-1)
	
while i < 100:
  val=fib(i)
   
  if val < limit:
    sequence[i:i]=[val]
    print val
  else:
    print "done"
    break

  i = i + 1

for v in sequence:
  if v % 2 ==0:
    print "Adding " + str(v) + " to sum" 
    result=result + v
    print "New sum=" + str(result)
  else:
    print str(v) + " is not an even number"
  

print result
print sequence	
  
	
  
