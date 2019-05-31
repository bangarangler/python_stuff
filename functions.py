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


