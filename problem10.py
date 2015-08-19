import math
def is_prime(n):
  """ code taken from http://stackoverflow.com/questions/18833759/python-prime-number-checker """
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

sum = 2 # account for 2 since we skip it in the loop below
for i in range(3, 2000000, 2): # count by 2's since even numbers are not prime except 2
  if is_prime(i):
    sum += i

print sum