import mymath
val=13195

def getPrimes(foo):
  i=1
  primes=[]
  while i < foo:
    if mymath.isPrime(i):
      #print i
      primes.append(i)
    i = i + 1
  return primes
 

def getPrimeFactors(foo, factors):
  print "Finding prime factors for " + str(foo)
  
  largestPrimeCandidate=int(foo**.5)+1
  print "Largest prime candidate=" + str(largestPrimeCandidate)
  
  #raw_input("Press any key to continue")
  primes=getPrimes(largestPrimeCandidate)
  print "here"
  primes.reverse()
  for p in primes:
    if foo % p == 0:
      print "Prime factor found: " + str(p)
      factors.append(p)
      getPrimeFactors(foo/p, factors)
      break
    #else:
      #print str(p) + " is not a factor"	   

factors=[]
#getPrimeFactors(13195, factors)
getPrimeFactors(600851475143, factors)
 
print factors
 


  
 

