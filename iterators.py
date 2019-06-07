# ITERATORS -- ITERABLES
'''
iterator is an object that can be iterated upon. object which returns data one
element at a time when next() is called on it

iterable is an object which will return an iterator when iter() is called on it
'''

# CUSTOM FOR LOOP JUST FOR UNDERSTANDING
# for num in [1,2,3]
# for char in "hi there"

# iter()
# next()
# next()

def my_for(iterable, func):
  iterator = iter(iterable)
  while True:
    try:
      item = next(iterator)
    except StopIteration:
      break
    else:
      func(item)

def square(x):
  print(x*x)

my_for([1,2,3,4,5],square)
my_for("lol", print)

class Counter:
  def __init__(self,low,high):
    self.current = low
    self.high = high

  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.high:
      num = self.current
      self.current += 1
      return num
    raise StopIteration

# c = Counter(0,10)
# iter(c)

for x in Counter(50,70):
  print(x)

