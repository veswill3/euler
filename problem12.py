import math
def factors(n):
    # from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    # which also provides a good explination of how it works
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

# starting values
x = 1
triangular_num = 1

# try each triangular number in turn
while len(factors(triangular_num)) < 500:
    x += 1
    triangular_num += x

print triangular_num