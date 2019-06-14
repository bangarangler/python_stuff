def remove_every_other(lst):
  '''accepts a list and returns a new list with every second value removed'''
  return [val for i, val in enumerate(lst) if i % 2 == 0]

print(remove_every_other((1,5,4,8,10,12)))

