'''
accepts a list and a nunber and returns the element at whatever index is the
number in the list. if the number is negative, the nth element from the end is
returned.
you can assume that number will always be between the negative value of the
list length, and the list length minus 1
'''

def nth(arr, idx):
  if idx >= 0:
    return arr[idx]
  return arr[idx + len(arr)]

print(nth([1,2,3,4,5,6,7,8,9], 1))
print(nth([1,2,3,4,5,6,7,8,9], 5))

