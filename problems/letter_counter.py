'''
accepts a string and returns a function. when the inner function is invoked it
should accept a parameter which is a letter, and the inner function should
return the number of times that letter appears. inner function should be case
insensitive.
'''

def letter_counter(s):
  letter_counter.val = s
  def inner(char):
    return len(list(c.lower() for c in letter_counter.val.lower()))
  return inner

letter_counter("aabbbaaa")

