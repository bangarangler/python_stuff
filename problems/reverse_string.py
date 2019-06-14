def reverse_string(str):
  '''accepts a string and returns a new reversed string'''
  s = ''
  for i, char in enumerate(str[::-1]):
    s += char
  return s

print(reverse_string("name"))
