import math
def is_prime(n):
  """ code taken from http://stackoverflow.com/questions/18833759/python-prime-number-checker """
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

count = 0
num = 1
while True:
  num += 1
  if is_prime(num):
    count += 1
    if count >= 10001:
      print num
      break