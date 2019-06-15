'''
accepts two lists of varying lengths. first list consists of keys and the
second one consists of values. should return a dictionary created from keys and
values. if not enough values, remaning keys should have a value of null. if
there not enough keys, just ignore the remaning values.
'''
def two_list_dictionary(keys, values):
  collection = {}

  for idx, val in enumerate(keys):
    if idx < len(values):
      collection[keys[idx]] = values[idx]
    else:
      collection[keys[idx]] = None

  return collection

print(two_list_dictionary(["one","two","three"], [1,2,3]))
