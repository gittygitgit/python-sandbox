divisors=range(20,10,-1)


def isEvenlyDivisible(n):
  for i in divisors:
    if not n % i == 0:
      return False
  return True


  
i=10000000
result=0
while i < 15000000:
  if isEvenlyDivisible(i):
    result=i
    break
  i = i + 1
  



def divisibleBy(n):
  if n == 1:
    return 1
  else:
    step=divisibleBy(n-1)
    number=0
	found=
	
	
print divisibleBy(3)