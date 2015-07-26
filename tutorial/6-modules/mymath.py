def isPrime(num):
  if num <= 1:
    return True
  else:
    for i in range(2,num-1):
      if num % i == 0:
        return False
  return True
