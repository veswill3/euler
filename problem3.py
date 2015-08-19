import math
def is_prime(n):
  """ code taken from http://stackoverflow.com/questions/18833759/python-prime-number-checker """
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# loop backwards on every number starting at 600851475143
for i in xrange(int(math.sqrt(600851475143)) + 1, 1, -1):
  # check if the number divides into 600851475143 evenly.
  if 600851475143 % i == 0:
    # check if that number is prime
    if is_prime(i):
      print i
      break