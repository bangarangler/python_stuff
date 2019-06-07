# DECORATORS
'''
higher order functions
we can pass funcs as args to other funcs
'''

def sum(n, func):
  total = 0
  for num in range(n):
    total += func(num)
  return total

def square(x):
  return x*x

def cube(x):
 return x*x*x

from random import choice
def greet(person):
  def get_mood():
    msg = choice(('Hello there ', 'Go away ', 'I love you '))
    return msg
  result = get_mood() + person
  return result

print(sum(10, cube))
print(greet("Maggie"))

def make_laugh_func():
  def get_laugh():
    l = choice(('HAHAHAH', 'lol', 'tehehe'))
    return l
  return get_laugh

laugh = make_laugh_func()
print(laugh())

def make_laugh_at_func(person):
  def get_laugh():
    laugh = choice(('HAHAHAH','lol','tehehe'))
    return f"{laugh} {person}"
  return get_laugh

laugh_at = make_laugh_at_func("Linz")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
