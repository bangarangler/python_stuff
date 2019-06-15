'''
take list of numbers as its argument and return the two highest numbers within
the list.  returned value should be a list in the format [second oldest age,
oldest age]
'''

def two_oldests(ages):
  return sorted(ages)[-2:]

print(two_oldests([1,2,3,4,5,6,7,8,9]))
