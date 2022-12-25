def isPrime(target):
  if target == 0 or target == 1:
    return False
  else:
    for i in range(2, target, 1):
      if target % i == 0:
        return False
    return True

# Compute the next prime number larger than 2^j
primes = []
for j in range(10,31):
  for i in range(2**j, 2**32):
    if isPrime(i): 
      print(i)
      primes.append(i)
      break
print(primes)