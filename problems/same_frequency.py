'''
accepts two numbers and returns True if they contain the same frequency of
digits. otherwise, it returns False.
'''

def same_frequency(num1, num2):
  d1 = {letter:str(num1).count(letter) for letter in str(num1)}
  d2 = {letter:str(num2).count(letter) for letter in str(num2)}

  for key, val in d1.items():
    if not key in d2.keys():
      return False
    elif d2[key] != d1[key]:
      return False
  return True


print(same_frequency(2,2))
print(same_frequency(12,2))
print(same_frequency(12,25))
