def find_factors(num):
  '''
  10 -> [1,2,5,10]
  11 -> [1,11]
  111 -> [1,3,37,111]
  '''
  factors = []
  i = 1
  while (i <= num):
    if (num % i == 0):
      factors.append(i)
    i += 1
  return factors

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(57))

