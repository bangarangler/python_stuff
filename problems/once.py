'''
accepts a function and returns a new function that can only be invoked once. if
invoked more than once, it should return None. Hint you will need to define a
new function inside of your once function and return that function. you can add
properties to your inner function to see if it has run already
'''

def once(fn):
  fn.is_called = False
  def inner(*args):
    if not (fn.is_called):
      fn.is_called = True
      return fn(*args)
  return inner

