def find_special_pythagorean_triplet():
  # start counting down from 1000
  for c in range(999, 1, -1):
    # b should always be less than c to be a triplet
    for b in range(c-1, 1, -1):
      # calculate a based on the special triplet being a + b + c = 1000
      a = 1000 - c - b
      # everything should be positive, and  we dont need to check a and b's overlap
      if a < 1 or a > b:
        break
      else:
        # make sure it obeys pythagorean's law
        if a ** 2 + b ** 2 == c ** 2:
          print "a:%i, b:%i, c:%i > a*b*c = %i" % (a, b, c, (a * b * c))
          return

find_special_pythagorean_triplet()