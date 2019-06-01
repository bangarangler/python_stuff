#FUNCTIONS 2
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total

print(sum_all_nums(2,4,5,8,67))

def contains_purple(*args):
  if "purple" in args: return True
  return False

def fav_colors(**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s favorite color is {color}'")
fav_colors(colt='purple',ruby='red',ethel='teal')

def special_greeting(**kwargs):
  if "Matt" in kwargs and kwargs["Matt"] == "special":
    return "You get a special greeting Matt!"
  elif "Matt" in kwargs:
    return f"{kwargs['Matt']} Matt!"
  return "Not sure who this is..."

print(special_greeting(Matt="Hello"))
print(special_greeting(Linz="Hello"))
print(special_greeting(Matt="special"))

def combine_words(word, **kwargs):
  if 'prefix' in kwargs:
    return kwargs['prefix'] + word
  elif 'suffix' in kwargs:
    return word + kwargs['suffix']
  return word

def display_names(first, second):
  print(f"{first} says hello to {second}")
names = {"first": "Jon", "second": "Linz"}

display_names(**names)

def add_and_multiply_numbers(a,b,c):
  print(a + b * c)
data = dict(a=1,b=2,c=3)

add_and_multiply_numbers(**data)

#abs return absolute value of a number
import math
print(abs(-5))

#sum takes iterable and optional start returns sum plus the start
print(sum([1,2,3], 10))
