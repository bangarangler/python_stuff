'''
accepts a collection, a value, and an optional starting index. should return
True if value exists in the collection when we search starting from the
starting index. Otherwise, it should return False.

collection can be a string, list, or dictionary. if it's a string or array, the
third parameter is a starting index for where to search from. if the collection
is a dictionary, the function searches for the value among values in the
dictionary; since objects have no sort order, the third parameter is ignored.
'''

def includes(item, val, start=None):
  if type(item) == dict:
    return val in item.values()
  if start is None:
    return val in item
  return val in item[start:]

print(includes((thing), 3, 4))
print(includes((thing, two), 1, 4))
print(includes([1,4,5,6,7,8,4,5], 1, 5))
