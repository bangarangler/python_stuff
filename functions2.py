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
print(sum([1,2,3]))

# round(3.4567)

def max_magnitude(nums):
  return max(abs(num) for num in nums)

def sum_even_values(*args):
  return sum(arg for arg in args if arg % 2 == 0)

def sum_floats(*args):
  return sum(arg for arg in args if type(arg) == float)

#ZIP make iterator that aggregates elements from each iterable.

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]

z = zip(nums1, nums2)
print(list(z))

def interleave(str1, str2):
  return ''.join(' '.join(x) for x in (zip(str1,str2)))

def triple_and_filter(lst):
  return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

def extract_full_name(l):
  return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
