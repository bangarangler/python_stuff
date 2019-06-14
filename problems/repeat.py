'''
accepts a string and a number and returns a new string with the string passed
to the function repeated the number of times. can't use built in repeat method
'''

def repeat(string, num):
  if (num == 0):
    return ''
  i = 0
  newStr = ""
  while (i < num):
    newStr += string
    i += 1
  return newStr

print(repeat("word here", 2))
print(repeat("Boy", 12))
print(repeat("girl", 5))
