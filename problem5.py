num = 20
while True:
  nope = False
  for i in range(20, 2, -1):
    if num % i != 0:
      nope = True
      break

  if nope:
    num += 20 # we know its gotta be divisible by 20
  else:
    break

print num