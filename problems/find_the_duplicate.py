'''
accepts an array of numbers containing a single duplicate. return number which
is a duplicate of None if there are no duplicates.
'''

def find_the_duplicate(arr):
  counter = {}
  for val in arr:
    if val in counter:
      counter[val] += 1
    else:
      counter[val] = 1

  for key in counter.keys():
    if counter[key] > 1:
      return int(key)



print(find_the_duplicate([1,2,2,3,4,5,6,7,8,9]))
print(find_the_duplicate([1,2,3,3,4,5,6,7,8,9]))
