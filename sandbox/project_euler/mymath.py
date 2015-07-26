def isPrime(num):
  # print num
  if num < 2:
    return False
  elif num == 2:
    return True
  elif not num & 1:
    return False 
  else:
    for i in range(3,int(num**.5)+1,2):
      if num % i == 0:
        return False
  return True
