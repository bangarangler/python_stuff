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

'''
decorator is a function that wrap other functions and enhance their behavior.
have their own syntax using @ syntax suger
'''
def be_polite(fn):
  def wrapper():
    print("what a pleasure to meet you")
    fn()
    print('have a great day')
  return wrapper

@be_polite
def greet():
  print("my name is jon")

greet = be_polite(greet)
print(greet())
print(greet())
print(greet())

@be_polite
def rage():
  print('i hate you')

# polite_rage = be_polite(rage)
# print(polite_rage())

print(greet())
print(rage())
