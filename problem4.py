def is_palindrome(num):
  string = str(num)
  return string == string[::-1]

largest = 0
# count down on all 3 digit numbers
for i in range(999, 100, -1):
  for j in range(999, 100, -1):
    if is_palindrome(i * j):
      if i * j > largest:
        largest = i * j

print largest