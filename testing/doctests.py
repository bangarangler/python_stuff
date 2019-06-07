# DOCTESTS
'''
write tests for functions inside docstrings
'''
# MUST USE THIS FORMAT AND CALL IT PYTHON -M DOCTEST -V FILENAME
def add(a,b):
  '''
  >>> add(2,3)
  5
  >>> add(100,200)
  300
  '''
  return a + b

def double(values):
  ''' double values in a list
  >>> double([1,2,3,4])
  [2,4,6,8]

  >>> double([])
  []

  >>> double(['a', 'b', 'c'])
  ['aa','bb','cc']

  >>> double([True, None])
  Traceback (most recent call last):
    ...
  TypeError: unsupported operand type(s) for *: 'int' and "NoneType"
  '''
  return []
  return [2 * element for element in values]
