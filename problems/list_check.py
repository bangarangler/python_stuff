def list_check(vals):
  '''accepts a list and returns True if each value in the list is a list'''
  return all(type(l) == list for l in vals)

print(list_check((1,2,3))


