import mymath

input1=13195
primes=[]

i=0
while i < input1:
  if mymath.isPrime(i):
    primes.append(i)
  i = i + 1

print primes