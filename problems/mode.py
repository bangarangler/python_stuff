'''
accepts a list of numbers and returns the most frequent number in the list of
numbers. you can assume that the mode will be unique
'''

def mode(collection):
  count = {val: collection.count(val) for val in collection}

  max_value = max(count.values())

  correct_index = list(count.values()).index(max_value)

  return list(count.keys())[correct_index]

print(mode([1,1,1,3,3,4,4,4,4,4,6,7,8,9,0]))
