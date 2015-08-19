previousNumber = 1
nextNumber = 2
total = 0

while nextNumber < 4000000:
  # only evens
  if nextNumber % 2 == 0:
    total += nextNumber
  temp = previousNumber
  previousNumber = nextNumber
  nextNumber = temp + nextNumber

print total