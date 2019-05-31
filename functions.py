# FUNCTIONS
from random import random

colors = ['red','orange','yellow','green','blue','indigo']

def say_hi():
  print('HI!')

say_hi()

def sing_happy_birthday(name):
  print("Happy birthday to you")
  print("Happy birthday to you")
  print(f"Happy birthday dear {name}")
  print("Happy birthday to you")

sing_happy_birthday('Linz')

def print_square_of_seven():
  print(7**2)

def square_of_seven():
  return 7**2

def coin_flip():
  if random() > .5:
    return 'Heads'
  else:
    return 'Tails'

print(coin_flip())

def generate_evens():
  return [x for x in range(1,50) if x%2 == 0]


def square(x):
  return x**2

print(square(4))
print(square(8))

def is_odd_number(num):
  if num % 2 == 0:
    return True
  return False

def exponent(num,power=2):
  return num ** power

print(exponent(2,3))
print(exponent(3,2))
print(exponent(3))

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def math(a,b, fn=add):
  return fn(a,b)

print(math(2,3))

noises = {
  "dog": "woof",
  "pig": "oink",
  "duck": "quack",
  "cat": "meow"
}

def speak(animal="dog"):
  noises = {"dog": "woof","pig": "oink", "duck": "quack", "cat": "meow"}
  return noises.get(animal, '?')

print(speak("dog"))
print(speak("cat"))
print(speak("duck"))
print(speak("pig"))
print(speak("mouse"))

total = 0

def increment():
  #how to access global .... try to avoid this crazyness
  global total
  total += 1
  return total
print(increment())

def outer():
  count = 0
  def inner():
    nonlocal count
    count += 1
    return count
  return inner()

def return_day(num):
  try:
    return ['Sunday','Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday"][num - 1]
  except IndexError as e:
    return None

print(return_day(41))

def last_element(l):
  if l:
    return l[-1]
  return None

def number_compare(a,b):
  if a > b:
    return "First is greater"
  elif b > a:
    return "Second is greater
  return "Numbers are equal

def single_letter_count(string, letter):
  return string.lower().count(letter.lower())

def multiple_letter_count(string):
  return {letter: string.count(letter) for letter in string}

def list_manipulation(collection, command, location, value=None):
  if (command == 'remove' and location == "end"):
    return collection.pop()
  elif (command == 'remove' and location == 'beginning'):
    return collection.pop(0)
  elif (command == 'add' and location == 'beginning'):
    collection.insert(0,value)
    return collection
  elif (command == 'add' and location == 'end'):
    collection.append(value)
    return collection

  # def is_palindrome(string):
    # return string == string[::-1]

  def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

  def frequency(collection, searchTerm):
    return collection.count(searchTerm)

  def multiply_even_numbers(lst):
    total = 1
    for val in lst:
      if val % 2 == 0:
        total = total * val
    return total

  def capitalize(string):
    return string[:1].upper() + string[1:]

  def compact(l):
    return [val for val in l if val]

  def intersection(l1,l2):
    return [val for val in l1 if val in l2]

  def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not
                                              fn(val)]]


